import numpy as np
import matplotlib.pyplot as plt
from agent import Agent

# plt.imshow(np.random.random((50, 50)))
# plt.colorbar()
# plt.show()


def displayer(state, agent: Agent):
    # the_state = np.array(state).reshape(3, 64, 64).transpose(1, 2, 0)
    # print(the_state * 1.0 / 255)
    # plt.imshow(the_state / 255)
    # plt.show()
    # for i in range(3):
    #     plt.imshow(the_state[i])
    #     plt.colorbar()
    #     plt.show()
    filters = agent.network.conv1(state)
    print(filters.shape)
    print(filters)
    images = filters
    x, y = 5, 4
    _, axs = plt.subplots(y, x)
    for i in range(20):
        axs[i // x, i % x].imshow(images[i], cmap='gray')
    plt.show()
