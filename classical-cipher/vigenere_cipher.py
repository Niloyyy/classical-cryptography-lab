def vigenere_encrypt(plaintext: str, key: str) -> str:
    key = key.upper()
    ciphertext = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            
            ciphertext.append(encrypted_char)
            key_index += 1 
        else:
            ciphertext.append(char)
            
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key = key.upper()
    plaintext = []
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)
            
    return "".join(plaintext)

if __name__ == "__main__":
    msg = "ATTACK AT DAWN"
    keyword = "LEMON"

    enc = vigenere_encrypt(msg, keyword)
    dec = vigenere_decrypt(enc, keyword)

    print(f"Plaintext : {msg}")
    print(f"Keyword   : {keyword}")
    print(f"Encrypted : {enc}")
    print(f"Decrypted : {dec}")