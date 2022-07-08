import random

num = 0
computer = 0
player = 0

def brGame(num):
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

    def updateStatus(playerName, opponent, num, currNum):
        for i in range(numChoice):
            num += 1
            print(playerName, num, sep='')
            if num == 31:
                print(opponent, ' win!', sep='')
                break

    while num < 31:
        if num == 31:
            break
        # it's the computer's turn
        currTimes = random.randint(1, 3)
        updateStatus(computer, player, num, currTimes)

        # player's turn
        currTimes = brGame(num)
        updateStatus(player, computer, num, currTimes)
