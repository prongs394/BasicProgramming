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

n=int(input())
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
d=[]

while(lolo!=0):
    for i in range(n-1,n-2-x,-1):
        if(a[i]==1):
            answer+=str(b[i])+' '
    print(answer)
    lolo=make(a,n)
    counter+=1
    answer=''
    if(counter>=p):
        x = x+1
        p = p*2


