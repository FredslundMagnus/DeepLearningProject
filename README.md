# Deep Learning Project

Q-learning implementation with deep off-policy exploration for the procgen environments.

# Requirements

```bash
python -m pip install torch torchvision
```

```bash
python -m pip install gym procgen
```

```bash
python -m pip install matplotlib
```

```bash
python -m pip install pynput
```

# Using the enviroment

## Initialize

```python
from agent import Agent
from environments import Environments
from collector import Collector

agent = Agent()
env = Environments(render=True, envs=["maze"] * 20, agent=agent)
collector = Collector()
```

## Run the training loop

```python
while True:
    obs, hn, cn = env.start()
    act, obs_old, h0, c0, hn, cn, bt, at = agent.chooseMulti(obs, hn, cn)
    obs, rew, done, info = env.step(act, hn, cn)
    collector.collect(rew, done, act)
    agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done, bt, at)
    agent.learn()
```
