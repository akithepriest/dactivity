from dactivity.pipe import create_pipe, send, read
import os 
from dactivity.config import Config
from dactivity.payload import activity_payload

config = Config.load()

handshake = {
    "v": 1,
    "client_id": config.CLIENT_ID
}

def start_activity(pipe) -> None:
    payload = activity_payload(config)

    send(pipe, 1, payload)
    _, res = read(pipe)

    print("Activity Payload: ", res)

def main() -> int:
    print("Connecting to Discord IPC")
    pipe = create_pipe()

    send(pipe, 0, handshake)
    opcode, _ = read(pipe)

    if opcode == 1:
        print("Handshake successful")
    else:
        print("Handshake failed")
    
    try:
        start_activity(pipe)
    except:
        pass 

    while True:
        pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.abort()