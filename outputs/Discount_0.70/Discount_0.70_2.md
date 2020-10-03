['main.py', 'Discount_0.70-2', '-lossf', 'MME', '-discount', '0.7', '-lambd', '0.5', '-lr', '0.0001', '-dropout', '0']
['Discount_0.70-2']
iscount_0.70-2
Discount_0.70-2 MME 0.9 0.9 0.001 0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-66>
Subject: Job 8003632: <Discount_0.70_2> in cluster <dcc> Done

Job <Discount_0.70_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 23:01:59 2020
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 23:01:59 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 23:01:59 2020
Terminated at Sat Oct  3 23:02:03 2020
Results reported at Sat Oct  3 23:02:03 2020

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

    CPU time :                                   1.08 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   113 sec.
    Turnaround time :                            4 sec.

The output (if any) is above this job summary.

