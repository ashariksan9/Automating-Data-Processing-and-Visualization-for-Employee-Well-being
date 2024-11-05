import pandas as pd
import psycopg2 as db
from io import StringIO


def create_table_postgre():

    conn_string = "dbname='postgres' host='localhost' user='airflow' password='airflow' port='5434'"
    conn = db.connect(conn_string)
    cur = conn.cursor()

    # Membuat tabel jika belum ada
    # sql = '''
    #     CREATE TABLE IF NOT EXISTS table_m3 (
    #             employee_id VARCHAR,
    #             age INT,
    #             gender VARCHAR,
    #             job_role VARCHAR,
    #             industry VARCHAR,
    #             years_of_experience INT,
    #             work_location VARCHAR,
    #             hours_worked_per_week INT,
    #             number_of_virtual_meetings INT,
    #             work_life_balance_rating INT,
    #             stress_level VARCHAR,
    #             mental_health_condition VARCHAR,
    #             access_to_mental_health_resources VARCHAR,
    #             productivity_change VARCHAR,
    #             social_isolation_rating INT,
    #             satisfaction_with_remote_work VARCHAR,
    #             company_support_for_remote_work INT,
    #             physical_activity VARCHAR,
    #             sleep_quality VARCHAR,
    #             region VARCHAR
    #         );
    # '''
    # cur.execute(sql)
    # conn.commit()

    # Baca file CSV menggunakan pandas
    df = pd.read_csv('P2M3_ashar_ihsan_data_raw.csv')

    print(df)
    
    # Buat StringIO buffer untuk mempersiapkan data sebelum di-copy ke PostgreSQL
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False)  # Convert DataFrame ke CSV format, tanpa index dan header
    buffer.seek(0)

    # Menggunakan COPY untuk mengimpor semua data
    cur.copy_expert("""
        COPY table_m3 ("employee_id", "age", "gender", "job_role", "industry", "years_of_experience", 
                       "work_location", "hours_worked_per_week", "number_of_virtual_meetings", "work_life_balance_rating", 
                       "stress_level", "mental_health_condition", "access_to_mental_health_resources", "productivity_change", 
                       "social_isolation_rating", "satisfaction_with_remote_work", "company_support_for_remote_work", "physical_activity",
                        "sleep_quality", "region") 
        FROM STDIN WITH CSV;
    """, buffer)

    # Commit and close the connection
    conn.commit()
    cur.close()
    conn.close()

create_table_postgre()