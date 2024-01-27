from fastapi.routing import APIRouter
from fastapi import APIRouter, HTTPException

import services
from models import qr as qr_model
from utils import generate_content

router = APIRouter()


@router.post("/generate-qr", summary="Generate QR", description="Generate QR Code")
def generate_qr(item: qr_model.QRModel):
    try:
        result = services.qr_generator.generate(item)
        data = "data:image/jpeg;base64," + str(result)
        return generate_content(code="ok", data=dict(result=data))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

