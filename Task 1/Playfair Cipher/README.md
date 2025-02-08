# Playfair Cipher

## Overview

The Playfair cipher is a polygraphic substitution cipher that encrypts pairs of letters instead of single letters. This implementation in `playfairCipher.py` provides both encryption and decryption capabilities.

## Features

- Encrypts plaintext using a keyword-based 5x5 matrix
- Handles J/I substitution automatically
- Supports decryption of ciphertext back to the original message
- Implements standard Playfair cipher rules

## How It Works

### Key Matrix Generation

- Creates a 5x5 matrix using the keyword and remaining alphabet (excluding J)
- Removes duplicate letters from the key
- Fills remaining spaces with unused letters

### Encryption Rules

- Splits message into pairs of letters
- For pairs in the same row: Use letters to their right
- For pairs in the same column: Use letters below
- For pairs in different row/column: Use rectangle corners

### Decryption Process

- Reverses the encryption rules
- Removes padding X's from the final message

## Usage

```bash
python playfairCipher.py
```

## Sample Output

```
Enter keyword: SECRET
Enter plaintext: HELLO WORLD
Encrypted text: XMCKL QYNVP
Decrypted text: HELLO WORLD
```

## Implementation Notes

- Input text is automatically converted to uppercase
- All J's are converted to I's
- X is used for padding when necessary
- Spaces and special characters are not supported

## Security Considerations

- More secure than simple substitution ciphers
- Resistant to frequency analysis of single letters
- Historical cipher, not suitable for modern cryptographic needs
