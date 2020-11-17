class Collector:
    def __init__(self, calculate_every: int = 500, total_agents: int = 20, **kwargs) -> None:
        self.calculate_every, self.total_agents = calculate_every, total_agents
        self.all_return, self.all_dones = [], []
        self.dones, self.total_rew, self.k, self.f = 0, 0, 0, 0

    def collect(self, rew, done, act):
        self.f += 1
        self.total_rew += sum(rew) / len(rew)
        self.dones += sum(done) / len(done)

        if self.f % self.calculate_every == 0:
            self.k += 1
            if self.dones != 0:
                self.all_dones.append(self.k * self.calculate_every / self.dones)
                self.all_return.append(self.total_rew / self.dones)
                self.dones, self.total_rew, self.k = 0, 0, 0
