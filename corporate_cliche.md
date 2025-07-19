Given email_server and email_server.c

Scanning through the source file, username needs to be admin while password is 🇦🇩🇲🇮🇳, but it can't be that easy and has to be done through buffer overflow. Into gdb I go to try out the executable and find the offset for buffer overflow. Luckily, the program gives the inputted username which means I didn't have to go into gdb at all. 

The payload will be `"🇦🇩🇲🇮🇳" + offset * '\x00' + "admin"`, since '🇦🇩🇲🇮🇳' is the password and 'admin' is the username. At first, I thought the offset would be 32 - 5 = 27, but after some trying using `pwn cyclic 32` and `pwn cyclic <username from failed access>`, it is 12. 🇦🇩🇲🇮🇳 is not ASCII, it is UTF-8 and takes up 20 bytes. How I checked it:

```
echo 🇦🇩🇲🇮🇳 > test.txt
file test.txt
ls -alu
```

So create a simple pwn program `pwned.py` to get in.