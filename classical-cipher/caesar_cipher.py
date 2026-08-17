def caesar_encrypt(plaintext : str , shift : int) -> str:
    ciphertext = []
    for char in plaintext:
        if char.islower():
            shifted = (ord(char) - ord('a') + shift) % 26
            ciphertext.append(chr(ord('a') + shifted))
        elif char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26
            ciphertext.append(chr(ord('A') + shifted))
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def caesar_decrypt(cipher : str) -> str:
    plaintext = []
    for shift in range(1 , 27):
        temp = []
        for char in cipher:
            if char.islower():
                shifted = ord(char) - shift
                if shifted < ord('a'):
                    shifted = shifted + 26
                temp.append(chr(shifted))
            elif char.isupper():
                shifted = ord(char) - shift
                if shifted < ord('A'):
                    shifted = shifted + 26
                temp.append(chr(shifted))
            else:
                temp.append(char)
        print("Shift = " , shift ,", Plaintext = ", "".join(temp))
        if shift == 8:
            plaintext = temp
            break
    return "".join(plaintext)

plaintext = "ihavenothingbro"
key = 8
cipher = caesar_encrypt(plaintext , key)
print("Ciphertext = " , cipher)
plaintext = caesar_decrypt(cipher)
print("Plaintext = " , plaintext)