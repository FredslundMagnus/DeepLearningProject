[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0.1_0returnbigfish-0
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
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11163643399 function calls (10906241082 primitive calls) in 82531.47 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82531.469 82531.469 {built-in method builtins.exec}
                      1    0.052    0.052 82531.469 82531.469 <string>:1(<module>)
                      1  560.596  560.596 82531.417 82531.417 main.py:92(main)
                2620120  273.541    0.000 52918.025    0.020 agent.py:84(learn)
                2515172  797.266    0.000 52016.764    0.021 agent.py:99(TD_learn)
                2515172  176.234    0.000 27273.733    0.011 memory.py:35(sample_distribution)
                2515172  277.630    0.000 26450.204    0.011 helpers.py:15(stack)
        275107854/17712151 1176.070    0.000 15172.753    0.001 module.py:710(_call_impl)
                7650464  217.515    0.000 14012.987    0.002 agent.py:231(forward)
               25467671 13887.328    0.001 13887.409    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2620120  187.786    0.000 13564.015    0.005 agent.py:70(chooseMulti)
               22951392 12066.953    0.001 12066.953    0.001 {built-in method cat}
              342878028 11606.256    0.000 11606.256    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               40768491  286.312    0.000 9669.830    0.000 container.py:115(forward)
                2620120   72.764    0.000 8724.360    0.003 environments.py:83(step)
                2516171   92.619    0.000 7196.101    0.003 agent.py:82(<listcomp>)
               50323420  132.467    0.000 6880.807    0.000 exploration.py:34(epsilonGreedy)
                7545516   39.996    0.000 6587.374    0.001 grad_mode.py:12(decorate_context)
                2516171   89.551    0.000 6555.790    0.003 agent.py:58(rememberMulti)
                7545516 1654.184    0.000 6494.775    0.001 adam.py:51(step)
                2516171  203.483    0.000 6093.403    0.002 agent.py:62(<listcomp>)
                7545516   33.975    0.000 5576.577    0.001 tensor.py:155(backward)
                2620120   58.094    0.000 5566.999    0.002 environments.py:85(<listcomp>)
                7545516   39.816    0.000 5542.602    0.001 __init__.py:57(backward)
               52549457 1477.793    0.000 5526.708    0.000 helpers.py:8(clean)
                7545516 5338.791    0.001 5338.791    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               60094973 4616.496    0.000 4616.496    0.000 {built-in method as_tensor}
               45902784   78.728    0.000 3590.714    0.000 conv.py:418(forward)
               45902784   95.709    0.000 3473.208    0.000 conv.py:410(_conv_forward)
               45902784 3360.804    0.000 3360.804    0.000 {built-in method conv2d}
               61101761  120.349    0.000 2932.291    0.000 linear.py:90(forward)
                2620120   53.543    0.000 2906.510    0.001 environments.py:84(<listcomp>)
               52402400  193.456    0.000 2852.966    0.000 interop.py:274(step)
               61101761  323.065    0.000 2749.911    0.000 functional.py:1655(linear)
                7650470  389.106    0.000 2161.902    0.000 rnn.py:109(flatten_parameters)
                7650464   94.102    0.000 1906.297    0.000 rnn.py:550(forward)
                7650464 1707.906    0.000 1707.906    0.000 {built-in method lstm}
               53553248 1608.384    0.000 1608.384    0.000 {built-in method addmm}
               96837910   81.828    0.000 1513.576    0.000 activation.py:653(forward)
               96837910  138.013    0.000 1431.748    0.000 functional.py:1277(leaky_relu)
                7650467 1286.147    0.000 1286.147    0.000 {built-in method _cudnn_rnn_flatten_weight}
               96837910 1280.641    0.000 1280.641    0.000 {built-in method torch._C._nn.leaky_relu}
               52402400   24.086    0.000 1246.098    0.000 wrapper.py:25(act)
               52402400   64.137    0.000 1222.012    0.000 env.py:197(act)
              150910320 1196.606    0.000 1196.606    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52402400 1118.845    0.000 1123.801    0.000 libenv.py:352(act)
              150910320 1058.225    0.000 1058.225    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              104951857   78.344    0.000  862.739    0.000 extract_dict_ob.py:9(observe)
              104951857   44.648    0.000  784.396    0.000 wrapper.py:19(observe)
               75455160  751.960    0.000  751.960    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              104951857  197.242    0.000  739.748    0.000 libenv.py:344(observe)
                   2620    1.010    0.000  627.720    0.240 agent.py:157(update_target_network)
                7545516  104.844    0.000  616.033    0.000 optimizer.py:166(zero_grad)
               75455160  613.598    0.000  613.598    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2516171    6.020    0.000  556.910    0.000 agent.py:249(avoid_similar_state)
              157354257  161.349    0.000  541.782    0.000 libenv.py:281(_maybe_copy_dict)
               75455160  506.538    0.000  506.538    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75455160  493.840    0.000  493.840    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              472065391  464.645    0.000  464.645    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7545516   14.873    0.000  442.275    0.000 loss.py:444(forward)
                7545516   60.973    0.000  427.401    0.000 functional.py:2621(mse_loss)
               35634035  386.752    0.000  413.573    0.000 module.py:774(__setattr__)
              389814683  406.667    0.000  406.667    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               52402400   44.243    0.000  390.698    0.000 wrapper.py:22(get_info)
               11540531  147.515    0.000  383.778    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               61101761  381.275    0.000  381.275    0.000 {method 't' of 'torch._C._TensorBase' objects}
               50323420  366.429    0.000  366.429    0.000 memory.py:17(inner)
               75455160  349.304    0.000  349.304    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2515172  268.739    0.000  349.075    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               52402400  180.399    0.000  346.455    0.000 libenv.py:363(get_info)
                   2620   95.227    0.036  341.317    0.130 memory.py:45(update_distribution)
               54922812  333.374    0.000  333.374    0.000 {built-in method numpy.array}
               15091032  302.581    0.000  302.581    0.000 {built-in method gather}
               25596374   24.678    0.000  281.632    0.000 <__array_function__ internals>:2(prod)
                2516171  214.139    0.000  279.206    0.000 agent.py:149(convert_values)
               58268748  265.475    0.000  265.475    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   5240  232.928    0.044  260.007    0.050 {built-in method _pickle.loads}
              377275908  220.209    0.000  257.289    0.000 tensor.py:725(grad)
               25596414   19.513    0.000  252.877    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7860360   14.602    0.000  241.329    0.000 functional.py:68(split)
                7650464   18.852    0.000  237.055    0.000 pooling.py:156(forward)
                7545516  236.508    0.000  236.508    0.000 {built-in method torch._C._nn.mse_loss}
               25596374   31.636    0.000  233.364    0.000 fromnumeric.py:2881(prod)
               52402400  230.577    0.000  230.577    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7860360   13.757    0.000  225.614    0.000 tensor.py:367(split)
                2715289  222.996    0.000  222.996    0.000 {built-in method tensor}
               30601868  193.653    0.000  218.682    0.000 __init__.py:66(is_acceptable)
                7650464   13.912    0.000  218.202    0.000 _jit_internal.py:237(fn)
                7860360  210.243    0.000  210.243    0.000 {function Tensor.split at 0x7f90f6dda9d0}
                7650464   16.064    0.000  202.898    0.000 functional.py:564(_max_pool2d)
               25596374   61.000    0.000  201.727    0.000 fromnumeric.py:70(_wrapreduction)
                2515172  197.326    0.000  197.326    0.000 memory.py:43(<listcomp>)
                7548513  195.112    0.000  195.112    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
              270288737  189.146    0.000  189.264    0.000 module.py:758(__getattr__)
                7650464  185.819    0.000  185.819    0.000 {built-in method max_pool2d}
                2620120   27.521    0.000  178.087    0.000 environments.py:86(<listcomp>)
               15092031  171.310    0.000  171.310    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                2620120   18.353    0.000  171.165    0.000 collector.py:8(collect)
                7545516   41.247    0.000  161.383    0.000 __init__.py:25(_make_grads)
               61101761   43.090    0.000  157.890    0.000 _overrides.py:779(has_torch_function)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8557620: <BIGFISH_U_S_0.1_0returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0.1_0returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:46 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Dec 11 16:01:47 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 11 16:01:47 2020
Terminated at Sat Dec 12 14:57:34 2020
Results reported at Sat Dec 12 14:57:34 2020

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

    CPU time :                                   86525.00 sec.
    Max Memory :                                 54095 MB
    Average Memory :                             53435.42 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7345.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82661 sec.
    Turnaround time :                            82548 sec.

The output (if any) is above this job summary.

