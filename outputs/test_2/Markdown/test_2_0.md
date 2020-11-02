User defined signal 2

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 8253832: <test_2_0> in cluster <dcc> Exited

Job <test_2_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Mon Nov  2 19:24:22 2020
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 19:24:23 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 19:24:23 2020
Terminated at Mon Nov  2 19:34:25 2020
Results reported at Mon Nov  2 19:34:25 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=20G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 10
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

TERM_RUNLIMIT: job killed after reaching LSF run time limit.
Exited with exit code 140.

Resource usage summary:

    CPU time :                                   150.00 sec.
    Max Memory :                                 4443 MB
    Average Memory :                             2827.50 MB
    Total Requested Memory :                     20480.00 MB
    Delta Memory :                               16037.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   624 sec.
    Turnaround time :                            603 sec.

The output (if any) is above this job summary.

