Traceback (most recent call last):
  File "main.py", line 2, in <module>
    from Utils.server import isServer, params, serverRun, saveAgent
ImportError: cannot import name 'saveAgent' from 'Utils.server' (/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/server.py)

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8253615: <Discount_0.70_0> in cluster <dcc> Exited

Job <Discount_0.70_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Nov  2 18:19:28 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 18:19:29 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 18:19:29 2020
Terminated at Mon Nov  2 18:19:31 2020
Results reported at Mon Nov  2 18:19:31 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=10G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 10
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.34 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     10240.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   65 sec.
    Turnaround time :                            3 sec.

The output (if any) is above this job summary.

