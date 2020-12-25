[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NOPE_final_chaser-0
    Discount :                  0.995
    Environment :               chaser
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


      8171092090 function calls (8000025194 primitive calls) in 64520.56 seconds

##    Ordered by: cumulative time
   List reduced from 1329 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 64520.557 64520.557 {built-in method builtins.exec}
                      1    0.021    0.021 64520.557 64520.557 <string>:1(<module>)
                      1  368.333  368.333 64520.533 64520.533 main.py:91(main)
                2253718  141.482    0.000 39032.907    0.017 agent.py:93(learn)
                2162763  333.696    0.000 38386.995    0.018 agent.py:106(TD_learn)
                2162763  140.610    0.000 21976.838    0.010 memory.py:35(sample_distribution)
                2162763  228.262    0.000 21309.733    0.010 helpers.py:15(stack)
                2253718   43.271    0.000 11572.293    0.005 agent.py:72(chooseMulti)
              293580664 11190.821    0.000 11190.821    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               19737840 11092.473    0.001 11092.525    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        181965114/10904770  749.961    0.000 10164.074    0.001 module.py:710(_call_impl)
                6579244  156.325    0.000 9814.313    0.001 agent.py:235(forward)
               19737732 9787.111    0.000 9787.111    0.000 {built-in method cat}
                2253718   59.674    0.000 8016.363    0.004 environments.py:83(step)
                2163762   78.563    0.000 7308.137    0.003 agent.py:88(<listcomp>)
               43275240  112.292    0.000 7034.723    0.000 exploration.py:34(epsilonGreedy)
               26316976  195.339    0.000 6219.068    0.000 container.py:115(forward)
                2163753    9.219    0.000 5348.307    0.002 agent.py:58(rememberMulti)
                2163753  187.532    0.000 5339.088    0.002 agent.py:63(<listcomp>)
                2253718   57.084    0.000 5015.115    0.002 environments.py:85(<listcomp>)
               45347534 1348.381    0.000 4993.994    0.000 helpers.py:8(clean)
                4325526   22.823    0.000 4480.936    0.001 grad_mode.py:12(decorate_context)
                4325526 1118.393    0.000 4429.184    0.001 adam.py:51(step)
               51835823 4085.409    0.000 4085.409    0.000 {built-in method as_tensor}
                4325526   17.535    0.000 3803.964    0.001 tensor.py:155(backward)
                4325526   23.523    0.000 3786.428    0.001 __init__.py:57(backward)
                4325526 3670.949    0.001 3670.949    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               39475464   70.125    0.000 2923.166    0.000 conv.py:418(forward)
               39475464   72.993    0.000 2824.640    0.000 conv.py:410(_conv_forward)
                2253718   45.125    0.000 2742.278    0.001 environments.py:84(<listcomp>)
               39475464 2738.118    0.000 2738.118    0.000 {built-in method conv2d}
               45074360  168.561    0.000 2697.153    0.000 interop.py:274(step)
                6579250  291.382    0.000 1625.673    0.000 rnn.py:109(flatten_parameters)
                6579244   66.702    0.000 1405.664    0.000 rnn.py:550(forward)
               45074360   22.193    0.000 1351.325    0.000 wrapper.py:25(act)
               45074360   60.311    0.000 1329.132    0.000 env.py:197(act)
                6579244 1258.554    0.000 1258.554    0.000 {built-in method lstm}
               45074360 1234.712    0.000 1239.298    0.000 libenv.py:352(act)
               26316976   55.233    0.000 1206.938    0.000 linear.py:90(forward)
               26316976   98.025    0.000 1124.655    0.000 functional.py:1655(linear)
                6579247 1002.742    0.000 1002.742    0.000 {built-in method _cudnn_rnn_flatten_weight}
               65792440   58.950    0.000  998.995    0.000 activation.py:653(forward)
               65792440   87.703    0.000  940.045    0.000 functional.py:1277(leaky_relu)
               65792440  843.391    0.000  843.391    0.000 {built-in method torch._C._nn.leaky_relu}
              103812624  824.992    0.000  824.992    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               26316976  758.295    0.000  758.295    0.000 {built-in method addmm}
              103812624  723.959    0.000  723.959    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               90421894   71.401    0.000  714.592    0.000 extract_dict_ob.py:9(observe)
               90421894   39.272    0.000  643.192    0.000 wrapper.py:19(observe)
               90421894  161.935    0.000  603.920    0.000 libenv.py:344(observe)
               51906312  512.046    0.000  512.046    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   2208    0.814    0.000  504.429    0.228 agent.py:161(update_target_network)
              135496254  139.811    0.000  439.298    0.000 libenv.py:281(_maybe_copy_dict)
               51906312  423.439    0.000  423.439    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4325526   71.313    0.000  420.056    0.000 optimizer.py:166(zero_grad)
              406490970  369.383    0.000  369.383    0.000 {method 'copy' of 'numpy.ndarray' objects}
              324930785  351.534    0.000  351.534    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               51906312  348.581    0.000  348.581    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11187420  126.622    0.000  334.723    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               45074360   33.568    0.000  329.230    0.000 wrapper.py:22(get_info)
               51906312  326.879    0.000  326.879    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               43275060  314.405    0.000  314.405    0.000 memory.py:17(inner)
               45074360  153.774    0.000  295.663    0.000 libenv.py:363(get_info)
               30644337  260.832    0.000  280.976    0.000 module.py:774(__setattr__)
                2162763  217.292    0.000  280.974    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               47241539  267.802    0.000  267.802    0.000 {built-in method numpy.array}
                   2208   75.196    0.034  267.184    0.121 memory.py:45(update_distribution)
                4325526    8.639    0.000  245.580    0.000 loss.py:444(forward)
               24537743   20.958    0.000  242.936    0.000 <__array_function__ internals>:2(prod)
               51906312  241.126    0.000  241.126    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4325526   32.009    0.000  236.941    0.000 functional.py:2621(mse_loss)
               24537783   18.179    0.000  218.146    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                2163762  148.514    0.000  214.757    0.000 agent.py:152(convert_values)
                   4416  191.948    0.043  214.655    0.049 {built-in method _pickle.loads}
               45074360  201.707    0.000  201.707    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24537743   27.814    0.000  199.967    0.000 fromnumeric.py:2881(prod)
                2253718   24.498    0.000  199.296    0.000 environments.py:86(<listcomp>)
                6761154   11.431    0.000  197.823    0.000 functional.py:68(split)
                6761154   11.135    0.000  185.418    0.000 tensor.py:367(split)
                6579244   13.422    0.000  182.652    0.000 pooling.py:156(forward)
              259531668  151.321    0.000  175.524    0.000 tensor.py:725(grad)
               45074380   30.347    0.000  174.807    0.000 environments.py:89(reset)
                6761154  172.921    0.000  172.921    0.000 {function Tensor.split at 0x7f83d4098a60}
               24537743   52.204    0.000  172.154    0.000 fromnumeric.py:70(_wrapreduction)
                6579244   10.319    0.000  169.230    0.000 _jit_internal.py:237(fn)
                2162763  166.245    0.000  166.245    0.000 memory.py:43(<listcomp>)
                8651052  161.628    0.000  161.628    0.000 {built-in method gather}
               26316976  157.863    0.000  157.863    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6579244   11.779    0.000  157.819    0.000 functional.py:564(_max_pool2d)
                2253718   16.642    0.000  157.023    0.000 collector.py:8(collect)
               26316988  136.496    0.000  153.284    0.000 __init__.py:66(is_acceptable)
                6579244  145.124    0.000  145.124    0.000 {built-in method max_pool2d}
               30551547  141.837    0.000  141.837    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                4507437  139.344    0.000  139.344    0.000 {built-in method builtins.sum}
                4325526  133.050    0.000  133.050    0.000 {built-in method torch._C._nn.mse_loss}
              180843788   47.353    0.000  128.691    0.000 libenv.py:271(_maybe_copy_ndarray)
               26702714  121.806    0.000  121.806    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              171237611  116.148    0.000  116.250    0.000 module.py:758(__getattr__)
              181965114  106.146    0.000  106.146    0.000 {built-in method torch._C._get_tracing_state}
                4325526   21.382    0.000   90.413    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8585236: <NOPE_final_chaser_0> in cluster <dcc> Done

Job <NOPE_final_chaser_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Dec 23 17:42:09 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Dec 24 11:37:41 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec 24 11:37:41 2020
Terminated at Fri Dec 25 05:33:07 2020
Results reported at Fri Dec 25 05:33:07 2020

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

    CPU time :                                   69654.00 sec.
    Max Memory :                                 56080 MB
    Average Memory :                             55446.05 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5360.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64631 sec.
    Turnaround time :                            129058 sec.

The output (if any) is above this job summary.

