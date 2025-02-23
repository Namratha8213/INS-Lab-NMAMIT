def feistel_round(L, R, K):
    """
    One round of the Feistel cipher.
    Uses a simple round function: f(R, K) = (sum of ASCII values of R + K) % 256.
    Then, new_R = L XOR f(R, K).
    """
    new_L = R  # The right half becomes the new left half.
    round_function = (sum(ord(c) for c in R) + K) % 256  # Sum ASCII values of R and add key
    new_R = "".join(chr(ord(L[i]) ^ round_function) for i in range(len(L)))  # XOR operation
    return new_L, new_R

def feistel_encrypt(plaintext, round_keys):
    """
    Encrypts a string plaintext using Feistel cipher with given round keys.
    """
    if len(plaintext) % 2 != 0:  # Ensure even length
        plaintext += "X"

    L, R = plaintext[:len(plaintext)//2], plaintext[len(plaintext)//2:]  # Split into two halves

    for K in round_keys:  # Apply multiple Feistel rounds
        L, R = feistel_round(L, R, K)

    return L + R  # Concatenate final halves as ciphertext

def feistel_decrypt(ciphertext, round_keys):
    """
    Decrypts a string ciphertext using Feistel cipher.
    Uses the round keys in reverse order.
    """
    L, R = ciphertext[:len(ciphertext)//2], ciphertext[len(ciphertext)//2:]  # Split into two halves

    for K in reversed(round_keys):  # Reverse the encryption rounds
        R, L = feistel_round(R, L, K)  # Reverse the Feistel process

    return (L + R).replace("X","")  # Concatenate to get the original plaintext


round_keys = [3, 7, 2, 5]  # Example round keys
plaintext = "HELLO"  # Example plaintext
encrypted_text = feistel_encrypt(plaintext, round_keys)
decrypted_text = feistel_decrypt(encrypted_text, round_keys)
print(f"Plaintext: {plaintext}")          # Expected: HELLO
print(f"Ciphertext: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")