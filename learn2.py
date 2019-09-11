import numpy as np


def InputFromPlayer(sPlayer):
    x = int(input("Enter Player " + str(sPlayer) + " X : "))
    y = int(input("Enter Player " + str(sPlayer) + " Y : "))
    if x == 10:
        return x, y, 1
    else:
        return InputDataProcess(x, y, int(sPlayer))


def InputDataProcess(x, y, sPlayer):
    global arr
    IsOverwrite = arr[x][y]
    if IsOverwrite == 0:
        arr[x][y] = int(sPlayer)
        if int(sPlayer) == 1:
            sPlayer = 2
        else:
            sPlayer = 1

        print(arr)
    else:
        print("value is already exists")

    return x, y, sPlayer


def WhichPlayerWin(iPlayer):
    global arr
    win=True
    print("win")
    print(arr[:-2])

    #print(arr[][:,1])


    return win



arr = np.zeros((3, 3), dtype=int)
iPlayer = 1

while True:
    x, y,iPlayer = InputFromPlayer(iPlayer)
    print('x value : {} ,  y value : {} '.format(x, y))

    if x == 10:
        break

    WhichPlayerWin(iPlayer)