count=0
maxcount=0
for i in range(500001,1000000,2):
    count=0
    n=i
    while (i!=16):
        if i%2==0:
            i=i/2
        else:
            i=3*i+1
        count+=1
    if count>maxcount:
        j=n
        maxcount=count
print (maxcount,j)
