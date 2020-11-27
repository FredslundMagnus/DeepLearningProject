from torch.nn import Module, Conv2d, Linear, MSELoss, LeakyReLU, Sequential, ReLU, ConvTranspose2d
from torch.optim import Adam
from environments import Environments
from agent import Agent
import torch
from helpers import device, count_parameters
from display_input import imageBig
import matplotlib.pyplot as plt
from pynput import keyboard
import pickle

showPrint, save = False, False


def on_press(key):
    global showPrint, save
    if keyboard.Key.f2 == key:
        showPrint = True
    if keyboard.Key.f3 == key:
        save = True


keyboard.Listener(on_press=on_press).start()


class NetWork(Module):
    def __init__(self):
        super(NetWork, self).__init__()

        self.encoder = Sequential(
            Conv2d(in_channels=3, out_channels=16, kernel_size=4, stride=2),
            LeakyReLU(),
            Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=2),
            LeakyReLU(),
            Conv2d(in_channels=32, out_channels=10, kernel_size=3, stride=2),
            LeakyReLU(),
        )

        self.decoder = Sequential(
            ConvTranspose2d(in_channels=10, out_channels=32, kernel_size=5, stride=3, padding=1),
            LeakyReLU(),
            ConvTranspose2d(in_channels=32, out_channels=16, kernel_size=5, stride=3),
            LeakyReLU(),
            Conv2d(in_channels=16, out_channels=8, kernel_size=2, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=12, out_channels=3, kernel_size=1, stride=1),
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x


total_agents, display_every = 20, 5000
agent = Agent(memory=50000, discount=0.995, uncertainty=False, update_every=100, double=True, use_distribution=False, reward_normalization=True)
env = Environments(render=True, envs=['bigfish', 'bossfight', 'caveflyer', 'chaser', 'climber', 'coinrun', 'dodgeball', 'fruitbot', 'heist', 'jumper', 'leaper', 'maze', 'miner', 'ninja', 'plunder', 'starpilot'], agent=agent)
network = NetWork().to(device)
print("Number of parameters in network:", count_parameters(network))
print("Number of parameters in encoder:", count_parameters(network.encoder))
print("Number of parameters in decoder:", count_parameters(network.decoder))
criterion = MSELoss()
optimizer = Adam(network.parameters(), lr=1e-4, weight_decay=1e-5)
for f in range(0, 10000000):
    obs, hn, cn = env.start()
    act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
    obs, rew, done, info = env.step(act, hn, cn)
    agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
    obs, action, obs_next, reward, h0, c0, hn, sn, done = agent.memory.sample(256)
    guess = network(obs)
    loss = criterion(guess, obs)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    if showPrint:
        plt.close('all')
        imageBig(obs[0].cpu(), y=200, x=600)
        imageBig(guess[0].detach().cpu().clamp(-1, 1), y=200, x=1200)
        showPrint = False
    if save:
        with open(f"Encoders/encoder{f}.obj", "wb") as file:
            print(f"Creating encoder{f}.obj")
            pickle.dump(network, file)
        save = False
    if f % 10 == 0:
        print(f, str(float(loss.detach()))[:10])
