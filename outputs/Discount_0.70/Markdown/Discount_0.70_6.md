Discount_0.70-6 MME 0.12 0.3 0.0001 0.0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-66>
Subject: Job 8003696: <Discount_0.70_6> in cluster <dcc> Done

Job <Discount_0.70_6> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 23:20:13 2020
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 23:20:15 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 23:20:15 2020
Terminated at Sat Oct  3 23:20:27 2020
Results reported at Sat Oct  3 23:20:27 2020

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

    CPU time :                                   1.22 sec.
    Max Memory :                                 1 MB
    Average Memory :                             0.67 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               1023.00 MB
    Max Swap :                                   -
    Max Processes :                              2
    Max Threads :                                4
    Run time :                                   2 sec.
    Turnaround time :                            14 sec.

The output (if any) is above this job summary.

Discount_0.70-6 MME 0.12 0.3 0.0001 0.0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-66>
Subject: Job 8003708: <Discount_0.70_6> in cluster <dcc> Done

Job <Discount_0.70_6> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 23:22:41 2020
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 23:22:43 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 23:22:43 2020
Terminated at Sat Oct  3 23:22:56 2020
Results reported at Sat Oct  3 23:22:56 2020

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

    CPU time :                                   1.36 sec.
    Max Memory :                                 2 MB
    Average Memory :                             2.00 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               1022.00 MB
    Max Swap :                                   -
    Max Processes :                              3
    Max Threads :                                4
    Run time :                                   19 sec.
    Turnaround time :                            15 sec.

The output (if any) is above this job summary.

