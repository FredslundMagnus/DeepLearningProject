[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NOPE_final_fruitbot-0
    Discount :                  0.995
    Environment :               fruitbot
    Hours :                     18
    Memory :                    500000
    Update every :              1000
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           1000
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0.1
    State difference :          0
    State difference weight :   0.0
    Minutes used :              1075 minutes.
    Hours used :                17 hours.

# Profiling

Traceback (most recent call last):
  File "main.py", line 108, in <module>
    serverRun()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 32, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 58, in profilingStats
    p = Stats('stats')
  File "/appl/python/3.8.2/lib/python3.8/pstats.py", line 96, in __init__
    self.init(arg)
  File "/appl/python/3.8.2/lib/python3.8/pstats.py", line 110, in init
    self.load_stats(arg)
  File "/appl/python/3.8.2/lib/python3.8/pstats.py", line 123, in load_stats
    with open(arg, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8585235: <NOPE_final_fruitbot_0> in cluster <dcc> Exited

Job <NOPE_final_fruitbot_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Dec 23 17:42:09 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Dec 23 17:42:10 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 23 17:42:10 2020
Terminated at Thu Dec 24 11:37:40 2020
Results reported at Thu Dec 24 11:37:40 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=60G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   68227.00 sec.
    Max Memory :                                 55675 MB
    Average Memory :                             54991.71 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5765.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64623 sec.
    Turnaround time :                            64531 sec.

The output (if any) is above this job summary.

