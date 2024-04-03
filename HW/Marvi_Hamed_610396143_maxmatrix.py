import copy
n , m = input().split()
n = int(n)
m = int(m)
matrix=[]
list=[]
for _ in range(n):
    for _ in range(n):
        list.append(int(input()))
    matrix.append(list[:])
    list=[]
howmany = n-m+1
#print(matrix)
if(n==1):
    print(matrix[0][0])
if(n!=1):
    max = 0
    second = 0
    firststart = [0,0]
    mylist = []
    for k in range(m):
        for l in range(m):
            max += matrix[k][l]
            mylist.append(matrix[k][l])
    mylist2=[]
   # print("first one is:",mylist)
    shoro = 0
    payan = m-1
    #for _ in range(howmany):
  #  print("howmany is:",howmany)
    if(True):
        for satr in range(howmany):
            for index in range(howmany):
                for i in range(m):
                    for j in range(m):
                        #print('avval:',satr+i, '    dovvom:',index+j)
                        second+=matrix[satr+i][index+j]
                        mylist2.append(matrix[satr+i][index+j])
                if(second>max):
                    max = second
                    mylist = copy.copy(mylist2)
                second = 0
                mylist2 = []
for i in range(m**2):
    if((i+1)%m!=0 and n!=1):
        print(mylist[i],end=" ")
    elif((i+1)%m==0 and n!=1):
        print(mylist[i])
#print("max is:",max)










