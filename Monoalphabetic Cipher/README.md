# Monoalphabetic Cipher

## Overview

A monoalphabetic cipher is a substitution cipher where each letter in the plaintext is replaced by another letter consistently throughout the encryption process. Unlike the Caesar Cipher, the substitution in a monoalphabetic cipher is not limited to shifting - any letter can be substituted for any other letter.

## Implementation Details

- **Language:** Python
- **Input:** Plaintext message (lowercase letters)
- **Output:** Encrypted ciphertext and decrypted original text
- **Key:** Fixed substitution mapping defined in the code

## How It Works

### Two arrays are used:

- `alpha`: Contains the regular alphabet (a-z)
- `keys`: Contains the substitution mapping

### Encryption Process:

1. Takes plaintext input
2. Maps each letter to its corresponding substitute from the key array
3. Maintains the original letter's position

### Decryption Process:

1. Takes ciphertext
2. Reverse maps each letter back to original using the key array
3. Recovers the original message

## Usage

### Example:

```shell
Enter the Plaintext
iswewishstoreplaceletter
The encrypted text is fbqyjfbeclaymiuwyiiyccya
The original text is iswewishstoreplaceletter
```

## Screenshot of implementation and Output

![Monoalphabetic Cipher](images/Monoalphabetic_Cipher.png)

## Advantages

- More secure than Caesar Cipher (26! possible combinations)
- Simple implementation
- Fixed substitution pattern

## Disadvantages

- Vulnerable to frequency analysis
- Can be broken using pattern recognition
- Key management is crucial
- Not suitable for modern cryptographic needs
