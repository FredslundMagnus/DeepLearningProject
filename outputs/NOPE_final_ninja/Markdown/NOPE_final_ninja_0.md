
    Name :                      NOPE_final_ninja-0
    Discount :                  0.995
    Environment :               ninja
    Hours :                     18
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
    State difference :          0
    State difference weight :   0.0
    Minutes used :              1075 minutes.
    Hours used :                17 hours.

# Profiling


      10492572188 function calls (10332549306 primitive calls) in 64520.80 seconds

##    Ordered by: cumulative time
   List reduced from 1354 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 64520.803 64520.803 {built-in method builtins.exec}
                      1    0.029    0.029 64520.803 64520.803 <string>:1(<module>)
                      1  387.337  387.337 64520.773 64520.773 main.py:91(main)
                2108130  146.785    0.000 41696.807    0.020 agent.py:93(learn)
                2023172  364.823    0.000 41058.422    0.020 agent.py:106(TD_learn)
                2023172  140.672    0.000 22575.926    0.011 memory.py:35(sample_distribution)
                2023172  232.628    0.000 21913.616    0.011 helpers.py:15(stack)
               18463530 11132.216    0.001 11132.273    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        170217142/10200818  759.156    0.000 10711.401    0.001 module.py:715(_call_impl)
                6154474  156.096    0.000 10339.766    0.002 agent.py:235(forward)
               18463422 10173.253    0.001 10173.253    0.001 {built-in method cat}
                2108130   41.970    0.000 9567.727    0.005 agent.py:72(chooseMulti)
              274054188 9179.718    0.000 9179.718    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2108130   58.497    0.000 7485.727    0.004 environments.py:83(step)
               24617896  191.287    0.000 6412.631    0.000 container.py:115(forward)
                2024171   75.571    0.000 5358.931    0.003 agent.py:88(<listcomp>)
                2024162    8.926    0.000 5215.485    0.003 agent.py:58(rememberMulti)
                2024162  183.635    0.000 5206.560    0.003 agent.py:63(<listcomp>)
               40483420  106.796    0.000 5095.852    0.000 exploration.py:34(epsilonGreedy)
                4046344   28.567    0.000 5063.319    0.001 grad_mode.py:23(decorate_context)
                4046344  195.386    0.000 4990.137    0.001 adam.py:55(step)
                2108130   50.208    0.000 4713.406    0.002 environments.py:85(<listcomp>)
               42261404 1209.895    0.000 4676.364    0.000 helpers.py:8(clean)
                4046344  930.779    0.000 4091.235    0.001 functional.py:53(adam)
               48330920 3974.190    0.000 3974.190    0.000 {built-in method as_tensor}
                4046344   33.375    0.000 3954.106    0.001 tensor.py:181(backward)
                4046344   20.357    0.000 3920.731    0.001 __init__.py:68(backward)
                4046344 3798.963    0.001 3798.963    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               36926844   66.554    0.000 3015.178    0.000 conv.py:422(forward)
               36926844   74.067    0.000 2917.770    0.000 conv.py:414(_conv_forward)
               36926844 2829.897    0.000 2829.897    0.000 {built-in method conv2d}
                2108130   43.278    0.000 2573.518    0.001 environments.py:84(<listcomp>)
               42162600  151.085    0.000 2530.240    0.000 interop.py:274(step)
                6154480  340.921    0.000 1837.208    0.000 rnn.py:110(flatten_parameters)
                6154474   73.926    0.000 1522.576    0.000 rnn.py:555(forward)
                6154474 1365.627    0.000 1365.627    0.000 {built-in method lstm}
               24617896   53.875    0.000 1276.819    0.000 linear.py:92(forward)
               42162600   19.975    0.000 1251.797    0.000 wrapper.py:25(act)
              339893004  736.826    0.000 1246.629    0.000 tensor.py:933(grad)
               42162600   52.543    0.000 1231.821    0.000 env.py:197(act)
               24617896  100.735    0.000 1195.656    0.000 functional.py:1669(linear)
               42162600 1146.317    0.000 1150.393    0.000 libenv.py:352(act)
                6154477 1084.185    0.000 1084.185    0.000 {built-in method _cudnn_rnn_flatten_weight}
                4046344  106.848    0.000 1082.825    0.000 optimizer.py:167(zero_grad)
               61544740   56.302    0.000 1026.048    0.000 activation.py:713(forward)
               61544740   81.100    0.000  969.746    0.000 functional.py:1292(leaky_relu)
               61544740  880.458    0.000  880.458    0.000 {built-in method torch._C._nn.leaky_relu}
               97112256  831.791    0.000  831.791    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24617896  798.160    0.000  798.160    0.000 {built-in method addmm}
               97112256  697.521    0.000  697.521    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               84424004   61.551    0.000  688.799    0.000 extract_dict_ob.py:9(observe)
               84424004   35.557    0.000  627.248    0.000 wrapper.py:19(observe)
              413067244  211.938    0.000  614.676    0.000 overrides.py:1073(has_torch_function)
               84424004  157.594    0.000  591.690    0.000 libenv.py:344(observe)
                   2066    0.810    0.000  491.600    0.238 agent.py:161(update_target_network)
               48556128  460.763    0.000  460.763    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              126586604  129.818    0.000  429.839    0.000 libenv.py:281(_maybe_copy_dict)
               48556128  427.738    0.000  427.738    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               48556128  386.909    0.000  386.909    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              445777852  155.706    0.000  384.295    0.000 {built-in method builtins.any}
              379761878  373.078    0.000  373.078    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11048418  133.894    0.000  350.148    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               48556128  340.701    0.000  340.701    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               28666075  298.008    0.000  321.321    0.000 module.py:781(__setattr__)
               42162600   34.911    0.000  316.257    0.000 wrapper.py:22(get_info)
                6324390   11.399    0.000  309.338    0.000 functional.py:74(split)
                6324390   26.153    0.000  297.068    0.000 tensor.py:460(split)
              303686492  293.467    0.000  293.467    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               42162600  145.743    0.000  281.346    0.000 libenv.py:363(get_info)
                2023172  215.156    0.000  279.813    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                6324390  269.590    0.000  269.590    0.000 {function Tensor.split at 0x7f532431ed30}
               40483240  265.252    0.000  265.252    0.000 memory.py:17(inner)
                   2066   74.899    0.036  262.295    0.127 memory.py:45(update_distribution)
                4046344    9.446    0.000  258.809    0.000 loss.py:445(forward)
               24120148   21.597    0.000  252.751    0.000 <__array_function__ internals>:2(prod)
               44189904  252.490    0.000  252.490    0.000 {built-in method numpy.array}
                4046344   31.573    0.000  249.363    0.000 functional.py:2637(mse_loss)
               48556128  248.681    0.000  248.681    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24120188   17.129    0.000  227.277    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              850752384  182.140    0.000  225.250    0.000 overrides.py:1086(<genexpr>)
               24120148   28.728    0.000  210.148    0.000 fromnumeric.py:2881(prod)
                6154474   17.358    0.000  207.268    0.000 pooling.py:152(forward)
                   4132  184.373    0.045  206.920    0.050 {built-in method _pickle.loads}
               42162600  194.288    0.000  194.288    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2024171  143.483    0.000  190.538    0.000 agent.py:152(convert_values)
                6154474   11.480    0.000  189.911    0.000 _jit_internal.py:257(fn)
               24617896  183.943    0.000  183.943    0.000 {method 't' of 'torch._C._TensorBase' objects}
               24120148   54.964    0.000  181.421    0.000 fromnumeric.py:70(_wrapreduction)
                6154474   11.932    0.000  177.438    0.000 functional.py:574(_max_pool2d)
                8092688  175.810    0.000  175.810    0.000 {built-in method gather}
                6154474  164.758    0.000  164.758    0.000 {built-in method max_pool2d}
                2023172  162.651    0.000  162.651    0.000 memory.py:43(<listcomp>)
               24617908  142.154    0.000  161.453    0.000 __init__.py:67(is_acceptable)
                4046344  148.709    0.000  148.709    0.000 {built-in method torch._C._nn.mse_loss}
               28579282  145.585    0.000  145.585    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2108130   14.576    0.000  143.154    0.000 collector.py:8(collect)
                2108130   22.192    0.000  140.306    0.000 environments.py:86(<listcomp>)
               48556344   59.624    0.000  132.246    0.000 tensor.py:596(__hash__)
               26145386  129.452    0.000  129.452    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                4216261  127.746    0.000  127.747    0.000 {built-in method builtins.sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8587608: <NOPE_final_ninja_0> in cluster <dcc> Done

Job <NOPE_final_ninja_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 25 20:02:00 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec 26 04:27:34 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec 26 04:27:34 2020
Terminated at Sat Dec 26 22:23:04 2020
Results reported at Sat Dec 26 22:23:04 2020

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

    CPU time :                                   67670.00 sec.
    Max Memory :                                 55890 MB
    Average Memory :                             55160.19 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5550.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64639 sec.
    Turnaround time :                            94864 sec.

The output (if any) is above this job summary.

