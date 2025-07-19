from collections import Counter
"""
['2247', '2247', '2247', '2418', '2247', '2247', '2418', '2106', '2106', '2106', '2418', '2329', '2329', '2329', '2418', '2247', '2247', '2418', '1979', '1979', '1979', '2418', '2247', '2247', '2418', '2174', '2174', '2418', '2188', '2418', '1979', '1979', '1979', '2418', '2174', '2174', '2418', '2061', '2061', '2061', '2061', '2418', '2106', '2106', '2418', '1979', '1979', '1979', '2418', '2174', '2418', '2061', '2061', '2061', '2061', '2418', '2329', '2418', '1979', '1979', '1979', '2418', '2106', '2106', '2106', '2418', '2106', '2106', '2106', '2418', '2061', '2061', '2061', '2418', '2174', '2174', '2418', '2247', '2418', '2174', '2174', '2418', '2247', '2418', '2033', '2033', '2418', '2174', '2174', '2418', '2061', '2061', '2061', '2418', '2188', '2418', '1979', '1979', '2418', '1979', '1979', '1979', '2418', '2061', '2061', '2061', '2061']
"""
# Paste your input string here
data_string = (
    "2247224722472418224722472418210621062106241823292329232924182247224724181979197919792418"
    "2247224724182174217424182188241819791979197924182174217424182061206120612061241821062106"
    "2418197919791979241821742418206120612061206124182329241819791979197924182106210621062418"
    "2106210621062418206120612061241821742174241822472418217421742418224724182033203324182174"
    "2174241820612061206124182188241819791979241819791979197924182061206120612061"
)

# Step 1: Split into 4-digit blocks
blocks = [data_string[i:i+4] for i in range(0, len(data_string), 4)]

# Step 2: Count frequency of each 4-digit code
counts = Counter(blocks)

# Step 3: Most frequent 8 non-delimiter codes → assign 3-bit codes
DELIMITER = '2418'
bit_codes = ['000', '001', '010', '011', '100', '101', '110', '111']

# Exclude the delimiter and get top 8
top_8 = [code for code, _ in counts.most_common() if code != DELIMITER][:8]
mapping = dict(zip(top_8, bit_codes))
mapping[DELIMITER] = '|'  # separator

# Step 4: Translate blocks to binary string
binary_string = ""
for code in blocks:
    val = mapping.get(code)
    if val == '|':
        binary_string += ' '
    elif val:
        binary_string += val

# Step 5: Convert binary to ASCII
binary_compact = binary_string.replace(' ', '')
decoded_chars = []
for i in range(0, len(binary_compact), 8):
    byte = binary_compact[i:i+8]
    if len(byte) == 8:
        decoded_chars.append(chr(int(byte, 2)))

decoded_message = ''.join(decoded_chars)

# Output result
print("Top 8 Frequencies Mapped:\n", mapping)
print("\nDecoded Message:\n", decoded_message)
