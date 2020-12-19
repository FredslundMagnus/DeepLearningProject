/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py:152: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  if state_differences is not 0:

    Name :                      U_S_0.1_0.1returnmaze-0
    Discount :                  0.99
    Environment :               maze
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


      13046241640 function calls (12854291469 primitive calls) in 82527.92 seconds

##    Ordered by: cumulative time
   List reduced from 1362 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82527.923 82527.923 {built-in method builtins.exec}
                      1    0.134    0.134 82527.923 82527.923 <string>:1(<module>)
                      1  420.274  420.274 82527.786 82527.786 main.py:92(main)
                2238796  189.850    0.000 53988.288    0.024 agent.py:89(learn)
                2149840  752.266    0.000 53273.707    0.025 agent.py:102(TD_learn)
                2149840  158.918    0.000 24254.701    0.011 memory.py:35(sample_distribution)
                2149840  298.218    0.000 23536.355    0.011 helpers.py:15(stack)
        209320182/17376631  947.050    0.000 14627.515    0.001 module.py:715(_call_impl)
                6538476  178.024    0.000 12742.362    0.002 agent.py:231(forward)
               26154010 12447.111    0.000 12447.138    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               23915108 11432.427    0.000 11432.427    0.000 {built-in method cat}
                6449520   42.225    0.000 9614.119    0.001 grad_mode.py:23(decorate_context)
                2238796  281.625    0.000 9517.156    0.004 agent.py:72(chooseMulti)
                6449520  277.674    0.000 9498.458    0.001 adam.py:55(step)
                2238796   61.782    0.000 9471.868    0.004 environments.py:83(step)
               30542539  275.334    0.000 9383.773    0.000 container.py:115(forward)
                2150830   43.738    0.000 8928.190    0.004 agent.py:58(rememberMulti)
                2150830  398.267    0.000 8633.720    0.004 agent.py:60(<listcomp>)
                6449520 1763.652    0.000 8179.458    0.001 functional.py:53(adam)
              377710605 8128.579    0.000 8128.579    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6449520   45.144    0.000 6175.556    0.001 tensor.py:181(backward)
                2238796   71.988    0.000 6147.809    0.003 environments.py:85(<listcomp>)
                6449520   26.044    0.000 6130.412    0.001 __init__.py:68(backward)
               44904950 1435.310    0.000 6096.465    0.000 helpers.py:8(clean)
                6449520 5930.782    0.001 5930.782    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               51354470 5170.595    0.000 5170.595    0.000 {built-in method as_tensor}
               39230856   73.347    0.000 3752.435    0.000 conv.py:422(forward)
               39230856   79.461    0.000 3648.064    0.000 conv.py:414(_conv_forward)
               39230856 3555.147    0.000 3555.147    0.000 {built-in method conv2d}
                2238796   50.847    0.000 3062.215    0.001 environments.py:84(<listcomp>)
               44775920  183.981    0.000 3011.368    0.000 interop.py:274(step)
               39319809   91.410    0.000 2572.153    0.000 linear.py:92(forward)
               39319809  275.677    0.000 2438.603    0.000 functional.py:1669(linear)
                6538482  392.019    0.000 2322.066    0.000 rnn.py:110(flatten_parameters)
              451466508 1208.255    0.000 1934.909    0.000 tensor.py:933(grad)
                6449520  187.788    0.000 1893.927    0.000 optimizer.py:167(zero_grad)
                2238796  107.257    0.000 1860.695    0.001 agent.py:87(<listcomp>)
              128990400 1723.774    0.000 1723.774    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6538476   73.116    0.000 1660.529    0.000 rnn.py:555(forward)
               74162030   73.964    0.000 1620.647    0.000 activation.py:713(forward)
                6538479 1550.317    0.000 1550.317    0.000 {built-in method _cudnn_rnn_flatten_weight}
               74162030  106.253    0.000 1546.683    0.000 functional.py:1292(leaky_relu)
               44775920   22.923    0.000 1506.788    0.000 wrapper.py:25(act)
                6538476 1503.699    0.000 1503.699    0.000 {built-in method lstm}
               44775920   74.678    0.000 1483.865    0.000 env.py:197(act)
              128990400 1454.514    0.000 1454.514    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               44775920  159.074    0.000 1438.651    0.000 exploration.py:34(epsilonGreedy)
               74162030 1431.138    0.000 1431.138    0.000 {built-in method torch._C._nn.leaky_relu}
               44775920 1363.261    0.000 1367.503    0.000 libenv.py:352(act)
                4388635   17.603    0.000 1358.049    0.000 agent.py:247(avoid_similar_state)
               32603424 1338.723    0.000 1338.723    0.000 {built-in method addmm}
               64495200  919.665    0.000  919.665    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              555281763  322.732    0.000  886.546    0.000 overrides.py:1073(has_torch_function)
               64495200  838.906    0.000  838.906    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89680870   79.158    0.000  793.767    0.000 extract_dict_ob.py:9(observe)
               64495200  765.208    0.000  765.208    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               89680870   43.689    0.000  714.608    0.000 wrapper.py:19(observe)
               64495200  690.148    0.000  690.148    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               89680870  173.266    0.000  670.919    0.000 libenv.py:344(observe)
              419935213  641.695    0.000  641.695    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               64495200  538.790    0.000  538.790    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              607500636  219.286    0.000  538.680    0.000 {built-in method builtins.any}
                   2194    0.953    0.000  524.731    0.239 agent.py:157(update_target_network)
              134456790  147.223    0.000  487.574    0.000 libenv.py:281(_maybe_copy_dict)
              403372564  433.030    0.000  433.030    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6449520   11.733    0.000  430.896    0.000 loss.py:445(forward)
                6449520   40.514    0.000  419.163    0.000 functional.py:2637(mse_loss)
               43016600  388.206    0.000  388.206    0.000 memory.py:17(inner)
               39319809  388.177    0.000  388.177    0.000 {method 't' of 'torch._C._TensorBase' objects}
               11262768  152.706    0.000  386.995    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6716388   12.955    0.000  384.915    0.000 functional.py:74(split)
               44775920   43.426    0.000  372.409    0.000 wrapper.py:22(get_info)
                6716388   29.711    0.000  371.104    0.000 tensor.py:460(split)
                6716388  339.766    0.000  339.766    0.000 {function Tensor.split at 0x7fbe0fcd2ca0}
               44775920  169.981    0.000  328.983    0.000 libenv.py:363(get_info)
               44775920  314.788    0.000  314.788    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
             1149883335  253.499    0.000  314.727    0.000 overrides.py:1086(<genexpr>)
               30455419  279.667    0.000  301.443    0.000 module.py:781(__setattr__)
                2149840  232.884    0.000  300.669    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               10749200  298.089    0.000  298.089    0.000 {built-in method gather}
                2150839  277.543    0.000  280.819    0.000 agent.py:148(convert_values)
               46930148  275.998    0.000  275.998    0.000 {built-in method numpy.array}
               24675516   23.571    0.000  271.834    0.000 <__array_function__ internals>:2(prod)
                6449520  269.193    0.000  269.193    0.000 {built-in method torch._C._nn.mse_loss}
                   2194   75.432    0.034  266.140    0.121 memory.py:45(update_distribution)
               38963988  263.929    0.000  263.929    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6716385  258.644    0.000  258.644    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                4301660   22.966    0.000  250.732    0.000 tensor.py:576(__iter__)
               24675556   18.777    0.000  243.878    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6538476   13.492    0.000  242.085    0.000 pooling.py:152(forward)
                   4388  205.317    0.047  232.637    0.053 {built-in method _pickle.loads}
                6538476   10.941    0.000  228.592    0.000 _jit_internal.py:257(fn)
               24675516   29.759    0.000  225.101    0.000 fromnumeric.py:2881(prod)
                4301660  218.557    0.000  218.557    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                6538476   11.765    0.000  216.469    0.000 functional.py:574(_max_pool2d)
                6538476  203.915    0.000  203.915    0.000 {built-in method max_pool2d}
                2238796   30.249    0.000  200.062    0.000 environments.py:86(<listcomp>)
               24675516   56.184    0.000  195.342    0.000 fromnumeric.py:70(_wrapreduction)
               64495446   87.275    0.000  191.422    0.000 tensor.py:596(__hash__)
               10838155  186.889    0.000  186.889    0.000 {method 'type' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 8575818: <U_S_0.1_0.1returnmaze_0> in cluster <dcc> Done

Job <U_S_0.1_0.1returnmaze_0> was submitted from host <n-62-30-3> by user <s183914> in cluster <dcc> at Fri Dec 18 16:26:01 2020
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Dec 18 21:28:47 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 18 21:28:47 2020
Terminated at Sat Dec 19 20:24:25 2020
Results reported at Sat Dec 19 20:24:25 2020

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

    CPU time :                                   85073.00 sec.
    Max Memory :                                 56877 MB
    Average Memory :                             56178.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4563.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82538 sec.
    Turnaround time :                            100704 sec.

The output (if any) is above this job summary.

