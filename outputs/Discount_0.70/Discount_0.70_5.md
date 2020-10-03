Discount_0.70-5 MME 0.2 0.3 0.0001 0.0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-66>
Subject: Job 8003673: <Discount_0.70_5> in cluster <dcc> Done

Job <Discount_0.70_5> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 23:10:24 2020
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 23:10:26 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 23:10:26 2020
Terminated at Sat Oct  3 23:10:30 2020
Results reported at Sat Oct  3 23:10:30 2020

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

    CPU time :                                   1.23 sec.
    Max Memory :                                 2 MB
    Average Memory :                             0.67 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               1022.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   81 sec.
    Turnaround time :                            6 sec.

The output (if any) is above this job summary.
