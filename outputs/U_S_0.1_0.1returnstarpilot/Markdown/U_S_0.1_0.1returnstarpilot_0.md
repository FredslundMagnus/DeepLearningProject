Traceback (most recent call last):
  File "main.py", line 109, in <module>
    serverRun()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 31, in serverRun
    showParams(params)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 101, in showParams
    timer = Timer()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 68, in __init__
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
  File "main.py", line 105, in main
    agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done, before_trace, after_trace)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 60, in rememberMulti
    [self.remember(obs_old.cpu(), act, obs.cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done), before_trace.detach().cpu(), state_diff_label.detach().cpu()) for obs_old, act, obs, rew, h0, c0, hn, cn, done, before_trace, state_diff_label in zip(*args)]
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 60, in <listcomp>
    [self.remember(obs_old.cpu(), act, obs.cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done), before_trace.detach().cpu(), state_diff_label.detach().cpu()) for obs_old, act, obs, rew, h0, c0, hn, cn, done, before_trace, state_diff_label in zip(*args)]
KeyboardInterrupt

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 8578471: <U_S_0.1_0.1returnstarpilot_0> in cluster <dcc> Exited

Job <U_S_0.1_0.1returnstarpilot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec 20 03:01:50 2020
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Dec 20 08:08:46 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec 20 08:08:46 2020
Terminated at Sun Dec 20 18:14:58 2020
Results reported at Sun Dec 20 18:14:58 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=60G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

TERM_ADMIN: job killed by root or an administrator.
Exited with exit code 130.

Resource usage summary:

    CPU time :                                   38407.00 sec.
    Max Memory :                                 56417 MB
    Average Memory :                             55390.57 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5023.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   36373 sec.
    Turnaround time :                            54788 sec.

The output (if any) is above this job summary.

