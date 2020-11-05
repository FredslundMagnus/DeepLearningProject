Traceback (most recent call last):
  File "main.py", line 45, in <module>
    serverRun()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 19, in serverRun
    showParams()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 101, in showParams
    timer = Timer()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 68, in __init__
    cProfile.run("main()", 'stats')
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.2/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 1, in <module>
  File "main.py", line 40, in main
    print(f"\n{i}. Total reward: {int(total_rew)}")
NameError: name 'i' is not defined
fruitbot_test-0 0.99 fruitbot 100000.0 100000

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 8265923: <fruitbot_test_0> in cluster <dcc> Exited

Job <fruitbot_test_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Thu Nov  5 18:30:54 2020
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov  5 18:42:29 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov  5 18:42:29 2020
Terminated at Thu Nov  5 18:42:44 2020
Results reported at Thu Nov  5 18:42:44 2020

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
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   6.00 sec.
    Max Memory :                                 2044 MB
    Average Memory :                             2044.00 MB
    Total Requested Memory :                     25600.00 MB
    Delta Memory :                               23556.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   16 sec.
    Turnaround time :                            710 sec.

The output (if any) is above this job summary.

