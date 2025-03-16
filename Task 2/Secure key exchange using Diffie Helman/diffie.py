from cryptography.hazmat.primitives.asymmetric import dh

# Generate DH parameters
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Generate Private Keys for two parties
private_key_A = parameters.generate_private_key()
private_key_B = parameters.generate_private_key()

# Exchange Public Keys
public_key_A = private_key_A.public_key()
public_key_B = private_key_B.public_key()

# Compute Shared Secret
shared_secret_A = private_key_A.exchange(public_key_B)
shared_secret_B = private_key_B.exchange(public_key_A)

assert shared_secret_A == shared_secret_B  # Both parties should have the same key
print("Shared Secret Established Securely!")
print("Shared Secret:", shared_secret_A)