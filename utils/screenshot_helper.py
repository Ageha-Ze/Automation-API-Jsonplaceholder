import os
from datetime import datetime
import mss

def capture_screenshot(name="screenshot"):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    try:
        with mss.mss() as sct:
            sct.shot(output=filepath)
        print(f"Screenshot tersimpan: {filepath}")
        return filepath
    except Exception as e:
        print(f"Gagal mengambil screenshot: {e}")
        return None
