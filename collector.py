class Collector:
    def __init__(self, calculate_every: int = 1000, total_agents: int = 20, **kwargs) -> None:
        self.calculate_every, self.total_agents = calculate_every, total_agents
        self.all_return, self.all_dones, self.onpolicy_all_return, self.onpolicy_all_dones = [], [], [], []
        self.dones, self.total_rew, self.k, self.f, self.onpolicy_f, self.onpolicy_total_rew, self.onpolicy_dones, self.onpolicy_k = 0, 0, 0, 0, 0, 0, 0, 0
        self.action_dist, self.action_dist_all = [0 for _ in range(15)], []

    def collect(self, rew, done, act, onpolicy=False):

        if onpolicy:
            self.onpolicy_f += 1
            self.onpolicy_total_rew += sum(rew) / len(rew)
            self.onpolicy_dones += sum(done) / len(done)
            for a in act:
                self.action_dist[a] += 1
        else:
            self.f += 1
            self.total_rew += sum(rew) / len(rew)
            self.dones += sum(done) / len(done)

        if self.f % self.calculate_every == 0 and not onpolicy:
            self.k += 1
            if self.dones != 0:
                self.all_dones.append(self.k * self.calculate_every / self.dones)
                self.all_return.append(self.total_rew / self.dones)
                self.dones, self.total_rew, self.k = 0, 0, 0

        if self.onpolicy_f % self.calculate_every == 0 and onpolicy:
            self.onpolicy_k += 1
            if self.onpolicy_dones != 0:
                self.onpolicy_all_dones.append(self.onpolicy_k * self.calculate_every / self.onpolicy_dones)
                self.onpolicy_all_return.append(self.onpolicy_total_rew / self.onpolicy_dones)
                self.onpolicy_dones, self.onpolicy_total_rew, self.onpolicy_k = 0, 0, 0
            self.action_dist_all.append([s / self.calculate_every / self.total_agents for s in self.action_dist])
            self.action_dist = [0 for _ in range(15)]
