Traceback (most recent call last):
  File "main.py", line 2, in <module>
    from environments import Environments
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/environments.py", line 1, in <module>
    import gym
ModuleNotFoundError: No module named 'gym'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8423588: <NoNormalizationYesUncertainty_0> in cluster <dcc> Exited

Job <NoNormalizationYesUncertainty_0> was submitted from host <n-62-30-7> by user <s183914> in cluster <dcc> at Tue Nov 24 20:07:34 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Nov 24 20:11:10 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 20:11:10 2020
Terminated at Tue Nov 24 20:11:11 2020
Results reported at Tue Nov 24 20:11:11 2020

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

    CPU time :                                   0.26 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   2 sec.
    Turnaround time :                            217 sec.

The output (if any) is above this job summary.

