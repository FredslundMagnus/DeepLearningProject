['Discount_0.70-1']
iscount_0.70-1
Discount_0.70-1 MME 0.9 0.9 0.001 0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-69>
Subject: Job 8003619: <Discount_0.70_1> in cluster <dcc> Done

Job <Discount_0.70_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 22:59:50 2020
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 22:59:51 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 22:59:51 2020
Terminated at Sat Oct  3 23:00:03 2020
Results reported at Sat Oct  3 23:00:03 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
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

Successfully completed.

Resource usage summary:

    CPU time :                                   1.09 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              1
    Max Threads :                                2
    Run time :                                   56 sec.
    Turnaround time :                            13 sec.

The output (if any) is above this job summary.

