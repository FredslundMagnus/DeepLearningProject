import cProfile
import sys
import time
from Utils.debug import profilingStats

defaults = {
    'lossf': 'MME',
    'discount': 0.9,
    'lambd': 0.9,
    'lr': 0.001,
    'dropout': 0,
}


def getvals(args):
    for i, s_ in enumerate(args):
        s = s_[1:]
        if s in defaults:
            try:
                defaults[s] = float(args[i + 1])
            except:
                defaults[s] = args[i + 1]
    return tuple([args[0].split(' ')[0]] + list(defaults.values()))


def debugger(nGames, addAgent, Thename, p, chooserfunction, env):
    explore, doTrain, impala, calcprobs, minmax, lossf, K, dropout, alpha, discount, lambd, lr, network, Features = p.explore, p.doTrain, p.ImpaleIsActivated, p.calcprobs, p.minimaxi, p.lossf, p.K, p.dropout, p.alpha, p.discount, p.lambd, p.lr, p.network, p.Features
    winNumber, maxRolls, Eatreward, basereward, stepreward = env.winNumber, env.maxRolls, env.Eatreward, env.basereward, env.stepreward
    start = time.time()
    cProfile.run(f'controller.run(NGames={nGames}, AddAgent={addAgent}, UI=False)', 'stats')
    end = time.time()
    sys.stdout = sys.__stdout__
    print(f"# Parameters for {Thename}\n")

    print(f"    Use the agent :             {sys.argv[4]}.\n")

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

    print(f'    Minutes used :              {int((end-start)//60)} minutes.')
    print(f'    Hours used :                {int((end-start)//3600)} hours.\n')

    profilingStats()
