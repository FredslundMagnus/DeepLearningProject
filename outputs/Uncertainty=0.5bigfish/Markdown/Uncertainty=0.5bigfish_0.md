
    Name :                      Uncertainty=0.5bigfish-0
    Discount :                  0.995
    Environment :               bigfish
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


      12796757713 function calls (12561926666 primitive calls) in 82524.62 seconds

##    Ordered by: cumulative time
   List reduced from 1348 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82524.620 82524.620 {built-in method builtins.exec}
                      1    0.025    0.025 82524.620 82524.620 <string>:1(<module>)
                      1  483.464  483.464 82524.593 82524.593 main.py:11(main)
                2446466  116.575    0.000 54528.947    0.022 agent.py:49(learn)
                2445966  441.393    0.000 53685.672    0.022 agent.py:59(TD_learn)
                2445966  182.284    0.000 29100.297    0.012 memory.py:35(sample_distribution)
                2445966  338.294    0.000 28262.626    0.012 helpers.py:12(stack)
        247055066/12230330 1055.779    0.000 16058.285    0.001 module.py:715(_call_impl)
                9784364  265.702    0.000 15782.768    0.002 agent.py:139(forward)
               26907126 14033.963    0.001 14033.963    0.001 {built-in method cat}
               22015260 13385.347    0.001 13385.354    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2446466   45.554    0.000 12089.901    0.005 agent.py:43(chooseMulti)
              331032102 12088.206    0.000 12088.206    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               39137456  272.011    0.000 9412.730    0.000 container.py:115(forward)
                2446466   68.163    0.000 8709.178    0.004 environments.py:73(step)
                2446466   91.664    0.000 7413.486    0.003 agent.py:47(<listcomp>)
               48929320  141.743    0.000 7087.042    0.000 exploration.py:33(epsilonGreedy)
                2446466    7.682    0.000 6520.377    0.003 agent.py:34(rememberMulti)
                2446466  224.531    0.000 6512.695    0.003 agent.py:35(<listcomp>)
                2446466   51.979    0.000 5649.772    0.002 environments.py:75(<listcomp>)
               49294522 1446.038    0.000 5646.801    0.000 helpers.py:8(clean)
                2445966   21.723    0.000 5502.479    0.002 grad_mode.py:23(decorate_context)
                2445966  204.009    0.000 5451.942    0.002 adam.py:55(step)
               56632420 4943.814    0.000 4943.814    0.000 {built-in method as_tensor}
               58706184  101.450    0.000 4779.278    0.000 conv.py:422(forward)
               58706184  123.057    0.000 4632.030    0.000 conv.py:414(_conv_forward)
               58706184 4488.144    0.000 4488.144    0.000 {built-in method conv2d}
                2445966 1006.390    0.000 4481.453    0.002 functional.py:53(adam)
                2445966   23.336    0.000 4374.620    0.002 tensor.py:181(backward)
                2445966   16.800    0.000 4351.284    0.002 __init__.py:68(backward)
                2445966 4265.738    0.002 4265.738    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9784370  511.618    0.000 2833.392    0.000 rnn.py:110(flatten_parameters)
                2446466   51.589    0.000 2769.440    0.001 environments.py:74(<listcomp>)
               48929320  178.974    0.000 2717.852    0.000 interop.py:274(step)
                9784364  113.226    0.000 2456.279    0.000 rnn.py:555(forward)
                9784364 2214.327    0.000 2214.327    0.000 {built-in method lstm}
                9784367 1705.742    0.000 1705.742    0.000 {built-in method _cudnn_rnn_flatten_weight}
               29353092   69.737    0.000 1592.217    0.000 linear.py:92(forward)
               29353092  124.695    0.000 1492.529    0.000 functional.py:1669(linear)
               88059276   84.094    0.000 1462.282    0.000 activation.py:713(forward)
               88059276  121.692    0.000 1378.188    0.000 functional.py:1292(leaky_relu)
              376678830  816.317    0.000 1371.723    0.000 tensor.py:933(grad)
               88059276 1243.722    0.000 1243.722    0.000 {built-in method torch._C._nn.leaky_relu}
                2445966  117.467    0.000 1183.969    0.000 optimizer.py:167(zero_grad)
               48929320   23.586    0.000 1170.295    0.000 wrapper.py:25(act)
               48929320   60.232    0.000 1146.709    0.000 env.py:197(act)
               48929320 1048.625    0.000 1053.340    0.000 libenv.py:352(act)
               29353092  991.828    0.000  991.828    0.000 {built-in method addmm}
              107622504  918.412    0.000  918.412    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               98223842   75.711    0.000  842.413    0.000 extract_dict_ob.py:9(observe)
              107622504  777.431    0.000  777.431    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               98223842   45.294    0.000  766.701    0.000 wrapper.py:19(observe)
                   4892    1.374    0.000  726.700    0.149 agent.py:93(update_target_network)
               98223842  190.074    0.000  721.407    0.000 libenv.py:344(observe)
              459843352  238.737    0.000  686.041    0.000 overrides.py:1073(has_torch_function)
                   4892  181.637    0.037  654.966    0.134 memory.py:45(update_distribution)
               51385070  552.683    0.000  552.683    0.000 {built-in method numpy.array}
              147153162  163.284    0.000  531.601    0.000 libenv.py:281(_maybe_copy_dict)
               39138625  481.300    0.000  509.052    0.000 module.py:781(__setattr__)
               53811252  491.004    0.000  491.004    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               53811252  467.108    0.000  467.108    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              441464378  456.115    0.000  456.115    0.000 {method 'copy' of 'numpy.ndarray' objects}
               53811252  430.666    0.000  430.666    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              494088400  169.415    0.000  423.723    0.000 {built-in method builtins.any}
                7339398   13.528    0.000  394.518    0.000 functional.py:74(split)
               11473138  148.500    0.000  390.692    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               48929320   40.149    0.000  384.371    0.000 wrapper.py:22(get_info)
               48929320  381.445    0.000  381.445    0.000 memory.py:17(inner)
                7339398   31.802    0.000  379.888    0.000 tensor.py:460(split)
               53811252  373.441    0.000  373.441    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              354761898  349.565    0.000  349.565    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7339398  346.460    0.000  346.460    0.000 {function Tensor.split at 0x7f81c7cd2d30}
                2445966  264.217    0.000  345.412    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               48929320  176.197    0.000  344.222    0.000 libenv.py:363(get_info)
                9784364   27.074    0.000  322.175    0.000 pooling.py:152(forward)
                9784364   17.349    0.000  295.102    0.000 _jit_internal.py:257(fn)
               25392382   24.960    0.000  287.502    0.000 <__array_function__ internals>:2(prod)
                9784364   17.054    0.000  276.180    0.000 functional.py:574(_max_pool2d)
               53811252  259.728    0.000  259.728    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               25392422   19.332    0.000  258.248    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                9784364  257.704    0.000  257.704    0.000 {built-in method max_pool2d}
              949039796  204.648    0.000  251.961    0.000 overrides.py:1086(<genexpr>)
               25392382   31.547    0.000  238.916    0.000 fromnumeric.py:2881(prod)
               39137468  207.599    0.000  235.876    0.000 __init__.py:67(is_acceptable)
               48929320  234.780    0.000  234.780    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               29353092  233.248    0.000  233.248    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2446466   27.414    0.000  221.802    0.000 environments.py:76(<listcomp>)
                9784364  214.614    0.000  214.614    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
                2445966  211.214    0.000  211.214    0.000 memory.py:43(<listcomp>)
               25392382   61.998    0.000  207.369    0.000 fromnumeric.py:70(_wrapreduction)
               48929340   33.289    0.000  194.400    0.000 environments.py:79(reset)
                7337898  179.385    0.000  179.385    0.000 {built-in method gather}
              235069748  174.093    0.000  174.231    0.000 module.py:765(__getattr__)
                2445966    6.498    0.000  163.839    0.000 loss.py:445(forward)
                2446466   15.662    0.000  163.398    0.000 collector.py:7(collect)
                2445966   21.804    0.000  157.342    0.000 functional.py:2637(mse_loss)
               24460660  154.575    0.000  154.575    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              196447684   54.888    0.000  153.408    0.000 libenv.py:271(_maybe_copy_ndarray)
               27843240  152.650    0.000  152.650    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                4892933  146.677    0.000  146.678    0.000 {built-in method builtins.sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8428972: <Uncertainty=0.5bigfish_0> in cluster <dcc> Done

Job <Uncertainty=0.5bigfish_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed Nov 25 23:45:29 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Nov 26 00:59:40 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov 26 00:59:40 2020
Terminated at Thu Nov 26 23:55:14 2020
Results reported at Thu Nov 26 23:55:14 2020

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

    CPU time :                                   87840.00 sec.
    Max Memory :                                 57030 MB
    Average Memory :                             56306.55 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4410.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82535 sec.
    Turnaround time :                            86985 sec.

The output (if any) is above this job summary.

  File "main.py", line 11
    if adsad !"#! asdsad":
             ^
SyntaxError: invalid syntax

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8444219: <Uncertainty=0.5bigfish_0> in cluster <dcc> Exited

Job <Uncertainty=0.5bigfish_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 01:16:36 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Nov 27 05:10:16 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 05:10:16 2020
Terminated at Fri Nov 27 05:10:18 2020
Results reported at Fri Nov 27 05:10:18 2020

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
    Turnaround time :                            14022 sec.

The output (if any) is above this job summary.

