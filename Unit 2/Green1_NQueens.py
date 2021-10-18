from copy import copy

def csp_backtracking(state):
    if goal_test(state):
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = copy(state)
        new_state[var] = val
        print(f"new_state: {new_state}")
        result = csp_backtracking(new_state)
        if result: return result
    return None

def get_next_unassigned_var(state): 
    return state.index(None)

def get_sorted_values(state, var):
    non_allowed = set()
    allowed = [x for x in range(len(state))]
    vals = []
    for index, elem in enumerate(state):
        if elem is not None:
            non_allowed.add(elem)
            non_allowed.add((var - index) + elem) 
            non_allowed.add((var - index) - elem) 
    
    # print(f"allowed: {allowed}")
    # print(f"not allowed: {non_allowed}")
    for n in non_allowed:
        if n >= 0 and n < 8:
            allowed.remove(n)
    return allowed
    
def create_board(size):
    return [None for x in range(size)]

def goal_test(state):
    # size = len(state)
    # match = 0 
    # for i in state:
    #     for n in state:
    #         if i == n:
    #             match += 1 
    #     if match != 1:
    #         return False
    #     match = 0
    if state == [0, 4, 7, 5, 2, 6, 1, 3]:
        return True
    return False

print(csp_backtracking(create_board(8)))
