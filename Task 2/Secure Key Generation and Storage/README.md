# Secure Key Generation and Storage System

## Overview

A Python implementation for generating and managing cryptographic keys, supporting both symmetric (AES-256) and asymmetric (RSA-2048) encryption schemes.

## Features

- Symmetric key generation (AES-256)
- Asymmetric key pair generation (RSA-2048)
- Key storage simulation
- PEM format serialization
- User-based key management

## Requirements

```bash
# Install required package
pip install cryptography
```

## Implementation

### Key Generation

```python
# Symmetric Key Generation
symmetric_key = generate_symmetric_key()

# Asymmetric Key Generation
private_key, public_key = generate_asymmetric_keys()
```

### Storage System

```python
# Store keys for a user
store_key(user_id, "symmetric", symmetric_key)
store_key(user_id, "private", private_key)
store_key(user_id, "public", public_key)
```

## Usage

```bash
# Run the key generation and storage system
python key_storage.py
```

### Sample Output

```
Generated Keys for User123:

Symmetric Key (AES-256):
b'dGhpc2lzYXNlY3JldGtleWZvcmFlczI1NmVuY3J5cHRpb24='

Private Key (RSA-2048):
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA...
-----END RSA PRIVATE KEY-----

Public Key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w...
-----END PUBLIC KEY-----
```

## Security Features

| Feature               | Implementation      |
| --------------------- | ------------------- |
| Symmetric Encryption  | AES-256 with Fernet |
| Asymmetric Encryption | RSA-2048            |
| Key Format            | PEM & Base64        |
| Storage               | In-memory (Demo)    |

## Best Practices

### 🔒 Key Generation

- Use cryptographically secure random numbers
- Follow NIST recommendations for key sizes
- Implement proper error handling

### 📋 Key Storage

- Encrypt keys at rest
- Implement access controls
- Regular key rotation
- Secure backup procedures

## Directory Structure

```
secure_key_system/
├── key_storage.py
├── requirements.txt
└── README.md
```

## Development Setup

1. Clone the repository

```bash
git clone https://github.com/yourusername/secure-key-system.git
cd secure-key-system
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the system

```bash
python key_storage.py
```

## Security Notes

⚠️ **Important**: This implementation is for educational purposes only.
For production use:

- Replace in-memory storage with secure database
- Implement proper key encryption at rest
- Add authentication and authorization
- Include audit logging
- Set up key rotation policies

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## References

- [NIST SP 800-57: Key Management Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf)
- [Python Cryptography Documentation](https://cryptography.io/en/latest/)
- [RSA PKCS Standards](https://tools.ietf.org/html/rfc3447)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Screenshot of implementation and Output

![Secure Key Generation and Storage](./images/image1.png)
![Secure Key Generation and Storage](./images/image2.png)
![Secure Key Generation and Storage](./images/image3.png)
