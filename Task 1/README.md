# Comparative Analysis of Classical Encryption Techniques

## Objective

Perform an in-depth analysis of substitution and transposition techniques.

## Tasks

### 1. Computational Complexity Analysis

Analyze the computational complexity of implementing the following encryption techniques:

- **Playfair Cipher**
- **Hill Cipher**
- **Vigenère Cipher**

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
