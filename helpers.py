from torch import as_tensor as tensor, cat as concatenation, device as devicer, cuda

device = devicer('cuda' if cuda.is_available() else 'cpu')
hidden_size = 50


def clean(obs):
    return tensor(obs.transpose(2, 0, 1).reshape(-1, 3, 64, 64)).float().to(device)


def stack(sample):
    # sample should not be too big otherwise slow
    arays = list(zip(*sample))
    return concatenation(arays[0], 0).to(device), tensor(arays[1]).unsqueeze(-1).to(device), concatenation(arays[2], 0).to(device), tensor(arays[3]).to(device), concatenation(arays[4], 1).detach().to(device), concatenation(arays[5], 1).detach().to(device), concatenation(arays[6], 1).detach().to(device), concatenation(arays[7], 1).detach().to(device), tensor(arays[8]).to(device)


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
