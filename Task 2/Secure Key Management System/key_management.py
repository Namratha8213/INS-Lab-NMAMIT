from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, dh, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os, time, base64

# Key Store Simulation (Dictionary-based for simplicity)
key_store = {}  # Stores user keys (symmetric & asymmetric)
revoked_keys = set()  # Stores revoked user IDs to prevent unauthorized access

# ============================
# 1. CENTRALIZED KEY DISTRIBUTION (SYMMETRIC ENCRYPTION)
# ============================

def generate_symmetric_key():
    """
    Generates a symmetric encryption key using Fernet (AES-128 encryption).
    """
    return Fernet.generate_key()

def store_symmetric_key(user_id, key, expiry_time=3600):  # Key expires in 1 hour
    """
    Stores the generated symmetric key securely with an expiry time.
    If the key expires, a new one must be generated.
    """
    if user_id not in key_store:
        key_store[user_id] = {}
    key_store[user_id]['symmetric'] = {'key': key, 'expiry': time.time() + expiry_time}
    print(f"Symmetric key stored for {user_id}, expires in {expiry_time} seconds")

def is_key_expired(user_id):
    """
    Checks if a symmetric key is expired based on the stored expiry time.
    """
    return user_id in key_store and 'symmetric' in key_store[user_id] and time.time() > key_store[user_id]['symmetric']['expiry']

# ============================
# 2. PUBLIC KEY INFRASTRUCTURE (PKI) - ASYMMETRIC ENCRYPTION
# ============================

def generate_asymmetric_keys():
    """
    Generates an RSA-2048 key pair.
    - RSA is used for secure key exchange and authentication.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Standard exponent for security
        key_size=2048,  # Ensures strong encryption
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_private_key(private_key, password):
    """
    Encrypts the private key using a password-derived key.
    - Uses PBKDF2HMAC (Password-Based Key Derivation) for secure key encryption.
    - Generates a random salt to prevent brute-force attacks.
    - Uses AES-128 encryption via Fernet to store the private key securely.
    """
    salt = os.urandom(16)  # Random salt for key derivation
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))  # Derive encryption key
    encrypted_key = Fernet(key).encrypt(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))
    return salt, encrypted_key

def decrypt_private_key(encrypted_key, salt, password):
    """
    Decrypts the private key using the stored salt and password.
    - Uses the same PBKDF2HMAC key derivation technique.
    """
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    decrypted_key = Fernet(key).decrypt(encrypted_key)
    return serialization.load_pem_private_key(decrypted_key, password=None, backend=default_backend())

def store_asymmetric_keys(user_id, private_key, public_key, password):
    """
    Stores encrypted private keys and public keys securely.
    - Encrypts private key before storing.
    """
    if user_id not in key_store:
        key_store[user_id] = {}
    salt, encrypted_private_key = encrypt_private_key(private_key, password)
    key_store[user_id]['private'] = (salt, encrypted_private_key)
    key_store[user_id]['public'] = public_key
    print(f"Asymmetric keys stored securely for {user_id}")

# ============================
# 3. SECURE KEY EXCHANGE (SIGNED DIFFIE-HELLMAN)
# ============================

def generate_dh_parameters():
    """
    Generates Diffie-Hellman (DH) parameters for secure key exchange.
    - Used to generate shared secret keys between two parties.
    """
    return dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

def generate_dh_private_key(parameters):
    """
    Generates a private key for Diffie-Hellman key exchange.
    """
    return parameters.generate_private_key()

def compute_shared_secret(private_key, peer_public_key):
    """
    Computes the shared secret using Diffie-Hellman exchange.
    - Ensures that both parties derive the same secret key.
    """
    return private_key.exchange(peer_public_key)

def derive_key_from_secret(shared_secret):
    """
    Derives a symmetric encryption key from the Diffie-Hellman shared secret.
    - Uses HKDF (HMAC-based Key Derivation Function) with SHA-256.
    """
    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b'key exchange', backend=default_backend())
    return hkdf.derive(shared_secret)

def sign_public_key(private_key, public_key_bytes):
    """
    Signs the public key using RSA private key.
    - Provides authentication to prevent man-in-the-middle (MITM) attacks.
    """
    return private_key.sign(
        public_key_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verify_signature(public_key, public_key_bytes, signature):
    """
    Verifies the public key signature to ensure authenticity.
    - Prevents unauthorized key substitutions.
    """
    try:
        public_key.verify(
            signature,
            public_key_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

# ============================
# 4. KEY REVOCATION SYSTEM
# ============================

def revoke_key(user_id):
    """
    Revokes all keys associated with a user, preventing further access.
    """
    if user_id in key_store:
        revoked_keys.add(user_id)
        del key_store[user_id]
        print(f"All keys revoked for {user_id}")

def is_key_revoked(user_id):
    """
    Checks if the user's keys have been revoked.
    """
    return user_id in revoked_keys

# ============================
# EXECUTION & TESTING
# ============================

user_id = input("Enter the user id: ")
password = input("Enter the password: ")

# Generate and store symmetric key
symmetric_key = generate_symmetric_key()
store_symmetric_key(user_id, symmetric_key)

# Generate and store asymmetric keys
private_key, public_key = generate_asymmetric_keys()
store_asymmetric_keys(user_id, private_key, public_key, password)

print("Symmetric key generated and securely stored.")  
print(f"Symmetric key hash: {hash(symmetric_key)}")  # Masked representation

# Diffie-Hellman Key Exchange with Signatures
parameters = generate_dh_parameters()
private_key_A = generate_dh_private_key(parameters)
private_key_B = generate_dh_private_key(parameters)
public_key_A = private_key_A.public_key()
public_key_B = private_key_B.public_key()

# Signing keys to prevent MITM attacks
signature_A = sign_public_key(private_key, public_key_A.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
signature_B = sign_public_key(private_key, public_key_B.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))

if verify_signature(public_key, public_key_A.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo), signature_A) and \
   verify_signature(public_key, public_key_B.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo), signature_B):
    print("Public keys authenticated!")
else:
    print("Warning: Possible MITM attack detected!")

# Secure key derivation
shared_secret_A = compute_shared_secret(private_key_A, public_key_B)
symmetric_key_A = derive_key_from_secret(shared_secret_A)
print("Secure symmetric key derived!")
