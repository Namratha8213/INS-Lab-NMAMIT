# Vigenère Cipher

## Overview

The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt text. It improves upon simple substitution ciphers by using multiple Caesar cipher shifts based on the letters of a keyword.

## Features

- Encrypts plaintext using a repeating keyword
- Implements polyalphabetic substitution
- Supports both encryption and decryption
- Handles uppercase and lowercase letters
- Preserves non-alphabetic characters

## How It Works

### Encryption Process

1. The keyword is repeated to match the length of the plaintext
2. Each letter of the plaintext is shifted based on the corresponding keyword letter
3. Shift amount is determined by the position of the keyword letter (A=0, B=1, etc.)
4. Formula: Ci = (Pi + Ki) mod 26
   - Ci = Ciphertext letter
   - Pi = Plaintext letter
   - Ki = Keyword letter

### Decryption Process

1. Uses the same repeated keyword
2. Reverses the shift for each letter
3. Formula: Pi = (Ci - Ki + 26) mod 26

## Usage

```python
key = "KEY"
plaintext = "HELLO WORLD"
ciphertext = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(ciphertext, key)
```

## Sample Output

```
Enter keyword: KEY
Enter plaintext: HELLO WORLD
Encrypted text: RIJVS UYVJN
Decrypted text: HELLO WORLD
```

## Implementation Notes

- Input text is automatically converted to uppercase
- Spaces and special characters remain unchanged
- Keyword is repeated to match message length
- Non-alphabetic characters in plaintext are preserved

## Security Considerations

- More secure than monoalphabetic ciphers
- Keyword length affects security strength
- Vulnerable to Kasiski examination
- Not suitable for modern cryptographic needs

## Requirements

- Python 3.x
- No additional libraries required
