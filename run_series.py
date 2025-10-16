import os
import random
import subprocess
import time

# ✅ Pastikan Python pakai UTF-8 biar emoji aman
os.environ["PYTHONUTF8"] = "1"

# 🔧 Daftar environment variable test
TEST_ENV_VARS = ["TEST_GET_PASS", "TEST_POST_PASS", "TEST_PUT_PASS", "TEST_DELETE_PASS"]

# 📂 Folder utama penyimpanan report
REPORTS_BASE = "reports"

# 🔁 Banyaknya batch run
TOTAL_RUNS = 4

# 📄 File rekap hasil
SUMMARY_FILE = os.path.join(REPORTS_BASE, "summary.txt")


def run_tests_with_env(run_number: int):
    """Jalankan 1 batch test dengan kombinasi acak PASS/FAIL."""
    print(f"\n🚀 Menjalankan Batch ke-{run_number} ...")

    # 🎲 Set PASS/FAIL acak untuk setiap test
    env_settings = {var: str(random.choice([0, 1])) for var in TEST_ENV_VARS}

    # 📁 Buat folder laporan per batch
    report_dir = os.path.join(REPORTS_BASE, f"run_{run_number}")
    os.makedirs(report_dir, exist_ok=True)

    # 🧩 Gabungkan env var
    env = os.environ.copy()
    env.update(env_settings)

    # 🧾 Cetak status konfigurasi
    print("🔧 KONFIGURASI ENV:")
    for k, v in env_settings.items():
        print(f"  {k} = {'PASS' if v == '1' else 'FAIL'}")

    # ▶️ Jalankan pytest + allure
    cmd = f"pytest tests --alluredir={report_dir}"
    result = subprocess.run(cmd, shell=True, env=env, capture_output=True, text=True, encoding="utf-8", errors="ignore")

    # 📊 Hitung hasil dari output pytest
    output = result.stdout
    passed = output.count("PASSED")
    failed = output.count("FAILED")

    # 📝 Simpan hasil ke summary.txt
    with open(SUMMARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"=== Batch {run_number} ===\n")
        for k, v in env_settings.items():
            f.write(f"{k}: {'PASS' if v == '1' else 'FAIL'}\n")
        f.write(f"Hasil Run: {passed} Passed, {failed} Failed\n\n")

    # 📋 Print ringkasan hasil di terminal
    print(f"\n📊 Hasil Batch {run_number}: {passed} Passed, {failed} Failed\n")

    # 🕐 Delay antar batch
    time.sleep(1)


def open_allure_report():
    """Buka Allure report terakhir di browser."""
    last_report = os.path.join(REPORTS_BASE, f"run_{TOTAL_RUNS}")
    print(f"\n📈 Membuka Allure report terakhir: {last_report}")
    try:
        subprocess.run(f"allure serve \"{last_report}\"", shell=True)
    except FileNotFoundError:
        print("⚠️ Allure CLI belum terinstall. Jalankan perintah berikut:")
        print("   npm install -g allure-commandline")
    except Exception as e:
        print(f"❌ Gagal membuka Allure: {e}")


if __name__ == "__main__":
    print("⚡ Memulai 4x run otomatis dengan kombinasi PASS/FAIL acak...\n")

    # 🧹 Kosongkan summary lama
    os.makedirs(REPORTS_BASE, exist_ok=True)
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write("📜 Rekap Hasil Otomatis - Allure Pytest Runs\n\n")

    # 🔁 Jalankan batch secara berurutan
    for i in range(1, TOTAL_RUNS + 1):
        run_tests_with_env(i)

    print("🎯 Semua batch selesai dijalankan!")
    print(f"📄 Lihat rekap hasil di: {SUMMARY_FILE}")

    # 🌐 Buka laporan Allure terakhir
    open_allure_report()
