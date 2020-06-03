import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)
experienced = []
inexperienced = []
squads = {}


def clean_data():
    for player in players:
        player['guardians'] = player['guardians'].split(' and ')
        player['height'] = int(player['height'][0:2])
        if player['experience'].lower() == 'yes':
            player['experience'] = True
            experienced.append(player)
        else:
            player['experience'] = False            
            inexperienced.append(player)




def balance_team():
    member_limit = len(players) // len(teams)
    balance = member_limit // 2
    for team in teams:
        squads[team] = []
        for i in range(balance):
            random_number = random.randint(0, len(experienced) - 1)
            poped_experienced = experienced.pop(random_number)
            poped_inexperienced = inexperienced.pop(random_number)
            squads[team].append(poped_experienced)
            squads[team].append(poped_inexperienced)



        
    
def menu():
    print()
    print("BASKETBALL TEAM STATS TOOL")
    print()
    print()
    print("----MENU-----")
    print()
    print(" Here are your choices: ")
    print()
    print()
    while True:
        display = "1) Display Team Stats"
        quit_menu = "2) Quit"
        print(display)
        print(quit_menu)
        print()
        try:
           options = int(input('\nEnter an option >  '))
        except:
            print('Please enter an option between 1-2.')   
        else:
            if options != 1:
                break
        
            else:
                if options == 1:
                    while True:
                        counter = 1
                        print()
                        for team in teams:
                            print ("{}) {} ".format(counter, team))
                            counter += 1
                        print ("{}) {} ".format(counter, 'quit'))
                        try:
                           options = int(input('\nEnter an option >  '))
                        except:
                            print('Please enter an option between 1-3.')   
                        else:
                            if options == 1:
                                print('Team: Panthers Stats')
                                print('--------------------')
                                ex = 0
                                inex = 0
                                average_height = 0
                                for player in squads['Panthers']:
                                    average_height += player['height']
                                    if player['experience'] == True:
                                       ex += 1
                                    else:
                                        inex += 1
                        
                                print('\nTotal players: {}'.format(len(squads['Panthers'])))
                                print('Total experienced : {}'.format(ex))
                                print('Total experienced : {}'.format(inex))
                                print('Average height: {}'.format(average_height // len(squads['Panthers'])))
                                print('Players on Team:')
                                players = ''
                                for player in squads['Panthers']:
                                    players += player['name']+ ', '
                                print(players[:-2])
                                print('\nGuardiands:')
                                guardians = ''
                                for player in squads['Panthers']:
                                    guardians += ', '.join(player['guardians']) + ', '
                                print(guardians[:-2])

                            if options == 2:
                                print('Team: Bandits Stats')
                                print('--------------------')
                                ex = 0
                                inex = 0
                                average_height = 0
                                for player in squads['Bandits']:
                                    average_height += player['height']
                                    if player['experience'] == True:
                                       ex += 1
                                    else:
                                        inex += 1
                                
                                print('\nTotal players: {}'.format(len(squads['Bandits'])))
                                print('Total experienced : {}'.format(ex))
                                print('Total experienced : {}'.format(inex))
                                print('Average height: {}'.format(average_height // len(squads['Bandits'])))
                                print('Players on Team:')
                                players = ''
                                for player in squads['Bandits']:
                                    players += player['name']+ ', '
                                print(players[:-2])
                                print('\nGuardiands:')
                                guardians = ''
                                for player in squads['Bandits']:
                                    guardians += ', '.join(player['guardians']) + ', '
                                print(guardians[:-2])

                                        
                            if options == 3:
                                print('Team: Warriors Stats')
                                print('--------------------')
                                ex = 0
                                inex = 0
                                average_height = 0
                                for player in squads['Warriors']:
                                    average_height += player['height']
                                    if player['experience'] == True:
                                       ex += 1
                                    else:
                                        inex += 1
                                
                                print('\nTotal players: {}'.format(len(squads['Warriors'])))
                                print('Total experienced : {}'.format(ex))
                                print('Total experienced : {}'.format(inex))
                                print('Average height: {}'.format(average_height // len(squads['Warriors'])))
                                print('Players on Team:')
                                players = ''
                                for player in squads['Warriors']:
                                    players += player['name']+ ', '
                                print(players[:-2])
                                print('\nGuardiands:')
                                guardians = ''
                                for player in squads['Warriors']:
                                    guardians += ', '.join(player['guardians']) + ', '
                                print(guardians[:-2])

                                        

                            if options == 4:
                                break
                                
            

        
