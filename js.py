import random
#history of prior nicknames (important later)
history = []
#signals whether a special condition is in effect
variant = False
nicknames = [ 'The Cowboy', 'QiQi', '?', 'The Bitter', 'The Indecisive', 'The Speler', 'White Wolf', '4782817', 'The Unlucky', 'The Chosen One', 'The Amnesiac', 'Mysterious Melon']

#I want to create a dictionary because it is faster.
nicknameMap = {}
for i in range(len(nicknames)):
    nicknameMap[nicknames[i]] = i

print('type "quit" to quit, "remove to remove a name, "add" to add a name, and "list" to see the full list of names')

def formatOutput(nameSplit,nickname):
    #account for one word names vs. two word names
    if len(nameSplit) > 1:
        print(nameSplit[0] + ' "' + nickname + '" ' + nameSplit[1])
    else:
        print(nameSplit[0] + ' "' + nickname + '"' )
def remove():
        removal = input('type a valid name to remove ')

        if removal in nicknameMap:
            del nicknameMap[removal]
            print(removal + ' removed')
        else:
            print('THATS NOT A VALID NICKNAME')
def add():
    addition = input('type a nickname to add. duplicates not allowed! ')

    if addition not in nicknameMap:
        nicknameMap[addition] = True
        print(addition + ' added')
    else:
        print("that nickname is already in the list")

#special condition, will repeat the previous 7 nicknames or until first nickname when 'The Amnesiac' is gotten
def amnesiac():
    global specialcon
    global variant
    length = len(history)
    info = specialcon['The Amnesiac']
    #this is the first time we are recieving it, calc
    if info['count'] == 0:
        if length >= 7:
            info['repeat'] = history[length -7 :length]
        else:
            info['repeat'] = history[0: length]
        info['count'] = 1
        nickname =  info['repeat'][0]
    else:
        nickname = info['repeat'][info['count']]
        info['count'] += 1

    if len(info['repeat']) == info['count']:
        variant = False
        info['count'] = 0
        info['repeat'] = ''
    return nickname

#special condition, calls you crap 5 times in a row if you get 'The Unlucky'
def unlucky():
    global specialcon
    global variant
    specialcon['The Unlucky']['count'] += 1
    if specialcon['The Unlucky']['count'] == 5:
        variant = False
        specialcon['The Unlucky']['count'] = 0
    return 'crap'

#main function
def repeat():
    global variant
    name = input("give your name or one of the commands ")
    if name == 'quit':
        return
    elif name == 'remove':
        remove()
    elif name == 'add':
        add()
    elif name == 'list':
        for i in nicknameMap:
            print(i)
    else:
        nameSplit = name.split(' ', 1)

        #check to see if special condition is in effect
        if variant:
            formatOutput(nameSplit, variant['func']())
        else:
            #possibility of getting rare one in 10 thousand nickname
            if random.random() < 0.0001:
                formatOutput(nameSplit, 'one in 10 thousand')
            else:
                #we want to add the name of the person as an actual nickname possibility as well
                if name not in nicknameMap:
                    nicknameMap[name] = True
                    nickname = random.choice(list(nicknameMap.keys()))
                    formatOutput(nameSplit, nickname)
                    del nicknameMap[name]
                else:
                    nickname = random.choice(list(nicknameMap.keys()))
                    formatOutput(nameSplit, nickname)
            #checks to see if the nickname will trigger future events
            if nickname in specialcon:
                variant = specialcon[nickname]
            history.append(nickname)
    repeat()

#these are special conditions which when the name is gotten, I want to have special recurring effects
specialcon = {'The Amnesiac' : {'func':amnesiac, 'count': 0
}, 'The Unlucky' : {'func':unlucky, 'count': 0}}
#func = what special condition takes effect
repeat()