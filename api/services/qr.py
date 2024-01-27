import io
import base64
import qrcode

from models import qr as qr_model


class Service():
    def generate(self, data: qr_model.QRModel):
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
        img.save(buffer)

        # Encode base 64 and decode utf-8
        return base64.b64encode(buffer.getvalue()).decode("utf-8")

qr_generator = Service()
