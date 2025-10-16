import os
import allure
import requests
import pytest
import json
from utils.screenshot_helper import capture_screenshot

@allure.feature("PUT Post")
def test_update_post():
    """Tes PUT (update) postingan."""
    try:
        if os.getenv("TEST_PUT_PASS") == "0":
            raise AssertionError("💥 Simulasi gagal PUT")

        payload = {
            "id": 55,
            "title": "VAJURA ON!~ YOU GOT THE THUNDER!!",
            "body": "Agha update data dengan semangat ⚡",
            "userId": 1
        }

        response = requests.put("https://jsonplaceholder.typicode.com/posts/55", json=payload)
        assert response.status_code == 200
        data = response.json()

        assert data["title"] == payload["title"]
        print("✅ PUT berhasil update:", json.dumps(data, indent=4))

    except AssertionError as e:
          # ⬇️ Ambil screenshot dan kirim ke Allure
        screenshot_path = capture_screenshot("PUT_FAIL")
        allure.attach.file(
            screenshot_path,
            name="Screenshot saat gagal PUT",
            attachment_type=allure.attachment_type.PNG
        )
        raise e
