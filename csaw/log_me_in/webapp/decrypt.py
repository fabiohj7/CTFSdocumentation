import json
import os
import re

from Crypto.Util.Padding import pad, unpad


def is_alphanumeric(text):
    pattern = r'^[a-zA-Z0-9]+$'
    if re.match(pattern, text):
        return True
    else:
        return False


def LOG(*args, **kwargs):
    print(*args, **kwargs, flush=True)


# Some cryptographic utilities
def encode(status: dict) -> str:
    try:
        plaintext = json.dumps(status).encode()
        print("Plaintext: ", plaintext)
        out = b''
        for i, j in zip(plaintext, os.environ['ENCRYPT_KEY'].encode()):
            out += bytes([i ^ j])
            print("Encode: ", out)
        return bytes.hex(out)
    except Exception as s:
        LOG(s)
        return None


def decode(inp: str) -> dict:
    try:
        token = bytes.fromhex(inp)
        print("Token: ", token)
        out = ''
        for i, j in zip(token, os.environ['ENCRYPT_KEY'].encode()):
            out += chr(i ^ j)
            print("Decode: ", out)
        user = json.loads(out)
        return user
    except Exception as s:
        LOG(s)
        return None


def main():
    x = input()
    # s = decode(x)
    encode(x)


if __name__ == '__main__':
    main()
