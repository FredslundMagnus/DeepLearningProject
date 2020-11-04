import numpy as np
import matplotlib.pyplot as plt
from agent import Agent
from helpers import device
import matplotlib
import math

# plt.imshow(np.random.random((50, 50)))
# plt.colorbar()
# plt.show()

temp = 0


def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)


def displayer(state, agent: Agent):
    plt.close('all')
    parametresSample(agent, x=1200, y=0, n=80, h=8)
    imageBig(state, x=600, y=485)
    filter5(state, agent, x=1200, y=485)
    filterColor(state, agent, x=600, y=0)
    enc = agent.network.color(state.to(device))
    # enc_stand = enc / enc.max()
    filters = agent.network.colorReverse(enc).detach().cpu().numpy().squeeze(0)
    imageBig(256 * filters, x=0, y=485)
    # plt.pause(8)


def parametres(agent: Agent, x: int = 1000, y: int = 0):
    global temp
    fig = plt.figure()
    move_figure(fig, x, y)
    model = agent.network
    ps = []
    for p in model.parameters():
        # print(p.shape, max(list(p.reshape(-1).detach().cpu().numpy())))
        ps += list(p.reshape(-1).detach().cpu().numpy())
    n = len(ps)
    h = math.ceil(math.sqrt(n // 10))
    image = np.array(ps)[:-(n % h)].reshape(-1, h).T
    plt.imshow((image - temp) / image.std())
    plt.colorbar()
    plt.show(block=False)
    temp = image


def parametresSample(agent: Agent, x: int = 1000, y: int = 0, n=100, h=None):
    global temp
    fig = plt.figure()
    move_figure(fig, x, y)
    model = agent.network
    ps = []
    for p in model.parameters():
        # print(p.shape, max(list(p.reshape(-1).detach().cpu().numpy())))
        ps += list(p.reshape(-1).detach().cpu().numpy())
    h = math.ceil(math.sqrt(n // 10)) if h is None else h
    image = np.array(ps)[:n].reshape(-1, h).T
    plt.imshow((image - temp) / image.std())
    plt.colorbar()
    plt.show(block=False)
    temp = image


def imageBig(state, x: int = 1000, y: int = 0):
    fig = plt.figure()
    move_figure(fig, x, y)
    the_state = np.array(state).reshape(3, 64, 64).transpose(1, 2, 0)
    plt.imshow(the_state / 255)
    plt.show(block=False)


def filter5(state, agent: Agent, x: int = 1000, y: int = 0):
    # plt.figure()
    filters = agent.network.conv1(agent.network.color(state.to(device))).detach().cpu().numpy().squeeze(0)
    n = filters.shape[0]
    v = math.ceil(math.sqrt(n))
    fig, axs = plt.subplots(v, v)
    move_figure(fig, x, y)
    for i in range(n):
        im = axs[i // v, i % v].imshow(filters[i], cmap='gray')

    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)
    plt.show(block=False)


def filterColor(state, agent: Agent, x: int = 1000, y: int = 0):
    # plt.figure()
    filters = agent.network.color(state.to(device)).detach().cpu().numpy().squeeze(0)
    # print("filter", filters.min())
    n = filters.shape[0]
    v = math.ceil(math.sqrt(n))
    fig, axs = plt.subplots(v, v)
    move_figure(fig, x, y)
    for i in range(n):
        im = axs[i // v, i % v].imshow(filters[i], cmap='gray')

    fig.subplots_adjust(right=0.8)
    # cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    # plt.clim(filters.min(), filters.max())
    # plt.colorbar()
    # fig.colorbar(im, cax=cbar_ax)
    plt.show(block=False)
