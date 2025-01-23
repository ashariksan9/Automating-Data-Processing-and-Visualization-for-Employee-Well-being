# Automating Data Processing and Visualization for Employee Well-being ✨

## Objective 🎩
Sebagai Data Analyst di perusahaan ini, saya ditugaskan untuk menganalisis bagaimana kondisi kerja (remote, hybrid, onsite) memengaruhi kesehatan mental dan produktivitas karyawan. Report ini akan menyajikan analisis visual terkait faktor-faktor seperti tingkat stres, isolasi sosial, keseimbangan kehidupan kerja, dan dukungan perusahaan. Hasil dari report ini akan memberikan wawasan kepada manajemen mengenai langkah-langkah yang dapat diambil untuk meningkatkan kesejahteraan mental karyawan, yang pada akhirnya diharapkan mampu meningkatkan produktivitas secara keseluruhan.

---

## Assignment Objectives 📚

- Mampu menggunakan **Apache Airflow** untuk mengotomasi pipeline data.
- Mampu melakukan validasi data dengan **Great Expectations**.
- Memahami konsep **NoSQL** secara keseluruhan.
- Memproses data sebelum dimasukkan ke database NoSQL.
- Mengolah dan memvisualisasikan data dengan **Kibana**.

---

## Dataset 📊
Dataset yang digunakan merupakan data employee dari suatu perusahaan yang diambil dari Kaggle dengan url berikut:

https://www.kaggle.com/datasets/waqi786/remote-work-and-mental-health/data 

---

## Problems 🔍
**Objective** dari analisis adalah menghasilkan laporan berisi **Exploratory Data Analysis (EDA)** dengan langkah berikut:

1. **Data Cleaning:**
   - Menghapus duplikasi data.
   - Normalisasi nama kolom menjadi format konsisten (lowercase, underscore).
   - Menangani nilai yang hilang (missing values).

2. **Data Validation:**
   - Menggunakan **7 Expectations** di Great Expectations.
   - Validasi mencakup “unique values”, “values in range”, dll.

3. **Data Automation:**
   - Membuat pipeline dengan Apache Airflow yang terdiri dari:
     - Fetch data dari PostgreSQL.
     - Data cleaning.
     - Load data ke Elasticsearch.

4. **Data Visualization:**
   - Membuat dashboard di Kibana dengan minimal **6 visualisasi** (Bar, Pie, Vertical Bar, dll).
   - Insight dilengkapi narasi dan rekomendasi bisnis.

---

## Methods and Tools Used 🦝

1. **Apache Airflow**
   - Automasi pipeline data untuk ETL.
2. **Great Expectations**
   - Validasi kualitas data secara komprehensif.
3. **PostgreSQL**
   - Menyimpan data mentah dan clean.
4. **Elasticsearch & Kibana**
   - Penyimpanan dan visualisasi data.
5. **Python**
   - Digunakan untuk semua proses data (ETL, cleaning, scripting).

---

## Strengths and Weaknesses 🎡

### Strengths:
- Pipeline otomatis untuk ETL meningkatkan efisiensi.
- Validasi data memastikan kualitas dataset.
- Visualisasi intuitif di Kibana membantu memahami insight dengan cepat.

### Weaknesses:
- Validasi Great Expectations memerlukan data yang cukup bersih.
- Analisis hanya terbatas pada data yang tersedia.
- Penggunaan Kibana membutuhkan akses Elasticsearch yang stabil.

---

## Conclusion and Insights 🎯
Berikut insight penting yang kita dapatkan dari analisis sebelumnya:

1. Dukungan perusahaan terhadap kerja remote berkisar pada rating rata-rata **3**. Meskipun ini menunjukkan adanya dukungan, masih terdapat ruang untuk perbaikan dalam meningkatkan kepuasan kerja remote.
2. Distribusi kondisi kesehatan mental karyawan menunjukkan bahwa **25.6%** karyawan mengalami burnout, diikuti oleh kecemasan.

### Recommendations:
- Tingkatkan program kesejahteraan mental karyawan, khususnya bagi mereka yang bekerja remote.
- Terapkan pelatihan manajemen stres dan waktu.
- Berikan insentif untuk tim hybrid untuk meningkatkan motivasi.

---

## Supporting Links 🔗
- [Great Expectations Documentation](https://greatexpectations.io/)
- [Kibana Overview](https://www.elastic.co/kibana)
- [Apache Airflow Tutorials](https://airflow.apache.org/docs/)

---

## Contact 📧
LinkedIn: www.linkedin.com/in/muhammadasharihsan  
Email: ashar4iksan@gmail.com
