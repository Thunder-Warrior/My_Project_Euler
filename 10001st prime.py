from math import sqrt  
  

def isPrime(n):  
    for i in range(2, int(sqrt(n))+1):  
        if n % i == 0:  
            return False  
    return True  
  
index = 2  
j=0
num = 600851475143  
maxPrime = None  
  
for index in range(1,1111111111111111,2):'''a prime number also as a odd number,one is not a prime number,i assume two as one. the number of prime befor 10001 is identical'''
    if isPrime(index):  
        maxPrime = index
        j+=1
    index += 1 
    if j==10001:
        break
  
print(maxPrime)  



'''
This python solution finishes in 1,5s on my computer

import time, math
s = time.time()
def IsPrime( n ):
	if n == 2:
		return 1
	elif n % 2 == 0:
		return 0
	
	i = 3
	range = int( math.sqrt(n) ) + 1
	while( i < range ):
		if( n % i == 0):
			return 0
		i += 1
	return 1
N,T = 1,3
while N < 10001:
	if IsPrime(T):
		N+=1
	T+=2
print T-2
print time.time() - s
'''
