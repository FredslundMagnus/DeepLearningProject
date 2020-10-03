['Discount_0.70-7']
iscount_0.70-7
Discount_0.70-7 MME 0.9 0.9 0.001 0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-66>
Subject: Job 8003625: <Discount_0.70_7> in cluster <dcc> Done

Job <Discount_0.70_7> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 22:59:51 2020
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 22:59:53 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 22:59:53 2020
Terminated at Sat Oct  3 22:59:58 2020
Results reported at Sat Oct  3 22:59:58 2020

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
    Max Memory :                                 48 MB
    Average Memory :                             17.00 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               976.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   51 sec.
    Turnaround time :                            7 sec.

The output (if any) is above this job summary.

