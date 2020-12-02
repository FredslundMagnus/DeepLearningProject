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
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 8451045: <UUncertainty+Avoid_State-1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State-1and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 12:55:31 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 12:57:08 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 12:57:08 2020
Terminated at Sun Nov 29 12:57:12 2020
Results reported at Sun Nov 29 12:57:12 2020

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

    CPU time :                                   1.13 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   4 sec.
    Turnaround time :                            101 sec.

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
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 8451072: <UUncertainty+Avoid_State-1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State-1and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:13:24 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:31:48 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:31:48 2020
Terminated at Sun Nov 29 13:31:52 2020
Results reported at Sun Nov 29 13:31:52 2020

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

    CPU time :                                   1.13 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   3 sec.
    Turnaround time :                            1108 sec.

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
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 8451093: <UUncertainty+Avoid_State-1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State-1and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:34:53 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:49:34 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:49:34 2020
Terminated at Sun Nov 29 13:49:37 2020
Results reported at Sun Nov 29 13:49:37 2020

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

    CPU time :                                   1.06 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   2 sec.
    Turnaround time :                            884 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/environments.py", line 72, in __init__
    agent.hasEncoder
AttributeError: 'NoneType' object has no attribute 'hasEncoder'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "main.py", line 107, in <module>
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
  File "main.py", line 95, in main
    env = Environments(render=False, envs=[environment for _ in range(total_agents)])
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/environments.py", line 74, in __init__
    agent.hasEncoder = False
AttributeError: 'NoneType' object has no attribute 'hasEncoder'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8451137: <UUncertainty+Avoid_State-1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State-1and0fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 14:32:56 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:06:02 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:06:02 2020
Terminated at Sun Nov 29 15:06:20 2020
Results reported at Sun Nov 29 15:06:20 2020

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

    CPU time :                                   5.00 sec.
    Max Memory :                                 1240 MB
    Average Memory :                             1240.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               60200.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   20 sec.
    Turnaround time :                            2004 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "main.py", line 107, in <module>
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
  File "main.py", line 100, in main
    act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 72, in chooseMulti
    vals = self.convert_values(vals, uncertainties, avoid_trace)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 119, in convert_values
    return vals + (self.uncertainty_weight * uncertainties * self.uncertainty) + (self.state_difference_weight * state_differences * self.state_difference)
TypeError: only integer tensors of a single element can be converted to an index

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8451175: <UUncertainty+Avoid_State-1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State-1and0fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 15:23:31 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:25:43 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:25:43 2020
Terminated at Sun Nov 29 15:25:57 2020
Results reported at Sun Nov 29 15:25:57 2020

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

    CPU time :                                   7.00 sec.
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               61436.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   15 sec.
    Turnaround time :                            146 sec.

The output (if any) is above this job summary.


    Name :                      UUncertainty+Avoid_State-1and0fruitbot-0
    Discount :                  0.995
    Environment :               fruitbot
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        -1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      15238860173 function calls (14987050883 primitive calls) in 82519.06 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82519.057 82519.057 {built-in method builtins.exec}
                      1    0.050    0.050 82519.057 82519.057 <string>:1(<module>)
                      1  562.463  562.463 82519.006 82519.006 main.py:93(main)
                2493412  189.854    0.000 56744.200    0.023 agent.py:75(learn)
                2492912  671.857    0.000 55506.965    0.022 agent.py:85(TD_learn)
                2492912  180.838    0.000 28615.786    0.011 memory.py:35(sample_distribution)
                2492912  327.489    0.000 27786.247    0.011 helpers.py:15(stack)
        264268172/12465560 1135.784    0.000 15693.795    0.001 module.py:715(_call_impl)
                7479236  231.484    0.000 14807.267    0.002 agent.py:194(forward)
               24931228 13747.198    0.001 13747.233    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               32409356 13472.026    0.000 13472.026    0.000 {built-in method cat}
               39889592  303.394    0.000 10250.821    0.000 container.py:115(forward)
                2493412   73.290    0.000 9709.782    0.004 environments.py:83(step)
                2493412  194.756    0.000 8293.024    0.003 agent.py:63(chooseMulti)
                2492912   26.528    0.000 7697.963    0.003 grad_mode.py:23(decorate_context)
                2492912  265.443    0.000 7638.724    0.003 adam.py:55(step)
                2493412   91.677    0.000 7020.568    0.003 agent.py:51(rememberMulti)
                2493412  231.459    0.000 6555.521    0.003 agent.py:55(<listcomp>)
              337561959 6452.547    0.000 6452.547    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2492912 1407.650    0.001 6268.322    0.003 functional.py:53(adam)
               50398928 1465.154    0.000 5876.917    0.000 helpers.py:8(clean)
                2493412   67.407    0.000 5873.795    0.002 environments.py:85(<listcomp>)
                2492912   26.962    0.000 5422.385    0.002 tensor.py:181(backward)
                2492912   17.470    0.000 5395.423    0.002 __init__.py:68(backward)
                2492912 5307.786    0.002 5307.786    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               57877664 5036.912    0.000 5036.912    0.000 {built-in method as_tensor}
               44875416   83.009    0.000 3769.583    0.000 conv.py:422(forward)
               44875416   99.685    0.000 3647.445    0.000 conv.py:414(_conv_forward)
               44875416 3530.674    0.000 3530.674    0.000 {built-in method conv2d}
                2493412   53.602    0.000 3504.524    0.001 environments.py:84(<listcomp>)
               49868240  189.110    0.000 3450.921    0.000 interop.py:274(step)
               59834888  127.025    0.000 3171.056    0.000 linear.py:92(forward)
               59834888  324.003    0.000 2981.277    0.000 functional.py:1669(linear)
                7479242  432.754    0.000 2321.124    0.000 rnn.py:110(flatten_parameters)
                7479236   91.875    0.000 1994.123    0.000 rnn.py:555(forward)
              553426572 1182.163    0.000 1993.166    0.000 tensor.py:933(grad)
               49868240   24.259    0.000 1875.748    0.000 wrapper.py:25(act)
               49868240   63.923    0.000 1851.489    0.000 env.py:197(act)
                7479236 1801.857    0.000 1801.857    0.000 {built-in method lstm}
                2493412   93.086    0.000 1768.356    0.001 agent.py:73(<listcomp>)
               49868240 1747.353    0.000 1752.622    0.000 libenv.py:352(act)
               52354652 1721.894    0.000 1721.894    0.000 {built-in method addmm}
                2492912  161.324    0.000 1691.958    0.001 optimizer.py:167(zero_grad)
               87258420   82.431    0.000 1500.231    0.000 activation.py:713(forward)
               49868240  145.639    0.000 1432.495    0.000 exploration.py:33(epsilonGreedy)
               87258420  121.268    0.000 1417.799    0.000 functional.py:1292(leaky_relu)
                7479239 1364.594    0.000 1364.594    0.000 {built-in method _cudnn_rnn_flatten_weight}
               87258420 1285.059    0.000 1285.059    0.000 {built-in method torch._C._nn.leaky_relu}
              149574720 1283.580    0.000 1283.580    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              149574720 1082.355    0.000 1082.355    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   4986    1.890    0.000 1047.381    0.210 agent.py:121(update_target_network)
              688049090  366.800    0.000 1036.446    0.000 overrides.py:1073(has_torch_function)
              100267168   78.832    0.000  864.406    0.000 extract_dict_ob.py:9(observe)
              100267168   45.644    0.000  785.574    0.000 wrapper.py:19(observe)
              100267168  191.517    0.000  739.930    0.000 libenv.py:344(observe)
               74787360  700.953    0.000  700.953    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   4986  183.652    0.037  671.450    0.135 memory.py:45(update_distribution)
               74787360  649.007    0.000  649.007    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              752869826  261.040    0.000  633.762    0.000 {built-in method builtins.any}
                2493412    6.750    0.000  607.866    0.000 agent.py:212(avoid_similar_state)
               74787360  598.784    0.000  598.784    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               52371124  566.021    0.000  566.021    0.000 {built-in method numpy.array}
              150135408  161.056    0.000  543.043    0.000 libenv.py:281(_maybe_copy_dict)
               74787360  521.657    0.000  521.657    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              450411210  469.258    0.000  469.258    0.000 {method 'copy' of 'numpy.ndarray' objects}
               59834888  446.057    0.000  446.057    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7480236   16.025    0.000  432.349    0.000 functional.py:74(split)
                7480236   32.243    0.000  415.298    0.000 tensor.py:460(split)
               34904591  375.091    0.000  401.309    0.000 module.py:781(__setattr__)
              373895804  392.820    0.000  392.820    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               49868240   42.161    0.000  385.441    0.000 wrapper.py:22(get_info)
               11515721  149.833    0.000  385.309    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7480236  381.420    0.000  381.420    0.000 {function Tensor.split at 0x7f0af9888d30}
               49868240  374.901    0.000  374.901    0.000 memory.py:17(inner)
             1435933068  299.216    0.000  370.280    0.000 overrides.py:1086(<genexpr>)
               74787360  366.437    0.000  366.437    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               49868240  178.003    0.000  343.281    0.000 libenv.py:363(get_info)
                2492912  263.007    0.000  341.471    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   9972  263.681    0.026  318.156    0.032 {built-in method _pickle.loads}
               25524494   24.918    0.000  279.058    0.000 <__array_function__ internals>:2(prod)
                2493412   27.566    0.000  258.174    0.000 environments.py:86(<listcomp>)
                7479236   19.699    0.000  252.865    0.000 pooling.py:152(forward)
               25524534   18.825    0.000  250.045    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               49868240  242.775    0.000  242.775    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               44874416  240.099    0.000  240.099    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                7479236   13.679    0.000  233.166    0.000 _jit_internal.py:257(fn)
               25524494   32.204    0.000  231.220    0.000 fromnumeric.py:2881(prod)
               49868260   35.919    0.000  230.622    0.000 environments.py:89(reset)
                9971648  226.864    0.000  226.864    0.000 {built-in method gather}
                7480236  222.096    0.000  222.096    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2493412  220.757    0.000  220.757    0.000 agent.py:115(convert_values)
                7479236   15.263    0.000  218.263    0.000 functional.py:574(_max_pool2d)
                2492912  211.433    0.000  211.433    0.000 memory.py:43(<listcomp>)
               29916956  180.837    0.000  203.424    0.000 __init__.py:67(is_acceptable)
                2872346  202.608    0.000  202.608    0.000 {built-in method tensor}
                7479236  202.014    0.000  202.014    0.000 {built-in method max_pool2d}
               74787630   91.163    0.000  201.989    0.000 tensor.py:596(__hash__)
               25524494   58.804    0.000  199.015    0.000 fromnumeric.py:70(_wrapreduction)
              264668174  192.686    0.000  192.906    0.000 module.py:765(__getattr__)
                2492912    7.323    0.000  169.869    0.000 loss.py:445(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8452491: <UUncertainty+Avoid_State-1and0fruitbot_0> in cluster <dcc> Done

Job <UUncertainty+Avoid_State-1and0fruitbot_0> was submitted from host <n-62-27-21> by user <s183914> in cluster <dcc> at Sun Nov 29 17:39:37 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 19:43:27 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 19:43:27 2020
Terminated at Mon Nov 30 18:38:51 2020
Results reported at Mon Nov 30 18:38:51 2020

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

Successfully completed.

Resource usage summary:

    CPU time :                                   85056.00 sec.
    Max Memory :                                 54861 MB
    Average Memory :                             54134.93 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6579.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82525 sec.
    Turnaround time :                            89954 sec.

The output (if any) is above this job summary.

  File "main.py", line 92
    if fortheloveofgod =!=!= CRASH:
                       ^
SyntaxError: invalid syntax

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8458904: <UUncertainty+Avoid_State-1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State-1and0fruitbot_0> was submitted from host <n-62-30-8> by user <s183914> in cluster <dcc> at Mon Nov 30 20:41:54 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec  2 01:27:23 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec  2 01:27:23 2020
Terminated at Wed Dec  2 01:27:24 2020
Results reported at Wed Dec  2 01:27:24 2020

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

    CPU time :                                   0.24 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   3 sec.
    Turnaround time :                            103530 sec.

The output (if any) is above this job summary.

