from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate a Symmetric Key (AES-256 using Fernet)
def generate_symmetric_key():
    return Fernet.generate_key()

# Generate an Asymmetric Key Pair (RSA-2048)
def generate_asymmetric_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Store keys securely (Simulated database)
key_store = {}

def store_key(user_id, key_type, key):
    key_store[user_id] = {key_type: key}
    print(f"Stored {key_type} key for {user_id}")

# Example Usage
user_id = "User123"
symmetric_key = generate_symmetric_key()
private_key, public_key = generate_asymmetric_keys()

store_key(user_id, "symmetric", symmetric_key)
store_key(user_id, "private", private_key)
store_key(user_id, "public", public_key)

# Display the Keys
print("\nGenerated Symmetric Key:")
print(symmetric_key.decode())

print("\nGenerated Private Key (RSA-2048):")
print(private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
).decode())

print("\nGenerated Public Key (RSA-2048):")
print(public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode())
