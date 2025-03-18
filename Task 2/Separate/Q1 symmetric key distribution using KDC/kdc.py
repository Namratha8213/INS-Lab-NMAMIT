from cryptography.fernet import Fernet

# Generate a symmetric key
def generate_symmetric_key():
    key = Fernet.generate_key()
    return key

# Securely store the key (simulated storage)
stored_keys = {}
def store_key(user_id, key):
    stored_keys[user_id] = key  # In practice, store securely in a database

# Secure key retrieval
def get_key(user_id):
    return stored_keys.get(user_id, None)

# Example Usage
user_id = "User123"
symmetric_key = generate_symmetric_key()
store_key(user_id, symmetric_key)

print(f"Distributed Symmetric Key for {user_id}: {get_key(user_id)}")
