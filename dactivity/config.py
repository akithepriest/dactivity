import tomllib as toml
from typing import Self

def read_config_file(filename: str = "config.toml") -> dict:
    with open(filename, "rb") as file:
        data = toml.load(file)
        return data

def validate(data: dict):
    match data:
        case {
            "client": {"client_id": str()},
            "activity": {"state": str(), "details": str(), "time_start": int()},
            "activity-assets": {"large_image": str(), "large_text": str(), "small_image": str(), "small_text": str()},
        }:
            pass
        case _:
            raise ValueError(f"Missing or invalid configuration values, check example.config.toml")

class Config:
    def __init__(
        self,
        client_id: str,
        state: str,
        details: str,
        time_start: int,
        time_end:int,
        large_image: str,
        large_text: str,
        small_image: str, 
        small_text: str,
    ):
        self.CLIENT_ID = client_id
        self.STATE = state
        self.DETAILS = details
        self.TIMESTAMPS_START = time_start
        self.TIMESTAMPS_END = time_end
        self.LARGE_IMAGE = large_image
        self.LARGE_TEXT = large_text
        self.SMALL_IMAGE = small_image
        self.SMALL_TEXT = small_text
        
    @classmethod
    def load(cls, config_filename: str = "config.toml") -> Self:
        data = read_config_file(config_filename)
        validate(data)

        client_id = data["client"]["client_id"]
        activity = data["activity"]
        assets = data["activity-assets"]

        return cls(
            client_id=client_id,
            state=activity["state"],
            details=activity["details"],
            time_start=activity["time_start"],
            time_end=activity["time_end"],
            large_image=assets["large_image"],
            large_text=assets["large_text"],
            small_image=assets["small_image"],
            small_text=assets["small_text"],
        )
