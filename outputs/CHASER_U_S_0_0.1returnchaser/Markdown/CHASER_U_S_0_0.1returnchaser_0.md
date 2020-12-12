
    Name :                      CHASER_U_S_0_0.1returnchaser-0
    Discount :                  0.995
    Environment :               chaser
    Hours :                     23
    Memory :                    500000
    Update every :              1000
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           1000
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12178247520 function calls (11977528534 primitive calls) in 82540.88 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82540.884 82540.884 {built-in method builtins.exec}
                      1    0.017    0.017 82540.884 82540.884 <string>:1(<module>)
                      1  586.765  586.765 82540.863 82540.863 main.py:92(main)
                2042511  349.218    0.000 57442.657    0.028 agent.py:84(learn)
                1961551  723.800    0.000 56478.340    0.029 agent.py:99(TD_learn)
                1961551  167.240    0.000 32420.771    0.017 memory.py:35(sample_distribution)
                1961551  312.923    0.000 31673.203    0.016 helpers.py:15(stack)
               17896839 18875.080    0.001 18875.080    0.001 {built-in method cat}
        214525182/13812816 1005.761    0.000 14213.332    0.001 module.py:715(_call_impl)
                5965613  195.757    0.000 13167.599    0.002 agent.py:231(forward)
               19859497 12039.472    0.001 12039.476    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2042511  177.054    0.000 9182.181    0.004 agent.py:70(chooseMulti)
               31790615  253.742    0.000 8905.247    0.000 container.py:115(forward)
                2042511   68.593    0.000 8437.740    0.004 environments.py:83(step)
              265426438 7429.254    0.000 7429.254    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                5884653   43.815    0.000 6717.409    0.001 grad_mode.py:23(decorate_context)
                1962550   88.951    0.000 6694.336    0.003 agent.py:58(rememberMulti)
                5884653  257.436    0.000 6602.729    0.001 adam.py:55(step)
                1962550  213.253    0.000 6232.555    0.003 agent.py:62(<listcomp>)
                5884653 1250.831    0.000 5444.966    0.001 functional.py:53(adam)
                2042511   58.134    0.000 5287.011    0.003 environments.py:85(<listcomp>)
               41162484 1360.512    0.000 5275.032    0.000 helpers.py:8(clean)
                5884653   44.822    0.000 5028.374    0.001 tensor.py:181(backward)
                5884653   28.312    0.000 4983.552    0.001 __init__.py:68(backward)
                5884653 4803.112    0.001 4803.112    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               47047137 4563.354    0.000 4563.354    0.000 {built-in method as_tensor}
               35793678   69.878    0.000 3330.312    0.000 conv.py:422(forward)
               35793678   89.063    0.000 3227.289    0.000 conv.py:414(_conv_forward)
               35793678 3123.937    0.000 3123.937    0.000 {built-in method conv2d}
                1962550   81.229    0.000 2915.951    0.001 agent.py:82(<listcomp>)
                2042511   46.869    0.000 2846.130    0.001 environments.py:84(<listcomp>)
               40850220  163.479    0.000 2799.261    0.000 interop.py:274(step)
               47646941  110.066    0.000 2765.252    0.000 linear.py:92(forward)
               39251000  121.932    0.000 2614.881    0.000 exploration.py:34(epsilonGreedy)
               47646941  273.714    0.000 2599.748    0.000 functional.py:1669(linear)
                5965619  396.496    0.000 2163.618    0.000 rnn.py:110(flatten_parameters)
                5965613   83.619    0.000 1882.770    0.000 rnn.py:555(forward)
                5965613 1707.199    0.000 1707.199    0.000 {built-in method lstm}
              411925818  952.179    0.000 1599.307    0.000 tensor.py:933(grad)
               41759291 1511.863    0.000 1511.863    0.000 {built-in method addmm}
               40850220   21.729    0.000 1411.887    0.000 wrapper.py:25(act)
               40850220   54.240    0.000 1390.158    0.000 env.py:197(act)
                5884653  134.165    0.000 1383.306    0.000 optimizer.py:167(zero_grad)
               75512456   74.443    0.000 1380.472    0.000 activation.py:713(forward)
               75512456  104.162    0.000 1306.029    0.000 functional.py:1292(leaky_relu)
               40850220 1301.068    0.000 1305.123    0.000 libenv.py:352(act)
                5965616 1266.377    0.000 1266.377    0.000 {built-in method _cudnn_rnn_flatten_weight}
               75512456 1191.096    0.000 1191.096    0.000 {built-in method torch._C._nn.leaky_relu}
              117693060 1106.984    0.000 1106.984    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              117693060  916.610    0.000  916.610    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              518419535  283.242    0.000  832.311    0.000 overrides.py:1073(has_torch_function)
               82012704   65.326    0.000  771.755    0.000 extract_dict_ob.py:9(observe)
               82012704   35.879    0.000  706.428    0.000 wrapper.py:19(observe)
               82012704  163.607    0.000  670.550    0.000 libenv.py:344(observe)
               58846530  615.428    0.000  615.428    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   2042    1.148    0.001  615.099    0.301 agent.py:157(update_target_network)
               58846530  579.535    0.000  579.535    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              577835806  211.901    0.000  524.132    0.000 {built-in method builtins.any}
                1962550    5.650    0.000  521.333    0.000 agent.py:249(avoid_similar_state)
               58846530  512.420    0.000  512.420    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              122862924  138.252    0.000  504.989    0.000 libenv.py:281(_maybe_copy_dict)
              368590814  444.341    0.000  444.341    0.000 {method 'copy' of 'numpy.ndarray' objects}
               58846530  443.256    0.000  443.256    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               39251000  418.338    0.000  418.338    0.000 memory.py:17(inner)
               27787389  389.061    0.000  414.122    0.000 module.py:781(__setattr__)
               47646941  399.431    0.000  399.431    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6127533   12.507    0.000  394.967    0.000 functional.py:74(split)
              301589638  390.107    0.000  390.107    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                5884653   12.944    0.000  386.237    0.000 loss.py:445(forward)
                6127533   29.014    0.000  381.526    0.000 tensor.py:460(split)
                5884653   46.412    0.000  373.293    0.000 functional.py:2637(mse_loss)
               10988777  140.588    0.000  368.582    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6127533  351.079    0.000  351.079    0.000 {function Tensor.split at 0x7fbc4196cd30}
               40850220   36.188    0.000  329.276    0.000 wrapper.py:22(get_info)
                   2042   86.732    0.042  325.421    0.159 memory.py:45(update_distribution)
               58846530  317.100    0.000  317.100    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               42815855  310.817    0.000  310.817    0.000 {built-in method numpy.array}
             1084486011  249.774    0.000  307.340    0.000 overrides.py:1086(<genexpr>)
                1961551  224.900    0.000  298.016    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               11769306  295.831    0.000  295.831    0.000 {built-in method gather}
               40850220  148.995    0.000  293.088    0.000 libenv.py:363(get_info)
               23939245   25.044    0.000  270.838    0.000 <__array_function__ internals>:2(prod)
                   4084  238.223    0.058  262.975    0.064 {built-in method _pickle.loads}
               45439513  249.158    0.000  249.158    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               23939285   18.289    0.000  241.540    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                5965613   23.693    0.000  237.975    0.000 pooling.py:152(forward)
                2042511   25.215    0.000  236.005    0.000 environments.py:86(<listcomp>)
               40850220  227.804    0.000  227.804    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1962550  204.332    0.000  226.449    0.000 agent.py:149(convert_values)
               23939245   33.015    0.000  223.251    0.000 fromnumeric.py:2881(prod)
                5884653  223.110    0.000  223.110    0.000 {built-in method torch._C._nn.mse_loss}
               23862464  196.009    0.000  217.029    0.000 __init__.py:67(is_acceptable)
                2117740  214.593    0.000  214.593    0.000 {built-in method tensor}
                5965613   11.820    0.000  214.282    0.000 _jit_internal.py:257(fn)
               40850240   33.441    0.000  210.828    0.000 environments.py:89(reset)
                5965613   13.064    0.000  201.437    0.000 functional.py:574(_max_pool2d)
                5887650  193.594    0.000  193.594    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               23939245   56.548    0.000  190.235    0.000 fromnumeric.py:70(_wrapreduction)
                5965613  187.545    0.000  187.545    0.000 {built-in method max_pool2d}
                1961551  177.277    0.000  177.277    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8557114: <CHASER_U_S_0_0.1returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0_0.1returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:11 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Dec 11 15:09:06 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 11 15:09:06 2020
Terminated at Sat Dec 12 14:05:13 2020
Results reported at Sat Dec 12 14:05:13 2020

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

    CPU time :                                   90229.00 sec.
    Max Memory :                                 54951 MB
    Average Memory :                             54250.15 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6489.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82567 sec.
    Turnaround time :                            82622 sec.

The output (if any) is above this job summary.

