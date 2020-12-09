[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      CHASER_U_S_0_0chaser-0
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
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      9074738015 function calls (8865435278 primitive calls) in 82515.27 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82515.267 82515.267 {built-in method builtins.exec}
                      1    0.048    0.048 82515.267 82515.267 <string>:1(<module>)
                      1  596.854  596.854 82515.215 82515.215 main.py:92(main)
                2130230  223.098    0.000 56779.905    0.027 agent.py:84(learn)
                2045272  727.095    0.000 55939.875    0.027 agent.py:99(TD_learn)
                2045272  167.014    0.000 29335.713    0.014 memory.py:35(sample_distribution)
                2045272  333.930    0.000 28582.433    0.014 helpers.py:15(stack)
               18662322 16555.977    0.001 16555.977    0.001 {built-in method cat}
        223698984/14402861 1030.839    0.000 15422.277    0.001 module.py:710(_call_impl)
                6220774  212.711    0.000 14252.192    0.002 agent.py:216(forward)
               20708701 11456.798    0.001 11456.800    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               33150141  288.739    0.000 9882.067    0.000 container.py:115(forward)
                2130230  206.445    0.000 9154.219    0.004 agent.py:70(chooseMulti)
                2130230   65.035    0.000 8623.816    0.004 environments.py:83(step)
                6135816   38.732    0.000 7983.184    0.001 grad_mode.py:12(decorate_context)
                6135816 1907.146    0.000 7898.199    0.001 adam.py:51(step)
                2046271   91.303    0.000 7189.247    0.004 agent.py:58(rememberMulti)
              277090826 7175.888    0.000 7175.888    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2046271  279.297    0.000 6728.263    0.003 agent.py:62(<listcomp>)
                6135816   39.130    0.000 6068.885    0.001 tensor.py:155(backward)
                6135816   35.991    0.000 6029.755    0.001 __init__.py:57(backward)
                6135816 5830.394    0.001 5830.394    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2130230   57.821    0.000 5283.742    0.002 environments.py:85(<listcomp>)
               42864261 1296.395    0.000 5263.116    0.000 helpers.py:8(clean)
               49000077 4552.899    0.000 4552.899    0.000 {built-in method as_tensor}
               37324644   67.349    0.000 3672.008    0.000 conv.py:418(forward)
               37324644   83.512    0.000 3571.140    0.000 conv.py:410(_conv_forward)
               37324644 3472.842    0.000 3472.842    0.000 {built-in method conv2d}
               49684231  105.409    0.000 3053.829    0.000 linear.py:90(forward)
                2130230   47.840    0.000 3039.299    0.001 environments.py:84(<listcomp>)
               42604600  174.478    0.000 2991.460    0.000 interop.py:274(step)
               49684231  295.362    0.000 2895.047    0.000 functional.py:1655(linear)
                2046271  101.044    0.000 2600.672    0.001 agent.py:82(<listcomp>)
                6220780  364.585    0.000 2321.731    0.000 rnn.py:109(flatten_parameters)
               40925420  139.002    0.000 2220.378    0.000 exploration.py:34(epsilonGreedy)
                6220774   77.104    0.000 1825.859    0.000 rnn.py:550(forward)
               43545418 1722.651    0.000 1722.651    0.000 {built-in method addmm}
                6220774 1660.567    0.000 1660.567    0.000 {built-in method lstm}
               78741830   73.079    0.000 1626.213    0.000 activation.py:653(forward)
              122716320 1567.610    0.000 1567.610    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               78741830  111.310    0.000 1553.134    0.000 functional.py:1277(leaky_relu)
                6220777 1510.509    0.000 1510.509    0.000 {built-in method _cudnn_rnn_flatten_weight}
               42604600   20.187    0.000 1502.636    0.000 wrapper.py:25(act)
               42604600   66.816    0.000 1482.450    0.000 env.py:197(act)
               78741830 1432.204    0.000 1432.204    0.000 {built-in method torch._C._nn.leaky_relu}
               42604600 1374.225    0.000 1378.190    0.000 libenv.py:352(act)
              122716320 1351.394    0.000 1351.394    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               61358160  908.047    0.000  908.047    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               85468861   71.353    0.000  814.944    0.000 extract_dict_ob.py:9(observe)
                6135816  117.890    0.000  764.421    0.000 optimizer.py:166(zero_grad)
               85468861   37.347    0.000  743.590    0.000 wrapper.py:19(observe)
               61358160  734.406    0.000  734.406    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               85468861  181.113    0.000  706.243    0.000 libenv.py:344(observe)
                   2130    1.053    0.000  616.932    0.290 agent.py:142(update_target_network)
               61358160  616.534    0.000  616.534    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               61358160  601.896    0.000  601.896    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2046271    5.704    0.000  587.024    0.000 agent.py:234(avoid_similar_state)
              310863859  584.190    0.000  584.190    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              128073461  145.665    0.000  517.786    0.000 libenv.py:281(_maybe_copy_dict)
               40925420  476.468    0.000  476.468    0.000 memory.py:17(inner)
               61358160  470.023    0.000  470.023    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              384222513  463.646    0.000  463.646    0.000 {method 'copy' of 'numpy.ndarray' objects}
               49684231  459.853    0.000  459.853    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6135816   14.451    0.000  439.473    0.000 loss.py:444(forward)
                6135816   53.432    0.000  425.022    0.000 functional.py:2621(mse_loss)
               28975475  389.869    0.000  412.662    0.000 module.py:774(__setattr__)
               11072558  153.845    0.000  389.096    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               42604600   39.885    0.000  358.007    0.000 wrapper.py:22(get_info)
                   2130   97.818    0.046  337.575    0.158 memory.py:45(update_distribution)
               44654132  320.070    0.000  320.070    0.000 {built-in method numpy.array}
               42604600  163.866    0.000  318.122    0.000 libenv.py:363(get_info)
                2045272  233.255    0.000  302.826    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               42604600  289.207    0.000  289.207    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24190528   22.965    0.000  273.611    0.000 <__array_function__ internals>:2(prod)
               37154728  260.452    0.000  260.452    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6390690   12.060    0.000  259.192    0.000 functional.py:68(split)
                2046271  257.239    0.000  258.906    0.000 agent.py:134(convert_values)
                6135816  256.238    0.000  256.238    0.000 {built-in method torch._C._nn.mse_loss}
                   4260  227.570    0.053  252.232    0.059 {built-in method _pickle.loads}
              306790908  220.265    0.000  251.631    0.000 tensor.py:725(grad)
                6220774   22.046    0.000  247.558    0.000 pooling.py:156(forward)
               24190568   17.856    0.000  246.535    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6390690   12.209    0.000  246.346    0.000 tensor.py:367(split)
                8181088  241.550    0.000  241.550    0.000 {built-in method gather}
                2130230   25.047    0.000  235.740    0.000 environments.py:86(<listcomp>)
                6390690  232.725    0.000  232.725    0.000 {function Tensor.split at 0x7f969004a9d0}
               24190528   29.316    0.000  228.679    0.000 fromnumeric.py:2881(prod)
                6220774   11.272    0.000  225.512    0.000 _jit_internal.py:237(fn)
               24883108  201.387    0.000  221.224    0.000 __init__.py:66(is_acceptable)
                6138813  217.924    0.000  217.924    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2208149  216.816    0.000  216.816    0.000 {built-in method tensor}
                6220774   13.574    0.000  213.192    0.000 functional.py:564(_max_pool2d)
               42604620   32.288    0.000  210.697    0.000 environments.py:89(reset)
               24190528   55.126    0.000  199.363    0.000 fromnumeric.py:70(_wrapreduction)
                6220774  198.900    0.000  198.900    0.000 {built-in method max_pool2d}
                2045272  188.026    0.000  188.026    0.000 memory.py:43(<listcomp>)
              223698984  175.622    0.000  175.622    0.000 {built-in method torch._C._get_tracing_state}
              219780467  165.212    0.000  165.306    0.000 module.py:758(__getattr__)
                6135816   35.035    0.000  161.255    0.000 __init__.py:25(_make_grads)
               26237930  151.924    0.000  151.924    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8552390: <CHASER_U_S_0_0chaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0_0chaser_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Tue Dec  8 22:35:06 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Dec  8 22:35:07 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec  8 22:35:07 2020
Terminated at Wed Dec  9 21:30:32 2020
Results reported at Wed Dec  9 21:30:32 2020

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

    CPU time :                                   88028.00 sec.
    Max Memory :                                 54405 MB
    Average Memory :                             53737.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7035.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82574 sec.
    Turnaround time :                            82526 sec.

The output (if any) is above this job summary.

