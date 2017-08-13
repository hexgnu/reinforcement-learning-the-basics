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

def policy(current_state, total_reward = 0):
    if (not isinstance(current_state, dict)):
        print("Finished game with total reward of {}".format(total_reward))
    else:
        new_state = max(current_state.keys())
    
        print("Taking action to get to state {}".format(new_state))

        policy(current_state[new_state], total_reward + new_state)


