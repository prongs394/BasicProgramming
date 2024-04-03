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

def change(list , m):
    esm = []
    for i in range(m):
        lol = []
        for j in range(i*m , i*m+m):
            lol.append(list[j])
        c = copy.copy(lol)
        esm.append(c)
    print("esm is:",esm)



m = int(input("Enter the number of vertices: "))
G=[[0 for j in range(m)] for i in range(m)]
graphRead(G, m)

n=m*m
b=2
a=[0]*n
k=n-1
answers=[]
while (k>=0) :
    print(a)
    a[n-1]=a[n-1]+1
    k=n-1
    while((k>=0) and (a[k]==b)):
        a[k]=0
        k=k-1
        if (k>=0): a[k]=a[k] +1
    c = copy.copy(a)
    answers.append(c)

print("answers: ", answers)

def check(mat , m):
    

for i in range(len(answers)):
    change(answers[i],m)





