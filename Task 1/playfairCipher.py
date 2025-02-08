def playfair(key,cipher):
    key="".join(dict.fromkeys((key+"ABCDEFGHIKLMNOPQRSTUVWXYZ").upper().replace("J","")))
    cipher=cipher.replace("J","I").upper()
    table=[key[i:i+5] for i in range(0,25,5)]
    pairs=[]
    i=0
    while(i<len(cipher)):
        a=cipher[i]
        b=cipher[i+1] if i+1<len(cipher) else "X"
        if a==b:
            pairs.append((a,"X"))
            i+=1
        else:
            pairs.append((a,b))
            i+=2
    def encrypt(pair):
        idx1=key.index(pair[0])
        idx2=key.index(pair[1])
        row1,col1=divmod(idx1,5)
        row2,col2=divmod(idx2,5)
        if row1==row2:
            return table[row1][(col1+1)%5]+table[row2][(col2+1)%5]
        elif col1==col2:
            return table[(row1+1)%5][col1]+table[(row2+1)%5][col2]
        else:
            return table[row1][col2]+table[row2][col1]
    encrypted_mes="".join(encrypt(pair)for pair in pairs)
    return encrypted_mes

#DECRYPTION FUNCTION 
def playfair_decrypt(key,cipher):
    key="".join(dict.fromkeys((key+"ABCDEFGHIKLMNOPQRSTUVWXYZ").upper().replace("J","")))
    cipher=cipher.replace("J","I").upper()
    table=[key[i:i+5] for i in range(0,25,5)]
    pairs=[]
    i=0
    while(i<len(cipher)):
        a=cipher[i]
        b=cipher[i+1] if i+1<len(cipher) else "X"
        if a==b:
            pairs.append((a,"X"))
            i+=1
        else:
            pairs.append((a,b))
            i+=2
    def decrypt(pair):
        idx1=key.index(pair[0])
        idx2=key.index(pair[1])
        row1,col1=divmod(idx1,5)
        row2,col2=divmod(idx2,5)
        if row1==row2:
            return table[row1][(col1+4)%5]+table[row2][(col2+4)%5]
        elif col1==col2:
            return table[(row1+4)%5][col1]+table[(row2+4)%5][col2]
        else:
            return table[row1][col2]+table[row2][col1]
    decrypted_mes="".join(decrypt(pair)for pair in pairs).replace("X", "") 
    return decrypted_mes

key=input("enter the key:")
mes=input("enter the cipher:")
enc=playfair(key,mes)
dec=playfair_decrypt(key,enc)

print("encrypted message:"+enc)

print("decrypted message:"+dec)
