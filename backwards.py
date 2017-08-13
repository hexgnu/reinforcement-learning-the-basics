MAZE = {
        3: {
            8: {
                99: 'End'
                }
            },
        12: {
            6: {
                5: 'End'
                }
            }
        }

def flat_map(array):
    new_array = []

    for a in array:
        if isinstance(a, list):
            new_array += flat_map(a)
        else:
            new_array.append(a)

    return new_array

def create_dict(flat_array):
    head, *tail = flat_array

    if len(tail) == 1:
        return {head: tail[0]}
    else:
        return {head: create_dict(tail)}

def invert_dict(dictionary, stack=None):
    if not stack: stack = []

    if (not isinstance(dictionary, dict)):
        return dictionary

    for k, v in dictionary.items():
        stack.append([invert_dict(v), k])

    return stack

def create_new_maze(dictionary):
    new_maze = {}
    for path in invert_dict(dictionary):
        new_maze.update(create_dict(flat_map(path)[1:]))

    return new_maze

def policy(current_state):
    upside_down_maze = create_new_maze(current_state)

    states = []
    while (isinstance(upside_down_maze, dict)):
        new_state = max(upside_down_maze.keys())
        states = [new_state] + states
        upside_down_maze = upside_down_maze[new_state]

    states = [upside_down_maze] + states

    total_reward = 0
    for s in states:
        total_reward += s
        print("Tacking action to get to state {}".format(s))

    print("Finished game with total reward of {}".format(total_reward))
