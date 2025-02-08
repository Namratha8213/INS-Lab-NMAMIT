import numpy as np
from hashlib import sha256
from secrets import token_bytes

class HybridCipher:
    def __init__(self, key_string):
        # Generate 128-bit keys using SHA-256
        hash_obj = sha256(key_string.encode())
        key_hash = hash_obj.digest()
        
        # Split hash into Hill cipher key and transposition key
        self.hill_key = self._generate_hill_matrix(key_hash[:16])  # First 128 bits
        self.trans_key = self._generate_trans_key(key_hash[16:32]) # Second 128 bits
        
    def _generate_hill_matrix(self, key_bytes):
        # Create 4x4 matrix (128-bit block size)
        matrix = np.frombuffer(key_bytes, dtype=np.uint8)
        return matrix.reshape(4, 4)
    
    def _generate_trans_key(self, key_bytes):
        return [x % 8 for x in key_bytes[:8]]  # 8 columns for transposition
    
    def encrypt(self, plaintext):
        # Step 1: Padding and blocking
        padded = self._pad_text(plaintext)
        blocks = [padded[i:i+16] for i in range(0, len(padded), 16)]
        
        # Step 2: Hill Cipher substitution
        substituted = []
        for block in blocks:
            nums = [ord(c) % 256 for c in block]
            matrix = np.array(nums).reshape(4, 4)
            sub_block = np.matmul(matrix, self.hill_key) % 256
            substituted.extend(sub_block.flatten())
        
        # Step 3: Columnar transposition
        transposed = self._columnar_transpose(bytes(substituted))
        
        return transposed.hex()

    def decrypt(self, ciphertext):
        # Reverse process...
        pass

    def _pad_text(self, text):
        pad_len = 16 - (len(text) % 16)
        return text + chr(pad_len) * pad_len
    
    def _columnar_transpose(self, data):
        rows = len(data) // 8
        matrix = [data[i:i+8] for i in range(0, len(data), 8)]
        result = bytearray()
        
        for col in self.trans_key:
            for row in range(rows):
                result.append(matrix[row][col])
        return result