[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
                                                                                                                                                                                                                                    
    Name :                      Uncertainty0state_difference0chaser-0
    Discount :                  0.995
    Environment :               chaser
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
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


      11008659130 function calls (10753975141 primitive calls) in 82536.09 seconds

##    Ordered by: cumulative time
   List reduced from 1331 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82536.092 82536.092 {built-in method builtins.exec}
                      1    0.038    0.038 82536.092 82536.092 <string>:1(<module>)
                      1  569.146  569.146 82536.052 82536.052 main.py:92(main)
                2521875  218.472    0.000 52752.009    0.021 agent.py:86(learn)
                2521375  733.190    0.000 51503.369    0.020 agent.py:96(TD_learn)
                2521375  175.241    0.000 27184.390    0.011 memory.py:35(sample_distribution)
                2521375  271.357    0.000 26366.233    0.010 helpers.py:15(stack)
        272328000/17650625 1144.782    0.000 15010.160    0.001 module.py:710(_call_impl)
                7564625  227.011    0.000 13847.529    0.002 agent.py:212(forward)
               25215858 13828.598    0.001 13828.620    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2521875  188.254    0.000 13424.859    0.005 agent.py:74(chooseMulti)
               22693875 12046.024    0.001 12046.024    0.001 {built-in method cat}
              341592961 11636.132    0.000 11636.132    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               40345000  287.357    0.000 9524.476    0.000 container.py:115(forward)
                2521875   70.077    0.000 8935.267    0.004 environments.py:83(step)
                2521875   98.007    0.000 7223.164    0.003 agent.py:84(<listcomp>)
               50437500  137.505    0.000 6887.003    0.000 exploration.py:34(epsilonGreedy)
                2521875   92.002    0.000 6645.694    0.003 agent.py:62(rememberMulti)
                7564125   41.186    0.000 6594.111    0.001 grad_mode.py:12(decorate_context)
                7564125 1669.573    0.000 6502.657    0.001 adam.py:51(step)
                2521875  216.642    0.000 6181.972    0.002 agent.py:66(<listcomp>)
                7564125   32.065    0.000 5571.101    0.001 tensor.py:155(backward)
                7564125   38.236    0.000 5539.036    0.001 __init__.py:57(backward)
                2521875   59.770    0.000 5417.215    0.002 environments.py:85(<listcomp>)
               50835742 1425.674    0.000 5407.300    0.000 helpers.py:8(clean)
                7564125 5343.230    0.001 5343.230    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               58399867 4552.453    0.000 4552.453    0.000 {built-in method as_tensor}
               45387750   82.076    0.000 3533.113    0.000 conv.py:418(forward)
               45387750   91.941    0.000 3413.204    0.000 conv.py:410(_conv_forward)
               45387750 3304.395    0.000 3304.395    0.000 {built-in method conv2d}
                2521875   52.321    0.000 3200.866    0.001 environments.py:84(<listcomp>)
               50437500  188.754    0.000 3148.545    0.000 interop.py:274(step)
               60518000  125.118    0.000 2892.602    0.000 linear.py:90(forward)
               60518000  321.679    0.000 2704.724    0.000 functional.py:1655(linear)
                7564631  399.506    0.000 2197.051    0.000 rnn.py:109(flatten_parameters)
                7564625   89.928    0.000 1841.971    0.000 rnn.py:550(forward)
                7564625 1650.498    0.000 1650.498    0.000 {built-in method lstm}
               50437500   24.252    0.000 1579.224    0.000 wrapper.py:25(act)
               52952375 1575.206    0.000 1575.206    0.000 {built-in method addmm}
               50437500   63.351    0.000 1554.972    0.000 env.py:197(act)
               95819250   79.945    0.000 1488.193    0.000 activation.py:653(forward)
               50437500 1453.394    0.000 1458.301    0.000 libenv.py:352(act)
               95819250  129.513    0.000 1408.248    0.000 functional.py:1277(leaky_relu)
                7564628 1307.150    0.000 1307.150    0.000 {built-in method _cudnn_rnn_flatten_weight}
               95819250 1265.878    0.000 1265.878    0.000 {built-in method torch._C._nn.leaky_relu}
              151282500 1206.925    0.000 1206.925    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              151282500 1052.737    0.000 1052.737    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   5043    1.787    0.000 1030.169    0.204 agent.py:139(update_target_network)
              101273242   80.986    0.000  858.905    0.000 extract_dict_ob.py:9(observe)
              101273242   43.009    0.000  777.920    0.000 wrapper.py:19(observe)
               75641250  747.431    0.000  747.431    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              101273242  195.512    0.000  734.911    0.000 libenv.py:344(observe)
                   5043  183.186    0.036  670.992    0.133 memory.py:45(update_distribution)
                7564125  108.832    0.000  614.538    0.000 optimizer.py:166(zero_grad)
               75641250  614.037    0.000  614.037    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               52968961  569.238    0.000  569.238    0.000 {built-in method numpy.array}
                2521875    5.944    0.000  560.527    0.000 agent.py:230(avoid_similar_state)
              151710742  159.977    0.000  536.556    0.000 libenv.py:281(_maybe_copy_dict)
               75641250  499.146    0.000  499.146    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75641250  488.627    0.000  488.627    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              455137269  459.763    0.000  459.763    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7564125   15.179    0.000  448.829    0.000 loss.py:444(forward)
              378618643  444.803    0.000  444.803    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7564125   62.639    0.000  433.650    0.000 functional.py:2621(mse_loss)
               35303085  380.568    0.000  408.591    0.000 module.py:774(__setattr__)
               50437500   41.892    0.000  379.989    0.000 wrapper.py:22(get_info)
               11545196  144.514    0.000  376.905    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               60518000  375.871    0.000  375.871    0.000 {method 't' of 'torch._C._TensorBase' objects}
               50437500  362.831    0.000  362.831    0.000 memory.py:17(inner)
                2521375  265.971    0.000  347.353    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               75641250  343.465    0.000  343.465    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               50437500  175.766    0.000  338.098    0.000 libenv.py:363(get_info)
                  10086  255.664    0.025  306.108    0.030 {built-in method _pickle.loads}
                2521875  214.947    0.000  279.812    0.000 agent.py:131(convert_values)
               25611907   24.771    0.000  277.976    0.000 <__array_function__ internals>:2(prod)
              378206358  227.517    0.000  264.199    0.000 tensor.py:725(grad)
                7565625   14.023    0.000  249.685    0.000 functional.py:68(split)
               25611947   18.699    0.000  249.061    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                2521875   26.792    0.000  247.108    0.000 environments.py:86(<listcomp>)
                7564125  239.370    0.000  239.370    0.000 {built-in method torch._C._nn.mse_loss}
               50437500  238.153    0.000  238.153    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7564625   19.137    0.000  236.343    0.000 pooling.py:156(forward)
                7565625   14.310    0.000  234.557    0.000 tensor.py:367(split)
               25611907   31.824    0.000  230.362    0.000 fromnumeric.py:2881(prod)
               30258512  207.220    0.000  229.048    0.000 __init__.py:66(is_acceptable)
               10085500  224.204    0.000  224.204    0.000 {built-in method gather}
               45386750  224.178    0.000  224.178    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2905141  221.278    0.000  221.278    0.000 {built-in method tensor}
               50437520   33.940    0.000  220.330    0.000 environments.py:89(reset)
                7565625  218.587    0.000  218.587    0.000 {function Tensor.split at 0x7f77b26ca9d0}
                7564625   13.864    0.000  217.207    0.000 _jit_internal.py:237(fn)
                7564625   15.326    0.000  202.171    0.000 functional.py:564(_max_pool2d)
               25611907   59.637    0.000  198.538    0.000 fromnumeric.py:70(_wrapreduction)
                7565625  197.858    0.000  197.858    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2521375  196.560    0.000  196.560    0.000 memory.py:43(<listcomp>)
              267689818  194.791    0.000  195.007    0.000 module.py:758(__getattr__)
                7564625  185.884    0.000  185.884    0.000 {built-in method max_pool2d}
                2521875   17.092    0.000  168.487    0.000 collector.py:7(collect)
              272328000  157.832    0.000  157.832    0.000 {built-in method torch._C._get_tracing_state}
                7564125   37.626    0.000  154.807    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8483324: <Uncertainty0state_difference0chaser_0> in cluster <dcc> Done

Job <Uncertainty0state_difference0chaser_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Sat Dec  5 16:31:58 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Dec  7 07:33:00 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec  7 07:33:00 2020
Terminated at Tue Dec  8 06:28:50 2020
Results reported at Tue Dec  8 06:28:50 2020

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

    CPU time :                                   86478.00 sec.
    Max Memory :                                 54461 MB
    Average Memory :                             53761.46 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6979.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82551 sec.
    Turnaround time :                            223012 sec.

The output (if any) is above this job summary.


    Name :                      Uncertainty0state_difference0chaser-0
    Discount :                  0.995
    Environment :               chaser
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsintosoftmax
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      10553526018 function calls (10328261713 primitive calls) in 82535.80 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82535.798 82535.798 {built-in method builtins.exec}
                      1    0.035    0.035 82535.798 82535.798 <string>:1(<module>)
                      1  510.886  510.886 82535.761 82535.761 main.py:92(main)
                2230591  197.266    0.000 51877.280    0.023 agent.py:86(learn)
                2230091  798.938    0.000 50888.266    0.023 agent.py:96(TD_learn)
                2230091  144.597    0.000 24049.568    0.011 memory.py:35(sample_distribution)
                2230091  264.777    0.000 23368.210    0.010 helpers.py:15(stack)
        240869328/15611637 1038.622    0.000 15350.179    0.001 module.py:710(_call_impl)
                2230591  207.944    0.000 14429.513    0.006 agent.py:74(chooseMulti)
                6690773  207.545    0.000 14166.822    0.002 agent.py:212(forward)
               22303018 12176.500    0.001 12176.558    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20072319 10831.476    0.001 10831.476    0.001 {built-in method cat}
               35684456  293.826    0.000 9835.081    0.000 container.py:115(forward)
                2230591   60.606    0.000 8497.147    0.004 environments.py:83(step)
              301095772 8428.250    0.000 8428.250    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6690273   39.277    0.000 8149.374    0.001 grad_mode.py:12(decorate_context)
                2230591  146.750    0.000 8073.390    0.004 agent.py:84(<listcomp>)
                6690273 1940.920    0.000 8064.092    0.001 adam.py:51(step)
               44611820 1311.939    0.000 7542.461    0.000 exploration.py:40(epsintosoftmax)
                2230591   95.599    0.000 7033.065    0.003 agent.py:62(rememberMulti)
                2230591  285.933    0.000 6575.939    0.003 agent.py:66(<listcomp>)
                6690273   31.959    0.000 6048.831    0.001 tensor.py:155(backward)
                6690273   35.350    0.000 6016.872    0.001 __init__.py:57(backward)
                6690273 5816.905    0.001 5816.905    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2230591   62.714    0.000 5179.161    0.002 environments.py:85(<listcomp>)
               44977772 1255.357    0.000 5165.638    0.000 helpers.py:8(clean)
               51668045 4351.944    0.000 4351.944    0.000 {built-in method as_tensor}
               40144638   70.165    0.000 3646.420    0.000 conv.py:418(forward)
               40144638   81.751    0.000 3543.619    0.000 conv.py:410(_conv_forward)
               40144638 3447.586    0.000 3447.586    0.000 {built-in method conv2d}
               53527184  107.069    0.000 3038.642    0.000 linear.py:90(forward)
                2230591   47.632    0.000 3009.345    0.001 environments.py:84(<listcomp>)
               44611820  174.500    0.000 2961.713    0.000 interop.py:274(step)
               53527184  309.363    0.000 2878.350    0.000 functional.py:1655(linear)
               44611820 1671.475    0.000 2500.073    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6690779  372.387    0.000 2349.728    0.000 rnn.py:109(flatten_parameters)
                6690773   80.556    0.000 1752.461    0.000 rnn.py:550(forward)
               46835411 1708.226    0.000 1708.226    0.000 {built-in method addmm}
              133805460 1617.743    0.000 1617.743    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               84750458   72.453    0.000 1613.366    0.000 activation.py:653(forward)
                6690773 1578.682    0.000 1578.682    0.000 {built-in method lstm}
               84750458  110.259    0.000 1540.913    0.000 functional.py:1277(leaky_relu)
                6690776 1518.196    0.000 1518.196    0.000 {built-in method _cudnn_rnn_flatten_weight}
               44611820   20.034    0.000 1495.527    0.000 wrapper.py:25(act)
               44611820   64.819    0.000 1475.493    0.000 env.py:197(act)
               84750458 1420.453    0.000 1420.453    0.000 {built-in method torch._C._nn.leaky_relu}
              133805460 1403.109    0.000 1403.109    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               44611820 1368.499    0.000 1372.644    0.000 libenv.py:352(act)
               66902730  887.807    0.000  887.807    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               89589592   71.389    0.000  806.104    0.000 extract_dict_ob.py:9(observe)
                6690273  124.559    0.000  798.335    0.000 optimizer.py:166(zero_grad)
                   4461    1.560    0.000  791.748    0.177 agent.py:139(update_target_network)
               66902730  740.052    0.000  740.052    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89589592   36.953    0.000  734.715    0.000 wrapper.py:19(observe)
               33357934   63.134    0.000  705.413    0.000 functional.py:1465(softmax)
               89589592  191.573    0.000  697.762    0.000 libenv.py:344(observe)
               66902730  643.719    0.000  643.719    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               58095937   66.358    0.000  637.406    0.000 <__array_function__ internals>:2(prod)
               33357934  636.788    0.000  636.788    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               66902730  619.692    0.000  619.692    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2230591    5.752    0.000  588.182    0.000 agent.py:230(avoid_similar_state)
              333816774  585.010    0.000  585.010    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               58095977   45.980    0.000  558.987    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               58095937   72.122    0.000  513.007    0.000 fromnumeric.py:2881(prod)
               66902730  492.195    0.000  492.195    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              134201412  142.301    0.000  491.293    0.000 libenv.py:281(_maybe_copy_dict)
                   4461  141.712    0.032  477.705    0.107 memory.py:45(update_distribution)
                6690273   14.194    0.000  447.292    0.000 loss.py:444(forward)
               53527184  441.441    0.000  441.441    0.000 {method 't' of 'torch._C._TensorBase' objects}
               58095937  135.504    0.000  440.885    0.000 fromnumeric.py:70(_wrapreduction)
              402608697  436.343    0.000  436.343    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6690273   55.203    0.000  433.099    0.000 functional.py:2621(mse_loss)
               46850833  414.743    0.000  414.743    0.000 {built-in method numpy.array}
               44611820  384.180    0.000  384.180    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               31225109  342.592    0.000  366.340    0.000 module.py:774(__setattr__)
               44611820  355.584    0.000  355.584    0.000 memory.py:17(inner)
               44611820   39.072    0.000  351.081    0.000 wrapper.py:22(get_info)
               44611820  164.644    0.000  312.009    0.000 libenv.py:363(get_info)
                2230591  259.295    0.000  288.778    0.000 agent.py:131(convert_values)
                2230091  213.531    0.000  273.067    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               60330489  268.623    0.000  268.623    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                   8922  219.518    0.025  266.479    0.030 {built-in method _pickle.loads}
               40143638  259.016    0.000  259.016    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6690273  257.600    0.000  257.600    0.000 {built-in method torch._C._nn.mse_loss}
                6691773   11.994    0.000  255.917    0.000 functional.py:68(split)
              334513758  221.166    0.000  254.554    0.000 tensor.py:725(grad)
                2230591   24.315    0.000  248.035    0.000 environments.py:86(<listcomp>)
                6691773   13.032    0.000  243.142    0.000 tensor.py:367(split)
                6690773   16.906    0.000  241.833    0.000 pooling.py:156(forward)
                8920364  241.068    0.000  241.068    0.000 {built-in method gather}
                6691773  228.721    0.000  228.721    0.000 {function Tensor.split at 0x7fcffb3ba9d0}
                6690773   11.300    0.000  224.926    0.000 _jit_internal.py:237(fn)
               44611840   31.538    0.000  223.748    0.000 environments.py:89(reset)
               26763104  196.861    0.000  217.578    0.000 __init__.py:66(is_acceptable)
                6691773  213.845    0.000  213.845    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6690773   12.823    0.000  212.417    0.000 functional.py:564(_max_pool2d)
                2569625  209.588    0.000  209.588    0.000 {built-in method tensor}
                6690773  198.847    0.000  198.847    0.000 {built-in method max_pool2d}
              240869328  181.238    0.000  181.238    0.000 {built-in method torch._C._get_tracing_state}
                2230091  173.385    0.000  173.385    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8483325: <Uncertainty0state_difference0chaser_0> in cluster <dcc> Done

Job <Uncertainty0state_difference0chaser_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Sat Dec  5 16:31:58 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Dec  7 09:50:00 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec  7 09:50:00 2020
Terminated at Tue Dec  8 08:45:51 2020
Results reported at Tue Dec  8 08:45:51 2020

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

    CPU time :                                   84947.00 sec.
    Max Memory :                                 54325 MB
    Average Memory :                             53620.77 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7115.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82552 sec.
    Turnaround time :                            231233 sec.

The output (if any) is above this job summary.

