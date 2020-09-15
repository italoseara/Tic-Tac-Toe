from random import randint
from time import sleep

red = '\033[1;31m'
blue = '\033[1;34m'
white = '\033[1;30m'
yellow = '\033[1;33m'
green = '\033[1;32m'
bold = '\033[1m'
end = '\033[m'
player = slot1 = slot2 = slot3 = slot4 = slot5 = slot6 = slot7 = slot8 = slot9 = ' '
cont = pc = playpc = r = 0

# Game Mode
game_mode = int(input(f'''
{blue}[ 1 ]{end} {red}1 Player{end}
{blue}[ 2 ]{end} {red}2 Players{end}
{blue}Select the Game Mode: {end}'''))

# ==================================================================================================================== #
# 2 Players

if game_mode == 2:
    print("\n" * 40 + f'''{bold}
                                                     |       |      
                                                 7   |   8   |   9 
                                              _______|_______|_______
                                                     |       |      
                                                 4   |   5   |   6 
                                              _______|_______|_______
                                                     |       |      
                                                 1   |   2   |   3 
                                                     |       |    






                                            \033[37m Press \033[34;1mEnter\033[37m to continue >>\033[1m''')
    input()

    a = randint(1, 2)

    while True:
        if a == 1:
            p = f'{blue}X{end}'
        elif a == 2:
            p = f'{red}O{end}'

        print("\n" * 40 + f'''
                                                     |       |      
                                                 {slot7 + bold}   |   {slot8 + bold}   |   {slot9 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot4 + bold}   |   {slot5 + bold}   |   {slot6 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot1 + bold}   |   {slot2 + bold}   |   {slot3 + bold} 
                                                     |       |    
                                                
                                                     Player {p}
        
        
        
        ''')
        square = int(input(f'                                                  {blue}Square{end}{red}:{end} '))

        if a == 1:  # X
            if square == 1:
                slot1 = f'{blue}X{end}'
            elif square == 2:
                slot2 = f'{blue}X{end}'
            elif square == 3:
                slot3 = f'{blue}X{end}'
            elif square == 4:
                slot4 = f'{blue}X{end}'
            elif square == 5:
                slot5 = f'{blue}X{end}'
            elif square == 6:
                slot6 = f'{blue}X{end}'
            elif square == 7:
                slot7 = f'{blue}X{end}'
            elif square == 8:
                slot8 = f'{blue}X{end}'
            elif square == 9:
                slot9 = f'{blue}X{end}'

        if a == 2:  # O
            if square == 1:
                slot1 = f'{red}O{end}'
            elif square == 2:
                slot2 = f'{red}O{end}'
            elif square == 3:
                slot3 = f'{red}O{end}'
            elif square == 4:
                slot4 = f'{red}O{end}'
            elif square == 5:
                slot5 = f'{red}O{end}'
            elif square == 6:
                slot6 = f'{red}O{end}'
            elif square == 7:
                slot7 = f'{red}O{end}'
            elif square == 8:
                slot8 = f'{red}O{end}'
            elif square == 9:
                slot9 = f'{red}O{end}'

        if a == 1:
            a = 2
        else:
            a = 1

        # Para a vitória de X

        if slot1 == slot2 == slot3 == f'{blue}X{end}' or\
                slot4 == slot5 == slot6 == f'{blue}X{end}' or\
                slot7 == slot8 == slot9 == f'{blue}X{end}' or\
                slot1 == slot4 == slot7 == f'{blue}X{end}' or\
                slot2 == slot5 == slot8 == f'{blue}X{end}' or\
                slot3 == slot6 == slot9 == f'{blue}X{end}' or\
                slot1 == slot5 == slot9 == f'{blue}X{end}' or\
                slot3 == slot5 == slot7 == f'{blue}X{end}':
            print("\n" * 40 + f'''
                                                     |       |      
                                                 {slot7 + bold}   |   {slot8 + bold}   |   {slot9 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot4 + bold}   |   {slot5 + bold}   |   {slot6 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot1 + bold}   |   {slot2 + bold}   |   {slot3 + bold} 
                                                     |       |    
    
                                                  {bold}Player{end} {blue}X{end} {bold}Wins!{end}
    
    
    
    ''')
            break

    # Para a vitória de O

        if slot1 == slot2 == slot3 == f'{red}O{end}' or\
                slot4 == slot5 == slot6 == f'{red}O{end}' or\
                slot7 == slot8 == slot9 == f'{red}O{end}' or\
                slot1 == slot4 == slot7 == f'{red}O{end}' or\
                slot2 == slot5 == slot8 == f'{red}O{end}' or\
                slot3 == slot6 == slot9 == f'{red}O{end}' or\
                slot1 == slot5 == slot9 == f'{red}O{end}' or\
                slot3 == slot5 == slot7 == f'{red}O{end}':
            print("\n" * 40 + f'''
                                                     |       |      
                                                 {slot7 + bold}   |   {slot8 + bold}   |   {slot9 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot4 + bold}   |   {slot5 + bold}   |   {slot6 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot1 + bold}   |   {slot2 + bold}   |   {slot3 + bold} 
                                                     |       |    
    
                                                  {bold}Player{end} {red}O{end} {bold}Wins!{end}
    
    
    
    ''')
            break

        if cont == 9:
            print("\n" * 40 + f'''
                                                     |       |      
                                                 {slot7 + bold}   |   {slot8 + bold}   |   {slot9 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot4 + bold}   |   {slot5 + bold}   |   {slot6 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot1 + bold}   |   {slot2 + bold}   |   {slot3 + bold} 
                                                     |       |    
    
                                                       {yellow}Draw!{end}
    
    
    
    ''')
            break

# ==================================================================================================================== #
# 1 Player

if game_mode == 1:
    XorO = str(input(f'{blue}X{end} or {red}O{end}? ')).lower()

    if XorO == 'x':
        player = f'{blue}X{end}'
        pc = f'{red}O{end}'
    elif XorO == 'o':
        player = f'{red}O{end}'
        pc = f'{blue}X{end}'

    difficult = str(input(f'{green}Easy{end}, {yellow}Medium{end} or {red}Hard{end}: ')).lower()

    print("\n" * 40 + f'''{bold}
                                                     |       |      
                                                 7   |   8   |   9 
                                              _______|_______|_______
                                                     |       |      
                                                 4   |   5   |   6 
                                              _______|_______|_______
                                                     |       |      
                                                 1   |   2   |   3 
                                                     |       |    






                                            \033[37m Press \033[34;1mEnter\033[37m to continue >>\033[1m''')
    input()

    a = randint(1, 2)
    while True:
        if a == 1:
            p = player
        elif a == 2:
            p = pc

        print("\n" * 40 + f'''
                                                     |       |      
                                                 {slot7 + bold}   |   {slot8 + bold}   |   {slot9 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot4 + bold}   |   {slot5 + bold}   |   {slot6 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot1 + bold}   |   {slot2 + bold}   |   {slot3 + bold} 
                                                     |       |    

                                                     Player {p}



        ''')

        cont += 1

        if a == 1:  # Player

            square = int(input(f'                                                  {blue}Square{end}{red}:{end} '))
            if square == 1:
                slot1 = player
            elif square == 2:
                slot2 = player
            elif square == 3:
                slot3 = player
            elif square == 4:
                slot4 = player
            elif square == 5:
                slot5 = player
            elif square == 6:
                slot6 = player
            elif square == 7:
                slot7 = player
            elif square == 8:
                slot8 = player
            elif square == 9:
                slot9 = player

    # Easy bot

        if difficult == 'easy':
            if a == 2:
                sleep(1.5)
                while True:
                    if a == 2:
                        def play():
                            cp = randint(1, 9)
                            return cp

                        playpc = play()

                        if playpc == 1 and slot1 == ' ':
                            slot1 = pc
                            break
                        elif playpc == 2 and slot2 == ' ':
                            slot2 = pc
                            break
                        elif playpc == 3 and slot3 == ' ':
                            slot3 = pc
                            break
                        elif playpc == 4 and slot4 == ' ':
                            slot4 = pc
                            break
                        elif playpc == 5 and slot5 == ' ':
                            slot5 = pc
                            break
                        elif playpc == 6 and slot6 == ' ':
                            slot6 = pc
                            break
                        elif playpc == 7 and slot7 == ' ':
                            slot7 = pc
                            break
                        elif playpc == 8 and slot8 == ' ':
                            slot8 = pc
                            break
                        elif playpc == 9 and slot9 == ' ':
                            slot9 = pc
                            break
        # medium bot

        if difficult == 'medium' and a == 2:
            sleep(1.5)
            while True:
                if a == 2:
                    def play():
                        cp = randint(1, 9)
                        return cp

                    if slot1 == slot2 == slot3 == slot4 == slot6 == slot7 == slot8 == slot9 == ' ' and slot5 != ' ':
                        playpc = play()

                    r = randint(1, 8)
                    if r == 1:
                        playpc = 1
                    elif r == 2:
                        playpc = 2
                    elif r == 3:
                        playpc = 3
                    elif r == 4:
                        playpc = 4
                    elif r == 5:
                        playpc = 6
                    elif r == 6:
                        playpc = 7
                    elif r == 7:
                        playpc = 8
                    elif r == 8:
                        playpc = 9

                    if slot5 == ' ':
                        playpc = 5

                    if slot8 == slot9 == player and slot7 == ' ' or slot4 == slot1 == player and slot7 == ' ' or\
                            slot3 == slot5 == player and slot7 == ' ' or \
                            slot8 == slot9 == pc and slot7 == ' ' or slot4 == slot1 == pc and slot7 == ' ' or\
                            slot3 == slot5 == pc and slot7 == ' ':

                        playpc = 7

                    elif slot7 == slot9 == player and slot8 == ' ' or slot5 == slot2 == player and slot8 == ' ' or \
                            slot7 == slot9 == pc and slot8 == ' ' or slot5 == slot2 == pc and slot8 == ' ':

                        playpc = 8

                    elif slot8 == slot7 == player and slot9 == ' ' or \
                            slot6 == slot3 == player and slot9 == ' ' or \
                            slot1 == slot5 == player and slot9 == ' 'or \
                            slot8 == slot7 == pc and slot9 == ' ' or \
                            slot6 == slot3 == pc and slot9 == ' ' or \
                            slot1 == slot5 == pc and slot9 == ' ':

                        playpc = 9

                    elif slot5 == slot6 == player and slot4 == ' ' or slot7 == slot1 == player and slot4 == ' ' or \
                            slot5 == slot6 == pc and slot4 == ' ' or slot7 == slot1 == pc and slot4 == ' ':

                        playpc = 4

                    elif slot9 == slot3 == player and slot6 == ' ' or slot4 == slot5 == player and slot6 == ' ' or \
                            slot9 == slot3 == pc and slot6 == ' ' or slot4 == slot5 == pc and slot6 == ' ':

                        playpc = 6

                    elif slot5 == slot9 == player and slot1 == ' ' or \
                            slot7 == slot4 == player and slot1 == ' ' or \
                            slot2 == slot3 == player and slot1 == ' ' or \
                            slot5 == slot9 == pc and slot1 == ' ' or \
                            slot7 == slot4 == pc and slot1 == ' ' or \
                            slot2 == slot3 == pc and slot1 == ' ':

                        playpc = 1

                    elif slot5 == slot8 == player and slot2 == ' ' or slot1 == slot3 == player and slot2 == ' ' or \
                            slot5 == slot8 == pc and slot2 == ' ' or slot1 == slot3 == pc and slot2 == ' ':

                        playpc = 2

                    elif slot5 == slot7 == player and slot1 == ' ' or \
                            slot9 == slot6 == player and slot1 == ' ' or \
                            slot2 == slot1 == player and slot1 == ' ' or \
                            slot5 == slot7 == pc and slot1 == ' ' or \
                            slot9 == slot6 == pc and slot1 == ' ' or \
                            slot2 == slot1 == pc and slot1 == ' ':

                        playpc = 3

                    if playpc == 1 and slot1 == ' ':
                        slot1 = pc
                        break
                    elif playpc == 2 and slot2 == ' ':
                        slot2 = pc
                        break
                    elif playpc == 3 and slot3 == ' ':
                        slot3 = pc
                        break
                    elif playpc == 4 and slot4 == ' ':
                        slot4 = pc
                        break
                    elif playpc == 5 and slot5 == ' ':
                        slot5 = pc
                        break
                    elif playpc == 6 and slot6 == ' ':
                        slot6 = pc
                        break
                    elif playpc == 7 and slot7 == ' ':
                        slot7 = pc
                        break
                    elif playpc == 8 and slot8 == ' ':
                        slot8 = pc
                        break
                    elif playpc == 9 and slot9 == ' ':
                        slot9 = pc
                        break

        if a == 1:
            a = 2
        else:
            a = 1

        if slot1 == slot2 == slot3 == f'{blue}X{end}' or \
                slot4 == slot5 == slot6 == f'{blue}X{end}' or \
                slot7 == slot8 == slot9 == f'{blue}X{end}' or \
                slot1 == slot4 == slot7 == f'{blue}X{end}' or \
                slot2 == slot5 == slot8 == f'{blue}X{end}' or \
                slot3 == slot6 == slot9 == f'{blue}X{end}' or \
                slot1 == slot5 == slot9 == f'{blue}X{end}' or \
                slot3 == slot5 == slot7 == f'{blue}X{end}':
            print("\n" * 40 + f'''
                                                     |       |      
                                                 {slot7 + bold}   |   {slot8 + bold}   |   {slot9 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot4 + bold}   |   {slot5 + bold}   |   {slot6 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot1 + bold}   |   {slot2 + bold}   |   {slot3 + bold} 
                                                     |       |    

                                                  {bold}Player{end} {blue}X{end} {bold}Wins!{end}



    ''')
            break

        # Para a vitória de O

        if slot1 == slot2 == slot3 == f'{red}O{end}' or \
                slot4 == slot5 == slot6 == f'{red}O{end}' or \
                slot7 == slot8 == slot9 == f'{red}O{end}' or \
                slot1 == slot4 == slot7 == f'{red}O{end}' or \
                slot2 == slot5 == slot8 == f'{red}O{end}' or \
                slot3 == slot6 == slot9 == f'{red}O{end}' or \
                slot1 == slot5 == slot9 == f'{red}O{end}' or \
                slot3 == slot5 == slot7 == f'{red}O{end}':
            print("\n" * 40 + f'''
                                                     |       |      
                                                 {slot7 + bold}   |   {slot8 + bold}   |   {slot9 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot4 + bold}   |   {slot5 + bold}   |   {slot6 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot1 + bold}   |   {slot2 + bold}   |   {slot3 + bold} 
                                                     |       |    

                                                  {bold}Player{end} {red}O{end} {bold}Wins!{end}



    ''')
            break

        if cont == 9:
            print("\n" * 40 + f'''
                                                     |       |      
                                                 {slot7 + bold}   |   {slot8 + bold}   |   {slot9 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot4 + bold}   |   {slot5 + bold}   |   {slot6 + bold} 
                                              _______|_______|_______
                                                     |       |      
                                                 {slot1 + bold}   |   {slot2 + bold}   |   {slot3 + bold} 
                                                     |       |    

                                                       {yellow}Draw!{end}



    ''')
            break

# ==================================================================================================================== #
