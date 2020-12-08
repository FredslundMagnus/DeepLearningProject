
    Name :                      Eps_state_transition0.25maze-0
    Discount :                  0.995
    Environment :               maze
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.25
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11917434752 function calls (11702013658 primitive calls) in 82523.59 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82523.593 82523.593 {built-in method builtins.exec}
                      1    0.186    0.186 82523.593 82523.593 <string>:1(<module>)
                      1  571.867  571.867 82523.402 82523.402 main.py:92(main)
                2133134  217.405    0.000 57153.329    0.027 agent.py:86(learn)
                2132634  578.411    0.000 55957.382    0.026 agent.py:96(TD_learn)
                2132634  160.973    0.000 33819.197    0.016 memory.py:35(sample_distribution)
                2132634  307.790    0.000 33063.356    0.016 helpers.py:15(stack)
               19195206 19700.917    0.001 19700.917    0.001 {built-in method cat}
        228211338/12796804 1027.243    0.000 14296.464    0.001 module.py:715(_call_impl)
                6398402  218.172    0.000 13334.489    0.002 agent.py:212(forward)
               21328448 12654.649    0.001 12654.673    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               34125144  259.081    0.000 9176.696    0.000 container.py:115(forward)
                2133134  181.300    0.000 8884.133    0.004 agent.py:74(chooseMulti)
                2133134   63.713    0.000 8565.298    0.004 environments.py:83(step)
              287543139 7837.069    0.000 7837.069    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2133134   85.889    0.000 7170.553    0.003 agent.py:62(rememberMulti)
                2133134  220.693    0.000 6724.186    0.003 agent.py:66(<listcomp>)
                4265268   33.517    0.000 5698.688    0.001 grad_mode.py:23(decorate_context)
                4265268  214.746    0.000 5614.624    0.001 adam.py:55(step)
                2133134   62.190    0.000 5438.603    0.003 environments.py:85(<listcomp>)
               42782458 1373.070    0.000 5393.969    0.000 helpers.py:8(clean)
                4265268 1066.846    0.000 4618.880    0.001 functional.py:53(adam)
               49180360 4616.387    0.000 4616.387    0.000 {built-in method as_tensor}
                4265268   34.146    0.000 4448.553    0.001 tensor.py:181(backward)
                4265268   22.545    0.000 4414.407    0.001 __init__.py:68(backward)
                4265268 4282.662    0.001 4282.662    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               38390412   72.548    0.000 3392.483    0.000 conv.py:422(forward)
               38390412   88.627    0.000 3284.409    0.000 conv.py:414(_conv_forward)
               38390412 3180.229    0.000 3180.229    0.000 {built-in method conv2d}
                2133134   84.746    0.000 2904.869    0.001 agent.py:84(<listcomp>)
                2133134   48.825    0.000 2891.767    0.001 environments.py:84(<listcomp>)
               51188216  111.060    0.000 2869.321    0.000 linear.py:92(forward)
               42662680  170.965    0.000 2842.942    0.000 interop.py:274(step)
               51188216  278.760    0.000 2701.597    0.000 functional.py:1669(linear)
               42662680  122.857    0.000 2593.394    0.000 exploration.py:34(epsilonGreedy)
                6398408  388.081    0.000 2115.326    0.000 rnn.py:110(flatten_parameters)
                6398402   80.021    0.000 1816.158    0.000 rnn.py:555(forward)
                6398402 1641.836    0.000 1641.836    0.000 {built-in method lstm}
               44788814 1558.423    0.000 1558.423    0.000 {built-in method addmm}
               81047092   77.003    0.000 1442.122    0.000 activation.py:713(forward)
               42662680   22.480    0.000 1402.906    0.000 wrapper.py:25(act)
              358282620  824.958    0.000 1389.491    0.000 tensor.py:933(grad)
               42662680   55.714    0.000 1380.426    0.000 env.py:197(act)
               81047092  115.840    0.000 1365.119    0.000 functional.py:1292(leaky_relu)
               42662680 1289.379    0.000 1293.493    0.000 libenv.py:352(act)
                6398405 1248.006    0.000 1248.006    0.000 {built-in method _cudnn_rnn_flatten_weight}
               81047092 1237.937    0.000 1237.937    0.000 {built-in method torch._C._nn.leaky_relu}
                4265268  117.841    0.000 1205.367    0.000 optimizer.py:167(zero_grad)
                   4266    2.041    0.000  978.543    0.229 agent.py:139(update_target_network)
              102366432  939.824    0.000  939.824    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               85445138   65.303    0.000  788.426    0.000 extract_dict_ob.py:9(observe)
              102366432  776.450    0.000  776.450    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              460654268  260.630    0.000  759.831    0.000 overrides.py:1073(has_torch_function)
               85445138   40.368    0.000  723.123    0.000 wrapper.py:19(observe)
               85445138  182.279    0.000  682.755    0.000 libenv.py:344(observe)
                   4266  162.948    0.038  623.371    0.146 memory.py:45(update_distribution)
                2133134    6.351    0.000  552.106    0.000 agent.py:230(avoid_similar_state)
               44803846  532.362    0.000  532.362    0.000 {built-in method numpy.array}
               51183216  510.748    0.000  510.748    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              128107818  141.414    0.000  499.431    0.000 libenv.py:281(_maybe_copy_dict)
               51183216  484.965    0.000  484.965    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              520373044  194.588    0.000  482.349    0.000 {built-in method builtins.any}
               42662680  442.486    0.000  442.486    0.000 memory.py:17(inner)
               51183216  436.658    0.000  436.658    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              384327720  435.516    0.000  435.516    0.000 {method 'copy' of 'numpy.ndarray' objects}
               51188216  419.397    0.000  419.397    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6399402   13.525    0.000  411.266    0.000 functional.py:74(split)
               29860711  378.123    0.000  401.744    0.000 module.py:781(__setattr__)
                6399402   28.751    0.000  396.798    0.000 tensor.py:460(split)
               51183216  385.002    0.000  385.002    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11159617  138.251    0.000  371.007    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6399402  366.520    0.000  366.520    0.000 {function Tensor.split at 0x7fd2136ffca0}
              317162000  361.812    0.000  361.812    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               42662680   38.687    0.000  342.421    0.000 wrapper.py:22(get_info)
                2132634  238.010    0.000  309.885    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               42662680  157.198    0.000  303.735    0.000 libenv.py:363(get_info)
                   8532  248.941    0.029  298.077    0.035 {built-in method _pickle.loads}
                4265268    9.947    0.000  290.838    0.000 loss.py:445(forward)
              972496752  226.450    0.000  284.063    0.000 overrides.py:1086(<genexpr>)
                4265268   35.473    0.000  280.891    0.000 functional.py:2637(mse_loss)
               51183216  276.001    0.000  276.001    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24452008   24.304    0.000  273.446    0.000 <__array_function__ internals>:2(prod)
               24452048   18.986    0.000  244.827    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                2133134  215.584    0.000  237.348    0.000 agent.py:131(convert_values)
                6398402   18.863    0.000  234.069    0.000 pooling.py:152(forward)
               42662680  226.729    0.000  226.729    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24452008   30.961    0.000  225.840    0.000 fromnumeric.py:2881(prod)
               38389412  219.631    0.000  219.631    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6398402   11.478    0.000  215.206    0.000 _jit_internal.py:257(fn)
                6399402  205.280    0.000  205.280    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2457348  203.080    0.000  203.080    0.000 {built-in method tensor}
                6398402   12.654    0.000  202.592    0.000 functional.py:574(_max_pool2d)
               25593620  179.479    0.000  199.254    0.000 __init__.py:67(is_acceptable)
               24452008   57.705    0.000  194.880    0.000 fromnumeric.py:70(_wrapreduction)
                6398402  189.029    0.000  189.029    0.000 {built-in method max_pool2d}
                2132634  188.381    0.000  188.381    0.000 memory.py:43(<listcomp>)
              226421111  172.198    0.000  172.397    0.000 module.py:765(__getattr__)
                2133134   24.445    0.000  171.215    0.000 environments.py:86(<listcomp>)
                4265268  169.853    0.000  169.853    0.000 {built-in method torch._C._nn.mse_loss}
                6397902  164.870    0.000  164.870    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8482842: <Eps_state_transition0.25maze_0> in cluster <dcc> Done

Job <Eps_state_transition0.25maze_0> was submitted from host <n-62-27-19> by user <s183914> in cluster <dcc> at Sat Dec  5 00:10:44 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec  5 02:21:29 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec  5 02:21:29 2020
Terminated at Sun Dec  6 01:17:02 2020
Results reported at Sun Dec  6 01:17:02 2020

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

    CPU time :                                   90466.00 sec.
    Max Memory :                                 54872 MB
    Average Memory :                             54188.60 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6568.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82535 sec.
    Turnaround time :                            90378 sec.

The output (if any) is above this job summary.

