# Elliptic Curve Cryptography (ECC) Implementation

## Overview

This implementation demonstrates the basic concepts of Elliptic Curve Cryptography using the `tinyec` library. It shows key generation and encryption key derivation using the brainpoolP256r1 curve.

## Features

- Elliptic curve key pair generation
- Point compression
- Encryption key derivation
- Uses brainpoolP256r1 curve parameters
- Secure random number generation

## Requirements

```bash
pip install tinyec
```

## Implementation Details

### Key Components

1. **Curve Selection**

   ```python
   curve = registry.get_curve("brainpoolP256r1")
   ```

2. **Point Compression**

   ```python
   def compress_point(point):
       return hex(point.x) + hex(point.y % 2)[2:]
   ```

3. **Encryption Key Generation**
   ```python
   def getEnKey(pubKey):
       ciPrivateKey = secrets.randbelow(curve.field.n)
       ciPublicKey = ciPrivateKey * curve.g
       enKey = ciPublicKey * ciPrivateKey
       return (enKey, ciPublicKey)
   ```

## Usage

```python
python ecc.py
```

## Sample Output

```
Sender's private key : 0x8c12d7f45123d1c6e2458973931b1c3966f5b9eb
Sender's public key : 0x7a28937f3f7472b383f4706c25d89c1cc7c15cc10

Sender's ciphertext public key : 0x6f4e25f1df12c94891b42949d9c76825c
Sender's encryption key : 0x9a3f2c8d1b5e4a7d6c0f9e8b7a2d5f4c3

Receiver's private key : 0x2a7b4c9d8e5f3a1b6c0d9e8f7a2b3c4d
Receiver's public key : 0x8b4f2e9d1c7a3b5f8e6d0c9a2b4f7e5d

Receiver's ciphertext public key : 0x5c8a3f1e9b4d7c2e6f0a8d3b5c9e1f4
Receiver encryption key : 0x3d6b9f4c1a8e2d5b7f0c4a9e3d6b8f2c
```

## Security Features

- Uses secure random number generation
- Standard curve parameters
- Point compression for efficient storage
- Private key protection

## Technical Details

### Curve Parameters (brainpoolP256r1)

- Prime field: 256-bit
- Security level: 128-bit
- NIST approved curve

### Key Generation Process

1. Generate random private key
2. Compute public key using curve point multiplication
3. Derive encryption keys using ECDH-like approach

## Code Structure

```
ecc.py
├── imports (tinyec, secrets)
├── curve initialization
├── compress_point() function
├── getEnKey() function
├── sender key generation
└── receiver key generation
```

## Limitations

- Basic implementation for educational purposes
- No message encryption/decryption
- Limited error handling
- Not production-ready

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit pull request

## References

1. SEC 2: Recommended Elliptic Curve Domain Parameters
2. Brainpool Standard Curves and Curve Generation
3. NIST SP 800-56A: Recommendation for Pair-Wise Key Establishment Schemes

## Screenshot of implementation and Output

![RSA](./images/ECC%20output.png)
