'''
Main file for scraping data from the NHL API (or scooping out the innards of a
pumpkin)
'''

import argparse

# Global Variables
BASE_URL = 'https://statsapi.web.nhl.com/api/v1'

def scoopPlayer(playerName):
    '''
    Given a playerName retrieves stats from API about single player
    '''
    print(playerName)

def scoopTeam(teamName):
    '''
    Given a teamName retrieves stats from API about entire roster
    '''
    print(teamName)

def main():
    '''
    Interaction if run from the command line.
    Usage:  python3 scooping.py [arg] [input]
    '''
    parser = argparse.ArgumentParser(description='Get information from the \
                                    NHL API')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-p', '--player', help='give player name',
                        action='store_true')
    group.add_argument('-t', '--team', help='give team name',
                        action='store_true')
    parser.add_argument('input', nargs='+')
    args = parser.parse_args()  # gets arguments from command line

    input = ' '.join(args.input).title()

    if args.player:
        scoopPlayer(input)
    elif args.team:
        scoopTeam(input)
    else:
        print('Please define the input type')

if __name__ == '__main__':
    main()