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
Subject: Job 8451044: <UUncertainty+Avoid_State0and1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and1fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 12:55:31 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 12:57:03 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 12:57:03 2020
Terminated at Sun Nov 29 12:57:06 2020
Results reported at Sun Nov 29 12:57:06 2020

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
    Turnaround time :                            95 sec.

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
Subject: Job 8451071: <UUncertainty+Avoid_State0and1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and1fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:13:24 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:18:38 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:18:38 2020
Terminated at Sun Nov 29 13:18:45 2020
Results reported at Sun Nov 29 13:18:45 2020

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

    CPU time :                                   1.61 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   7 sec.
    Turnaround time :                            321 sec.

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
Subject: Job 8451092: <UUncertainty+Avoid_State0and1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and1fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:34:53 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:49:20 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:49:20 2020
Terminated at Sun Nov 29 13:49:23 2020
Results reported at Sun Nov 29 13:49:23 2020

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

    CPU time :                                   1.05 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   3 sec.
    Turnaround time :                            870 sec.

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
Subject: Job 8451136: <UUncertainty+Avoid_State0and1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and1fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 14:32:56 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:05:47 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:05:47 2020
Terminated at Sun Nov 29 15:05:58 2020
Results reported at Sun Nov 29 15:05:58 2020

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

    CPU time :                                   4.01 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   15 sec.
    Turnaround time :                            1982 sec.

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
Subject: Job 8451174: <UUncertainty+Avoid_State0and1fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and1fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 15:23:31 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:25:28 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:25:28 2020
Terminated at Sun Nov 29 15:25:41 2020
Results reported at Sun Nov 29 15:25:41 2020

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

    CPU time :                                   6.64 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   14 sec.
    Turnaround time :                            130 sec.

The output (if any) is above this job summary.


    Name :                      UUncertainty+Avoid_State0and1fruitbot-0
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
    State difference weight :   1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14125993684 function calls (13892660728 primitive calls) in 82519.58 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82519.584 82519.584 {built-in method builtins.exec}
                      1    0.046    0.046 82519.584 82519.584 <string>:1(<module>)
                      1  500.507  500.507 82519.536 82519.536 main.py:93(main)
                2310478  168.071    0.000 56254.402    0.024 agent.py:75(learn)
                2309978  757.347    0.000 55172.524    0.024 agent.py:85(TD_learn)
                2309978  157.957    0.000 25080.541    0.011 memory.py:35(sample_distribution)
                2309978  264.480    0.000 24319.150    0.011 helpers.py:15(stack)
        244877168/11550890 1058.629    0.000 16371.169    0.001 module.py:715(_call_impl)
                6930434  223.500    0.000 15441.944    0.002 agent.py:194(forward)
               23101888 12547.083    0.001 12547.146    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               30031214 11345.860    0.000 11345.860    0.000 {built-in method cat}
               36962648  305.631    0.000 10835.750    0.000 container.py:115(forward)
                2309978   22.856    0.000 9474.775    0.004 grad_mode.py:23(decorate_context)
                2310478   65.460    0.000 9429.590    0.004 environments.py:83(step)
                2309978  248.335    0.000 9423.763    0.004 adam.py:55(step)
                2310478  219.134    0.000 8670.178    0.004 agent.py:63(chooseMulti)
                2309978 1735.360    0.001 8103.950    0.004 functional.py:53(adam)
                2310478   96.881    0.000 7474.605    0.003 agent.py:51(rememberMulti)
                2310478  298.378    0.000 7003.155    0.003 agent.py:55(<listcomp>)
              312133290 6769.083    0.000 6769.083    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2309978   22.970    0.000 5994.142    0.003 tensor.py:181(backward)
                2309978   13.685    0.000 5971.172    0.003 __init__.py:68(backward)
                2309978 5884.864    0.003 5884.864    0.003 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2310478   66.297    0.000 5821.663    0.003 environments.py:85(<listcomp>)
               46468923 1355.950    0.000 5791.531    0.000 helpers.py:8(clean)
               53398857 5015.983    0.000 5015.983    0.000 {built-in method as_tensor}
               41582604   73.586    0.000 3924.817    0.000 conv.py:422(forward)
               41582604   85.178    0.000 3816.261    0.000 conv.py:414(_conv_forward)
               41582604 3715.128    0.000 3715.128    0.000 {built-in method conv2d}
               55444472  120.377    0.000 3438.546    0.000 linear.py:92(forward)
                2310478   49.025    0.000 3334.307    0.001 environments.py:84(<listcomp>)
               46209560  181.823    0.000 3285.282    0.000 interop.py:274(step)
               55444472  324.379    0.000 3259.941    0.000 functional.py:1669(linear)
                6930440  421.324    0.000 2562.196    0.000 rnn.py:110(flatten_parameters)
              512815224 1293.494    0.000 2030.906    0.000 tensor.py:933(grad)
                2309978  189.311    0.000 1936.957    0.001 optimizer.py:167(zero_grad)
               48513038 1929.018    0.000 1929.018    0.000 {built-in method addmm}
                2310478  104.545    0.000 1872.644    0.001 agent.py:73(<listcomp>)
                6930434   82.585    0.000 1857.979    0.000 rnn.py:555(forward)
               46209560   20.526    0.000 1757.303    0.000 wrapper.py:25(act)
              138598680 1740.378    0.000 1740.378    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               46209560   69.050    0.000 1736.777    0.000 env.py:197(act)
                6930434 1679.670    0.000 1679.670    0.000 {built-in method lstm}
               80855730   72.584    0.000 1673.140    0.000 activation.py:713(forward)
                6930437 1659.781    0.000 1659.781    0.000 {built-in method _cudnn_rnn_flatten_weight}
               46209560 1622.108    0.000 1626.830    0.000 libenv.py:352(act)
               80855730  106.107    0.000 1600.556    0.000 functional.py:1292(leaky_relu)
               80855730 1485.119    0.000 1485.119    0.000 {built-in method torch._C._nn.leaky_relu}
               46209560  158.918    0.000 1459.462    0.000 exploration.py:33(epsilonGreedy)
              138598680 1455.073    0.000 1455.073    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              637559306  341.510    0.000  940.243    0.000 overrides.py:1073(has_torch_function)
                   4620    1.689    0.000  913.808    0.198 agent.py:121(update_target_network)
               69299340  875.961    0.000  875.961    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               92678483   73.416    0.000  823.633    0.000 extract_dict_ob.py:9(observe)
               69299340  820.054    0.000  820.054    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               69299340  768.136    0.000  768.136    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92678483   40.420    0.000  750.217    0.000 wrapper.py:19(observe)
               92678483  190.601    0.000  709.797    0.000 libenv.py:344(observe)
               69299340  685.767    0.000  685.767    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2310478    6.475    0.000  653.618    0.000 agent.py:212(avoid_similar_state)
                   4620  164.045    0.036  583.603    0.126 memory.py:45(update_distribution)
              697623758  230.420    0.000  568.716    0.000 {built-in method builtins.any}
               55444472  526.009    0.000  526.009    0.000 {method 't' of 'torch._C._TensorBase' objects}
               69299340  522.103    0.000  522.103    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              346265775  509.348    0.000  509.348    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              138888043  153.746    0.000  509.231    0.000 libenv.py:281(_maybe_copy_dict)
               48528778  504.031    0.000  504.031    0.000 {built-in method numpy.array}
              416668749  446.587    0.000  446.587    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11333630  158.219    0.000  404.551    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6931434   13.114    0.000  398.442    0.000 functional.py:74(split)
                6931434   32.022    0.000  384.497    0.000 tensor.py:460(split)
               46209560   41.456    0.000  373.190    0.000 wrapper.py:22(get_info)
               32343515  347.175    0.000  372.353    0.000 module.py:781(__setattr__)
                6931434  350.926    0.000  350.926    0.000 {function Tensor.split at 0x7fd8a4011d30}
                2309978  258.813    0.000  336.720    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
             1330563084  268.670    0.000  336.189    0.000 overrides.py:1086(<genexpr>)
               46209560  174.555    0.000  331.734    0.000 libenv.py:363(get_info)
               46209560  323.570    0.000  323.570    0.000 memory.py:17(inner)
               46209560  308.637    0.000  308.637    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24977378   24.258    0.000  291.095    0.000 <__array_function__ internals>:2(prod)
               41581604  280.034    0.000  280.034    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   9240  225.352    0.024  277.159    0.030 {built-in method _pickle.loads}
                2310478  268.989    0.000  268.989    0.000 agent.py:115(convert_values)
                6930434   16.560    0.000  264.552    0.000 pooling.py:152(forward)
               24977418   19.430    0.000  262.681    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                9239912  250.606    0.000  250.606    0.000 {built-in method gather}
                6930434   12.262    0.000  247.992    0.000 _jit_internal.py:257(fn)
               24977378   31.816    0.000  243.251    0.000 fromnumeric.py:2881(prod)
                6931434  240.417    0.000  240.417    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6930434   12.746    0.000  234.528    0.000 functional.py:574(_max_pool2d)
                6930434  221.012    0.000  221.012    0.000 {built-in method max_pool2d}
               24977378   57.712    0.000  211.435    0.000 fromnumeric.py:70(_wrapreduction)
                2310478   28.006    0.000  208.161    0.000 environments.py:86(<listcomp>)
                2661596  194.517    0.000  194.517    0.000 {built-in method tensor}
               27721748  171.245    0.000  190.925    0.000 __init__.py:67(is_acceptable)
               69299610   86.609    0.000  186.535    0.000 tensor.py:596(__hash__)
               46209580   33.257    0.000  180.169    0.000 environments.py:89(reset)
                2309978  177.211    0.000  177.211    0.000 memory.py:43(<listcomp>)
              245247890  175.422    0.000  175.618    0.000 module.py:765(__getattr__)
                2309978    6.497    0.000  170.249    0.000 loss.py:445(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8452490: <UUncertainty+Avoid_State0and1fruitbot_0> in cluster <dcc> Done

Job <UUncertainty+Avoid_State0and1fruitbot_0> was submitted from host <n-62-27-21> by user <s183914> in cluster <dcc> at Sun Nov 29 17:39:37 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 18:01:51 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 18:01:51 2020
Terminated at Mon Nov 30 16:57:20 2020
Results reported at Mon Nov 30 16:57:20 2020

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

    CPU time :                                   84050.00 sec.
    Max Memory :                                 54851 MB
    Average Memory :                             54099.32 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6589.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82529 sec.
    Turnaround time :                            83863 sec.

The output (if any) is above this job summary.

