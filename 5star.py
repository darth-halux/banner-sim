from math import *
from random import *

rate5 = 0.006
rate4 = 0.051
three_rewards = ['Slingshot', "Sharpshooter's Oath", "Raven Bow",
                 "Emerald Orb", "Thrilling Tales of Dragon Slayers",
                 "Magic Guide", "Debate Club", "Bloodstained Greatsword",
                 "Ferrous Shadow", "Black Tassel", "Skyrider Sword",
                 "Harbinger of Dawn", "Cool Steel"]

five_rewards = ['Diluc', 'Mona', 'Jean', 'Qiqi', 'Keqing']

four_weapons = ['Rainslasher', 'Sacrificial Greatsword', 'The Stringless',
                'Favonius Warbow', 'Eye of Perception', 'Sacrificial Fragments',
                'The Widsith', 'Favonius Codex', 'The Bell',
                'Favonius Greatsword', 'Favonius Lance', "Dragon's Bane",
                "Lion's Roar", "Sacrificial Sword", 'The Flute',
                'Favonius Sword']

four_chars = ['Sayu', 'Diona', 'Chongyun', 'Rosaria', 'Fischl', 'Beidou',
              'Razor', 'Noelle', 'Ningguang', 'Xingqiu', 'Barbara',
              'Xinyan', 'Bennett', 'Yanfei']

four_chars_featured = ['Sucrose', 'Xiangling', 'Kujou Sara']

def pull(pity4=1, pity5=1):
    x = random()
    prob5 = rate5 + max(0, (pity5 - 73)* 10 * rate5)
    prob4 = rate4 + max(0, (pity4 - 8) * 10 * rate4)

    if x< prob5:
        return '5star',  pity4 + 1, 1

    elif x< prob4 + prob5:
        return '4star', 1, pity5 + 1

    else:
        return '3 star', pity4 + 1, pity5 + 1

def process_data(reward):
    global ff4
    global ff5
    
    if reward == '3 star':
        return three_rewards[randint(0,12)]
    
    elif reward ==  '4star':
        if ff4 or randint(0,1) == 0:
            ff4 = False
            return '---' + four_chars_featured[randint(0,2)] + '---'
        elif randint(0,1) == 0:
            ff4 = True
            return '--' + four_chars[randint(0,13)] + '--'
        else:
            ff4 = True
            return '-' + four_weapons[randint(0,15)] + '-'
        
    else:
        if(ff5 or randint(0,1) == 0):
            ff5 =  False
            return '-----Raiden Shogun-----'
        else:
            ff5 = True
            return '----' + five_rewards[randint(0,4)] + '----'

data = [None, 1, 1]
global ff4
global ff5
ff4 = False
ff5 = False
i = 1
history = dict()

print("\n{:^44}".format('WISH SIMULATOR'))
print('\n\n {:-^40}'.format('Commands'))
print('Press Enter for a single pull\nType a number to pull that many times')
print('Type "Reset" to clear pity and 50/50')
print('Type "History" to see what you have gotten so far')
print('Type "Exit" to finish\n')

while(True):
    buffer = input()
    
    if buffer == 'Exit' or buffer == 'exit':
        break

    elif buffer == 'History' or buffer == 'history':
        keys = list(history.keys())
        keys.sort()
        for key in keys:
            print(f'{key} : {history[key]}')
            
    elif buffer == 'Reset' or buffer == 'reset':
        i = 1
        ff4 = False
        ff5 = False
        data = [None, 1, 1]
        history = dict()
    
    elif buffer == '':
        data = pull(data[1], data[2])
        result = process_data(data[0])
        print(i, result)
        history[result] = history.setdefault(result, 0) + 1
        i += 1
        
    elif buffer.isnumeric():
        for j in range(int(buffer)):
            data = pull(data[1], data[2])
            result = process_data(data[0])
            print(i, result, '\n')
            history[result] = history.setdefault(result, 0) + 1
            i += 1
            
    else:
        print('Press Enter for a single pull\nType a number to pull that many times')
        print('Type "Reset" to clear pity and 50/50')
        print('Type "History" to see what you have gotten so far')
        print('Type "Exit" to finish\n')

