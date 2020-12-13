
    Name :                      CHASER_U_S_0_0.2returnchaser-0
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.2
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13414503421 function calls (13193177432 primitive calls) in 82513.95 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82513.947 82513.947 {built-in method builtins.exec}
                      1    0.014    0.014 82513.947 82513.947 <string>:1(<module>)
                      1  517.289  517.289 82513.931 82513.931 main.py:92(main)
                2253369  248.790    0.000 56690.744    0.025 agent.py:84(learn)
                2162414  933.694    0.000 55901.933    0.026 agent.py:99(TD_learn)
                2162414  159.632    0.000 25440.319    0.012 memory.py:35(sample_distribution)
                2162414  311.729    0.000 24680.008    0.011 helpers.py:15(stack)
        236548221/15228852 1063.636    0.000 16373.387    0.001 module.py:715(_call_impl)
                6578197  219.204    0.000 15137.117    0.002 agent.py:231(forward)
               19734591 12193.481    0.001 12193.481    0.001 {built-in method cat}
               21898112 11799.617    0.001 11799.618    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               35054398  292.061    0.000 10585.601    0.000 container.py:115(forward)
                6487242   42.838    0.000 9400.023    0.001 grad_mode.py:23(decorate_context)
                6487242  278.758    0.000 9282.425    0.001 adam.py:55(step)
                2253369   65.596    0.000 9100.339    0.004 environments.py:83(step)
                2253369  210.599    0.000 8719.248    0.004 agent.py:70(chooseMulti)
                6487242 1740.680    0.000 7989.693    0.001 functional.py:53(adam)
                2163413   94.839    0.000 7308.100    0.003 agent.py:58(rememberMulti)
                2163413  295.619    0.000 6830.571    0.003 agent.py:62(<listcomp>)
              293552857 6554.786    0.000 6554.786    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6487242   48.138    0.000 6286.204    0.001 tensor.py:181(backward)
                6487242   30.593    0.000 6238.067    0.001 __init__.py:68(backward)
                6487242 6028.574    0.001 6028.574    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2253369   68.781    0.000 5693.243    0.003 environments.py:85(<listcomp>)
               45423025 1322.791    0.000 5674.950    0.000 helpers.py:8(clean)
               51910267 4942.476    0.000 4942.476    0.000 {built-in method as_tensor}
               39469182   70.025    0.000 3873.627    0.000 conv.py:422(forward)
               39469182   83.067    0.000 3770.468    0.000 conv.py:414(_conv_forward)
               39469182 3673.024    0.000 3673.024    0.000 {built-in method conv2d}
               52537618  116.602    0.000 3365.797    0.000 linear.py:92(forward)
               52537618  314.602    0.000 3194.905    0.000 functional.py:1669(linear)
                2253369   47.386    0.000 3094.463    0.001 environments.py:84(<listcomp>)
               45067380  181.967    0.000 3047.077    0.000 interop.py:274(step)
                6578203  418.848    0.000 2568.253    0.000 rnn.py:110(flatten_parameters)
               46047379 1893.468    0.000 1893.468    0.000 {built-in method addmm}
              454107048 1191.692    0.000 1882.666    0.000 tensor.py:933(grad)
                6487242  178.570    0.000 1817.215    0.000 optimizer.py:167(zero_grad)
                2163413  103.155    0.000 1812.468    0.001 agent.py:82(<listcomp>)
                6578197   79.054    0.000 1790.364    0.000 rnn.py:555(forward)
               83265190   77.314    0.000 1757.999    0.000 activation.py:713(forward)
              129744840 1708.298    0.000 1708.298    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               83265190  112.322    0.000 1680.684    0.000 functional.py:1292(leaky_relu)
                6578200 1662.369    0.000 1662.369    0.000 {built-in method _cudnn_rnn_flatten_weight}
                6578197 1621.504    0.000 1621.504    0.000 {built-in method lstm}
               83265190 1558.468    0.000 1558.468    0.000 {built-in method torch._C._nn.leaky_relu}
               45067380   20.082    0.000 1547.515    0.000 wrapper.py:25(act)
               45067380   66.856    0.000 1527.433    0.000 env.py:197(act)
               45067380 1414.372    0.000 1419.125    0.000 libenv.py:352(act)
              129744840 1409.488    0.000 1409.488    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               43268260  153.815    0.000 1408.074    0.000 exploration.py:34(epsilonGreedy)
              571517332  322.763    0.000  887.842    0.000 overrides.py:1073(has_torch_function)
               64872420  882.609    0.000  882.609    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               64872420  811.312    0.000  811.312    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               90490405   73.793    0.000  810.860    0.000 extract_dict_ob.py:9(observe)
               64872420  744.422    0.000  744.422    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               90490405   37.033    0.000  737.066    0.000 wrapper.py:19(observe)
               90490405  175.917    0.000  700.033    0.000 libenv.py:344(observe)
               64872420  668.806    0.000  668.806    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2163413    6.762    0.000  638.462    0.000 agent.py:249(avoid_similar_state)
              637029458  222.333    0.000  544.160    0.000 {built-in method builtins.any}
                   2253    0.946    0.000  540.022    0.240 agent.py:157(update_target_network)
              333473751  531.838    0.000  531.838    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               52537618  517.801    0.000  517.801    0.000 {method 't' of 'torch._C._TensorBase' objects}
              135557785  145.374    0.000  510.296    0.000 libenv.py:281(_maybe_copy_dict)
               64872420  505.319    0.000  505.319    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              406675608  458.000    0.000  458.000    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6487242   15.173    0.000  452.940    0.000 loss.py:445(forward)
                6487242   46.595    0.000  437.766    0.000 functional.py:2637(mse_loss)
               11189117  163.613    0.000  408.581    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               30639451  361.145    0.000  385.559    0.000 module.py:781(__setattr__)
                6760107   12.908    0.000  384.484    0.000 functional.py:74(split)
                6760107   30.567    0.000  370.634    0.000 tensor.py:460(split)
               12974484  366.000    0.000  366.000    0.000 {built-in method gather}
               45067380   39.382    0.000  363.962    0.000 wrapper.py:22(get_info)
               43268260  358.362    0.000  358.362    0.000 memory.py:17(inner)
                6760107  338.401    0.000  338.401    0.000 {function Tensor.split at 0x7fb16271ad30}
               50099342  328.833    0.000  328.833    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2162414  252.937    0.000  326.139    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               45067380  167.963    0.000  324.580    0.000 libenv.py:363(get_info)
             1195572282  252.844    0.000  316.903    0.000 overrides.py:1086(<genexpr>)
               45067380  312.364    0.000  312.364    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24540788   24.087    0.000  285.446    0.000 <__array_function__ internals>:2(prod)
               47234300  284.615    0.000  284.615    0.000 {built-in method numpy.array}
                   2253   80.759    0.036  280.611    0.125 memory.py:45(update_distribution)
                6487242  276.847    0.000  276.847    0.000 {built-in method torch._C._nn.mse_loss}
                2163413  272.465    0.000  276.231    0.000 agent.py:149(convert_values)
                6578197   16.439    0.000  258.356    0.000 pooling.py:152(forward)
               24540828   19.631    0.000  257.251    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                2253369   29.079    0.000  247.038    0.000 environments.py:86(<listcomp>)
                6578197   11.883    0.000  241.916    0.000 _jit_internal.py:257(fn)
               24540788   30.460    0.000  237.621    0.000 fromnumeric.py:2881(prod)
                6490239  236.393    0.000  236.393    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                   4506  207.066    0.046  233.691    0.052 {built-in method _pickle.loads}
                6578197   13.198    0.000  228.922    0.000 functional.py:574(_max_pool2d)
               45067400   35.029    0.000  217.963    0.000 environments.py:89(reset)
                6578197  214.975    0.000  214.975    0.000 {built-in method max_pool2d}
               12975483  214.665    0.000  214.665    0.000 {method 'type' of 'torch._C._TensorBase' objects}
               24540788   56.057    0.000  207.161    0.000 fromnumeric.py:70(_wrapreduction)
               26312800  180.416    0.000  202.807    0.000 __init__.py:67(is_acceptable)
                2334639  201.750    0.000  201.750    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8557116: <CHASER_U_S_0_0.2returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0_0.2returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:11 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec 12 16:39:32 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec 12 16:39:32 2020
Terminated at Sun Dec 13 15:34:50 2020
Results reported at Sun Dec 13 15:34:50 2020

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

    CPU time :                                   85172.00 sec.
    Max Memory :                                 54940 MB
    Average Memory :                             54223.63 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6500.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82518 sec.
    Turnaround time :                            174399 sec.

The output (if any) is above this job summary.

