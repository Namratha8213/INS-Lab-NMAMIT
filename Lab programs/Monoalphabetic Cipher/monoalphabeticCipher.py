alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
keys=['u','v','w','x','y','z','d','e','f','g','h','i','j','k','l','m','n','a','b','c','o','p','q','r','s','t']

plaintext=input("Enter the Plaintext\n")
ciphertext=""
for i in plaintext:
    for j in alpha:
        if i==j:
            ciphertext+=keys[alpha.index(j)]

print(f"The encrypted text is {ciphertext}")

originalText=""
for i in ciphertext:
    for j in keys:
        if i==j:
            originalText+=alpha[keys.index(j)]

print(f"The original text is {originalText}")
