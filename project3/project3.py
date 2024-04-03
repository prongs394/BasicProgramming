from graphics import *
import copy

win = GraphWin("My Test", 1000, 1000)


class Game():
    # _______________________________________________________

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.player = Circle(Point(x, y), 5)
        self.player.setFill(color)
        self.list_of_woods = []
        self.x_of_jump = 0
        self.y_of_jump = 0

    # _______________________________________________________

    def move(self, key):
        if (key == 'w'):
            self.player.move(0, -20)
            self.y -= 20

        elif (key == 's'):
            self.player.move(0, 20)
            self.y += 20

        elif (key == 'a'):
            self.player.move(-20, 0)
            self.x -= 20

        elif (key == 'd'):
            self.player.move(20, 0)
            self.x += 20

    # _______________________________________________________
    def walls(self, x, y, jahat):  # jahat = o(ofoghi) OR  a(amodi)

        self.x_of_board = x * 20
        self.y_of_board = y * 20

        if (jahat == 'o'):
            list1 = []
            list2 = []
            list3 = []
            x1 = self.x_of_board - 20
            y1 = self.y_of_board
            x2 = self.x_of_board
            y2 = self.y_of_board
            x3 = self.x_of_board + 20
            y3 = self.y_of_board
            list1.append(x1)
            list1.append(y1)
            list2.append(x2)
            list2.append(y2)
            list3.append(x3)
            list3.append(y3)
            first = []
            second = []
            first.append(list1)
            first.append(list2)
            second.append(list2)
            second.append(list3)
            self.list_of_woods.append(first)
            self.list_of_woods.append(second)

            aLine = Line(Point(x1, y1), Point(x2, y2))
            aLine.setFill("red")
            aLine.draw(win)
            aLine = Line(Point(x2, y2), Point(x3, y3))
            aLine.setFill("red")
            aLine.draw(win)
        if (jahat == 'a'):
            list1 = []
            list2 = []
            list3 = []
            x1 = self.x_of_board
            y1 = self.y_of_board - 20
            x2 = self.x_of_board
            y2 = self.y_of_board
            x3 = self.x_of_board
            y3 = self.y_of_board + 20
            list1.append(x1)
            list1.append(y1)
            list2.append(x2)
            list2.append(y2)
            list3.append(x3)
            list3.append(y3)
            first = []
            second = []
            first.append(list1)
            first.append(list2)
            second.append(list2)
            second.append(list3)
            self.list_of_woods.append(first)
            self.list_of_woods.append(second)

            aLine = Line(Point(x1, y1), Point(x2, y2))
            aLine.setFill("red")
            aLine.draw(win)
            aLine = Line(Point(x2, y2), Point(x3, y3))
            aLine.setFill("red")
            aLine.draw(win)

    # _______________________________________________________
    def check_woods_in_the_board(self, x_of_wood, y_of_wood, jahat):

        x_of_wood = x_of_wood * 20
        y_of_wood = y_of_wood * 20

        if (jahat == 'o'):
            if (x_of_wood - 20 >= 0 and x_of_wood + 20 <= 220 and y_of_wood <= 220 and y_of_wood >= 0):
                return True
            else:
                return False
        if (jahat == 'a'):
            #print('im in the first checking of jahat==a')
            if (y_of_wood - 20 >= 0 and y_of_wood + 20 <= 220 and x_of_wood <= 220 and x_of_wood >= 0):
                return True
            else:
                return False

    # _______________________________________________________
    def check_woods_not_in_each_other(self, x_of_wood, y_of_wood, jahat):
        #print('im in check woods not in eachother')
        x_of_wood = x_of_wood * 20
        y_of_wood = y_of_wood * 20
        if (jahat == 'o'):
            first = [x_of_wood - 20, y_of_wood]
            second = [x_of_wood, y_of_wood]
            third = [x_of_wood + 20, y_of_wood]
            list1 = []
            list2 = []
            list1.append(first)
            list1.append(second)
            list2.append(second)
            list2.append(third)
            if ((list1 not in self.list_of_woods) and (list2 not in self.list_of_woods)):
                list3 = []
                list3.append(second)
                fourth = [x_of_wood, y_of_wood - 20]
                list3.append(fourth)
                list4 = []
                list4.append(second)
                fifth = [x_of_wood, y_of_wood + 20]
                list4.append(fifth)
                if (list3 not in self.list_of_woods and list4 not in self.list_of_woods):
                    return True

        if (jahat == 'a'):
            first = [x_of_wood, y_of_wood - 20]
            second = [x_of_wood, y_of_wood]
            third = [x_of_wood, y_of_wood + 20]
            list1 = []
            list11 = []
            list2 = []
            list22 = []
            list1.append(first)
            list1.append(second)
            list11.append(second)
            list11.append(first)
            list22.append(third)
            list22.append(second)
            list2.append(second)
            list2.append(third)
            if ((list1 not in self.list_of_woods) and (list2 not in self.list_of_woods) and (list11 not in self.list_of_woods) and (list22 not in self.list_of_woods)):
                print('passed here')
                list3 = []
                list3.append(second)
                fourth = [x_of_wood + 20, y_of_wood]
                list3.append(fourth)
                list33 = []
                list33.append(fourth)
                list33.append(second)
                list4 = []
                list44 = []
                list4.append(second)
                fifth = [x_of_wood - 20, y_of_wood]
                list4.append(fifth)
                list44.append(fifth)
                list44.append(second)
                if ((list3 in self.list_of_woods or list33 not in self.list_of_woods) and (list4 not in self.list_of_woods and list44 not in self.list_of_woods)):
                    #if((list3 in self.list_of_woods or list33 in self.list_of_woods) and (list4 not in self.list_of_woods or list44 not in self.list_of_woods)):
                        print('passed here too')
                        return True
                if(list3 in self.list_of_woods and list33 in self.list_of_woods and list4 not in self.list_of_woods and list44 not in self.list_of_woods):
                    print('ok')
                    return True
                if(list3 in self.list_of_woods and list33 in self.list_of_woods and list4 not in self.list_of_woods and list44 not in self.list_of_woods):
                    print('i have passed this')
                    if(list3 not in self.list_of_woodsa and list33 not in self.list_of_woods and list4 in self.list_of_woods and list44 in self.list_of_woods):
                        print('i have passed this')
                        return True

        return False

    # _______________________________________________________
    def checkboarders(self, key):

        if (key == 'w'):
            if (self.y - 20 >= 10):
                return True

        elif (key == 's'):
            if (self.y + 20 <= 210):
                return True

        elif (key == 'a'):
            if (self.x - 20 >= 10):
                return True

        elif (key == 'd'):
            if (self.x + 20 <= 210):
                return True

        return False

    # _______________________________________________________
    def checkwalls(self, key):

        if (key == 'w'):
            list = []
            first = []
            second = []
            first.append(self.x - 10)
            first.append(self.y - 10)
            second.append(self.x + 10)
            second.append(self.y - 10)
            list.append(first)
            list.append(second)

        if (key == 's'):
            list = []
            first = []
            second = []
            first.append(self.x - 10)
            first.append(self.y + 10)
            second.append(self.x + 10)
            second.append(self.y + 10)
            list.append(first)
            list.append(second)

        if (key == 'a'):
            list = []
            first = []
            second = []
            first.append(self.x - 10)
            first.append(self.y - 10)
            second.append(self.x - 10)
            second.append(self.y + 10)
            list.append(first)
            list.append(second)

        if (key == 'd'):
            list = []
            first = []
            second = []
            first.append(self.x + 10)
            first.append(self.y - 10)
            second.append(self.x + 10)
            second.append(self.y + 10)
            list.append(first)
            list.append(second)

        if (list not in self.list_of_woods):
            return True
        else:
            return False

    # _______________________________________________________

    def check_jumping_possible_2(self,jahat):
        self.y_of_jump = 10
        self.x_of_jump = 10
        if(jahat=='a'):
            list1 = [[self.x-10 , self.y-10],[self.x-10,self.y+10]]
            list11 = [[self.x-10,self.y+10],[self.x-10 , self.y-10]]
            list2 = [[self.x-30 , self.y-10],[self.x-30,self.y+10]]
            list22 = [[self.x-30,self.y+10],[self.x-30 , self.y-10]]
            self.x_of_jump=self.x-40

        if(jahat=='d'):
            list1 = [[self.x+10 , self.y-10],[self.x+10 , self.y+10]]
            list11 = [[self.x+10 , self.y+10] , [self.x+10 , self.y-10]]
            list2=[[self.x+30 , self.y-10],[self.x+30 , self.y+10]]
            list22=[[self.x+30 , self.y+10],[self.x+30 , self.y-10]]
            self.x_of_jump=self.x+40

        if(jahat=='s'):
            list1=[[self.x-10,self.y+10],[self.x+10,self.y+10]]
            list11=[[self.x+10,self.y+10],[self.x-10,self.y+10]]
            list2=[[self.x-10,self.y+30],[self.x+10,self.y+30]]
            list22=[[self.x+10,self.y+30],[self.x-10,self.y+30]]
            self.y_of_jump=self.y+40

        if(jahat=='w'):
            list1=[[self.x-10,self.y-10],[self.x+10,self.y-10]]
            list11=[[self.x+10,self.y-10],[self.x-10,self.y-10]]
            list2=[[self.x-10,self.y-30],[self.x+10,self.y-30]]
            list22=[[self.x+10,self.y-30],[self.x-10,self.y-30]]
            self.y_of_jump=self.y-40

        if(list1 not in self.list_of_woods and list11 not in self.list_of_woods and list2 not in self.list_of_woods and list22 not in self.list_of_woods and self.x_of_jump>=10 and self.x_of_jump<=210 and self.y_of_jump>=10 and self.y_of_jump<=210):
            return True
        else:
            return False
# _______________________________________________________
    def jump2(self , key):
        if(key=='w'):
            self.player.move(0,-40)
            self.y-=40
        if(key=='s'):
            self.player.move(0,40)
            self.y+=40
        if(key=='a'):
            self.player.move(-40,0)
            self.x-=40
        if(key=='d'):
            self.player.move(40,0)
            self.x+=40


# _______________________________________________________
def check_there_is_jumping(jahat , count , number):

    if(number == '2'):
        print('i have passed number is 2')
        if(count%2==0):
            print('i have passe that count is even')
            if(jahat=='a'):
                list = [[red.x-10 , red.y-10],[red.x-10,red.y+10]]
                if(red.y == blue.y and red.x == blue.x+20 and  list not in red.list_of_woods):
                    return True
            if(jahat=='d'):
                list = [[red.x + 10, red.y - 10], [red.x + 10, red.y + 10]]
                if (red.y == blue.y and red.x == blue.x - 20 and list not in red.list_of_woods):
                    return True
            if(jahat=='s'):
                list = [[red.x-10 , red.y + 10], [red.x+10, red.y + 10]]
                if (red.x == blue.x and red.y == blue.y - 20 and list not in red.list_of_woods):
                    print('i say its true for s')
                    return True
                else:
                    pass
                    print('i say its wrong for s')
            if(jahat=='w'):
                list = [[red.x - 10, red.y - 10], [red.x + 10, red.y - 10]]
                if (red.x == blue.x and red.y == blue.y + 20 and list not in red.list_of_woods):
                    print('i say its true for w')
                    return True
                else:
                    print('i say its wrong for w')
        if(count%2==1):
            if (jahat == 'a'):
                list = [[blue.x - 10, blue.y - 10], [blue.x - 10, blue.y + 10]]
                if (blue.y == red.y and blue.x == red.x + 20 and list not in blue.list_of_woods):
                    return True
            if (jahat == 'd'):
                list = [[blue.x + 10, blue.y - 10], [blue.x + 10, blue.y + 10]]
                if (blue.y == red.y and blue.x == red.x - 20 and list not in blue.list_of_woods):
                    return True
            if (jahat == 's'):
                list = [[blue.x - 10, blue.y + 10], [blue.x + 10, blue.y + 10]]
                if (blue.x == red.x and blue.y == red.y - 20 and list not in blue.list_of_woods):
                    return True
            if (jahat == 'w'):
                list = [[blue.x - 10, blue.y - 10], [blue.x + 10, blue.y - 10]]
                if (blue.x == red.x and blue.y == red.y + 20 and list not in blue.list_of_woods):
                    return True
        return False
    if(number==4):
        pass
# _______________________________________________________





# _______________________________________________________
# displaying the board
x = 20
for i in range(10):
    aLine = Line(Point(x, 0), Point(x, 220))
    aLine.setFill("blue")
    x += 20
    aLine.draw(win)
y = 20
for i in range(10):
    aLine = Line(Point(0, y), Point(220, y))
    aLine.setFill("blue")
    y += 20
    aLine.draw(win)
# _______________________________________________________
# getting number of players

message = Text(Point(700, 20), 'Enter number of players')
message.draw(win)

number = Entry(Point(700, 40), 15).draw(win)
win.getMouse()
number_of_players = number.getText()

message.undraw()
number.undraw()

# _______________________________________________________
# game
if (number_of_players == '2'):
    print('sirdagh')
    red = Game(110, 10, 'red')
    blue = Game(110, 210, 'blue')
    blue.player.draw(win)
    red.player.draw(win)
    count = 0
    can_play = True
    while (can_play):

        if (count % 2 == 0):
            can_input = True
            while (can_input):
                message = Text(Point(700, 20), ' player red Enter m to move your player or w to put a wood')
                message.draw(win)

                what_to_do = Entry(Point(700, 40), 15).draw(win)
                win.getMouse()
                what_we_want_to_do = what_to_do.getText()

                if (what_we_want_to_do == 'm' or what_we_want_to_do == 'w'):
                    can_input = False
                else:
                    message.undraw()
                    what_to_do.undraw()

            message.undraw()
            what_to_do.undraw()

            if (what_we_want_to_do == 'm'):
                can_move = True
                while (can_move):
                    message = Text(Point(700, 20), ' player red press w,a,s or d to move')
                    message.draw(win)

                    where_to_move = Entry(Point(700, 40), 15).draw(win)
                    win.getMouse()
                    where_we_want_to_move = where_to_move.getText()

                    if ((
                            where_we_want_to_move == 's' or where_we_want_to_move == 'w' or where_we_want_to_move == 'a' or where_we_want_to_move == 'd') and red.checkboarders(
                            where_we_want_to_move) and red.checkwalls(where_we_want_to_move)):
                        #print('i am about to check jumping')
                        if(check_there_is_jumping(where_we_want_to_move , count , number_of_players)):
                            #print('im in jumping and there is a probability it may happen')
                            if(red.check_jumping_possible_2(where_we_want_to_move)):
                                #print('jumping will happen')
                                can_move = False
                                message.undraw()
                                where_to_move.undraw()
                            if(not red.check_jumping_possible_2(where_we_want_to_move)):
                                #print('jumping cant happen vorodies are wrong for red')
                                message.undraw()
                                where_to_move.undraw()
                        if(not check_there_is_jumping(where_we_want_to_move,count,number_of_players)): #اگه اشتباه باشه یعنی تابع جواب بده false پس بعدش cam_move برابر میشه یا false
                            #print('there is no jumping')
                            can_move = False
                            message.undraw()
                            where_to_move.undraw()

                    else:
                        message.undraw()
                        where_to_move.undraw()
                #print('im here at last!')
                message.undraw()
                where_to_move.undraw()
                #print('im out here')
                if (red.checkboarders(where_we_want_to_move)):
                    #print('im in first')
                    if (red.checkwalls(where_we_want_to_move)):
                        #print("i'm in second")
                        if (check_there_is_jumping(where_we_want_to_move , count , number_of_players) and red.check_jumping_possible_2(where_we_want_to_move)):  # here we check if there is a condotion of jumping if there is, the checking def will return 1 (instead if True we will write:checking==1)
                            red.jump2(where_we_want_to_move)  # the jumping function
                        else:
                            #print('i have reached third')
                            red.move(where_we_want_to_move)
                        if (red.y == 210):
                                message.undraw()
                                can_play = False
                                message = Text(Point(700, 20), ' player red wins')
                                message.draw(win)
                                win.setBackground('red')

            if (what_we_want_to_do == 'w'):
                can_put_wood = True
                while (can_put_wood):
                    #print('look! i am here!')
                    message = Text(Point(700, 20), 'player red enter where you want to place the wood')
                    message.draw(win)

                    wood = Entry(Point(700, 40), 15).draw(win)
                    win.getMouse()
                    x_of_wood, y_of_wood, jahat = wood.getText().split()
                    x_of_wood = int(x_of_wood)
                    y_of_wood = int(y_of_wood)

                    if (red.check_woods_in_the_board(x_of_wood, y_of_wood, jahat)):
                        #print('ive passed first checking')
                        if (red.check_woods_not_in_each_other(x_of_wood, y_of_wood, jahat)):
                            #print('also second one')
                            can_put_wood = False
                        else:
                            message.undraw()
                            wood.undraw()
                    else:
                        message.undraw()
                        wood.undraw()

                message.undraw()
                wood.undraw()
                red.walls(x_of_wood, y_of_wood, jahat)
                blue.list_of_woods = copy.copy(red.list_of_woods)
            #print("the red one is:", red.list_of_woods)
            #print("the blue one is:", blue.list_of_woods)

            count += 1

        if (count % 2 == 1 and can_play):
            can_input = True
            while (can_input):
                message = Text(Point(700, 20), ' player blue Enter m to move your player or w to put a wood')
                message.draw(win)

                what_to_do = Entry(Point(700, 40), 15).draw(win)
                win.getMouse()
                what_we_want_to_do = what_to_do.getText()

                if (what_we_want_to_do == 'm' or what_we_want_to_do == 'w'):
                    can_input = False
                else:
                    message.undraw()
                    what_to_do.undraw()

            message.undraw()
            what_to_do.undraw()

            if (what_we_want_to_do == 'm'):
                can_move = True
                while (can_move):
                    message = Text(Point(700, 20), ' player blue press w,a,s or d to move')
                    message.draw(win)

                    where_to_move = Entry(Point(700, 40), 15).draw(win)
                    win.getMouse()
                    where_we_want_to_move = where_to_move.getText()

                    if ((
                            where_we_want_to_move == 's' or where_we_want_to_move == 'w' or where_we_want_to_move == 'a' or where_we_want_to_move == 'd') and blue.checkboarders(
                        where_we_want_to_move) and blue.checkwalls(where_we_want_to_move)):
                        can_move = False
                    else:
                        message.undraw()
                        where_to_move.undraw()

                message.undraw()
                where_to_move.undraw()
                #print('im out here')
                if (blue.checkboarders(where_we_want_to_move)):
                    # print('im in first')
                    if (blue.checkwalls(where_we_want_to_move)):
                        # print("i'm in second")
                        if (check_there_is_jumping(where_we_want_to_move, count,
                                                   number_of_players) and blue.check_jumping_possible_2(
                                where_we_want_to_move)):  # here we check if there is a condotion of jumping if there is, the checking def will return 1 (instead if True we will write:checking==1)
                            blue.jump2(where_we_want_to_move)  # the jumping function
                        else:
                            # print('i have reached third')
                            blue.move(where_we_want_to_move)
                        if (blue.y == 10):
                                message.undraw()
                                can_play = False
                                message = Text(Point(700, 20), ' player blue wins')
                                message.draw(win)
                                win.setBackground('blue')

            if (what_we_want_to_do == 'w'):
                can_put_wood = True
                while (can_put_wood):
                    #print('look! i am here!')
                    message = Text(Point(700, 20), 'player blue enter where you want to place the wood')
                    message.draw(win)

                    wood = Entry(Point(700, 40), 15).draw(win)
                    win.getMouse()
                    x_of_wood, y_of_wood, jahat = wood.getText().split()
                    x_of_wood = int(x_of_wood)
                    y_of_wood = int(y_of_wood)

                    if (blue.check_woods_in_the_board(x_of_wood, y_of_wood, jahat)):
                        #print('ive passed first checking')
                        if (blue.check_woods_not_in_each_other(x_of_wood, y_of_wood, jahat)):
                            #print('also second one')s
                            can_put_wood = False
                        else:
                            message.undraw()
                            wood.undraw()
                    else:
                        message.undraw()
                        wood.undraw()

                message.undraw()
                wood.undraw()
                blue.walls(x_of_wood, y_of_wood, jahat)
                red.list_of_woods = copy.copy(blue.list_of_woods)
            count += 1

win.getMouse()
win.close()

if (number_of_players == 4):
    pass