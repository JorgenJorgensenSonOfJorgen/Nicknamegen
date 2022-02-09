#I want to create a nickname generator, but I also want to create a locked mode nickname generator
#we also need to add an ability to add or remove nicknames, to view full nickname list.

import random

nicknames = ['The Flash', 'The Cowboy', 'QiQi', 'The Addict', '?', 'The Bitter', 'The Indecisive', 'The Speler', 'White Wolf', '4782817', 'The Unlucky', 'The Chosen One', 'The Amnesiac', 'Happy Apple', 'Mysterious Melon']

#I want to create a dictionary because it is faster.
nicknameMap = {}
for i in range(len(nicknames)):
    nicknameMap[nicknames[i]] = i

print('type "quit" to quit, "remove to remove a name, "add" to add a name, and "list" to see the full list of names')

def formatOutput(nameSplit,nickname):
    if len(nameSplit) > 1:
        print(nameSplit[0] + ' "' + nickname + '" ' + nameSplit[1])
    else:
        print(nameSplit[0] + ' "' + nickname + '"' )

def repeat(variant,count):
    name = input("give your name or one of the commands ")

    if name == 'quit':
        return
    elif name == 'remove':
        removal = input('type a valid name to remove ')

        if removal in nicknameMap:
            del nicknameMap[removal]
            print(removal + ' removed')
        else:
            print('THATS NOT A VALID NICKNAME')

    elif name == 'add':
        addition = input('type a nickname to add. duplicates not allowed! ')

        if addition not in nicknameMap:
            nicknameMap[addition] = True
            print(addition + ' added')
        else:
            print("that nickname is already in the list!")

    elif name == 'list':
        for i in nicknameMap:
            print(i)

    else:
        nameSplit = name.split(' ', 1)

        #after we are done this, we must implemenet AMNESIA
        if variant:
            formatOutput(nameSplit, variant['func'])
            count -=1
            if count == 0:
                variant = False
        else:
            if random.random() < 0.0001:
                formatOutput(nameSplit, 'one in 10 thousand')
            else:
                #ok we want to add the name of the person as an actual nickname possibility as well
                if name not in nicknameMap:
                    nicknameMap[name] = True
                    nickname = random.choice(list(nicknameMap.keys()))
                    formatOutput(nameSplit, nickname)
                    del nicknameMap[name]
                else:
                    nickname = random.choice(list(nicknameMap.keys()))
                    formatOutput(nameSplit, nickname)
            if nickname in specialcon:
                variant = specialcon[nickname]
                count = specialcon[nickname]['count']
    repeat(variant,count)

#these are special conditions which when the name is gotten, I want to have special recurring effects
specialcon = {'The Amnesiac' : {'func':'The Amnesiac', 'count': 5
}, 'The Unlucky' : {'func':'crap', 'count': 5}}
repeat(False, 0)