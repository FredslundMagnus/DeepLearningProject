[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NOPE_final_coinrun-0
    Discount :                  0.995
    Environment :               coinrun
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


      7953723090 function calls (7787186876 primitive calls) in 64513.75 seconds

##    Ordered by: cumulative time
   List reduced from 1329 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 64513.747 64513.747 {built-in method builtins.exec}
                      1    0.037    0.037 64513.747 64513.747 <string>:1(<module>)
                      1  413.169  413.169 64513.708 64513.708 main.py:91(main)
                2192967  150.592    0.000 39815.510    0.018 agent.py:93(learn)
                2106010  356.871    0.000 39167.368    0.019 agent.py:106(TD_learn)
                2106010  141.824    0.000 22309.252    0.011 memory.py:35(sample_distribution)
                2106010  215.607    0.000 21635.971    0.010 helpers.py:15(stack)
               19215069 11442.861    0.001 11442.887    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2192967   44.379    0.000 11103.916    0.005 agent.py:72(chooseMulti)
              285607157 10781.073    0.000 10781.073    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
        177146669/10617007  751.036    0.000 10431.696    0.001 module.py:710(_call_impl)
                6404987  155.928    0.000 10056.983    0.002 agent.py:235(forward)
               19214961 9702.600    0.001 9702.600    0.001 {built-in method cat}
                2192967   57.950    0.000 7832.768    0.004 environments.py:83(step)
                2107009   72.164    0.000 6974.739    0.003 agent.py:88(<listcomp>)
               42140180  108.407    0.000 6717.541    0.000 exploration.py:34(epsilonGreedy)
               25619948  185.399    0.000 6195.926    0.000 container.py:115(forward)
                2107000    8.536    0.000 5187.601    0.002 agent.py:58(rememberMulti)
                2107000  166.736    0.000 5179.065    0.002 agent.py:63(<listcomp>)
                2192967   49.348    0.000 4584.555    0.002 environments.py:85(<listcomp>)
               43923854 1222.318    0.000 4543.197    0.000 helpers.py:8(clean)
                4212020   23.452    0.000 4383.353    0.001 grad_mode.py:12(decorate_context)
                4212020 1103.054    0.000 4330.630    0.001 adam.py:51(step)
                4212020   18.757    0.000 3887.075    0.001 tensor.py:155(backward)
                4212020   23.890    0.000 3868.318    0.001 __init__.py:57(backward)
               50241884 3818.368    0.000 3818.368    0.000 {built-in method as_tensor}
                4212020 3749.425    0.001 3749.425    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2192967   43.753    0.000 3050.740    0.001 environments.py:84(<listcomp>)
               43859340  153.905    0.000 3006.988    0.000 interop.py:274(step)
               38429922   67.266    0.000 2943.935    0.000 conv.py:418(forward)
               38429922   74.683    0.000 2845.292    0.000 conv.py:410(_conv_forward)
               38429922 2754.965    0.000 2754.965    0.000 {built-in method conv2d}
                6404993  306.940    0.000 1722.958    0.000 rnn.py:109(flatten_parameters)
               43859340   19.935    0.000 1699.032    0.000 wrapper.py:25(act)
               43859340   52.782    0.000 1679.098    0.000 env.py:197(act)
               43859340 1593.073    0.000 1597.333    0.000 libenv.py:352(act)
                6404987   71.970    0.000 1561.939    0.000 rnn.py:550(forward)
                6404987 1405.063    0.000 1405.063    0.000 {built-in method lstm}
               25619948   52.287    0.000 1198.399    0.000 linear.py:90(forward)
               25619948   94.476    0.000 1117.169    0.000 functional.py:1655(linear)
                6404990 1034.295    0.000 1034.295    0.000 {built-in method _cudnn_rnn_flatten_weight}
               64049870   55.480    0.000  975.393    0.000 activation.py:653(forward)
               64049870   85.425    0.000  919.913    0.000 functional.py:1277(leaky_relu)
               64049870  826.009    0.000  826.009    0.000 {built-in method torch._C._nn.leaky_relu}
              101088480  801.003    0.000  801.003    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               25619948  757.817    0.000  757.817    0.000 {built-in method addmm}
              101088480  703.003    0.000  703.003    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               87783194   63.242    0.000  700.639    0.000 extract_dict_ob.py:9(observe)
               87783194   38.153    0.000  637.397    0.000 wrapper.py:19(observe)
               87783194  160.756    0.000  599.243    0.000 libenv.py:344(observe)
               50544240  501.075    0.000  501.075    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   2149    0.844    0.000  497.550    0.232 agent.py:161(update_target_network)
              131642534  133.657    0.000  437.666    0.000 libenv.py:281(_maybe_copy_dict)
               50544240  412.175    0.000  412.175    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4212020   70.922    0.000  407.397    0.000 optimizer.py:166(zero_grad)
              394929751  373.900    0.000  373.900    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11134407  132.887    0.000  348.454    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               29833803  314.995    0.000  339.015    0.000 module.py:774(__setattr__)
               50544240  335.700    0.000  335.700    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              316468893  326.598    0.000  326.598    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               50544240  324.921    0.000  324.921    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               43859340   35.128    0.000  323.210    0.000 wrapper.py:22(get_info)
                2106010  221.405    0.000  288.278    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               43859340  149.030    0.000  288.082    0.000 libenv.py:363(get_info)
                   2149   76.658    0.036  273.086    0.127 memory.py:45(update_distribution)
               42140000  269.109    0.000  269.109    0.000 memory.py:17(inner)
               45969648  266.847    0.000  266.847    0.000 {built-in method numpy.array}
                4212020    9.209    0.000  260.608    0.000 loss.py:444(forward)
               24374964   21.980    0.000  253.116    0.000 <__array_function__ internals>:2(prod)
                4212020   37.432    0.000  251.399    0.000 functional.py:2621(mse_loss)
               50544240  232.798    0.000  232.798    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24375004   17.236    0.000  227.357    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               24374964   28.007    0.000  210.121    0.000 fromnumeric.py:2881(prod)
                2107009  144.930    0.000  208.309    0.000 agent.py:152(convert_values)
                   4298  181.570    0.042  203.286    0.047 {built-in method _pickle.loads}
                6578901   11.026    0.000  200.520    0.000 functional.py:68(split)
                6404987   17.145    0.000  198.210    0.000 pooling.py:156(forward)
               43859340  191.592    0.000  191.592    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6578901   11.772    0.000  188.624    0.000 tensor.py:367(split)
               24374964   52.445    0.000  182.114    0.000 fromnumeric.py:70(_wrapreduction)
                6404987   11.273    0.000  181.065    0.000 _jit_internal.py:237(fn)
                6578901  175.513    0.000  175.513    0.000 {function Tensor.split at 0x7f8e665a79d0}
               25619960  154.201    0.000  172.306    0.000 __init__.py:66(is_acceptable)
              252721308  148.587    0.000  171.870    0.000 tensor.py:725(grad)
                6404987   11.857    0.000  168.755    0.000 functional.py:564(_max_pool2d)
                8424040  165.670    0.000  165.670    0.000 {built-in method gather}
                2106010  164.488    0.000  164.488    0.000 memory.py:43(<listcomp>)
               25619948  159.867    0.000  159.867    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6404987  156.109    0.000  156.109    0.000 {built-in method max_pool2d}
               29745011  143.205    0.000  143.205    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2192967   15.404    0.000  142.900    0.000 collector.py:8(collect)
                4212020  140.094    0.000  140.094    0.000 {built-in method torch._C._nn.mse_loss}
                2192967   23.487    0.000  139.522    0.000 environments.py:86(<listcomp>)
               26483123  132.071    0.000  132.071    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              166702209  131.169    0.000  131.259    0.000 module.py:758(__getattr__)
                4385935  126.498    0.000  126.498    0.000 {built-in method builtins.sum}
              175566388   45.469    0.000  126.235    0.000 libenv.py:271(_maybe_copy_ndarray)
               43859360   25.726    0.000  116.040    0.000 environments.py:89(reset)
              177146669   99.888    0.000   99.888    0.000 {built-in method torch._C._get_tracing_state}
                4212020   24.368    0.000   93.623    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8587062: <NOPE_final_coinrun_0> in cluster <dcc> Done

Job <NOPE_final_coinrun_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Thu Dec 24 13:34:59 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Dec 25 07:30:31 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 25 07:30:31 2020
Terminated at Sat Dec 26 01:25:51 2020
Results reported at Sat Dec 26 01:25:51 2020

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

    CPU time :                                   68012.00 sec.
    Max Memory :                                 55695 MB
    Average Memory :                             55024.94 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5745.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64521 sec.
    Turnaround time :                            129052 sec.

The output (if any) is above this job summary.

