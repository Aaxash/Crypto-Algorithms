from random import randint
  
#input variables
p = 1229
q = 1511

#calculate n
n = p*q 
#calculate totient
totient = (p-1)*(q-1) 


def gcd(a, b):
	while b:
		a, b = b, a%b
	return a


#calculate e
r = randint(2,totient) # For efficiency 2 < e < 100
while True:
	if gcd(r, totient) == 1:
		break
	else:
		r += 1
e = r
  

# function to find modular inverse
def modinv(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m

# function to find extended gcd
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)


d = modinv(e, totient)
m =int(input("Enter message: "))
# Encryption of m
c =(m**e) % n
print("Encrypted message = %d" % c)
# Decryption of m
m1 = (c**d) % n
print("Decrypted message = %d" % m1)
