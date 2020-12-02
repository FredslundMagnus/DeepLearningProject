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
Subject: Job 8451046: <UUncertainty+Avoid_State1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State1and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 12:55:32 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 12:57:13 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 12:57:13 2020
Terminated at Sun Nov 29 12:57:17 2020
Results reported at Sun Nov 29 12:57:17 2020

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
    Turnaround time :                            105 sec.

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
Subject: Job 8451073: <UUncertainty+Avoid_State1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State1and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:13:24 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:31:53 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:31:53 2020
Terminated at Sun Nov 29 13:31:56 2020
Results reported at Sun Nov 29 13:31:56 2020

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

    CPU time :                                   1.12 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   3 sec.
    Turnaround time :                            1112 sec.

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
Subject: Job 8451094: <UUncertainty+Avoid_State1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State1and0fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:34:53 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:49:38 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:49:38 2020
Terminated at Sun Nov 29 13:49:41 2020
Results reported at Sun Nov 29 13:49:41 2020

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
    Run time :                                   3 sec.
    Turnaround time :                            888 sec.

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
Subject: Job 8451138: <UUncertainty+Avoid_State1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State1and0fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 14:32:56 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:06:22 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:06:22 2020
Terminated at Sun Nov 29 15:06:33 2020
Results reported at Sun Nov 29 15:06:33 2020

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

    CPU time :                                   4.22 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   13 sec.
    Turnaround time :                            2017 sec.

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
Subject: Job 8451176: <UUncertainty+Avoid_State1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State1and0fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 15:23:32 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:25:58 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:25:58 2020
Terminated at Sun Nov 29 15:26:12 2020
Results reported at Sun Nov 29 15:26:12 2020

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
    Max Memory :                                 47 MB
    Average Memory :                             47.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               61393.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   14 sec.
    Turnaround time :                            160 sec.

The output (if any) is above this job summary.


    Name :                      UUncertainty+Avoid_State1and0fruitbot-0
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
    Uncertainty weight :        1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14110356899 function calls (13877403198 primitive calls) in 82527.93 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82527.931 82527.931 {built-in method builtins.exec}
                      1    0.046    0.046 82527.930 82527.930 <string>:1(<module>)
                      1  496.828  496.828 82527.883 82527.883 main.py:93(main)
                2306723  166.141    0.000 56154.766    0.024 agent.py:75(learn)
                2306223  759.576    0.000 55072.949    0.024 agent.py:85(TD_learn)
                2306223  162.215    0.000 25062.998    0.011 memory.py:35(sample_distribution)
                2306223  254.718    0.000 24300.322    0.011 helpers.py:15(stack)
        244479138/11532115 1037.940    0.000 16292.850    0.001 module.py:715(_call_impl)
                6919169  222.126    0.000 15372.087    0.002 agent.py:194(forward)
               23064338 12619.717    0.001 12619.718    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               29982399 11273.904    0.000 11273.904    0.000 {built-in method cat}
               36902568  304.363    0.000 10757.268    0.000 container.py:115(forward)
                2306723   65.858    0.000 9512.912    0.004 environments.py:83(step)
                2306223   22.467    0.000 9462.269    0.004 grad_mode.py:23(decorate_context)
                2306223  245.083    0.000 9411.795    0.004 adam.py:55(step)
                2306723  219.036    0.000 8661.409    0.004 agent.py:63(chooseMulti)
                2306223 1736.341    0.001 8098.892    0.004 functional.py:53(adam)
                2306723   95.905    0.000 7509.116    0.003 agent.py:51(rememberMulti)
                2306723  291.590    0.000 7045.706    0.003 agent.py:55(<listcomp>)
              311609551 6828.097    0.000 6828.097    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2306223   24.868    0.000 6012.114    0.003 tensor.py:181(backward)
                2306223   15.965    0.000 5987.246    0.003 __init__.py:68(backward)
                2306223 5900.307    0.003 5900.307    0.003 {method 'run_backward' of 'torch._C._EngineBase' objects}
               46746947 1354.480    0.000 5851.247    0.000 helpers.py:8(clean)
                2306723   66.854    0.000 5831.198    0.003 environments.py:85(<listcomp>)
               53665616 5074.280    0.000 5074.280    0.000 {built-in method as_tensor}
               41515014   72.895    0.000 3902.257    0.000 conv.py:422(forward)
               41515014   84.177    0.000 3793.821    0.000 conv.py:414(_conv_forward)
               41515014 3693.697    0.000 3693.697    0.000 {built-in method conv2d}
               55354352  120.170    0.000 3412.691    0.000 linear.py:92(forward)
                2306723   48.824    0.000 3331.034    0.001 environments.py:84(<listcomp>)
               46134460  185.014    0.000 3282.210    0.000 interop.py:274(step)
               55354352  320.145    0.000 3234.219    0.000 functional.py:1669(linear)
                6919175  414.870    0.000 2564.517    0.000 rnn.py:110(flatten_parameters)
              511981614 1265.165    0.000 2003.577    0.000 tensor.py:933(grad)
               48434183 1920.643    0.000 1920.643    0.000 {built-in method addmm}
                2306223  182.740    0.000 1904.714    0.001 optimizer.py:167(zero_grad)
                2306723  104.820    0.000 1881.145    0.001 agent.py:73(<listcomp>)
                6919169   79.384    0.000 1866.905    0.000 rnn.py:555(forward)
               46134460   20.040    0.000 1770.687    0.000 wrapper.py:25(act)
               46134460   67.325    0.000 1750.647    0.000 env.py:197(act)
              138373380 1732.239    0.000 1732.239    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6919169 1694.907    0.000 1694.907    0.000 {built-in method lstm}
                6919172 1666.338    0.000 1666.338    0.000 {built-in method _cudnn_rnn_flatten_weight}
               80724305   73.002    0.000 1666.133    0.000 activation.py:713(forward)
               46134460 1638.237    0.000 1642.520    0.000 libenv.py:352(act)
               80724305  107.077    0.000 1593.131    0.000 functional.py:1292(leaky_relu)
               80724305 1476.520    0.000 1476.520    0.000 {built-in method torch._C._nn.leaky_relu}
               46134460  156.699    0.000 1469.523    0.000 exploration.py:33(epsilonGreedy)
              138373380 1454.844    0.000 1454.844    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              636522926  336.584    0.000  938.199    0.000 overrides.py:1073(has_torch_function)
                   4613    1.694    0.000  915.676    0.198 agent.py:121(update_target_network)
               69186690  881.481    0.000  881.481    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               92881407   75.701    0.000  826.034    0.000 extract_dict_ob.py:9(observe)
               69186690  822.117    0.000  822.117    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               69186690  769.931    0.000  769.931    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92881407   40.629    0.000  750.333    0.000 wrapper.py:19(observe)
               92881407  188.883    0.000  709.705    0.000 libenv.py:344(observe)
               69186690  678.846    0.000  678.846    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2306723    6.744    0.000  649.189    0.000 agent.py:212(avoid_similar_state)
                   4613  164.104    0.036  584.069    0.127 memory.py:45(update_distribution)
              696489748  234.669    0.000  569.683    0.000 {built-in method builtins.any}
               55354352  518.309    0.000  518.309    0.000 {method 't' of 'torch._C._TensorBase' objects}
               69186690  517.623    0.000  517.623    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              139015867  149.709    0.000  511.138    0.000 libenv.py:281(_maybe_copy_dict)
               48449909  503.912    0.000  503.912    0.000 {built-in method numpy.array}
              344979463  502.866    0.000  502.866    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              417052214  449.335    0.000  449.335    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11331669  159.884    0.000  409.320    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6920169   13.571    0.000  399.530    0.000 functional.py:74(split)
                6920169   33.023    0.000  385.067    0.000 tensor.py:460(split)
               32290945  342.696    0.000  366.751    0.000 module.py:781(__setattr__)
               46134460   40.004    0.000  364.047    0.000 wrapper.py:22(get_info)
                6920169  350.547    0.000  350.547    0.000 {function Tensor.split at 0x7f18c2a01d30}
             1328400204  266.588    0.000  333.028    0.000 overrides.py:1086(<genexpr>)
                2306223  255.527    0.000  332.962    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               46134460  171.765    0.000  324.043    0.000 libenv.py:363(get_info)
               46134460  321.379    0.000  321.379    0.000 memory.py:17(inner)
               46134460  306.803    0.000  306.803    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24969701   24.607    0.000  293.127    0.000 <__array_function__ internals>:2(prod)
                2306723   28.319    0.000  284.822    0.000 environments.py:86(<listcomp>)
               41514014  279.497    0.000  279.497    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   9226  226.603    0.025  278.568    0.030 {built-in method _pickle.loads}
                2306723  269.127    0.000  269.127    0.000 agent.py:115(convert_values)
                6919169   19.142    0.000  264.600    0.000 pooling.py:152(forward)
               24969741   20.409    0.000  264.161    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               46134480   34.681    0.000  256.539    0.000 environments.py:89(reset)
                9224892  252.364    0.000  252.364    0.000 {built-in method gather}
                6919169   12.497    0.000  245.458    0.000 _jit_internal.py:257(fn)
               24969701   31.781    0.000  243.752    0.000 fromnumeric.py:2881(prod)
                6920169  240.091    0.000  240.091    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6919169   13.144    0.000  231.757    0.000 functional.py:574(_max_pool2d)
                6919169  217.838    0.000  217.838    0.000 {built-in method max_pool2d}
               24969701   57.962    0.000  211.971    0.000 fromnumeric.py:70(_wrapreduction)
               27676688  175.425    0.000  195.746    0.000 __init__.py:67(is_acceptable)
               69186960   85.515    0.000  187.276    0.000 tensor.py:596(__hash__)
                2657309  186.347    0.000  186.347    0.000 {built-in method tensor}
                2306223  176.812    0.000  176.812    0.000 memory.py:43(<listcomp>)
              244849300  175.871    0.000  176.064    0.000 module.py:765(__getattr__)
                2306223    6.022    0.000  170.426    0.000 loss.py:445(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8452492: <UUncertainty+Avoid_State1and0fruitbot_0> in cluster <dcc> Done

Job <UUncertainty+Avoid_State1and0fruitbot_0> was submitted from host <n-62-27-21> by user <s183914> in cluster <dcc> at Sun Nov 29 17:39:37 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Nov 30 08:27:59 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 30 08:27:59 2020
Terminated at Tue Dec  1 07:23:38 2020
Results reported at Tue Dec  1 07:23:38 2020

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

    CPU time :                                   83923.00 sec.
    Max Memory :                                 54815 MB
    Average Memory :                             54042.71 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6625.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82539 sec.
    Turnaround time :                            135841 sec.

The output (if any) is above this job summary.

  File "main.py", line 92
    if fortheloveofgod =!=!= CRASH:
                       ^
SyntaxError: invalid syntax

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8458905: <UUncertainty+Avoid_State1and0fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State1and0fruitbot_0> was submitted from host <n-62-30-8> by user <s183914> in cluster <dcc> at Mon Nov 30 20:41:55 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec  2 01:27:26 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec  2 01:27:26 2020
Terminated at Wed Dec  2 01:27:28 2020
Results reported at Wed Dec  2 01:27:28 2020

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

    CPU time :                                   0.25 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   2 sec.
    Turnaround time :                            103533 sec.

The output (if any) is above this job summary.

