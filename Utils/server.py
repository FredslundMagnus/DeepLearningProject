import cProfile
from Utils.debug import checkServer, getvals, profilingStats, Timer, enablePrint, disablePrint

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


def debugger(nGames, addAgent, Thename, p, chooserfunction, env):
    disablePrint()
    explore, doTrain, impala, calcprobs, minmax, lossf, K, dropout, alpha, discount, lambd, lr, network, Features = p.explore, p.doTrain, p.ImpaleIsActivated, p.calcprobs, p.minimaxi, p.lossf, p.K, p.dropout, p.alpha, p.discount, p.lambd, p.lr, p.network, p.Features
    winNumber, maxRolls, Eatreward, basereward, stepreward = env.winNumber, env.maxRolls, env.Eatreward, env.basereward, env.stepreward
    timer = Timer(lambda: cProfile.run(f'controller.run(NGames={nGames}, AddAgent={addAgent}, UI=False)', 'stats'))
    enablePrint()
    print(f"# Parameters for {Thename}\n")

    print(f"    Play for :                  {nGames} games.")
    print(f"      Add Agent every :         {addAgent} game.")
    print(f"      Game length :             {maxRolls} rolls.")
    print(f"      Win with :                {winNumber} ants.")
    print(f"      Eatreward :               {Eatreward}.")
    print(f"      Basereward :              {basereward}.")
    print(f"      Stepreward :              {stepreward}.\n")

    print(f"      Features :                {Features}.\n")

    if network is not None:
        print(f"      Network :                 {network}.\n")

    print(f'    Explore enabled :           {str(explore)}.')
    print(f'      K :                       {str(K)}.')
    print(f'      Dropout :                 {str(dropout)}.\n')

    print(f'    DoTrain enabled :           {str(doTrain)}.')
    print(f'      Lossfunction  :           {str(lossf)}.')
    print(f'      Value of alpha :          {str(alpha)}.')
    print(f'      Value of discount :       {str(discount)}.')
    print(f'      Value of lambda :         {str(lambd)}.')
    print(f'      Learningrate :            {str(lr)}.\n')

    print(f'    Impala enabled :            {str(impala)}.')
    print(f'      historyLength :           {str(p.historyLength)}.')
    print(f'      startAfterNgames :        {str(p.startAfterNgames)}.')
    print(f'      batchSize :               {str(p.batchSize)}.')
    print(f'      sampleLenth :             {str(p.sampleLenth)}.\n')

    print(f'    Minimax enabled :           {str(minmax)}.')
    print(f'      TopNvalues :              {str(p.TopNvalues)}.')
    print(f'      cutOffdepth :             {str(p.cutOffdepth)}.')
    print(f'      ValueCutOff :             {str(p.ValueCutOff)}.')
    print(f'      ValueDiffCutOff :         {str(p.ValueDiffCutOff)}.')
    print(f'      ProbabilityCutOff :       {str(p.ProbabilityCutOff)}.\n')

    print(f'    Calcprobs enabled :         {str(calcprobs)}.\n')

    print(f'    Chooserfunction :           {str(chooserfunction)}.\n')

    print(f'    Minutes used :              {timer.minutes} minutes.')
    print(f'    Hours used :                {timer.hours} hours.\n')

    profilingStats()
