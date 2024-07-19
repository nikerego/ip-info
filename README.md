# Local Time API

### Description:

This is an example [Fast API](https://fastapi.tiangolo.com/) which provides IP address information on a URL 
provided by the user. IP information is collected with the help of [nslookup](https://pypi.org/project/nslookup/) and 
https://ipstack.com/.



### Setup:
You will need to create a `.env` and include the environment variables shown below. To acquire your `IP_STACK_API_KEY` 
please refer to https://ipstack.com/


```bash
IP_STACK_API_KEY=
LOGLEVEL=
VERSION=
```

### API Running & Testing:

You can run the API locally or within docker.

_Note: For all unit tests to pass you need to have the API live._ 

**Local:**

1. Serving: `python main.py`
2. Testing: `pytest`

**Docker:**

`docker compose up --build`

OR 

1. `docker compose up serve --build`
2. `docker compose up test --build`


### Endpoints:

#### 1. `GET /health_check`
```bash
curl --location --request GET 'http://127.0.0.1:8080/health_check'
```
 

#### 2. `POST /ip_info `

```bash
curl --location 'http://127.0.0.1:8080/ip_info' \
--header 'Content-Type: application/json' \
--data '{"url":"www.google.com"}'
```
