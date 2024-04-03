global numbers
numbers={}

def shownumber():
    print("Telephone Numbers:")
    for x in numbers.keys():
        print("Name: ", x, "\tNumber:", numbers[x])
    print()

def addnumber():
    print("Add Name and Number")
    name = input("Name: ")
    phone = input("Number: ")
    numbers[name] = phone

def removenumber():
    print("Remove Name and Number")
    name = input("Name: ")
    if name in numbers:
        del numbers[name]
    else:
        print(name, "was not found")

def find():
    print("Lookup Number")
    name = input("Name: ")
    if name in numbers:
        print("The number is", numbers[name])
    else:
        print(name, "was not found")


def menu(which):
    if(which!=1 or which!=2 or which!=3 or which!=4 or which!=5):
        showmenu()
    else:
        domenu(which)

def domenu(which):

    if(which == 1):
        shownumber()

    if(which == 2):
        addnumber()

    if(which == 3):
        removenumber()

    if(which == 4):
        find()

    if(which == 5):
        quit()


def showmenu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    which = int(input("enter a number from 1 to 5:"))
    domenu(which)



global which
which = 0
while(which!=5):
    menu(which)




