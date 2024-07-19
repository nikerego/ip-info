from pydantic import BaseModel, field_validator
from typing import Optional


class InputRequest(BaseModel):
    url: str

    @field_validator('url')
    def validate_x(v: str) -> str:
        allowed_extensions = ('.com', '.org', '.net', '.edu')
        if not any(v.endswith(ext) for ext in allowed_extensions):
            raise ValueError('URL must end with one of the following extensions: .com, .org, .net, .edu')
        return v


class LanguageModel(BaseModel):
    code: str
    name: str
    native: str


class LocationModel(BaseModel):
    geoname_id: int
    capital: str
    languages: list[LanguageModel]
    country_flag: str
    country_flag_emoji: str
    country_flag_emoji_unicode: str
    calling_code: str
    is_eu: bool


class TimeZoneModel(BaseModel):
    id: str
    current_time: str
    gmt_offset: int
    code: str
    is_daylight_saving: bool


class CurrencyModel(BaseModel):
    code: str
    name: str
    plural: str
    symbol: str
    symbol_native: str


class ConnectionModel(BaseModel):
    asn: int
    isp: str


class SecurityModel(BaseModel):
    is_proxy: bool
    proxy_type: str
    is_crawler: bool
    crawler_name: str
    crawler_type: str
    is_tor: bool
    threat_level: str
    threat_types: str


class OutputRequest(BaseModel):
    url: str
    ip: str
    type: str
    continent_code: Optional[str] = None
    continent_name: Optional[str] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    region_code: Optional[str] = None
    region_name: Optional[str] = None
    city: Optional[str] = None
    zip: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    location: Optional[LocationModel] = None
    time_zone: Optional[TimeZoneModel] = None
    currency: Optional[CurrencyModel] = None
    connection: Optional[ConnectionModel] = None
    security: Optional[SecurityModel] = None



