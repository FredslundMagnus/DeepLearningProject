import matplotlib.pyplot as plt
import pickle
import numpy as np
from collector import Collector
from environments import Environments
from display_input import displayer
import matplotlib.pyplot as plt
from pynput import keyboard

showPrint, save = False, False


def on_press(key):
    global showPrint, save
    if keyboard.Key.f2 == key:
        showPrint = True
    if keyboard.Key.f3 == key:
        save = True


keyboard.Listener(on_press=on_press).start()


def standardPlot(name, label, width=100):
    name = f"{name}-0"
    data = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Collectors/{name}.collect", "rb")).all_return
    mean = []
    sd = []
    for i in range(len(data) - width):
        mean.append(np.array(data[i:i + width]).mean())
        sd.append(np.array(data[i:i + width]).std())
    plt.plot(mean, linewidth=1.0, label=label)
    plt.fill_between(list(range(len(mean))), [r - sd for r, sd in zip(mean, sd)], [r + sd for r, sd in zip(mean, sd)], alpha=0.4)


# for env in ['maze', 'miner', 'ninja', 'plunder', 'starpilot']:
#     standardPlot(f'Base_v2_{env}', f"{env.capitalize()} V2")
#     standardPlot(f'Base_{env}', f"{env.capitalize()} V1")
#     plt.legend(loc='upper left')
#     plt.title(env.capitalize())
#     plt.show()


standardPlot('Final_stateUncertainty0and0bigfish', "No Unsertainty")
standardPlot('Final_stateUncertainty0.25and0bigfish', "Unsertainty")
plt.plot([9.6] * 5000, '--', linewidth=1.0, label="No Unsertainty Evaluate")
plt.plot([15.8] * 5000, '--', linewidth=1.0, label="Unsertainty Evaluate")
plt.legend(loc='upper left')
plt.title("Unsertainty")
plt.show()


# names = ['Uncertainty0state_difference0.1chaser', 'Uncertainty0state_difference0chaser']
# total_agents, display_every = 20, 5000
# names = [name + '-0' for name in names]
# agents = [pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "rb")) for name in names]
# env = Environments(render=True, envs=['chaser' for _ in range(total_agents)], agent=agents[0])
# collector = Collector(calculate_every=500, total_agents=total_agents)
# for f in range(1, 10000000):
#     obs, hn, cn = env.start()
#     act, obs_old, h0, c0, hn, cn = agents[0].chooseMulti(obs, hn, cn)
#     obs, rew, done, info = env.step(act, hn, cn)
#     collector.collect(rew, done, act)
#     # agents[0].rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
#     # agents[0].learn()

#     if showPrint:
#         plt.close('all')
#         #showFilters(obs[0], y=200, x=600)
#         #returnplot(collector.all_return, x=1200, y=200)
#         for agent in agents:
#             displayer(obs[0], agent, collector)
#         showPrint = False
