def is_terminal(state):
    i = 0
    j = 0
    while i < 9 and j < 3:
        #checking state for row-wise
        s = state[i: i+3]
        if s == 'XXX' or s == 'OOO':            
            if s == 'XXX':
                return (True, 1)
            return (True, -1)
        
        #checking state for column-wise
        s = state[j] + state[j+3] + state[j+6]
        if s == 'XXX' or s == 'OOO':
            if s == 'XXX':
                return (True, 1)
            return (True, -1)
        i += 3
        j += 1

    #checking state diagonally.
    s1 = state[0] + state[4] + state[8]
    s2 = state[2] + state[4] + state[6]
    if s1 == 'XXX' or s2 == 'XXX':
        return (True, 1)
    if s1 == 'OOO' or s2 == 'OOO':
        return (True, -1)
    
    if 'N' not in state:
        return (True, 0)
    return (False, None)
    
def is_valid(state, position):
    if state[position - 1] == 'N':
        return True
    False

def create_state(state, character, position):
    assert 1 <= position <= 9, str(position) + 'Please enter position between 1-9: '
    if is_valid(state, position):           # Checking if state is valid.
        state = state[:position - 1] + character + state[position:]
        return state
    return False

# def set_move(state, character, position):
#     return create_state(state, character, position)