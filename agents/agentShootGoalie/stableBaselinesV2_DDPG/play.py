import gym
import gym_ssl
import numpy as np

from stable_baselines import DDPG

env = gym.make('grSimSSLShootGoalie-v0')
model = DDPG.load("./models/ddpg_shootgoalie2")

while True:
    done = False
    obs = env.reset()
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
