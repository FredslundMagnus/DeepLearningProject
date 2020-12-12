
    Name :                      CHASER_U_S_0.1_0returnchaser-0
    Discount :                  0.995
    Environment :               chaser
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


      13931042371 function calls (13701088321 primitive calls) in 82515.40 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82515.400 82515.400 {built-in method builtins.exec}
                      1    0.025    0.025 82515.400 82515.400 <string>:1(<module>)
                      1  502.617  502.617 82515.373 82515.373 main.py:92(main)
                2340161  246.764    0.000 56318.237    0.024 agent.py:84(learn)
                2247207  946.282    0.000 55529.954    0.025 agent.py:99(TD_learn)
                2247207  154.488    0.000 24480.887    0.011 memory.py:35(sample_distribution)
                2247207  248.642    0.000 23747.614    0.011 helpers.py:15(stack)
        245771832/15824402 1066.804    0.000 16631.070    0.001 module.py:715(_call_impl)
                6834575  227.077    0.000 15378.314    0.002 agent.py:231(forward)
               22752039 12304.309    0.001 12304.368    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20503725 10837.484    0.001 10837.484    0.001 {built-in method cat}
               36421081  303.214    0.000 10754.021    0.000 container.py:115(forward)
                6741621   43.827    0.000 9629.461    0.001 grad_mode.py:23(decorate_context)
                6741621  284.583    0.000 9510.808    0.001 adam.py:55(step)
                2340161   63.363    0.000 9267.637    0.004 environments.py:83(step)
                2340161  216.532    0.000 8888.543    0.004 agent.py:70(chooseMulti)
                6741621 1768.260    0.000 8173.100    0.001 functional.py:53(adam)
                2248206   96.033    0.000 7360.145    0.003 agent.py:58(rememberMulti)
                2248206  299.455    0.000 6883.961    0.003 agent.py:62(<listcomp>)
              305382101 6675.015    0.000 6675.015    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6741621   50.503    0.000 6394.858    0.001 tensor.py:181(backward)
                6741621   29.592    0.000 6344.356    0.001 __init__.py:68(backward)
                6741621 6131.990    0.001 6131.990    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2340161   67.380    0.000 5857.629    0.003 environments.py:85(<listcomp>)
               47099697 1349.929    0.000 5831.884    0.000 helpers.py:8(clean)
               53841318 5062.828    0.000 5062.828    0.000 {built-in method as_tensor}
               41007450   75.870    0.000 3937.204    0.000 conv.py:422(forward)
               41007450   84.408    0.000 3828.417    0.000 conv.py:414(_conv_forward)
               41007450 3729.287    0.000 3729.287    0.000 {built-in method conv2d}
               54586643  122.739    0.000 3414.142    0.000 linear.py:92(forward)
               54586643  322.931    0.000 3237.170    0.000 functional.py:1669(linear)
                2340161   51.156    0.000 3110.328    0.001 environments.py:84(<listcomp>)
               46803220  186.696    0.000 3059.173    0.000 interop.py:274(step)
                6834581  433.338    0.000 2628.070    0.000 rnn.py:110(flatten_parameters)
              471913578 1238.547    0.000 1957.717    0.000 tensor.py:933(grad)
               47842025 1910.800    0.000 1910.800    0.000 {built-in method addmm}
                6741621  184.283    0.000 1884.250    0.000 optimizer.py:167(zero_grad)
                2248206  107.476    0.000 1859.445    0.001 agent.py:82(<listcomp>)
                6834575   81.793    0.000 1806.129    0.000 rnn.py:555(forward)
               86511312   75.568    0.000 1786.024    0.000 activation.py:713(forward)
              134832420 1746.001    0.000 1746.001    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               86511312  113.996    0.000 1710.456    0.000 functional.py:1292(leaky_relu)
                6834578 1695.043    0.000 1695.043    0.000 {built-in method _cudnn_rnn_flatten_weight}
                6834575 1629.669    0.000 1629.669    0.000 {built-in method lstm}
               86511312 1586.261    0.000 1586.261    0.000 {built-in method torch._C._nn.leaky_relu}
               46803220   21.582    0.000 1532.874    0.000 wrapper.py:25(act)
               46803220   68.581    0.000 1511.292    0.000 env.py:197(act)
              134832420 1451.715    0.000 1451.715    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               44964120  155.966    0.000 1444.514    0.000 exploration.py:34(epsilonGreedy)
               46803220 1395.713    0.000 1400.554    0.000 libenv.py:352(act)
              593916677  336.214    0.000  922.268    0.000 overrides.py:1073(has_torch_function)
               67416210  905.072    0.000  905.072    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67416210  831.327    0.000  831.327    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               93902917   75.323    0.000  819.986    0.000 extract_dict_ob.py:9(observe)
               67416210  762.674    0.000  762.674    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               93902917   38.797    0.000  744.663    0.000 wrapper.py:19(observe)
               93902917  183.164    0.000  705.866    0.000 libenv.py:344(observe)
               67416210  682.164    0.000  682.164    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2248206    6.736    0.000  647.789    0.000 agent.py:249(avoid_similar_state)
              661986586  230.918    0.000  561.039    0.000 {built-in method builtins.any}
              346948769  548.605    0.000  548.605    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                   2340    0.911    0.000  541.520    0.231 agent.py:157(update_target_network)
               54586643  524.491    0.000  524.491    0.000 {method 't' of 'torch._C._TensorBase' objects}
               67416210  519.085    0.000  519.085    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              140706137  145.571    0.000  506.074    0.000 libenv.py:281(_maybe_copy_dict)
                6741621   14.208    0.000  455.706    0.000 loss.py:445(forward)
              422120751  450.775    0.000  450.775    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6741621   46.568    0.000  441.498    0.000 functional.py:2637(mse_loss)
               11273420  157.533    0.000  399.464    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7020483   13.337    0.000  386.593    0.000 functional.py:74(split)
               31834549  354.708    0.000  381.468    0.000 module.py:781(__setattr__)
               13483242  373.757    0.000  373.757    0.000 {built-in method gather}
                7020483   32.423    0.000  372.375    0.000 tensor.py:460(split)
               46803220   42.036    0.000  370.639    0.000 wrapper.py:22(get_info)
                7020483  338.284    0.000  338.284    0.000 {function Tensor.split at 0x7f6b3cbfcd30}
               52057577  333.653    0.000  333.653    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               46803220  174.594    0.000  328.604    0.000 libenv.py:363(get_info)
             1242419997  259.660    0.000  325.236    0.000 overrides.py:1086(<genexpr>)
               44964120  321.255    0.000  321.255    0.000 memory.py:17(inner)
                2247207  246.182    0.000  320.046    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               46803220  318.695    0.000  318.695    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               49055107  291.748    0.000  291.748    0.000 {built-in method numpy.array}
                   2340   82.188    0.035  286.574    0.122 memory.py:45(update_distribution)
                2248206  280.297    0.000  285.652    0.000 agent.py:149(convert_values)
               24794187   24.532    0.000  284.029    0.000 <__array_function__ internals>:2(prod)
                6741621  279.362    0.000  279.362    0.000 {built-in method torch._C._nn.mse_loss}
                6834575   21.245    0.000  270.104    0.000 pooling.py:152(forward)
               24794227   18.620    0.000  255.230    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6834575   12.071    0.000  248.859    0.000 _jit_internal.py:257(fn)
                6744618  238.443    0.000  238.443    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               24794187   30.915    0.000  236.611    0.000 fromnumeric.py:2881(prod)
                2340161   29.066    0.000  236.317    0.000 environments.py:86(<listcomp>)
                6834575   14.016    0.000  235.579    0.000 functional.py:574(_max_pool2d)
                   4680  202.175    0.043  229.270    0.049 {built-in method _pickle.loads}
                6834575  220.805    0.000  220.805    0.000 {built-in method max_pool2d}
               13484241  219.266    0.000  219.266    0.000 {method 'type' of 'torch._C._TensorBase' objects}
               27338312  187.623    0.000  208.895    0.000 __init__.py:67(is_acceptable)
               46803240   34.408    0.000  207.255    0.000 environments.py:89(reset)
               24794187   56.568    0.000  205.695    0.000 fromnumeric.py:70(_wrapreduction)
                2426044  198.382    0.000  198.382    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8557113: <CHASER_U_S_0.1_0returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0.1_0returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:11 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Dec 11 15:08:12 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 11 15:08:12 2020
Terminated at Sat Dec 12 14:03:34 2020
Results reported at Sat Dec 12 14:03:34 2020

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

    CPU time :                                   83938.00 sec.
    Max Memory :                                 55072 MB
    Average Memory :                             54373.75 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6368.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82521 sec.
    Turnaround time :                            82523 sec.

The output (if any) is above this job summary.

