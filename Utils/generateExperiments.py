file = open('Utils/experiments.sh', 'w')
file.write('#!/bin/sh\n')

features = set(['lossf', 'discount', 'lambd', 'lr', 'dropout', 'K', 'batchSize', 'historyLength'])
folders = ['csv', 'trained', 'TrainingCurve', 'Weights', 'Elo_Rating', 'Increase_in_Elo_over_time', 'data']


def check(params):
    for name in params:
        if name not in features:
            raise Exception(f'The feature "{name}" does not exist.')


def createFolders(name):
    file.write(f"mkdir outputs/{name}\n")
    for folder in folders:
        file.write(f"mkdir outputs/{name}/{folder}\n")


def genExperiments(name, n=10, **params):
    createFolders(name)
    check(params)
    for i in range(n):
        file.write(f'bsub -o "outputs/{name}/{name}-{i}.md" -J "{name}-{i}" -P "{name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit.sh\n')


# genExperiments('Discount-0.70', lossf='MME', discount=0.70, lambd=0.5, lr=0.0001, dropout=0, K=2000, batchSize=100, historyLength=20)
