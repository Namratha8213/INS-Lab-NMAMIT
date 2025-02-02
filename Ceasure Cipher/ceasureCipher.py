def encrypt(text,shift):
    cipherText=""
    for i in range(len(text)):
        cha=text[i]
        if cha.isalpha():
            if cha.isupper():
                cipherText+= chr((ord(cha)+ shift-65)%26 +65)
            else:
                cipherText+= chr((ord(cha)+ shift-97)%26 +97)
        else:
            print("Please don't enter the numbers")
    return cipherText
    
def decrypt(text,shift):
    cipherText=""
    for i in range(len(text)):
        cha=text[i]
        if cha.isalpha():
            if cha.isupper():
                cipherText+= chr((ord(cha)- shift-65)%26 +65)
            else:
                cipherText+= chr((ord(cha)- shift-97)%26 +97)
        else:
            print("Please don't enter the numbers")
    return cipherText
    

text=input("Enter the text")
shift=int(input("Enter the shift size"))          
print(f"Encryption {encrypt(text,shift)}")
text=encrypt(text,shift)
print(f"Decryption {decrypt(text,shift)}")