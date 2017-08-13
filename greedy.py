maze = {
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


def greedy_policy(current_state, total_reward = 0):
    if (not isinstance(current_state, dict)):
        print("Finished game with total reward of {}".format(total_reward))
    else:
        new_state = max(current_state.keys())
    
        print("Taking action to get to state {}".format(new_state))

        greedy_policy(current_state[new_state], total_reward + new_state)


def backwards_policy(current_state):
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

def discounted_reward(current_state, gamma = 0.9):
    if (isinstance(current_state, dict)):
        return sum([k + gamma * discounted_reward(v) for k,v in current_state.items()])
    else:
        return 0
    
def bellman_policy(current_state, total_reward = 0, gamma = 0.9):
    if (not isinstance(current_state, dict)):
        print("Finished game with total reward of {}".format(total_reward))
    else:
        bellman_maze = {(k + gamma * discounted_reward(v), k): v for k,v in current_state.items()}

        new_state = max(bellman_maze.keys())

        print("Taking action to get to state {} with expected payoff of {}".format(new_state[1], new_state[0]))

        bellman_policy(bellman_maze[new_state], total_reward + new_state[1])


