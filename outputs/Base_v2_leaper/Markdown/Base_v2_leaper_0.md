[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_leaper-0
    Discount :                  0.995
    Environment :               leaper
    Hours :                     24
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      9322681212 function calls (9118672410 primitive calls) in 86113.26 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86113.256 86113.256 {built-in method builtins.exec}
                      1    0.043    0.043 86113.256 86113.256 <string>:1(<module>)
                      1  490.811  490.811 86113.212 86113.212 main.py:11(main)
                2684620   98.067    0.000 51635.945    0.019 agent.py:46(learn)
                2684120  337.831    0.000 50762.993    0.019 agent.py:54(TD_learn)
                2684120  187.213    0.000 29404.651    0.011 memory.py:27(sample_distribution)
                2684120  291.321    0.000 28518.787    0.011 helpers.py:12(stack)
              364138186 18083.986    0.000 18083.986    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2684620   40.699    0.000 17597.058    0.007 agent.py:41(chooseMulti)
        217423720/13421100  930.991    0.000 15071.103    0.001 module.py:710(_call_impl)
               10736980  225.515    0.000 14779.726    0.001 agent.py:119(forward)
               24158634 14725.492    0.001 14725.528    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2684620  101.994    0.000 13316.536    0.005 agent.py:44(<listcomp>)
               24158580 13101.870    0.001 13101.870    0.001 {built-in method cat}
               53692400  148.258    0.000 12974.603    0.000 exploration.py:33(epsilonGreedy)
                2684620   72.986    0.000 9508.034    0.004 environments.py:73(step)
               32210940  232.247    0.000 8388.652    0.000 container.py:115(forward)
                2684620    8.276    0.000 6688.419    0.002 agent.py:32(rememberMulti)
                2684620  223.699    0.000 6680.142    0.002 agent.py:33(<listcomp>)
                2684620   57.949    0.000 5827.012    0.002 environments.py:75(<listcomp>)
               54148691 1533.606    0.000 5826.276    0.000 helpers.py:8(clean)
               64421880  107.993    0.000 5021.659    0.000 conv.py:418(forward)
               62201051 4969.097    0.000 4969.097    0.000 {built-in method as_tensor}
               64421880  134.742    0.000 4866.019    0.000 conv.py:410(_conv_forward)
               64421880 4708.428    0.000 4708.428    0.000 {built-in method conv2d}
                2684120   16.964    0.000 4185.798    0.002 grad_mode.py:12(decorate_context)
                2684120   15.698    0.000 4179.936    0.002 tensor.py:155(backward)
                2684120   18.741    0.000 4164.238    0.002 __init__.py:57(backward)
                2684120 1049.515    0.000 4149.231    0.002 adam.py:51(step)
                2684120 4074.597    0.002 4074.597    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2684620   53.115    0.000 3352.886    0.001 environments.py:74(<listcomp>)
               53692400  198.723    0.000 3299.770    0.000 interop.py:274(step)
               10736986  508.570    0.000 2917.183    0.000 rnn.py:109(flatten_parameters)
               10736980  118.241    0.000 2699.973    0.000 rnn.py:550(forward)
               10736980 2438.896    0.000 2438.896    0.000 {built-in method lstm}
               10736983 1807.314    0.000 1807.314    0.000 {built-in method _cudnn_rnn_flatten_weight}
               53692400   26.519    0.000 1649.649    0.000 wrapper.py:25(act)
               53692400   64.839    0.000 1623.130    0.000 env.py:197(act)
               53692400 1518.028    0.000 1522.989    0.000 libenv.py:352(act)
               75158860   68.204    0.000 1253.159    0.000 activation.py:653(forward)
               75158860  113.802    0.000 1184.955    0.000 functional.py:1277(leaky_relu)
               75158860 1060.579    0.000 1060.579    0.000 {built-in method torch._C._nn.leaky_relu}
              107841091   81.778    0.000  893.131    0.000 extract_dict_ob.py:9(observe)
              107841091   48.135    0.000  811.354    0.000 wrapper.py:19(observe)
                   5369    1.322    0.000  774.884    0.144 agent.py:81(update_target_network)
               96628320  769.371    0.000  769.371    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              107841091  204.667    0.000  763.218    0.000 libenv.py:344(observe)
                   5369  199.851    0.037  709.865    0.132 memory.py:37(update_distribution)
               10736980   27.564    0.000  683.232    0.000 linear.py:90(forward)
               96628320  677.301    0.000  677.301    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10736980   58.959    0.000  640.070    0.000 functional.py:1655(linear)
               56387258  604.493    0.000  604.493    0.000 {built-in method numpy.array}
              161533491  170.713    0.000  558.656    0.000 libenv.py:281(_maybe_copy_dict)
               42948900  515.646    0.000  547.195    0.000 module.py:774(__setattr__)
              484605842  477.153    0.000  477.153    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48314160  467.878    0.000  467.878    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10736980  427.063    0.000  427.063    0.000 {built-in method addmm}
               11708614  157.069    0.000  403.069    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               53692400   43.371    0.000  402.055    0.000 wrapper.py:22(get_info)
               48314160  400.888    0.000  400.888    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              376646244  397.922    0.000  397.922    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                2684120  298.494    0.000  386.199    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                2684120   66.892    0.000  382.490    0.000 optimizer.py:166(zero_grad)
               53692400  369.943    0.000  369.943    0.000 memory.py:15(inner)
               53692400  184.363    0.000  358.684    0.000 libenv.py:363(get_info)
               10736980   32.651    0.000  330.460    0.000 pooling.py:156(forward)
               48314160  324.248    0.000  324.248    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48314160  315.307    0.000  315.307    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10736980   17.987    0.000  297.809    0.000 _jit_internal.py:237(fn)
               26101488   25.546    0.000  294.406    0.000 <__array_function__ internals>:2(prod)
               10736980   20.551    0.000  278.113    0.000 functional.py:564(_max_pool2d)
               26101528   19.779    0.000  264.591    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                8053860   13.818    0.000  263.921    0.000 functional.py:68(split)
               42947932  230.666    0.000  260.746    0.000 __init__.py:66(is_acceptable)
               10736980  256.136    0.000  256.136    0.000 {built-in method max_pool2d}
                2684620   30.438    0.000  255.149    0.000 environments.py:76(<listcomp>)
                8053860   13.688    0.000  249.079    0.000 tensor.py:367(split)
               26101488   33.129    0.000  244.811    0.000 fromnumeric.py:2881(prod)
               53692400  239.938    0.000  239.938    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8053860  234.012    0.000  234.012    0.000 {function Tensor.split at 0x7fef234a5940}
               53692420   33.632    0.000  224.715    0.000 environments.py:79(reset)
               48314160  217.276    0.000  217.276    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               26101488   60.418    0.000  211.682    0.000 fromnumeric.py:70(_wrapreduction)
                2684120  208.536    0.000  208.536    0.000 memory.py:35(<listcomp>)
                2684120    7.676    0.000  180.545    0.000 loss.py:444(forward)
                2684620   17.113    0.000  174.812    0.000 collector.py:7(collect)
                2684120   25.461    0.000  172.869    0.000 functional.py:2621(mse_loss)
              241570854  140.860    0.000  164.065    0.000 tensor.py:725(grad)
               28790977  162.560    0.000  162.560    0.000 {method 'reduce' of 'numpy.ufunc' objects}
               26842200  160.149    0.000  160.149    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              215682182   56.723    0.000  157.253    0.000 libenv.py:271(_maybe_copy_ndarray)
                5369241  156.429    0.000  156.429    0.000 {built-in method builtins.sum}
              204217729  155.406    0.000  155.532    0.000 module.py:758(__getattr__)
              217423720  136.255    0.000  136.255    0.000 {built-in method torch._C._get_tracing_state}
                5368240  130.892    0.000  130.892    0.000 {built-in method gather}
                2684120   98.929    0.000   98.929    0.000 {built-in method torch._C._nn.mse_loss}
               10736980   29.881    0.000   95.459    0.000 rnn.py:524(check_forward_args)
               10736980   90.673    0.000   90.673    0.000 {method 't' of 'torch._C._TensorBase' objects}
              901905820   84.339    0.000   84.339    0.000 {method 'values' of 'collections.OrderedDict' objects}
               54148731   41.397    0.000   82.189    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8410446: <Base_v2_leaper_0> in cluster <dcc> Done

Job <Base_v2_leaper_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Sat Nov 21 14:15:16 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov 21 18:43:11 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 21 18:43:11 2020
Terminated at Sun Nov 22 18:38:29 2020
Results reported at Sun Nov 22 18:38:29 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=80G]"
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

    CPU time :                                   92668.00 sec.
    Max Memory :                                 56743 MB
    Average Memory :                             56033.96 MB
    Total Requested Memory :                     81920.00 MB
    Delta Memory :                               25177.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86118 sec.
    Turnaround time :                            102193 sec.

The output (if any) is above this job summary.

