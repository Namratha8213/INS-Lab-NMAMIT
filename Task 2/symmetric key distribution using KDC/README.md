# Symmetric Key Distribution using KDC (Key Distribution Center)

## Overview

This implementation demonstrates symmetric key generation and distribution using a Key Distribution Center (KDC) approach. It uses Python's `cryptography` library with Fernet (symmetric encryption) for secure key generation and management.

## Features

- Secure symmetric key generation
- Key storage simulation
- User-based key management
- Fernet-based encryption system

## Requirements

```bash
pip install cryptography
```

## Implementation Details

### Components

1. **Key Generation**

   ```python
   def generate_symmetric_key():
       return Fernet.generate_key()
   ```

2. **Key Storage System**

   ```python
   stored_keys = {}
   def store_key(user_id, key):
       stored_keys[user_id] = key
   ```

3. **Key Retrieval**
   ```python
   def get_key(user_id):
       return stored_keys.get(user_id, None)
   ```

## Usage

```bash
python kdc.py
```

## Sample Output

```
Distributed Symmetric Key for User123: b'YOUR_GENERATED_KEY_HERE...'
```

## Security Features

### 1. Key Generation

- Uses cryptographically secure random number generator
- 256-bit key length (Fernet specification)
- URL-safe base64-encoded format

### 2. Key Management

- User-specific key storage
- Key retrieval by user ID
- Simulated secure storage system

## Technical Details

### Key Properties

- **Algorithm**: Fernet (AES-128-CBC + HMAC-SHA256)
- **Key Length**: 256 bits
- **Encoding**: URL-safe base64

### Process Flow

1. Generate symmetric key
2. Associate key with user ID
3. Store key in secure storage
4. Retrieve key when needed

## Best Practices

1. **Key Storage**

   - Use secure database in production
   - Encrypt keys at rest
   - Implement access controls

2. **Key Distribution**
   - Use secure channels
   - Implement authentication
   - Add key rotation mechanism

## Code Structure

```
kdc.py
├── Key Generation
│   └── generate_symmetric_key()
├── Key Storage
│   ├── store_key()
│   └── get_key()
└── Example Usage
```

## Limitations

- Demonstration implementation only
- In-memory key storage (not persistent)
- Basic error handling
- No authentication mechanism

## Security Considerations

- Implement proper key storage
- Add error handling
- Use secure communication channels
- Add user authentication
- Implement key rotation
- Monitor key usage

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit pull request

## References

1. NIST SP 800-57: Key Management Guidelines
2. Fernet Specification
3. Python Cryptography Library Documentation

## License

MIT License

## Note

This implementation is for educational purposes. For production use:

- Replace in-memory storage with secure database
- Add proper error handling
- Implement authentication
- Use secure communication channels
- Add key rotation mechanism
