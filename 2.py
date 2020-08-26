a=0
b=1
c=0
z=[]
sum=0
while(b<4000000):   
   c=a+b
   z.append(c) 
   a=b
   b=c
   sum=sum+c
s=0
print(z)
print(len(z))
i=0
even=0
odd=0
for i in range(len(z)):
    if((i%2)==0):
        print("hello",z[i])
        even=even+z[i]
    else:
        odd=odd+z[i]
        
print(even)
print(odd)
