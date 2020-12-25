
    Name :                      NOPE_final_bossfight-0
    Discount :                  0.995
    Environment :               bossfight
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


      10641521153 function calls (10479274023 primitive calls) in 64519.00 seconds

##    Ordered by: cumulative time
   List reduced from 1354 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 64518.997 64518.997 {built-in method builtins.exec}
                      1    0.061    0.061 64518.997 64518.997 <string>:1(<module>)
                      1  389.874  389.874 64518.934 64518.934 main.py:91(main)
                2136646  145.066    0.000 40804.179    0.019 agent.py:93(learn)
                2051688  357.126    0.000 40177.324    0.020 agent.py:106(TD_learn)
                2051688  136.794    0.000 22087.104    0.011 memory.py:35(sample_distribution)
                2051688  211.293    0.000 21444.473    0.010 helpers.py:15(stack)
               18720174 11100.503    0.001 11100.507    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        172583970/10343398  726.255    0.000 10426.571    0.001 module.py:715(_call_impl)
                6240022  152.818    0.000 10063.723    0.002 agent.py:235(forward)
                2136646   43.705    0.000 9837.603    0.005 agent.py:72(chooseMulti)
               18720066 9786.026    0.001 9786.026    0.001 {built-in method cat}
              278015725 9506.636    0.000 9506.636    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2136646   57.517    0.000 8162.369    0.004 environments.py:83(step)
               24960088  184.749    0.000 6212.244    0.000 container.py:115(forward)
                2052687   72.573    0.000 5711.355    0.003 agent.py:88(<listcomp>)
               41053740  105.309    0.000 5450.685    0.000 exploration.py:34(epsilonGreedy)
                2052678    8.386    0.000 5159.232    0.003 agent.py:58(rememberMulti)
                2052678  174.380    0.000 5150.846    0.003 agent.py:63(<listcomp>)
                4103376   28.335    0.000 4970.616    0.001 grad_mode.py:23(decorate_context)
                4103376  202.883    0.000 4900.678    0.001 adam.py:55(step)
                2136646   50.587    0.000 4622.391    0.002 environments.py:85(<listcomp>)
               43075026 1187.897    0.000 4614.764    0.000 helpers.py:8(clean)
                4103376  900.043    0.000 4002.877    0.001 functional.py:53(adam)
               49230090 3899.674    0.000 3899.674    0.000 {built-in method as_tensor}
                4103376   30.182    0.000 3864.304    0.001 tensor.py:181(backward)
                4103376   19.906    0.000 3834.122    0.001 __init__.py:68(backward)
                4103376 3714.416    0.001 3714.416    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2136646   44.078    0.000 3298.849    0.002 environments.py:84(<listcomp>)
               42732920  156.707    0.000 3254.771    0.000 interop.py:274(step)
               37440132   65.039    0.000 2912.882    0.000 conv.py:422(forward)
               37440132   72.165    0.000 2817.847    0.000 conv.py:414(_conv_forward)
               37440132 2732.238    0.000 2732.238    0.000 {built-in method conv2d}
               42732920   20.272    0.000 1979.949    0.000 wrapper.py:25(act)
               42732920   52.319    0.000 1959.677    0.000 env.py:197(act)
               42732920 1874.128    0.000 1878.275    0.000 libenv.py:352(act)
                6240028  331.166    0.000 1791.007    0.000 rnn.py:110(flatten_parameters)
                6240022   69.876    0.000 1516.916    0.000 rnn.py:555(forward)
                6240022 1366.781    0.000 1366.781    0.000 {built-in method lstm}
              344683692  746.318    0.000 1242.220    0.000 tensor.py:933(grad)
               24960088   51.894    0.000 1234.525    0.000 linear.py:92(forward)
               24960088   91.488    0.000 1156.009    0.000 functional.py:1669(linear)
                4103376  113.517    0.000 1086.238    0.000 optimizer.py:167(zero_grad)
                6240025 1059.212    0.000 1059.212    0.000 {built-in method _cudnn_rnn_flatten_weight}
               62400220   55.137    0.000 1009.764    0.000 activation.py:713(forward)
               62400220   76.849    0.000  954.627    0.000 functional.py:1292(leaky_relu)
               62400220  870.068    0.000  870.068    0.000 {built-in method torch._C._nn.leaky_relu}
               98481024  816.653    0.000  816.653    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24960088  779.033    0.000  779.033    0.000 {built-in method addmm}
               98481024  689.113    0.000  689.113    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               85807946   62.626    0.000  687.769    0.000 extract_dict_ob.py:9(observe)
               85807946   36.935    0.000  625.144    0.000 wrapper.py:19(observe)
              418884508  204.817    0.000  599.174    0.000 overrides.py:1073(has_torch_function)
               85807946  155.377    0.000  588.208    0.000 libenv.py:344(observe)
                   2094    0.828    0.000  481.789    0.230 agent.py:161(update_target_network)
               49240512  445.448    0.000  445.448    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              128540866  131.948    0.000  432.481    0.000 libenv.py:281(_maybe_copy_dict)
               49240512  417.148    0.000  417.148    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               49240512  381.725    0.000  381.725    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              452051372  152.336    0.000  375.295    0.000 {built-in method builtins.any}
              385624692  367.174    0.000  367.174    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11079691  131.313    0.000  342.511    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               49240512  337.866    0.000  337.866    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               29065299  299.064    0.000  320.894    0.000 module.py:781(__setattr__)
                6409938   11.288    0.000  317.404    0.000 functional.py:74(split)
               42732920   35.961    0.000  312.517    0.000 wrapper.py:22(get_info)
                6409938   26.121    0.000  305.300    0.000 tensor.py:460(split)
              307532133  285.192    0.000  285.192    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                6409938  277.881    0.000  277.881    0.000 {function Tensor.split at 0x7f823b0b8d30}
               42732920  142.347    0.000  276.556    0.000 libenv.py:363(get_info)
                2051688  210.718    0.000  272.854    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               41053560  264.240    0.000  264.240    0.000 memory.py:17(inner)
                   2094   73.099    0.035  256.987    0.123 memory.py:45(update_distribution)
               44788796  253.699    0.000  253.699    0.000 {built-in method numpy.array}
                4103376    9.519    0.000  251.877    0.000 loss.py:445(forward)
               49240512  247.278    0.000  247.278    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24211210   22.074    0.000  245.808    0.000 <__array_function__ internals>:2(prod)
                4103376   29.654    0.000  242.359    0.000 functional.py:2637(mse_loss)
               24211250   16.936    0.000  219.943    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              862729104  177.180    0.000  219.768    0.000 overrides.py:1086(<genexpr>)
                   4188  181.135    0.043  203.148    0.049 {built-in method _pickle.loads}
               24211210   27.936    0.000  203.006    0.000 fromnumeric.py:2881(prod)
                6240022   18.684    0.000  201.206    0.000 pooling.py:152(forward)
               42732920  194.763    0.000  194.763    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2052687  141.492    0.000  192.263    0.000 agent.py:152(convert_values)
                2136646   21.051    0.000  183.613    0.000 environments.py:86(<listcomp>)
                6240022   10.264    0.000  182.521    0.000 _jit_internal.py:257(fn)
               24960088  177.776    0.000  177.776    0.000 {method 't' of 'torch._C._TensorBase' objects}
               24211210   51.269    0.000  175.070    0.000 fromnumeric.py:70(_wrapreduction)
                8206752  172.758    0.000  172.758    0.000 {built-in method gather}
                6240022   10.927    0.000  171.293    0.000 functional.py:574(_max_pool2d)
               42732940   26.505    0.000  162.575    0.000 environments.py:89(reset)
                6240022  159.634    0.000  159.634    0.000 {built-in method max_pool2d}
                2051688  155.950    0.000  155.950    0.000 memory.py:43(<listcomp>)
               24960100  135.068    0.000  152.141    0.000 __init__.py:67(is_acceptable)
                4103376  147.268    0.000  147.268    0.000 {built-in method torch._C._nn.mse_loss}
                2136646   14.433    0.000  142.928    0.000 collector.py:8(collect)
               28978506  142.068    0.000  142.068    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               49240728   56.899    0.000  127.673    0.000 tensor.py:596(__hash__)
                4273293  127.648    0.000  127.649    0.000 {built-in method builtins.sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 8585269: <NOPE_final_bossfight_0> in cluster <dcc> Done

Job <NOPE_final_bossfight_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Dec 23 18:21:53 2020
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec 23 18:52:36 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 23 18:52:36 2020
Terminated at Thu Dec 24 12:48:00 2020
Results reported at Thu Dec 24 12:48:00 2020

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

    CPU time :                                   67765.00 sec.
    Max Memory :                                 54748 MB
    Average Memory :                             54019.97 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6692.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64525 sec.
    Turnaround time :                            66367 sec.

The output (if any) is above this job summary.

