from pydantic.main import BaseModel


class QRModel(BaseModel):
    link: str
