# Asymmetric Key Distribution using KDC (Key Distribution Center)

## Overview

This implementation demonstrates asymmetric key generation and distribution using a Key Distribution Center (KDC) approach with RSA algorithm. It uses the Python `cryptography` library for secure key generation and management.

## Features

- RSA key pair generation (2048-bit)
- PEM format key serialization
- PKCS#8 standard compliance
- No encryption for educational demonstration

## Requirements

```bash
pip install cryptography
```

## Implementation Details

### Key Generation Process

```python
from cryptography.hazmat.primitives.asymmetric import rsa
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
```

### Key Properties

- **Key Size**: 2048 bits
- **Public Exponent**: 65537 (standard RSA exponent)
- **Format**: PKCS#8
- **Encoding**: PEM

## Usage

```bash
python kdc.py
```

## Sample Output

```
Private Key:
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC9QFi8...
-----END PRIVATE KEY-----

Public Key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvUBYvD6RF7...
-----END PUBLIC KEY-----
```

## Security Features

1. **Strong Key Generation**

   - Cryptographically secure random number generation
   - Standard RSA key size (2048 bits)
   - Standard public exponent (65537)

2. **Standard Formats**
   - PKCS#8 for private key
   - SubjectPublicKeyInfo for public key
   - PEM encoding for both keys

## Code Structure

```
kdc.py
├── Key Generation
│   └── RSA key pair creation
├── Key Serialization
│   ├── Private key to PEM
│   └── Public key to PEM
└── Output Display
```

## Best Practices

1. **Key Storage**

   - Store private keys securely
   - Use proper permissions
   - Consider encryption at rest

2. **Key Distribution**
   - Secure channel for private key
   - Public key can be distributed freely
   - Implement proper authentication

## Limitations

- Demo implementation (no encryption of private key)
- Basic error handling
- No key storage implementation
- Educational purposes only

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit pull request

## References

1. PKCS #8: Private-Key Information Syntax Specification
2. RFC 5280: X.509 Public Key Infrastructure
3. NIST SP 800-57: Key Management Guidelines

## License

MIT License

## Note

This implementation is for educational purposes. For production use:

- Implement proper key storage
- Add error handling
- Use key encryption
- Follow security best practices

## Screenshot of implementation and Output

![Asymmetric key distribution using KDC](./images/image1.png)
![Asymmetric key distribution using KDC](./images/image2.png)
