#I want to create a nickname generator, but I also want to create a locked mode nickname generator
#we also need to add an ability to add or remove nicknames, to view full nickname list.

import random

nicknames = ['The Flash', 'The Cowboy', 'QiQi', 'The Addict', '?', 'The Bitter', 'The Indecisive', 'The Speler', 'White Wolf', '4782817', 'The Unlucky', 'The Chosen One', 'The Amnesiac', 'C', 'Happy Apple', 'Mysterious Melon']

#we create a nicknameMap of arrays where we assign each nickname to an index (I just wanted to try this out because its fast)

nicknameMap = {}
for i in range(len(nicknames)):
    nicknameMap[nicknames[i]] = i
print('type "quit" to quit, "remove to remove a name, "add" to add a name, and "list" to see the full list of names')

def Unlucky():
    pass

def cursed(i):
    input("give your name or one of the commands ")
    print('CURSED'[i])
    if i ==  5:
        i = 0
    else:
        i += 1
    cursed(i)
    pass

def Amnesia():
    pass

def repeat(variant):
    name = input("give your name or one of the commands ")

    if name == 'quit':
        return
    elif name == 'remove':
        removal = input('type a valid name to remove ')

        if removal in nicknameMap: #this is fast
            nicknames.pop(nicknameMap[removal])
            del nicknameMap[removal]
            print(removal + ' removed')
        else:
            print('THATS NOT A VALID NICKNAME')

    elif name == 'add':
        addition = input('type a nickname to add. duplicates not allowed! ')

        if addition not in nicknameMap:
            nicknameMap[addition] = len(nicknames)
            nicknames.append(addition)
            print(addition + ' added')
        else:
            print("that nickname is already in the list!")

    elif name == 'list':
        for i in nicknames:
            print(i)

    else:
        #ok we want to add the name of the person as an actual nickname possibility as well

        nicknames.append(name)
        name = name.split(' ', 1)

        #after we are done this, we must implemenet AMNESIA

        rand = random.random()
        if rand < 0.0001:
            print(name[0] + ' "1 in 10 thousand" ' + name[len(name) - 1])
        else:

            rand = nicknames[random.randint(0,len(nicknames) - 1)]
            if len(name) > 1:
                print(name[0] + ' "' + rand + '" ' + name[len(name) - 1])
            else:
                print(name[0] + ' "' + rand + '" ' )
        nicknames.pop()

        if rand == 'C':
            cursed(1)
        elif rand in specialcon:
            pass
    repeat(variant)

#these are special conditions which when the name is gotten, I want to have special recurring effects
specialcon = {'Amnesiac' : {'func':Amnesia, 'count': 0}, 'Unlucky' : {'func':Unlucky, 'count': 0}}
repeat()