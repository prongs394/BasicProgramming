import copy

def graphRead(G, n):
    i,j=0,0
    while ((i!=-1) and (j!=-1)):
        print("Enter two connected vertices or (-1, -1) for end: ", end='')
        a=tuple(map(int,input().strip().split(" ")))
        #print("a is:",a)
        i=a[0]; j=a[1]
        if ((i>=0) and (j>=0)) :
            if ((i<n) and (j<n)) :
                G[i][j]=1 ; G[j][i]=1
            else:
                print("wrong vertex number, try again.")

m = int(input("Enter the number of vertices: "))
G=[[0 for j in range(m)] for i in range(m)]
graphRead(G, m)

n=m
b=m
a=[0]*n
k=n-1
answers = []
while (k>=0) :
    #print(a)
    a[n-1]=a[n-1]+1
    k=n-1
    while((k>=0) and (a[k]==b)):
        a[k]=0
        k=k-1
        if (k>=0): a[k]=a[k] +1
    c = copy.copy(a)
    answers.append(c)

def check(list):
    count = 0
    for i in range(len(list)):
        if(i in list):
            count+=1
    if (count == len(list)):
        return True
    else:
        return False

dorost = []
for i in range(len(answers)):
    if(check(answers[i])):
        dorost.append(answers[i])

#print(dorost)

for i in range(len(dorost)):
    count = 0
    for j in range(m-1):
        if(G[dorost[i][j]][dorost[i][j+1]]==1):
            count+=1
    if(count==m-1):
        print(dorost[i])

print("_______________________")
print("برنامه دور های تکراری چاپ میکند")