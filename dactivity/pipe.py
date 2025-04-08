import win32file, win32pipe 
import json
import struct

def create_pipe():
    pipe_name = r'\\?\pipe\discord-ipc-0'
    pipe = win32file.CreateFile(
        pipe_name,
        win32file.GENERIC_READ | win32file.GENERIC_WRITE,
        0,
        None,
        win32file.OPEN_EXISTING,
        0,
        None, 
    )

    return pipe 

def send(pipe, opcode: int, payload):
    payload_bytes = json.dumps(payload).encode('utf-8') 
    header = struct.pack("<II", opcode, len(payload_bytes))

    win32file.WriteFile(pipe, header + payload_bytes)

def read(pipe):
    resp = win32file.ReadFile(pipe, 8)
    opcode, length = struct.unpack("<II", resp[1])

    data = win32file.ReadFile(pipe, length)[1]
    return opcode, json.loads(data)