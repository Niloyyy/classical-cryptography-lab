def generate_playfair_matrix(key : str):
    matrix = []
    used_char = set()
    key = key.upper().replace("J" , "I")
    for char in key:
        if char.isalpha() and char not in used_char:
            matrix.append(char)
            used_char.add(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in used_char:
            matrix.append(char)
            used_char.add(char)
    
    grid = [matrix[i : i + 5] for i in range(0 , 25 , 5)]
    return grid


def prepared_plaintext(text : str):
    clean = [c.upper().replace("J" , "I") for c in text if c.isalpha()]
    prepared = []
    i = 0 
    while i < len(clean):
        if i + 1 < len(clean):
            if clean[i] == clean[i+1]: 
                prepared.append(clean[i])
                prepared.append('X')
                i += 1
            else:
                prepared.append(clean[i])
                prepared.append(clean[i+1])
                i += 2
        else:
            prepared.append(clean[i])
            prepared.append('X')
            i += 1
    diagraph = [prepared[i : i + 2] for i in range (0 , len(prepared) , 2)]
    return diagraph

def find_pos(matrix , char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row , col
    return None            

def encrypt_pair(matrix , P1 , P2):
    R1 , C1 = find_pos(matrix , P1)
    R2 , C2 = find_pos(matrix , P2)
    if R1 == R2:
        return matrix[R1][(C1 + 1) % 5] + matrix[R2][(C2 + 1) % 5]
    elif C1 == C2:
        return matrix[(R1 + 1) % 5][C1] + matrix[(R2 + 1) % 5][C2]
    else:
        return matrix[R1][C2] + matrix[R2][C1]

def decrypt_pair(matrix , P1 , P2):
    R1 , C1 = find_pos(matrix , P1)
    R2 , C2 = find_pos(matrix , P2)
    if R1 == R2:
        return matrix[R1][(C1 - 1) % 5] + matrix[R2][(C2 - 1) % 5]
    elif C1 == C2:
        return matrix[(R1 - 1) % 5][C1] + matrix[(R2 - 1) % 5][C2]
    else:
        return matrix[R1][C2] + matrix[R2][C1]


def playfair_decrypt(key : str , cipher_text : str):
    matrix = generate_playfair_matrix(key)
    clean_cipher = [c.upper().replace("J" , "I") for c in cipher_text]
    diagraph = [clean_cipher[i : i + 2] for i in range(0 , len(clean_cipher) , 2)]
    plain = [encrypt_pair(matrix , P[0] , P[1]) for P in diagraph]
    return "".join(plain) 


def playfair_encrypt(key : str , msg : str):
    matrix = generate_playfair_matrix(key)
    diagraph = prepared_plaintext(msg)
    cipher = [encrypt_pair(matrix , P[0] , P[1]) for P in diagraph]
    return "".join(cipher) 


if __name__ == "__main__":
    key = "MONARCHY"
    msg = "SECRET"
    matrix = generate_playfair_matrix(key)
    #print(matrix)
    for row in matrix:
        print(" " + " ".join(row))
    cipher_text = playfair_encrypt(key , msg)
    print(cipher_text)
    plain_text = playfair_decrypt(key , cipher_text)
    print(plain_text)