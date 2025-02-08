# Comparative Analysis of Classical Encryption Techniques

## Objective

Perform an in-depth analysis of substitution and transposition techniques.

## Tasks

### 1. Computational Complexity Analysis

Analyze the computational complexity of implementing the following encryption techniques:

#### **Playfair Cipher**

- **Key Generation:** \( O(1) \) (Creating a 5×5 matrix from a keyword is constant time)
- **Encryption/Decryption:**
  - Splitting text into digraphs: \( O(n) \)
  - Searching for letters in the matrix: \( O(1) \) (constant time lookup in a 5×5 grid)
  - Applying substitution rules: \( O(n) \)
  - **Overall Complexity:** \( O(n) \)

#### **Hill Cipher**

- **Key Generation:** \( O(m^2) \) (Creating an \( m \times m \) matrix key)
- **Encryption:**
  - Splitting plaintext into blocks of size \( m \): \( O(n) \)
  - Matrix multiplication: \( O(m^3) \) (Standard matrix multiplication complexity)
  - **Overall Complexity:** \( O(nm^3) \)
- **Decryption:**
  - Computing matrix inverse: \( O(m^3) \) (Using Gaussian elimination)
  - Matrix multiplication with inverse: \( O(m^3) \)
  - **Overall Complexity:** \( O(nm^3) \)

#### **Vigenère Cipher**

- **Key Expansion (if needed):** \( O(n) \) (Repeating key to match plaintext length)
- **Encryption/Decryption:**
  - Shifting each letter based on the key: \( O(n) \) (Single pass through the text)
  - **Overall Complexity:** \( O(n) \)

### **Summary of Complexity**

| Cipher   | Key Generation | Encryption Complexity | Decryption Complexity |
| -------- | -------------- | --------------------- | --------------------- |
| Playfair | \( O(1) \)     | \( O(n) \)            | \( O(n) \)            |
| Hill     | \( O(m^2) \)   | \( O(nm^3) \)         | \( O(nm^3) \)         |
| Vigenère | \( O(n) \)     | \( O(n) \)            | \( O(n) \)            |

- **Playfair and Vigenère** are **efficient** with linear complexity.
- **Hill Cipher** has a higher complexity due to **matrix operations** but provides stronger security.

### 2. Cryptanalysis

Provide a mathematical explanation for breaking each cipher using cryptanalysis techniques.

### 3. Hybrid Cipher Design

Design and implement a hybrid cipher that combines a substitution and a transposition technique, ensuring:

- At least **128-bit encryption strength**.
- Justification of why this hybrid approach is more secure than using the techniques individually.

## Submission Requirements

Submit a detailed report including:

- Cipher design process.
- Encryption and decryption examples.
- Security evaluation of the hybrid cipher.

### Submission Includes:

- **Source code**
- **Working examples**
- **Detailed report explaining the encryption process**

## Repository Structure

```
📂 Comparative-Encryption-Analysis
│── 📁 src            # Source code for encryption techniques
│── 📁 examples       # Sample encryption and decryption outputs
│── 📄 report.pdf     # Detailed report with analysis and justification
│── 📜 README.md      # Project documentation
```

## How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/Comparative-Encryption-Analysis.git

# Navigate to the source directory
cd Comparative-Encryption-Analysis/src

# Run the encryption program
python hybrid_cipher.py
```

## Security Justification

- The hybrid approach enhances security by combining the strengths of substitution and transposition techniques.
- It achieves **128-bit encryption strength**, making brute-force attacks infeasible.
- The combination mitigates weaknesses present in individual classical encryption techniques.

## License

This project is licensed under the MIT License.
