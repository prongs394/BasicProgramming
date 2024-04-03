import copy

def make(matrix , n):
    a = [0] * n
    k = n - 1
    while (k >= 0):
        #matrix.append(a)
        a[n - 1] = a[n - 1] + 1
        k = n - 1
        while ((k >= 0) and (a[k] == 2)):
            a[k] = 0
            k = k - 1
            if (k >= 0): a[k] = a[k] + 1
        c = copy.copy(a)
        matrix.append(c)

def check(list , n):
    start = 0
    end = 0
    for i in range(n):
        if(list[i]==0):
            start+=1
        if(list[i]==1):
            end+=1
        if(start<end):
            return False
    if(start == end):
        return True

matrix = []
n=int(input("Enter the number of parathesses:"))
m = n*2
make(matrix , m)
for j in range(len(matrix)):
    if(check(matrix[j] , m)):
        for i in range(m):
            if(matrix[j][i]==0):
                print('(',end="")
            if(matrix[j][i]==1):
                print(')',end="")
        print(matrix[j])
        print()