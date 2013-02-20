
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


