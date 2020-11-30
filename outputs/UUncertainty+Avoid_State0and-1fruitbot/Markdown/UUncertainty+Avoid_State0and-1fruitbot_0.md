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
Subject: Job 8451043: <UUncertainty+Avoid_State0and-1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and-1fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 12:55:31 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 12:56:58 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 12:56:58 2020
Terminated at Sun Nov 29 12:57:01 2020
Results reported at Sun Nov 29 12:57:01 2020

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
    Turnaround time :                            90 sec.

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
Subject: Job 8451070: <UUncertainty+Avoid_State0and-1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and-1fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:13:23 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:18:31 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:18:31 2020
Terminated at Sun Nov 29 13:18:37 2020
Results reported at Sun Nov 29 13:18:37 2020

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

    CPU time :                                   1.51 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   7 sec.
    Turnaround time :                            314 sec.

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
Subject: Job 8451091: <UUncertainty+Avoid_State0and-1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and-1fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:34:53 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:49:16 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:49:16 2020
Terminated at Sun Nov 29 13:49:19 2020
Results reported at Sun Nov 29 13:49:19 2020

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
    Run time :                                   5 sec.
    Turnaround time :                            866 sec.

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
Subject: Job 8451135: <UUncertainty+Avoid_State0and-1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and-1fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 14:32:55 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:05:32 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:05:32 2020
Terminated at Sun Nov 29 15:05:43 2020
Results reported at Sun Nov 29 15:05:43 2020

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

    CPU time :                                   3.98 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   12 sec.
    Turnaround time :                            1968 sec.

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
Subject: Job 8451173: <UUncertainty+Avoid_State0and-1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and-1fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 15:23:31 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:25:12 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:25:12 2020
Terminated at Sun Nov 29 15:25:26 2020
Results reported at Sun Nov 29 15:25:26 2020

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
    Run time :                                   14 sec.
    Turnaround time :                            115 sec.

The output (if any) is above this job summary.


    Name :                      UUncertainty+Avoid_State0and-1fruitbot-0
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   -1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      15472883792 function calls (15217110454 primitive calls) in 82515.50 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82515.503 82515.503 {built-in method builtins.exec}
                      1    0.077    0.077 82515.503 82515.503 <string>:1(<module>)
                      1  510.321  510.321 82515.425 82515.425 main.py:93(main)
                2532660  176.480    0.000 55842.857    0.022 agent.py:75(learn)
                2532160  657.158    0.000 54609.520    0.022 agent.py:85(TD_learn)
                2532160  167.850    0.000 27486.969    0.011 memory.py:35(sample_distribution)
                2532160  252.598    0.000 26667.187    0.011 helpers.py:15(stack)
        268428460/12661800 1154.258    0.000 15623.799    0.001 module.py:715(_call_impl)
                7596980  220.456    0.000 14729.810    0.002 agent.py:194(forward)
               25323708 13583.291    0.001 13583.357    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               32919580 12666.272    0.000 12666.272    0.000 {built-in method cat}
               40517560  292.979    0.000 10395.110    0.000 container.py:115(forward)
                2532660   74.527    0.000 10380.145    0.004 environments.py:83(step)
                2532660  198.003    0.000 8410.587    0.003 agent.py:63(chooseMulti)
                2532160   24.214    0.000 8004.498    0.003 grad_mode.py:23(decorate_context)
                2532160  261.800    0.000 7948.952    0.003 adam.py:55(step)
                2532660  100.312    0.000 7162.067    0.003 agent.py:51(rememberMulti)
                2532660  254.266    0.000 6645.584    0.003 agent.py:55(<listcomp>)
                2532160 1484.438    0.001 6543.918    0.003 functional.py:53(adam)
              343011238 6508.983    0.000 6508.983    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2532660   69.515    0.000 6449.816    0.003 environments.py:85(<listcomp>)
               51000114 1674.730    0.000 6430.072    0.000 helpers.py:8(clean)
                2532160   22.691    0.000 5516.927    0.002 tensor.py:181(backward)
                2532160   14.314    0.000 5494.236    0.002 __init__.py:68(backward)
                2532160 5410.309    0.002 5410.309    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               58596594 5307.178    0.000 5307.178    0.000 {built-in method as_tensor}
               45581880   83.792    0.000 3773.302    0.000 conv.py:422(forward)
               45581880   92.651    0.000 3649.589    0.000 conv.py:414(_conv_forward)
                2532660   54.881    0.000 3620.834    0.001 environments.py:84(<listcomp>)
               50653200  201.603    0.000 3565.953    0.000 interop.py:274(step)
               45581880 3539.743    0.000 3539.743    0.000 {built-in method conv2d}
               60776840  129.750    0.000 3240.070    0.000 linear.py:92(forward)
               60776840  330.430    0.000 3045.608    0.000 functional.py:1669(linear)
                7596986  393.965    0.000 2212.974    0.000 rnn.py:110(flatten_parameters)
              562139628 1206.426    0.000 2070.755    0.000 tensor.py:933(grad)
               50653200   24.636    0.000 1930.020    0.000 wrapper.py:25(act)
                7596980   81.702    0.000 1906.614    0.000 rnn.py:555(forward)
               50653200   65.799    0.000 1905.384    0.000 env.py:197(act)
               50653200 1798.436    0.000 1803.573    0.000 libenv.py:352(act)
                2532160  162.483    0.000 1766.378    0.001 optimizer.py:167(zero_grad)
               53178860 1761.519    0.000 1761.519    0.000 {built-in method addmm}
                2532660   97.891    0.000 1750.283    0.001 agent.py:73(<listcomp>)
                7596980 1727.003    0.000 1727.003    0.000 {built-in method lstm}
               88632100   86.421    0.000 1532.656    0.000 activation.py:713(forward)
               88632100  114.639    0.000 1446.235    0.000 functional.py:1292(leaky_relu)
               50653200  154.265    0.000 1403.730    0.000 exploration.py:33(epsilonGreedy)
                7596983 1350.254    0.000 1350.254    0.000 {built-in method _cudnn_rnn_flatten_weight}
              151929600 1328.323    0.000 1328.323    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               88632100 1320.009    0.000 1320.009    0.000 {built-in method torch._C._nn.leaky_relu}
              151929600 1127.711    0.000 1127.711    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              698881538  368.776    0.000 1090.969    0.000 overrides.py:1073(has_torch_function)
                   5065    1.864    0.000 1056.857    0.209 agent.py:121(update_target_network)
              101653314   75.187    0.000  881.555    0.000 extract_dict_ob.py:9(observe)
              101653314   45.442    0.000  806.367    0.000 wrapper.py:19(observe)
              101653314  201.794    0.000  760.925    0.000 libenv.py:344(observe)
               75964800  712.651    0.000  712.651    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   5065  182.677    0.036  685.893    0.135 memory.py:45(update_distribution)
              764722722  273.921    0.000  684.048    0.000 {built-in method builtins.any}
               75964800  680.124    0.000  680.124    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               75964800  634.105    0.000  634.105    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2532660    6.776    0.000  627.665    0.000 agent.py:212(avoid_similar_state)
               53195490  593.494    0.000  593.494    0.000 {built-in method numpy.array}
              152306514  165.350    0.000  553.887    0.000 libenv.py:281(_maybe_copy_dict)
               75964800  553.279    0.000  553.279    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              456924607  478.546    0.000  478.546    0.000 {method 'copy' of 'numpy.ndarray' objects}
               60776840  445.842    0.000  445.842    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7597980   14.213    0.000  427.372    0.000 functional.py:74(split)
                7597980   33.068    0.000  412.089    0.000 tensor.py:460(split)
             1458539916  327.550    0.000  407.747    0.000 overrides.py:1086(<genexpr>)
               50653200   45.211    0.000  395.810    0.000 wrapper.py:22(get_info)
              380301351  394.965    0.000  394.965    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               75964800  390.510    0.000  390.510    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11561162  147.035    0.000  381.324    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7597980  377.116    0.000  377.116    0.000 {function Tensor.split at 0x7fd72bd73d30}
               35454063  335.317    0.000  361.384    0.000 module.py:781(__setattr__)
                2532160  275.368    0.000  356.134    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               50653200  351.851    0.000  351.851    0.000 memory.py:17(inner)
               50653200  181.172    0.000  350.599    0.000 libenv.py:363(get_info)
                  10130  255.335    0.025  311.381    0.031 {built-in method _pickle.loads}
               25654624   24.914    0.000  278.049    0.000 <__array_function__ internals>:2(prod)
                7596980   18.464    0.000  251.049    0.000 pooling.py:152(forward)
               25654664   19.075    0.000  248.776    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               50653200  248.663    0.000  248.663    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               45580880  237.866    0.000  237.866    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2532660   29.444    0.000  234.969    0.000 environments.py:86(<listcomp>)
                7596980   13.620    0.000  232.585    0.000 _jit_internal.py:257(fn)
                2917598  230.496    0.000  230.496    0.000 {built-in method tensor}
               25654624   31.176    0.000  229.701    0.000 fromnumeric.py:2881(prod)
                2532660  227.162    0.000  227.162    0.000 agent.py:115(convert_values)
               10128640  225.441    0.000  225.441    0.000 {built-in method gather}
                7597980  225.006    0.000  225.006    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                7596980   13.782    0.000  217.677    0.000 functional.py:574(_max_pool2d)
               75965070   93.481    0.000  209.534    0.000 tensor.py:596(__hash__)
               50653220   34.696    0.000  205.532    0.000 environments.py:89(reset)
                7596980  202.932    0.000  202.932    0.000 {built-in method max_pool2d}
              268834782  200.365    0.000  200.596    0.000 module.py:765(__getattr__)
               25654624   60.671    0.000  198.525    0.000 fromnumeric.py:70(_wrapreduction)
                2532160  197.921    0.000  197.921    0.000 memory.py:43(<listcomp>)
                2532660   17.203    0.000  189.392    0.000 collector.py:7(collect)
               30387932  162.542    0.000  184.592    0.000 __init__.py:67(is_acceptable)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 8452489: <UUncertainty+Avoid_State0and-1fruitbot_0> in cluster <dcc> Done

Job <UUncertainty+Avoid_State0and-1fruitbot_0> was submitted from host <n-62-27-21> by user <s183914> in cluster <dcc> at Sun Nov 29 17:39:36 2020
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 17:49:24 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 17:49:24 2020
Terminated at Mon Nov 30 16:44:44 2020
Results reported at Mon Nov 30 16:44:44 2020

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

    CPU time :                                   84102.00 sec.
    Max Memory :                                 54884 MB
    Average Memory :                             54142.68 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6556.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82519 sec.
    Turnaround time :                            83108 sec.

The output (if any) is above this job summary.

