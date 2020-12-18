
    Name :                      MAZE_U_S_0.1_0returnmaze-0
    Discount :                  0.99
    Environment :               maze
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
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13888421057 function calls (13659121386 primitive calls) in 82513.91 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82513.909 82513.909 {built-in method builtins.exec}
                      1    0.104    0.104 82513.909 82513.909 <string>:1(<module>)
                      1  496.401  496.401 82513.803 82513.803 main.py:92(main)
                2333682  245.389    0.000 56446.199    0.024 agent.py:84(learn)
                2240728  951.552    0.000 55658.679    0.025 agent.py:99(TD_learn)
                2240728  154.099    0.000 24552.113    0.011 memory.py:35(sample_distribution)
                2240728  258.369    0.000 23796.289    0.011 helpers.py:15(stack)
        245072100/15779049 1059.309    0.000 16627.359    0.001 module.py:715(_call_impl)
                6815138  215.553    0.000 15380.597    0.002 agent.py:231(forward)
               22687249 12223.629    0.001 12223.630    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20445414 10955.659    0.001 10955.659    0.001 {built-in method cat}
               36317417  298.521    0.000 10740.618    0.000 container.py:115(forward)
                6722184   45.907    0.000 9558.815    0.001 grad_mode.py:23(decorate_context)
                6722184  279.345    0.000 9439.196    0.001 adam.py:55(step)
                2333682   65.525    0.000 9166.872    0.004 environments.py:83(step)
                2333682  213.432    0.000 8833.786    0.004 agent.py:70(chooseMulti)
                6722184 1752.103    0.000 8130.870    0.001 functional.py:53(adam)
                2241727   96.114    0.000 7386.940    0.003 agent.py:58(rememberMulti)
                2241727  286.406    0.000 6908.254    0.003 agent.py:62(<listcomp>)
              304484158 6754.418    0.000 6754.418    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6722184   49.500    0.000 6457.187    0.001 tensor.py:181(backward)
                6722184   30.798    0.000 6407.687    0.001 __init__.py:68(backward)
                6722184 6193.150    0.001 6193.150    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2333682   67.488    0.000 5816.434    0.002 environments.py:85(<listcomp>)
               46806468 1347.729    0.000 5767.609    0.000 helpers.py:8(clean)
               53528652 4995.695    0.000 4995.695    0.000 {built-in method as_tensor}
               40890828   72.688    0.000 3956.134    0.000 conv.py:422(forward)
               40890828   80.904    0.000 3850.873    0.000 conv.py:414(_conv_forward)
               40890828 3754.227    0.000 3754.227    0.000 {built-in method conv2d}
               54431147  118.122    0.000 3404.153    0.000 linear.py:92(forward)
               54431147  317.218    0.000 3230.026    0.000 functional.py:1669(linear)
                2333682   51.019    0.000 3102.445    0.001 environments.py:84(<listcomp>)
               46673640  181.222    0.000 3051.427    0.000 interop.py:274(step)
                6815144  430.664    0.000 2628.758    0.000 rnn.py:110(flatten_parameters)
               47705966 1924.187    0.000 1924.187    0.000 {built-in method addmm}
              470552988 1201.019    0.000 1905.044    0.000 tensor.py:933(grad)
                2241727  103.171    0.000 1902.850    0.001 agent.py:82(<listcomp>)
                6722184  181.364    0.000 1851.707    0.000 optimizer.py:167(zero_grad)
                6815138   82.090    0.000 1830.614    0.000 rnn.py:555(forward)
               86265110   76.276    0.000 1783.346    0.000 activation.py:713(forward)
              134443680 1732.512    0.000 1732.512    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               86265110  111.322    0.000 1707.070    0.000 functional.py:1292(leaky_relu)
                6815141 1703.677    0.000 1703.677    0.000 {built-in method _cudnn_rnn_flatten_weight}
                6815138 1656.920    0.000 1656.920    0.000 {built-in method lstm}
               86265110 1585.830    0.000 1585.830    0.000 {built-in method torch._C._nn.leaky_relu}
               46673640   21.302    0.000 1532.236    0.000 wrapper.py:25(act)
               46673640   68.248    0.000 1510.933    0.000 env.py:197(act)
               44834540  150.997    0.000 1497.289    0.000 exploration.py:34(epsilonGreedy)
              134443680 1443.143    0.000 1443.143    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               46673640 1397.382    0.000 1401.534    0.000 libenv.py:352(act)
              592206221  328.345    0.000  904.154    0.000 overrides.py:1073(has_torch_function)
               67221840  901.900    0.000  901.900    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67221840  828.400    0.000  828.400    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               93480108   74.741    0.000  816.017    0.000 extract_dict_ob.py:9(observe)
               67221840  760.800    0.000  760.800    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               93480108   38.981    0.000  741.276    0.000 wrapper.py:19(observe)
               93480108  190.739    0.000  702.295    0.000 libenv.py:344(observe)
               67221840  688.258    0.000  688.258    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2241727    6.266    0.000  637.011    0.000 agent.py:249(avoid_similar_state)
              660081760  228.539    0.000  554.061    0.000 {built-in method builtins.any}
                   2333    0.930    0.000  542.132    0.232 agent.py:157(update_target_network)
              346267981  525.935    0.000  525.935    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               67221840  521.674    0.000  521.674    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               54431147  518.017    0.000  518.017    0.000 {method 't' of 'torch._C._TensorBase' objects}
              140153748  146.076    0.000  498.293    0.000 libenv.py:281(_maybe_copy_dict)
                6722184   14.351    0.000  463.524    0.000 loss.py:445(forward)
                6722184   49.086    0.000  449.172    0.000 functional.py:2637(mse_loss)
              420463577  444.695    0.000  444.695    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11264108  166.467    0.000  415.915    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               31743843  360.092    0.000  383.753    0.000 module.py:781(__setattr__)
                7001046   14.180    0.000  380.231    0.000 functional.py:74(split)
               13444368  372.257    0.000  372.257    0.000 {built-in method gather}
               46673640   40.917    0.000  366.810    0.000 wrapper.py:22(get_info)
                7001046   31.340    0.000  365.173    0.000 tensor.py:460(split)
                2240728  262.088    0.000  339.483    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                7001046  332.188    0.000  332.188    0.000 {function Tensor.split at 0x7f45986cfd30}
               51908560  331.487    0.000  331.487    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               44834540  326.438    0.000  326.438    0.000 memory.py:17(inner)
               46673640  172.847    0.000  325.893    0.000 libenv.py:363(get_info)
             1238843589  255.816    0.000  320.731    0.000 overrides.py:1086(<genexpr>)
               46673640  313.729    0.000  313.729    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               48919034  292.990    0.000  292.990    0.000 {built-in method numpy.array}
               24769084   24.275    0.000  292.526    0.000 <__array_function__ internals>:2(prod)
                   2333   81.873    0.035  287.249    0.123 memory.py:45(update_distribution)
                6722184  284.615    0.000  284.615    0.000 {built-in method torch._C._nn.mse_loss}
                2241727  275.442    0.000  282.398    0.000 agent.py:149(convert_values)
                6815138   16.146    0.000  266.948    0.000 pooling.py:152(forward)
               24769124   19.472    0.000  264.215    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6815138   12.144    0.000  250.802    0.000 _jit_internal.py:257(fn)
               24769084   31.171    0.000  244.743    0.000 fromnumeric.py:2881(prod)
                6815138   13.718    0.000  237.583    0.000 functional.py:574(_max_pool2d)
                6725181  236.286    0.000  236.286    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                   4666  202.514    0.043  229.424    0.049 {built-in method _pickle.loads}
                6815138  223.121    0.000  223.121    0.000 {built-in method max_pool2d}
               13445367  219.207    0.000  219.207    0.000 {method 'type' of 'torch._C._TensorBase' objects}
               24769084   56.379    0.000  213.572    0.000 fromnumeric.py:70(_wrapreduction)
                2419033  198.320    0.000  198.320    0.000 {built-in method tensor}
               27260564  172.186    0.000  192.872    0.000 __init__.py:67(is_acceptable)
               67222086   86.396    0.000  187.351    0.000 tensor.py:596(__hash__)
                2333682   28.181    0.000  182.467    0.000 environments.py:86(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8570465: <MAZE_U_S_0.1_0returnmaze_0> in cluster <dcc> Done

Job <MAZE_U_S_0.1_0returnmaze_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Dec 16 20:56:12 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec 16 22:25:05 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 16 22:25:05 2020
Terminated at Thu Dec 17 21:20:22 2020
Results reported at Thu Dec 17 21:20:22 2020

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

    CPU time :                                   84078.00 sec.
    Max Memory :                                 54609 MB
    Average Memory :                             53928.45 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6831.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82519 sec.
    Turnaround time :                            87850 sec.

The output (if any) is above this job summary.

