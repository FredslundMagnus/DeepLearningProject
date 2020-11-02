from server import defaults

file = open('Utils/experiments.sh', 'w')
file.write('#!/bin/sh\n')

features, folders = set(defaults.keys()), ['', 'Markdown', 'Agents']


def check(params):
    for name in params:
        if name not in features:
            raise Exception(f'The feature "{name}" does not exist.')


def createFolders(name):
    for folder in folders:
        file.write(f"mkdir ../outputs/{name}/{folder}\n")


def genExperiments(name, n=1, **params):
    createFolders(name)
    check(params)
    for i in range(n):
        file.write(f'bsub -o "../outputs/{name}/Markdown/{name}_{i}.md" -J "{name}_{i}" -P "{name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit.sh\n')


genExperiments('test_1', lossf='MME', discount=0.120, lambd=0.3, lr=0.0001, dropout=0)

file.close()
