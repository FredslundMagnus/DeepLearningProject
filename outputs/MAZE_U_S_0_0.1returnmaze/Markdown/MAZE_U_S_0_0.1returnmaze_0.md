
    Name :                      MAZE_U_S_0_0.1returnmaze-0
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11382692573 function calls (11195176680 primitive calls) in 82533.18 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82533.179 82533.179 {built-in method builtins.exec}
                      1    0.190    0.190 82533.179 82533.179 <string>:1(<module>)
                      1  599.543  599.543 82532.984 82532.984 main.py:92(main)
                1909056  353.690    0.000 57948.101    0.030 agent.py:84(learn)
                1832094  687.120    0.000 56983.861    0.031 agent.py:99(TD_learn)
                1832094  156.847    0.000 34338.817    0.019 memory.py:35(sample_distribution)
                1832094  313.551    0.000 33621.060    0.018 helpers.py:15(stack)
               16719732 21438.090    0.001 21438.090    0.001 {built-in method cat}
        200411892/12902619  931.425    0.000 13350.135    0.001 module.py:715(_call_impl)
                5573244  188.126    0.000 12372.563    0.002 agent.py:231(forward)
               18552933 11409.964    0.001 11409.965    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                1909056  165.864    0.000 9337.258    0.005 agent.py:70(chooseMulti)
               29699313  232.153    0.000 8372.767    0.000 container.py:115(forward)
                1909056   63.941    0.000 7918.075    0.004 environments.py:83(step)
              247349820 7885.010    0.000 7885.010    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1833093   82.294    0.000 6548.905    0.004 agent.py:58(rememberMulti)
                5496282   39.944    0.000 6266.183    0.001 grad_mode.py:23(decorate_context)
                5496282  243.237    0.000 6162.813    0.001 adam.py:55(step)
                1833093  200.881    0.000 6110.094    0.003 agent.py:62(<listcomp>)
                5496282 1181.138    0.000 5080.192    0.001 functional.py:53(adam)
                1909056   51.942    0.000 5008.590    0.003 environments.py:85(<listcomp>)
               38319055 1297.808    0.000 4977.298    0.000 helpers.py:8(clean)
                5496282   40.621    0.000 4754.683    0.001 tensor.py:181(backward)
                5496282   26.428    0.000 4714.062    0.001 __init__.py:68(backward)
                5496282 4550.900    0.001 4550.900    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               43815337 4332.256    0.000 4332.256    0.000 {built-in method as_tensor}
                1833093   75.351    0.000 3444.516    0.002 agent.py:82(<listcomp>)
               36661860  108.576    0.000 3159.279    0.000 exploration.py:34(epsilonGreedy)
               33439464   66.084    0.000 3122.582    0.000 conv.py:422(forward)
               33439464   77.434    0.000 3025.363    0.000 conv.py:414(_conv_forward)
               33439464 2932.652    0.000 2932.652    0.000 {built-in method conv2d}
                1909056   42.901    0.000 2665.022    0.001 environments.py:84(<listcomp>)
               38181120  153.866    0.000 2622.121    0.000 interop.py:274(step)
               44511987   98.506    0.000 2599.046    0.000 linear.py:92(forward)
               44511987  251.721    0.000 2446.864    0.000 functional.py:1669(linear)
                5573250  367.203    0.000 1992.689    0.000 rnn.py:110(flatten_parameters)
                5573244   73.886    0.000 1813.811    0.000 rnn.py:555(forward)
                5573244 1655.410    0.000 1655.410    0.000 {built-in method lstm}
              384739848  878.170    0.000 1481.531    0.000 tensor.py:933(grad)
               39012708 1411.826    0.000 1411.826    0.000 {built-in method addmm}
               70545114   69.119    0.000 1311.014    0.000 activation.py:713(forward)
               38181120   18.495    0.000 1290.015    0.000 wrapper.py:25(act)
                5496282  128.320    0.000 1284.429    0.000 optimizer.py:167(zero_grad)
               38181120   51.940    0.000 1271.519    0.000 env.py:197(act)
               70545114  100.813    0.000 1241.895    0.000 functional.py:1292(leaky_relu)
               38181120 1188.378    0.000 1192.097    0.000 libenv.py:352(act)
                5573247 1164.884    0.000 1164.884    0.000 {built-in method _cudnn_rnn_flatten_weight}
               70545114 1131.540    0.000 1131.540    0.000 {built-in method torch._C._nn.leaky_relu}
              109925640 1029.117    0.000 1029.117    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              109925640  852.778    0.000  852.778    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              484214901  266.176    0.000  775.807    0.000 overrides.py:1073(has_torch_function)
               76500175   59.015    0.000  733.287    0.000 extract_dict_ob.py:9(observe)
               76500175   35.381    0.000  674.272    0.000 wrapper.py:19(observe)
               76500175  159.509    0.000  638.891    0.000 libenv.py:344(observe)
                   1909    1.205    0.001  610.549    0.320 agent.py:157(update_target_network)
               54962820  571.541    0.000  571.541    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               54962820  536.771    0.000  536.771    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1833093    4.954    0.000  492.734    0.000 agent.py:249(avoid_similar_state)
              539719476  196.181    0.000  490.198    0.000 {built-in method builtins.any}
              114681295  132.105    0.000  482.150    0.000 libenv.py:281(_maybe_copy_dict)
               54962820  478.269    0.000  478.269    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               36661860  450.857    0.000  450.857    0.000 memory.py:17(inner)
              344045794  424.112    0.000  424.112    0.000 {method 'copy' of 'numpy.ndarray' objects}
               25958999  400.132    0.000  421.255    0.000 module.py:781(__setattr__)
               54962820  412.062    0.000  412.062    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               44511987  391.152    0.000  391.152    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5727168   12.116    0.000  389.153    0.000 functional.py:74(split)
                5727168   25.565    0.000  376.238    0.000 tensor.py:460(split)
              281488995  361.228    0.000  361.228    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                5496282   11.885    0.000  360.100    0.000 loss.py:445(forward)
               10857564  137.134    0.000  359.013    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                5727168  349.345    0.000  349.345    0.000 {function Tensor.split at 0x7f21f4716d30}
                5496282   43.341    0.000  348.214    0.000 functional.py:2637(mse_loss)
                   1909   88.778    0.047  325.078    0.170 memory.py:45(update_distribution)
               38181120   35.854    0.000  318.205    0.000 wrapper.py:22(get_info)
               40017032  303.160    0.000  303.160    0.000 {built-in method numpy.array}
               54962820  295.859    0.000  295.859    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1012941789  234.053    0.000  289.354    0.000 overrides.py:1086(<genexpr>)
                1832094  215.183    0.000  282.749    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               38181120  141.859    0.000  282.351    0.000 libenv.py:363(get_info)
               10992564  281.121    0.000  281.121    0.000 {built-in method gather}
               23547362   24.298    0.000  261.379    0.000 <__array_function__ internals>:2(prod)
                   3818  235.593    0.062  258.807    0.068 {built-in method _pickle.loads}
               42446010  241.725    0.000  241.725    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               23547402   18.216    0.000  232.903    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                5573244   18.714    0.000  222.628    0.000 pooling.py:152(forward)
                1833093  193.707    0.000  222.116    0.000 agent.py:149(convert_values)
               38181120  217.659    0.000  217.659    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               23547362   30.055    0.000  214.687    0.000 fromnumeric.py:2881(prod)
                5496282  209.367    0.000  209.367    0.000 {built-in method torch._C._nn.mse_loss}
                1978175  206.354    0.000  206.354    0.000 {built-in method tensor}
                5573244   10.692    0.000  203.914    0.000 _jit_internal.py:257(fn)
                5573244   12.492    0.000  192.238    0.000 functional.py:574(_max_pool2d)
               22292988  170.834    0.000  192.032    0.000 __init__.py:67(is_acceptable)
                5499279  185.675    0.000  185.675    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               23547362   54.568    0.000  184.632    0.000 fromnumeric.py:70(_wrapreduction)
                1909056   22.933    0.000  180.523    0.000 environments.py:86(<listcomp>)
                5573244  178.967    0.000  178.967    0.000 {built-in method max_pool2d}
                1832094  176.246    0.000  176.246    0.000 memory.py:43(<listcomp>)
               54963066   71.729    0.000  158.672    0.000 tensor.py:596(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8570466: <MAZE_U_S_0_0.1returnmaze_0> in cluster <dcc> Done

Job <MAZE_U_S_0_0.1returnmaze_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Dec 16 20:56:12 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec 17 15:44:43 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec 17 15:44:43 2020
Terminated at Fri Dec 18 14:40:33 2020
Results reported at Fri Dec 18 14:40:33 2020

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

    CPU time :                                   92388.00 sec.
    Max Memory :                                 54639 MB
    Average Memory :                             54000.70 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6801.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82552 sec.
    Turnaround time :                            150261 sec.

The output (if any) is above this job summary.

