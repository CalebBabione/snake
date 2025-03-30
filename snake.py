import time
import os
import keyboard

board = [20, 20]
body = [[10, 10],[10, 9],[10,8]]
length = 3
vector = [1, "up"]

def isBody(x,y):
    for i in range(length):
        if body[i][0] == x and body[i][1] == y:
            return True
def motion():
    body.append([body[length - 1][0], body[length - 1][1] - 1]) 
    body.remove(body[0])
while True:
    os.system('clear')
    for verti in range(board[1]):
        for hori in range(board[0]):
            if verti == 0 or verti == 19:
                print("*", end="")
            if verti > 0 and verti < 19:
                if hori == 0 or hori == 19:
                    print("*", end="")
                else:
                    if isBody(hori, verti):
                        print("$", end="")
                    else:
                        print(".", end="")
            if hori == 19:
                print("")
    motion()
    time.sleep(.75)