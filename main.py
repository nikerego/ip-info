from os import getenv
from fastapi import FastAPI
import logging
from logging.config import dictConfig
from utils.data_contracts import OutputRequest, InputRequest
from utils.log_config_file import log_config
from utils.ip_functions import (
    get_ip_address,
    get_ip_stack_data,
)
import uvicorn

ip_stack_api_key = getenv('IP_STACK_API_KEY')
version = getenv('VERSION')
dictConfig(log_config)

app = FastAPI(
    title='IP Information API',
    version=version,
)

logging.info("Initialized IP Information API...")


@app.get("/health_check")
async def health_check():
    return {"status_code": 200}


@app.post("/ip_info")
async def get_ip_info(request: InputRequest):
    ip_address = get_ip_address(request.url)
    ip_data = get_ip_stack_data(
        domain=request.url,
        ip_address=ip_address,
        ip_stack_api_key=ip_stack_api_key,
    )
    return OutputRequest.model_validate(ip_data)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)

