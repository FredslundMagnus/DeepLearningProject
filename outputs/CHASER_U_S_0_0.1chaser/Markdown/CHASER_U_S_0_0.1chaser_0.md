[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      CHASER_U_S_0_0.1chaser-0
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


      10921564323 function calls (10669056703 primitive calls) in 82521.04 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82521.040 82521.040 {built-in method builtins.exec}
                      1    0.055    0.055 82521.040 82521.040 <string>:1(<module>)
                      1  583.820  583.820 82520.979 82520.979 main.py:92(main)
                2570292  220.629    0.000 52707.850    0.021 agent.py:84(learn)
                2467343  669.845    0.000 51840.936    0.021 agent.py:99(TD_learn)
                2467343  175.632    0.000 27783.474    0.011 memory.py:35(sample_distribution)
                2467343  310.551    0.000 26963.117    0.011 helpers.py:15(stack)
        269876355/17375349 1147.189    0.000 15052.991    0.001 module.py:710(_call_impl)
                7504978  218.765    0.000 13904.965    0.002 agent.py:216(forward)
               24983384 13611.395    0.001 13611.402    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2570292  190.589    0.000 13373.414    0.005 agent.py:70(chooseMulti)
               22514934 12829.926    0.001 12829.926    0.001 {built-in method cat}
              336122786 11402.256    0.000 11402.256    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               39993232  285.765    0.000 9607.742    0.000 container.py:115(forward)
                2570292   71.762    0.000 9042.551    0.004 environments.py:83(step)
                2468342   93.701    0.000 7029.595    0.003 agent.py:82(<listcomp>)
               49366840  132.249    0.000 6702.204    0.000 exploration.py:34(epsilonGreedy)
                2468342   89.026    0.000 6619.854    0.003 agent.py:58(rememberMulti)
                7402029   38.865    0.000 6507.331    0.001 grad_mode.py:12(decorate_context)
                7402029 1639.702    0.000 6417.927    0.001 adam.py:51(step)
                2468342  208.667    0.000 6161.211    0.002 agent.py:62(<listcomp>)
                7402029   31.599    0.000 5512.923    0.001 tensor.py:155(backward)
                2570292   65.684    0.000 5495.261    0.002 environments.py:85(<listcomp>)
                7402029   38.542    0.000 5481.323    0.001 __init__.py:57(backward)
               51793613 1451.119    0.000 5477.820    0.000 helpers.py:8(clean)
                7402029 5278.472    0.001 5278.472    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               59195642 4591.231    0.000 4591.231    0.000 {built-in method as_tensor}
               45029868   82.883    0.000 3594.237    0.000 conv.py:418(forward)
               45029868   96.353    0.000 3474.530    0.000 conv.py:410(_conv_forward)
               45029868 3361.544    0.000 3361.544    0.000 {built-in method conv2d}
                2570292   55.015    0.000 3222.669    0.001 environments.py:84(<listcomp>)
               51405840  190.334    0.000 3167.654    0.000 interop.py:274(step)
               59939872  122.181    0.000 2914.208    0.000 linear.py:90(forward)
               59939872  322.458    0.000 2729.498    0.000 functional.py:1655(linear)
                7504984  391.905    0.000 2196.611    0.000 rnn.py:109(flatten_parameters)
                7504978   89.661    0.000 1835.884    0.000 rnn.py:550(forward)
                7504978 1645.591    0.000 1645.591    0.000 {built-in method lstm}
               52534846 1593.860    0.000 1593.860    0.000 {built-in method addmm}
               51405840   22.943    0.000 1592.718    0.000 wrapper.py:25(act)
               51405840   64.751    0.000 1569.775    0.000 env.py:197(act)
               94996420   81.341    0.000 1482.662    0.000 activation.py:653(forward)
               51405840 1466.445    0.000 1471.193    0.000 libenv.py:352(act)
               94996420  127.633    0.000 1401.322    0.000 functional.py:1277(leaky_relu)
                7504981 1317.411    0.000 1317.411    0.000 {built-in method _cudnn_rnn_flatten_weight}
               94996420 1261.063    0.000 1261.063    0.000 {built-in method torch._C._nn.leaky_relu}
              148040580 1190.897    0.000 1190.897    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              148040580 1038.182    0.000 1038.182    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              103199453   76.436    0.000  856.308    0.000 extract_dict_ob.py:9(observe)
              103199453   43.416    0.000  779.872    0.000 wrapper.py:19(observe)
               74020290  739.021    0.000  739.021    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              103199453  188.427    0.000  736.456    0.000 libenv.py:344(observe)
                   2570    1.018    0.000  646.285    0.251 agent.py:142(update_target_network)
               74020290  614.721    0.000  614.721    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7402029  102.541    0.000  598.750    0.000 optimizer.py:166(zero_grad)
                2468342    6.505    0.000  557.944    0.000 agent.py:234(avoid_similar_state)
              154605293  159.932    0.000  546.742    0.000 libenv.py:281(_maybe_copy_dict)
               74020290  497.712    0.000  497.712    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               74020290  477.932    0.000  477.932    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              463818449  471.658    0.000  471.658    0.000 {method 'copy' of 'numpy.ndarray' objects}
              376744273  446.118    0.000  446.118    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7402029   14.469    0.000  432.596    0.000 loss.py:444(forward)
                7402029   59.078    0.000  418.126    0.000 functional.py:2621(mse_loss)
               34956433  383.107    0.000  408.738    0.000 module.py:774(__setattr__)
               49366840  385.854    0.000  385.854    0.000 memory.py:17(inner)
               51405840   42.277    0.000  383.091    0.000 wrapper.py:22(get_info)
               59939872  381.643    0.000  381.643    0.000 {method 't' of 'torch._C._TensorBase' objects}
               11491651  146.650    0.000  375.619    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                   2570   98.276    0.038  354.901    0.138 memory.py:45(update_distribution)
               53878323  341.478    0.000  341.478    0.000 {built-in method numpy.array}
               74020290  341.137    0.000  341.137    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               51405840  175.922    0.000  340.814    0.000 libenv.py:363(get_info)
                2467343  262.860    0.000  340.295    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               25450785   24.190    0.000  272.275    0.000 <__array_function__ internals>:2(prod)
                   5140  237.938    0.046  264.395    0.051 {built-in method _pickle.loads}
                7710876   14.204    0.000  256.392    0.000 functional.py:68(split)
                2570292   28.669    0.000  252.860    0.000 environments.py:86(<listcomp>)
              370101558  215.056    0.000  249.736    0.000 tensor.py:725(grad)
               25450825   19.394    0.000  244.053    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               51405840  241.848    0.000  241.848    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7710876   13.098    0.000  241.103    0.000 tensor.py:367(split)
                7504978   22.553    0.000  240.286    0.000 pooling.py:156(forward)
                7402029  231.698    0.000  231.698    0.000 {built-in method torch._C._nn.mse_loss}
               30019924  203.649    0.000  228.393    0.000 __init__.py:66(is_acceptable)
                7710876  226.478    0.000  226.478    0.000 {function Tensor.split at 0x7f9b377709d0}
                9869372  225.422    0.000  225.422    0.000 {built-in method gather}
               25450785   30.255    0.000  224.659    0.000 fromnumeric.py:2881(prod)
               51405860   35.216    0.000  224.207    0.000 environments.py:89(reset)
               44823970  224.000    0.000  224.000    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2468342  215.044    0.000  221.406    0.000 agent.py:134(convert_values)
                2663660  220.578    0.000  220.578    0.000 {built-in method tensor}
                7504978   13.423    0.000  217.733    0.000 _jit_internal.py:237(fn)
                2467343  205.242    0.000  205.242    0.000 memory.py:43(<listcomp>)
                7504978   14.459    0.000  203.082    0.000 functional.py:564(_max_pool2d)
                7405026  197.086    0.000  197.086    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               25450785   58.341    0.000  194.404    0.000 fromnumeric.py:70(_wrapreduction)
                7504978  187.694    0.000  187.694    0.000 {built-in method max_pool2d}
              265148896  185.416    0.000  185.529    0.000 module.py:758(__getattr__)
                2570292   19.026    0.000  167.744    0.000 collector.py:8(collect)
              269876355  166.070    0.000  166.070    0.000 {built-in method torch._C._get_tracing_state}
                7402029   40.548    0.000  161.794    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8552392: <CHASER_U_S_0_0.1chaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0_0.1chaser_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Tue Dec  8 22:35:06 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Dec  8 23:45:55 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec  8 23:45:55 2020
Terminated at Wed Dec  9 22:41:23 2020
Results reported at Wed Dec  9 22:41:23 2020

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

    CPU time :                                   86943.00 sec.
    Max Memory :                                 54565 MB
    Average Memory :                             53883.93 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6875.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82530 sec.
    Turnaround time :                            86777 sec.

The output (if any) is above this job summary.

