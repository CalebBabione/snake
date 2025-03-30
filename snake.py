import time
import os
import keyboard

board = [20, 20]
body = [[10, 10],[10, 9],[10,8]]
length = 3
vector = [1, "right"]

def isBody(x,y):
    for i in range(length):
        if body[i][0] == x and body[i][1] == y:
            return True
def motion():
    if vector[1] == "up":
        body.append([body[length - 1][0], body[length - 1][1] - 1])
        body.remove(body[0])
    if vector[1] == "down":
        body.append([body[length - 1][0], body[length - 1][1] + 1])
        body.remove(body[0])
    if vector[1] == "left":
        body.append([body[length - 1][0] - 1, body[length - 1][1]])
        body.remove(body[0])
    if vector[1] == "right":
        body.append([body[length - 1][0] + 1, body[length - 1][1]])
        body.remove(body[0])
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
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
    if keyboard.is_pressed('w'):
        if keyboard.is_pressed:
            vector[1] = "up"
    if keyboard.is_pressed('s'):
        if keyboard.is_pressed:
            vector[1] = "down"
    if keyboard.is_pressed('a'):
        if keyboard.is_pressed:
            vector[1] = "left"
    if keyboard.is_pressed('d'):
        if keyboard.is_pressed:
            vector[1] = "right"
        else:
            continue
    motion()
    time.sleep(.5)