'''it is a Pascal's triangle'''

a=[]
for i in range(1,22):
    a.append(i)
print(a)

b=[]
for j in range(1,20):
    b=[]
    b.append(1)
    for k in range(1,21):
        b.append(a[k]+b[k-1])
    print(b)
    a=b
print (a[20])


'''
This is what I find 2 months ago when I solved it:

Each movement in the horizontal is a zero.
Each movement in the vertical is a one.

1st binary# in this series:
0000000000000000000011111111111111111111
last:
1111111111111111111100000000000000000000
For the numbers in between, the amount of
 zeros should be the same as ones. In other
 words, the ones and zeros have to be rearranged.

The total is: 40!/(20!)(20!)
Just use the MS calculator.
137846528820
Best,
Rudy.


Posting my approach. It's written in python.

def binom(n, m):
     b = [0] * (n + 1)
     b[0] = 1
     for i in xrange(1, n+1):
             b = 1
             j = i - 1
             while j > 0:
                     b[j] += b[j-1]
                     j -= 1
     return b[m]

print binom(40, 20)
'''