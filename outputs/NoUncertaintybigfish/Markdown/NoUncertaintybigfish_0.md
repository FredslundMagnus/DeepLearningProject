
    Name :                      NoUncertaintybigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12256523746 function calls (12019498171 primitive calls) in 82518.67 seconds

##    Ordered by: cumulative time
   List reduced from 1347 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82518.668 82518.668 {built-in method builtins.exec}
                      1    0.046    0.046 82518.668 82518.668 <string>:1(<module>)
                      1  457.632  457.632 82518.621 82518.621 main.py:11(main)
                2469326  111.562    0.000 55716.105    0.023 agent.py:49(learn)
                2468826  488.826    0.000 54893.628    0.022 agent.py:59(TD_learn)
                2468826  171.286    0.000 26927.225    0.011 memory.py:35(sample_distribution)
                2468826  295.154    0.000 26097.247    0.011 helpers.py:12(stack)
        249363926/12344630 1085.463    0.000 18658.234    0.002 module.py:715(_call_impl)
                9875804  290.496    0.000 18358.343    0.002 agent.py:139(forward)
               22221000 13415.150    0.001 13415.153    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               22220934 11827.149    0.001 11827.149    0.001 {built-in method cat}
               39503216  305.515    0.000 11029.357    0.000 container.py:115(forward)
                2469326   68.379    0.000 9466.800    0.004 environments.py:73(step)
              334211010 9149.443    0.000 9149.443    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2469326   45.504    0.000 8919.897    0.004 agent.py:43(chooseMulti)
                2469326    7.623    0.000 7762.599    0.003 agent.py:34(rememberMulti)
                2469326  325.242    0.000 7754.976    0.003 agent.py:35(<listcomp>)
                2468826   21.529    0.000 6361.195    0.003 grad_mode.py:23(decorate_context)
                2468826  181.831    0.000 6310.928    0.003 adam.py:55(step)
                2469326   60.105    0.000 6241.925    0.003 environments.py:75(<listcomp>)
               49540195 1463.198    0.000 6203.861    0.000 helpers.py:8(clean)
               59254824  103.921    0.000 5551.338    0.000 conv.py:422(forward)
               56946673 5458.415    0.000 5458.415    0.000 {built-in method as_tensor}
               59254824  112.584    0.000 5401.284    0.000 conv.py:414(_conv_forward)
                2468826 1155.633    0.000 5389.556    0.002 functional.py:53(adam)
               59254824 5268.878    0.000 5268.878    0.000 {built-in method conv2d}
                2468826   27.660    0.000 4873.209    0.002 tensor.py:181(backward)
                2468826   17.584    0.000 4845.549    0.002 __init__.py:68(backward)
                2468826 4749.361    0.002 4749.361    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2469326  115.977    0.000 3673.132    0.001 agent.py:47(<listcomp>)
                9875810  582.387    0.000 3586.551    0.000 rnn.py:110(flatten_parameters)
               49386520  171.775    0.000 3223.457    0.000 exploration.py:33(epsilonGreedy)
                2469326   53.711    0.000 2952.183    0.001 environments.py:74(<listcomp>)
               49386520  196.465    0.000 2898.472    0.000 interop.py:274(step)
                9875804  108.903    0.000 2549.568    0.000 rnn.py:555(forward)
                9875807 2353.638    0.000 2353.638    0.000 {built-in method _cudnn_rnn_flatten_weight}
                9875804 2308.648    0.000 2308.648    0.000 {built-in method lstm}
               29627412   69.839    0.000 1902.672    0.000 linear.py:92(forward)
               88882236   82.836    0.000 1838.256    0.000 activation.py:713(forward)
               29627412  128.608    0.000 1798.211    0.000 functional.py:1669(linear)
               88882236  123.792    0.000 1755.421    0.000 functional.py:1292(leaky_relu)
               88882236 1620.119    0.000 1620.119    0.000 {built-in method torch._C._nn.leaky_relu}
              330822750  891.605    0.000 1391.153    0.000 tensor.py:933(grad)
                2468826  128.023    0.000 1312.764    0.001 optimizer.py:167(zero_grad)
               49386520   23.124    0.000 1292.639    0.000 wrapper.py:25(act)
               49386520   73.874    0.000 1269.514    0.000 env.py:197(act)
               29627412 1219.518    0.000 1219.518    0.000 {built-in method addmm}
               49386520 1146.406    0.000 1151.037    0.000 libenv.py:352(act)
               88877736 1148.960    0.000 1148.960    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               88877736  956.260    0.000  956.260    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               98926715   78.703    0.000  841.062    0.000 extract_dict_ob.py:9(observe)
               98926715   41.379    0.000  762.360    0.000 wrapper.py:19(observe)
               98926715  190.779    0.000  720.981    0.000 libenv.py:344(observe)
                   4938    1.307    0.000  710.915    0.144 agent.py:93(update_target_network)
                   4938  175.666    0.036  637.018    0.129 memory.py:45(update_distribution)
              404889204  226.202    0.000  623.671    0.000 overrides.py:1073(has_torch_function)
               44438868  599.158    0.000  599.158    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               51865222  552.009    0.000  552.009    0.000 {built-in method numpy.array}
               44438868  544.447    0.000  544.447    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              356123634  529.855    0.000  529.855    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              148313235  163.173    0.000  522.169    0.000 libenv.py:281(_maybe_copy_dict)
               44438868  511.738    0.000  511.738    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               39504385  478.041    0.000  508.237    0.000 module.py:781(__setattr__)
              444944643  457.960    0.000  457.960    0.000 {method 'copy' of 'numpy.ndarray' objects}
               44438868  456.933    0.000  456.933    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11494630  168.310    0.000  421.224    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               49386520   44.816    0.000  402.020    0.000 wrapper.py:22(get_info)
                7407978   13.024    0.000  395.112    0.000 functional.py:74(split)
                7407978   34.103    0.000  381.121    0.000 tensor.py:460(split)
              439454292  154.786    0.000  377.903    0.000 {built-in method builtins.any}
                9875804   25.138    0.000  370.266    0.000 pooling.py:152(forward)
                2468826  278.384    0.000  364.002    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               49386520  187.007    0.000  357.204    0.000 libenv.py:363(get_info)
               49386520  352.923    0.000  352.923    0.000 memory.py:17(inner)
               44438868  348.555    0.000  348.555    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7407978  345.376    0.000  345.376    0.000 {function Tensor.split at 0x7f35558dbd30}
                9875804   16.811    0.000  345.128    0.000 _jit_internal.py:257(fn)
               49386520  333.698    0.000  333.698    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9875804   18.965    0.000  326.612    0.000 functional.py:574(_max_pool2d)
                9875804  306.451    0.000  306.451    0.000 {built-in method max_pool2d}
               29627412  303.497    0.000  303.497    0.000 {method 't' of 'torch._C._TensorBase' objects}
               25458226   25.239    0.000  301.026    0.000 <__array_function__ internals>:2(prod)
               25458266   20.857    0.000  271.405    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                9875804  256.783    0.000  256.783    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
               39503228  226.412    0.000  254.779    0.000 __init__.py:67(is_acceptable)
               25458226   34.021    0.000  250.547    0.000 fromnumeric.py:2881(prod)
              839405820  173.924    0.000  220.953    0.000 overrides.py:1086(<genexpr>)
               25458226   59.696    0.000  216.526    0.000 fromnumeric.py:70(_wrapreduction)
                2469326   33.742    0.000  204.313    0.000 environments.py:76(<listcomp>)
               24689260  196.348    0.000  196.348    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2468826  195.634    0.000  195.634    0.000 memory.py:43(<listcomp>)
                2468826    7.643    0.000  190.693    0.000 loss.py:445(forward)
                2468826   20.888    0.000  183.049    0.000 functional.py:2637(mse_loss)
              237266608  181.914    0.000  182.051    0.000 module.py:765(__getattr__)
              249363926  176.963    0.000  176.963    0.000 {built-in method torch._C._get_tracing_state}
                2469326   17.356    0.000  172.035    0.000 collector.py:7(collect)
               49386540   35.201    0.000  170.585    0.000 environments.py:79(reset)
               27931990  164.611    0.000  164.611    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              197853430   51.260    0.000  161.846    0.000 libenv.py:271(_maybe_copy_ndarray)
                4938653  153.632    0.000  153.633    0.000 {built-in method builtins.sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8428973: <NoUncertaintybigfish_0> in cluster <dcc> Done

Job <NoUncertaintybigfish_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed Nov 25 23:45:29 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Nov 26 02:16:05 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov 26 02:16:05 2020
Terminated at Fri Nov 27 01:11:30 2020
Results reported at Fri Nov 27 01:11:30 2020

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

    CPU time :                                   85183.00 sec.
    Max Memory :                                 56938 MB
    Average Memory :                             56197.91 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4502.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82525 sec.
    Turnaround time :                            91561 sec.

The output (if any) is above this job summary.

  File "main.py", line 11
    if adsad !"#! asdsad":
             ^
SyntaxError: invalid syntax

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8444220: <NoUncertaintybigfish_0> in cluster <dcc> Exited

Job <NoUncertaintybigfish_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 01:16:36 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Nov 27 06:04:03 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 06:04:03 2020
Terminated at Fri Nov 27 06:04:06 2020
Results reported at Fri Nov 27 06:04:06 2020

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

    CPU time :                                   0.37 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   3 sec.
    Turnaround time :                            17250 sec.

The output (if any) is above this job summary.

