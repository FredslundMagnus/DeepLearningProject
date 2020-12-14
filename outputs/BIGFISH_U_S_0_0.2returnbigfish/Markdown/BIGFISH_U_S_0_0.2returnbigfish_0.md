[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0_0.2returnbigfish-0
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.2
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      10378320028 function calls (10139344695 primitive calls) in 82523.99 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82523.989 82523.989 {built-in method builtins.exec}
                      1    0.037    0.037 82523.988 82523.988 <string>:1(<module>)
                      1  524.893  524.893 82523.951 82523.951 main.py:92(main)
                2432212  253.727    0.000 54760.502    0.023 agent.py:84(learn)
                2335260  931.235    0.000 53935.861    0.023 agent.py:99(TD_learn)
                2335260  163.864    0.000 25259.639    0.011 memory.py:35(sample_distribution)
                2335260  290.462    0.000 24477.251    0.010 helpers.py:15(stack)
        255413490/16444771 1101.802    0.000 16215.697    0.001 module.py:710(_call_impl)
                7102732  222.335    0.000 14985.848    0.002 agent.py:231(forward)
               23644563 12822.584    0.001 12822.632    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               21308196 11173.784    0.001 11173.784    0.001 {built-in method cat}
                2432212  217.617    0.000 10835.155    0.004 agent.py:70(chooseMulti)
               37849919  308.065    0.000 10437.487    0.000 container.py:115(forward)
              317704167 8864.932    0.000 8864.932    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2432212   68.079    0.000 8806.085    0.004 environments.py:83(step)
                7005780   39.767    0.000 8565.620    0.001 grad_mode.py:12(decorate_context)
                7005780 2035.892    0.000 8475.510    0.001 adam.py:51(step)
                2336259   98.171    0.000 7403.486    0.003 agent.py:58(rememberMulti)
                2336259  304.347    0.000 6937.877    0.003 agent.py:62(<listcomp>)
                7005780   30.381    0.000 6359.284    0.001 tensor.py:155(backward)
                7005780   36.205    0.000 6328.904    0.001 __init__.py:57(backward)
                7005780 6119.267    0.001 6119.267    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2432212   66.993    0.000 5608.266    0.002 environments.py:85(<listcomp>)
               48996417 1371.523    0.000 5587.743    0.000 helpers.py:8(clean)
               56002197 4777.444    0.000 4777.444    0.000 {built-in method as_tensor}
                2336259  104.797    0.000 4014.957    0.002 agent.py:82(<listcomp>)
               42616392   76.143    0.000 3868.783    0.000 conv.py:418(forward)
               42616392   88.386    0.000 3756.349    0.000 conv.py:410(_conv_forward)
               42616392 3652.953    0.000 3652.953    0.000 {built-in method conv2d}
               46725180  153.756    0.000 3630.336    0.000 exploration.py:34(epsilonGreedy)
               56727901  118.582    0.000 3215.433    0.000 linear.py:90(forward)
               56727901  321.774    0.000 3040.144    0.000 functional.py:1655(linear)
                2432212   52.297    0.000 2891.430    0.001 environments.py:84(<listcomp>)
               48644240  197.153    0.000 2839.133    0.000 interop.py:274(step)
                7102738  376.292    0.000 2417.859    0.000 rnn.py:109(flatten_parameters)
                7102732   85.621    0.000 1887.999    0.000 rnn.py:550(forward)
               49719124 1817.498    0.000 1817.498    0.000 {built-in method addmm}
               89905302   75.454    0.000 1714.526    0.000 activation.py:653(forward)
                7102732 1701.738    0.000 1701.738    0.000 {built-in method lstm}
              140115600 1689.018    0.000 1689.018    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               89905302  115.568    0.000 1639.072    0.000 functional.py:1277(leaky_relu)
                7102735 1573.757    0.000 1573.757    0.000 {built-in method _cudnn_rnn_flatten_weight}
               89905302 1512.269    0.000 1512.269    0.000 {built-in method torch._C._nn.leaky_relu}
              140115600 1479.907    0.000 1479.907    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               48644240   21.587    0.000 1251.276    0.000 wrapper.py:25(act)
               48644240   71.644    0.000 1229.689    0.000 env.py:197(act)
               48644240 1110.880    0.000 1116.019    0.000 libenv.py:352(act)
               70057800  924.838    0.000  924.838    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                7005780  142.992    0.000  867.716    0.000 optimizer.py:166(zero_grad)
               97640657   77.938    0.000  852.841    0.000 extract_dict_ob.py:9(observe)
               70057800  780.732    0.000  780.732    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               97640657   40.054    0.000  774.903    0.000 wrapper.py:19(observe)
               97640657  190.463    0.000  734.849    0.000 libenv.py:344(observe)
               70057800  673.149    0.000  673.149    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               70057800  660.957    0.000  660.957    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2336259    6.188    0.000  612.911    0.000 agent.py:249(avoid_similar_state)
              360828250  578.791    0.000  578.791    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                   2432    0.936    0.000  570.915    0.235 agent.py:157(update_target_network)
              146284897  155.358    0.000  531.374    0.000 libenv.py:281(_maybe_copy_dict)
               70057800  520.426    0.000  520.426    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              438857123  473.726    0.000  473.726    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7005780   14.870    0.000  464.307    0.000 loss.py:444(forward)
               56727901  459.979    0.000  459.979    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7005780   56.673    0.000  449.437    0.000 functional.py:2621(mse_loss)
               11361383  160.418    0.000  404.813    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               33083283  361.172    0.000  388.916    0.000 module.py:774(__setattr__)
               48644240   43.582    0.000  387.710    0.000 wrapper.py:22(get_info)
               46725180  365.887    0.000  365.887    0.000 memory.py:17(inner)
               14011560  345.482    0.000  345.482    0.000 {built-in method gather}
               48644240  181.312    0.000  344.128    0.000 libenv.py:363(get_info)
                2335260  260.857    0.000  341.092    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               54098788  315.593    0.000  315.593    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               50984364  308.205    0.000  308.205    0.000 {built-in method numpy.array}
                   2432   86.524    0.036  305.805    0.126 memory.py:45(update_distribution)
                2336259  269.618    0.000  300.580    0.000 agent.py:149(convert_values)
               48644240  290.256    0.000  290.256    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
              350289108  247.809    0.000  288.894    0.000 tensor.py:725(grad)
               25058166   24.367    0.000  288.561    0.000 <__array_function__ internals>:2(prod)
                7005780  266.200    0.000  266.200    0.000 {built-in method torch._C._nn.mse_loss}
               25058206   18.786    0.000  260.048    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7102732   18.560    0.000  254.105    0.000 pooling.py:156(forward)
               25058166   31.181    0.000  241.261    0.000 fromnumeric.py:2881(prod)
                   4864  213.332    0.044  240.042    0.049 {built-in method _pickle.loads}
                2432212   27.935    0.000  238.310    0.000 environments.py:86(<listcomp>)
                7296636   12.859    0.000  235.817    0.000 functional.py:68(split)
                7102732   12.174    0.000  235.545    0.000 _jit_internal.py:237(fn)
                7102732   13.754    0.000  222.199    0.000 functional.py:564(_max_pool2d)
                7296636   12.796    0.000  221.994    0.000 tensor.py:367(split)
                7008777  220.293    0.000  220.293    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               28410940  193.710    0.000  215.172    0.000 __init__.py:66(is_acceptable)
               48644260   33.422    0.000  210.409    0.000 environments.py:89(reset)
               25058166   57.009    0.000  210.080    0.000 fromnumeric.py:70(_wrapreduction)
                7296636  207.600    0.000  207.600    0.000 {function Tensor.split at 0x7ff9fde0f9d0}
                7102732  207.524    0.000  207.524    0.000 {built-in method max_pool2d}
                2521089  204.744    0.000  204.744    0.000 {built-in method tensor}
               14012559  200.185    0.000  200.185    0.000 {method 'type' of 'torch._C._TensorBase' objects}
              255413490  186.258    0.000  186.258    0.000 {built-in method torch._C._get_tracing_state}
                2335260  183.824    0.000  183.824    0.000 memory.py:43(<listcomp>)
              250939157  179.022    0.000  179.123    0.000 module.py:758(__getattr__)
                7005780   36.293    0.000  170.864    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8557623: <BIGFISH_U_S_0_0.2returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0_0.2returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:46 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Dec 13 00:41:11 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec 13 00:41:11 2020
Terminated at Sun Dec 13 23:36:44 2020
Results reported at Sun Dec 13 23:36:44 2020

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

    CPU time :                                   85121.00 sec.
    Max Memory :                                 54114 MB
    Average Memory :                             53453.30 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7326.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82622 sec.
    Turnaround time :                            200098 sec.

The output (if any) is above this job summary.

