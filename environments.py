import gym

"""
https://github.com/openai/procgen#environment-options

obs : Box(64, 64, 3) = shape(64, 64, 3)
action_space : Discrete(15) = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
"""


class Environment:
    def __init__(self, render=False) -> None:
        self.render = render
        self.interactive = True
        self.bigfish = 'procgen:procgen-bigfish-v0'
        self.bossfight = 'procgen:procgen-bossfight-v0'
        self.caveflyer = 'procgen:procgen-caveflyer-v0'
        self.chaser = 'procgen:procgen-chaser-v0'
        self.climber = 'procgen:procgen-climber-v0'
        self.coinrun = 'procgen:procgen-coinrun-v0'
        self.dodgeball = 'procgen:procgen-dodgeball-v0'
        self.fruitbot = 'procgen:procgen-fruitbot-v0'
        self.heist = 'procgen:procgen-heist-v0'
        self.jumper = 'procgen:procgen-jumper-v0'
        self.leaper = 'procgen:procgen-leaper-v0'
        self.maze = 'procgen:procgen-maze-v0'
        self.miner = 'procgen:procgen-miner-v0'
        self.ninja = 'procgen:procgen-ninja-v0'
        self.plunder = 'procgen:procgen-plunder-v0'
        self.starpilot = 'procgen:procgen-starpilot-v0'

    def __getattribute__(self, name: str):
        evn_name = object.__getattribute__(self, name)
        if object.__getattribute__(self, 'render'):
            return gym.make(evn_name, render_mode="human")
        else:
            return gym.make(evn_name)

    def __getitem__(self, name):
        evn_name = object.__getattribute__(self, name)
        if object.__getattribute__(self, 'render'):
            return gym.make(evn_name, render_mode="human")
        else:
            return gym.make(evn_name)


if __name__ == "__main__":
    from procgen.interactive import make_interactive, ENV_NAMES
    print(ENV_NAMES)
    make_interactive("human", record_dir=None, env_name=input(), distribution_mode="hard", start_level=0, num_levels=0).run()
