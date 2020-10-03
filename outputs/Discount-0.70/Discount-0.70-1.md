Discount-0.70-1 MME 0.9 0.9 0.001 0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-69>
Subject: Job 8003580: <Discount-0.70-1> in cluster <dcc> Done

Job <Discount-0.70-1> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Sat Oct  3 22:45:07 2020
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 22:45:08 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 22:45:08 2020
Terminated at Sat Oct  3 22:45:20 2020
Results reported at Sat Oct  3 22:45:20 2020

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

    CPU time :                                   1.15 sec.
    Max Memory :                                 1 MB
    Average Memory :                             1.00 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               1023.00 MB
    Max Swap :                                   -
    Max Processes :                              1
    Max Threads :                                2
    Run time :                                   87 sec.
    Turnaround time :                            13 sec.

The output (if any) is above this job summary.

Discount-0.70-1 MME 0.9 0.9 0.001 0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-69>
Subject: Job 8003606: <Discount-0.70-1> in cluster <dcc> Done

Job <Discount-0.70-1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 22:56:45 2020
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 22:56:46 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 22:56:46 2020
Terminated at Sat Oct  3 22:56:49 2020
Results reported at Sat Oct  3 22:56:49 2020

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

    CPU time :                                   0.96 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   54 sec.
    Turnaround time :                            4 sec.

The output (if any) is above this job summary.

