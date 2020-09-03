arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
max_arr=-1
for i in range(len(arr)):
	if(arr[i]>max_arr):
		max_arr=arr[i]
print(max_arr)
x=2
res=1
while(x<=max_arr):
	indexes=[]
	for j in range(len(arr)):
		if(arr[j]%x==0):
			indexes.append(j)
	if(len(indexes)>1):
		for j in range(len(indexes)):
			arr[indexes[j]]=int(arr[indexes[j]]/x)
		res*=x
	else:
		x+=1
print(arr)
for i in range(len(arr)):
	res*=arr[i]
print(res)