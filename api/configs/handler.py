from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import utils


def validation_exception_handler(request, exc: RequestValidationError):
    def _get_messages():
        formatted = []
        for error in exc.errors():
            if (
                error.get("type") and error.get("loc") and
                len(error.get("loc")) > 1
            ):
                msg = dict(field=error.get("loc")[1], type=error.get("type"))
                formatted.append(msg)
        
        return formatted

    messages = _get_messages()
    content = utils.generate_content("validation_error", messages, error=True)
    return JSONResponse(content=content, status_code=400)
