def gcd(a,b):
  while b:
    a,b=b,a%b
  return a

def rsa(p,q,mes):
  n=p*q
  phi=(p-1)*(q-1)
  
  for i in range(2,phi):
    if(gcd(i,phi)==1):
      e=i
      break
  print(e)
  j=0
  
  while True:
    if(j*e%phi)==1:
      d=j
      break
    j+=1
    
  print(d) 
  c=(mes**e)%n
  print(f"Encrypted message: {c}")
  
  m=(c**d)%n
  print(f"Decrypted message: {m}")
  
  if(mes==m):
    print("decryption is working")

p=int(input("Enter a prime number p: "))
q=int(input("Enter a prime number q: "))
mes=int(input("Enter the message: "))
rsa(p,q,mes)
