import io
import os
from pathlib import Path

import qrcode

BASE_DIR = Path(__file__).resolve().parent.parent


def generate_qr(hex_code):

    hex_code = hex_code.strip()

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

    buffer = io.BytesIO()

    img.save(buffer, format="PNG")

    buffer.seek(0)

    return buffer


if __name__ == "__main__":
    generate_qr_code("B91E47", "qr_code.png")
