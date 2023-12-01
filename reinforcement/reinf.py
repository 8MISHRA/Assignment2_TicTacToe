import json
import sys
from helper import *
    
file_path = "states.json"
with open(file_path) as json_file:
    tree = json.load(json_file)

def game_board(state):
    print(f'|--{state[0]}--|--{state[1]}--|--{state[2]}--|')
    print(f'|--{state[3]}--|--{state[4]}--|--{state[5]}--|')
    print(f'|--{state[6]}--|--{state[7]}--|--{state[8]}--|')
    print()

def human(player, state):
    status = is_terminal(state) 
    if status[0]:
        return game_over(status[1])
    e = input('Your turn! choose places between 1 and 9: ')
    incorrect = True
    while incorrect:
        # s = set_move(state, player, int(e))
        s = create_state(state, player, int(e))
        if not s:
            e = input('Do not choose wrong place: ')
        else:
            incorrect = False
    return s

def ai(state, player):
    status = is_terminal(state)     
    if status[0]:
        return game_over(status[1])
    best = -float("inf")
    possible_states = []
    for i in range(9):
        if state[i] == 'N':
            possible_states.append(create_state(state, 'X', i + 1))
    for s in possible_states: 
        if tree[s] > best:
            state = s
            best = tree[s]
    return state

def game_over(score):
    if score == 1:
        print('Computer won')
    elif score == -1:
        print('You won')
    else:
        print('Draw! Play again')
    
    return 'Ended'

def main():
    starting_state = 'NNNNNNNNN'
    play = True
    while play:
        game_board(starting_state)
        state = human('O', starting_state)

        if state == 'game_over':
            i = input('Do you want to play again? Press y for yes: ')
            if 'Y' == i.upper():
                starting_state = 'NNNNNNNNN'
            else:
                play = False
        else:
            game_board(state)
            state = ai(state, 'X')

            if state == 'game_over':
                i = input('Do you want to play again? Press y for yes: ')
                if 'Y' == i.upper():
                    starting_state = 'NNNNNNNNN'
                else:
                    play = False
            else:
                starting_state = state


if __name__ == '__main__':
    main()