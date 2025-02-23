# Feistel Cipher Implementation

## Overview

A Feistel Cipher implementation in Python that demonstrates the basic structure of many modern block ciphers. This implementation includes a simple round function using ASCII values and XOR operations.

## Features

- Symmetric block cipher structure
- Multiple round encryption/decryption
- Configurable round keys
- Automatic padding for odd-length inputs
- Simple round function implementation

## How It Works

### Round Function

```python
f(R, K) = (sum(ASCII values of R) + K) mod 256
```

### Encryption Process

1. Split plaintext into two halves (L₀, R₀)
2. For each round i:
   ```
   Lᵢ₊₁ = Rᵢ
   Rᵢ₊₁ = Lᵢ ⊕ f(Rᵢ, Kᵢ)
   ```
3. Concatenate final (Lₙ, Rₙ) for ciphertext

### Decryption Process

- Uses same algorithm with reversed round keys
- Automatically removes padding

## Usage

```python
# Example usage
round_keys = [3, 7, 2, 5]
plaintext = "HELLO"

# Encryption
encrypted_text = feistel_encrypt(plaintext, round_keys)

# Decryption
decrypted_text = feistel_decrypt(encrypted_text, round_keys)
```

## Sample Output

```
Plaintext: HELLO
Ciphertext: KJ#$P
Decrypted: HELLO
```

## Functions

### `feistel_round(L, R, K)`

- **Parameters:**
  - `L`: Left half of the block
  - `R`: Right half of the block
  - `K`: Round key
- **Returns:** Tuple of new (L, R) values

### `feistel_encrypt(plaintext, round_keys)`

- **Parameters:**
  - `plaintext`: Text to encrypt
  - `round_keys`: List of round keys
- **Returns:** Encrypted text

### `feistel_decrypt(ciphertext, round_keys)`

- **Parameters:**
  - `ciphertext`: Text to decrypt
  - `round_keys`: List of round keys
- **Returns:** Original plaintext

## Security Properties

- Symmetric encryption
- Balanced Feistel structure
- Security depends on:
  - Number of rounds
  - Round function complexity
  - Key schedule strength

## Implementation Notes

- Uses simple ASCII-based round function
- Supports variable length messages
- Adds 'X' padding if needed
- Round keys are integers

## Requirements

- Python 3.x
- No external dependencies

## Running the Code

```bash
python fiestalCipher.py
```

## Limitations

- Basic implementation for educational purposes
- Simple round function
- Fixed block size
- Not cryptographically secure

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit pull request

## License

MIT License
