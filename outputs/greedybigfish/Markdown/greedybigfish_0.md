
    Name :                      greedybigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      0
    Exploration :               greedy
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11995316979 function calls (11757196716 primitive calls) in 82550.35 seconds

##    Ordered by: cumulative time
   List reduced from 1342 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82550.351 82550.351 {built-in method builtins.exec}
                      1    0.049    0.049 82550.351 82550.351 <string>:1(<module>)
                      1  488.165  488.165 82550.301 82550.301 main.py:11(main)
                2480729  120.193    0.000 55074.074    0.022 agent.py:57(learn)
                2480229  418.810    0.000 54133.510    0.022 agent.py:67(TD_learn)
                2480229  177.749    0.000 30737.067    0.012 memory.py:35(sample_distribution)
                2480229  340.436    0.000 29871.002    0.012 helpers.py:12(stack)
        250515629/12401645 1080.611    0.000 16396.870    0.001 module.py:715(_call_impl)
                9921416  283.529    0.000 16119.973    0.002 agent.py:147(forward)
               22323561 14493.163    0.001 14493.163    0.001 {built-in method cat}
               22323627 14387.604    0.001 14387.607    0.001 {method 'to' of 'torch._C._TensorBase' objects}
              347302060 11685.679    0.000 11685.679    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2480729   42.431    0.000 10814.601    0.004 agent.py:51(chooseMulti)
               39685664  276.250    0.000 9589.271    0.000 container.py:115(forward)
                2480729   72.199    0.000 8954.318    0.004 environments.py:73(step)
                2480729    8.082    0.000 6994.024    0.003 agent.py:42(rememberMulti)
                2480729  249.757    0.000 6985.942    0.003 agent.py:43(<listcomp>)
                2480729   88.571    0.000 6091.520    0.002 agent.py:55(<listcomp>)
               49614580  113.475    0.000 5777.695    0.000 exploration.py:27(greedy)
                2480729   54.284    0.000 5754.424    0.002 environments.py:75(<listcomp>)
               49988666 1490.582    0.000 5750.228    0.000 helpers.py:8(clean)
               57429353 5069.416    0.000 5069.416    0.000 {built-in method as_tensor}
               59528496  106.369    0.000 4823.828    0.000 conv.py:422(forward)
                2480229   21.423    0.000 4773.403    0.002 grad_mode.py:23(decorate_context)
                2480229  182.348    0.000 4722.231    0.002 adam.py:55(step)
               59528496  119.661    0.000 4666.380    0.000 conv.py:414(_conv_forward)
               59528496 4523.651    0.000 4523.651    0.000 {built-in method conv2d}
                2480229   25.078    0.000 4030.056    0.002 tensor.py:181(backward)
                2480229   16.139    0.000 4004.979    0.002 __init__.py:68(backward)
                2480229 3916.190    0.002 3916.190    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2480229  881.413    0.000 3844.837    0.002 functional.py:53(adam)
                9921422  536.685    0.000 2911.103    0.000 rnn.py:110(flatten_parameters)
                2480729   56.868    0.000 2889.855    0.001 environments.py:74(<listcomp>)
               49614580  195.466    0.000 2832.987    0.000 interop.py:274(step)
                9921416  112.631    0.000 2505.872    0.000 rnn.py:555(forward)
                9921416 2256.209    0.000 2256.209    0.000 {built-in method lstm}
                9921419 1737.396    0.000 1737.396    0.000 {built-in method _cudnn_rnn_flatten_weight}
               29764248   67.607    0.000 1621.749    0.000 linear.py:92(forward)
               29764248  126.780    0.000 1521.855    0.000 functional.py:1669(linear)
               89292744   88.513    0.000 1511.563    0.000 activation.py:713(forward)
               89292744  125.004    0.000 1423.050    0.000 functional.py:1292(leaky_relu)
               89292744 1284.636    0.000 1284.636    0.000 {built-in method torch._C._nn.leaky_relu}
              332350752  739.717    0.000 1243.678    0.000 tensor.py:933(grad)
               49614580   24.799    0.000 1213.564    0.000 wrapper.py:25(act)
               49614580   69.125    0.000 1188.765    0.000 env.py:197(act)
               49614580 1077.990    0.000 1082.878    0.000 libenv.py:352(act)
                2480229  101.992    0.000 1056.028    0.000 optimizer.py:167(zero_grad)
               29764248 1005.150    0.000 1005.150    0.000 {built-in method addmm}
               99603246   78.304    0.000  877.334    0.000 extract_dict_ob.py:9(observe)
                   4961    1.550    0.000  820.371    0.165 agent.py:101(update_target_network)
               99603246   47.207    0.000  799.030    0.000 wrapper.py:19(observe)
               89288244  771.608    0.000  771.608    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               99603246  192.038    0.000  751.823    0.000 libenv.py:344(observe)
                   4961  189.358    0.038  746.211    0.150 memory.py:45(update_distribution)
               89288244  645.605    0.000  645.605    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               52104731  640.614    0.000  640.614    0.000 {built-in method numpy.array}
              406759296  218.783    0.000  628.691    0.000 overrides.py:1073(has_torch_function)
              149217826  165.018    0.000  556.290    0.000 libenv.py:281(_maybe_copy_dict)
               39686833  491.533    0.000  520.221    0.000 module.py:781(__setattr__)
              447658439  481.697    0.000  481.697    0.000 {method 'copy' of 'numpy.ndarray' objects}
               44644122  425.379    0.000  425.379    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               44644122  402.771    0.000  402.771    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               49614580   45.730    0.000  399.538    0.000 wrapper.py:22(get_info)
              441484026  156.864    0.000  390.064    0.000 {built-in method builtins.any}
                7442187   13.095    0.000  387.122    0.000 functional.py:74(split)
              368876489  374.360    0.000  374.360    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               44644122  374.069    0.000  374.069    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                7442187   31.498    0.000  373.013    0.000 tensor.py:460(split)
                2480229  274.510    0.000  366.243    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               49614580  363.523    0.000  363.523    0.000 memory.py:17(inner)
               49614580  183.472    0.000  353.809    0.000 libenv.py:363(get_info)
                7442187  339.944    0.000  339.944    0.000 {function Tensor.split at 0x7f8586f8eca0}
               44644122  328.622    0.000  328.622    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9921416   22.720    0.000  328.205    0.000 pooling.py:152(forward)
                9921416   17.615    0.000  305.485    0.000 _jit_internal.py:257(fn)
                9921416   18.031    0.000  286.074    0.000 functional.py:574(_max_pool2d)
                9921416  266.671    0.000  266.671    0.000 {built-in method max_pool2d}
               39685676  211.777    0.000  240.830    0.000 __init__.py:67(is_acceptable)
               29764248  239.369    0.000  239.369    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2480729   28.815    0.000  237.840    0.000 environments.py:76(<listcomp>)
               44644122  233.577    0.000  233.577    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              843282840  187.936    0.000  230.865    0.000 overrides.py:1086(<genexpr>)
               49614580  225.254    0.000  225.254    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9921416  220.779    0.000  220.779    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
                2480229  213.381    0.000  213.381    0.000 memory.py:43(<listcomp>)
               49614600   36.821    0.000  209.080    0.000 environments.py:79(reset)
              238362446  185.923    0.000  186.065    0.000 module.py:765(__getattr__)
                2480729   15.918    0.000  170.335    0.000 collector.py:7(collect)
                2480229    6.836    0.000  168.359    0.000 loss.py:445(forward)
                2480229   21.183    0.000  161.523    0.000 functional.py:2637(mse_loss)
              199206492   54.906    0.000  157.698    0.000 libenv.py:271(_maybe_copy_ndarray)
               24803290  157.286    0.000  157.286    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                4961459  153.234    0.000  153.235    0.000 {built-in method builtins.sum}
              250515629  148.999    0.000  148.999    0.000 {built-in method torch._C._get_tracing_state}
                4960458  132.311    0.000  132.311    0.000 {built-in method gather}
               44644296   56.882    0.000  125.358    0.000 tensor.py:596(__hash__)
             1041748180  100.595    0.000  100.595    0.000 {method 'values' of 'collections.OrderedDict' objects}
                2480229   95.152    0.000   95.152    0.000 {built-in method torch._C._nn.mse_loss}
                9921419   34.813    0.000   94.783    0.000 __init__.py:246(__init__)
                9921416   32.672    0.000   92.893    0.000 rnn.py:529(check_forward_args)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8447007: <greedybigfish_0> in cluster <dcc> Done

Job <greedybigfish_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 12:57:11 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Nov 27 13:14:46 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 13:14:46 2020
Terminated at Sat Nov 28 12:11:01 2020
Results reported at Sat Nov 28 12:11:01 2020

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

    CPU time :                                   87170.00 sec.
    Max Memory :                                 57016 MB
    Average Memory :                             56221.58 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4424.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82575 sec.
    Turnaround time :                            83630 sec.

The output (if any) is above this job summary.


    Name :                      greedybigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      0
    Exploration :               greedy
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11989855136 function calls (11751837209 primitive calls) in 82521.29 seconds

##    Ordered by: cumulative time
   List reduced from 1342 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82521.294 82521.294 {built-in method builtins.exec}
                      1    0.057    0.057 82521.294 82521.294 <string>:1(<module>)
                      1  454.349  454.349 82521.237 82521.237 main.py:11(main)
                2479663  108.340    0.000 55739.002    0.022 agent.py:57(learn)
                2479163  486.128    0.000 54907.000    0.022 agent.py:67(TD_learn)
                2479163  169.800    0.000 27316.674    0.011 memory.py:35(sample_distribution)
                2479163  287.549    0.000 26480.303    0.011 helpers.py:12(stack)
        250407963/12396315 1074.141    0.000 18509.715    0.001 module.py:715(_call_impl)
                9917152  299.436    0.000 18210.461    0.002 agent.py:147(forward)
               22314033 13522.921    0.001 13522.944    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               22313967 12116.829    0.001 12116.829    0.001 {built-in method cat}
               39668608  301.814    0.000 10909.073    0.000 container.py:115(forward)
              347152820 9839.619    0.000 9839.619    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2479663   70.910    0.000 9383.682    0.004 environments.py:73(step)
                2479663   43.199    0.000 9147.536    0.004 agent.py:51(chooseMulti)
                2479663    7.435    0.000 7596.799    0.003 agent.py:42(rememberMulti)
                2479663  314.148    0.000 7589.363    0.003 agent.py:43(<listcomp>)
                2479163   20.810    0.000 6261.321    0.003 grad_mode.py:23(decorate_context)
                2479163  177.918    0.000 6211.553    0.003 adam.py:55(step)
                2479663   57.977    0.000 6147.571    0.002 environments.py:75(<listcomp>)
               49951807 1451.472    0.000 6140.618    0.000 helpers.py:8(clean)
               59502912  103.673    0.000 5501.702    0.000 conv.py:422(forward)
               57389296 5401.014    0.000 5401.014    0.000 {built-in method as_tensor}
               59502912  114.864    0.000 5354.935    0.000 conv.py:414(_conv_forward)
                2479163 1146.489    0.000 5325.836    0.002 functional.py:53(adam)
               59502912 5220.600    0.000 5220.600    0.000 {built-in method conv2d}
                2479163   25.136    0.000 4740.782    0.002 tensor.py:181(backward)
                2479163   16.591    0.000 4715.646    0.002 __init__.py:68(backward)
                2479163 4621.103    0.002 4621.103    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2479663  103.564    0.000 3975.938    0.002 agent.py:55(<listcomp>)
               49593260  139.005    0.000 3556.101    0.000 exploration.py:27(greedy)
                9917158  573.122    0.000 3552.166    0.000 rnn.py:110(flatten_parameters)
                2479663   51.599    0.000 2922.390    0.001 environments.py:74(<listcomp>)
               49593260  191.467    0.000 2870.791    0.000 interop.py:274(step)
                9917152  115.401    0.000 2549.929    0.000 rnn.py:555(forward)
                9917155 2329.818    0.000 2329.818    0.000 {built-in method _cudnn_rnn_flatten_weight}
                9917152 2300.724    0.000 2300.724    0.000 {built-in method lstm}
               29751456   68.462    0.000 1876.788    0.000 linear.py:92(forward)
               89254368   83.367    0.000 1825.450    0.000 activation.py:713(forward)
               29751456  130.311    0.000 1777.759    0.000 functional.py:1669(linear)
               89254368  123.545    0.000 1742.083    0.000 functional.py:1292(leaky_relu)
               89254368 1607.801    0.000 1607.801    0.000 {built-in method torch._C._nn.leaky_relu}
              332207908  842.603    0.000 1322.878    0.000 tensor.py:933(grad)
               49593260   22.370    0.000 1266.418    0.000 wrapper.py:25(act)
                2479163  124.399    0.000 1259.723    0.001 optimizer.py:167(zero_grad)
               49593260   73.589    0.000 1244.047    0.000 env.py:197(act)
               29751456 1207.122    0.000 1207.122    0.000 {built-in method addmm}
               89249868 1131.568    0.000 1131.568    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               49593260 1121.514    0.000 1125.983    0.000 libenv.py:352(act)
               89249868  947.164    0.000  947.164    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               99545067   80.518    0.000  863.118    0.000 extract_dict_ob.py:9(observe)
               99545067   40.761    0.000  782.600    0.000 wrapper.py:19(observe)
               99545067  195.834    0.000  741.840    0.000 libenv.py:344(observe)
                   4959    1.302    0.000  723.663    0.146 agent.py:101(update_target_network)
                   4959  184.440    0.037  649.845    0.131 memory.py:45(update_distribution)
              406584472  217.819    0.000  601.289    0.000 overrides.py:1073(has_torch_function)
               44624934  581.715    0.000  581.715    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               52082341  556.915    0.000  556.915    0.000 {built-in method numpy.array}
               44624934  537.732    0.000  537.732    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              149138327  163.965    0.000  534.435    0.000 libenv.py:281(_maybe_copy_dict)
              368748733  523.928    0.000  523.928    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               44624934  510.605    0.000  510.605    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               39669777  480.272    0.000  507.874    0.000 module.py:781(__setattr__)
              447419940  470.023    0.000  470.023    0.000 {method 'copy' of 'numpy.ndarray' objects}
               44624934  454.268    0.000  454.268    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               49593260   43.276    0.000  395.871    0.000 wrapper.py:22(get_info)
                7438989   12.981    0.000  382.837    0.000 functional.py:74(split)
                2479163  283.162    0.000  375.449    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                9917152   21.127    0.000  370.199    0.000 pooling.py:152(forward)
                7438989   32.715    0.000  368.928    0.000 tensor.py:460(split)
              441294278  148.743    0.000  366.301    0.000 {built-in method builtins.any}
               49593260  185.095    0.000  352.595    0.000 libenv.py:363(get_info)
                9917152   17.039    0.000  349.073    0.000 _jit_internal.py:257(fn)
               49593260  341.897    0.000  341.897    0.000 memory.py:17(inner)
               44624934  341.169    0.000  341.169    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7438989  334.590    0.000  334.590    0.000 {function Tensor.split at 0x7f5fef4faca0}
                9917152   18.109    0.000  330.398    0.000 functional.py:574(_max_pool2d)
               49593260  316.273    0.000  316.273    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9917152  311.174    0.000  311.174    0.000 {built-in method max_pool2d}
               29751456  298.532    0.000  298.532    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9917152  254.606    0.000  254.606    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
               39668620  223.612    0.000  250.576    0.000 __init__.py:67(is_acceptable)
                2479663   33.019    0.000  242.810    0.000 environments.py:76(<listcomp>)
              842920400  170.765    0.000  215.178    0.000 overrides.py:1086(<genexpr>)
               49593280   32.538    0.000  209.805    0.000 environments.py:79(reset)
               24792630  197.652    0.000  197.652    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2479163  191.878    0.000  191.878    0.000 memory.py:43(<listcomp>)
                2479163    7.282    0.000  188.815    0.000 loss.py:445(forward)
                2479163   20.309    0.000  181.533    0.000 functional.py:2637(mse_loss)
                2479663   17.479    0.000  174.010    0.000 collector.py:7(collect)
              250407963  172.616    0.000  172.616    0.000 {built-in method torch._C._get_tracing_state}
              238260010  170.682    0.000  170.819    0.000 module.py:765(__getattr__)
              199090134   51.691    0.000  163.021    0.000 libenv.py:271(_maybe_copy_ndarray)
                4958326  156.502    0.000  156.502    0.000 {built-in method gather}
                4959327  155.525    0.000  155.526    0.000 {built-in method builtins.sum}
               44625108   58.371    0.000  123.635    0.000 tensor.py:596(__hash__)
                2479163  112.593    0.000  112.593    0.000 {built-in method torch._C._nn.mse_loss}
             1041300460   94.861    0.000   94.861    0.000 {method 'values' of 'collections.OrderedDict' objects}
                9917155   33.544    0.000   91.817    0.000 __init__.py:246(__init__)
                9917152   27.304    0.000   87.677    0.000 rnn.py:529(check_forward_args)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8447010: <greedybigfish_0> in cluster <dcc> Done

Job <greedybigfish_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 13:03:44 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Nov 27 14:40:33 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 14:40:33 2020
Terminated at Sat Nov 28 13:36:02 2020
Results reported at Sat Nov 28 13:36:02 2020

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

    CPU time :                                   85112.00 sec.
    Max Memory :                                 57015 MB
    Average Memory :                             56288.29 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4425.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82529 sec.
    Turnaround time :                            88338 sec.

The output (if any) is above this job summary.

