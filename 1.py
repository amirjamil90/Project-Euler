for i in range(0,1001):
    a.append(i)
sum=0
for i in range(0,1000):
    if((a[i]%3==0) or (a[i]%5==0)):
        sum=sum+a[i]
print(sum)
