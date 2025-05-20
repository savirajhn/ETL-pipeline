# ETL Pipeline Sederhana

Proyek ini mengimplementasikan pipeline **ETL (Extract, Transform, Load)** menggunakan Python. Data diekstraksi dari sumber tertentu, diproses (transformasi), lalu diunggah ke Google Sheets menggunakan Google Sheets API.

## Struktur Proyek

    ETL-pipeline/
    ├── tests
    │ ├── test_extract.py
    │ ├── test_transform.py
    │ ├── test_load.py
    ├── utils
    │ ├── utils_extract.py
    │ ├── utils_transform.py
    │ ├── utils_load.py
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── google-sheets-api.json


- `tests/` : Berisi unit test untuk masing-masing fungsi ETL.
- `utils/` : Berisi modul Python untuk proses extract, transform, dan load.
- `main.py` : File utama untuk menjalankan seluruh proses ETL.
- `requirements.txt` : Daftar dependensi Python yang dibutuhkan.
- `google-sheets-api.json` : File credential untuk autentikasi dengan Google Sheets API.
- `README.md` : Dokumen ini yang berisi penjelasan lengkap tentang proyek, struktur file, cara instalasi, dan cara menjalankan kode.
  
---

## Langkah-Langkah Penggunaan

### 1. Clone Repository di Google Colab
Setelah repo tersedia, jalankan di Google Colab:

```python
!git clone https://github.com/savirajhn/ETL-pipeline /content/ETL-pipeline
%cd /content/ETL-pipeline
```
### 2. Menginstall Dependencies
```python
!pip install -r requirements.txt
```

### 3. Menjalankan Skrip Utama (main.py)
```python
!python main.py
```
### 4. Menjalankan Test Coverage
Untuk memastikan semua bagian berjalan dengan baik dan mendapatkan laporan coverage:
```python
!coverage run -m pytest tests
!coverage report
```

### Hasil Output
Hasil akhir dari proses ETL akan dikirimkan ke Google Sheets yang sudah terhubung melalui credential API. Pastikan sudah mengatur URL dan ID Sheet dengan benar di dalam kode. Data bisa dilihat pada link ini :
[Google Sheet](https://docs.google.com/spreadsheets/d/1S4S_eH_7HNQ-Su2evTFauJYBA1KnZoSgL6Ii_yqPym8/edit?gid=0#gid=0)
