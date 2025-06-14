import logging
import logging.config
import os
import sys

from fastapi import Request
from fastapi.responses import JSONResponse

CWD = os.getcwd()
LOG_DIR = os.path.join(CWD, "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")
os.makedirs(LOG_DIR, exist_ok=True)


def setup_logging():
    log_file = os.path.join(os.getcwd(), LOG_FILE)
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s %(levelname)s %(name)s %(lineno)d %(funcName)s %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": log_file,
                "formatter": "default",
                "mode": "a",
                "encoding": "utf-8",
            },
        },
        "root": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
    }
    logging.config.dictConfig(logging_config)


def add_logging_middleware(app):
    import logging

    logger = logging.getLogger("uvicorn.access")

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        try:
            response = await call_next(request)
        except Exception as exc:
            logger.exception(f"Error handling request: {exc}")
            return JSONResponse(
                status_code=500, content={"detail": "Internal Server Error"}
            )
        logger.info(f"Response status: {response.status_code}")
        return response
