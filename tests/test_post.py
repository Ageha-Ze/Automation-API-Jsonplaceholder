import os
import allure
import requests
import pytest
import json
from utils.screenshot_helper import capture_screenshot

def test_create_post():
    """Tes POST postingan."""
    try:
        if os.getenv("TEST_POST_PASS") == "0":
            raise AssertionError("💥 Simulasi gagal POST")

        payload = {
            "title": "VAJURA ON!~ YOU GOT THE THUNDER!!",
            "body": "Post test dari Ageha",
            "userId": 1
        }

        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
        assert response.status_code == 201
        print("✅ POST berhasil:", json.dumps(response.json(), indent=4))

    except AssertionError as e:
         # ⬇️ Ambil screenshot dan kirim ke Allure
        screenshot_path = capture_screenshot("POST_FAIL")
        allure.attach.file(
            screenshot_path,
            name="Screenshot saat gagal POST",
            attachment_type=allure.attachment_type.PNG
        )        
        raise e
