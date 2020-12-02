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
Subject: Job 8451047: <UUncertainty+Avoid_State0and10fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and10fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 12:55:32 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 12:57:18 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 12:57:18 2020
Terminated at Sun Nov 29 12:57:22 2020
Results reported at Sun Nov 29 12:57:22 2020

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
    Turnaround time :                            110 sec.

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
Subject: Job 8451074: <UUncertainty+Avoid_State0and10fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and10fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:13:24 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:31:58 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:31:58 2020
Terminated at Sun Nov 29 13:32:02 2020
Results reported at Sun Nov 29 13:32:02 2020

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
    Run time :                                   3 sec.
    Turnaround time :                            1118 sec.

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
Subject: Job 8451095: <UUncertainty+Avoid_State0and10fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and10fruitbot_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Sun Nov 29 13:34:54 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 13:49:42 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 13:49:42 2020
Terminated at Sun Nov 29 13:49:45 2020
Results reported at Sun Nov 29 13:49:45 2020

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
    Turnaround time :                            891 sec.

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
Subject: Job 8451139: <UUncertainty+Avoid_State0and10fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and10fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 14:32:56 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:06:37 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:06:37 2020
Terminated at Sun Nov 29 15:06:48 2020
Results reported at Sun Nov 29 15:06:48 2020

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

    CPU time :                                   4.00 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   11 sec.
    Turnaround time :                            2032 sec.

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
Subject: Job 8451177: <UUncertainty+Avoid_State0and10fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and10fruitbot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Nov 29 15:23:32 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Nov 29 15:26:13 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 29 15:26:13 2020
Terminated at Sun Nov 29 15:26:27 2020
Results reported at Sun Nov 29 15:26:27 2020

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
    Turnaround time :                            175 sec.

The output (if any) is above this job summary.


    Name :                      UUncertainty+Avoid_State0and10fruitbot-0
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
    State difference weight :   10
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13874745193 function calls (13645721806 primitive calls) in 82539.02 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82539.019 82539.019 {built-in method builtins.exec}
                      1    0.054    0.054 82539.019 82539.019 <string>:1(<module>)
                      1  500.822  500.822 82538.964 82538.964 main.py:93(main)
                2267809  163.850    0.000 56317.203    0.025 agent.py:75(learn)
                2267309  757.059    0.000 55240.210    0.024 agent.py:85(TD_learn)
                2267309  157.795    0.000 25444.272    0.011 memory.py:35(sample_distribution)
                2267309  284.243    0.000 24685.127    0.011 helpers.py:15(stack)
        240354254/11337545 1046.064    0.000 16311.547    0.001 module.py:715(_call_impl)
                6802427  224.002    0.000 15391.200    0.002 agent.py:198(forward)
               22675198 12458.052    0.001 12458.067    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               29476517 11788.368    0.000 11788.368    0.000 {built-in method cat}
               36279944  309.481    0.000 10779.701    0.000 container.py:115(forward)
                2267809   64.474    0.000 9456.800    0.004 environments.py:83(step)
                2267309   22.875    0.000 9293.837    0.004 grad_mode.py:23(decorate_context)
                2267309  237.893    0.000 9241.080    0.004 adam.py:55(step)
                2267809  220.089    0.000 8619.445    0.004 agent.py:63(chooseMulti)
                2267309 1704.865    0.001 7951.208    0.004 functional.py:53(adam)
                2267809   96.480    0.000 7446.955    0.003 agent.py:51(rememberMulti)
                2267809  299.373    0.000 6980.513    0.003 agent.py:55(<listcomp>)
              306201435 6729.687    0.000 6729.687    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2267309   23.469    0.000 5944.074    0.003 tensor.py:181(backward)
                2267309   13.812    0.000 5920.605    0.003 __init__.py:68(backward)
                2267309 5833.190    0.003 5833.190    0.003 {method 'run_backward' of 'torch._C._EngineBase' objects}
               45854439 1339.649    0.000 5804.890    0.000 helpers.py:8(clean)
                2267809   66.140    0.000 5799.891    0.003 environments.py:85(<listcomp>)
               52656366 5044.947    0.000 5044.947    0.000 {built-in method as_tensor}
               40814562   77.643    0.000 3923.735    0.000 conv.py:422(forward)
               40814562   84.938    0.000 3812.155    0.000 conv.py:414(_conv_forward)
               40814562 3712.864    0.000 3712.864    0.000 {built-in method conv2d}
               54420416  119.625    0.000 3395.253    0.000 linear.py:92(forward)
                2267809   49.233    0.000 3333.079    0.001 environments.py:84(<listcomp>)
               45356180  181.792    0.000 3283.846    0.000 interop.py:274(step)
               54420416  319.804    0.000 3219.969    0.000 functional.py:1669(linear)
                6802433  424.923    0.000 2567.235    0.000 rnn.py:110(flatten_parameters)
              503342706 1265.358    0.000 1991.349    0.000 tensor.py:933(grad)
               47616989 1907.542    0.000 1907.542    0.000 {built-in method addmm}
                2267309  183.164    0.000 1893.936    0.001 optimizer.py:167(zero_grad)
                2267809  104.614    0.000 1858.830    0.001 agent.py:73(<listcomp>)
                6802427   78.931    0.000 1854.752    0.000 rnn.py:555(forward)
               45356180   20.456    0.000 1772.815    0.000 wrapper.py:25(act)
               45356180   69.636    0.000 1752.358    0.000 env.py:197(act)
              136038540 1708.754    0.000 1708.754    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6802427 1683.643    0.000 1683.643    0.000 {built-in method lstm}
               79362315   77.604    0.000 1670.975    0.000 activation.py:713(forward)
                6802430 1648.163    0.000 1648.163    0.000 {built-in method _cudnn_rnn_flatten_weight}
               45356180 1636.905    0.000 1641.889    0.000 libenv.py:352(act)
               79362315  101.230    0.000 1593.371    0.000 functional.py:1292(leaky_relu)
               79362315 1482.612    0.000 1482.612    0.000 {built-in method torch._C._nn.leaky_relu}
               45356180  157.438    0.000 1447.675    0.000 exploration.py:33(epsilonGreedy)
              136038540 1427.548    0.000 1427.548    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              625782662  335.814    0.000  924.392    0.000 overrides.py:1073(has_torch_function)
                   4535    1.701    0.000  913.143    0.201 agent.py:125(update_target_network)
               68019270  860.625    0.000  860.625    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               91210619   75.915    0.000  826.647    0.000 extract_dict_ob.py:9(observe)
               68019270  805.591    0.000  805.591    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               68019270  752.184    0.000  752.184    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91210619   39.102    0.000  750.732    0.000 wrapper.py:19(observe)
               91210619  181.395    0.000  711.629    0.000 libenv.py:344(observe)
               68019270  668.728    0.000  668.728    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2267809    6.141    0.000  647.098    0.000 agent.py:216(avoid_similar_state)
                   4535  165.204    0.036  581.989    0.128 memory.py:45(update_distribution)
              684737720  226.914    0.000  559.531    0.000 {built-in method builtins.any}
               54420416  519.692    0.000  519.692    0.000 {method 't' of 'torch._C._TensorBase' objects}
              136566799  152.341    0.000  514.163    0.000 libenv.py:281(_maybe_copy_dict)
               68019270  507.525    0.000  507.525    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              341483402  503.258    0.000  503.258    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               47632559  500.481    0.000  500.481    0.000 {built-in method numpy.array}
              409704932  452.624    0.000  452.624    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11291825  161.213    0.000  404.712    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6803427   13.289    0.000  404.462    0.000 functional.py:74(split)
                6803427   31.612    0.000  390.317    0.000 tensor.py:460(split)
               31746149  347.295    0.000  372.806    0.000 module.py:781(__setattr__)
               45356180   41.506    0.000  365.420    0.000 wrapper.py:22(get_info)
                6803427  357.163    0.000  357.163    0.000 {function Tensor.split at 0x7fc68001cd30}
               45356180  332.213    0.000  332.213    0.000 memory.py:17(inner)
             1305985740  264.912    0.000  330.555    0.000 overrides.py:1086(<genexpr>)
                2267309  253.360    0.000  329.194    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               45356180  170.119    0.000  323.914    0.000 libenv.py:363(get_info)
               45356180  306.541    0.000  306.541    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24851099   24.571    0.000  285.797    0.000 <__array_function__ internals>:2(prod)
               40813562  279.036    0.000  279.036    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   9070  226.363    0.025  278.051    0.031 {built-in method _pickle.loads}
                2267809  265.086    0.000  265.086    0.000 agent.py:119(convert_values)
                6802427   17.761    0.000  264.973    0.000 pooling.py:152(forward)
                2267809   28.210    0.000  259.355    0.000 environments.py:86(<listcomp>)
               24851139   19.096    0.000  256.918    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                9069236  250.138    0.000  250.138    0.000 {built-in method gather}
                6802427   12.320    0.000  247.212    0.000 _jit_internal.py:257(fn)
                6803427  238.808    0.000  238.808    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               24851099   30.828    0.000  237.822    0.000 fromnumeric.py:2881(prod)
                6802427   12.833    0.000  233.718    0.000 functional.py:574(_max_pool2d)
               45356200   34.675    0.000  231.205    0.000 environments.py:89(reset)
                6802427  220.112    0.000  220.112    0.000 {built-in method max_pool2d}
               24851099   57.345    0.000  206.994    0.000 fromnumeric.py:70(_wrapreduction)
               27209720  174.752    0.000  196.676    0.000 __init__.py:67(is_acceptable)
                2612467  192.431    0.000  192.431    0.000 {built-in method tensor}
               68019540   84.818    0.000  184.350    0.000 tensor.py:596(__hash__)
                2267309  180.292    0.000  180.292    0.000 memory.py:43(<listcomp>)
              240718176  170.937    0.000  171.133    0.000 module.py:765(__getattr__)
                2267309    6.636    0.000  171.082    0.000 loss.py:445(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8452493: <UUncertainty+Avoid_State0and10fruitbot_0> in cluster <dcc> Done

Job <UUncertainty+Avoid_State0and10fruitbot_0> was submitted from host <n-62-27-21> by user <s183914> in cluster <dcc> at Sun Nov 29 17:39:37 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Nov 30 23:20:17 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 30 23:20:17 2020
Terminated at Tue Dec  1 22:16:13 2020
Results reported at Tue Dec  1 22:16:13 2020

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

    CPU time :                                   84248.00 sec.
    Max Memory :                                 54930 MB
    Average Memory :                             54161.95 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6510.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82557 sec.
    Turnaround time :                            189396 sec.

The output (if any) is above this job summary.

  File "main.py", line 92
    if fortheloveofgod =!=!= CRASH:
                       ^
SyntaxError: invalid syntax

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8458906: <UUncertainty+Avoid_State0and10fruitbot_0> in cluster <dcc> Exited

Job <UUncertainty+Avoid_State0and10fruitbot_0> was submitted from host <n-62-30-8> by user <s183914> in cluster <dcc> at Mon Nov 30 20:41:55 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec  2 02:18:32 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec  2 02:18:32 2020
Terminated at Wed Dec  2 02:18:34 2020
Results reported at Wed Dec  2 02:18:34 2020

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

    CPU time :                                   0.26 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   32 sec.
    Turnaround time :                            106599 sec.

The output (if any) is above this job summary.

