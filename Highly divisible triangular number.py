'''
def numofdi(d):
    numofdivisor=0
    for i in range(1,d):
        if d%i==0:
            numofdivisor+=1
    return numofdivisor
a=1
j=0
c=0
n=0
while 1:
    c=c+a
    n=numofdi(c)
    if n>=500:
        break
    a+=1
print(c)
'''


# 
i = 0
primes = range(2, 100)
while i < len(primes):
    primes = [x for x in primes if x == primes[i] or x % primes[i] != 0]
    i = i + 1

def numbersOfFactors(n):
    factorNumbers = 1
    factorTimes = 0
    i = 0
    while i < len(primes):
        if n % primes[i] == 0:
            factorTimes += 1
            n /= primes[i]
            continue
        else:
            if factorTimes != 0:
                factorNumbers *= factorTimes + 1
                factorTimes = 0
            i = i + 1
            if n == 1:
                break
    return factorNumbers


n = 3
while numbersOfFactors(n*(n+1)/2) < 500:
    n += 2


if numbersOfFactors(n*(n-1)/2) > 500:
    print (n*(n-1)/2)
else:
    print (n*(n+1)/2)




'''
def facp(n) :
  for i in xrange(2,n) :
    while n%i == 0 :
      n /= i
      yield i
    if i**2 > n : break
  if n!=1 : yield n

for n in xrange(3,99999) :
  p = list(facp(n/2))+list(facp(n+1)) if n%2==0 else list(facp(n))+list(facp((n+1)/2))
  c = reduce( lambda x,y: x*y, [p.count(i)+1 for i in set(p)] )
  if c > 500 : break
print n*(n+1)/2
'''