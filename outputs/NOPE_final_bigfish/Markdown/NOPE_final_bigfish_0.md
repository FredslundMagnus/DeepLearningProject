[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/agent.py:156: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  if state_differences is not 0:

    Name :                      NOPE_final_bigfish-0
    Discount :                  0.995
    Environment :               bigfish
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


      7455674269 function calls (7299798289 primitive calls) in 64521.53 seconds

##    Ordered by: cumulative time
   List reduced from 1329 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 64521.529 64521.529 {built-in method builtins.exec}
                      1    0.025    0.025 64521.529 64521.529 <string>:1(<module>)
                      1  442.823  442.823 64521.503 64521.503 main.py:91(main)
                2053632  163.523    0.000 41996.649    0.020 agent.py:93(learn)
                1970673  352.763    0.000 41261.626    0.021 agent.py:106(TD_learn)
                1970673  149.762    0.000 24929.380    0.013 memory.py:35(sample_distribution)
                1970673  278.420    0.000 24235.566    0.012 helpers.py:15(stack)
               17984934 11912.255    0.001 11912.255    0.001 {built-in method cat}
               17985042 11739.567    0.001 11739.579    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        165805752/9936324  749.904    0.000 10293.685    0.001 module.py:710(_call_impl)
                5994978  153.628    0.000 9933.723    0.002 agent.py:235(forward)
                2053632   46.489    0.000 9479.350    0.005 agent.py:72(chooseMulti)
              266715442 9142.286    0.000 9142.286    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2053632   58.436    0.000 7188.448    0.004 environments.py:83(step)
               23979912  187.212    0.000 6100.318    0.000 container.py:115(forward)
                1971672   73.186    0.000 5331.632    0.003 agent.py:88(<listcomp>)
                1971663    9.134    0.000 5245.377    0.003 agent.py:58(rememberMulti)
                1971663  182.881    0.000 5236.243    0.003 agent.py:63(<listcomp>)
               39433440  105.511    0.000 5069.158    0.000 exploration.py:34(epsilonGreedy)
                2053632   48.762    0.000 4567.205    0.002 environments.py:85(<listcomp>)
               41226682 1250.358    0.000 4538.509    0.000 helpers.py:8(clean)
                3941346   22.291    0.000 4184.115    0.001 grad_mode.py:12(decorate_context)
                3941346 1070.291    0.000 4133.789    0.001 adam.py:51(step)
               47138701 3830.808    0.000 3830.808    0.000 {built-in method as_tensor}
                3941346   18.899    0.000 3743.396    0.001 tensor.py:155(backward)
                3941346   24.606    0.000 3724.497    0.001 __init__.py:57(backward)
                3941346 3607.821    0.001 3607.821    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               35969868   65.253    0.000 2884.069    0.000 conv.py:418(forward)
               35969868   76.452    0.000 2787.865    0.000 conv.py:410(_conv_forward)
               35969868 2697.619    0.000 2697.619    0.000 {built-in method conv2d}
                2053632   45.117    0.000 2395.343    0.001 environments.py:84(<listcomp>)
               41072640  160.208    0.000 2350.226    0.000 interop.py:274(step)
                5994984  314.830    0.000 1702.132    0.000 rnn.py:109(flatten_parameters)
                5994978   70.575    0.000 1569.593    0.000 rnn.py:550(forward)
                5994978 1413.198    0.000 1413.198    0.000 {built-in method lstm}
               23979912   51.365    0.000 1180.713    0.000 linear.py:90(forward)
               23979912   95.109    0.000 1102.484    0.000 functional.py:1655(linear)
               41072640   20.837    0.000 1025.285    0.000 wrapper.py:25(act)
               41072640   52.150    0.000 1004.448    0.000 env.py:197(act)
                5994981 1000.550    0.000 1000.550    0.000 {built-in method _cudnn_rnn_flatten_weight}
               59949780   54.085    0.000  964.410    0.000 activation.py:653(forward)
               41072640  919.051    0.000  922.945    0.000 libenv.py:352(act)
               59949780   82.701    0.000  910.325    0.000 functional.py:1277(leaky_relu)
               59949780  819.195    0.000  819.195    0.000 {built-in method torch._C._nn.leaky_relu}
               94592304  767.541    0.000  767.541    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               23979912  745.085    0.000  745.085    0.000 {built-in method addmm}
               82299322   63.116    0.000  710.113    0.000 extract_dict_ob.py:9(observe)
               94592304  671.418    0.000  671.418    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               82299322   36.831    0.000  646.996    0.000 wrapper.py:19(observe)
               82299322  153.576    0.000  610.165    0.000 libenv.py:344(observe)
                   2012    0.994    0.000  571.500    0.284 agent.py:161(update_target_network)
               47296152  471.493    0.000  471.493    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              123371962  136.560    0.000  459.709    0.000 libenv.py:281(_maybe_copy_dict)
              370117898  393.415    0.000  393.415    0.000 {method 'copy' of 'numpy.ndarray' objects}
                3941346   67.878    0.000  386.800    0.000 optimizer.py:166(zero_grad)
               47296152  384.107    0.000  384.107    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               10996272  136.684    0.000  356.280    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               27923093  316.920    0.000  338.277    0.000 module.py:774(__setattr__)
              295470825  329.679    0.000  329.679    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               41072640   34.806    0.000  327.767    0.000 wrapper.py:22(get_info)
               47296152  321.618    0.000  321.618    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   2012   78.704    0.039  317.175    0.158 memory.py:45(update_distribution)
               43047337  309.022    0.000  309.022    0.000 {built-in method numpy.array}
               47296152  307.336    0.000  307.336    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               41072640  152.310    0.000  292.961    0.000 libenv.py:363(get_info)
                1970673  220.447    0.000  287.691    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               39433260  286.161    0.000  286.161    0.000 memory.py:17(inner)
               23963357   23.445    0.000  257.953    0.000 <__array_function__ internals>:2(prod)
                3941346    8.911    0.000  249.150    0.000 loss.py:444(forward)
                3941346   36.730    0.000  240.239    0.000 functional.py:2621(mse_loss)
                   4024  210.730    0.052  232.447    0.058 {built-in method _pickle.loads}
               23963397   18.128    0.000  230.403    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               47296152  219.966    0.000  219.966    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               23963357   29.009    0.000  212.274    0.000 fromnumeric.py:2881(prod)
                6160896   10.920    0.000  210.996    0.000 functional.py:68(split)
                6160896   11.078    0.000  199.279    0.000 tensor.py:367(split)
               41072640  196.446    0.000  196.446    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                5994978   17.294    0.000  196.040    0.000 pooling.py:156(forward)
                1971672  143.679    0.000  190.251    0.000 agent.py:152(convert_values)
                6160896  186.982    0.000  186.982    0.000 {function Tensor.split at 0x7f23a93f29d0}
               23963357   54.531    0.000  183.265    0.000 fromnumeric.py:70(_wrapreduction)
                5994978   11.592    0.000  178.746    0.000 _jit_internal.py:237(fn)
                1970673  174.514    0.000  174.514    0.000 memory.py:43(<listcomp>)
               23979924  154.204    0.000  172.059    0.000 __init__.py:66(is_acceptable)
                2053632   22.916    0.000  167.464    0.000 environments.py:86(<listcomp>)
                5994978   12.278    0.000  166.068    0.000 functional.py:564(_max_pool2d)
                7882692  163.612    0.000  163.612    0.000 {built-in method gather}
              236480868  139.033    0.000  161.140    0.000 tensor.py:725(grad)
               23979912  159.124    0.000  159.124    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5994978  152.958    0.000  152.958    0.000 {built-in method max_pool2d}
               41072660   29.497    0.000  144.561    0.000 environments.py:89(reset)
                2053632   15.597    0.000  143.061    0.000 collector.py:8(collect)
               27838299  139.608    0.000  139.608    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                3941346  132.964    0.000  132.964    0.000 {built-in method torch._C._nn.mse_loss}
               25936042  130.177    0.000  130.177    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                4107265  126.485    0.000  126.485    0.000 {built-in method builtins.sum}
              164598644   43.656    0.000  124.148    0.000 libenv.py:271(_maybe_copy_ndarray)
              156031015  118.298    0.000  118.388    0.000 module.py:758(__getattr__)
              165805752  100.093    0.000  100.093    0.000 {built-in method torch._C._get_tracing_state}
                3941346   24.035    0.000   90.754    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8585234: <NOPE_final_bigfish_0> in cluster <dcc> Done

Job <NOPE_final_bigfish_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Dec 23 17:42:08 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Dec 23 17:42:10 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 23 17:42:10 2020
Terminated at Thu Dec 24 11:37:41 2020
Results reported at Thu Dec 24 11:37:41 2020

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

    CPU time :                                   68128.00 sec.
    Max Memory :                                 55675 MB
    Average Memory :                             54768.43 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5765.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64623 sec.
    Turnaround time :                            64533 sec.

The output (if any) is above this job summary.

