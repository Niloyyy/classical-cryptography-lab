ENGLISH_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def auto_solve_substitution(ciphertext):
    counts = {}
    for char in ciphertext.upper():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    sorted_cipher_letters = sorted(counts, key=counts.get, reverse=True)

    mapping = {}
    for i in range(len(sorted_cipher_letters)):
        if i < len(ENGLISH_ORDER):
            mapping[sorted_cipher_letters[i]] = ENGLISH_ORDER[i]

    decrypted_text = []
    for char in ciphertext:
        if char.upper() in mapping:
            plain_char = mapping[char.upper()]
            decrypted_text.append(plain_char.lower() if char.islower() else plain_char)
        else:
            decrypted_text.append(char)

    return "".join(decrypted_text), mapping

cipher_input = (
    "WKLV LV D VDPSOH FLSKHU WHAW WR GHPRQVWUDWH IUHTXHQFB "
    "DQDOBVLV DQG VXEVWLWXWLRQ GHFRGLQJ LQ FODVV."
)

result, letter_map = auto_solve_substitution(cipher_input)

print("AUTOMATICALLY RECOVERED PLAINTEXT:")
print("-" * 50)
print(result)
print("-" * 50)

print("\nGENERATED FREQUENCY MAPPING (Cipher -> Plain):")
for c_letter, p_letter in letter_map.items():
    print(f"{c_letter} -> {p_letter}", end=" | ")
print()