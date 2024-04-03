def show(matrix , n):
    for i in range(n):
        for j in range(n):
            if(matrix[i][j]<10):
                print(matrix[i][j],end = "    ")
            if(matrix[i][j]>=10 and matrix[i][j]<=99):
                print(matrix[i][j],end = "   ")
            if(matrix[i][j]>=100):
                print(matrix[i][j],end= "  ")
        print()

n = int(input("if you want to have numbers from 1 to n*n, then enter number n:"))
matrix = []
for i in range(n):
    list=[]
    for i in range(n):
        list.append(0)
    matrix.append(list)




# میخوایم از 1 شروع کنیم اگه عدد زوج باشه مثل 16 میشه 4*4 و وقتی تقسیم بر 2 میکنم چون لیست از 0 شروع میشه نه 1 پس وقتی تقسیم بر 2 کردیم یه دونه ازش کم میکنیم اگه فرد بود خودش درسته
if(n%2==1):
    i = n//2
    #i = i-1
    j = i
if(n%2==0):
    i = n//2-1
    j = i
jahat = 1
count = 1
howmany = 0
when = 1
matrix[i][j] = 1
while(count<=n*n):
    #print("i'm here in the while")
    #"""
    #print("jahat is:",jahat)
    if(jahat%4==1):
        #if(when==0):
            #i-=1
        howmany+=1
        #print("in first")
    if(jahat%4==2):
        pass
        #j+=1
        #print("in second")
    if(jahat%4==3):
        #i+=1
        #print("in third")
        howmany+=1
    if(jahat%4==0):
        pass
        #j-=1
        #print("in fourth")
        #"""
    #print("howmany is:",howmany)
    for lol in range(howmany):
        #print("i is:",i,"& j is:",j)
        matrix[i][j]=count
        count+=1
        #show(matrix , n)
        #print("_____________________")
        #if(n==1):
            #when = 0
        if (jahat % 4 == 1):
            if (when != 2):
                j += 1
            #howmany += 1
            #print("in first")
        if (jahat % 4 == 2):
            i += 1
            #print("in second")
        if (jahat % 4 == 3):
            j -= 1
            #print("in third")
            #howmany += 1
        if (jahat % 4 == 0):
            i -= 1
            #print("in fourth")
    jahat+=1
    when = 0
show(matrix, n)
