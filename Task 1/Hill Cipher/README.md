# Hill Cipher

## Overview

The Hill cipher is a polygraphic substitution cipher based on linear algebra. It operates on blocks of letters using matrix multiplication for encryption and matrix inversion for decryption.

## Features

- Encrypts plaintext using a key matrix
- Supports customizable matrix dimensions (2x2, 3x3)
- Performs matrix operations for encryption/decryption
- Includes modular arithmetic operations
- Handles automatic padding of messages

## How It Works

### Key Matrix

- Uses a square matrix of dimensions n×n as the cipher key
- Matrix must be invertible modulo 26
- Each element in matrix represents a number (A=0, B=1, ..., Z=25)

### Encryption Process

1. Convert plaintext to numeric values (A=0, B=1, ...)
2. Group the numbers into vectors of size n
3. Multiply each vector by the key matrix
4. Convert results back to letters modulo 26

### Decryption Process

1. Find inverse of key matrix modulo 26
2. Convert ciphertext to numeric values
3. Multiply by inverse matrix
4. Convert results back to letters

## Usage

```python
# Example for 2x2 matrix
key = [[3, 3],
       [2, 5]]
plaintext = "HELLO"
ciphertext = encrypt(key, plaintext)
decrypted = decrypt(key, ciphertext)
```

## Sample Output

```
Enter key matrix (2x2):
3 3
2 5
Enter plaintext: HELLO
Encrypted text: HVFQS
Decrypted text: HELLO
```

## Implementation Notes

- Input text is automatically converted to uppercase
- Messages are padded if length isn't multiple of matrix size
- Spaces and special characters are removed
- Uses modular arithmetic operations
- Requires numpy library for matrix operations

## Security Considerations

- Security depends on key matrix size
- Larger matrices provide better security
- Vulnerable to known-plaintext attacks
- Not suitable for modern cryptographic applications

## Requirements

- Python 3.x
- Numpy library
