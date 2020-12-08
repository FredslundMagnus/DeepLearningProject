[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Uncertainty0state_difference0.1chaser-0
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
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      9939360974 function calls (9709690443 primitive calls) in 82515.38 seconds

##    Ordered by: cumulative time
   List reduced from 1331 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82515.381 82515.381 {built-in method builtins.exec}
                      1    0.057    0.057 82515.381 82515.381 <string>:1(<module>)
                      1  493.094  493.094 82515.322 82515.322 main.py:92(main)
                2274217  194.386    0.000 54504.385    0.024 agent.py:86(learn)
                2273717  823.932    0.000 53371.089    0.023 agent.py:96(TD_learn)
                2273717  155.946    0.000 24485.560    0.011 memory.py:35(sample_distribution)
                2273717  264.066    0.000 23706.874    0.010 helpers.py:15(stack)
        245580936/15917019 1108.447    0.000 16262.455    0.001 module.py:710(_call_impl)
                6821651  224.500    0.000 14991.297    0.002 agent.py:212(forward)
               22739278 12129.896    0.001 12129.901    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20464953 11155.825    0.001 11155.825    0.001 {built-in method cat}
               36382472  313.519    0.000 10596.186    0.000 container.py:115(forward)
                2274217  224.078    0.000 9962.357    0.004 agent.py:74(chooseMulti)
                2274217   66.447    0.000 9726.805    0.004 environments.py:83(step)
                6821151   41.840    0.000 9100.625    0.001 grad_mode.py:12(decorate_context)
                6821151 2141.960    0.000 9007.196    0.001 adam.py:51(step)
              307158399 7943.103    0.000 7943.103    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2274217  109.700    0.000 7629.756    0.003 agent.py:62(rememberMulti)
                2274217  325.160    0.000 7097.459    0.003 agent.py:66(<listcomp>)
                6821151   32.063    0.000 6555.318    0.001 tensor.py:155(backward)
                6821151   35.622    0.000 6523.255    0.001 __init__.py:57(backward)
                6821151 6312.900    0.001 6312.900    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2274217   67.006    0.000 6076.433    0.003 environments.py:85(<listcomp>)
               45770900 1546.715    0.000 6053.698    0.000 helpers.py:8(clean)
               52592051 5023.976    0.000 5023.976    0.000 {built-in method as_tensor}
               40929906   82.227    0.000 3856.924    0.000 conv.py:418(forward)
               40929906   83.558    0.000 3739.262    0.000 conv.py:410(_conv_forward)
               40929906 3639.137    0.000 3639.137    0.000 {built-in method conv2d}
                2274217   53.883    0.000 3312.579    0.001 environments.py:84(<listcomp>)
               54574208  126.156    0.000 3291.552    0.000 linear.py:90(forward)
               45484340  204.118    0.000 3258.695    0.000 interop.py:274(step)
               54574208  338.782    0.000 3105.684    0.000 functional.py:1655(linear)
                2274217  113.095    0.000 3084.111    0.001 agent.py:84(<listcomp>)
               45484340  165.232    0.000 2660.793    0.000 exploration.py:34(epsilonGreedy)
                6821657  375.811    0.000 2412.981    0.000 rnn.py:109(flatten_parameters)
               47751557 1844.669    0.000 1844.669    0.000 {built-in method addmm}
              136423020 1817.456    0.000 1817.456    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               86408246   80.945    0.000 1773.759    0.000 activation.py:653(forward)
                6821651   82.356    0.000 1772.644    0.000 rnn.py:550(forward)
               86408246  120.836    0.000 1692.814    0.000 functional.py:1277(leaky_relu)
               45484340   22.979    0.000 1644.284    0.000 wrapper.py:25(act)
               45484340   75.892    0.000 1621.304    0.000 env.py:197(act)
                6821654 1597.354    0.000 1597.354    0.000 {built-in method _cudnn_rnn_flatten_weight}
                6821651 1595.676    0.000 1595.676    0.000 {built-in method lstm}
              136423020 1589.581    0.000 1589.581    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               86408246 1560.284    0.000 1560.284    0.000 {built-in method torch._C._nn.leaky_relu}
               45484340 1494.458    0.000 1499.140    0.000 libenv.py:352(act)
               68211510  991.416    0.000  991.416    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   4548    1.637    0.000  938.911    0.206 agent.py:139(update_target_network)
                6821151  144.246    0.000  907.894    0.000 optimizer.py:166(zero_grad)
               91255240   78.354    0.000  864.403    0.000 extract_dict_ob.py:9(observe)
               68211510  830.409    0.000  830.409    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               91255240   39.645    0.000  786.049    0.000 wrapper.py:19(observe)
               91255240  195.642    0.000  746.405    0.000 libenv.py:344(observe)
               68211510  709.763    0.000  709.763    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               68211510  695.465    0.000  695.465    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2274217    6.415    0.000  653.792    0.000 agent.py:230(avoid_similar_state)
              340692575  629.463    0.000  629.463    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                   4548  163.016    0.036  606.886    0.133 memory.py:45(update_distribution)
               68211510  553.543    0.000  553.543    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               47767153  537.164    0.000  537.164    0.000 {built-in method numpy.array}
              136739580  153.474    0.000  527.979    0.000 libenv.py:281(_maybe_copy_dict)
              410223288  477.358    0.000  477.358    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6821151   14.106    0.000  475.029    0.000 loss.py:444(forward)
               54574208  463.533    0.000  463.533    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6821151   55.258    0.000  460.923    0.000 functional.py:2621(mse_loss)
               11300210  162.984    0.000  414.735    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               45484340   43.918    0.000  385.417    0.000 wrapper.py:22(get_info)
               45484340  350.038    0.000  350.038    0.000 memory.py:17(inner)
                2273717  266.254    0.000  345.723    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               31835873  319.283    0.000  344.239    0.000 module.py:774(__setattr__)
               45484340  179.949    0.000  341.499    0.000 libenv.py:363(get_info)
               45484340  310.223    0.000  310.223    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2274217  289.825    0.000  309.878    0.000 agent.py:131(convert_values)
               24874277   25.404    0.000  295.491    0.000 <__array_function__ internals>:2(prod)
              341057658  253.653    0.000  290.334    0.000 tensor.py:725(grad)
                   9096  226.754    0.025  279.407    0.031 {built-in method _pickle.loads}
               40928906  278.734    0.000  278.734    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6821151  276.647    0.000  276.647    0.000 {built-in method torch._C._nn.mse_loss}
                2274217   28.537    0.000  271.347    0.000 environments.py:86(<listcomp>)
               24874317   19.655    0.000  265.393    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                9094868  253.219    0.000  253.219    0.000 {built-in method gather}
                6821651   15.610    0.000  251.206    0.000 pooling.py:156(forward)
               24874277   32.492    0.000  245.737    0.000 fromnumeric.py:2881(prod)
                6822651   12.970    0.000  243.118    0.000 functional.py:68(split)
               45484360   39.713    0.000  242.815    0.000 environments.py:89(reset)
                2619863  241.663    0.000  241.663    0.000 {built-in method tensor}
                6821651   12.365    0.000  235.596    0.000 _jit_internal.py:237(fn)
                6822651  233.455    0.000  233.455    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6822651   13.235    0.000  229.200    0.000 tensor.py:367(split)
                6821651   13.932    0.000  222.021    0.000 functional.py:564(_max_pool2d)
                6822651  214.244    0.000  214.244    0.000 {function Tensor.split at 0x7f93630079d0}
               24874277   58.909    0.000  213.245    0.000 fromnumeric.py:70(_wrapreduction)
               27286616  191.589    0.000  212.264    0.000 __init__.py:66(is_acceptable)
                6821651  207.121    0.000  207.121    0.000 {built-in method max_pool2d}
              245580936  195.997    0.000  195.997    0.000 {built-in method torch._C._get_tracing_state}
                2273717  181.683    0.000  181.683    0.000 memory.py:43(<listcomp>)
              241398470  181.320    0.000  181.515    0.000 module.py:758(__getattr__)
                2274217   17.099    0.000  179.337    0.000 collector.py:7(collect)
                6821151   35.303    0.000  172.044    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 8483321: <Uncertainty0state_difference0.1chaser_0> in cluster <dcc> Done

Job <Uncertainty0state_difference0.1chaser_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Sat Dec  5 16:31:57 2020
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Dec  6 03:42:30 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec  6 03:42:30 2020
Terminated at Mon Dec  7 02:37:50 2020
Results reported at Mon Dec  7 02:37:50 2020

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

    CPU time :                                   84560.00 sec.
    Max Memory :                                 54425 MB
    Average Memory :                             53730.86 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7015.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82520 sec.
    Turnaround time :                            122753 sec.

The output (if any) is above this job summary.

