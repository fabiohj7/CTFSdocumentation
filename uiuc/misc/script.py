from hashlib import sha256
from time import time


def find_lucky_number(length):
    hex_alpha = "0123456789abcdef"
    last = time()
    lastcount = 0

    for i in range(0, int("f" * 32, 16)):
        lucky_number = f"{i:x}".zfill(64)
        hash = sha256(bytes.fromhex(lucky_number)[::-1]).digest()[::-1].hex()

        if len(set(hash[:length])) == 1:
            return lucky_number, hash[:length]

        if time() - last > 1:
            print(i - lastcount, flush=True)
            last = time()
            lastcount = i
    return None, None


# Change the length to the desired number of slots
length = 10
lucky_number, matching_hash = find_lucky_number(length)

if lucky_number:
    print(f"Lucky Number: {lucky_number}")
    print(f"Matching Hash: {matching_hash}")
else:
    print("No suitable lucky number found.")
