import requests
from fastapi import HTTPException
import logging
from nslookup import Nslookup


def get_ip_address(
        domain: str,
) -> str:
    dns_query = Nslookup()
    ip_address = dns_query.dns_lookup_all(domain).answer[0]
    return ip_address


def get_ip_stack_data(
        domain: str,
        ip_address: str,
        ip_stack_api_key,
) -> dict:

    url = f"http://api.ipstack.com/{ip_address}?access_key={ip_stack_api_key}&output=json"
    response = requests.get(url)
    response_json = response.json()
    output = {
        "url": domain,
        **response_json,
    }

    if (response.status_code != 200) or (not response_json.get('ip')):
        logging.error(f"Error fetching data from ipstack API for {ip_address}")
        raise HTTPException(status_code=500, detail="Error fetching data from ipstack API")

    return output


if __name__ == "__main__":
    pass
