a=1                #first term
b=2
t=1
sum=0
while(b<=4000000):
    if(b%2==0):
        sum=sum+b           #sum of even valued numbers
    t=a                 #swapping of numbers for the next term generation
    a=b
    b=t+b
print(sum)                 #answer 
