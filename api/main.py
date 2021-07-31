from fastapi import FastAPI
from configs import config, routes

from fastapi.middleware.cors import CORSMiddleware
settings = config.settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    openapi_tags=settings.TAGS_METADATA
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# You can change this prefix, but beware of the nginx.conf
app.include_router(routes.router, prefix="/api")