def Seive(n):
	#take boolean array and initialise all the elements by True
	#for prime number bollean value will be False. Else True 
	prime=[True for i in range(n+1)]
	p=2
	a=[]
	while(p*p <= n):
			if(prime[p]==True):
				for i in range(p*p,n+1,p):
					prime[i]=False 
			p+=1
	for j in range(2,n+1):
		if(prime[j]):
			a.append(j)
	print(a[10000])
Seive(10000000)		
