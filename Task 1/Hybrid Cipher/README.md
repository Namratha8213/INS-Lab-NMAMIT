# Hybrid Classical Cipher

## Overview

This implementation combines two classical ciphers - Caesar Cipher and Rail Fence Cipher - to create a hybrid encryption system that provides both substitution and transposition techniques.

## Features

- Combines Caesar Cipher (substitution) and Rail Fence (transposition)
- Preserves case sensitivity
- Handles special characters and spaces
- Two-layer encryption/decryption process
- Configurable shift and rail keys

## Implementation Details

### Encryption Process

1. **Caesar Cipher Layer**
   - Shifts each letter by a specified amount
   - Preserves case and special characters
2. **Rail Fence Layer**
   - Arranges text in zigzag pattern
   - Creates transposition based on rail key

### Mathematical Foundation

```
Caesar Encryption: C = (P + k) mod 26
Rail Fence Pattern: zigzag of depth n
where:
- C = ciphertext letter
- P = plaintext letter
- k = shift key
- n = number of rails
```

## Usage

```python
# Basic usage example
plaintext = "Hello World!"
shift_key = 3
rail_key = 3

# Encryption
encrypted = hybrid_encrypt(plaintext, shift_key, rail_key)

# Decryption
decrypted = hybrid_decrypt(encrypted, shift_key, rail_key)
```

## Sample Input/Output

```
Enter the plain text: Hello World!
Enter the shift key: 3
Enter the rail key: 3

Encrypted: Kryze Zruog!
Decrypted: Hello World!
```

## Functions

### Encryption Functions

- `caesar_cipher(text, shift)`: Performs Caesar cipher encryption
- `rail_fence_encrypt(text, key)`: Performs Rail Fence encryption
- `hybrid_encrypt(text, shift, rail_key)`: Combines both ciphers for encryption

### Decryption Functions

- `caesar_decipher(text, shift)`: Reverses Caesar cipher
- `rail_fence_decrypt(cipher, key)`: Reverses Rail Fence cipher
- `hybrid_decrypt(cipher, shift, rail_key)`: Complete hybrid decryption

## Security Considerations

1. **Strengths**

   - Multiple encryption layers
   - Combination of substitution and transposition
   - Configurable parameters

2. **Limitations**
   - Based on classical ciphers
   - Not cryptographically secure
   - Vulnerable to modern cryptanalysis

## Requirements

- Python 3.x
- No external dependencies

## Installation

1. Clone the repository
2. Navigate to the directory
3. Run the script:

```bash
python hybridCipher.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request
