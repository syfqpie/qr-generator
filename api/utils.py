from fastapi.encoders import jsonable_encoder
from models import core


def generate_content(code: str, data: object, error=False) -> core.ResponseContentSchema:
    """Generate content for response

    Args:
        code (str): response code
        data (object): response data
        error (bool, optional): if this is error response. defaults to False.

    Returns:
        ResponseContentSchema: response content
    """
    if error:
        kwargs = dict(data=None, errors=data)
    else:
        kwargs = dict(data=data, errors=None)

    return jsonable_encoder(dict(code=code, **kwargs))
