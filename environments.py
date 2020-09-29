import gym

"""
https://github.com/openai/procgen#environment-options
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

    def __getattribute__(self, name: str) -> str:

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
    kwargs = {}
    kwargs["distribution_mode"] = "hard"
    kwargs["start_level"] = 0
    kwargs["num_levels"] = 0
    ia = make_interactive(
        "human", record_dir=None, env_name=input(), **kwargs
    )
    ia.run()
