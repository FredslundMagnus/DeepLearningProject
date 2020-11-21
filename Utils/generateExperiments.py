from server import defaults

file = open('Utils/experiments.sh', 'w')
file.write('#!/bin/sh\n')

features, folders = set(defaults.keys()), ['', 'Markdown', 'Agents', "Collectors"]

environments = ['bigfish', 'bossfight', 'caveflyer', 'chaser', 'climber', 'coinrun', 'dodgeball', 'fruitbot', 'heist', 'jumper', 'leaper', 'maze', 'miner', 'ninja', 'plunder', 'starpilot']
environments = ['bigfish', 'fruitbot', 'jumper', 'leaper']

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


# for environment in ['bigfish', 'chaser', 'fruitbot']:
#     genExperiments(f'{environment}_normalised', environment=environment)

# genExperiments('Discount_0.9_1', environment='fruitbot', discount=0.9, hours=20)
# genExperiments('Discount_0.95_1', environment='fruitbot', discount=0.95, hours=20)
# genExperiments('Discount_0.99_1', environment='fruitbot', discount=0.99, hours=20)
# genExperiments('Discount_0.995_1', environment='fruitbot', discount=0.995, hours=20)
# genExperiments('Discount_0.999_1', environment='fruitbot', discount=0.999, hours=20)


# genExperiments('Discount_0.995_dist', environment='fruitbot', discount=0.995, hours=15, use_distribution=1)
# genExperiments('Discount_0.995_samp', environment='fruitbot', discount=0.995, hours=15, use_distribution=0)
# genExperiments('Dist_eps', environment='fruitbot', use_distribution=1)
# genExperiments('NoDist_eps', environment='fruitbot', use_distribution=0)
# genExperiments('Dist_LowMem_eps', environment='fruitbot', use_distribution=1, memory=50000)
# genExperiments('NoDist_LowMem_eps', environment='fruitbot', use_distribution=0, memory=50000)

for env in environments:
    genExperiments(f"Base_v2_{env}", environment=env)

file.close()
