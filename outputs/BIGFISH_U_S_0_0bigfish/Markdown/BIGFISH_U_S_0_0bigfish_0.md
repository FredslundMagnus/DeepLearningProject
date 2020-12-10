
    Name :                      BIGFISH_U_S_0_0bigfish-0
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14022539651 function calls (13790441841 primitive calls) in 82524.05 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82524.050 82524.050 {built-in method builtins.exec}
                      1    0.070    0.070 82524.050 82524.050 <string>:1(<module>)
                      1  501.653  501.653 82523.980 82523.980 main.py:92(main)
                2362752  192.649    0.000 56447.629    0.024 agent.py:84(learn)
                2267799  781.799    0.000 55687.978    0.025 agent.py:99(TD_learn)
                2267799  157.446    0.000 24941.021    0.011 memory.py:35(sample_distribution)
                2267799  272.656    0.000 24188.451    0.011 helpers.py:15(stack)
        248061735/15970545 1079.596    0.000 16667.852    0.001 module.py:715(_call_impl)
                6898350  228.116    0.000 15412.941    0.002 agent.py:216(forward)
               22963956 12433.273    0.001 12433.323    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20695050 11143.623    0.001 11143.623    0.001 {built-in method cat}
               36760548  298.904    0.000 10787.814    0.000 container.py:115(forward)
                6803397   44.711    0.000 9674.300    0.001 grad_mode.py:23(decorate_context)
                6803397  281.939    0.000 9555.835    0.001 adam.py:55(step)
                2362752   65.493    0.000 8977.107    0.004 environments.py:83(step)
                2362752  217.978    0.000 8923.089    0.004 agent.py:70(chooseMulti)
                6803397 1769.601    0.000 8209.772    0.001 functional.py:53(adam)
                2268798   99.713    0.000 7482.687    0.003 agent.py:58(rememberMulti)
                2268798  298.029    0.000 7005.892    0.003 agent.py:62(<listcomp>)
              308225979 6885.281    0.000 6885.281    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6803397   49.629    0.000 6446.452    0.001 tensor.py:181(backward)
                6803397   31.794    0.000 6396.824    0.001 __init__.py:68(backward)
                6803397 6182.380    0.001 6182.380    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2362752   68.727    0.000 5913.364    0.003 environments.py:85(<listcomp>)
               47422880 1366.555    0.000 5868.221    0.000 helpers.py:8(clean)
               54226277 5068.336    0.000 5068.336    0.000 {built-in method as_tensor}
               41390100   77.409    0.000 3950.013    0.000 conv.py:422(forward)
               41390100   85.037    0.000 3838.286    0.000 conv.py:414(_conv_forward)
               41390100 3739.047    0.000 3739.047    0.000 {built-in method conv2d}
               55094844  118.225    0.000 3440.275    0.000 linear.py:92(forward)
               55094844  321.045    0.000 3266.370    0.000 functional.py:1669(linear)
                2362752   49.036    0.000 2810.750    0.001 environments.py:84(<listcomp>)
               47255040  181.622    0.000 2761.715    0.000 interop.py:274(step)
                6898356  423.165    0.000 2572.570    0.000 rnn.py:110(flatten_parameters)
              476237898 1246.370    0.000 1972.592    0.000 tensor.py:933(grad)
               48288450 1947.185    0.000 1947.185    0.000 {built-in method addmm}
                2268798  103.552    0.000 1933.044    0.001 agent.py:82(<listcomp>)
                6803397  187.140    0.000 1900.738    0.000 optimizer.py:167(zero_grad)
                6898350   84.389    0.000 1852.698    0.000 rnn.py:555(forward)
               87317796   74.961    0.000 1787.858    0.000 activation.py:713(forward)
              136067940 1759.568    0.000 1759.568    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               87317796  112.635    0.000 1712.897    0.000 functional.py:1292(leaky_relu)
                6898350 1673.045    0.000 1673.045    0.000 {built-in method lstm}
                6898353 1660.196    0.000 1660.196    0.000 {built-in method _cudnn_rnn_flatten_weight}
               87317796 1589.670    0.000 1589.670    0.000 {built-in method torch._C._nn.leaky_relu}
               45375960  152.338    0.000 1528.902    0.000 exploration.py:34(epsilonGreedy)
              136067940 1448.189    0.000 1448.189    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               47255040   20.405    0.000 1235.324    0.000 wrapper.py:25(act)
               47255040   72.292    0.000 1214.919    0.000 env.py:197(act)
               47255040 1095.725    0.000 1100.416    0.000 libenv.py:352(act)
              599366958  341.956    0.000  928.990    0.000 overrides.py:1073(has_torch_function)
               68033970  907.841    0.000  907.841    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               68033970  836.506    0.000  836.506    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               94677920   77.130    0.000  819.575    0.000 extract_dict_ob.py:9(observe)
               68033970  770.400    0.000  770.400    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               94677920   37.971    0.000  742.445    0.000 wrapper.py:19(observe)
               94677920  183.562    0.000  704.474    0.000 libenv.py:344(observe)
               68033970  691.714    0.000  691.714    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2268798    6.760    0.000  646.123    0.000 agent.py:234(avoid_similar_state)
                   2362    0.938    0.000  567.002    0.240 agent.py:142(update_target_network)
              668068620  231.991    0.000  564.506    0.000 {built-in method builtins.any}
               68033970  526.423    0.000  526.423    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               55094844  521.595    0.000  521.595    0.000 {method 't' of 'torch._C._TensorBase' objects}
              141932960  149.280    0.000  506.238    0.000 libenv.py:281(_maybe_copy_dict)
              345950344  505.677    0.000  505.677    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                6803397   14.366    0.000  459.578    0.000 loss.py:445(forward)
              425801242  446.845    0.000  446.845    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6803397   47.685    0.000  445.212    0.000 functional.py:2637(mse_loss)
               11291766  161.140    0.000  404.443    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7088256   14.277    0.000  399.468    0.000 functional.py:74(split)
                7088256   31.080    0.000  384.284    0.000 tensor.py:460(split)
               32130833  355.504    0.000  380.277    0.000 module.py:781(__setattr__)
               47255040   42.063    0.000  371.375    0.000 wrapper.py:22(get_info)
                7088256  351.489    0.000  351.489    0.000 {function Tensor.split at 0x7fc30f41bd30}
               45375960  329.835    0.000  329.835    0.000 memory.py:17(inner)
               47255040  175.952    0.000  329.313    0.000 libenv.py:363(get_info)
                2267799  252.441    0.000  327.745    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
             1253828760  261.663    0.000  327.358    0.000 overrides.py:1086(<genexpr>)
               47255040  311.867    0.000  311.867    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                   2362   86.964    0.037  309.079    0.131 memory.py:45(update_distribution)
               49527563  308.766    0.000  308.766    0.000 {built-in method numpy.array}
               24851471   24.373    0.000  285.266    0.000 <__array_function__ internals>:2(prod)
                6803397  281.525    0.000  281.525    0.000 {built-in method torch._C._nn.mse_loss}
               41200194  280.496    0.000  280.496    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2268798  273.369    0.000  274.079    0.000 agent.py:134(convert_values)
                9071196  270.521    0.000  270.521    0.000 {built-in method gather}
                6898350   16.175    0.000  263.130    0.000 pooling.py:152(forward)
               24851511   18.642    0.000  256.793    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6898350   12.834    0.000  246.954    0.000 _jit_internal.py:257(fn)
               24851471   31.593    0.000  238.150    0.000 fromnumeric.py:2881(prod)
                6806394  238.083    0.000  238.083    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6898350   13.084    0.000  232.884    0.000 functional.py:574(_max_pool2d)
                   4724  204.482    0.043  231.738    0.049 {built-in method _pickle.loads}
                6898350  219.007    0.000  219.007    0.000 {built-in method max_pool2d}
               24851471   56.744    0.000  206.557    0.000 fromnumeric.py:70(_wrapreduction)
                2448308  195.648    0.000  195.648    0.000 {built-in method tensor}
               27593412  172.144    0.000  194.596    0.000 __init__.py:67(is_acceptable)
               68034216   89.538    0.000  192.283    0.000 tensor.py:596(__hash__)
                2362752   28.938    0.000  187.500    0.000 environments.py:86(<listcomp>)
                2267799  179.386    0.000  179.386    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8552382: <BIGFISH_U_S_0_0bigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0_0bigfish_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Tue Dec  8 22:26:38 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec  9 01:28:08 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec  9 01:28:08 2020
Terminated at Thu Dec 10 00:23:41 2020
Results reported at Thu Dec 10 00:23:41 2020

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

    CPU time :                                   84176.00 sec.
    Max Memory :                                 54766 MB
    Average Memory :                             54076.27 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6674.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82535 sec.
    Turnaround time :                            93423 sec.

The output (if any) is above this job summary.

