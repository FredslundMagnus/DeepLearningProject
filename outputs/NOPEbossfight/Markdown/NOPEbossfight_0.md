
    Name :                      NOPEbossfight-0
    Discount :                  0.99
    Environment :               bossfight
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


      10598513023 function calls (10358261017 primitive calls) in 42925.27 seconds

##    Ordered by: cumulative time
   List reduced from 1358 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 42925.265 42925.265 {built-in method builtins.exec}
                      1    0.025    0.025 42925.265 42925.265 <string>:1(<module>)
                      1  178.142  178.142 42925.239 42925.239 main.py:92(main)
                1671876  114.740    0.000 18292.673    0.011 agent.py:89(learn)
                1604909  383.450    0.000 17822.287    0.011 agent.py:102(TD_learn)
                1671876   38.554    0.000 15697.198    0.009 environments.py:83(step)
        287216327/46970947 1207.589    0.000 14800.470    0.000 module.py:715(_call_impl)
               33997742 1654.332    0.000 13306.393    0.000 helpers.py:8(clean)
                1671876   38.500    0.000 13125.272    0.008 environments.py:85(<listcomp>)
               51919608  351.305    0.000 11716.425    0.000 container.py:115(forward)
               82640566  176.697    0.000 6905.089    0.000 conv.py:422(forward)
               82640566  167.102    0.000 6650.044    0.000 conv.py:414(_conv_forward)
               82640566 6451.324    0.000 6451.324    0.000 {built-in method conv2d}
                4881694   98.875    0.000 5486.611    0.001 agent.py:231(forward)
                1604909   82.167    0.000 5140.043    0.003 memory.py:35(sample_distribution)
                1604909  146.672    0.000 4737.176    0.003 helpers.py:15(stack)
                1671876  148.547    0.000 4320.379    0.003 agent.py:72(chooseMulti)
                1605899   25.036    0.000 4298.466    0.003 agent.py:58(rememberMulti)
                1605899  180.817    0.000 4164.559    0.003 agent.py:60(<listcomp>)
                4814727   26.686    0.000 4065.464    0.001 grad_mode.py:23(decorate_context)
              283033093 4024.112    0.000 4024.112    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                4814727  142.932    0.000 3990.134    0.001 adam.py:55(step)
               38812469 3593.417    0.000 3593.417    0.000 {built-in method as_tensor}
                4814727  741.148    0.000 3266.359    0.001 functional.py:53(adam)
               17854900 2930.157    0.000 2930.157    0.000 {built-in method cat}
                4814727   27.515    0.000 2623.044    0.001 tensor.py:181(backward)
                4814727   15.876    0.000 2595.529    0.001 __init__.py:68(backward)
                4814727 2480.606    0.001 2480.606    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1671876   30.182    0.000 2207.673    0.001 environments.py:84(<listcomp>)
               33437520  113.738    0.000 2177.491    0.000 interop.py:274(step)
              108720910  103.782    0.000 1849.403    0.000 activation.py:713(forward)
              108720910  153.041    0.000 1745.622    0.000 functional.py:1292(leaky_relu)
              108720910 1577.332    0.000 1577.332    0.000 {built-in method torch._C._nn.leaky_relu}
               19526886 1507.314    0.000 1507.348    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               29357128   63.907    0.000 1431.315    0.000 linear.py:92(forward)
               29357128  169.368    0.000 1343.350    0.000 functional.py:1669(linear)
               33437520   16.104    0.000 1323.676    0.000 wrapper.py:25(act)
               33437520   41.582    0.000 1307.572    0.000 env.py:197(act)
               33437520 1241.963    0.000 1245.148    0.000 libenv.py:352(act)
                4881700  211.984    0.000 1169.532    0.000 rnn.py:110(flatten_parameters)
                1671876   60.208    0.000 1065.298    0.001 agent.py:87(<listcomp>)
              269624824  608.921    0.000 1032.401    0.000 tensor.py:933(grad)
                4881694   43.071    0.000  947.522    0.000 rnn.py:555(forward)
                4814727   91.683    0.000  890.935    0.000 optimizer.py:167(zero_grad)
                4881694  851.339    0.000  851.339    0.000 {built-in method lstm}
               33437520   88.549    0.000  848.730    0.000 exploration.py:34(epsilonGreedy)
                3276784   11.213    0.000  770.751    0.000 agent.py:247(avoid_similar_state)
                4881697  735.822    0.000  735.822    0.000 {built-in method _cudnn_rnn_flatten_weight}
               24341503  718.380    0.000  718.380    0.000 {built-in method addmm}
               77035632  658.841    0.000  658.841    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               77035632  564.068    0.000  564.068    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              337499984  179.984    0.000  533.110    0.000 overrides.py:1073(has_torch_function)
               67435262   48.590    0.000  436.229    0.000 extract_dict_ob.py:9(observe)
               67435262   25.542    0.000  387.639    0.000 wrapper.py:19(observe)
               38517816  377.525    0.000  377.525    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67435262   91.810    0.000  362.097    0.000 libenv.py:344(observe)
                   1638    0.540    0.000  355.646    0.217 agent.py:157(update_target_network)
              376486590  142.701    0.000  339.549    0.000 {built-in method builtins.any}
               38517816  336.592    0.000  336.592    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              347638774  331.943    0.000  331.943    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1671876   15.377    0.000  325.698    0.000 environments.py:86(<listcomp>)
               33437540   19.009    0.000  310.443    0.000 environments.py:89(reset)
               38517816  306.966    0.000  306.966    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               38517816  268.981    0.000  268.981    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              100872782   86.740    0.000  257.401    0.000 libenv.py:281(_maybe_copy_dict)
                4814727    7.773    0.000  245.856    0.000 loss.py:445(forward)
                4814727   25.163    0.000  238.083    0.000 functional.py:2637(mse_loss)
                5015628    7.609    0.000  235.305    0.000 functional.py:74(split)
                5015628   18.868    0.000  227.029    0.000 tensor.py:460(split)
               32117980  222.980    0.000  222.980    0.000 memory.py:17(inner)
                7396540   80.905    0.000  217.622    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              302619984  217.139    0.000  217.139    0.000 {method 'copy' of 'numpy.ndarray' objects}
               33437520   24.385    0.000  213.811    0.000 wrapper.py:22(get_info)
                5015628  207.056    0.000  207.056    0.000 {function Tensor.split at 0x7f3cf7336d30}
               38517816  200.363    0.000  200.363    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              704357096  157.094    0.000  193.756    0.000 overrides.py:1086(<genexpr>)
               29357128  192.614    0.000  192.614    0.000 {method 't' of 'torch._C._TensorBase' objects}
               33437520  103.011    0.000  189.426    0.000 libenv.py:363(get_info)
                   1638   53.423    0.033  188.150    0.115 memory.py:45(update_distribution)
               35045705  186.888    0.000  186.888    0.000 {built-in method numpy.array}
              290428125  185.050    0.000  185.050    0.000 {built-in method torch._C._get_tracing_state}
              251812315  169.393    0.000  169.465    0.000 module.py:765(__getattr__)
                1604909  132.087    0.000  169.421    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               16398129   13.929    0.000  159.193    0.000 <__array_function__ internals>:2(prod)
               33437520  156.360    0.000  156.360    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8024545  155.858    0.000  155.858    0.000 {built-in method gather}
                   3276  132.550    0.040  150.357    0.046 {built-in method _pickle.loads}
                1605908  143.271    0.000  145.266    0.000 agent.py:148(convert_values)
               16398169   11.576    0.000  142.689    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                4814727  142.630    0.000  142.630    0.000 {built-in method torch._C._nn.mse_loss}
                5015625  139.670    0.000  139.670    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               29089263  132.516    0.000  132.516    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               22738443  115.759    0.000  131.512    0.000 module.py:781(__setattr__)
               16398129   17.469    0.000  131.113    0.000 fromnumeric.py:2881(prod)
             1200784916  128.237    0.000  128.237    0.000 {method 'values' of 'collections.OrderedDict' objects}
               16398129   34.584    0.000  113.644    0.000 fromnumeric.py:70(_wrapreduction)
                1671876    9.177    0.000  111.256    0.000 collector.py:8(collect)
                1604909  109.971    0.000  109.971    0.000 memory.py:43(<listcomp>)
                3211798   12.544    0.000  108.871    0.000 tensor.py:576(__iter__)
               38518032   46.512    0.000  106.167    0.000 tensor.py:596(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 8582540: <NOPEbossfight_0> in cluster <dcc> Done

Job <NOPEbossfight_0> was submitted from host <n-62-30-7> by user <s183914> in cluster <dcc> at Tue Dec 22 15:37:43 2020
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec 23 03:33:26 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 23 03:33:26 2020
Terminated at Wed Dec 23 15:29:00 2020
Results reported at Wed Dec 23 15:29:00 2020

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

    CPU time :                                   43672.00 sec.
    Max Memory :                                 10273 MB
    Average Memory :                             10181.74 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               51167.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   42952 sec.
    Turnaround time :                            85877 sec.

The output (if any) is above this job summary.

