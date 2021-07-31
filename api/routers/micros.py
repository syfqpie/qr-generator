import services

from fastapi.routing import APIRouter
from fastapi import APIRouter, HTTPException

from services.qr_gen import QRModel

router = APIRouter()

@router.post("/generate_qr", summary="Generate QR", description="Generate QR Code")
def generate_qr(item: QRModel):
    try:
        result = services.qr_generator.generate(item)
        return "data:image/jpeg;base64," + str(result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))