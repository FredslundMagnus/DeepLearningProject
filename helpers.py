from torch import as_tensor as tensor, cat as concatenation, device as devicer, cuda

device = devicer('cuda' if cuda.is_available() else 'cpu')
hidden_size = 100


def clean(obs):
    return tensor(obs.transpose(2, 0, 1).reshape(-1, 3, 64, 64)).float().to(device)


def stack(sample):
    # sample should not be too big otherwise slow
    arays = list(zip(*sample))
    return concatenation(arays[0], 0), tensor(arays[1]).unsqueeze(-1).to(device), concatenation(arays[2], 0), tensor(arays[3]).to(device), concatenation(arays[4], 1).detach(), concatenation(arays[5], 1).detach(), concatenation(arays[6], 1).detach(), concatenation(arays[7], 1).detach(), tensor(arays[8]).to(device)
