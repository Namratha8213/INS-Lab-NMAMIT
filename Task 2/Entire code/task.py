from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

# Key Store Simulation
key_store = {}
revoked_keys = set()

# 1. Centralized Key Distribution for Symmetric Encryption

def generate_symmetric_key():
    """
    Generates a symmetric key using Fernet (AES-128).
    """
    return Fernet.generate_key()

def store_symmetric_key(user_id, key):
    """
    Stores the symmetric key in the key store.
    """
    if user_id not in key_store:
        key_store[user_id] = {}
    key_store[user_id]['symmetric'] = key
    print(f"Symmetric key stored for {user_id}")

# 2. Public Key Infrastructure (PKI) for Asymmetric Encryption

def generate_asymmetric_keys():
    """
    Generates an RSA-2048 key pair.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def store_asymmetric_keys(user_id, private_key, public_key):
    """
    Stores the RSA key pair in the key store.
    """
    if user_id not in key_store:
        key_store[user_id] = {}
    key_store[user_id]['private'] = private_key
    key_store[user_id]['public'] = public_key
    print(f"Asymmetric keys stored for {user_id}")

# 3. Secure Key Exchange Using Diffie-Hellman

def generate_dh_parameters():
    """
    Generates Diffie-Hellman parameters.
    """
    return dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

def generate_dh_private_key(parameters):
    """
    Generates a Diffie-Hellman private key.
    """
    return parameters.generate_private_key()

def compute_shared_secret(private_key, peer_public_key):
    """
    Computes the shared secret using Diffie-Hellman exchange.
    """
    return private_key.exchange(peer_public_key)

# 4. Key Revocation Mechanism

def revoke_key(user_id):
    """
    Revokes all keys associated with the user_id.
    """
    if user_id in key_store:
        revoked_keys.add(user_id)
        del key_store[user_id]
        print(f"All keys revoked for {user_id}")
    else:
        print(f"No keys found for {user_id}")

def is_key_revoked(user_id):
    """
    Checks if the user's keys have been revoked.
    """
    return user_id in revoked_keys

# Example Usage

# Generate and store symmetric key
user_id = "User123"
symmetric_key = generate_symmetric_key()
store_symmetric_key(user_id, symmetric_key)

# Generate and store asymmetric keys
private_key, public_key = generate_asymmetric_keys()
store_asymmetric_keys(user_id, private_key, public_key)

# Diffie-Hellman Key Exchange
parameters = generate_dh_parameters()
private_key_A = generate_dh_private_key(parameters)
private_key_B = generate_dh_private_key(parameters)
public_key_A = private_key_A.public_key()
public_key_B = private_key_B.public_key()
shared_secret_A = compute_shared_secret(private_key_A, public_key_B)
shared_secret_B = compute_shared_secret(private_key_B, public_key_A)
assert shared_secret_A == shared_secret_B
print("Shared secret established securely.")

# Revoke keys
revoke_key(user_id)
print(f"Are {user_id}'s keys revoked? {is_key_revoked(user_id)}")
