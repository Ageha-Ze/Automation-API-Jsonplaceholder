import os
import allure
import requests
import pytest
from utils.screenshot_helper import capture_screenshot

def test_get_post():
    """Tes GET postingan."""
    try:
        if os.getenv("TEST_GET_PASS") == "0":
            raise AssertionError("💥 Simulasi gagal GET")

        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status_code == 200
        print("✅ GET berhasil:", response.status_code)

    except AssertionError as e:
     # ⬇️ Ambil screenshot dan kirim ke Allure
        screenshot_path = capture_screenshot("GET_FAIL")
        allure.attach.file(
            screenshot_path,
            name="Screenshot saat gagal GET",
            attachment_type=allure.attachment_type.PNG
        )        
        raise e
