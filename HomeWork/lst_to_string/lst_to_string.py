spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['Лайм', 'Лангсат', 'Лардизабала', 'Лимон', 'Лимон',
         'дикий Личи', 'Лонган', 'Лукума', 'Лума остроконечная']


def lst_to_str(lst):
    string = ''
    global quantity
    quantity = len(lst) - 1
    global counter
    counter = 0
    for i in lst:
        if counter < quantity:
            string = string + i + ', '
        else:
            string = string + 'and ' + i
        counter += 1
    return string


print(lst_to_str(spam))
print(lst_to_str(spam2))
