import math 
maxPrime = -1
n=600851475143
while(n%2==0):                                     #sieve algo
  maxPrime=i
  n/=2
for(i in range int(math.srt(n))+1,2):                   #this checking is for Odd numbers 
  while(n%i==0):
    maxPrime=i
    n/=2
if(n>2):
  maxPrime=n
print(maxPrime)
