
def isPalindrome(n):  

    if n<10:
        return False
    elif n<100:
        if int(n/10)==n%10:
            return True
    elif n<1000:
        if int(n/100)==n%10:
            return True
    elif n<10000:
        if int(n/1000) == n%10 and (int(n/100))%10 == (int(n/10))%10:
            return True
    elif n<100000:
        if int(n/10000) == n%10 and (int(n/1000))%10 == (int(n/10))%10:
            return True
    elif n<1000000:
        if int(n/100000) == n%10 and (int(n/10000))%10 ==(int(n/10))%10 and (int(n/1000)) %10== (int(n/100))%10:
            return True
    else:
        return False   
  
index = 10  
num = 998001 
maxPalindrome = 0 
a=0
b=0

for i in range(100,1000):
    for j in range(i+1,1000):
        index = i*j
        if isPalindrome(index): 
            if index > maxPalindrome:
                maxPalindrome = index
                a=i
                b=j  
print(maxPalindrome,a,b)  




'''
The palindrome can be written as:

abccba

Which then simpifies to:

100000a + 10000b + 1000c + 100c + 10b + a

And then:

100001a + 10010b + 1100c

Factoring out 11, you get:

11(9091a + 910b + 100c)

So the palindrome must be divisible by 11.  Seeing as 11 is prime, at least one of the numbers must be divisible by 11.  So brute force in Python, only with less numbers to be checked:

def c():
   max = maxI = maxJ = 0
   i = 999
   j = 990
   while (i > 100):
      j = 990
      while (j > 100):
         product = i * j
         if (product > max):
            productString = str(product)
            if (productString == productString[::-1]):
               max = product
               maxI = i
               maxJ = j
         j -= 11
      i -= 1
   return max, maxI, maxJ
'''



'''
You can also do this with pen and paper.  You have a number:

(100a + 10b + c)(100d + 10e + f) 

Which is a palindrone.  This factors out to:

                   100cd + 10ce + cf +
          1000bd + 100be + 10bf +
10000ad + 1000ae + 100af

Assuming the first digit is 9, then cf must be equal to nine.
Also, both a and d must then be equal to nine.  The only ways
to make the last digit of the product of two integers 9 would
be if those integers were either of:

1 and 9
3 and 3
7 and 7

So, both numbers must start with 9, end with either 1, 3, 7,
or 9, and one of them must be divisible by 11.  The only 
numbers divisible by 11 from 900 - 1000 are:

902
913
924
935
946
957
968
979
990

You can discard all of those that do not end in either 1, 3,
7, or 9, and you are left with:

913
957
979

So now the presumed answer is either:

(900 + 10 + 3)(900 + 10x + 3)
(900 + 50 + 7)(900 + 10x + 7)
(900 + 70 + 9)(900 + 10x + 1)

Factoring all those out, you get:

810000 + 9000x + 2700 + 9000 + 100x + 30 + 2700 + 30x + 9
824439 + 9130x

Now, for the first digit 824439 + 9130x to be 9, x must be 9
(if x were 8, then 824439 + 9130x = 897479, and the first
digit is 8).  And so you have 913 * 993, which is the answer.
You can factor the others out to see if they produce a bigger
answer, which they don't.
'''
