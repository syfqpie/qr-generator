class ResponseContentSchema:
    """ Response content schema

    Ok content:
        {
            "code": {
                "data": ...,
                "errors": null
            }
        }
    
    Error content:
        {
            "code": {
                "data": null,
                "errors": ...
            }
        }
    """
    code: str
    data: object | None
    errors: object | list | None
