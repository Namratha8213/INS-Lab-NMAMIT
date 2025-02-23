import numpy as np

def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m using Extended Euclidean Algorithm."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # No modular inverse exists

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")

    # Pad plaintext with 'X' if necessary
    extra_chars = (n - len(plaintext) % n) % n  # How many 'X' are added
    plaintext += "X" * extra_chars

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""

    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)

    return ciphertext, extra_chars  # Return the number of added 'X' characters

def hill_cipher_decrypt(ciphertext, key_matrix, extra_chars):
    n = len(key_matrix)
    
    # Compute determinant
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = mod_inverse(det, 26)

    if det_inv is None:
        raise ValueError("Key matrix is not invertible under mod 26. Choose a different key.")

    # Compute adjugate (cofactor matrix transposed)
    adjugate = np.round(np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)).astype(int) % 26

    # Multiply adjugate by modular inverse of determinant
    key_inverse = (det_inv * adjugate) % 26

    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    originaltext = ""

    for i in range(0, len(ciphertext_vector), n):
        block = ciphertext_vector[i:i + n]
        result = np.dot(key_inverse, block) % 26
        originaltext += "".join(chr(int(num) + ord('A')) for num in result)

    # Remove extra 'X' padding added during encryption
    if extra_chars > 0:
        originaltext = originaltext[:-extra_chars]

    return originaltext

# Example usage
plaintext = input("Enter the text: ")
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Example 3x3 key matrix

ciphertext, extra_chars = hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted:", ciphertext)

try:
    originaltext = hill_cipher_decrypt(ciphertext, key_matrix, extra_chars)
    print("Decrypted:", originaltext)
except ValueError as e:
    print(e)
