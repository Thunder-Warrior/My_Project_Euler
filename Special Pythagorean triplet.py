'''Pythagorean triplet feature: if m is a odd integer, (m^2-1)/2 and(m^2+1)/2 were the triplet'''
'''1:find odd number
     2:if m (m^2-1)/2 (m^2+1)/2 were integer
        3:if  the sum of them is 1000
             break
'''
'''out put all of the Pythagorean triplet which the sum of it under or equal to 1000'''
'''
a=0
b=0
c=0
for i in range(1,1000,1):
    if ((i**22-1)/2)%1==0 and ((i**2+1)/2)%1==0:
        for j in range(1,300000):
            if i+(i**2-1)/2+(i**2+1)/2==j:
                flag=1
                a=i
                b=(i**2-1)/2
                c=(i**2+1)/2
                print(a+b+c,a*b*c,a,b,c)
'''
'''
a=0
b=0
c=0
m=0
n=0
result=0
for m in range(2,23):
    t=500/m-m
    n=int(t)
    if t-n==0 and m>n:
        print (m,n)
        a=m*m-n*n
        b=2*m*n
        c=m*n+n*m
        result=a*b*c
        print(a,b,c,result)
'''
import math
z=0
for i in range(3,1000):
    for j in range (i+1,1000):
        c=int(math.sqrt(i**2+j**2))
        if c**2==i**2+j**2 and j>i and c<1000 and c+i+j==1000:
            print(c,i,j,c*i*j)



'''Without programming:

a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
a + b + c = 1000;

2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
2mn + 2m^2 = 1000;
2m(m+n) = 1000;
m(m+n) = 500;

m>n;

m= 20; n= 5;

a= 200; b= 375; c= 425;
'''
