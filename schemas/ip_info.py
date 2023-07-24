from pydantic import IPvAnyAddress, BaseModel


class ResponseIpInfo(BaseModel):
    ip: IPvAnyAddress
    hostname: str
    city: str
    country: str
    loc: str
    latitude: float = None
    longitude: float = None
    org: str
    postal: str
    timezone: str

    def parse_loc_to_longitude_and_latitude(self) -> None:
        self.latitude, self.longitude = map(lambda x: float(x), self.loc.split(','))
