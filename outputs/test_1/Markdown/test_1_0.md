Traceback (most recent call last):
  File "main.py", line 42, in <module>
    serverRun()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 20, in serverRun
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
  File "main.py", line 41, in main
    saveAgent(agent, name)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 25, in saveAgent
    pickle.dump(agent, open(f"outputs/{'_'.join(name.split('_')[:-1])}/Agents/{name}.obj", "wb"))
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/test/Agents/test_1-0.obj'
test_1-0 MME 0.12 0.3 0.0001 0.0

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8253643: <test_1_0> in cluster <dcc> Exited

Job <test_1_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Nov  2 18:25:18 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 18:25:19 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 18:25:19 2020
Terminated at Mon Nov  2 18:26:30 2020
Results reported at Mon Nov  2 18:26:30 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=10G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 10
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   64.00 sec.
    Max Memory :                                 3133 MB
    Average Memory :                             2826.67 MB
    Total Requested Memory :                     10240.00 MB
    Delta Memory :                               7107.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   76 sec.
    Turnaround time :                            72 sec.

The output (if any) is above this job summary.

