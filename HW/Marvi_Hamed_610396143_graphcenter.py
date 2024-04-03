import copy
maxnumbers=[]
#get data:
n = int(input("enter n, the graph has n : "))
matrix = []
for i in range(n):
    list = []
    for j in range(n):
        m = -2
        if(i>j and j!=i):
            m = matrix[j][i]
        elif(i!=j and j>i):
            print("enter weight of %s to %s" % (i , j),"it should be an integer >=0:" , end=" ")
            m = int(input())
        elif(i==j):
            m = -1

        list.append(m)

    matrix.append(list)
    print("matrix is:",matrix)
    print("i is:",i)
    print("j is:",j)
    print("________________________")
print(matrix)
#getting data finished the graph is the object name matrix
for i in range(n):
    max = -1
    list=[]
    for j in range(n):
        if(matrix[i][j]>=max):
            max = matrix[i][j]
    maxnumbers.append(max)
print("max numbers is:",maxnumbers)
min = maxnumbers[0]
for i in range(n):
    if(min>maxnumbers[i]):
        min = maxnumbers[i]
answer = min
print("the graph center is:",answer)


"""
d = [-1 for x in range(0,n)]
matrix = [d for x in range(0,n)]
print(matrix)

matris = [[-1]]
matris[0]*=n
matris*=n
matrix = copy.copy(matris)
print(matrix)

for i in range(n):
    for j in range(n):
        print("i'm here")
        second = True
        third = True
        if(i == j):
            second = False
            third = False
        if(matrix[i][j]!=-1 and second):
            third = False
        if(matrix[i][j]==-1 and i!=j and third):
            print("enter weight of", i+1,"to", j+1,":", end = " ")
            x = True
            while(x):
                if(matrix[i][j]<0):
                    matrix[i][j]=int(input())
                if(matrix[i][j]>=0):
                    x = False
            matrix[j][i]=matrix[i][j]
        print("i is:",i)
        print("j is:",j)
        print("matrix is:",matrix)
        print("____________")
print(matrix)
"""
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
"""
-1 +4 +2 +3 +7
+4 -1 +2 +2 +5
+2 +2 -1 +6 +9
+3 +2 +6 -1 +8
+7 +5 +9 +8 -1
"""
















