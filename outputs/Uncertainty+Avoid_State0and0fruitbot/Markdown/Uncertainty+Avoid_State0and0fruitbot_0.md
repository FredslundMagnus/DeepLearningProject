Traceback (most recent call last):
  File "main.py", line 10, in <module>
    from pynput import keyboard
ModuleNotFoundError: No module named 'pynput'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8450178: <Uncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Exited

Job <Uncertainty+Avoid_State0and0fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Nov 28 19:27:54 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Nov 28 23:06:18 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 28 23:06:18 2020
Terminated at Sat Nov 28 23:06:28 2020
Results reported at Sat Nov 28 23:06:28 2020

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   1.11 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   10 sec.
    Turnaround time :                            13114 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "main.py", line 10, in <module>
    from pynput import keyboard
ModuleNotFoundError: No module named 'pynput'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8450626: <Uncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Exited

Job <Uncertainty+Avoid_State0and0fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 00:46:31 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 02:31:20 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 02:31:20 2020
Terminated at Sun Nov 29 02:31:34 2020
Results reported at Sun Nov 29 02:31:34 2020

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   2.01 sec.
    Max Memory :                                 69 MB
    Average Memory :                             55.67 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               61371.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   14 sec.
    Turnaround time :                            6303 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "main.py", line 10, in <module>
    from pynput import keyboard
  File "/zhome/ea/9/137501/Desktop/DeepAI/project-env/lib/python3.8/site-packages/pynput/__init__.py", line 40, in <module>
    from . import keyboard
  File "/zhome/ea/9/137501/Desktop/DeepAI/project-env/lib/python3.8/site-packages/pynput/keyboard/__init__.py", line 31, in <module>
    backend = backend(__name__)
  File "/zhome/ea/9/137501/Desktop/DeepAI/project-env/lib/python3.8/site-packages/pynput/_util/__init__.py", line 76, in backend
    raise ImportError('this platform is not supported: {}'.format(
ImportError: this platform is not supported: ('failed to acquire X connection: Bad display name ""', DisplayNameError(''))

Try one of the following resolutions:

 * Please make sure that you have an X server running, and that the DISPLAY environment variable is set correctly

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8451010: <Uncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Exited

Job <Uncertainty+Avoid_State0and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 12:19:51 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 12:32:17 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 12:32:17 2020
Terminated at Sun Nov 29 12:32:35 2020
Results reported at Sun Nov 29 12:32:35 2020

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   2.19 sec.
    Max Memory :                                 63 MB
    Average Memory :                             61.33 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               61377.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   19 sec.
    Turnaround time :                            764 sec.

The output (if any) is above this job summary.
