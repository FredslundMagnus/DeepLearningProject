
    Name :                      Uncertainty0state_difference0dodgeball-0
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
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14045888869 function calls (13814264083 primitive calls) in 82521.38 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82521.384 82521.384 {built-in method builtins.exec}
                      1    0.045    0.045 82521.384 82521.384 <string>:1(<module>)
                      1  420.560  420.560 82521.338 82521.338 main.py:92(main)
                2293566  174.555    0.000 55686.484    0.024 agent.py:86(learn)
                2293066  802.906    0.000 54626.995    0.024 agent.py:96(TD_learn)
                2293066  146.003    0.000 23680.604    0.010 memory.py:35(sample_distribution)
                2293066  240.645    0.000 22957.595    0.010 helpers.py:15(stack)
        247670628/16052462 1083.297    0.000 16301.779    0.001 module.py:715(_call_impl)
                6879698  211.864    0.000 15037.678    0.002 agent.py:212(forward)
               22932768 11981.569    0.001 11981.629    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               36692056  303.528    0.000 10772.319    0.000 container.py:115(forward)
               20639094 10435.967    0.001 10435.967    0.001 {built-in method cat}
                6879198   42.965    0.000 10174.339    0.001 grad_mode.py:23(decorate_context)
                6879198  295.503    0.000 10050.506    0.001 adam.py:55(step)
                2293566   61.815    0.000 9747.862    0.004 environments.py:83(step)
                2293566  215.424    0.000 8787.969    0.004 agent.py:74(chooseMulti)
                6879198 1866.302    0.000 8647.177    0.001 functional.py:53(adam)
                2293566  104.656    0.000 7679.758    0.003 agent.py:62(rememberMulti)
                2293566  320.051    0.000 7175.614    0.003 agent.py:66(<listcomp>)
              309849825 6944.854    0.000 6944.854    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6879198   46.163    0.000 6479.302    0.001 tensor.py:181(backward)
                6879198   27.554    0.000 6433.140    0.001 __init__.py:68(backward)
                2293566   70.532    0.000 6281.074    0.003 environments.py:85(<listcomp>)
               46199528 1466.077    0.000 6261.399    0.000 helpers.py:8(clean)
                6879198 6228.016    0.001 6228.016    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               53078726 5312.222    0.000 5312.222    0.000 {built-in method as_tensor}
               41278188   77.095    0.000 3885.925    0.000 conv.py:422(forward)
               41278188   79.145    0.000 3776.605    0.000 conv.py:414(_conv_forward)
               41278188 3681.876    0.000 3681.876    0.000 {built-in method conv2d}
               55038584  119.719    0.000 3408.324    0.000 linear.py:92(forward)
               55038584  329.308    0.000 3232.692    0.000 functional.py:1669(linear)
                2293566   51.535    0.000 3161.181    0.001 environments.py:84(<listcomp>)
               45871320  190.645    0.000 3109.646    0.000 interop.py:274(step)
                6879704  387.388    0.000 2411.716    0.000 rnn.py:110(flatten_parameters)
              481543968 1293.531    0.000 2082.179    0.000 tensor.py:933(grad)
                6879198  202.329    0.000 2034.707    0.000 optimizer.py:167(zero_grad)
               48157886 1904.608    0.000 1904.608    0.000 {built-in method addmm}
                2293566  107.435    0.000 1887.380    0.001 agent.py:84(<listcomp>)
               87143508   77.209    0.000 1841.675    0.000 activation.py:713(forward)
              137583960 1830.093    0.000 1830.093    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               87143508  112.777    0.000 1764.466    0.000 functional.py:1292(leaky_relu)
                6879698   72.485    0.000 1697.921    0.000 rnn.py:555(forward)
               87143508 1640.510    0.000 1640.510    0.000 {built-in method torch._C._nn.leaky_relu}
                6879701 1611.322    0.000 1611.322    0.000 {built-in method _cudnn_rnn_flatten_weight}
               45871320   24.488    0.000 1565.225    0.000 wrapper.py:25(act)
              137583960 1541.217    0.000 1541.217    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               45871320   75.308    0.000 1540.737    0.000 env.py:197(act)
                6879698 1537.459    0.000 1537.459    0.000 {built-in method lstm}
               45871320  162.569    0.000 1464.033    0.000 exploration.py:34(epsilonGreedy)
               45871320 1417.516    0.000 1421.990    0.000 libenv.py:352(act)
              605374778  353.481    0.000  996.154    0.000 overrides.py:1073(has_torch_function)
               68791980  957.330    0.000  957.330    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   4587    1.605    0.000  884.934    0.193 agent.py:139(update_target_network)
               68791980  884.285    0.000  884.285    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               92070848   79.287    0.000  821.888    0.000 extract_dict_ob.py:9(observe)
               68791980  810.200    0.000  810.200    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92070848   39.164    0.000  742.601    0.000 wrapper.py:19(observe)
               68791980  733.181    0.000  733.181    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               92070848  179.335    0.000  703.437    0.000 libenv.py:344(observe)
                2293566    6.549    0.000  673.188    0.000 agent.py:230(avoid_similar_state)
              674171782  250.395    0.000  613.302    0.000 {built-in method builtins.any}
               68791980  568.997    0.000  568.997    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   4587  155.834    0.034  558.711    0.122 memory.py:45(update_distribution)
              343590940  514.607    0.000  514.607    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               55038584  510.549    0.000  510.549    0.000 {method 't' of 'torch._C._TensorBase' objects}
              137942168  156.157    0.000  509.902    0.000 libenv.py:281(_maybe_copy_dict)
               48173560  490.017    0.000  490.017    0.000 {built-in method numpy.array}
                6879198   14.967    0.000  456.363    0.000 loss.py:445(forward)
              413831091  447.746    0.000  447.746    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6879198   46.190    0.000  441.396    0.000 functional.py:2637(mse_loss)
               11318223  152.723    0.000  388.896    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6880698   12.663    0.000  381.242    0.000 functional.py:74(split)
               45871320   42.426    0.000  380.928    0.000 wrapper.py:22(get_info)
                6880698   30.583    0.000  367.640    0.000 tensor.py:460(split)
             1265788140  281.838    0.000  357.840    0.000 overrides.py:1086(<genexpr>)
               45871320  176.785    0.000  338.502    0.000 libenv.py:363(get_info)
                6880698  335.269    0.000  335.269    0.000 {function Tensor.split at 0x7f0f5a6ced30}
                2293066  246.194    0.000  319.492    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               45871320  318.302    0.000  318.302    0.000 memory.py:17(inner)
               45871320  315.911    0.000  315.911    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               32106759  283.057    0.000  305.875    0.000 module.py:781(__setattr__)
                2293566  285.220    0.000  288.886    0.000 agent.py:131(convert_values)
               41277188  286.719    0.000  286.719    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6879198  280.882    0.000  280.882    0.000 {built-in method torch._C._nn.mse_loss}
               24929652   23.549    0.000  276.296    0.000 <__array_function__ internals>:2(prod)
                   9174  217.463    0.024  271.549    0.030 {built-in method _pickle.loads}
                9172264  264.369    0.000  264.369    0.000 {built-in method gather}
                6879698   15.783    0.000  250.304    0.000 pooling.py:152(forward)
               24929692   19.156    0.000  248.179    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                2293566   28.564    0.000  243.792    0.000 environments.py:86(<listcomp>)
                6880698  242.667    0.000  242.667    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6879698   11.574    0.000  234.521    0.000 _jit_internal.py:257(fn)
               24929652   29.909    0.000  229.023    0.000 fromnumeric.py:2881(prod)
                6879698   11.434    0.000  221.655    0.000 functional.py:574(_max_pool2d)
               45871340   37.586    0.000  215.260    0.000 environments.py:89(reset)
                6879698  209.417    0.000  209.417    0.000 {built-in method max_pool2d}
                2642176  203.627    0.000  203.627    0.000 {built-in method tensor}
               68792226   90.136    0.000  202.311    0.000 tensor.py:596(__hash__)
               24929652   56.626    0.000  199.114    0.000 fromnumeric.py:70(_wrapreduction)
              247670628  179.328    0.000  179.328    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 8483549: <Uncertainty0state_difference0dodgeball_0> in cluster <dcc> Done

Job <Uncertainty0state_difference0dodgeball_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec  6 01:18:08 2020
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Dec  7 13:16:56 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec  7 13:16:56 2020
Terminated at Tue Dec  8 12:12:26 2020
Results reported at Tue Dec  8 12:12:26 2020

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

    CPU time :                                   83968.00 sec.
    Max Memory :                                 54812 MB
    Average Memory :                             54205.92 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6628.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82531 sec.
    Turnaround time :                            212058 sec.

The output (if any) is above this job summary.

