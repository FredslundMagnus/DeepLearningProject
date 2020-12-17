[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0_0.001returnbigfish-0
    Discount :                  0.995
    Environment :               bigfish
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
    State difference weight :   0.001
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11112598971 function calls (10856423198 primitive calls) in 82523.72 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82523.724 82523.724 {built-in method builtins.exec}
                      1    0.021    0.021 82523.723 82523.723 <string>:1(<module>)
                      1  572.941  572.941 82523.701 82523.701 main.py:92(main)
                2607976  274.113    0.000 53178.219    0.020 agent.py:84(learn)
                2503028  785.317    0.000 52275.010    0.021 agent.py:99(TD_learn)
                2503028  180.525    0.000 28015.589    0.011 memory.py:35(sample_distribution)
                2503028  331.505    0.000 27185.928    0.011 helpers.py:15(stack)
        273796302/17627143 1141.398    0.000 14822.368    0.001 module.py:710(_call_impl)
               25346231 13775.656    0.001 13775.702    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                7614032  222.420    0.000 13701.032    0.002 agent.py:231(forward)
                2607976  189.033    0.000 13437.183    0.005 agent.py:70(chooseMulti)
               22842096 12853.352    0.001 12853.352    0.001 {built-in method cat}
              341184443 11658.249    0.000 11658.249    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               40574187  274.710    0.000 9382.292    0.000 container.py:115(forward)
                2607976   71.777    0.000 8549.016    0.003 environments.py:83(step)
                2504027   87.080    0.000 7211.647    0.003 agent.py:82(<listcomp>)
               50080540  132.836    0.000 6909.142    0.000 exploration.py:34(epsilonGreedy)
                2504027   89.193    0.000 6589.677    0.003 agent.py:58(rememberMulti)
                7509084   40.062    0.000 6456.641    0.001 grad_mode.py:12(decorate_context)
                7509084 1633.470    0.000 6365.866    0.001 adam.py:51(step)
                2504027  221.684    0.000 6142.584    0.002 agent.py:62(<listcomp>)
                7509084   30.709    0.000 5487.208    0.001 tensor.py:155(backward)
                2607976   58.793    0.000 5460.193    0.002 environments.py:85(<listcomp>)
                7509084   38.351    0.000 5456.499    0.001 __init__.py:57(backward)
               52369545 1444.417    0.000 5426.753    0.000 helpers.py:8(clean)
                7509084 5260.724    0.001 5260.724    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               59878629 4553.529    0.000 4553.529    0.000 {built-in method as_tensor}
               45684192   79.750    0.000 3518.125    0.000 conv.py:418(forward)
               45684192   95.601    0.000 3401.063    0.000 conv.py:410(_conv_forward)
               45684192 3288.849    0.000 3288.849    0.000 {built-in method conv2d}
               60810305  119.478    0.000 2848.956    0.000 linear.py:90(forward)
                2607976   52.632    0.000 2823.395    0.001 environments.py:84(<listcomp>)
               52159520  184.334    0.000 2770.763    0.000 interop.py:274(step)
               60810305  304.886    0.000 2668.826    0.000 functional.py:1655(linear)
                7614038  392.819    0.000 2127.948    0.000 rnn.py:109(flatten_parameters)
                7614032   89.470    0.000 1897.546    0.000 rnn.py:550(forward)
                7614032 1706.458    0.000 1706.458    0.000 {built-in method lstm}
               53298224 1570.876    0.000 1570.876    0.000 {built-in method addmm}
               96376438   85.100    0.000 1434.441    0.000 activation.py:653(forward)
               96376438  120.630    0.000 1349.341    0.000 functional.py:1277(leaky_relu)
                7614035 1253.342    0.000 1253.342    0.000 {built-in method _cudnn_rnn_flatten_weight}
               96376438 1216.153    0.000 1216.153    0.000 {built-in method torch._C._nn.leaky_relu}
               52159520   22.756    0.000 1211.044    0.000 wrapper.py:25(act)
              150181680 1196.343    0.000 1196.343    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52159520   60.435    0.000 1188.288    0.000 env.py:197(act)
               52159520 1089.398    0.000 1094.463    0.000 libenv.py:352(act)
              150181680 1034.367    0.000 1034.367    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              104529065   74.196    0.000  836.557    0.000 extract_dict_ob.py:9(observe)
              104529065   44.855    0.000  762.361    0.000 wrapper.py:19(observe)
              104529065  188.179    0.000  717.507    0.000 libenv.py:344(observe)
               75090840  716.938    0.000  716.938    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   2607    1.030    0.000  629.096    0.241 agent.py:157(update_target_network)
               75090840  606.540    0.000  606.540    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7509084  106.820    0.000  603.546    0.000 optimizer.py:166(zero_grad)
                2504027    6.573    0.000  536.445    0.000 agent.py:249(avoid_similar_state)
              156688585  157.490    0.000  530.276    0.000 libenv.py:281(_maybe_copy_dict)
               75090840  492.903    0.000  492.903    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75090840  470.345    0.000  470.345    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              470068362  455.490    0.000  455.490    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7509084   14.797    0.000  432.941    0.000 loss.py:444(forward)
                7509084   58.864    0.000  418.144    0.000 functional.py:2621(mse_loss)
              387788714  415.485    0.000  415.485    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               35464019  380.134    0.000  406.711    0.000 module.py:774(__setattr__)
               52159520   42.800    0.000  388.265    0.000 wrapper.py:22(get_info)
               50080540  380.087    0.000  380.087    0.000 memory.py:17(inner)
               11533590  141.962    0.000  370.036    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               60810305  368.212    0.000  368.212    0.000 {method 't' of 'torch._C._TensorBase' objects}
               52159520  179.988    0.000  345.465    0.000 libenv.py:363(get_info)
               75090840  341.650    0.000  341.650    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2503028  259.857    0.000  337.676    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   2607   94.773    0.036  337.292    0.129 memory.py:45(update_distribution)
               54667762  325.815    0.000  325.815    0.000 {built-in method numpy.array}
               15018168  296.600    0.000  296.600    0.000 {built-in method gather}
                2504027  206.924    0.000  272.289    0.000 agent.py:149(convert_values)
               25570348   23.853    0.000  270.606    0.000 <__array_function__ internals>:2(prod)
                   5214  239.421    0.046  265.825    0.051 {built-in method _pickle.loads}
               57989436  260.046    0.000  260.046    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              375454308  210.422    0.000  245.424    0.000 tensor.py:725(grad)
               25570388   18.063    0.000  242.599    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7614032   22.313    0.000  238.034    0.000 pooling.py:156(forward)
                7823928   13.559    0.000  237.473    0.000 functional.py:68(split)
                7509084  233.502    0.000  233.502    0.000 {built-in method torch._C._nn.mse_loss}
               25570348   30.718    0.000  224.536    0.000 fromnumeric.py:2881(prod)
               52159520  222.986    0.000  222.986    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7823928   13.150    0.000  222.883    0.000 tensor.py:367(split)
               30456140  194.023    0.000  216.256    0.000 __init__.py:66(is_acceptable)
                7614032   13.139    0.000  215.721    0.000 _jit_internal.py:237(fn)
                2503028  211.793    0.000  211.793    0.000 memory.py:43(<listcomp>)
                2702157  209.340    0.000  209.340    0.000 {built-in method tensor}
                7823928  208.147    0.000  208.147    0.000 {function Tensor.split at 0x7f373c4099d0}
                7614032   15.916    0.000  201.282    0.000 functional.py:564(_max_pool2d)
               25570348   56.678    0.000  193.819    0.000 fromnumeric.py:70(_wrapreduction)
                2607976   27.654    0.000  193.651    0.000 environments.py:86(<listcomp>)
                7512081  191.464    0.000  191.464    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
              269000433  186.045    0.000  186.155    0.000 module.py:758(__getattr__)
                7614032  184.348    0.000  184.348    0.000 {built-in method max_pool2d}
                2607976   18.820    0.000  168.049    0.000 collector.py:8(collect)
               52159540   34.728    0.000  166.049    0.000 environments.py:89(reset)
               15019167  164.841    0.000  164.841    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                7509084   37.662    0.000  154.852    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8557630: <BIGFISH_U_S_0_0.001returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0_0.001returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:47 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Dec 16 14:01:42 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 16 14:01:42 2020
Terminated at Thu Dec 17 12:57:14 2020
Results reported at Thu Dec 17 12:57:14 2020

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

    CPU time :                                   87152.00 sec.
    Max Memory :                                 54200 MB
    Average Memory :                             53558.36 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7240.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82533 sec.
    Turnaround time :                            507327 sec.

The output (if any) is above this job summary.

