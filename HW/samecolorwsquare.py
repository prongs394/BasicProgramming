n = int(input("enter n:"))   # we have n*n matrix

matrix = []   #اطلاعات را در این آرایه ذخیره میکنیم

for i in range(n):
    list=[]
    for i in range(n):
        list.append(0)
    matrix.append(list)

for i in range(n):                      #ورودی
    for j in range(n):
        print("entee[",i,"},[",j,"]")
        k=int(input())
        matrix[i][j]=k
print(matrix)

max=0
for i in range(n):
    for j in range(n):            #start is (i,j)
        for y in range(i , n):
            for x in range(j,n):              #end is (y,x)
                p=matrix[i][j]
                print("p is:",p,"anddddddddddd:",i,",",j,"alsooooooooooooooooooo",y,",",x,"the max is:",max)
                counter=0
                for satr in range(i,y+1):
                    for soton in range(j,x+1):
                        if (matrix[satr][soton]==p):
                            counter=counter+1
                           # print("counter is:",counter)
                print("hhhhhhhhhhhhhhhhhhhh:",((i-y+1)*(j-x+1)),"and final counter is:",counter)

                if(counter>=max and counter==((y - i + 1)*(x-j+1))):
                    max=counter
                    satrstart=i
                    sotonstart=j
                    satrend=y
                    sotonend=x


print("max is:",max)
print("and it starts from",satrstart,",",sotonstart,"and finishes at",satrend,",",sotonend)