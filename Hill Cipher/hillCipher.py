import numpy as np
def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""
    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)
        print(ciphertext)
    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    key_inverse=np.linalg.inv(key_matrix)
    key_inverse=np.round(key_inverse*np.linalg.det(key_matrix))%26
    key_inverse=np.mod(np.rint(key_inverse*pow(int(np.linalg.det(key_matrix)))))
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    originaltext = ""
    for i in range(0, len(ciphertext_vector), n):
        block = ciphertext_vector[i:i + n]
        result = np.dot(key_inverse, block) % 26
        originaltext += "".join(chr(num + ord('A')) for num in result)
    return originaltext
    
# Example usage
plaintext = input("Enter the text\n")
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Example 3x3 key matrix
ciphertext=hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted:", ciphertext)
originaltext=hill_cipher_decrypt(ciphertext,key_matrix)
print("Decrypted:", originaltext)
