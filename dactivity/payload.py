import os
import time
from uuid import uuid4
from dactivity.config import Config

"""
Create a new activity payload
"""
def activity_payload(config: Config) -> dict:
    # Determine timestamps
    timestamps = {
        "start": int(time.time()) if config.TIMESTAMPS_START == 0 else config.TIMESTAMPS_START
    }

    if config.TIMESTAMPS_END != 0:
        timestamps["end"] = config.TIMESTAMPS_END

    payload = {
        "cmd": "SET_ACTIVITY",
        "args": {
            "pid": os.getpid(),
            "activity": {
                "application_id": config.CLIENT_ID,
                "state": config.STATE,
                "details": config.DETAILS,
                "timestamps": timestamps,
                "assets": {
                    "large_image": config.LARGE_IMAGE,
                    "large_text": config.LARGE_TEXT,

                    "small_image": config.SMALL_IMAGE,
                    "small_text": config.SMALL_TEXT,
                }
            }
        },
        "nonce": str(uuid4())
    }

    return payload
