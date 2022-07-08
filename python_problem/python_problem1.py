import random

num = 0
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

for i in range(numChoice):
    num += 1
    print(num)
