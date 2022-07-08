import random


def brGame():
    while True:
        # the while True loops allows a block of code to be executed repeatedly until
        # we get a False boolean or a break
        try:
            numChoice = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
        except ValueError:
            print('정수를 입력하세요')
        else:
            if numChoice < 1 or numChoice > 3:
                print('1,2,3 중 하나를 입력하세요')
            else:
                break

    return numChoice

# something to improve ... i don't know how to make parameters work in python ...
# how to eliminate repetitive code even more?
num = 0
while num < 31:
    # it's the computer's turn
    numChoice = random.randint(1, 3)
    for i in range(numChoice):
        num += 1
        print('computer : ', num, sep='')
        if num == 31:
            print('player win!', sep='')
            exit()
    # now it's my turn
    numChoice = brGame()
    for i in range(numChoice):
        num += 1
        print('player : ', num, sep='')
        if num == 31:
            print('computer win!', sep='')
            exit()
