import numpy as np
import matplotlib.pyplot as plt
from agent import Agent
from helpers import device

# plt.imshow(np.random.random((50, 50)))
# plt.colorbar()
# plt.show()

temp = 0

def displayer(state, agent: Agent):
    parametres(agent)
    imageBig(state)
    filter5(state, agent)
    plt.pause(5)
    plt.close('all')

def parametres(agent: Agent):
    global temp
    model = agent.network
    ps = [0]
    for p in model.parameters():
        ps += list(p.reshape(-1).detach().cpu().numpy())
    image = np.array(ps).reshape(-1,59).T
    plt.imshow(image-temp)
    plt.colorbar()
    plt.show(block=False)
    temp = image
    

def imageBig(state):
    plt.figure()
    the_state = np.array(state).reshape(3, 64, 64).transpose(1, 2, 0)
    plt.imshow(the_state / 255)
    plt.show(block=False)

def filter5(state, agent: Agent):
    # plt.figure()
    filters = agent.network.conv1(state.to(device)).detach().cpu().numpy().squeeze(0)
    x, y = 5, 4
    fig, axs = plt.subplots(y, x)
    for i in range(20):
        im = axs[i // x, i % x].imshow(filters[i], cmap='gray')

    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)
    plt.show(block=False)


