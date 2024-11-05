'''
====================================================================
Milestone 3

Nama  : Muhammad Ashar Ihsan
Batch : FTDS-035-RMT

Program ini dibuat untuk melakukan automatisasi fetch data raw dari PostgreSQL dan melakukan data cleaning 
seperti hapus duplikat dan normalisasi yang hasilnya akan disimpan di file csv yang diberi nama clean.
Setelah tersimpannya data clean tadi function ke 2 membuat datanya terkirim kepada elasticsearch yang mana
akan kita visualisasikan disana.

Adapun dataset yang digunakan merupakan data employee dari suatu perusahaan yang akan kita gunakan untuk menganalisis
bagaimana kondisi kerja (remote, hybrid, onsite) dapat memengaruhi kesehatan mental dan produktivitas karyawan.
=================================================

'''

import pandas as pd
import psycopg2 as db
import datetime as dt
from datetime import timedelta
from elasticsearch import Elasticsearch

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def fetch_and_clean_data():
    conn_string = "dbname='postgres' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)
    query = "SELECT * FROM table_m3;"
    
    # Ambil data dari PostgreSQL
    df = pd.read_sql(query, conn)
    conn.close()

    # Hapus data duplikat
    df = df.drop_duplicates()

    # Normalisasi nama kolom
    df.columns = df.columns.str.strip()  # Menghapus spasi/tab di awal/akhir nama kolom
    df.columns = df.columns.str.lower()  # Mengubah semua menjadi lowercase
    df.columns = df.columns.str.replace(' ', '_')  # Mengganti spasi dengan underscore
    df.columns = df.columns.str.replace(r'\W', '', regex=True)  # Menghapus simbol yang tidak diperlukan

    # Handling missing values
    for column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            df[column].fillna(df[column].median(), inplace=True)
        else:
            df[column].fillna('Unknown', inplace=True)

    # Simpan data yang sudah dibersihkan ke file CSV clean
    df.to_csv('/opt/airflow/dags/P2M3_ashar_ihsan_data_clean.csv', index=False)


def post_to_elasticsearch():
    # Koneksi ke Elasticsearch
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

    # Memastikan koneksi Elasticsearch dengan ping()
    if not es.ping():
        print("Tidak dapat terhubung ke Elasticsearch")
        return
    else:
        print("Terhubung ke Elasticsearch")

    # Membaca data dari CSV yang telah dibersihkan
    df_clean = pd.read_csv('/opt/airflow/dags/P2M3_ashar_ihsan_data_clean.csv')

    # Looping untuk memasukkan data ke Elasticsearch per row
    for i, row in df_clean.iterrows():
        doc = row.to_dict()  # Konversi setiap row menjadi dictionary
        es.index(index="data_karyawan", id=i, body=doc)

    print("Data successfully posted to Elasticsearch")


#_______________________DAG_________________________#

# Pengaturan DAG
default_args = {
    'owner': 'iksan',
    'start_date': dt.datetime(2024, 10, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG('DAGS',
         default_args=default_args,
         schedule_interval= "30 6 * * *", # interval tiap jam 6.30
         catchup=False
         ) as dag:

    print_starting = BashOperator(task_id='starting',
                                  bash_command='echo "I am reading the CSV now....."')
    
    fetch_clean = PythonOperator(task_id='fetch_n_clean', 
                                 python_callable=fetch_and_clean_data)
    
    post_to_es_task = PythonOperator(task_id='post_to_elasticsearch',
                                     python_callable=post_to_elasticsearch,
                                     dag=dag
                                     )

print_starting >> fetch_clean >> post_to_es_task
