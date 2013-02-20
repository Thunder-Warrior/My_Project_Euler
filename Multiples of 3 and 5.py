'''Calculate the sum of all multiples of 3 or 5 bellow 1000 '''
def main():
    sum=0
    for i in range(1,1000):
        if (i%3==0) or (i%5==0):
            sum+=i
    print (sum)
main()
