
    Name :                      Uncertainty=0.5chaser-0
    Discount :                  0.995
    Environment :               chaser
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12836686449 function calls (12601123594 primitive calls) in 82522.78 seconds

##    Ordered by: cumulative time
   List reduced from 1348 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82522.775 82522.775 {built-in method builtins.exec}
                      1    0.034    0.034 82522.775 82522.775 <string>:1(<module>)
                      1  459.229  459.229 82522.739 82522.739 main.py:11(main)
                2454089  116.421    0.000 57184.297    0.023 agent.py:49(learn)
                2453589  529.006    0.000 56368.027    0.023 agent.py:59(TD_learn)
                2453589  171.485    0.000 26727.121    0.011 memory.py:35(sample_distribution)
                2453589  273.911    0.000 25914.381    0.011 helpers.py:12(stack)
        247824989/12268445 1029.814    0.000 18302.621    0.001 module.py:715(_call_impl)
                9814856  289.825    0.000 18009.880    0.002 agent.py:139(forward)
               22083867 13432.262    0.001 13432.281    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               26990979 11801.490    0.000 11801.490    0.000 {built-in method cat}
               39259424  308.950    0.000 10805.716    0.000 container.py:115(forward)
                2454089   68.432    0.000 9710.910    0.004 environments.py:73(step)
                2454089    7.398    0.000 7604.608    0.003 agent.py:34(rememberMulti)
                2454089  321.872    0.000 7597.209    0.003 agent.py:35(<listcomp>)
                2453589   21.859    0.000 7494.099    0.003 grad_mode.py:23(decorate_context)
                2453589  198.877    0.000 7443.467    0.003 adam.py:55(step)
              332093945 7411.391    0.000 7411.391    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2454089   50.097    0.000 7365.762    0.003 agent.py:43(chooseMulti)
                2453589 1380.277    0.001 6421.087    0.003 functional.py:53(adam)
                2454089   60.021    0.000 6097.994    0.002 environments.py:75(<listcomp>)
               49473111 1438.606    0.000 6093.426    0.000 helpers.py:8(clean)
               58889136  102.459    0.000 5457.652    0.000 conv.py:422(forward)
               56833878 5336.191    0.000 5336.191    0.000 {built-in method as_tensor}
               58889136  114.710    0.000 5311.105    0.000 conv.py:414(_conv_forward)
                2453589   24.747    0.000 5235.156    0.002 tensor.py:181(backward)
                2453589   15.298    0.000 5210.409    0.002 __init__.py:68(backward)
               58889136 5176.074    0.000 5176.074    0.000 {built-in method conv2d}
                2453589 5115.298    0.002 5115.298    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9814862  577.222    0.000 3579.450    0.000 rnn.py:110(flatten_parameters)
                2454089   51.105    0.000 3281.921    0.001 environments.py:74(<listcomp>)
               49081780  193.509    0.000 3230.816    0.000 interop.py:274(step)
                9814856  113.882    0.000 2457.257    0.000 rnn.py:555(forward)
                9814859 2348.651    0.000 2348.651    0.000 {built-in method _cudnn_rnn_flatten_weight}
                9814856 2213.656    0.000 2213.656    0.000 {built-in method lstm}
                2454089  116.645    0.000 2088.968    0.001 agent.py:47(<listcomp>)
               29444568   68.597    0.000 1858.718    0.000 linear.py:92(forward)
               88333704   82.967    0.000 1803.031    0.000 activation.py:713(forward)
               29444568  126.374    0.000 1760.316    0.000 functional.py:1669(linear)
               88333704  115.610    0.000 1720.064    0.000 functional.py:1292(leaky_relu)
               49081780  175.768    0.000 1644.272    0.000 exploration.py:33(epsilonGreedy)
               49081780   23.286    0.000 1627.157    0.000 wrapper.py:25(act)
               49081780   71.414    0.000 1603.871    0.000 env.py:197(act)
               88333704 1593.568    0.000 1593.568    0.000 {built-in method torch._C._nn.leaky_relu}
              377852772  990.373    0.000 1552.556    0.000 tensor.py:933(grad)
                2453589  145.119    0.000 1501.966    0.001 optimizer.py:167(zero_grad)
               49081780 1481.932    0.000 1486.935    0.000 libenv.py:352(act)
              107957916 1374.461    0.000 1374.461    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               29444568 1192.926    0.000 1192.926    0.000 {built-in method addmm}
              107957916 1145.279    0.000 1145.279    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               98554891   81.868    0.000  867.850    0.000 extract_dict_ob.py:9(observe)
               98554891   40.419    0.000  785.983    0.000 wrapper.py:19(observe)
               98554891  198.374    0.000  745.563    0.000 libenv.py:344(observe)
                   4908    1.289    0.000  699.849    0.143 agent.py:93(update_target_network)
               53978958  699.153    0.000  699.153    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              461276476  248.092    0.000  693.043    0.000 overrides.py:1073(has_torch_function)
               53978958  650.273    0.000  650.273    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   4908  177.118    0.036  627.039    0.128 memory.py:45(update_distribution)
               53978958  605.222    0.000  605.222    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              355847713  547.456    0.000  547.456    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               53978958  546.103    0.000  546.103    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               51545185  540.268    0.000  540.268    0.000 {built-in method numpy.array}
              147636671  158.711    0.000  535.935    0.000 libenv.py:281(_maybe_copy_dict)
               39260593  478.061    0.000  506.575    0.000 module.py:781(__setattr__)
              442914921  473.176    0.000  473.176    0.000 {method 'copy' of 'numpy.ndarray' objects}
              495628246  170.212    0.000  421.890    0.000 {built-in method builtins.any}
               11478515  164.220    0.000  420.285    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               53978958  413.181    0.000  413.181    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7362267   14.182    0.000  393.246    0.000 functional.py:74(split)
               49081780   43.107    0.000  388.833    0.000 wrapper.py:22(get_info)
                7362267   33.210    0.000  378.116    0.000 tensor.py:460(split)
                9814856   25.988    0.000  365.188    0.000 pooling.py:152(forward)
                2453589  273.897    0.000  360.015    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               49081780  180.768    0.000  345.725    0.000 libenv.py:363(get_info)
               49081780  344.295    0.000  344.295    0.000 memory.py:17(inner)
                7362267  343.308    0.000  343.308    0.000 {function Tensor.split at 0x7f34303a8d30}
                9814856   16.856    0.000  339.200    0.000 _jit_internal.py:257(fn)
               49081780  328.050    0.000  328.050    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9814856   17.604    0.000  320.663    0.000 functional.py:574(_max_pool2d)
               25410759   25.149    0.000  302.863    0.000 <__array_function__ internals>:2(prod)
                9814856  301.938    0.000  301.938    0.000 {built-in method max_pool2d}
               29444568  296.806    0.000  296.806    0.000 {method 't' of 'torch._C._TensorBase' objects}
               25410799   19.959    0.000  273.158    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                2454089   32.575    0.000  262.563    0.000 environments.py:76(<listcomp>)
               39259436  226.436    0.000  254.855    0.000 __init__.py:67(is_acceptable)
               25410759   33.357    0.000  253.200    0.000 fromnumeric.py:2881(prod)
                9814856  251.477    0.000  251.477    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
              951997520  199.306    0.000  249.496    0.000 overrides.py:1086(<genexpr>)
               49081800   35.656    0.000  230.003    0.000 environments.py:79(reset)
               25410759   59.596    0.000  219.843    0.000 fromnumeric.py:70(_wrapreduction)
                7360767  213.044    0.000  213.044    0.000 {built-in method gather}
               24536890  191.159    0.000  191.159    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2453589  183.775    0.000  183.775    0.000 memory.py:43(<listcomp>)
                2453589    6.661    0.000  182.701    0.000 loss.py:445(forward)
                2453589   20.068    0.000  176.039    0.000 functional.py:2637(mse_loss)
              235802356  173.194    0.000  173.334    0.000 module.py:765(__getattr__)
              247824989  172.493    0.000  172.493    0.000 {built-in method torch._C._get_tracing_state}
                2454089   15.647    0.000  170.377    0.000 collector.py:7(collect)
               27869256  165.977    0.000  165.977    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              197109782   52.215    0.000  159.941    0.000 libenv.py:271(_maybe_copy_ndarray)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8428974: <Uncertainty=0.5chaser_0> in cluster <dcc> Done

Job <Uncertainty=0.5chaser_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed Nov 25 23:45:29 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Nov 26 06:18:33 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov 26 06:18:33 2020
Terminated at Fri Nov 27 05:14:03 2020
Results reported at Fri Nov 27 05:14:03 2020

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

    CPU time :                                   83985.00 sec.
    Max Memory :                                 57516 MB
    Average Memory :                             56719.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               3924.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82531 sec.
    Turnaround time :                            106114 sec.

The output (if any) is above this job summary.

  File "main.py", line 11
    if adsad !"#! asdsad":
             ^
SyntaxError: invalid syntax

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8444221: <Uncertainty=0.5chaser_0> in cluster <dcc> Exited

Job <Uncertainty=0.5chaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 01:16:36 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Nov 27 06:04:07 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 06:04:07 2020
Terminated at Fri Nov 27 06:04:09 2020
Results reported at Fri Nov 27 06:04:09 2020

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

    CPU time :                                   0.36 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   3 sec.
    Turnaround time :                            17253 sec.

The output (if any) is above this job summary.

