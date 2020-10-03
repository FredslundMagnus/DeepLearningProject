['main.py', 'Discount_0.70-7', '-lossf', 'MME', '-discount', '0.7', '-lambd', '0.5', '-lr', '0.0001', '-dropout', '0']
['Discount_0.70-7']
iscount_0.70-7
Discount_0.70-7 MME 0.9 0.9 0.001 0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-66>
Subject: Job 8003637: <Discount_0.70_7> in cluster <dcc> Done

Job <Discount_0.70_7> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 23:02:00 2020
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 23:02:00 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 23:02:00 2020
Terminated at Sat Oct  3 23:02:04 2020
Results reported at Sat Oct  3 23:02:04 2020

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
    Max Memory :                                 52 MB
    Average Memory :                             18.00 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               972.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   113 sec.
    Turnaround time :                            4 sec.

The output (if any) is above this job summary.

iscount_0.70-7
lossf
ME
discount
.7
lambd
.5
lr
.0001
dropout

Discount_0.70-7 MME 0.7 0.5 0.0001 0.0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-66>
Subject: Job 8003650: <Discount_0.70_7> in cluster <dcc> Done

Job <Discount_0.70_7> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Sat Oct  3 23:06:14 2020
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Oct  3 23:06:15 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Oct  3 23:06:15 2020
Terminated at Sat Oct  3 23:06:29 2020
Results reported at Sat Oct  3 23:06:29 2020

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

    CPU time :                                   1.46 sec.
    Max Memory :                                 2 MB
    Average Memory :                             2.00 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               1022.00 MB
    Max Swap :                                   -
    Max Processes :                              3
    Max Threads :                                4
    Run time :                                   123 sec.
    Turnaround time :                            15 sec.

The output (if any) is above this job summary.

