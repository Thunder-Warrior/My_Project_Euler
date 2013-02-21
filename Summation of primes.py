'''
from math import sqrt  
  

def isPrime(n):  
    for i in range(2, int(sqrt(n))+1):  
        if n % i == 0:  
            return False  
    return True  
  
index = 2  
num = 2000000  
sumOfPrime = 0  
  
while index <= num:  
    if isPrime(index):  
        sumOfPrime += index  
    index += 1  
  
print(sumOfPrime)  
'''
marked = [0] * 1000000
value = 3
s = 2
while value < 1000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 1000000:
            marked = 1
            i += value
    value += 2
print (s)