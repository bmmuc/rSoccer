# '''
# #
# # Reinforcement Learing Space
# # 
# # - Each gym is a type of environment with its actions, rewards and states!
# #
# '''

import gym
import rc_gym

# Using penalty env
env = gym.make('rSimVSS3v3-v0')

env.reset()
# # Run for 10 episode and print reward at the end
for i in range(10):
    done = False
    env.render()
    while not done:
        action = env.action_space.sample()
        next_state, reward, done, _ = env.step(action)
    print(reward)