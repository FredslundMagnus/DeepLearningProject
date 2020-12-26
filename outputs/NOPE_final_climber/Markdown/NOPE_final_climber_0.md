[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NOPE_final_climber-0
    Discount :                  0.995
    Environment :               climber
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


      7802095092 function calls (7638801572 primitive calls) in 64522.78 seconds

##    Ordered by: cumulative time
   List reduced from 1329 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 64522.777 64522.777 {built-in method builtins.exec}
                      1    0.021    0.021 64522.777 64522.777 <string>:1(<module>)
                      1  426.253  426.253 64522.755 64522.755 main.py:91(main)
                2151394  157.379    0.000 40683.610    0.019 agent.py:93(learn)
                2064437  363.848    0.000 40024.818    0.019 agent.py:106(TD_learn)
                2064437  149.144    0.000 23061.469    0.011 memory.py:35(sample_distribution)
                2064437  273.880    0.000 22374.384    0.011 helpers.py:15(stack)
               18840912 11211.068    0.001 11211.088    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2151394   46.468    0.000 10778.127    0.005 agent.py:72(chooseMulti)
               18840804 10580.461    0.001 10580.461    0.001 {built-in method cat}
        173696110/10409142  752.576    0.000 10401.300    0.001 module.py:710(_call_impl)
              279828215 10378.080    0.000 10378.080    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6280268  158.691    0.000 10026.069    0.002 agent.py:235(forward)
                2151394   59.322    0.000 7326.272    0.003 environments.py:83(step)
                2065436   72.900    0.000 6658.491    0.003 agent.py:88(<listcomp>)
               41308720  109.977    0.000 6401.130    0.000 exploration.py:34(epsilonGreedy)
               25121072  182.744    0.000 6146.355    0.000 container.py:115(forward)
                2065427    9.096    0.000 5138.310    0.002 agent.py:58(rememberMulti)
                2065427  173.781    0.000 5129.214    0.002 agent.py:63(<listcomp>)
                2151394   50.332    0.000 4509.283    0.002 environments.py:85(<listcomp>)
               43090726 1205.028    0.000 4466.845    0.000 helpers.py:8(clean)
                4128874   23.753    0.000 4395.485    0.001 grad_mode.py:12(decorate_context)
                4128874 1099.175    0.000 4339.058    0.001 adam.py:51(step)
                4128874   25.193    0.000 3988.129    0.001 tensor.py:155(backward)
                4128874   27.009    0.000 3962.936    0.001 __init__.py:57(backward)
                4128874 3841.808    0.001 3841.808    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               49284037 3810.204    0.000 3810.204    0.000 {built-in method as_tensor}
               37681608   63.390    0.000 2920.734    0.000 conv.py:418(forward)
               37681608   74.494    0.000 2826.352    0.000 conv.py:410(_conv_forward)
               37681608 2737.755    0.000 2737.755    0.000 {built-in method conv2d}
                2151394   44.980    0.000 2616.063    0.001 environments.py:84(<listcomp>)
               43027880  157.445    0.000 2571.083    0.000 interop.py:274(step)
                6280274  315.039    0.000 1732.668    0.000 rnn.py:109(flatten_parameters)
                6280268   73.880    0.000 1567.919    0.000 rnn.py:550(forward)
                6280268 1400.095    0.000 1400.095    0.000 {built-in method lstm}
               43027880   19.003    0.000 1285.971    0.000 wrapper.py:25(act)
               43027880   52.624    0.000 1266.969    0.000 env.py:197(act)
               25121072   51.767    0.000 1193.897    0.000 linear.py:90(forward)
               43027880 1181.855    0.000 1185.800    0.000 libenv.py:352(act)
               25121072   95.370    0.000 1114.539    0.000 functional.py:1655(linear)
                6280271 1020.245    0.000 1020.245    0.000 {built-in method _cudnn_rnn_flatten_weight}
               62802680   56.190    0.000  964.817    0.000 activation.py:653(forward)
               62802680   85.197    0.000  908.627    0.000 functional.py:1277(leaky_relu)
               62802680  815.009    0.000  815.009    0.000 {built-in method torch._C._nn.leaky_relu}
               99092976  803.991    0.000  803.991    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               25121072  749.347    0.000  749.347    0.000 {built-in method addmm}
               99092976  703.871    0.000  703.871    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               86118606   62.129    0.000  676.930    0.000 extract_dict_ob.py:9(observe)
               86118606   34.808    0.000  614.802    0.000 wrapper.py:19(observe)
               86118606  161.943    0.000  579.993    0.000 libenv.py:344(observe)
               49546488  514.230    0.000  514.230    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   2108    0.850    0.000  501.413    0.238 agent.py:161(update_target_network)
              129146486  132.003    0.000  422.671    0.000 libenv.py:281(_maybe_copy_dict)
               49546488  412.985    0.000  412.985    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4128874   69.686    0.000  406.916    0.000 optimizer.py:166(zero_grad)
              387441566  357.638    0.000  357.638    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11092297  133.300    0.000  345.470    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               29251781  318.212    0.000  342.500    0.000 module.py:774(__setattr__)
               49546488  335.216    0.000  335.216    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              310152838  334.100    0.000  334.100    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               49546488  322.754    0.000  322.754    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               43027880   33.691    0.000  320.139    0.000 wrapper.py:22(get_info)
               41308540  294.187    0.000  294.187    0.000 memory.py:17(inner)
               43027880  147.752    0.000  286.448    0.000 libenv.py:363(get_info)
                2064437  216.476    0.000  281.433    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   2108   74.976    0.036  268.244    0.127 memory.py:45(update_distribution)
               45096533  263.548    0.000  263.548    0.000 {built-in method numpy.array}
                4128874    9.459    0.000  260.415    0.000 loss.py:444(forward)
                4128874   37.877    0.000  250.956    0.000 functional.py:2621(mse_loss)
               24249171   22.040    0.000  248.274    0.000 <__array_function__ internals>:2(prod)
               49546488  231.976    0.000  231.976    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24249211   17.615    0.000  222.495    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                   4216  190.097    0.045  211.649    0.050 {built-in method _pickle.loads}
                2065436  146.899    0.000  207.304    0.000 agent.py:152(convert_values)
               24249171   28.158    0.000  204.880    0.000 fromnumeric.py:2881(prod)
                6454182   11.954    0.000  197.560    0.000 functional.py:68(split)
                6280268   17.141    0.000  197.193    0.000 pooling.py:156(forward)
               43027880  190.850    0.000  190.850    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6454182   11.004    0.000  184.767    0.000 tensor.py:367(split)
               25121084  162.615    0.000  182.627    0.000 __init__.py:66(is_acceptable)
                6280268   11.408    0.000  180.052    0.000 _jit_internal.py:237(fn)
               24249171   52.938    0.000  176.722    0.000 fromnumeric.py:70(_wrapreduction)
                2064437  173.835    0.000  173.835    0.000 memory.py:43(<listcomp>)
                6454182  172.440    0.000  172.440    0.000 {function Tensor.split at 0x7fecf9c859d0}
              247732548  143.972    0.000  168.655    0.000 tensor.py:725(grad)
                6280268   13.679    0.000  167.538    0.000 functional.py:564(_max_pool2d)
               25121072  165.555    0.000  165.555    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8257748  164.528    0.000  164.528    0.000 {built-in method gather}
                6280268  153.091    0.000  153.091    0.000 {built-in method max_pool2d}
                2151394   16.290    0.000  143.160    0.000 collector.py:8(collect)
               29162989  142.552    0.000  142.552    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2151394   22.409    0.000  141.603    0.000 environments.py:86(<listcomp>)
                4128874  139.133    0.000  139.133    0.000 {built-in method torch._C._nn.mse_loss}
               26315716  126.966    0.000  126.966    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              163456235  126.291    0.000  126.382    0.000 module.py:758(__getattr__)
                4302789  125.859    0.000  125.859    0.000 {built-in method builtins.sum}
              172237212   43.486    0.000  120.987    0.000 libenv.py:271(_maybe_copy_ndarray)
               43027900   26.993    0.000  119.207    0.000 environments.py:89(reset)
              173696110   97.550    0.000   97.550    0.000 {built-in method torch._C._get_tracing_state}
                4128874   24.237    0.000   92.678    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8587061: <NOPE_final_climber_0> in cluster <dcc> Done

Job <NOPE_final_climber_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Thu Dec 24 13:34:59 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Dec 25 05:33:09 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 25 05:33:09 2020
Terminated at Fri Dec 25 23:28:41 2020
Results reported at Fri Dec 25 23:28:41 2020

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

    CPU time :                                   68882.00 sec.
    Max Memory :                                 55582 MB
    Average Memory :                             54852.48 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5858.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64607 sec.
    Turnaround time :                            122022 sec.

The output (if any) is above this job summary.

