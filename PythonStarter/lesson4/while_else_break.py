attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    password = input('enter your password '
                     '(you have {} attempts left): '.format(attempts_left + 1))
    if password == 'a':
        print('Access granted')
        break
else:  # если while будет прерван и не получит значение False. else выполнятся не будет
    print('Access denied')
