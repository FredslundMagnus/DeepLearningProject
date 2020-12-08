
    Name :                      Uncertainty0.1state_difference0softepsdodgeball-0
    Discount :                  0.995
    Environment :               dodgeball
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsintosoftmax
    Hidden size :               40
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      15587509283 function calls (15345149005 primitive calls) in 82515.44 seconds

##    Ordered by: cumulative time
   List reduced from 1358 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82515.437 82515.437 {built-in method builtins.exec}
                      1    0.044    0.044 82515.437 82515.437 <string>:1(<module>)
                      1  435.212  435.212 82515.392 82515.392 main.py:92(main)
                2399858  178.314    0.000 50378.323    0.021 agent.py:86(learn)
                2399358  654.026    0.000 49368.960    0.021 agent.py:96(TD_learn)
                2399358  133.832    0.000 24300.464    0.010 memory.py:35(sample_distribution)
                2399358  209.348    0.000 23636.072    0.010 helpers.py:15(stack)
                2399858  176.770    0.000 15771.011    0.007 agent.py:74(chooseMulti)
        259150164/16796506 1025.635    0.000 13897.695    0.001 module.py:715(_call_impl)
                7198574  204.668    0.000 12819.671    0.002 agent.py:212(forward)
               23995688 12461.813    0.001 12461.869    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               21595722 10760.863    0.000 10760.863    0.000 {built-in method cat}
              324627325 10115.426    0.000 10115.426    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2399858  132.942    0.000 9806.898    0.004 agent.py:84(<listcomp>)
               47997160 1254.021    0.000 9316.587    0.000 exploration.py:40(epsintosoftmax)
                2399858   63.531    0.000 9235.736    0.004 environments.py:83(step)
               38392728  259.356    0.000 9087.219    0.000 container.py:115(forward)
                7198074   45.640    0.000 7626.545    0.001 grad_mode.py:23(decorate_context)
                7198074  279.690    0.000 7505.434    0.001 adam.py:55(step)
                2399858   90.192    0.000 6508.384    0.003 agent.py:62(rememberMulti)
                7198074 1392.230    0.000 6164.014    0.001 functional.py:53(adam)
                2399858  225.298    0.000 6068.973    0.003 agent.py:66(<listcomp>)
               49297686 1487.604    0.000 5852.685    0.000 helpers.py:8(clean)
                2399858   67.855    0.000 5743.138    0.002 environments.py:85(<listcomp>)
                7198074   43.298    0.000 5326.384    0.001 tensor.py:181(backward)
                7198074   27.369    0.000 5283.086    0.001 __init__.py:68(backward)
                7198074 5100.842    0.001 5100.842    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               56495760 4757.995    0.000 4757.995    0.000 {built-in method as_tensor}
               43191444   76.641    0.000 3329.086    0.000 conv.py:422(forward)
               43191444   80.914    0.000 3220.555    0.000 conv.py:414(_conv_forward)
               43191444 3124.578    0.000 3124.578    0.000 {built-in method conv2d}
                2399858   50.044    0.000 3019.100    0.001 environments.py:84(<listcomp>)
               47997160  179.377    0.000 2969.056    0.000 interop.py:274(step)
               57589592  120.826    0.000 2843.452    0.000 linear.py:92(forward)
               57589592  295.540    0.000 2666.283    0.000 functional.py:1669(linear)
               47997160 1669.629    0.000 2492.858    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7198580  346.286    0.000 1926.220    0.000 rnn.py:110(flatten_parameters)
              503865288 1130.118    0.000 1908.674    0.000 tensor.py:933(grad)
                7198074  165.512    0.000 1662.408    0.000 optimizer.py:167(zero_grad)
                7198574   75.476    0.000 1607.204    0.000 rnn.py:555(forward)
               50390018 1539.928    0.000 1539.928    0.000 {built-in method addmm}
               47997160   22.443    0.000 1531.429    0.000 wrapper.py:25(act)
               47997160   62.386    0.000 1508.986    0.000 env.py:197(act)
               91182604   78.584    0.000 1450.138    0.000 activation.py:713(forward)
                7198574 1446.925    0.000 1446.925    0.000 {built-in method lstm}
               47997160 1410.217    0.000 1414.736    0.000 libenv.py:352(act)
               91182604  120.347    0.000 1371.554    0.000 functional.py:1292(leaky_relu)
              143961480 1254.077    0.000 1254.077    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               91182604 1239.925    0.000 1239.925    0.000 {built-in method torch._C._nn.leaky_relu}
                7198577 1184.232    0.000 1184.232    0.000 {built-in method _cudnn_rnn_flatten_weight}
              143961480 1057.775    0.000 1057.775    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              633435866  336.350    0.000  987.341    0.000 overrides.py:1073(has_torch_function)
                   4799    1.602    0.000  831.049    0.173 agent.py:139(update_target_network)
               97294846   78.976    0.000  804.692    0.000 extract_dict_ob.py:9(observe)
               97294846   41.851    0.000  725.717    0.000 wrapper.py:19(observe)
               71980740  691.158    0.000  691.158    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               97294846  179.673    0.000  683.866    0.000 libenv.py:344(observe)
               36572368   66.833    0.000  649.330    0.000 functional.py:1479(softmax)
               71980740  644.067    0.000  644.067    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               61821450   62.162    0.000  623.887    0.000 <__array_function__ internals>:2(prod)
              705421630  260.103    0.000  621.773    0.000 {built-in method builtins.any}
               71980740  585.377    0.000  585.377    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               36572368  576.952    0.000  576.952    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2399858    6.418    0.000  554.424    0.000 agent.py:230(avoid_similar_state)
               61821490   51.248    0.000  550.311    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               71980740  517.227    0.000  517.227    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   4799  143.414    0.030  501.957    0.105 memory.py:45(update_distribution)
               61821450   73.224    0.000  499.063    0.000 fromnumeric.py:2881(prod)
              145292006  144.903    0.000  492.872    0.000 libenv.py:281(_maybe_copy_dict)
               50406116  431.597    0.000  431.597    0.000 {built-in method numpy.array}
              435880817  428.612    0.000  428.612    0.000 {method 'copy' of 'numpy.ndarray' objects}
               61821450  143.614    0.000  425.840    0.000 fromnumeric.py:70(_wrapreduction)
                2399858   27.780    0.000  409.967    0.000 environments.py:86(<listcomp>)
                7199574   13.058    0.000  404.779    0.000 functional.py:74(split)
                7198074   11.609    0.000  398.387    0.000 loss.py:445(forward)
                7199574   30.268    0.000  390.821    0.000 tensor.py:460(split)
               57589592  387.594    0.000  387.594    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7198074   45.771    0.000  386.777    0.000 functional.py:2637(mse_loss)
               47997180   39.020    0.000  382.194    0.000 environments.py:89(reset)
               71980740  380.602    0.000  380.602    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7199574  359.013    0.000  359.013    0.000 {function Tensor.split at 0x7fddf9289ca0}
               47997160  357.369    0.000  357.369    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
             1324461324  287.722    0.000  356.363    0.000 overrides.py:1086(<genexpr>)
              358018184  353.864    0.000  353.864    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               47997160   38.472    0.000  348.886    0.000 wrapper.py:22(get_info)
               47997160  164.625    0.000  310.413    0.000 libenv.py:363(get_info)
               33594847  282.803    0.000  305.672    0.000 module.py:781(__setattr__)
               47997160  300.587    0.000  300.587    0.000 memory.py:17(inner)
                   9598  221.742    0.023  275.253    0.029 {built-in method _pickle.loads}
                2399358  213.454    0.000  271.409    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                2399858  217.837    0.000  265.649    0.000 agent.py:131(convert_values)
               64225607  244.764    0.000  244.764    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                7198074  229.252    0.000  229.252    0.000 {built-in method torch._C._nn.mse_loss}
                9597432  218.197    0.000  218.197    0.000 {built-in method gather}
                7198574   14.320    0.000  215.358    0.000 pooling.py:152(forward)
               43190444  212.418    0.000  212.418    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                7198574   11.160    0.000  201.038    0.000 _jit_internal.py:257(fn)
               71980986   86.865    0.000  196.010    0.000 tensor.py:596(__hash__)
                7199574  195.770    0.000  195.770    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                7198574   12.703    0.000  188.703    0.000 functional.py:574(_max_pool2d)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 8483547: <Uncertainty0.1state_difference0softepsdodgeball_0> in cluster <dcc> Done

Job <Uncertainty0.1state_difference0softepsdodgeball_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec  6 01:18:08 2020
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Dec  6 11:24:45 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec  6 11:24:45 2020
Terminated at Mon Dec  7 10:20:04 2020
Results reported at Mon Dec  7 10:20:04 2020

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

    CPU time :                                   85476.00 sec.
    Max Memory :                                 54813 MB
    Average Memory :                             54125.91 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6627.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82519 sec.
    Turnaround time :                            118916 sec.

The output (if any) is above this job summary.

