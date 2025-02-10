def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep spaces or special characters unchanged
    return result


def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)


def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        rail[row][col] = char
        col += 1
        row += 1 if direction_down else -1

    result = ''.join([''.join(row) for row in rail if row != '\n'])
    return result.replace('\n', '')


def rail_fence_decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        result.append(rail[row][col])
        col += 1
        row += 1 if direction_down else -1

    return ''.join(result)


def hybrid_encrypt(text, shift, rail_key):
    caesar_encrypted = caesar_cipher(text, shift)
    rail_fence_encrypted = rail_fence_encrypt(caesar_encrypted, rail_key)
    return rail_fence_encrypted


def hybrid_decrypt(cipher, shift, rail_key):
    rail_fence_decrypted = rail_fence_decrypt(cipher, rail_key)
    caesar_decrypted = caesar_decipher(rail_fence_decrypted, shift)
    return caesar_decrypted


# Example Usage
plaintext = input("Enter the plain text")
shift = int(input("Enter the shift key"))
rail_key =int(input("Enter the rail key"))

encrypted_text = hybrid_encrypt(plaintext, shift, rail_key)
print("Encrypted:", encrypted_text)

decrypted_text = hybrid_decrypt(encrypted_text, shift, rail_key)
print("Decrypted:", decrypted_text)
