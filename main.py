import gym
import sys

params = sys.argv[1:]
print(bool(params))
if params:
    # Runs un server
    pass
else:
    env = gym.make('procgen:procgen-coinrun-v0')
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            break
