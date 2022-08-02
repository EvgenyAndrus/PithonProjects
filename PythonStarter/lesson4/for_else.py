for attempts_left in range(3, 0, -1):
    password = input('enter your password '
                     '(you have {} attempts left): '.format(attempts_left))
    if password == 'a':
        print('Access granted')
        break
else:  # если for будет прерван и счетчик не дойдет до конца. else выполнятся не будет
    print('Access denied')
