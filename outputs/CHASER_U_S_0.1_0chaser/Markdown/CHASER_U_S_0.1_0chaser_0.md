[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      CHASER_U_S_0.1_0chaser-0
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
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11106635321 function calls (10849807593 primitive calls) in 82546.54 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82546.538 82546.538 {built-in method builtins.exec}
                      1    0.065    0.065 82546.537 82546.537 <string>:1(<module>)
                      1  537.689  537.689 82546.470 82546.470 main.py:92(main)
                2614431  211.919    0.000 51689.764    0.020 agent.py:84(learn)
                2509483  650.382    0.000 50825.686    0.020 agent.py:99(TD_learn)
                2509483  165.471    0.000 26397.088    0.011 memory.py:35(sample_distribution)
                2509483  249.249    0.000 25596.202    0.010 helpers.py:15(stack)
        274493442/17672328 1155.215    0.000 15018.005    0.001 module.py:710(_call_impl)
                7633397  225.777    0.000 13862.259    0.002 agent.py:216(forward)
                2614431  195.101    0.000 13450.584    0.005 agent.py:70(chooseMulti)
               25410781 13332.797    0.001 13332.812    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               22900191 11856.621    0.001 11856.621    0.001 {built-in method cat}
              342016894 11404.108    0.000 11404.108    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2614431   73.615    0.000 9834.755    0.004 environments.py:83(step)
               40677467  291.700    0.000 9718.890    0.000 container.py:115(forward)
                2510482   97.861    0.000 6955.921    0.003 agent.py:82(<listcomp>)
                7528449   39.882    0.000 6874.445    0.001 grad_mode.py:12(decorate_context)
                2510482   97.708    0.000 6784.511    0.003 agent.py:58(rememberMulti)
                7528449 1724.785    0.000 6784.372    0.001 adam.py:51(step)
               50209640  147.977    0.000 6619.858    0.000 exploration.py:34(epsilonGreedy)
                2510482  247.827    0.000 6286.843    0.003 agent.py:62(<listcomp>)
                2614431   63.685    0.000 6118.022    0.002 environments.py:85(<listcomp>)
               52703349 1679.449    0.000 6110.557    0.000 helpers.py:8(clean)
                7528449   29.033    0.000 5673.193    0.001 tensor.py:155(backward)
                7528449   36.323    0.000 5644.160    0.001 __init__.py:57(backward)
                7528449 5447.052    0.001 5447.052    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               60231798 4951.298    0.000 4951.298    0.000 {built-in method as_tensor}
               45800382   82.810    0.000 3612.148    0.000 conv.py:418(forward)
               45800382   92.141    0.000 3494.203    0.000 conv.py:410(_conv_forward)
               45800382 3385.383    0.000 3385.383    0.000 {built-in method conv2d}
                2614431   56.481    0.000 3367.531    0.001 environments.py:84(<listcomp>)
               52288620  191.933    0.000 3311.049    0.000 interop.py:274(step)
               60965225  127.091    0.000 2943.742    0.000 linear.py:90(forward)
               60965225  320.315    0.000 2755.067    0.000 functional.py:1655(linear)
                7633403  366.550    0.000 2093.289    0.000 rnn.py:109(flatten_parameters)
                7633397   81.424    0.000 1788.141    0.000 rnn.py:550(forward)
               52288620   24.276    0.000 1680.573    0.000 wrapper.py:25(act)
               52288620   67.405    0.000 1656.297    0.000 env.py:197(act)
               53433779 1615.988    0.000 1615.988    0.000 {built-in method addmm}
                7633397 1609.063    0.000 1609.063    0.000 {built-in method lstm}
               52288620 1546.461    0.000 1551.867    0.000 libenv.py:352(act)
               96621728   82.379    0.000 1513.174    0.000 activation.py:653(forward)
               96621728  124.631    0.000 1430.795    0.000 functional.py:1277(leaky_relu)
               96621728 1293.021    0.000 1293.021    0.000 {built-in method torch._C._nn.leaky_relu}
                7633400 1282.419    0.000 1282.419    0.000 {built-in method _cudnn_rnn_flatten_weight}
              150568980 1277.017    0.000 1277.017    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              150568980 1100.828    0.000 1100.828    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              104991969   77.305    0.000  887.201    0.000 extract_dict_ob.py:9(observe)
              104991969   47.658    0.000  809.896    0.000 wrapper.py:19(observe)
               75284490  782.743    0.000  782.743    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              104991969  203.719    0.000  762.238    0.000 libenv.py:344(observe)
                7528449  120.867    0.000  670.448    0.000 optimizer.py:166(zero_grad)
                   2614    1.010    0.000  652.158    0.249 agent.py:142(update_target_network)
               75284490  646.295    0.000  646.295    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2510482    6.951    0.000  578.972    0.000 agent.py:234(avoid_similar_state)
              157280589  164.619    0.000  553.513    0.000 libenv.py:281(_maybe_copy_dict)
               75284490  521.320    0.000  521.320    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75284490  505.676    0.000  505.676    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              471844381  476.019    0.000  476.019    0.000 {method 'copy' of 'numpy.ndarray' objects}
              383302526  464.398    0.000  464.398    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7528449   12.865    0.000  433.323    0.000 loss.py:444(forward)
                7528449   55.462    0.000  420.458    0.000 functional.py:2621(mse_loss)
               52288620   45.957    0.000  398.543    0.000 wrapper.py:22(get_info)
               11537252  147.496    0.000  379.977    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               60965225  373.516    0.000  373.516    0.000 {method 't' of 'torch._C._TensorBase' objects}
               75284490  369.452    0.000  369.452    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               35554389  343.150    0.000  367.965    0.000 module.py:774(__setattr__)
                   2614   97.107    0.037  364.970    0.140 memory.py:45(update_distribution)
               54803331  359.571    0.000  359.571    0.000 {built-in method numpy.array}
               52288620  183.115    0.000  352.586    0.000 libenv.py:363(get_info)
               50209640  351.917    0.000  351.917    0.000 memory.py:17(inner)
                2509483  271.933    0.000  347.901    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                2614431   30.387    0.000  275.588    0.000 environments.py:86(<listcomp>)
               25584127   24.407    0.000  275.101    0.000 <__array_function__ internals>:2(prod)
              376422558  236.322    0.000  273.433    0.000 tensor.py:725(grad)
                   5228  231.436    0.044  259.117    0.050 {built-in method _pickle.loads}
                7843293   13.216    0.000  251.731    0.000 functional.py:68(split)
               52288620  246.677    0.000  246.677    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25584167   19.029    0.000  246.382    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               52288640   36.125    0.000  245.235    0.000 environments.py:89(reset)
                7843293   13.604    0.000  237.378    0.000 tensor.py:367(split)
                2709144  236.512    0.000  236.512    0.000 {built-in method tensor}
                7528449  236.353    0.000  236.353    0.000 {built-in method torch._C._nn.mse_loss}
               45590486  232.756    0.000  232.756    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                7633397   16.798    0.000  232.010    0.000 pooling.py:156(forward)
                2510482  223.511    0.000  229.618    0.000 agent.py:134(convert_values)
               25584127   31.756    0.000  227.353    0.000 fromnumeric.py:2881(prod)
               10037932  226.974    0.000  226.974    0.000 {built-in method gather}
                7843293  222.159    0.000  222.159    0.000 {function Tensor.split at 0x7f1dcd7fd9d0}
                7633397   12.909    0.000  215.211    0.000 _jit_internal.py:237(fn)
               30533600  190.774    0.000  212.525    0.000 __init__.py:66(is_acceptable)
                7531446  203.729    0.000  203.729    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                7633397   14.120    0.000  201.036    0.000 functional.py:564(_max_pool2d)
                2614431   20.163    0.000  196.775    0.000 collector.py:8(collect)
               25584127   58.565    0.000  195.597    0.000 fromnumeric.py:70(_wrapreduction)
                2509483  192.068    0.000  192.068    0.000 memory.py:43(<listcomp>)
                7633397  185.863    0.000  185.863    0.000 {built-in method max_pool2d}
              269685223  182.842    0.000  182.957    0.000 module.py:758(__getattr__)
                5228863  175.009    0.000  175.009    0.000 {built-in method builtins.sum}
              274493442  169.614    0.000  169.614    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 8552391: <CHASER_U_S_0.1_0chaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0.1_0chaser_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Tue Dec  8 22:35:06 2020
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Dec  8 23:26:24 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec  8 23:26:24 2020
Terminated at Wed Dec  9 22:22:26 2020
Results reported at Wed Dec  9 22:22:26 2020

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

    CPU time :                                   86404.00 sec.
    Max Memory :                                 54577 MB
    Average Memory :                             53873.61 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6863.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82562 sec.
    Turnaround time :                            85640 sec.

The output (if any) is above this job summary.

