Discount_0.70-1 MME 0.12 0.3 0.0001 0.0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-69>
Subject: Job 8003691: <Discount_0.70_1> in cluster <dcc> Done

Job <Discount_0.70_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 23:20:12 2020
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 23:20:13 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 23:20:13 2020
Terminated at Sat Oct  3 23:20:25 2020
Results reported at Sat Oct  3 23:20:25 2020

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

    CPU time :                                   0.91 sec.
    Max Memory :                                 2 MB
    Average Memory :                             1.33 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               1022.00 MB
    Max Swap :                                   -
    Max Processes :                              3
    Max Threads :                                4
    Run time :                                   107 sec.
    Turnaround time :                            13 sec.

The output (if any) is above this job summary.

Discount_0.70-1 MME 0.12 0.3 0.0001 0.0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-69>
Subject: Job 8003703: <Discount_0.70_1> in cluster <dcc> Done

Job <Discount_0.70_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 23:22:40 2020
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 23:22:41 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 23:22:41 2020
Terminated at Sat Oct  3 23:22:55 2020
Results reported at Sat Oct  3 23:22:55 2020

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

    CPU time :                                   0.89 sec.
    Max Memory :                                 1 MB
    Average Memory :                             1.00 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               1023.00 MB
    Max Swap :                                   -
    Max Processes :                              1
    Max Threads :                                2
    Run time :                                   7 sec.
    Turnaround time :                            15 sec.

The output (if any) is above this job summary.
