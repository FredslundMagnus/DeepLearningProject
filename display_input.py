from collector import Collector
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


def displayer(state, agent: Agent, collector: Collector):
    returns, dones, names, true_returns, true_dones = collector.all_return, collector.all_dones, f"seen frames in {collector.total_agents * collector.calculate_every}'s", collector.onpolicy_all_return, collector.onpolicy_all_dones
    plt.close('all')
    returnplot(returns, true_returns, x=100, y=500, xlabel=names)
    returnplot(dones, true_dones, x=100, y=0, ylabel="Game length (frames per game)", xlabel=names)
    parametres(agent, x=1300, y=0)
    imageBig(state, x=700, y=500)
    showFilters(agent.network.conv1(agent.network.color(state.to(device))), x=1300, y=500)
    showFilters(agent.network.color(state.to(device)), x=700, y=0)


def returnplot(returns, true_returns, x: int = 1000, y: int = 500, xlabel=None, ylabel="Return (per game)"):
    runnings = [0] * len(returns)
    true_runnings = [0] * len(true_returns)
    for i in range(1, len(runnings) + 1):
        if i < 50:
            runnings[i - 1] = sum(returns[:i]) / i
        else:
            runnings[i - 1] = sum(returns[(i - 50):i]) / 50
    extend_true_runnings = [0] * len(returns)
    final_true_runnings = [0] * len(returns)
    try:
        for i in range(int(len(runnings))):
            extend_true_runnings[i] = (i % (len(extend_true_runnings)//len(true_returns)))/(len(extend_true_runnings)//len(true_returns)) * true_returns[int(min((i*len(true_returns))//len(extend_true_runnings),len(true_returns)))] + true_returns[int(min((i*len(true_returns))//len(extend_true_runnings)+1,len(true_returns)-1))] * (1 - (i % (len(extend_true_runnings)//len(true_returns)))/(len(extend_true_runnings)//len(true_returns)))
        for i in range(1, len(extend_true_runnings) + 1):
            if i < 350:
                final_true_runnings[i - 1] = sum(extend_true_runnings[:i]) / i
            else:
                final_true_runnings[i - 1] = sum(extend_true_runnings[(i - 350):i]) / 350
    except ZeroDivisionError:
        pass
    fig = plt.figure()
    move_figure(fig, x, y)
    plt.plot(runnings)
    plt.plot(final_true_runnings)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show(block=False)


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


def imageBig(state, x: int = 1000, y: int = 0):
    fig = plt.figure()
    move_figure(fig, x, y)
    the_state = np.array(state.cpu()).reshape(3, 64, 64).transpose(1, 2, 0) + 1
    plt.imshow(the_state / 2)
    plt.show(block=False)


def showFilters(filters, x: int = 1000, y: int = 0):
    filters = filters.detach().cpu().numpy().squeeze(0)
    n = filters.shape[0]
    v = math.ceil(math.sqrt(n))
    h = math.ceil(n / v)
    fig, axs = plt.subplots(h, v)
    move_figure(fig, x, y)
    for i in range(n):
        im = axs[i // v, i % v].imshow(filters[i], cmap='gray', vmin=float(filters.min()), vmax=float(filters.max()))

    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)
    plt.show(block=False)
