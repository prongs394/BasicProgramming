#quoridor game
def matrixi(b , n , m):
	for _ in range(n):
		b.append([])
	for i in range(n):
		for j in range(m):
			b[i].append('*')
	o = 0
	for lol in range(0 , 9):
		b[0][(lol+1)*2]=" "
		o=o+1
	o = 0
	for lolo in range(0 , 10):
		b[(lolo+1)*2][0]=" "
		o = o+1
	b[0][0]=" "	
	o = 0
	for khat1 in range (0 , 10):
		b[0][(khat1+1)*2-1]=" "
		o = o+1
	o = 0	
	for soton1 in range(0 , 10):
		b[(soton1+1)*2-1][0]=" "
		o = o+1
	o = 0
	y = 1
	while(y<21):
		x = 2
		while(x<20):
			b[y][x]="G"
			x = x+2
		y = y+2	
	o = 0
	y = 2
	while(y<22):
		x = 1
		while(x<21):
			b[y][x]="G"
			x = x+2
		y = y+2	
	o = 0
	y = 2
	while(y<21):
		x = 2
		while(x<20):
			b[y][x]=" "
			x = x+2
		y = y+2	

		
		
def matrixp(b):
	for i in range(len(b)):
		for j in range(len(b[i])):
			print(b[i][j], ' ', end='')
		print()
	return


b = []
n = 21
m = 20
matrixi(b , n , m)
matrixp(b)

playera=[1 , 9]
playerb=[19 , 11]
global cantpass
cantpass=[1]
def playa():
	global cantpass
	print("player a press W , A , S and D to move or type wood to place an obstacle")
	move = input()
	if(move == "wood"):
		x1 = int(input("enter x"))
		y1 = int(input("enter y"))
		where=input("enter ofoghi or amodi")
		if(where=="amodi"):
			x2 = x1
			y2 = y1+2
		if(where=="ofoghi"):
			x2 = x1+2
			y2 = y1
		b[y1][x1]="S"
		b[y2][x2]="S"
		cantpass[0]=0
		
	if(move == "w" and b[playera[0]-1][playera[1]]!="S"):
		b[playera[0]][playera[1]]="*"
		playera[0]=playera[0]-2
		cantpass[0]=0
	elif(b[playera[0]-1][playera[1]]=="S" and move == "w"):
		print("you can't go there, try again")
		cantpass[0]=1

	if(move =="s" and b[playera[0]+1][playera[1]]!="S"):
		b[playera[0]][playera[1]]="*"
		playera[0]=playera[0]+2
		cantpass[0]=0
	elif(b[playera[0]+1][playera[1]]=="S" and move =="s"):
		print("you can't go there, try again")
		cantpass[0]=1

	if(move =="a" and b[playera[0]][playera[1]-1]!="S"):
		b[playera[0]][playera[1]]="*"
		playera[1]=playera[1]-2
		cantpass[0]=0
	elif(b[playera[0]][playera[1]-1]=="S" and move =="a"):
		print("you can't go there, try again")
		cantpass[0]=1
		

	if(move =="d" and b[playera[0]][playera[1]+1]!="S"):
		b[playera[0]][playera[1]]="*"
		playera[1]=playera[1]+2
		cantpass[0]=0
	elif(b[playera[0]][playera[1]+1]=="S" and move =="d"):
		print("you can't go there, try again")
		cantpass[0]=1

	b[playera[0]][playera[1]]="a"	
	matrixp(b)	


def playb():
	global cantpass
	print("player b press W , A , S and D to move or type wood to place an obstacle")
	move = input()
	if(move == "wood"):
		x1 = int(input("enter x"))
		y1 = int(input("enter y"))
		where=input("enter ofoghi or amodi")
		if(where=="amodi"):
			x2 = x1
			y2 = y1+2
		if(where=="ofoghi"):
			x2 = x1+2
			y2 = y1
		b[y1][x1]="S"
		b[y2][x2]="S"
		cantpass[0]=0
		
	if(move == "w" and b[playerb[0]-1][playerb[1]]!="S"):
		b[playerb[0]][playerb[1]]="*"
		playerb[0]=playerb[0]-2
		cantpass[0]=0
	elif(b[playerb[0]-1][playerb[1]]=="S" and move == "w"):
		print("you can't go there, try again")
		cantpass[0]=1

	if(move =="s" and b[playerb[0]+1][playerb[1]]!="S"):
		b[playerb[0]][playerb[1]]="*"
		playerb[0]=playerb[0]+2
		cantpass[0]=0
	elif(b[playera[0]+1][playera[1]]=="S" and move =="s"):
		print("you can't go there, try again")
		cantpass[0]=1

	if(move =="a" and b[playerb[0]][playerb[1]-1]!="S"):
		b[playerb[0]][playerb[1]]="*"
		playerb[1]=playerb[1]-2
		cantpass[0]=0
	elif(b[playera[0]][playera[1]-1]=="S" and move =="a"):
		print("you can't go there, try again")
		cantpass[0]=1

	if(move =="d" and b[playerb[0]][playerb[1]+1]!="S"):
		b[playerb[0]][playerb[1]]="*"
		playerb[1]=playerb[1]+2
		cantpass[0]=0
	elif(b[playera[0]][playera[1]+1]=="S" and move =="d"):
		print("you can't go there, try again")
		cantpass[0]=1

	b[playerb[0]][playerb[1]]="b"	
	matrixp(b)
w=1
while(w==1):
	while(cantpass[0]==1):
		playa()
	cantpass[0]=1
	if(playera[0]==19):
		print("a is the winner!")
		w=0
		break
	while(cantpass[0]==1):
		playb()
	cantpass[0]=1
	if(playerb[0]==1):
		print("b is the winner!")
		w=0
		break



	

