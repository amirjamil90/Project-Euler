#function to check palindrome in O(N)
def isPal(num):
	n=num
	r=0
	while(n!=0):
		k=n%10
		r=r*10+k
		n=n/10
	if(r==num):
		return 0 
	else:
		return 1

#the largest pallindrome for 3 numbers is 909. We can be guessing that the maximum nunmber lies between 900 and 1000
#this worked for me. 
max=909

for i in range(900,1000):
	for j in range(900,1000):
		if(isPal(i*j)==0):
			max=i*j
			print(i," and ",j)
			print(max)

print(max)
