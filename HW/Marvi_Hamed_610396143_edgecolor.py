def printMatrix(b):
    for i in range(len(b)):
        print (b[i])

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

def coloring(G , n):
    color = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            go = True
            number = 0
            if(j<i):
                go = False
            if(G[i][j]==1 and go):
                for count in range(n):
                    for a in range(n):
                        if(color[i][a]==number):
                            number+=1
                for count in range(n):
                    for b in range(n):
                        if(color[b][j]==number):
                            number+=1
                color[i][j]=number
                color[j][i]=number
    for i in range(n):
        for j in range(n):
            if(i<=j):
                print("from %s to %s is:" % (i , j) , color[i][j])






n = int(input("Enter the number of vertices: "))
G=[[0 for j in range(n)] for i in range(n)]
#printMatrix(G)
graphRead(G, n)
coloring(G , n)
printMatrix(G)