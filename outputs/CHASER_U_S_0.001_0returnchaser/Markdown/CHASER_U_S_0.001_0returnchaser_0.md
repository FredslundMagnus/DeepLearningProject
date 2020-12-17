
    Name :                      CHASER_U_S_0.001_0returnchaser-0
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
    Uncertainty weight :        0.001
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14930586603 function calls (14683961454 primitive calls) in 82513.99 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82513.986 82513.986 {built-in method builtins.exec}
                      1    0.027    0.027 82513.986 82513.986 <string>:1(<module>)
                      1  534.450  534.450 82513.957 82513.957 main.py:92(main)
                2510684  265.331    0.000 54458.157    0.022 agent.py:84(learn)
                2409734  806.719    0.000 53594.264    0.022 agent.py:99(TD_learn)
                2409734  166.853    0.000 26495.069    0.011 memory.py:35(sample_distribution)
                2409734  251.613    0.000 25720.392    0.011 helpers.py:15(stack)
        263588616/16970087 1133.358    0.000 15288.309    0.001 module.py:715(_call_impl)
                7330152  210.229    0.000 14135.403    0.002 agent.py:231(forward)
               24401297 13226.716    0.001 13226.718    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               21990456 11876.108    0.001 11876.108    0.001 {built-in method cat}
                2510684  186.436    0.000 11540.195    0.005 agent.py:70(chooseMulti)
               39061493  277.750    0.000 9832.851    0.000 container.py:115(forward)
              328139764 9513.357    0.000 9513.357    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2510684   67.384    0.000 9127.418    0.004 environments.py:83(step)
                7229202   48.110    0.000 7808.640    0.001 grad_mode.py:23(decorate_context)
                7229202  303.070    0.000 7681.454    0.001 adam.py:55(step)
                2410733   90.537    0.000 6669.325    0.003 agent.py:58(rememberMulti)
                7229202 1459.582    0.000 6318.643    0.001 functional.py:53(adam)
                2410733  236.936    0.000 6204.189    0.003 agent.py:62(<listcomp>)
                2510684   63.716    0.000 5701.881    0.002 environments.py:85(<listcomp>)
               50516175 1436.204    0.000 5677.383    0.000 helpers.py:8(clean)
                7229202   52.586    0.000 5668.483    0.001 tensor.py:181(backward)
                7229202   34.302    0.000 5615.896    0.001 __init__.py:68(backward)
                7229202 5411.575    0.001 5411.575    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2410733   91.957    0.000 5030.214    0.002 agent.py:82(<listcomp>)
               57745377 4820.575    0.000 4820.575    0.000 {built-in method as_tensor}
               48214660  137.974    0.000 4701.053    0.000 exploration.py:34(epsilonGreedy)
               43980912   77.309    0.000 3656.926    0.000 conv.py:422(forward)
               43980912   99.319    0.000 3543.824    0.000 conv.py:414(_conv_forward)
               43980912 3428.256    0.000 3428.256    0.000 {built-in method conv2d}
                2510684   51.816    0.000 3140.255    0.001 environments.py:84(<listcomp>)
               50213680  180.993    0.000 3088.440    0.000 interop.py:274(step)
               58543263  123.441    0.000 3038.270    0.000 linear.py:92(forward)
               58543263  308.249    0.000 2855.631    0.000 functional.py:1669(linear)
                7330158  409.386    0.000 2273.345    0.000 rnn.py:110(flatten_parameters)
              506044248 1124.227    0.000 1889.092    0.000 tensor.py:933(grad)
                7330152   87.464    0.000 1809.560    0.000 rnn.py:555(forward)
               51311064 1657.592    0.000 1657.592    0.000 {built-in method addmm}
                7229202  167.300    0.000 1638.816    0.000 optimizer.py:167(zero_grad)
                7330152 1627.246    0.000 1627.246    0.000 {built-in method lstm}
               92783290   80.077    0.000 1539.223    0.000 activation.py:713(forward)
               50213680   23.261    0.000 1530.244    0.000 wrapper.py:25(act)
               50213680   63.280    0.000 1506.983    0.000 env.py:197(act)
               92783290  116.537    0.000 1459.146    0.000 functional.py:1292(leaky_relu)
               50213680 1404.278    0.000 1409.215    0.000 libenv.py:352(act)
                7330155 1362.567    0.000 1362.567    0.000 {built-in method _cudnn_rnn_flatten_weight}
               92783290 1330.910    0.000 1330.910    0.000 {built-in method torch._C._nn.leaky_relu}
              144584040 1278.734    0.000 1278.734    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              144584040 1071.073    0.000 1071.073    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              636879777  332.967    0.000  980.869    0.000 overrides.py:1073(has_torch_function)
              100729855   74.844    0.000  854.622    0.000 extract_dict_ob.py:9(observe)
              100729855   43.248    0.000  779.777    0.000 wrapper.py:19(observe)
              100729855  196.444    0.000  736.529    0.000 libenv.py:344(observe)
               72292020  705.292    0.000  705.292    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               72292020  658.291    0.000  658.291    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              709881468  256.888    0.000  623.041    0.000 {built-in method builtins.any}
                   2510    0.973    0.000  598.561    0.238 agent.py:157(update_target_network)
               72292020  596.394    0.000  596.394    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2410733    6.374    0.000  577.563    0.000 agent.py:249(avoid_similar_state)
              150943535  159.327    0.000  533.358    0.000 libenv.py:281(_maybe_copy_dict)
               72292020  523.794    0.000  523.794    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              452833115  459.938    0.000  459.938    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7229202   15.660    0.000  429.818    0.000 loss.py:445(forward)
               58543263  425.755    0.000  425.755    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7229202   49.828    0.000  414.159    0.000 functional.py:2637(mse_loss)
              372801183  401.895    0.000  401.895    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               34141911  373.314    0.000  401.153    0.000 module.py:781(__setattr__)
                7532052   13.361    0.000  394.753    0.000 functional.py:74(split)
                7532052   32.338    0.000  380.374    0.000 tensor.py:460(split)
               50213680   40.917    0.000  378.116    0.000 wrapper.py:22(get_info)
               11434344  143.483    0.000  374.195    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               72292020  368.018    0.000  368.018    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1332302817  293.078    0.000  360.567    0.000 overrides.py:1086(<genexpr>)
                7532052  346.376    0.000  346.376    0.000 {function Tensor.split at 0x7f55af26ed30}
               48214660  339.114    0.000  339.114    0.000 memory.py:17(inner)
               50213680  174.918    0.000  337.198    0.000 libenv.py:363(get_info)
                2409734  254.795    0.000  330.573    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               14458404  320.667    0.000  320.667    0.000 {built-in method gather}
                   2510   89.600    0.036  320.284    0.128 memory.py:45(update_distribution)
               52628434  312.712    0.000  312.712    0.000 {built-in method numpy.array}
               25278562   24.036    0.000  273.079    0.000 <__array_function__ internals>:2(prod)
               55827682  272.364    0.000  272.364    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2410733  226.818    0.000  270.011    0.000 agent.py:149(convert_values)
                   5020  224.256    0.045  251.526    0.050 {built-in method _pickle.loads}
                7229202  247.311    0.000  247.311    0.000 {built-in method torch._C._nn.mse_loss}
                7330152   20.005    0.000  247.148    0.000 pooling.py:152(forward)
               50213680  245.598    0.000  245.598    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25278602   19.432    0.000  244.637    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7330152   12.539    0.000  227.143    0.000 _jit_internal.py:257(fn)
               25278562   30.624    0.000  225.205    0.000 fromnumeric.py:2881(prod)
                2510684   26.232    0.000  217.898    0.000 environments.py:86(<listcomp>)
                7330152   14.969    0.000  213.473    0.000 functional.py:574(_max_pool2d)
                7232199  209.077    0.000  209.077    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2601491  207.523    0.000  207.523    0.000 {built-in method tensor}
               29320620  184.156    0.000  204.202    0.000 __init__.py:67(is_acceptable)
                7330152  197.627    0.000  197.627    0.000 {built-in method max_pool2d}
               72292266   88.115    0.000  196.830    0.000 tensor.py:596(__hash__)
               25278562   59.424    0.000  194.581    0.000 fromnumeric.py:70(_wrapreduction)
               50213700   32.439    0.000  191.670    0.000 environments.py:89(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8557122: <CHASER_U_S_0.001_0returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0.001_0returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:12 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Dec 15 16:24:06 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec 15 16:24:06 2020
Terminated at Wed Dec 16 15:19:23 2020
Results reported at Wed Dec 16 15:19:23 2020

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

    CPU time :                                   85557.00 sec.
    Max Memory :                                 55010 MB
    Average Memory :                             54307.83 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6430.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82578 sec.
    Turnaround time :                            432671 sec.

The output (if any) is above this job summary.

