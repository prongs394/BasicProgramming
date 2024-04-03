import copy
n = int(input('enter the number of numbers: '))
list = []
for i in range(n):
    z = int(input("enter the numbers: "))
    list.append(z)
print(list)

sum = 0
for i in range(n):
    sum+=list[i]

if(sum%2==1):
    status = False
    print("not possible")
if(sum%2==0):
    status = True

def check(sums , sum):
    if(sums*2 == sum):
        return True
    if(sums*2 != sum):
        return False

if(status):
    answers = []
    b = 2
    a = [0] * n
    k = n - 1
    while (k >= 0):
        a[n - 1] = a[n - 1] + 1
        k = n - 1
        while ((k >= 0) and (a[k] == b)):
            a[k] = 0
            k = k - 1
            if (k >= 0): a[k] = a[k] + 1
        c = copy.copy(a)
        answers.append(c)
    matrix = []
    for i in range(len(answers)):
        lol = 0
        for j in range(len(answers[i])):
            if(answers[i][j]==1):
                lol = lol + list[j]
        if(check(lol , sum)):
            first = []
            second = []
            for k in range(len(answers[i])):
                if(answers[i][k]==1):
                    first.append(list[k])
                if(answers[i][k]==0):
                    second.append(list[k])
            print(first , end = " ")
            print("and ",second)