def make(a,m):
    lol=m-1
    a[m-1]+=1
    while((lol>=0) and (a[lol]==2)):
        a[lol]=0
        lol=lol-1
        if(lol>=0):
            a[lol]+=1
        else:
            return(0)

n=int(input("enter n, numbers are from 1 to n:"))
k = int(input("enter k, k is the lenght of subsets:"))
which = int(input("if you want to rank enter 1 if you want to unrank type 2:"))
b=tuple(n-i for i in range(n))
a=[0]*n
#print("b is:",b)
lolo=make(a,n)
#print("first lolo is:",lolo)
counter=1
p=2
x=0
# answer baraye in ke: be string tabdil mikonim javab ro bad hey ye space ezafe mikonim
answer=''
#d=[]

matrix=[]
global count
count = 0
while(lolo!=0):
    list = []
    index = 0
    for i in range(n-1,n-2-x,-1):
        if(a[i]==1):
            list.append(b[i])
    if(len(list)==k):
        matrix.append(list)
        #print(list)
    lolo=make(a,n)
    counter+=1
    answer=''
    if(counter>=p):
        x = x+1
        p = p*2
#print(matrix)
def unrank(k):
    number = int(input("if you want the nth subset, type n:"))
    for i in range(k):
        print(matrix[number-1][i], end = ' ')

def rank(k):
    print("enter the subset for example: 1 2 3")
    vorodi =[]
    vorodii = input().split()
    for i in range(len(vorodii)):
        if(vorodii[i]==' '):
            pass
        else:
            adad = int(vorodii[i])
            vorodi.append(adad)
    #for i in range(k):
        #int(vorodi[i])
    #print(vorodi)
    true = 0
    for i in range(len(matrix)):
        if(vorodi==matrix[i]):
            print(i+1)
            true = 1
            i = len(matrix)
    if(true==0):
        print("not found")
if(which==1):
    rank(k)
if(which==2):
    unrank(k)

