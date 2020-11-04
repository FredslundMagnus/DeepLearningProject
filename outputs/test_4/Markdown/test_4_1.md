User defined signal 2

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8254049: <test_4_1> in cluster <dcc> Exited

Job <test_4_1> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Tue Nov  3 01:15:33 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Nov  3 02:06:59 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov  3 02:06:59 2020
Terminated at Tue Nov  3 18:49:09 2020
Results reported at Tue Nov  3 18:49:09 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=25G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1000
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

TERM_RUNLIMIT: job killed after reaching LSF run time limit.
Exited with exit code 140.

Resource usage summary:

    CPU time :                                   16776.00 sec.
    Max Memory :                                 13062 MB
    Average Memory :                             12292.30 MB
    Total Requested Memory :                     25600.00 MB
    Delta Memory :                               12538.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   60130 sec.
    Turnaround time :                            63216 sec.

The output (if any) is above this job summary.

