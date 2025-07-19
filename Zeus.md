Given zeus which is an ELF, and the challenge is a reverse engineering challenge. 
Using Ghidra, it is looking for some conditions:

```
if (((argc == 3) && (iVar1 = FUN_00101050(*(undefined8 *)(argv + 8),"-invocation"), iVar1 == 0))
    && (iVar1 = FUN_00101050(*(undefined8 *)(argv + 0x10),pcStack_10), iVar1 == 0))
```
This means binary takes 2 command line arguments since argc = 3, the rest I have no idea. Thankfully, chatGPT to the rescue and takes an educated guess that FUN_00101050 is function similiar to strcmp(), so we just need to put -invocation as first arg, and content of pcstack_10 as second arg

```
pcstack_10 = "To Zeus Maimaktes, Zeus who comes when the north wind blows, we offer our praise, we make you welcome!"
```

So, a simple python pwn script later:
```
from pwn import *

p = process(["./zeus", "-invocation", "To Zeus Maimaktes, Zeus who comes when the north wind blows, we offer our praise, we make you welcome!"])

p.interactive()
```