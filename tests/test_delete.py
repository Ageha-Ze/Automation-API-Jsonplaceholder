import os
import requests
import pytest
from utils.screenshot_helper import capture_screenshot

def test_delete_post():
    """Tes DELETE postingan."""
    try:
        if os.getenv("TEST_DELETE_PASS") == "0":
            raise AssertionError("💥 Simulasi gagal DELETE")

        response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status_code == 200
        print("✅ DELETE berhasil:", response.status_code)

    except AssertionError as e:
        capture_screenshot("DELETE_FAIL")
        raise e
