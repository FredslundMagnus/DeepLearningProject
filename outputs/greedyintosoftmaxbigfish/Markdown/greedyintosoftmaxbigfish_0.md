Traceback (most recent call last):
  File "main.py", line 10, in <module>
    from pynput import keyboard
ModuleNotFoundError: No module named 'pynput'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8447015: <greedyintosoftmaxbigfish_0> in cluster <dcc> Exited

Job <greedyintosoftmaxbigfish_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 13:06:21 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Nov 28 15:12:25 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 28 15:12:25 2020
Terminated at Sat Nov 28 15:12:37 2020
Results reported at Sat Nov 28 15:12:37 2020

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

    CPU time :                                   1.37 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   11 sec.
    Turnaround time :                            93976 sec.

The output (if any) is above this job summary.

