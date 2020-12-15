
    Name :                      CHASER_U_S_0_0.05returnchaser-0
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
    State difference weight :   0.05
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13908632570 function calls (13679060502 primitive calls) in 82514.85 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82514.853 82514.853 {built-in method builtins.exec}
                      1    0.026    0.026 82514.853 82514.853 <string>:1(<module>)
                      1  501.924  501.924 82514.824 82514.824 main.py:92(main)
                2336379  247.564    0.000 56375.109    0.024 agent.py:84(learn)
                2243425  965.586    0.000 55589.418    0.025 agent.py:99(TD_learn)
                2243425  155.558    0.000 24383.452    0.011 memory.py:35(sample_distribution)
                2243425  253.977    0.000 23626.048    0.011 helpers.py:15(stack)
        245363376/15797928 1077.398    0.000 16722.796    0.001 module.py:715(_call_impl)
                6823229  213.472    0.000 15465.709    0.002 agent.py:231(forward)
               22714219 12205.226    0.001 12205.250    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               36360569  302.528    0.000 10841.503    0.000 container.py:115(forward)
               20469687 10802.916    0.001 10802.916    0.001 {built-in method cat}
                6730275   43.708    0.000 9624.419    0.001 grad_mode.py:23(decorate_context)
                6730275  282.531    0.000 9508.093    0.001 adam.py:55(step)
                2336379   63.276    0.000 9202.676    0.004 environments.py:83(step)
                2336379  216.015    0.000 8904.433    0.004 agent.py:70(chooseMulti)
                6730275 1774.322    0.000 8198.597    0.001 functional.py:53(adam)
                2244424   98.084    0.000 7347.002    0.003 agent.py:58(rememberMulti)
                2244424  294.262    0.000 6860.916    0.003 agent.py:62(<listcomp>)
              304853913 6665.403    0.000 6665.403    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6730275   48.492    0.000 6455.688    0.001 tensor.py:181(backward)
                6730275   31.313    0.000 6407.197    0.001 __init__.py:68(backward)
                6730275 6192.770    0.001 6192.770    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2336379   68.138    0.000 5794.813    0.002 environments.py:85(<listcomp>)
               47048943 1353.017    0.000 5771.624    0.000 helpers.py:8(clean)
               53779218 4998.989    0.000 4998.989    0.000 {built-in method as_tensor}
               40939374   70.843    0.000 3991.595    0.000 conv.py:422(forward)
               40939374   84.197    0.000 3887.788    0.000 conv.py:414(_conv_forward)
               40939374 3789.073    0.000 3789.073    0.000 {built-in method conv2d}
               54495875  113.729    0.000 3430.639    0.000 linear.py:92(forward)
               54495875  325.934    0.000 3260.007    0.000 functional.py:1669(linear)
                2336379   49.135    0.000 3108.873    0.001 environments.py:84(<listcomp>)
               46727580  183.311    0.000 3059.738    0.000 interop.py:274(step)
                6823235  430.991    0.000 2652.361    0.000 rnn.py:110(flatten_parameters)
               47762603 1932.280    0.000 1932.280    0.000 {built-in method addmm}
              471119358 1203.761    0.000 1905.580    0.000 tensor.py:933(grad)
                2244424  107.669    0.000 1883.851    0.001 agent.py:82(<listcomp>)
                6730275  187.900    0.000 1860.064    0.000 optimizer.py:167(zero_grad)
               86367596   77.942    0.000 1803.017    0.000 activation.py:713(forward)
                6823229   78.845    0.000 1794.454    0.000 rnn.py:555(forward)
              134605500 1765.562    0.000 1765.562    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6823232 1725.953    0.000 1725.953    0.000 {built-in method _cudnn_rnn_flatten_weight}
               86367596  120.678    0.000 1725.074    0.000 functional.py:1292(leaky_relu)
                6823229 1623.275    0.000 1623.275    0.000 {built-in method lstm}
               86367596 1594.108    0.000 1594.108    0.000 {built-in method torch._C._nn.leaky_relu}
               46727580   21.299    0.000 1554.603    0.000 wrapper.py:25(act)
               46727580   67.193    0.000 1533.304    0.000 env.py:197(act)
               44888480  154.713    0.000 1470.546    0.000 exploration.py:34(epsilonGreedy)
              134605500 1454.873    0.000 1454.873    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               46727580 1418.640    0.000 1423.093    0.000 libenv.py:352(act)
              592918229  330.987    0.000  899.750    0.000 overrides.py:1073(has_torch_function)
               67302750  898.341    0.000  898.341    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67302750  827.917    0.000  827.917    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               93776523   73.805    0.000  813.348    0.000 extract_dict_ob.py:9(observe)
               67302750  763.486    0.000  763.486    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               93776523   38.889    0.000  739.543    0.000 wrapper.py:19(observe)
               93776523  182.558    0.000  700.653    0.000 libenv.py:344(observe)
               67302750  686.130    0.000  686.130    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2244424    6.297    0.000  648.873    0.000 agent.py:249(avoid_similar_state)
              660874678  226.242    0.000  546.901    0.000 {built-in method builtins.any}
              346306515  540.150    0.000  540.150    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                   2336    0.915    0.000  538.128    0.230 agent.py:157(update_target_network)
               54495875  525.365    0.000  525.365    0.000 {method 't' of 'torch._C._TensorBase' objects}
               67302750  522.884    0.000  522.884    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              140504103  145.718    0.000  500.081    0.000 libenv.py:281(_maybe_copy_dict)
                6730275   14.660    0.000  459.771    0.000 loss.py:445(forward)
              421514645  447.125    0.000  447.125    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6730275   46.964    0.000  445.111    0.000 functional.py:2637(mse_loss)
               11272014  167.512    0.000  418.442    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7009137   14.236    0.000  384.467    0.000 functional.py:74(split)
               31781601  356.667    0.000  381.872    0.000 module.py:781(__setattr__)
               13460550  374.259    0.000  374.259    0.000 {built-in method gather}
                7009137   30.562    0.000  369.327    0.000 tensor.py:460(split)
               46727580   40.625    0.000  361.058    0.000 wrapper.py:22(get_info)
                2243425  261.678    0.000  337.984    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                7009137  337.106    0.000  337.106    0.000 {function Tensor.split at 0x7f35fd231d30}
               51970591  331.811    0.000  331.811    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               44888480  321.325    0.000  321.325    0.000 memory.py:17(inner)
               46727580  170.818    0.000  320.433    0.000 libenv.py:363(get_info)
               46727580  316.847    0.000  316.847    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
             1240332333  251.662    0.000  315.816    0.000 overrides.py:1086(<genexpr>)
               24787593   24.109    0.000  292.959    0.000 <__array_function__ internals>:2(prod)
               48975677  291.513    0.000  291.513    0.000 {built-in method numpy.array}
                   2336   81.555    0.035  285.033    0.122 memory.py:45(update_distribution)
                2244424  279.581    0.000  284.990    0.000 agent.py:149(convert_values)
                6730275  283.025    0.000  283.025    0.000 {built-in method torch._C._nn.mse_loss}
                6823229   17.132    0.000  269.081    0.000 pooling.py:152(forward)
               24787633   18.882    0.000  264.826    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6823229   12.086    0.000  251.949    0.000 _jit_internal.py:257(fn)
               24787593   30.617    0.000  245.944    0.000 fromnumeric.py:2881(prod)
                6733272  240.942    0.000  240.942    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6823229   13.951    0.000  238.783    0.000 functional.py:574(_max_pool2d)
                2336379   29.173    0.000  235.715    0.000 environments.py:86(<listcomp>)
                   4672  201.139    0.043  227.947    0.049 {built-in method _pickle.loads}
                6823229  224.074    0.000  224.074    0.000 {built-in method max_pool2d}
               13461549  220.127    0.000  220.127    0.000 {method 'type' of 'torch._C._TensorBase' objects}
               24787593   56.184    0.000  215.327    0.000 fromnumeric.py:70(_wrapreduction)
               46727600   33.182    0.000  206.547    0.000 environments.py:89(reset)
                2421958  203.062    0.000  203.062    0.000 {built-in method tensor}
               27292928  182.659    0.000  202.947    0.000 __init__.py:67(is_acceptable)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8557120: <CHASER_U_S_0_0.05returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0_0.05returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:12 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Dec 14 17:04:54 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec 14 17:04:54 2020
Terminated at Tue Dec 15 16:00:12 2020
Results reported at Tue Dec 15 16:00:12 2020

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

    CPU time :                                   83986.00 sec.
    Max Memory :                                 54995 MB
    Average Memory :                             54302.26 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6445.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82519 sec.
    Turnaround time :                            348720 sec.

The output (if any) is above this job summary.

