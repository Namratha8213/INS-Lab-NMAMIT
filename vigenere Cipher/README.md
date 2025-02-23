# Vigenère Cipher Implementation

## Overview

The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt text. Each letter in the plaintext is shifted by a varying amount determined by the corresponding letter in the keyword.

## Features

- Case-insensitive encryption/decryption
- Preserves non-alphabetic characters
- Automatic key repetition
- Simple and efficient implementation

## Implementation Details

### Encryption Algorithm

```python
# Formula: Ci = (Pi + Ki) mod 26
# where:
# Ci = ciphertext letter
# Pi = plaintext letter (0-25)
# Ki = keyword letter value (0-25)
```

### Decryption Algorithm

```python
# Formula: Pi = (Ci - Ki + 26) mod 26
# where:
# Pi = plaintext letter
# Ci = ciphertext letter (0-25)
# Ki = keyword letter value (0-25)
```

## Usage

```python
# Example usage
plaintext = "HELLO WORLD"
key = "KEY"

# Encryption
ciphertext = vignereCipher(plaintext, key)

# Decryption
originaltext = vignereCipher_decrypt(ciphertext, key)
```

## Sample Output

```
Enter the plaintext: HELLO WORLD
Enter the key: KEY
Ciphertext: RIJVS UYVJN
Originaltext: HELLO WORLD
```

## Function Documentation

### `vignereCipher(plaintext, key)`

- **Parameters:**
  - `plaintext`: String to encrypt
  - `key`: Encryption key
- **Returns:** Encrypted text
- **Features:**
  - Converts input to uppercase
  - Preserves spaces and special characters
  - Repeats key as needed

### `vignereCipher_decrypt(ciphertext, key)`

- **Parameters:**
  - `ciphertext`: String to decrypt
  - `key`: Decryption key
- **Returns:** Original text
- **Features:**
  - Case-insensitive processing
  - Maintains original formatting
  - Automatic key cycling

## Security Considerations

- Stronger than simple substitution ciphers
- Key length affects security strength
- Vulnerable to:
  - Kasiski examination
  - Statistical analysis
  - Known-plaintext attacks

## Requirements

- Python 3.x
- No external dependencies

## Running the Program

```bash
python vignereCipher.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit pull request

## License

MIT License

## Note

This implementation is for educational purposes only. For real security needs, use modern cryptographic algorithms.
