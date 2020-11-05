from agent import Agent
import time
from os import listdir, remove
from os.path import isfile, getsize
import pickle

start = time.time()


def updateMemory(agent):
    location = 'trainlocally/multi'
    fileNames = [f"{location}/Data/{f}" for f in listdir(f"{location}/Data/") if isfile(f"{location}/Data/{f}")]
    if len(fileNames) == 0:
        return
    fileNames.sort(key=lambda x: getsize(x), reverse=True)
    fileName = fileNames[0]
    if getsize(fileName) == 0:
        return
    with open(fileName, 'rb') as file:
        memory = pickle.load(file)
        remove(fileName)
    for mem in memory:
        agent.remember(*mem)


agent = Agent(memory=30000)
while time.time() - start < 200:
    updateMemory(agent)
    print(1)
    time.sleep(1)
