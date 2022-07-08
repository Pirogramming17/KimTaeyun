import random

num = 0
while True:
    # the while True loops allows a block of code to be executed repeatedly until
    # we get a False boolean or a break
    try:
        get = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
    except ValueError:
        print('정수를 입력하세요')
    else:
        if get < 1 or get > 3:
            print('1,2,3 중 하나를 입력하세요')
        else:
            break
