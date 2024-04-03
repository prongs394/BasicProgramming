a = list(map(str,input().split()))
b = list(map(str,input().split()))

#sorting a
for i in range(len(a)):
	for j in range(len(a)):
		if(a[i]<a[j]):
			t = a[i]
			a[i] = a[j]
			a[j] = t
#print(a)

#sorting b
for i in range(len(b)):
	for j in range(len(b)):
		if(b[i]<b[j]):
			t = b[i]
			b[i] = b[j]
			b[j] = t
#print(b)

#merging
list = [None]*(len(a)+len(b))
list = a + b
for i in range(len(list)):
	for j in range(len(list)):
		if(list[i]<list[j]):
			t = list[i]
			list[i] = list[j]
			list[j] = t

#print("final result:")
for k in range(len(list)):
	print(list[k], end=" ")