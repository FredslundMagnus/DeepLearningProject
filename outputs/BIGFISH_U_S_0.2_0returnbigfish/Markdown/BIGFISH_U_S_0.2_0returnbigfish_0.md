[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0.2_0returnbigfish-0
    Discount :                  0.995
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
    Uncertainty weight :        0.2
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11169369140 function calls (10911864611 primitive calls) in 82524.60 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82524.604 82524.604 {built-in method builtins.exec}
                      1    0.052    0.052 82524.604 82524.604 <string>:1(<module>)
                      1  556.630  556.630 82524.551 82524.551 main.py:92(main)
                2621132  271.410    0.000 52955.481    0.020 agent.py:84(learn)
                2516184  806.723    0.000 52057.709    0.021 agent.py:99(TD_learn)
                2516184  176.838    0.000 27406.593    0.011 memory.py:35(sample_distribution)
                2516184  287.590    0.000 26580.220    0.011 helpers.py:15(stack)
        275217150/17719235 1154.948    0.000 15031.501    0.001 module.py:710(_call_impl)
                7653500  223.026    0.000 13883.880    0.002 agent.py:231(forward)
               25477791 13856.706    0.001 13856.751    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2621132  188.329    0.000 13562.676    0.005 agent.py:70(chooseMulti)
               22960500 12221.363    0.001 12221.363    0.001 {built-in method cat}
              343017572 11718.056    0.000 11718.056    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               40784683  283.143    0.000 9528.238    0.000 container.py:115(forward)
                2621132   73.077    0.000 8625.276    0.003 environments.py:83(step)
                2517183   87.812    0.000 7249.995    0.003 agent.py:82(<listcomp>)
               50343660  133.917    0.000 6946.443    0.000 exploration.py:34(epsilonGreedy)
                2517183   91.317    0.000 6619.425    0.003 agent.py:58(rememberMulti)
                7548552   39.939    0.000 6600.920    0.001 grad_mode.py:12(decorate_context)
                7548552 1661.504    0.000 6511.014    0.001 adam.py:51(step)
                2517183  213.024    0.000 6156.941    0.002 agent.py:62(<listcomp>)
                7548552   32.879    0.000 5554.433    0.001 tensor.py:155(backward)
                7548552   39.045    0.000 5521.554    0.001 __init__.py:57(backward)
                2621132   61.406    0.000 5469.232    0.002 environments.py:85(<listcomp>)
               52636914 1438.283    0.000 5433.912    0.000 helpers.py:8(clean)
                7548552 5320.904    0.001 5320.904    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               60185466 4559.966    0.000 4559.966    0.000 {built-in method as_tensor}
               45921000   80.349    0.000 3545.402    0.000 conv.py:418(forward)
               45921000   94.135    0.000 3425.703    0.000 conv.py:410(_conv_forward)
               45921000 3315.288    0.000 3315.288    0.000 {built-in method conv2d}
               61126049  121.443    0.000 2893.240    0.000 linear.py:90(forward)
                2621132   52.338    0.000 2888.642    0.001 environments.py:84(<listcomp>)
               52422640  193.201    0.000 2836.304    0.000 interop.py:274(step)
               61126049  313.606    0.000 2710.352    0.000 functional.py:1655(linear)
                7653506  390.705    0.000 2161.378    0.000 rnn.py:109(flatten_parameters)
                7653500   90.300    0.000 1892.690    0.000 rnn.py:550(forward)
                7653500 1698.906    0.000 1698.906    0.000 {built-in method lstm}
               53574500 1589.169    0.000 1589.169    0.000 {built-in method addmm}
               96876366   83.405    0.000 1479.719    0.000 activation.py:653(forward)
               96876366  129.194    0.000 1396.314    0.000 functional.py:1277(leaky_relu)
                7653503 1284.184    0.000 1284.184    0.000 {built-in method _cudnn_rnn_flatten_weight}
               96876366 1253.943    0.000 1253.943    0.000 {built-in method torch._C._nn.leaky_relu}
               52422640   23.663    0.000 1230.938    0.000 wrapper.py:25(act)
              150971040 1216.661    0.000 1216.661    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52422640   64.205    0.000 1207.275    0.000 env.py:197(act)
               52422640 1105.598    0.000 1110.491    0.000 libenv.py:352(act)
              150971040 1068.584    0.000 1068.584    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              105059554   77.162    0.000  864.948    0.000 extract_dict_ob.py:9(observe)
              105059554   45.152    0.000  787.785    0.000 wrapper.py:19(observe)
               75485520  745.814    0.000  745.814    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              105059554  195.323    0.000  742.633    0.000 libenv.py:344(observe)
                   2621    1.008    0.000  626.363    0.239 agent.py:157(update_target_network)
                7548552  107.986    0.000  616.277    0.000 optimizer.py:166(zero_grad)
               75485520  614.550    0.000  614.550    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              157482194  162.336    0.000  545.123    0.000 libenv.py:281(_maybe_copy_dict)
                2517183    6.093    0.000  544.892    0.000 agent.py:249(avoid_similar_state)
               75485520  499.887    0.000  499.887    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75485520  482.591    0.000  482.591    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              472449203  468.132    0.000  468.132    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7548552   15.592    0.000  444.157    0.000 loss.py:444(forward)
                7548552   59.831    0.000  428.565    0.000 functional.py:2621(mse_loss)
              389836997  420.655    0.000  420.655    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               35648203  384.267    0.000  412.833    0.000 module.py:774(__setattr__)
               52422640   43.371    0.000  391.225    0.000 wrapper.py:22(get_info)
               11542697  148.977    0.000  379.877    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               61126049  373.168    0.000  373.168    0.000 {method 't' of 'torch._C._TensorBase' objects}
               50343660  364.709    0.000  364.709    0.000 memory.py:17(inner)
                2516184  269.240    0.000  349.372    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               75485520  348.116    0.000  348.116    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               52422640  182.299    0.000  347.854    0.000 libenv.py:363(get_info)
                   2621   95.165    0.036  339.398    0.129 memory.py:45(update_distribution)
               54944066  330.318    0.000  330.318    0.000 {built-in method numpy.array}
               15097104  304.828    0.000  304.828    0.000 {built-in method gather}
                2517183  213.272    0.000  279.045    0.000 agent.py:149(convert_values)
               25601718   24.393    0.000  275.490    0.000 <__array_function__ internals>:2(prod)
               58292024  262.935    0.000  262.935    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   5242  233.427    0.045  260.587    0.050 {built-in method _pickle.loads}
              377427708  222.185    0.000  259.079    0.000 tensor.py:725(grad)
               25601758   18.658    0.000  247.092    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7863396   13.871    0.000  239.417    0.000 functional.py:68(split)
                7653500   20.654    0.000  238.621    0.000 pooling.py:156(forward)
                7548552  237.101    0.000  237.101    0.000 {built-in method torch._C._nn.mse_loss}
               25601718   31.553    0.000  228.433    0.000 fromnumeric.py:2881(prod)
                7863396   13.711    0.000  224.418    0.000 tensor.py:367(split)
               52422640  223.232    0.000  223.232    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               30614012  198.767    0.000  222.543    0.000 __init__.py:66(is_acceptable)
                2716377  221.580    0.000  221.580    0.000 {built-in method tensor}
                7653500   13.348    0.000  217.967    0.000 _jit_internal.py:237(fn)
                7863396  209.100    0.000  209.100    0.000 {function Tensor.split at 0x7fafc61559d0}
                7653500   15.484    0.000  203.434    0.000 functional.py:564(_max_pool2d)
                2516184  200.041    0.000  200.041    0.000 memory.py:43(<listcomp>)
               25601718   57.935    0.000  196.880    0.000 fromnumeric.py:70(_wrapreduction)
                2621132   28.239    0.000  194.326    0.000 environments.py:86(<listcomp>)
              270396089  192.344    0.000  192.464    0.000 module.py:758(__getattr__)
                7551549  191.855    0.000  191.855    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                7653500  186.944    0.000  186.944    0.000 {built-in method max_pool2d}
                2621132   18.719    0.000  174.676    0.000 collector.py:8(collect)
               15098103  168.236    0.000  168.236    0.000 {method 'type' of 'torch._C._TensorBase' objects}
               52422660   32.634    0.000  166.114    0.000 environments.py:89(reset)
               61126049   42.658    0.000  160.003    0.000 _overrides.py:779(has_torch_function)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8557622: <BIGFISH_U_S_0.2_0returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0.2_0returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:46 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Dec 12 14:57:36 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec 12 14:57:36 2020
Terminated at Sun Dec 13 13:53:10 2020
Results reported at Sun Dec 13 13:53:10 2020

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

    CPU time :                                   86686.00 sec.
    Max Memory :                                 54092 MB
    Average Memory :                             53367.39 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7348.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82535 sec.
    Turnaround time :                            165084 sec.

The output (if any) is above this job summary.

