/zhome/ee/d/137643/.lsbatch/1604335277.8253410.shell: line 14: 94460 Killed                  python main.py $LSB_PROJECT_NAME

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 8253410: <Discount_0.70_0> in cluster <dcc> Exited

Job <Discount_0.70_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Nov  2 17:41:17 2020
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 17:41:19 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 17:41:19 2020
Terminated at Mon Nov  2 17:41:43 2020
Results reported at Mon Nov  2 17:41:43 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=1G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 10
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

TERM_MEMLIMIT: job killed after reaching LSF memory usage limit.
Exited with exit code 137.

Resource usage summary:

    CPU time :                                   3.00 sec.
    Max Memory :                                 1024 MB
    Average Memory :                             717.67 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               0.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   117 sec.
    Turnaround time :                            26 sec.

The output (if any) is above this job summary.

User defined signal 2

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8253415: <Discount_0.70_0> in cluster <dcc> Exited

Job <Discount_0.70_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Nov  2 17:46:22 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 17:46:24 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 17:46:24 2020
Terminated at Mon Nov  2 17:56:40 2020
Results reported at Mon Nov  2 17:56:40 2020

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

TERM_RUNLIMIT: job killed after reaching LSF run time limit.
Exited with exit code 140.

Resource usage summary:

    CPU time :                                   581.00 sec.
    Max Memory :                                 9868 MB
    Average Memory :                             5793.50 MB
    Total Requested Memory :                     10240.00 MB
    Delta Memory :                               372.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   655 sec.
    Turnaround time :                            618 sec.

The output (if any) is above this job summary.

