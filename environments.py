import gym
from typing import List
from helpers import device, hidden_size, clean, clean
import torch

"""
https://github.com/openai/procgen#environment-options

obs : Box(64, 64, 3) = shape(64, 64, 3)
action_space : Discrete(15) = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

("LEFT", "DOWN"),
("LEFT",),
("LEFT", "UP"),
("DOWN",),
(),
("UP",),
("RIGHT", "DOWN"),
("RIGHT",),
("RIGHT", "UP"),
("D",),
("A",),
("W",),
("S",),
("Q",),
("E",),
"""


class Environment:
    settings = {'distribution_mode': "easy",
                'use_backgrounds': False,
                'use_monochrome_assets': True,
                'restrict_themes': True,
                'use_generated_assets': False,
                'paint_vel_info': False}

    def __init__(self, render: bool = False) -> None:
        self.render = render
        self.bigfish: Environment = None
        self.bossfight: Environment = None
        self.caveflyer: Environment = None
        self.chaser: Environment = None
        self.climber: Environment = None
        self.coinrun: Environment = None
        self.dodgeball: Environment = None
        self.fruitbot: Environment = None
        self.heist: Environment = None
        self.jumper: Environment = None
        self.leaper: Environment = None
        self.maze: Environment = None
        self.miner: Environment = None
        self.ninja: Environment = None
        self.plunder: Environment = None
        self.starpilot: Environment = None

    def __getattribute__(self, name: str):
        return Environment.create(name, object.__getattribute__(self, 'render'))

    def __getitem__(self, name: str):
        return Environment.create(name, object.__getattribute__(self, 'render'))

    @staticmethod
    def create(name: str, render: bool):
        return gym.make(f'procgen:procgen-{name}-v0', render_mode="human", **Environment.settings) if render else gym.make(f'procgen:procgen-{name}-v0', **Environment.settings)


class Environments:
    def __init__(self, envs: List[str], render: bool = False) -> None:
        self.envs = [Environment.create(name, render and not bool(i)) for i, name in enumerate(envs)]
        self.obs, self.hn, self.cn = tuple(zip(*[self.reset(env, True, None, None, None) for env in self.envs]))

    def step(self, actions: List[int], hns, cns):
        obses, rews, dones, infos = tuple(zip(*[env.step(act) for env, act in zip(self.envs, actions)]))
        obses = [clean(obs) for obs in obses]
        self.obs, self.hn, self.cn = tuple(zip(*[Environments.reset(env, done, obs, hn, cn) for env, done, obs, hn, cn in zip(self.envs, dones, obses, hns, cns)]))
        return obses, rews, dones, infos

    @staticmethod
    def reset(env, done, obs, hn, cn):
        if done:
            env.close()
            return clean(env.reset()), torch.zeros(1, 1, hidden_size, device=device), torch.zeros(1, 1, hidden_size, device=device)
        return obs, hn.detach(), cn.detach()

    def start(self):
        return self.obs, self.hn, self.cn


if __name__ == "__main__":
    """
    https://github.com/openai/procgen/blob/master/procgen/env.py
    """
    from procgen.interactive import make_interactive, ENV_NAMES
    print(ENV_NAMES)
    make_interactive("human", record_dir=None, env_name=input(), distribution_mode="easy", start_level=0, num_levels=0).run()
