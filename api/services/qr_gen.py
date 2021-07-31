import io
import base64
import qrcode

from pydantic.main import BaseModel

class QRModel(BaseModel):
    link: str

class Service():
    def generate(self, data: QRModel):
        # Configure
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Generate
        qr.add_data(data.link)
        qr.make(fit=True)
        buffer = io.BytesIO()
        img = qr.make_image(fill_color="black", back_color="white")

        # Saving
        img.save(buffer, format="png")
        # Encode base 64 and decode utf-8
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return img_base64

qr_generator = Service()