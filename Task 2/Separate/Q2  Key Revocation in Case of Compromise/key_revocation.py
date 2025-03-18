from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Key Storage
key_store = {}  # Stores active keys
revoked_keys = set()  # Stores revoked user IDs


# Function to Generate a Symmetric Key (AES-256 using Fernet)
def generate_symmetric_key():
    return Fernet.generate_key()


# Function to Generate an Asymmetric Key Pair (RSA-2048)
def generate_asymmetric_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


# Function to Store Keys Securely
def store_key(user_id, key_type, key):
    if user_id in revoked_keys:
        print(f"Cannot store key for {user_id}, as they are revoked.")
        return
    if user_id not in key_store:
        key_store[user_id] = {}
    key_store[user_id][key_type] = key
    print(f"Stored {key_type} key for {user_id}")


# Function to Revoke a User's Keys
def revoke_key(user_id):
    if user_id in key_store:
        revoked_keys.add(user_id)
        del key_store[user_id]
        print(f"Revoked all keys for {user_id}")
    else:
        print(f"No keys found for {user_id}")


# Function to Check if a User's Key is Revoked
def is_key_revoked(user_id):
    return user_id in revoked_keys


# Function to Print Revoked Keys
def print_revoked_keys():
    if revoked_keys:
        print("\nRevoked Keys List:")
        for user in revoked_keys:
            print(f"- {user}")
    else:
        print("\nNo revoked keys found.")


# Example Usage
user_id1 = "User123"
user_id2 = "User456"

# Step 1: Generate Keys
symmetric_key1 = generate_symmetric_key()
private_key1, public_key1 = generate_asymmetric_keys()

symmetric_key2 = generate_symmetric_key()
private_key2, public_key2 = generate_asymmetric_keys()

# Step 2: Store Keys
store_key(user_id1, "symmetric", symmetric_key1)
store_key(user_id1, "private", private_key1)
store_key(user_id1, "public", public_key1)

store_key(user_id2, "symmetric", symmetric_key2)
store_key(user_id2, "private", private_key2)
store_key(user_id2, "public", public_key2)

# Step 3: Revoke Keys and Print Revoked List
revoke_key(user_id1)
revoke_key(user_id2)

# Step 4: Display Revoked Keys
print_revoked_keys()
