
'''generrate fibonacci numbers of mine'''
total=0
fibonacci_number1=1
fibonacci_number2=2
fibonacci_number3=0

total=fibonacci_number2
while 1:
    fibonacci_number3 = fibonacci_number1+fibonacci_number2
    if fibonacci_number3<4000001:
        if fibonacci_number3%2==0:
            total+=fibonacci_number3
    else:
        break
    fibonacci_number1=fibonacci_number2
    fibonacci_number2=fibonacci_number3
print (total)


'''optim solution
This may be a small improvement.  The Fibonacci series is:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

Now, replacing an odd number with O and an even with E, we get:

O, O, E, O, O, E, O, O, E, O, O, E, O, O, E...

And so each third number is even.  We don't need to calculate the odd numbers.  Starting from an two odd terms x, y, the series is:

x, y, x + y, x + 2y, 2x + 3y, 3x + 5y '''

'''program as above method
x = y = 1
sum = 0
while (sum < 4000001):
   sum += (x + y)
   x, y = x + 2 * y, 2 * x + 3 * y
print (sum)
'''


'''
I estimate that I had written about 3 million lines
 of assembler code in my whole life. Now, code only
 when strictly necessary.

Phi (golden ratio) is the approximate ratio between
 two consecutive terms in a Fibonacci sequence.
The ratio between consecutive even terms approaches
 phi^3 (4.236068) because each 3rd term is even.
Use a calculator and round the results to the nearest
 integer when calculating the next terms:

 2,8,34,.. multiplying by 4.236068 each time: 144,610,
 2584,10946,46368,196418 & 832040

The sum is 1089154
'''


