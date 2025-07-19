Given challenge.py and output.txt

From a brief look, this should be a simple xor encryption stack using the fact that xor is reversible

Let's assume that `len(flag) = x`, initial steps of `main()` makes `len(flag) = x + 6x = 7x`, with the flag in the first x letters

Now, from output.txt, the first hex corresponding to `flag[::1]` (which is just the whole flag) is 994 hex letters. Assuming ASCII, it is 497 ASCII letters and so x = 71. We know that the format is `DUCTF{(a-z_)*}`, so we know the first 6 letters and last letter.

