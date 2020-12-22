
    Name :                      U_S_0.1_0.1returndodgeball-0
    Discount :                  0.99
    Environment :               dodgeball
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
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12796021436 function calls (12607835922 primitive calls) in 82544.00 seconds

##    Ordered by: cumulative time
   List reduced from 1362 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82543.995 82543.995 {built-in method builtins.exec}
                      1    0.040    0.040 82543.995 82543.995 <string>:1(<module>)
                      1  439.617  439.617 82543.954 82543.954 main.py:92(main)
                2194721  190.066    0.000 55830.899    0.025 agent.py:89(learn)
                2107764  611.623    0.000 55128.386    0.026 agent.py:102(TD_learn)
                2107764  157.641    0.000 32364.735    0.015 memory.py:35(sample_distribution)
                2107764  244.421    0.000 31674.504    0.015 helpers.py:15(stack)
               25641102 24833.558    0.001 24833.615    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        205214919/17036025  892.094    0.000 12305.405    0.001 module.py:715(_call_impl)
                2194721  215.517    0.000 11275.604    0.005 agent.py:72(chooseMulti)
                6410249  165.243    0.000 10753.128    0.002 agent.py:231(forward)
               23446275 10695.967    0.000 10695.967    0.000 {built-in method cat}
                2194721   57.128    0.000 7836.406    0.004 environments.py:83(step)
               29943480  218.551    0.000 7656.887    0.000 container.py:115(forward)
                2108754   40.192    0.000 6967.494    0.003 agent.py:58(rememberMulti)
                2108754  257.159    0.000 6708.789    0.003 agent.py:60(<listcomp>)
                6323292   42.631    0.000 6700.411    0.001 grad_mode.py:23(decorate_context)
                6323292  261.302    0.000 6590.036    0.001 adam.py:55(step)
              370142891 6447.796    0.000 6447.796    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6323292 1213.213    0.000 5388.817    0.001 functional.py:53(adam)
                6323292   46.146    0.000 4905.354    0.001 tensor.py:181(backward)
                2194721   52.772    0.000 4882.578    0.002 environments.py:85(<listcomp>)
               44169322 1244.617    0.000 4865.266    0.000 helpers.py:8(clean)
                6323292   28.628    0.000 4859.208    0.001 __init__.py:68(backward)
                6323292 4679.840    0.001 4679.840    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               50492614 4107.437    0.000 4107.437    0.000 {built-in method as_tensor}
               38461494   68.807    0.000 3103.174    0.000 conv.py:422(forward)
               38461494   77.821    0.000 3001.665    0.000 conv.py:414(_conv_forward)
               38461494 2908.125    0.000 2908.125    0.000 {built-in method conv2d}
                2194721   46.006    0.000 2719.586    0.001 environments.py:84(<listcomp>)
               43894420  157.163    0.000 2673.580    0.000 interop.py:274(step)
               38548448   85.921    0.000 2054.905    0.000 linear.py:92(forward)
               38548448  232.496    0.000 1925.957    0.000 functional.py:1669(linear)
                6410255  367.573    0.000 1895.774    0.000 rnn.py:110(flatten_parameters)
              442630548  984.981    0.000 1658.492    0.000 tensor.py:933(grad)
                6410249   73.135    0.000 1625.538    0.000 rnn.py:555(forward)
                2194721   79.589    0.000 1471.040    0.001 agent.py:87(<listcomp>)
                6410249 1462.350    0.000 1462.350    0.000 {built-in method lstm}
                6323292  138.125    0.000 1423.806    0.000 optimizer.py:167(zero_grad)
               43894420   21.063    0.000 1338.145    0.000 wrapper.py:25(act)
               43894420   55.422    0.000 1317.082    0.000 env.py:197(act)
               43894420 1227.507    0.000 1231.668    0.000 libenv.py:352(act)
               72707458   63.484    0.000 1228.430    0.000 activation.py:713(forward)
               43894420  118.914    0.000 1181.777    0.000 exploration.py:34(epsilonGreedy)
               72707458  102.411    0.000 1164.945    0.000 functional.py:1292(leaky_relu)
                6410252 1121.023    0.000 1121.023    0.000 {built-in method _cudnn_rnn_flatten_weight}
              126465840 1090.420    0.000 1090.420    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4302484   16.326    0.000 1073.897    0.000 agent.py:247(avoid_similar_state)
               72707458 1053.452    0.000 1053.452    0.000 {built-in method torch._C._nn.leaky_relu}
               31964288 1042.563    0.000 1042.563    0.000 {built-in method addmm}
              126465840  924.393    0.000  924.393    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              544412162  285.097    0.000  822.584    0.000 overrides.py:1073(has_torch_function)
               88063742   64.755    0.000  721.655    0.000 extract_dict_ob.py:9(observe)
               88063742   38.588    0.000  656.900    0.000 wrapper.py:19(observe)
               88063742  163.114    0.000  618.312    0.000 libenv.py:344(observe)
               63232920  608.946    0.000  608.946    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               63232920  561.858    0.000  561.858    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              595607218  207.857    0.000  515.916    0.000 {built-in method builtins.any}
               63232920  512.839    0.000  512.839    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   2151    0.875    0.000  512.446    0.238 agent.py:157(update_target_network)
               63232920  456.464    0.000  456.464    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              131958162  136.941    0.000  454.581    0.000 libenv.py:281(_maybe_copy_dict)
              411232430  390.107    0.000  390.107    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              395876637  389.425    0.000  389.425    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6323292   12.622    0.000  378.957    0.000 loss.py:445(forward)
                6323292   45.001    0.000  366.334    0.000 functional.py:2637(mse_loss)
               11215559  138.654    0.000  357.831    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6584163   11.673    0.000  346.250    0.000 functional.py:74(split)
               29858359  310.680    0.000  334.524    0.000 module.py:781(__setattr__)
                6584163   27.517    0.000  333.711    0.000 tensor.py:460(split)
               42175080  331.340    0.000  331.340    0.000 memory.py:17(inner)
               43894420   37.624    0.000  331.225    0.000 wrapper.py:22(get_info)
               63232920  321.653    0.000  321.653    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6584163  304.703    0.000  304.703    0.000 {function Tensor.split at 0x7fabeea02ca0}
             1127372772  243.759    0.000  303.357    0.000 overrides.py:1086(<genexpr>)
               43894420  151.140    0.000  293.600    0.000 libenv.py:363(get_info)
                2107764  223.264    0.000  289.008    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               38548448  283.857    0.000  283.857    0.000 {method 't' of 'torch._C._TensorBase' objects}
                   2151   75.005    0.035  269.894    0.125 memory.py:45(update_distribution)
               46006486  266.383    0.000  266.383    0.000 {built-in method numpy.array}
               24539022   23.196    0.000  256.102    0.000 <__array_function__ internals>:2(prod)
               10538820  236.565    0.000  236.565    0.000 {built-in method gather}
               24539062   17.462    0.000  229.032    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6323292  219.615    0.000  219.615    0.000 {built-in method torch._C._nn.mse_loss}
                   4302  195.860    0.046  219.445    0.051 {built-in method _pickle.loads}
                4217508   19.964    0.000  218.513    0.000 tensor.py:576(__iter__)
                6410249   20.078    0.000  216.992    0.000 pooling.py:152(forward)
               24539022   29.095    0.000  211.570    0.000 fromnumeric.py:2881(prod)
               43894420  209.673    0.000  209.673    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6584160  199.228    0.000  199.228    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6410249   11.594    0.000  196.914    0.000 _jit_internal.py:257(fn)
                2108763  191.381    0.000  194.205    0.000 agent.py:148(convert_values)
                4217508  192.015    0.000  192.015    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               38200623  187.041    0.000  187.041    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6410249   11.753    0.000  184.234    0.000 functional.py:574(_max_pool2d)
               24539022   54.249    0.000  182.475    0.000 fromnumeric.py:70(_wrapreduction)
                2194721   23.325    0.000  177.115    0.000 environments.py:86(<listcomp>)
               63233166   81.031    0.000  175.613    0.000 tensor.py:596(__hash__)
                6410249  171.703    0.000  171.703    0.000 {built-in method max_pool2d}
                2107764  160.370    0.000  160.370    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 8578473: <U_S_0.1_0.1returndodgeball_0> in cluster <dcc> Done

Job <U_S_0.1_0.1returndodgeball_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec 20 03:01:51 2020
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Dec 21 08:47:28 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec 21 08:47:28 2020
Terminated at Tue Dec 22 07:43:24 2020
Results reported at Tue Dec 22 07:43:24 2020

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

    CPU time :                                   76895.00 sec.
    Max Memory :                                 56784 MB
    Average Memory :                             56070.22 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4656.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   74040 sec.
    Turnaround time :                            189693 sec.

The output (if any) is above this job summary.

