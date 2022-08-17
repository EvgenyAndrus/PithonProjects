"""Напишите функцию displayinventory (), которая принимает в качестве аргумента
описание любого “инвентаря” и отображаег его примерно в следующем виде.
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

Напишите функцию addToInventory(inventory, addedltems),
в которой параметр inventory — это словарь,
представлящий инвентарь игрока (как в предыдущем проекте),
а параметр addedltems — это список наподобие dragonLoot.
Функция addToInventory () должна возвращать словарь, представляющий обновленный инвентарь.
Обратите внимание на то, что в списке addedltems один и тот же элемент может встречаться
несколько раз.
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print('---------------------------------')
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))
    print('---------------------------------')


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1


display_inventory(stuff)
add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
