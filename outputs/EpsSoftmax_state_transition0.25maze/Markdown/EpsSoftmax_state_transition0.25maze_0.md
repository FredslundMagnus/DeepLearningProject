
    Name :                      EpsSoftmax_state_transition0.25maze-0
    Discount :                  0.995
    Environment :               maze
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      0
    Exploration :               epsintosoftmax
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.25
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13216601965 function calls (12992009263 primitive calls) in 82530.86 seconds

##    Ordered by: cumulative time
   List reduced from 1358 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82530.858 82530.858 {built-in method builtins.exec}
                      1    0.159    0.159 82530.858 82530.858 <string>:1(<module>)
                      1  508.961  508.961 82530.695 82530.695 main.py:92(main)
                2223942  192.866    0.000 51410.290    0.023 agent.py:86(learn)
                2223442  580.496    0.000 50323.710    0.023 agent.py:96(TD_learn)
                2223442  152.884    0.000 27193.488    0.012 memory.py:35(sample_distribution)
                2223442  289.782    0.000 26477.040    0.012 helpers.py:15(stack)
        237927794/13341652 1063.992    0.000 14668.044    0.001 module.py:715(_call_impl)
                2223942  187.484    0.000 14517.353    0.007 agent.py:74(chooseMulti)
                6670826  212.095    0.000 13672.001    0.002 agent.py:212(forward)
               20012478 13506.697    0.001 13506.697    0.001 {built-in method cat}
               22236528 12444.035    0.001 12444.079    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               35578072  273.588    0.000 9621.025    0.000 container.py:115(forward)
                2223942   67.893    0.000 9187.287    0.004 environments.py:83(step)
              300168893 8494.695    0.000 8494.695    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2223942  141.633    0.000 8269.236    0.004 agent.py:84(<listcomp>)
               44478840 1298.845    0.000 7751.902    0.000 exploration.py:40(epsintosoftmax)
                2223942   96.844    0.000 6700.031    0.003 agent.py:62(rememberMulti)
                2223942  239.058    0.000 6209.108    0.003 agent.py:66(<listcomp>)
                4446884   33.748    0.000 6178.931    0.001 grad_mode.py:23(decorate_context)
                4446884  226.319    0.000 6089.531    0.001 adam.py:55(step)
                2223942   66.510    0.000 5934.158    0.003 environments.py:85(<listcomp>)
               44606668 1501.315    0.000 5887.195    0.000 helpers.py:8(clean)
                4446884 1142.902    0.000 5016.425    0.001 functional.py:53(adam)
               51276994 4832.152    0.000 4832.152    0.000 {built-in method as_tensor}
                4446884   34.108    0.000 4741.831    0.001 tensor.py:181(backward)
                4446884   25.808    0.000 4707.722    0.001 __init__.py:68(backward)
                4446884 4565.251    0.001 4565.251    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               40024956   79.435    0.000 3534.982    0.000 conv.py:422(forward)
               40024956   91.032    0.000 3419.156    0.000 conv.py:414(_conv_forward)
               40024956 3311.901    0.000 3311.901    0.000 {built-in method conv2d}
                2223942   50.377    0.000 3002.792    0.001 environments.py:84(<listcomp>)
               53367608  121.808    0.000 3001.543    0.000 linear.py:92(forward)
               44478840  178.621    0.000 2952.416    0.000 interop.py:274(step)
               53367608  306.436    0.000 2818.864    0.000 functional.py:1669(linear)
               44478840 1684.687    0.000 2532.151    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6670832  386.120    0.000 2105.756    0.000 rnn.py:110(flatten_parameters)
                6670826   77.745    0.000 1741.666    0.000 rnn.py:555(forward)
               46695782 1627.145    0.000 1627.145    0.000 {built-in method addmm}
                6670826 1571.904    0.000 1571.904    0.000 {built-in method lstm}
               84497796   81.158    0.000 1529.145    0.000 activation.py:713(forward)
              373538364  889.954    0.000 1508.789    0.000 tensor.py:933(grad)
               44478840   22.354    0.000 1458.895    0.000 wrapper.py:25(act)
               84497796  127.868    0.000 1447.988    0.000 functional.py:1292(leaky_relu)
               44478840   59.418    0.000 1436.541    0.000 env.py:197(act)
               44478840 1341.304    0.000 1345.988    0.000 libenv.py:352(act)
               84497796 1308.469    0.000 1308.469    0.000 {built-in method torch._C._nn.leaky_relu}
                4446884  125.208    0.000 1301.074    0.000 optimizer.py:167(zero_grad)
                6670829 1266.066    0.000 1266.066    0.000 {built-in method _cudnn_rnn_flatten_weight}
              106725216 1019.581    0.000 1019.581    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   4447    1.815    0.000  893.714    0.201 agent.py:139(update_target_network)
              106725216  856.196    0.000  856.196    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              480268796  282.338    0.000  824.112    0.000 overrides.py:1073(has_torch_function)
               89085508   70.939    0.000  802.062    0.000 extract_dict_ob.py:9(observe)
               89085508   42.641    0.000  731.123    0.000 wrapper.py:19(observe)
               89085508  186.176    0.000  688.482    0.000 libenv.py:344(observe)
               33229133   70.522    0.000  661.179    0.000 functional.py:1479(softmax)
               57952129   66.544    0.000  647.150    0.000 <__array_function__ internals>:2(prod)
               33229133  584.553    0.000  584.553    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2223942    6.468    0.000  581.733    0.000 agent.py:230(avoid_similar_state)
               57952169   50.163    0.000  567.847    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               53362608  563.048    0.000  563.048    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   4447  149.651    0.034  545.127    0.123 memory.py:45(update_distribution)
               53362608  526.709    0.000  526.709    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              542530196  209.490    0.000  522.165    0.000 {built-in method builtins.any}
               57952129   77.354    0.000  517.684    0.000 fromnumeric.py:2881(prod)
              133564348  152.264    0.000  503.847    0.000 libenv.py:281(_maybe_copy_dict)
               53362608  472.067    0.000  472.067    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46711176  470.167    0.000  470.167    0.000 {built-in method numpy.array}
               57952129  147.046    0.000  440.330    0.000 fromnumeric.py:70(_wrapreduction)
              400697491  434.317    0.000  434.317    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6671826   14.497    0.000  432.121    0.000 functional.py:74(split)
               53367608  419.564    0.000  419.564    0.000 {method 't' of 'torch._C._TensorBase' objects}
               53362608  416.947    0.000  416.947    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6671826   32.496    0.000  416.673    0.000 tensor.py:460(split)
              331042966  382.753    0.000  382.753    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                6671826  382.602    0.000  382.602    0.000 {function Tensor.split at 0x7fa19adabd30}
               44478840  375.701    0.000  375.701    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               44478840   40.170    0.000  366.758    0.000 wrapper.py:22(get_info)
               31132023  330.309    0.000  354.809    0.000 module.py:781(__setattr__)
               44478840  350.807    0.000  350.807    0.000 memory.py:17(inner)
               44478840  165.006    0.000  326.589    0.000 libenv.py:363(get_info)
             1013905200  247.105    0.000  308.954    0.000 overrides.py:1086(<genexpr>)
                4446884   11.027    0.000  300.541    0.000 loss.py:445(forward)
               53362608  296.262    0.000  296.262    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   8894  239.942    0.027  292.480    0.033 {built-in method _pickle.loads}
                4446884   35.355    0.000  289.514    0.000 functional.py:2637(mse_loss)
                2223442  221.290    0.000  282.092    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                2223942  227.578    0.000  258.960    0.000 agent.py:131(convert_values)
               60180018  251.651    0.000  251.651    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                6670826   20.384    0.000  240.688    0.000 pooling.py:152(forward)
                6670826   12.775    0.000  220.304    0.000 _jit_internal.py:257(fn)
               40023956  217.506    0.000  217.506    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2561912  217.481    0.000  217.481    0.000 {built-in method tensor}
                6671826  209.839    0.000  209.839    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6670826   13.653    0.000  206.344    0.000 functional.py:574(_max_pool2d)
                2223442  192.553    0.000  192.553    0.000 memory.py:43(<listcomp>)
                6670826  191.836    0.000  191.836    0.000 {built-in method max_pool2d}
              236061239  184.228    0.000  184.441    0.000 module.py:765(__getattr__)
                2223942   26.796    0.000  182.444    0.000 environments.py:86(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 8482840: <EpsSoftmax_state_transition0.25maze_0> in cluster <dcc> Done

Job <EpsSoftmax_state_transition0.25maze_0> was submitted from host <n-62-27-19> by user <s183914> in cluster <dcc> at Sat Dec  5 00:10:43 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec  5 01:48:41 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec  5 01:48:41 2020
Terminated at Sun Dec  6 00:44:22 2020
Results reported at Sun Dec  6 00:44:22 2020

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

    CPU time :                                   85441.00 sec.
    Max Memory :                                 55020 MB
    Average Memory :                             54365.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6420.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82541 sec.
    Turnaround time :                            88419 sec.

The output (if any) is above this job summary.

