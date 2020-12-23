
    Name :                      NOPEstarpilot-0
    Discount :                  0.99
    Environment :               starpilot
    Hours :                     12
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
    State difference weight :   0.1
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      10485370227 function calls (10248292793 primitive calls) in 42927.53 seconds

##    Ordered by: cumulative time
   List reduced from 1358 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 42927.526 42927.526 {built-in method builtins.exec}
                      1    0.024    0.024 42927.526 42927.526 <string>:1(<module>)
                      1  216.765  216.765 42927.500 42927.500 main.py:92(main)
                1658075  120.582    0.000 19077.350    0.012 agent.py:89(learn)
                1591108  391.914    0.000 18563.186    0.012 agent.py:102(TD_learn)
        283358520/46287712 1160.040    0.000 14452.006    0.000 module.py:715(_call_impl)
                1658075   38.883    0.000 14441.566    0.009 environments.py:83(step)
               33424915 1570.929    0.000 12528.596    0.000 helpers.py:8(clean)
                1658075   36.312    0.000 12465.672    0.008 environments.py:85(<listcomp>)
               51194970  312.576    0.000 11279.210    0.000 container.py:115(forward)
               81370703  163.932    0.000 6587.636    0.000 conv.py:422(forward)
               81370703  156.262    0.000 6350.043    0.000 conv.py:414(_conv_forward)
               81370703 6164.969    0.000 6164.969    0.000 {built-in method conv2d}
                4840291   96.069    0.000 5657.815    0.001 agent.py:231(forward)
                1591108   92.169    0.000 5558.088    0.003 memory.py:35(sample_distribution)
                1591108  175.883    0.000 5108.744    0.003 helpers.py:15(stack)
                1592098   26.495    0.000 4634.891    0.003 agent.py:58(rememberMulti)
                1592098  173.218    0.000 4499.472    0.003 agent.py:60(<listcomp>)
                1658075  150.777    0.000 4420.468    0.003 agent.py:72(chooseMulti)
              280577309 4361.983    0.000 4361.983    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                4773324   27.034    0.000 4078.367    0.001 grad_mode.py:23(decorate_context)
                4773324  145.513    0.000 4001.746    0.001 adam.py:55(step)
               38198239 3457.649    0.000 3457.649    0.000 {built-in method as_tensor}
                4773324  738.861    0.000 3278.185    0.001 functional.py:53(adam)
               17703089 3193.291    0.000 3193.291    0.000 {built-in method cat}
                4773324   28.235    0.000 2767.859    0.001 tensor.py:181(backward)
                4773324   17.640    0.000 2739.624    0.001 __init__.py:68(backward)
                4773324 2619.237    0.001 2619.237    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              107230231  116.494    0.000 1790.030    0.000 activation.py:713(forward)
                1658075   30.974    0.000 1747.205    0.001 environments.py:84(<listcomp>)
               33161500  112.275    0.000 1716.231    0.000 interop.py:274(step)
              107230231  148.438    0.000 1673.536    0.000 functional.py:1292(leaky_relu)
               19361274 1577.217    0.000 1577.239    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              107230231 1510.927    0.000 1510.927    0.000 {built-in method torch._C._nn.leaky_relu}
               29108710   62.576    0.000 1460.911    0.000 linear.py:92(forward)
               29108710  170.315    0.000 1371.453    0.000 functional.py:1669(linear)
                4840297  225.392    0.000 1205.006    0.000 rnn.py:110(flatten_parameters)
                1658075   58.536    0.000 1097.278    0.001 agent.py:87(<listcomp>)
              267306256  615.585    0.000 1033.093    0.000 tensor.py:933(grad)
                4840291   45.365    0.000 1017.295    0.000 rnn.py:555(forward)
                4840291  916.205    0.000  916.205    0.000 {built-in method lstm}
                4773324   88.621    0.000  890.304    0.000 optimizer.py:167(zero_grad)
               33161500   88.863    0.000  887.402    0.000 exploration.py:34(epsilonGreedy)
               33161500   14.180    0.000  781.286    0.000 wrapper.py:25(act)
                3249182   10.923    0.000  778.977    0.000 agent.py:247(avoid_similar_state)
               33161500   40.089    0.000  767.105    0.000 env.py:197(act)
                4840294  743.700    0.000  743.700    0.000 {built-in method _cudnn_rnn_flatten_weight}
               24134488  738.449    0.000  738.449    0.000 {built-in method addmm}
               33161500  702.337    0.000  705.515    0.000 libenv.py:352(act)
               76373184  670.001    0.000  670.001    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               76373184  560.083    0.000  560.083    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              334601774  179.825    0.000  526.174    0.000 overrides.py:1073(has_torch_function)
               66586415   49.452    0.000  497.845    0.000 extract_dict_ob.py:9(observe)
               66586415   26.861    0.000  448.393    0.000 wrapper.py:19(observe)
               66586415  115.340    0.000  421.533    0.000 libenv.py:344(observe)
                   1625    0.609    0.000  393.582    0.242 agent.py:157(update_target_network)
               38186592  377.258    0.000  377.258    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               38186592  335.500    0.000  335.500    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              373257156  134.322    0.000  333.223    0.000 {built-in method builtins.any}
              344955359  329.102    0.000  329.102    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               38186592  311.768    0.000  311.768    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               99747915   95.541    0.000  298.240    0.000 libenv.py:281(_maybe_copy_dict)
               38186592  272.586    0.000  272.586    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              299245370  253.573    0.000  253.573    0.000 {method 'copy' of 'numpy.ndarray' objects}
               31841960  252.805    0.000  252.805    0.000 memory.py:17(inner)
                4773324    7.763    0.000  252.525    0.000 loss.py:445(forward)
                4773324   27.182    0.000  244.763    0.000 functional.py:2637(mse_loss)
                4974225    7.965    0.000  235.503    0.000 functional.py:74(split)
               33161500   24.945    0.000  230.221    0.000 wrapper.py:22(get_info)
                4974225   19.651    0.000  226.877    0.000 tensor.py:460(split)
                7367730   86.962    0.000  225.853    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                   1625   57.604    0.035  212.480    0.131 memory.py:45(update_distribution)
               34755858  206.782    0.000  206.782    0.000 {built-in method numpy.array}
                4974225  206.048    0.000  206.048    0.000 {function Tensor.split at 0x7fbb06f64d30}
               33161500  108.319    0.000  205.276    0.000 libenv.py:363(get_info)
               38186592  198.083    0.000  198.083    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               29108710  196.538    0.000  196.538    0.000 {method 't' of 'torch._C._TensorBase' objects}
              698312258  154.825    0.000  195.789    0.000 overrides.py:1086(<genexpr>)
                1658075   15.014    0.000  189.806    0.000 environments.py:86(<listcomp>)
                1591108  147.320    0.000  188.709    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
              286542716  178.536    0.000  178.536    0.000 {built-in method torch._C._get_tracing_state}
               33161520   17.664    0.000  174.934    0.000 environments.py:89(reset)
              248540096  164.108    0.000  164.179    0.000 module.py:765(__getattr__)
                   3250  145.479    0.045  163.377    0.050 {built-in method _pickle.loads}
               16326708   14.785    0.000  162.724    0.000 <__array_function__ internals>:2(prod)
                7955540  159.111    0.000  159.111    0.000 {built-in method gather}
               33161500  151.340    0.000  151.340    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                4773324  147.290    0.000  147.290    0.000 {built-in method torch._C._nn.mse_loss}
               16326748   10.991    0.000  145.244    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                1592107  140.507    0.000  142.622    0.000 agent.py:148(convert_values)
                4974222  141.807    0.000  141.807    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               22545229  126.592    0.000  141.089    0.000 module.py:781(__setattr__)
               16326708   18.046    0.000  134.253    0.000 fromnumeric.py:2881(prod)
               28840845  132.424    0.000  132.424    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                1591108  121.209    0.000  121.209    0.000 memory.py:43(<listcomp>)
             1184629050  116.229    0.000  116.229    0.000 {method 'values' of 'collections.OrderedDict' objects}
               16326708   35.162    0.000  116.207    0.000 fromnumeric.py:70(_wrapreduction)
                3184196   13.053    0.000  108.925    0.000 tensor.py:576(__iter__)
                1658075    9.541    0.000  106.810    0.000 collector.py:8(collect)
               38186808   47.245    0.000  105.553    0.000 tensor.py:596(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8582539: <NOPEstarpilot_0> in cluster <dcc> Done

Job <NOPEstarpilot_0> was submitted from host <n-62-30-7> by user <s183914> in cluster <dcc> at Tue Dec 22 15:37:43 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Dec 22 15:37:45 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec 22 15:37:45 2020
Terminated at Wed Dec 23 03:33:24 2020
Results reported at Wed Dec 23 03:33:24 2020

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

    CPU time :                                   43880.00 sec.
    Max Memory :                                 10286 MB
    Average Memory :                             10199.74 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               51154.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   43002 sec.
    Turnaround time :                            42941 sec.

The output (if any) is above this job summary.

