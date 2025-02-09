# Classical Ciphers Implementation and Analysis

This repository contains the implementation and analysis of three classical ciphers: **Playfair Cipher**, **Hill Cipher**, and **Vigenère Cipher**. Additionally, a **Hybrid Cipher** combining the Hill and Vigenère ciphers is implemented to achieve enhanced security.

---

## Table of Contents

1. [Cipher Design Process](#cipher-design-process)
   - [Playfair Cipher](#playfair-cipher)
   - [Hill Cipher](#hill-cipher)
   - [Vigenère Cipher](#vigenère-cipher)
2. [Encryption and Decryption Examples](#encryption-and-decryption-examples)
3. [Security Evaluation](#security-evaluation)
   - [Cryptanalysis Results](#cryptanalysis-results)
   - [Computational Complexity](#computational-complexity)
   - [Breaking Classical Ciphers](#breaking-classical-ciphers)
4. [Hybrid Cipher Implementation](#hybrid-cipher-implementation)
5. [Source Code Organization](#source-code-organization)
6. [Running the Examples](#running-the-examples)
7. [Security Recommendations](#security-recommendations)
8. [Future Improvements](#future-improvements)
9. [References](#references)

---

## 1. Cipher Design Process

### 1.1 Playfair Cipher

- **Design Components**:
  - 5x5 Matrix generation
  - Digraph processing
  - Encryption/Decryption rules

```python
def generate_matrix(key):
    matrix = [[0 for x in range(5)] for y in range(5)]
    # Matrix filling logic with key
    return matrix

def encrypt(plaintext, key):
    matrix = generate_matrix(key)
    digraphs = get_digraphs(plaintext)
    # Encryption logic
    return ciphertext
```

### 1.2 Hill Cipher

- **Design Components**:
  - Key matrix generation
  - Matrix multiplication
  - Modular arithmetic

```python
def create_key_matrix(key, n):
    # Creates nxn matrix from key
    matrix = np.array(key).reshape(n, n)
    return matrix

def hill_encrypt(plaintext, key_matrix):
    # Matrix multiplication for encryption
    return np.dot(plaintext, key_matrix) % 26
```

### 1.3 Vigenère Cipher

- **Design Components**:
  - Keyword expansion
  - Character shift calculation

```python
def vigenere_encrypt(plaintext, key):
    # Repeating key to match plaintext length
    full_key = key * (len(plaintext) // len(key) + 1)
    # Encryption using shifts
    return encrypted_text
```

## 2. Working Examples

### 2.1 Playfair Cipher Example

```
Key: "MONARCHY"
Plaintext: "HELLO WORLD"
Matrix:
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z

Encrypted: "HGNNV VQTNW"
```

### 2.2 Hill Cipher Example

```
Key Matrix:
| 2 3 |
| 1 4 |

Plaintext: "HELP"
Numeric: [7 4 11 15]
Encrypted: "RRKA"
```

### 2.3 Vigenère Cipher Example

```
Key: "KEY"
Plaintext: "HELLO"
Key Stream: "KEYEK"
Encrypted: "RIJVS"
```

## 3. Security Evaluation

### 3.1 Cryptanalysis Results

| Cipher   | Security Level | Vulnerabilities            |
| -------- | -------------- | -------------------------- |
| Playfair | Medium         | Digraph frequency analysis |
| Hill     | High           | Known plaintext attack     |
| Vigenère | Medium         | Kasiski examination        |

### 3.2 Computational Complexity

```python
# Time Complexity Analysis
Playfair: O(n) - Linear time
Hill: O(n*m³) - Cubic with matrix size
Vigenère: O(n) - Linear time
```

### 3.3 Hybrid Cipher Implementation

```python
class HybridCipher:
    def __init__(self):
        self.hill_key = self.generate_hill_key()
        self.vigenere_key = self.generate_vigenere_key()

    def encrypt(self, plaintext):
        # First layer: Hill Cipher
        hill_result = self.hill_encrypt(plaintext)
        # Second layer: Vigenère Cipher
        final_result = self.vigenere_encrypt(hill_result)
        return final_result
```

## 4. Source Code Organization

```
Task1/
├── playfair/
│   ├── playfair.py
│   └── test_playfair.py
├── hill/
│   ├── hill.py
│   └── test_hill.py
├── vigenere/
│   ├── vigenere.py
│   └── test_vigenere.py
└── hybrid/
    ├── hybrid.py
    └── test_hybrid.py
```

## 5. Running the Examples

```bash
# Navigate to cipher directory
cd Task1/playfair
python playfair.py

cd ../hill
python hill.py

cd ../vigenere
python vigenere.py
```

## 6. Security Recommendations

1. **Key Management**

   - Use strong random keys
   - Implement secure key distribution
   - Regular key rotation

2. **Implementation Security**

   - Input validation
   - Error handling
   - Buffer overflow prevention

3. **Usage Guidelines**
   - Educational purposes only
   - Not for sensitive data
   - Modern encryption recommended for production

## 7. Future Improvements

1. **Enhanced Security**

   - Larger matrix sizes
   - Multiple rounds
   - Key strengthening

2. **Performance Optimization**
   - Matrix multiplication optimization
   - Memory efficiency
   - Parallel processing

## 8. References

1. Cryptography and Network Security - William Stallings
2. Applied Cryptography - Bruce Schneier
3. NIST Special Publication 800-57: Key Management Guidelines
