Traceback (most recent call last):
  File "main.py", line 24, in <module>
    serverRun()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 27, in serverRun
    showParams(params)
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
  File "main.py", line 11, in main
    agent = Agent(**params)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/agent.py", line 23, in __init__
    self.memory = ReplayBuffer(memory)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/memory.py", line 10, in __init__
    self.reset(size)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/memory.py", line 53, in reset
    self.size, self.position, self.memory, self.rewads, self.dones, self.distribution = size, 0, [None for _ in range(size)], [None for _ in range(size)], [None for _ in range(size)], None
TypeError: 'float' object cannot be interpreted as an integer

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8366041: <Dist_LowMem_0> in cluster <dcc> Exited

Job <Dist_LowMem_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Nov 16 19:52:14 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov 16 19:52:44 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 16 19:52:44 2020
Terminated at Mon Nov 16 19:52:57 2020
Results reported at Mon Nov 16 19:52:57 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=30G]"
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

    CPU time :                                   3.60 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   15 sec.
    Turnaround time :                            43 sec.

The output (if any) is above this job summary.

