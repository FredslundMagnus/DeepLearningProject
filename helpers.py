from torch import as_tensor as tensor, cat as concatenation


def clean(obs):
    return tensor(obs.transpose(2, 0, 1).reshape(-1, 3, 64, 64)).float()


def stack(sample):
    # sample should not be too big otherwise slow
    arays = list(zip(*sample))
    return concatenation(arays[0], 0), tensor(arays[1]).unsqueeze(-1), concatenation(arays[2], 0), tensor(arays[3])
