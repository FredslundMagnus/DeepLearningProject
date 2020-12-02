from os import sep
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

#genExperiments('NoNormalizationNoUncertainty', environment='fruitbot', use_distribution=0, uncertainty=0, reward_normalization=0, memory=500000)
#genExperiments('YesNormalizationNoUncertainty', environment='fruitbot', use_distribution=0, uncertainty=0, reward_normalization=1, memory=500000)
#genExperiments('NoNormalizationYesUncertainty', environment='fruitbot', use_distribution=0, uncertainty=1, reward_normalization=0, memory=500000)
#genExperiments('YesNormalizationYesUncertainty', environment='fruitbot', use_distribution=0, uncertainty=1, reward_normalization=1, memory=500000)

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

#genExperiments(f"UUncertainty+Avoid_State0and0{env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=0)
#genExperiments(f"UUncertainty+Avoid_State0and-1{env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=-1)
#genExperiments(f"UUncertainty+Avoid_State0and1{env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=1)
#genExperiments(f"UUncertainty+Avoid_State-1and0{env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=-1, state_difference_weight=0)
#genExperiments(f"UUncertainty+Avoid_State1and0{env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=1, state_difference_weight=0)
#genExperiments(f"UUncertainty+Avoid_State0and10{env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=10)

""" genExperiments(f"Final_stateUncertainty(-0.5_0){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=-0.5, state_difference_weight=0)
genExperiments(f"Final_stateUncertainty(0_-0.5){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=-0.5)
genExperiments(f"Final_stateUncertainty(1_0){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=1, state_difference_weight=0)
genExperiments(f"Final_stateUncertainty(0_1){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=1)
genExperiments(f"Final_stateUncertainty(0.5_0.5){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0.5, state_difference_weight=0.5)
genExperiments(f"Final_stateUncertainty(0.5_0){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0.5, state_difference_weight=0)
genExperiments(f"Final_stateUncertainty(0_0.5){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=0.5)
"""



environments = ['bigfish']

for env in environments:
    genExperiments(f"Final_stateUncertainty(0and0){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=0)
    genExperiments(f"Final_stateUncertainty(0dot25and0){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0.25, state_difference_weight=0)
    genExperiments(f"Final_stateUncertainty(0and0dot25){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0, state_difference_weight=0.25)
    genExperiments(f"Final_stateUncertainty(0dot25and0dot25){env}", environment=env, uncertainty=1, state_difference=1, uncertainty_weight=0.25, state_difference_weight=0.25)

file.close()
