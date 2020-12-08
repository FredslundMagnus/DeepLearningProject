
    Name :                      EpsSoftmax_state_transition0.1maze-0
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
    Exploration :               epsintosoftmax
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11902721945 function calls (11700323387 primitive calls) in 82532.84 seconds

##    Ordered by: cumulative time
   List reduced from 1358 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82532.836 82532.836 {built-in method builtins.exec}
                      1    0.191    0.191 82532.836 82532.836 <string>:1(<module>)
                      1  512.368  512.368 82532.639 82532.639 main.py:92(main)
                2004198  188.589    0.000 53930.086    0.027 agent.py:86(learn)
                2003698  655.834    0.000 52957.958    0.026 agent.py:96(TD_learn)
                2003698  140.249    0.000 27499.140    0.014 memory.py:35(sample_distribution)
                2003698  297.194    0.000 26840.969    0.013 helpers.py:15(stack)
        214415186/12023188  973.601    0.000 15396.496    0.001 module.py:715(_call_impl)
               18034782 14981.170    0.001 14981.170    0.001 {built-in method cat}
                6011594  203.813    0.000 14355.637    0.002 agent.py:212(forward)
                2004198  201.750    0.000 12356.996    0.006 agent.py:74(chooseMulti)
               20039088 11264.067    0.001 11264.136    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               32062168  281.283    0.000 10066.755    0.000 container.py:115(forward)
                2004198   59.238    0.000 8424.592    0.004 environments.py:83(step)
                4007396   29.889    0.000 7179.915    0.002 grad_mode.py:23(decorate_context)
                2004198   91.939    0.000 7131.690    0.004 agent.py:62(rememberMulti)
                4007396  208.605    0.000 7101.574    0.002 adam.py:55(step)
                2004198  277.896    0.000 6680.761    0.003 agent.py:66(<listcomp>)
              269618059 6577.763    0.000 6577.763    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                4007396 1339.651    0.000 6106.187    0.002 functional.py:53(adam)
                2004198  142.756    0.000 5946.828    0.003 agent.py:84(<listcomp>)
                2004198   64.223    0.000 5416.282    0.003 environments.py:85(<listcomp>)
               40083960 1276.880    0.000 5406.345    0.000 exploration.py:40(epsintosoftmax)
               40209041 1233.539    0.000 5371.142    0.000 helpers.py:8(clean)
                4007396   40.938    0.000 5229.391    0.001 tensor.py:181(backward)
                4007396   23.065    0.000 5188.454    0.001 __init__.py:68(backward)
                4007396 5045.399    0.001 5045.399    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               46220135 4646.294    0.000 4646.294    0.000 {built-in method as_tensor}
               36069564   65.743    0.000 3683.533    0.000 conv.py:422(forward)
               36069564   80.339    0.000 3585.661    0.000 conv.py:414(_conv_forward)
               36069564 3491.644    0.000 3491.644    0.000 {built-in method conv2d}
               48093752  108.555    0.000 3206.065    0.000 linear.py:92(forward)
               48093752  297.768    0.000 3045.172    0.000 functional.py:1669(linear)
                2004198   43.718    0.000 2775.496    0.001 environments.py:84(<listcomp>)
               40083960  163.025    0.000 2731.778    0.000 interop.py:274(step)
                6011600  392.603    0.000 2386.946    0.000 rnn.py:110(flatten_parameters)
               40083960 1579.828    0.000 2364.849    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               42081158 1798.146    0.000 1798.146    0.000 {built-in method addmm}
                6011594   73.746    0.000 1744.882    0.000 rnn.py:555(forward)
               76147524   72.973    0.000 1692.896    0.000 activation.py:713(forward)
               76147524  109.557    0.000 1619.923    0.000 functional.py:1292(leaky_relu)
                6011594 1588.483    0.000 1588.483    0.000 {built-in method lstm}
                6011597 1538.851    0.000 1538.851    0.000 {built-in method _cudnn_rnn_flatten_weight}
               76147524 1499.915    0.000 1499.915    0.000 {built-in method torch._C._nn.leaky_relu}
              336621372  954.363    0.000 1471.460    0.000 tensor.py:933(grad)
                4007396  141.646    0.000 1412.463    0.000 optimizer.py:167(zero_grad)
               40083960   18.974    0.000 1344.374    0.000 wrapper.py:25(act)
               40083960   62.718    0.000 1325.400    0.000 env.py:197(act)
               96177504 1295.175    0.000 1295.175    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               40083960 1223.394    0.000 1227.415    0.000 libenv.py:352(act)
               96177504 1059.307    0.000 1059.307    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   4008    1.696    0.000  783.539    0.195 agent.py:139(update_target_network)
               80293001   67.327    0.000  754.578    0.000 extract_dict_ob.py:9(observe)
               29054173   66.536    0.000  716.691    0.000 functional.py:1479(softmax)
               48088752  691.106    0.000  691.106    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              432804092  250.759    0.000  690.259    0.000 overrides.py:1073(has_torch_function)
               80293001   36.374    0.000  687.250    0.000 wrapper.py:19(observe)
               80293001  172.291    0.000  650.876    0.000 libenv.py:344(observe)
               29054173  644.471    0.000  644.471    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               48088752  621.992    0.000  621.992    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2004198    5.987    0.000  616.772    0.000 agent.py:230(avoid_similar_state)
               53117585   61.542    0.000  614.346    0.000 <__array_function__ internals>:2(prod)
               48088752  567.095    0.000  567.095    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               53117625   43.772    0.000  541.258    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               48088752  513.519    0.000  513.519    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               48093752  504.263    0.000  504.263    0.000 {method 't' of 'torch._C._TensorBase' objects}
               53117585   71.204    0.000  497.486    0.000 fromnumeric.py:2881(prod)
              297421210  473.188    0.000  473.188    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              120376961  136.542    0.000  471.128    0.000 libenv.py:281(_maybe_copy_dict)
                   4008  144.143    0.036  461.092    0.115 memory.py:45(update_distribution)
               53117585  127.922    0.000  426.282    0.000 fromnumeric.py:70(_wrapreduction)
              488912660  169.983    0.000  422.815    0.000 {built-in method builtins.any}
                6012594   11.944    0.000  422.261    0.000 functional.py:74(split)
              361134891  421.269    0.000  421.269    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6012594   29.056    0.000  409.454    0.000 tensor.py:460(split)
               40083960  397.727    0.000  397.727    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               48088752  385.609    0.000  385.609    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               40083960  385.421    0.000  385.421    0.000 memory.py:17(inner)
               42095674  384.115    0.000  384.115    0.000 {built-in method numpy.array}
                6012594  379.110    0.000  379.110    0.000 {function Tensor.split at 0x7f81973d6ca0}
               28055607  350.580    0.000  373.343    0.000 module.py:781(__setattr__)
               40083960   36.854    0.000  337.363    0.000 wrapper.py:22(get_info)
                4007396    9.814    0.000  307.518    0.000 loss.py:445(forward)
               40083960  155.324    0.000  300.509    0.000 libenv.py:363(get_info)
                4007396   31.990    0.000  297.704    0.000 functional.py:2637(mse_loss)
                   8016  221.605    0.028  269.679    0.034 {built-in method _pickle.loads}
                2004198  262.826    0.000  267.028    0.000 agent.py:131(convert_values)
               36068564  260.851    0.000  260.851    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               55125291  260.295    0.000  260.295    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                2003698  196.516    0.000  251.045    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
              913701936  201.338    0.000  249.425    0.000 overrides.py:1086(<genexpr>)
                6011594   14.830    0.000  245.007    0.000 pooling.py:152(forward)
                6012594  230.477    0.000  230.477    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6011594   10.818    0.000  230.177    0.000 _jit_internal.py:257(fn)
                6011594   12.021    0.000  218.303    0.000 functional.py:574(_max_pool2d)
                6011594  205.546    0.000  205.546    0.000 {built-in method max_pool2d}
                4007396  191.131    0.000  191.131    0.000 {built-in method torch._C._nn.mse_loss}
                2308804  190.978    0.000  190.978    0.000 {built-in method tensor}
               24046388  167.137    0.000  186.950    0.000 __init__.py:67(is_acceptable)
                6011094  185.707    0.000  185.707    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8482839: <EpsSoftmax_state_transition0.1maze_0> in cluster <dcc> Done

Job <EpsSoftmax_state_transition0.1maze_0> was submitted from host <n-62-27-19> by user <s183914> in cluster <dcc> at Sat Dec  5 00:10:43 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec  5 00:40:01 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec  5 00:40:01 2020
Terminated at Sat Dec  5 23:35:49 2020
Results reported at Sat Dec  5 23:35:49 2020

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

    CPU time :                                   86711.00 sec.
    Max Memory :                                 54885 MB
    Average Memory :                             54235.91 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6555.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82550 sec.
    Turnaround time :                            84306 sec.

The output (if any) is above this job summary.

