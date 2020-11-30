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
Subject: Job 8451042: <UUncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 12:55:31 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 12:56:52 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 12:56:52 2020
Terminated at Sun Nov 29 12:56:57 2020
Results reported at Sun Nov 29 12:56:57 2020

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

    CPU time :                                   1.15 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   4 sec.
    Turnaround time :                            86 sec.

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
Subject: Job 8451069: <UUncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:13:23 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:18:23 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:18:23 2020
Terminated at Sun Nov 29 13:18:30 2020
Results reported at Sun Nov 29 13:18:30 2020

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

    CPU time :                                   1.66 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   7 sec.
    Turnaround time :                            307 sec.

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
Subject: Job 8451090: <UUncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:34:53 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:49:00 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:49:00 2020
Terminated at Sun Nov 29 13:49:04 2020
Results reported at Sun Nov 29 13:49:04 2020

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

    CPU time :                                   1.14 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   6 sec.
    Turnaround time :                            851 sec.

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
Subject: Job 8451134: <UUncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and0fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 14:32:55 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:05:05 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:05:05 2020
Terminated at Sun Nov 29 15:05:30 2020
Results reported at Sun Nov 29 15:05:30 2020

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
    Max Memory :                                 540 MB
    Average Memory :                             540.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               60900.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   24 sec.
    Turnaround time :                            1955 sec.

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
Subject: Job 8451172: <UUncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and0fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 15:23:31 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:24:38 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:24:38 2020
Terminated at Sun Nov 29 15:25:11 2020
Results reported at Sun Nov 29 15:25:11 2020

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

    CPU time :                                   10.00 sec.
    Max Memory :                                 949 MB
    Average Memory :                             949.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               60491.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   34 sec.
    Turnaround time :                            100 sec.

The output (if any) is above this job summary.


    Name :                      UUncertainty+Avoid_State0and0fruitbot-0
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
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14363629362 function calls (14126417804 primitive calls) in 82525.98 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82525.983 82525.983 {built-in method builtins.exec}
                      1    0.067    0.067 82525.983 82525.983 <string>:1(<module>)
                      1  553.378  553.378 82525.914 82525.914 main.py:93(main)
                2348880  187.506    0.000 57314.352    0.024 agent.py:75(learn)
                2348380  641.551    0.000 56059.887    0.024 agent.py:85(TD_learn)
                2348380  172.575    0.000 30492.787    0.013 memory.py:35(sample_distribution)
                2348380  331.885    0.000 29686.891    0.013 helpers.py:15(stack)
               30530440 15448.622    0.001 15448.622    0.001 {built-in method cat}
        248947780/11742900 1079.261    0.000 14994.787    0.001 module.py:715(_call_impl)
                7045640  215.767    0.000 14155.195    0.002 agent.py:194(forward)
               23485908 13663.217    0.001 13663.221    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               37577080  291.736    0.000 9795.512    0.000 container.py:115(forward)
                2348880   68.854    0.000 9400.457    0.004 environments.py:83(step)
                2348880  188.023    0.000 7916.695    0.003 agent.py:63(chooseMulti)
                2348380   25.105    0.000 7287.987    0.003 grad_mode.py:23(decorate_context)
                2348380  255.983    0.000 7233.062    0.003 adam.py:55(step)
                2348880   89.423    0.000 7149.860    0.003 agent.py:51(rememberMulti)
                2348880  234.388    0.000 6694.590    0.003 agent.py:55(<listcomp>)
              317466668 6530.729    0.000 6530.729    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2348380 1324.277    0.001 5900.934    0.003 functional.py:53(adam)
               47491307 1431.236    0.000 5651.229    0.000 helpers.py:8(clean)
                2348880   59.872    0.000 5641.084    0.002 environments.py:85(<listcomp>)
                2348380   24.937    0.000 5115.747    0.002 tensor.py:181(backward)
                2348380   14.171    0.000 5090.809    0.002 __init__.py:68(backward)
                2348380 5011.921    0.002 5011.921    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               54536447 4841.737    0.000 4841.737    0.000 {built-in method as_tensor}
               42273840   75.106    0.000 3601.700    0.000 conv.py:422(forward)
               42273840   94.356    0.000 3487.847    0.000 conv.py:414(_conv_forward)
                2348880   50.548    0.000 3436.267    0.001 environments.py:84(<listcomp>)
               46977600  186.254    0.000 3385.718    0.000 interop.py:274(step)
               42273840 3377.129    0.000 3377.129    0.000 {built-in method conv2d}
               56366120  120.126    0.000 3023.334    0.000 linear.py:92(forward)
               56366120  308.738    0.000 2842.117    0.000 functional.py:1669(linear)
                7045646  411.262    0.000 2222.902    0.000 rnn.py:110(flatten_parameters)
              521340468 1144.346    0.000 1940.588    0.000 tensor.py:933(grad)
                7045640   85.251    0.000 1911.065    0.000 rnn.py:555(forward)
               46977600   22.887    0.000 1840.162    0.000 wrapper.py:25(act)
               46977600   63.863    0.000 1817.275    0.000 env.py:197(act)
                7045640 1727.864    0.000 1727.864    0.000 {built-in method lstm}
               46977600 1714.154    0.000 1718.910    0.000 libenv.py:352(act)
                2348880   86.451    0.000 1650.532    0.001 agent.py:73(<listcomp>)
               49319480 1631.088    0.000 1631.088    0.000 {built-in method addmm}
                2348380  148.625    0.000 1626.684    0.001 optimizer.py:167(zero_grad)
               82199800   80.241    0.000 1421.037    0.000 activation.py:713(forward)
               82199800  114.244    0.000 1340.795    0.000 functional.py:1292(leaky_relu)
               46977600  138.651    0.000 1332.537    0.000 exploration.py:33(epsilonGreedy)
                7045643 1305.223    0.000 1305.223    0.000 {built-in method _cudnn_rnn_flatten_weight}
               82199800 1215.808    0.000 1215.808    0.000 {built-in method torch._C._nn.leaky_relu}
              140902800 1211.355    0.000 1211.355    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   4697    2.024    0.000 1066.959    0.227 agent.py:121(update_target_network)
              140902800 1021.956    0.000 1021.956    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              648158258  346.430    0.000 1009.532    0.000 overrides.py:1073(has_torch_function)
               94468907   70.799    0.000  847.874    0.000 extract_dict_ob.py:9(observe)
               94468907   40.016    0.000  777.075    0.000 wrapper.py:19(observe)
               94468907  185.538    0.000  737.059    0.000 libenv.py:344(observe)
                   4697  180.906    0.039  696.593    0.148 memory.py:45(update_distribution)
               70451400  648.135    0.000  648.135    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              709221162  257.097    0.000  629.845    0.000 {built-in method builtins.any}
               70451400  615.571    0.000  615.571    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               49335374  594.302    0.000  594.302    0.000 {built-in method numpy.array}
                2348880    6.220    0.000  577.571    0.000 agent.py:212(avoid_similar_state)
               70451400  568.105    0.000  568.105    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              141446507  157.450    0.000  553.768    0.000 libenv.py:281(_maybe_copy_dict)
               70451400  490.854    0.000  490.854    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              424344218  477.731    0.000  477.731    0.000 {method 'copy' of 'numpy.ndarray' objects}
               56366120  431.225    0.000  431.225    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7046640   14.276    0.000  427.731    0.000 functional.py:74(split)
                7046640   33.453    0.000  412.454    0.000 tensor.py:460(split)
               32881143  366.319    0.000  394.200    0.000 module.py:781(__setattr__)
               11376532  146.548    0.000  379.775    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               46977600   41.269    0.000  377.288    0.000 wrapper.py:22(get_info)
                7046640  377.222    0.000  377.222    0.000 {function Tensor.split at 0x7ff431ea0d30}
               46977600  375.713    0.000  375.713    0.000 memory.py:17(inner)
             1352682636  295.256    0.000  370.366    0.000 overrides.py:1086(<genexpr>)
              351666495  367.520    0.000  367.520    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               70451400  347.600    0.000  347.600    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               46977600  173.155    0.000  336.020    0.000 libenv.py:363(get_info)
                2348380  253.327    0.000  329.466    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   9394  259.153    0.028  311.828    0.033 {built-in method _pickle.loads}
               25101584   25.135    0.000  275.861    0.000 <__array_function__ internals>:2(prod)
                2348880   26.361    0.000  254.252    0.000 environments.py:86(<listcomp>)
                7045640   23.610    0.000  250.312    0.000 pooling.py:152(forward)
               25101624   18.608    0.000  246.585    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               46977600  231.544    0.000  231.544    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25101584   30.339    0.000  227.977    0.000 fromnumeric.py:2881(prod)
               46977620   35.508    0.000  227.939    0.000 environments.py:89(reset)
                7045640   13.274    0.000  226.703    0.000 _jit_internal.py:257(fn)
               42272840  225.217    0.000  225.217    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                9393520  216.264    0.000  216.264    0.000 {built-in method gather}
                7045640   15.373    0.000  212.238    0.000 functional.py:574(_max_pool2d)
                2348880  210.784    0.000  210.784    0.000 agent.py:115(convert_values)
                7046640  209.156    0.000  209.156    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2348380  207.865    0.000  207.865    0.000 memory.py:43(<listcomp>)
                2705850  202.942    0.000  202.942    0.000 {built-in method tensor}
               70451670   90.455    0.000  198.535    0.000 tensor.py:596(__hash__)
               25101584   58.097    0.000  197.638    0.000 fromnumeric.py:70(_wrapreduction)
               28182572  174.986    0.000  196.959    0.000 __init__.py:67(is_acceptable)
                7045640  195.996    0.000  195.996    0.000 {built-in method max_pool2d}
              249324662  191.374    0.000  191.585    0.000 module.py:765(__getattr__)
                2348880   15.201    0.000  160.839    0.000 collector.py:7(collect)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8452488: <UUncertainty+Avoid_State0and0fruitbot_0> in cluster <dcc> Done

Job <UUncertainty+Avoid_State0and0fruitbot_0> was submitted from host <n-62-27-21> by user <s183914> in cluster <dcc> at Sun Nov 29 17:39:36 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 17:45:29 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 17:45:29 2020
Terminated at Mon Nov 30 16:41:04 2020
Results reported at Mon Nov 30 16:41:04 2020

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

    CPU time :                                   85905.00 sec.
    Max Memory :                                 54815 MB
    Average Memory :                             54134.02 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6625.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82535 sec.
    Turnaround time :                            82888 sec.

The output (if any) is above this job summary.

