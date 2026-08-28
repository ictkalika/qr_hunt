import os
from pathlib import Path

import qrcode

BASE_DIR = Path(__file__).resolve().parent.parent

QR_DIR = BASE_DIR / "qr_codes"


def generate_qr_code(hex_code, filename):

    hex_code = hex_code.strip()

    os.makedirs(QR_DIR, exist_ok=True)

    if not filename.lower().endswith(".png"):
        filename += ".png"

    output_path = os.path.join(QR_DIR, filename)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(hex_code)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white",
    )

    img.save(output_path)

    return output_path


if __name__ == "__main__":
    generate_qr_code("B91E47", "qr_code.png")
