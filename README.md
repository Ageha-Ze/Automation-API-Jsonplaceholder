# 🧪 Automation API Testing - Jsonplaceholder

Project ini merupakan **automation testing API** menggunakan **Pytest** dan **Allure Report**.  
Contoh API yang diuji: [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)

---

## ⚙️ Struktur Folder
```
📦 API SERIES
├── tests/                # Folder untuk test cases
│   ├── test_users.py     # Contoh pengujian endpoint /users
│   └── test_posts.py     # Contoh pengujian endpoint /posts
├── utils/                # Helper functions (misal: capture_screenshot, api utils)
├── run_series.py         # Script untuk menjalankan semua test
├── pytest.ini            # Konfigurasi Pytest
├── .env                  # Menyimpan environment variable (misal base_url, token)
└── README.md             # Dokumentasi proyek
```

---

## 🚀 Cara Menjalankan Test

### 1️⃣ Install dependencies
Pastikan sudah menginstall Python 3.9+  
Kemudian jalankan:
```bash
pip install -r requirements.txt
```

### 2️⃣ Jalankan semua test
```bash
pytest -v
```

### 3️⃣ Jalankan dan simpan hasil untuk Allure
```bash
pytest --alluredir=reports/allure-results
```

### 4️⃣ Tampilkan laporan Allure
```bash
allure serve reports/allure-results
```

---

## 📸 Screenshot Otomatis
File `utils/capture_screenshot.py` akan otomatis mengambil screenshot saat test gagal.  
Screenshot tersimpan di folder:
```
screenshots/
```

---

## 🧰 Tools yang digunakan
- **Python 3.9+**
- **Pytest**
- **Allure Pytest**
- **Requests**
- **Mss** (untuk screenshot)

---

## 💡 Catatan
- Pastikan Git sudah diinstall sebelum melakukan push ke repository.
- Untuk inisialisasi project ke GitHub:
  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  git branch -M main
  git remote add origin https://github.com/Ageha-Ze/Automation-API-Jsonplaceholder.git
  git push -u origin main
  ```

---

🧤 Dibuat oleh **Ageha-Ze**  
Untuk pembelajaran dan implementasi automation API testing.
