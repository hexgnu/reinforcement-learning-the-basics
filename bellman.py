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

MAZE2 = {
        3: {
            -100: {
                3: 'End'
                }
            },
        4: {
            100: {
                3: 'End'
                }
            }
        }

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


