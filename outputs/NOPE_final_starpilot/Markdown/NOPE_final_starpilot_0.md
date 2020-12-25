/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py:156: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  if state_differences is not 0:

    Name :                      NOPE_final_starpilot-0
    Discount :                  0.995
    Environment :               starpilot
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


      10639485883 function calls (10477228301 primitive calls) in 64523.93 seconds

##    Ordered by: cumulative time
   List reduced from 1354 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 64523.928 64523.928 {built-in method builtins.exec}
                      1    0.037    0.037 64523.928 64523.928 <string>:1(<module>)
                      1  390.988  390.988 64523.890 64523.890 main.py:91(main)
                2136780  144.306    0.000 41575.064    0.019 agent.py:93(learn)
                2051822  365.275    0.000 40943.117    0.020 agent.py:106(TD_learn)
                2051822  139.268    0.000 22492.304    0.011 memory.py:35(sample_distribution)
                2051822  226.524    0.000 21832.000    0.011 helpers.py:15(stack)
               18721380 11163.806    0.001 11163.814    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        172595092/10344068  758.405    0.000 10661.638    0.001 module.py:715(_call_impl)
                6240424  155.426    0.000 10293.194    0.002 agent.py:235(forward)
               18721272 10071.849    0.001 10071.849    0.001 {built-in method cat}
                2136780   42.648    0.000 9753.021    0.005 agent.py:72(chooseMulti)
              278034767 9460.357    0.000 9460.357    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2136780   55.457    0.000 7327.131    0.003 environments.py:83(step)
               24961696  189.725    0.000 6397.039    0.000 container.py:115(forward)
                2052821   74.540    0.000 5553.065    0.003 agent.py:88(<listcomp>)
                2052812    8.441    0.000 5309.328    0.003 agent.py:58(rememberMulti)
                2052812  190.579    0.000 5300.887    0.003 agent.py:63(<listcomp>)
               41056420  108.861    0.000 5294.328    0.000 exploration.py:34(epsilonGreedy)
                4103644   28.166    0.000 5081.209    0.001 grad_mode.py:23(decorate_context)
                4103644  193.031    0.000 5007.113    0.001 adam.py:55(step)
                2136780   48.481    0.000 4733.727    0.002 environments.py:85(<listcomp>)
               42942479 1206.258    0.000 4712.062    0.000 helpers.py:8(clean)
                4103644  937.525    0.000 4115.666    0.001 functional.py:53(adam)
               49097945 4010.032    0.000 4010.032    0.000 {built-in method as_tensor}
                4103644   31.560    0.000 3939.186    0.001 tensor.py:181(backward)
                4103644   19.903    0.000 3907.627    0.001 __init__.py:68(backward)
                4103644 3786.070    0.001 3786.070    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               37442544   65.594    0.000 3008.411    0.000 conv.py:422(forward)
               37442544   81.379    0.000 2912.146    0.000 conv.py:414(_conv_forward)
               37442544 2816.644    0.000 2816.644    0.000 {built-in method conv2d}
                2136780   43.145    0.000 2375.378    0.001 environments.py:84(<listcomp>)
               42735600  151.751    0.000 2332.233    0.000 interop.py:274(step)
                6240430  338.541    0.000 1832.479    0.000 rnn.py:110(flatten_parameters)
                6240424   70.747    0.000 1506.759    0.000 rnn.py:555(forward)
                6240424 1353.185    0.000 1353.185    0.000 {built-in method lstm}
               24961696   53.530    0.000 1254.791    0.000 linear.py:92(forward)
              344706204  731.860    0.000 1243.730    0.000 tensor.py:933(grad)
               24961696   94.540    0.000 1174.852    0.000 functional.py:1669(linear)
                4103644  107.045    0.000 1085.160    0.000 optimizer.py:167(zero_grad)
                6240427 1079.029    0.000 1079.029    0.000 {built-in method _cudnn_rnn_flatten_weight}
               42735600   19.313    0.000 1046.065    0.000 wrapper.py:25(act)
               62404240   60.084    0.000 1043.095    0.000 activation.py:713(forward)
               42735600   53.186    0.000 1026.752    0.000 env.py:197(act)
               62404240   87.849    0.000  983.011    0.000 functional.py:1292(leaky_relu)
               42735600  940.945    0.000  945.017    0.000 libenv.py:352(act)
               62404240  887.216    0.000  887.216    0.000 {built-in method torch._C._nn.leaky_relu}
               98487456  837.347    0.000  837.347    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24961696  787.197    0.000  787.197    0.000 {built-in method addmm}
               98487456  702.156    0.000  702.156    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               85678079   63.880    0.000  698.816    0.000 extract_dict_ob.py:9(observe)
               85678079   35.483    0.000  634.936    0.000 wrapper.py:19(observe)
              418911844  210.520    0.000  610.854    0.000 overrides.py:1073(has_torch_function)
               85678079  166.605    0.000  599.453    0.000 libenv.py:344(observe)
                   2094    0.801    0.000  487.642    0.233 agent.py:161(update_target_network)
               49243728  463.194    0.000  463.194    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               49243728  432.205    0.000  432.205    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              128413679  132.590    0.000  432.127    0.000 libenv.py:281(_maybe_copy_dict)
               49243728  384.682    0.000  384.682    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              452080852  154.494    0.000  382.577    0.000 {built-in method builtins.any}
              385243131  368.666    0.000  368.666    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11079411  133.818    0.000  349.142    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               49243728  343.838    0.000  343.838    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               29067175  302.710    0.000  323.836    0.000 module.py:781(__setattr__)
               42735600   33.790    0.000  317.153    0.000 wrapper.py:22(get_info)
                6410340   11.761    0.000  309.988    0.000 functional.py:74(split)
              307823371  297.803    0.000  297.803    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                6410340   27.097    0.000  297.323    0.000 tensor.py:460(split)
               42735600  147.296    0.000  283.363    0.000 libenv.py:363(get_info)
                2051822  215.516    0.000  281.164    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                6410340  268.970    0.000  268.970    0.000 {function Tensor.split at 0x7f95cecc9d30}
               41056240  267.068    0.000  267.068    0.000 memory.py:17(inner)
                   2094   73.662    0.035  260.168    0.124 memory.py:45(update_distribution)
                4103644    9.887    0.000  254.873    0.000 loss.py:445(forward)
               24210784   22.897    0.000  251.723    0.000 <__array_function__ internals>:2(prod)
               44791610  251.603    0.000  251.603    0.000 {built-in method numpy.array}
               49243728  250.790    0.000  250.790    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4103644   30.642    0.000  244.987    0.000 functional.py:2637(mse_loss)
               24210824   17.084    0.000  224.882    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              862785384  182.489    0.000  224.685    0.000 overrides.py:1086(<genexpr>)
               24210784   28.678    0.000  207.799    0.000 fromnumeric.py:2881(prod)
                   4188  182.989    0.044  205.318    0.049 {built-in method _pickle.loads}
                6240424   13.793    0.000  203.890    0.000 pooling.py:152(forward)
                2052821  144.349    0.000  193.347    0.000 agent.py:152(convert_values)
               42735600  190.764    0.000  190.764    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6240424   11.138    0.000  190.097    0.000 _jit_internal.py:257(fn)
               24961696  182.729    0.000  182.729    0.000 {method 't' of 'torch._C._TensorBase' objects}
               24210784   52.745    0.000  179.121    0.000 fromnumeric.py:70(_wrapreduction)
                6240424   12.276    0.000  177.934    0.000 functional.py:574(_max_pool2d)
                8207288  175.700    0.000  175.700    0.000 {built-in method gather}
                6240424  164.916    0.000  164.916    0.000 {built-in method max_pool2d}
                2136780   22.016    0.000  162.569    0.000 environments.py:86(<listcomp>)
               24961708  142.489    0.000  160.496    0.000 __init__.py:67(is_acceptable)
                2051822  160.179    0.000  160.179    0.000 memory.py:43(<listcomp>)
                4103644  146.294    0.000  146.294    0.000 {built-in method torch._C._nn.mse_loss}
               28980382  144.242    0.000  144.242    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2136780   14.596    0.000  140.871    0.000 collector.py:8(collect)
               42735620   26.378    0.000  140.602    0.000 environments.py:89(reset)
               49243944   58.995    0.000  130.402    0.000 tensor.py:596(__hash__)
               26264700  128.323    0.000  128.323    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8585268: <NOPE_final_starpilot_0> in cluster <dcc> Done

Job <NOPE_final_starpilot_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Dec 23 18:21:53 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec 23 18:47:40 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 23 18:47:40 2020
Terminated at Thu Dec 24 12:43:13 2020
Results reported at Thu Dec 24 12:43:13 2020

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

    CPU time :                                   67698.00 sec.
    Max Memory :                                 56041 MB
    Average Memory :                             55327.98 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5399.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64533 sec.
    Turnaround time :                            66080 sec.

The output (if any) is above this job summary.

