# DES (Data Encryption Standard) Key Generation

## Overview

This implementation demonstrates the key generation process of the Data Encryption Standard (DES) algorithm. It generates multiple round keys from an initial input string using bit manipulation and circular shifts.

## Features

- Binary conversion of input string
- Left and right block splitting
- Circular shift operations
- Random bit selection
- Multiple round key generation

## Implementation Details

### Key Generation Process

1. **Input Processing**

   ```python
   # Convert input string to binary
   result = ''.join(format(ord(i),'08b') for i in s)
   ```

2. **Block Division**

   - Splits binary string into left and right halves
   - Removes every 8th bit for parity

3. **Round Key Generation**
   - Performs circular left shifts
   - Applies random bit selection
   - Generates 8 different round keys

## Usage

```python
# Run the program
python des.py

# Example input
Enter a string: HELLO
```

## Sample Output

```
Key 1 = 11010110101100
Key 2 = 10110101100110
Key 3 = 11001101011010
Key 4 = 10101100110110
Key 5 = 11011010110010
Key 6 = 10110011011010
Key 7 = 11010110101100
Key 8 = 10101100110110
```

## Technical Details

### Shift Schedule

```python
lt = [2, 3, 6, 7, 1, 6, 5, 9]  # Left shift values for each round
```

### Key Generation Steps

1. Binary conversion of input
2. Split into 32-bit blocks
3. Apply circular left shifts
4. Random bit selection
5. Key combination

## Functions and Operations

### Binary Conversion

```python
result = ''.join(format(ord(i),'08b') for i in s)
```

### Block Operations

```python
left = answer[:l]    # Left half
right = answer[l:]   # Right half
```

### Shift Operations

```python
nl = bin(nl<<lt[i])  # Left shift operation
```

## Security Considerations

- Implementation focuses on key generation only
- Does not include full DES encryption/decryption
- For educational purposes only

## Requirements

- Python 3.x
- No external dependencies

## Running the Program

```bash
python des.py
```

## Implementation Notes

- Simplified version for educational purposes
- Demonstrates basic concepts of DES key generation
- Not for production use

## Limitations

- Only implements key generation phase
- Does not include S-box operations
- Simplified permutation tables
- Not cryptographically secure

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit pull request

## License

MIT License

## References

- FIPS 46-3: Data Encryption Standard (DES)
- Cryptography and Network Security - William Stallings

## Screenshot of implementation and Output
