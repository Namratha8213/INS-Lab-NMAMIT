import math
p=int(input("Enter the prime numbers"))
a=int(input("Enter the primitive root"))
Xa=int(input("Enter the private key of a"))
Xb=int(input("enter the private key of b"))
Ya=(math.pow(a,Xa))%p
Yb=(math.pow(a,Xb))%p
print(f"Public Key of a {Ya}")
print(f"Public Key of b {Yb}")
Qa=(math.pow(Ya,Xa))%p
Qb=(math.pow(Yb,Xb))%p
print(f"Shared Key of a {Qa}")
print(f"Shared Key of b {Qb}")