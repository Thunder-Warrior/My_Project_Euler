N = 11*13*17*19
a = [11,12,13,14,15,16,17,18,19,20]
for j in range(N,100000000000000000000000000,19):
    for i in range(0,len(a)):
        if j%a[i]!=0:
            break
    if a[i]==20:
        minimun=j
        break
        
print(minimun)



'''
Python:
i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print i
'''
