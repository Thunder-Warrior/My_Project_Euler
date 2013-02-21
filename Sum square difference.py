sum1=0
sum2=0
for i in range(1,101):
    i=i**2
    sum1+=i
for j in range(1,101):
    sum2+=j
sum2=sum2**2
diff=sum1-sum2
print(diff)



'''
(1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4

1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6

Thus easily applicable to any n.
'''

'''
An interesting fact related to this problem is that the difference between the square of the sum and the sum of the cubes is always 0, for any n:

(1+2+3+...+n)^2=(1^3)+(2^3)+(3^3)+...+(n^3)
'''
