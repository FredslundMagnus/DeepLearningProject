import cProfile
from Utils.debug import checkServer, getvals, profilingStats, Timer, enablePrint, disablePrint, showParams

isServer = checkServer()

defaults = {
    'name': "Agent",
    'lossf': 'MME',
    'discount': 0.9,
    'lambd': 0.9,
    'lr': 0.001,
    'dropout': 0,
}

params = getvals(defaults) if isServer else None


def debugger():
    disablePrint()
    timer = Timer(lambda: cProfile.run(f'main_function()', 'stats'))
    enablePrint()
    showParams(timer)
    profilingStats()
