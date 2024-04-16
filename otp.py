import random
key = []
alpha = []
global encrypted
message = input("Input message: ")
for i in 'abcdefghijklmnopqrstuvwxyz':
  alpha.append(i)
key = random.sample(alpha, len(message))
print("Suggested key: " , key)

def encrypt(message, key):
  numerical = []
  numericalkey = []
  for i in message:
    for k in alpha:
      if i == k:
        numerical.append(alpha.index(k))
  for j in key:
    for h in alpha:
      if j == h:
        numericalkey.append(alpha.index(h))
        
  encrypted = []
  for x in range(len(numerical)):
    for y in range(len(numericalkey)):
      if x == y:
        encrypted.append((numerical[x]+numericalkey[y])%26)
  
  denumeralize = []
  for z in encrypted:
    for a in range(len(alpha)):
      if z == a:
        denumeralize.append(alpha[a])
  return print("Ciphertext: ",denumeralize)

def decrypt(message, key):
  numerical = []
  numericalkey = []
  for i in message:
    for k in alpha:
      if i == k:
        numerical.append(alpha.index(k))
  for j in key:
    for h in alpha:
      if j == h:
        numericalkey.append(alpha.index(h))
  
  encrypted = []
  for x in range(len(numerical)):
    for y in range(len(numericalkey)):
      if x == y:
        encrypted.append((numerical[x]-numericalkey[y])%26)
  
  denumeralize = []
  for z in encrypted:
    for a in range(len(alpha)):
      if z == a:
        denumeralize.append(alpha[a])
        
  return print("Originaltext: ",denumeralize)

encrypt(message, key)
message = input("Type ciphertext: ")
key = input("Type key: ")
decrypt(message, key)

