from os import getenv

loglevel = getenv("LOGLEVEL", "INFO").upper()

log_config = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        },
        "handlers": {
            "error_stream": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file_handler": {
                "formatter": "default",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "IP-Info.log",
                "mode": "a",
                "maxBytes": 1048576,
                "backupCount": 10,
            },
        },
        "loggers": {
            "gunicorn": {"access": {"propagate": True}, "error": {"propagate": True}},
            "uvicorn": {"access": {"propagate": True}, "error": {"propagate": True}},
        },
        "root": {
            "level": loglevel,
            "handlers": ["error_stream", "file_handler"],
        },
    },
}
