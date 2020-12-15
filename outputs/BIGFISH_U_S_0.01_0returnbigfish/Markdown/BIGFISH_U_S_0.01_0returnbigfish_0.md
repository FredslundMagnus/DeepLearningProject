[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0.01_0returnbigfish-0
    Discount :                  0.995
    Environment :               bigfish
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
    Uncertainty weight :        0.01
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      9224751636 function calls (9012655709 primitive calls) in 82525.08 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82525.079 82525.079 {built-in method builtins.exec}
                      1    0.027    0.027 82525.079 82525.079 <string>:1(<module>)
                      1  595.262  595.262 82525.051 82525.051 main.py:92(main)
                2159251  313.134    0.000 56894.712    0.026 agent.py:84(learn)
                2072294  720.018    0.000 55953.370    0.027 agent.py:99(TD_learn)
                2072294  164.254    0.000 34090.001    0.016 memory.py:35(sample_distribution)
                2072294  308.900    0.000 33325.016    0.016 helpers.py:15(stack)
               18911517 20355.245    0.001 20355.245    0.001 {built-in method cat}
        226683327/14594014 1025.758    0.000 13733.433    0.001 module.py:710(_call_impl)
                6303839  202.401    0.000 12711.458    0.002 agent.py:231(forward)
               20984918 12405.978    0.001 12405.981    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2159251  173.145    0.000 10105.717    0.005 agent.py:70(chooseMulti)
              280946354 8788.358    0.000 8788.358    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               33592488  249.770    0.000 8581.214    0.000 container.py:115(forward)
                2159251   69.411    0.000 8003.861    0.004 environments.py:83(step)
                2073293   83.595    0.000 6737.893    0.003 agent.py:58(rememberMulti)
                2073293  202.550    0.000 6288.529    0.003 agent.py:62(<listcomp>)
                6216882   34.541    0.000 5647.512    0.001 grad_mode.py:12(decorate_context)
                6216882 1462.063    0.000 5569.956    0.001 adam.py:51(step)
                2159251   55.263    0.000 5112.454    0.002 environments.py:85(<listcomp>)
               43410315 1386.555    0.000 5088.245    0.000 helpers.py:8(clean)
                6216882   28.316    0.000 4953.964    0.001 tensor.py:155(backward)
                6216882   33.502    0.000 4925.648    0.001 __init__.py:57(backward)
                6216882 4750.418    0.001 4750.418    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               49627197 4280.731    0.000 4280.731    0.000 {built-in method as_tensor}
                2073293   82.485    0.000 4180.936    0.002 agent.py:82(<listcomp>)
               41465860  116.158    0.000 3890.995    0.000 exploration.py:34(epsilonGreedy)
               37823034   70.362    0.000 3213.780    0.000 conv.py:418(forward)
               37823034   96.014    0.000 3109.161    0.000 conv.py:410(_conv_forward)
               37823034 2998.351    0.000 2998.351    0.000 {built-in method conv2d}
                2159251   48.488    0.000 2620.230    0.001 environments.py:84(<listcomp>)
               50346752  105.233    0.000 2606.995    0.000 linear.py:90(forward)
               43185020  173.177    0.000 2571.742    0.000 interop.py:274(step)
               50346752  271.969    0.000 2446.505    0.000 functional.py:1655(linear)
                6303845  351.947    0.000 1954.168    0.000 rnn.py:109(flatten_parameters)
                6303839   79.610    0.000 1917.615    0.000 rnn.py:550(forward)
                6303839 1738.932    0.000 1738.932    0.000 {built-in method lstm}
               44126873 1432.977    0.000 1432.977    0.000 {built-in method addmm}
               79792654   82.525    0.000 1328.010    0.000 activation.py:653(forward)
               79792654  103.246    0.000 1245.485    0.000 functional.py:1277(leaky_relu)
                6303842 1146.554    0.000 1146.554    0.000 {built-in method _cudnn_rnn_flatten_weight}
               79792654 1131.320    0.000 1131.320    0.000 {built-in method torch._C._nn.leaky_relu}
               43185020   20.546    0.000 1126.749    0.000 wrapper.py:25(act)
               43185020   57.531    0.000 1106.202    0.000 env.py:197(act)
              124337640 1026.083    0.000 1026.083    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               43185020 1013.961    0.000 1018.539    0.000 libenv.py:352(act)
              124337640  886.714    0.000  886.714    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               86595335   69.804    0.000  792.561    0.000 extract_dict_ob.py:9(observe)
               86595335   39.226    0.000  722.757    0.000 wrapper.py:19(observe)
               86595335  173.003    0.000  683.531    0.000 libenv.py:344(observe)
               62168820  633.383    0.000  633.383    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   2159    1.155    0.001  628.208    0.291 agent.py:157(update_target_network)
               62168820  538.145    0.000  538.145    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                6216882   94.336    0.000  526.290    0.000 optimizer.py:166(zero_grad)
              129780355  141.586    0.000  511.053    0.000 libenv.py:281(_maybe_copy_dict)
                2073293    5.469    0.000  490.295    0.000 agent.py:249(avoid_similar_state)
              389343224  442.361    0.000  442.361    0.000 {method 'copy' of 'numpy.ndarray' objects}
               62168820  422.827    0.000  422.827    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               41465860  417.182    0.000  417.182    0.000 memory.py:17(inner)
               29361779  391.479    0.000  416.227    0.000 module.py:774(__setattr__)
               62168820  407.430    0.000  407.430    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              319423994  394.241    0.000  394.241    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                6216882   12.707    0.000  389.906    0.000 loss.py:444(forward)
                6216882   52.775    0.000  377.200    0.000 functional.py:2621(mse_loss)
               11096151  140.088    0.000  368.258    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               50346752  358.240    0.000  358.240    0.000 {method 't' of 'torch._C._TensorBase' objects}
               43185020   37.966    0.000  343.584    0.000 wrapper.py:22(get_info)
                   2159   89.639    0.042  343.126    0.159 memory.py:45(update_distribution)
               45261632  329.868    0.000  329.868    0.000 {built-in method numpy.array}
                2072294  238.923    0.000  311.180    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               43185020  158.158    0.000  305.618    0.000 libenv.py:363(get_info)
               62168820  290.829    0.000  290.829    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               12433764  278.975    0.000  278.975    0.000 {built-in method gather}
               24264736   23.511    0.000  269.400    0.000 <__array_function__ internals>:2(prod)
                   4318  234.298    0.054  258.619    0.060 {built-in method _pickle.loads}
               48010590  246.605    0.000  246.605    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6477753   12.223    0.000  243.513    0.000 functional.py:68(split)
               24264776   18.867    0.000  241.893    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6477753   12.019    0.000  230.309    0.000 tensor.py:367(split)
                2073293  190.534    0.000  225.598    0.000 agent.py:149(convert_values)
              310844208  193.404    0.000  224.325    0.000 tensor.py:725(grad)
                2237375  224.011    0.000  224.011    0.000 {built-in method tensor}
               24264736   30.166    0.000  223.026    0.000 fromnumeric.py:2881(prod)
                6303839   18.867    0.000  218.797    0.000 pooling.py:156(forward)
                6477753  216.907    0.000  216.907    0.000 {function Tensor.split at 0x7f5b42e3b9d0}
               25215368  194.322    0.000  215.739    0.000 __init__.py:66(is_acceptable)
               43185020  214.855    0.000  214.855    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6216882  209.989    0.000  209.989    0.000 {built-in method torch._C._nn.mse_loss}
                2159251   25.148    0.000  201.766    0.000 environments.py:86(<listcomp>)
                6303839   12.301    0.000  199.930    0.000 _jit_internal.py:237(fn)
               24264736   56.842    0.000  192.860    0.000 fromnumeric.py:70(_wrapreduction)
                6303839   12.801    0.000  186.494    0.000 functional.py:564(_max_pool2d)
                2072294  184.769    0.000  184.769    0.000 memory.py:43(<listcomp>)
                6219879  178.089    0.000  178.089    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               43185040   32.105    0.000  176.645    0.000 environments.py:89(reset)
                6303839  172.882    0.000  172.882    0.000 {built-in method max_pool2d}
              222713086  168.543    0.000  168.637    0.000 module.py:758(__getattr__)
                2159251   18.352    0.000  158.178    0.000 collector.py:8(collect)
               12434763  152.059    0.000  152.059    0.000 {method 'type' of 'torch._C._TensorBase' objects}
               26339189  145.713    0.000  145.713    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8557624: <BIGFISH_U_S_0.01_0returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0.01_0returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:46 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Dec 13 15:22:22 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec 13 15:22:22 2020
Terminated at Mon Dec 14 14:18:03 2020
Results reported at Mon Dec 14 14:18:03 2020

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

    CPU time :                                   91566.00 sec.
    Max Memory :                                 54010 MB
    Average Memory :                             53358.89 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7430.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82540 sec.
    Turnaround time :                            252977 sec.

The output (if any) is above this job summary.

