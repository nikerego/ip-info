import pytest
from os import getenv
from fastapi import HTTPException
from fastapi.testclient import TestClient
from utils.ip_functions import get_ip_address, get_ip_stack_data
from utils.data_contracts import OutputRequest
from main import app

ip_stack_api_key = getenv('IP_STACK_API_KEY')

# IP Address:
pass_domains = ["google.com", "github.com", "amazon.com"]

# Pydantic validation will only allow: .com, .org, .net, .edu
fail_domains = ["www.michigan.gov"]


@pytest.mark.parametrize("domain", pass_domains)
def get_ip_address_pass(domain):
    ip_address = get_ip_address(domain)
    assert isinstance(ip_address, str)


@pytest.mark.parametrize("domain", fail_domains)
def test_get_ip_stack_realtime(domain):
    client = TestClient(app)
    input_json = {"url": domain}
    with pytest.raises(ValueError):
        client.post("/ip_info", json=input_json)


@pytest.mark.parametrize("domain", pass_domains)
def test_get_ip_stack_data_pass(domain):
    ip_address = get_ip_address(domain)
    ip_info = get_ip_stack_data(
        domain=domain,
        ip_address=ip_address,
        ip_stack_api_key=ip_stack_api_key,
    )
    output = OutputRequest.model_validate(ip_info)
    assert isinstance(output, OutputRequest)


@pytest.mark.parametrize("domain", pass_domains)
def test_get_ip_stack_data_fail(domain):
    ip_address = get_ip_address(domain)
    with pytest.raises(HTTPException):
        get_ip_stack_data(
            domain=domain,
            ip_address=ip_address,
            ip_stack_api_key=None,
        )


@pytest.mark.parametrize("domain", pass_domains)
def test_get_ip_stack_realtime(domain):
    client = TestClient(app)
    input_json = {"url": domain}
    output = client.post("/ip_info", json=input_json)
    assert output.status_code == 200
