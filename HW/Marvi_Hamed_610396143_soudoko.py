# n = tole jadval masalan age soudoko mamoli bashe n = 9 ====> 9*9
#a = soudoko
global a
global dict
global dict2
global n
global counter___
global counterIII
global counterG
counter___=[0]
counterIII=[0]
counterG=[0]
a = []
n =int(input("enter n(the matrix should be n*n and n should be k*k:"))
o=n**(1/2)
o = int(o)
#print("o is:",o)
print("enter the matrix:")
for _ in range(n):
    a.append(list(map(int,input().split())))
print(a)
dict = {}
for i in range(n**2):
    dict[i+1]=i+1
dict2 = dict.copy()


# y = first index in matrix    x = second index in matrix
def check___(x):
    dict2 = dict.copy()
    for i in range(n):
        if(a[x][i] in dict2):
            counter___[0]+=1
            del dict2[a[x][i]]
        else:
            i = n
            return -1
  #  print("___:",counter___[0])



def checkIII(y):
    dict2 = dict.copy()
    for i in range(n):
        if(a[i][y] in dict2):
            counterIII[0]+=1
            del dict2[a[i][y]]
        else:
            i = n
            return -1
 #   print("III:",counterIII[0])
    return

# G : shabihe moraba hast baraye hamin G entakhab kardam
def checkG(x , y):
    dict2 = dict.copy()
#this line 2 should be n**(0.5)
    for i in range(x , x+(o)):
        for j in range(y , y+(o)):
            if(a[i][j] in dict2):
                counterG[0]+=1
                del dict2[a[i][j]]
            else:
                i = x+(n**(0.5))+1
                j = y+(n**(0.5))+1
                return -1
 #  print("G:",counterG[0])

# III
total = 0
status = True
go = True
x = 0
I = 0

while(go):
    for x in range(n):
        counterIII[0] = 0
        result = checkIII(x)
      #  print("now III is:",counterIII[0])
        if(result==-1):
            status = False
            go = False
        if(counterIII[0]!=n):
            status = False
            go = False
        if (counterIII[0] == n):
            I+=1
            go = False
        x+=1
#print("I is:",I)
if (I == n):
    total += 1


#___
go = True
x = 0
_ = 0
while(go and status):
    for x in range(n):
        counter___[0] = 0
        result = check___(x)
     #   print("now _ is:", counter___[0])
        if(result==-1):
            status = False
            go = False
        if(counter___[0]!=n):
            status = False
            go = False
        if (counter___[0] == n):
            _+=1
            #total+=1
            go = False
if(_==n):
    total+=1
    #x+=1
#print("_ is:",_)


#print("total befor G:",total)
#G
go = True
x = 0
y = 0
g = 0
#while(go and status):
    # n**(0.5) should be instead of 2 in these 2 fors bellow

for x in range(0,n,o):
    for y in range(0,n,o):
        counterG = [0]
        result = checkG(x , y)
        if(result==-1):
            status = False
            go = False
        if(counterG[0]!=n):
            status = False
            go = False
        if (counterG[0] == n):
            g+=1
            go = False
        if(g==n):
            total+=1
#print("g is:",g)

#n**(0.5)
# inja 3 doroste hamishe 3 bayad bashe
#print("total is:",total)
if(total == 3):
    print("it is a sousoko")
if(total!=3):
    print("it's not a soudoko")





#print("dict1is:",dict)
#print("dict2is:",dict2)



