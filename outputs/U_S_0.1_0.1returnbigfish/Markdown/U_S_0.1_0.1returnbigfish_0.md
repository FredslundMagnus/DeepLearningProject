
    Name :                      U_S_0.1_0.1returnbigfish-0
    Discount :                  0.99
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
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12781703218 function calls (12593697136 primitive calls) in 82514.16 seconds

##    Ordered by: cumulative time
   List reduced from 1362 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82514.164 82514.164 {built-in method builtins.exec}
                      1    0.042    0.042 82514.164 82514.164 <string>:1(<module>)
                      1  434.306  434.306 82514.122 82514.122 main.py:92(main)
                2192682  187.594    0.000 54819.524    0.025 agent.py:89(learn)
                2105725  780.446    0.000 54102.350    0.026 agent.py:102(TD_learn)
                2105725  158.624    0.000 24347.543    0.012 memory.py:35(sample_distribution)
                2105725  288.386    0.000 23613.549    0.011 helpers.py:15(stack)
        205019175/17019713  960.592    0.000 14929.133    0.001 module.py:715(_call_impl)
                6404132  175.578    0.000 13028.987    0.002 agent.py:231(forward)
               25616634 11643.062    0.000 11643.081    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               23423846 11508.971    0.000 11508.971    0.000 {built-in method cat}
                6317175   43.044    0.000 9764.956    0.002 grad_mode.py:23(decorate_context)
                6317175  284.199    0.000 9648.128    0.002 adam.py:55(step)
               29914934  269.562    0.000 9497.345    0.000 container.py:115(forward)
                2192682   63.714    0.000 9305.134    0.004 environments.py:83(step)
                2106715   42.755    0.000 8981.454    0.004 agent.py:58(rememberMulti)
                2192682  282.527    0.000 8778.827    0.004 agent.py:72(chooseMulti)
                2106715  404.753    0.000 8683.885    0.004 agent.py:60(<listcomp>)
                6317175 1799.108    0.000 8303.265    0.001 functional.py:53(adam)
              369774408 8194.772    0.000 8194.772    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6317175   47.559    0.000 6369.523    0.001 tensor.py:181(backward)
                6317175   28.726    0.000 6321.964    0.001 __init__.py:68(backward)
                2192682   74.414    0.000 6226.551    0.003 environments.py:85(<listcomp>)
               44014604 1487.502    0.000 6178.022    0.000 helpers.py:8(clean)
                6317175 6115.921    0.001 6115.921    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               50331779 5189.994    0.000 5189.994    0.000 {built-in method as_tensor}
               38424792   73.097    0.000 3808.266    0.000 conv.py:422(forward)
               38424792   81.699    0.000 3701.704    0.000 conv.py:414(_conv_forward)
               38424792 3603.728    0.000 3603.728    0.000 {built-in method conv2d}
                2192682   52.183    0.000 2804.489    0.001 environments.py:84(<listcomp>)
               43853640  186.891    0.000 2752.306    0.000 interop.py:274(step)
               38511746   90.328    0.000 2604.268    0.000 linear.py:92(forward)
               38511746  283.238    0.000 2467.600    0.000 functional.py:1669(linear)
                6404138  408.503    0.000 2410.547    0.000 rnn.py:110(flatten_parameters)
              442202358 1226.592    0.000 1978.078    0.000 tensor.py:933(grad)
                6317175  191.491    0.000 1936.205    0.000 optimizer.py:167(zero_grad)
                2192682  108.996    0.000 1907.291    0.001 agent.py:87(<listcomp>)
                6404132   75.851    0.000 1752.566    0.000 rnn.py:555(forward)
              126343500 1750.900    0.000 1750.900    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               72638132   67.746    0.000 1617.117    0.000 activation.py:713(forward)
                6404135 1597.113    0.000 1597.113    0.000 {built-in method _cudnn_rnn_flatten_weight}
                6404132 1588.196    0.000 1588.196    0.000 {built-in method lstm}
               72638132  103.295    0.000 1549.371    0.000 functional.py:1292(leaky_relu)
               43853640  162.723    0.000 1479.674    0.000 exploration.py:34(epsilonGreedy)
              126343500 1472.438    0.000 1472.438    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               72638132 1436.220    0.000 1436.220    0.000 {built-in method torch._C._nn.leaky_relu}
                4298406   18.287    0.000 1362.523    0.000 agent.py:247(avoid_similar_state)
               31933703 1353.708    0.000 1353.708    0.000 {built-in method addmm}
               43853640   22.775    0.000 1228.310    0.000 wrapper.py:25(act)
               43853640   72.853    0.000 1205.534    0.000 env.py:197(act)
               43853640 1084.885    0.000 1089.329    0.000 libenv.py:352(act)
               63171750  926.455    0.000  926.455    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              543886100  328.009    0.000  913.489    0.000 overrides.py:1073(has_torch_function)
               63171750  837.384    0.000  837.384    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               87868244   75.555    0.000  810.333    0.000 extract_dict_ob.py:9(observe)
               63171750  785.803    0.000  785.803    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               87868244   37.860    0.000  734.777    0.000 wrapper.py:19(observe)
               63171750  705.994    0.000  705.994    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               87868244  184.035    0.000  696.917    0.000 libenv.py:344(observe)
              411055121  652.770    0.000  652.770    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              595032220  233.319    0.000  559.276    0.000 {built-in method builtins.any}
               63171750  547.372    0.000  547.372    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   2149    0.935    0.000  529.581    0.246 agent.py:157(update_target_network)
              131721884  154.712    0.000  502.345    0.000 libenv.py:281(_maybe_copy_dict)
                6317175   12.586    0.000  439.743    0.000 loss.py:445(forward)
              395167801  438.305    0.000  438.305    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6317175   43.902    0.000  427.156    0.000 functional.py:2637(mse_loss)
               11216959  160.344    0.000  405.726    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               38511746  392.333    0.000  392.333    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6578046   12.526    0.000  385.123    0.000 functional.py:74(split)
               43853640   40.853    0.000  373.215    0.000 wrapper.py:22(get_info)
                6578046   32.247    0.000  371.634    0.000 tensor.py:460(split)
               42134300  367.783    0.000  367.783    0.000 memory.py:17(inner)
                6578046  337.589    0.000  337.589    0.000 {function Tensor.split at 0x7f784fde8ca0}
               43853640  170.577    0.000  332.362    0.000 libenv.py:363(get_info)
             1126283946  257.906    0.000  321.352    0.000 overrides.py:1086(<genexpr>)
               29829813  296.426    0.000  320.157    0.000 module.py:781(__setattr__)
               43853640  318.622    0.000  318.622    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2105725  243.591    0.000  315.033    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               10528625  305.364    0.000  305.364    0.000 {built-in method gather}
               45963663  287.982    0.000  287.982    0.000 {built-in method numpy.array}
               24539783   24.668    0.000  284.584    0.000 <__array_function__ internals>:2(prod)
                2106724  279.255    0.000  282.608    0.000 agent.py:148(convert_values)
                   2149   76.119    0.035  276.419    0.129 memory.py:45(update_distribution)
                6317175  272.586    0.000  272.586    0.000 {built-in method torch._C._nn.mse_loss}
               38163921  267.176    0.000  267.176    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6578043  258.346    0.000  258.346    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               24539823   18.848    0.000  255.315    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                4213430   23.542    0.000  254.813    0.000 tensor.py:576(__iter__)
                6404132   16.133    0.000  252.112    0.000 pooling.py:152(forward)
               24539783   30.737    0.000  236.467    0.000 fromnumeric.py:2881(prod)
                6404132   11.558    0.000  235.979    0.000 _jit_internal.py:257(fn)
                   4298  200.328    0.047  227.354    0.053 {built-in method _pickle.loads}
                6404132   12.508    0.000  223.207    0.000 functional.py:574(_max_pool2d)
                4213430  221.985    0.000  221.985    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2192682   31.886    0.000  210.379    0.000 environments.py:86(<listcomp>)
                6404132  209.818    0.000  209.818    0.000 {built-in method max_pool2d}
               24539783   57.662    0.000  205.730    0.000 fromnumeric.py:70(_wrapreduction)
               63171996   87.332    0.000  193.241    0.000 tensor.py:596(__hash__)
               10615581  190.184    0.000  190.184    0.000 {method 'type' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 8575819: <U_S_0.1_0.1returnbigfish_0> in cluster <dcc> Done

Job <U_S_0.1_0.1returnbigfish_0> was submitted from host <n-62-30-3> by user <s183914> in cluster <dcc> at Fri Dec 18 16:26:01 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Dec 18 22:12:14 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 18 22:12:14 2020
Terminated at Sat Dec 19 21:07:32 2020
Results reported at Sat Dec 19 21:07:32 2020

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

    CPU time :                                   84279.00 sec.
    Max Memory :                                 56793 MB
    Average Memory :                             56051.21 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4647.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82519 sec.
    Turnaround time :                            103291 sec.

The output (if any) is above this job summary.

