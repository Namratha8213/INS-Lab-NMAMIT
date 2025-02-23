def vignereCipher(plaintext,key):
    key=key.upper()
    ciphertext=""
    key_index=0
    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext+=char
    
    return ciphertext


def vignereCipher_decrypt(ciphertext,key):
    key=key.upper()
    originaltext=""
    key_index=0
    for char in ciphertext.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            originaltext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            originaltext+=char
    
    return originaltext
        
        
        
plaintext=input("Enter the plaintext\n")
key=input("Enter the key\n")
ciphertext=vignereCipher(plaintext,key)
print(ciphertext)
originaltext=vignereCipher_decrypt(ciphertext,key)
print(originaltext)