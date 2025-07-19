from pwn import *

p = process(["./zeus", "-invocation", "To Zeus Maimaktes, Zeus who comes when the north wind blows, we offer our praise, we make you welcome!"])

p.interactive()