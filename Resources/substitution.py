from collections import Counter

ciphertext = ['2247', '2247', '2247', '2418', '2247', '2247', '2418', '2106', '2106', '2106', '2418', '2329', '2329', '2329', '2418', '2247', '2247', '2418', '1979', '1979', '1979', '2418', '2247', '2247', '2418', '2174', '2174', '2418', '2188', '2418', '1979', '1979', '1979', '2418', '2174', '2174', '2418', '2061', '2061', '2061', '2061', '2418', '2106', '2106', '2418', '1979', '1979', '1979', '2418', '2174', '2418', '2061', '2061', '2061', '2061', '2418', '2329', '2418', '1979', '1979', '1979', '2418', '2106', '2106', '2106', '2418', '2106', '2106', '2106', '2418', '2061', '2061', '2061', '2418', '2174', '2174', '2418', '2247', '2418', '2174', '2174', '2418', '2247', '2418', '2033', '2033', '2418', '2174', '2174', '2418', '2061', '2061', '2061', '2418', '2188', '2418', '1979', '1979', '2418', '1979', '1979', '1979', '2418', '2061', '2061', '2061', '2061']
ciphertext = "".join(ciphertext).split("2418")

sequence_counts = Counter(ciphertext)
if '' in sequence_counts:
    del sequence_counts['']

for seq, count in sequence_counts.most_common():
    print(f"'{seq}': {count}")

"""
'197919791979': 5
'21742174': 5
'22472247': 3
'210621062106': 3
'2061206120612061': 3
'2188': 2
'206120612061': 2
'2247': 2
'224722472247': 1
'232923292329': 1
'21062106': 1
'2174': 1
'2329': 1
'20332033': 1
'19791979': 1
"""

print(ciphertext)

# replace the _
# english letter frequency "ETAON RISHD LFCMU GYPWB VKJXZQ", E being the most commonly used letter
subs_dict = dict()
subs_dict["197919791979"] = "A"
subs_dict["21742174"] = "B"
subs_dict["22472247"] = "C"
subs_dict["210621062106"] = "D"
subs_dict["2061206120612061"] = "E"
subs_dict["2188"] = "F"
subs_dict["206120612061"] = "G"
subs_dict["2247"] = "H"
subs_dict["224722472247"] = "I"
subs_dict["232923292329"] = "J"
subs_dict["21062106"] = "K"
subs_dict["2174"] = "L"
subs_dict["2329"] = "M"
subs_dict["20332033"] = "N"
subs_dict["19791979"] = "O"
# ICDJCACBFABEKALEMADDGBHBHNBGFOAE
# frequency
# modulate

for i, cipher_letter in enumerate(ciphertext):
    if cipher_letter in subs_dict:
        ciphertext[i] = subs_dict[cipher_letter]

print("".join(ciphertext))