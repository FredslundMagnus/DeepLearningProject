[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0_0.05returnbigfish-0
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
    State difference weight :   0.05
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11529302666 function calls (11263372142 primitive calls) in 82525.52 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82525.520 82525.520 {built-in method builtins.exec}
                      1    0.037    0.037 82525.520 82525.520 <string>:1(<module>)
                      1  487.433  487.433 82525.482 82525.482 main.py:92(main)
                2707289  256.294    0.000 51814.300    0.019 agent.py:84(learn)
                2598343  764.813    0.000 50936.031    0.020 agent.py:99(TD_learn)
                2598343  163.822    0.000 26405.101    0.010 memory.py:35(sample_distribution)
                2598343  260.598    0.000 25615.777    0.010 helpers.py:15(stack)
        284222256/18298346 1187.169    0.000 14683.556    0.001 module.py:710(_call_impl)
                2707289  194.206    0.000 14021.146    0.005 agent.py:70(chooseMulti)
                7903975  217.191    0.000 13539.395    0.002 agent.py:231(forward)
               26311375 13489.102    0.001 13489.156    0.001 {method 'to' of 'torch._C._TensorBase' objects}
              354519559 12111.358    0.000 12111.358    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               23711925 11700.416    0.000 11700.416    0.000 {built-in method cat}
               42119217  289.865    0.000 9574.004    0.000 container.py:115(forward)
                2707289   72.386    0.000 9255.044    0.003 environments.py:83(step)
                2599342   95.350    0.000 7544.752    0.003 agent.py:82(<listcomp>)
               51986840  134.709    0.000 7220.513    0.000 exploration.py:34(epsilonGreedy)
                7795029   39.259    0.000 6932.204    0.001 grad_mode.py:12(decorate_context)
                7795029 1725.580    0.000 6840.806    0.001 adam.py:51(step)
                2599342   95.097    0.000 6731.132    0.003 agent.py:58(rememberMulti)
                2599342  232.693    0.000 6245.756    0.002 agent.py:62(<listcomp>)
                2707289   66.920    0.000 6059.191    0.002 environments.py:85(<listcomp>)
               54301766 1619.807    0.000 6012.350    0.000 helpers.py:8(clean)
                7795029   40.328    0.000 5676.627    0.001 tensor.py:155(backward)
                7795029   36.104    0.000 5636.300    0.001 __init__.py:57(backward)
                7795029 5441.317    0.001 5441.317    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               62096795 4910.449    0.000 4910.449    0.000 {built-in method as_tensor}
               47423850   80.321    0.000 3513.705    0.000 conv.py:418(forward)
               47423850   88.020    0.000 3398.731    0.000 conv.py:410(_conv_forward)
               47423850 3292.427    0.000 3292.427    0.000 {built-in method conv2d}
                2707289   54.479    0.000 2931.301    0.001 environments.py:84(<listcomp>)
               63125851  125.339    0.000 2905.073    0.000 linear.py:90(forward)
               54145780  200.231    0.000 2876.822    0.000 interop.py:274(step)
               63125851  317.010    0.000 2718.084    0.000 functional.py:1655(linear)
                7903981  340.325    0.000 1929.810    0.000 rnn.py:109(flatten_parameters)
                7903975   79.514    0.000 1779.112    0.000 rnn.py:550(forward)
                7903975 1604.544    0.000 1604.544    0.000 {built-in method lstm}
               55327825 1594.651    0.000 1594.651    0.000 {built-in method addmm}
              100046384   84.641    0.000 1497.287    0.000 activation.py:653(forward)
              100046384  126.312    0.000 1412.646    0.000 functional.py:1277(leaky_relu)
              100046384 1273.651    0.000 1273.651    0.000 {built-in method torch._C._nn.leaky_relu}
              155900580 1272.070    0.000 1272.070    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               54145780   26.511    0.000 1259.947    0.000 wrapper.py:25(act)
               54145780   69.484    0.000 1233.435    0.000 env.py:197(act)
                7903978 1185.814    0.000 1185.814    0.000 {built-in method _cudnn_rnn_flatten_weight}
               54145780 1123.348    0.000 1128.408    0.000 libenv.py:352(act)
              155900580 1112.266    0.000 1112.266    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              108447546   84.130    0.000  859.461    0.000 extract_dict_ob.py:9(observe)
               77950290  838.000    0.000  838.000    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              108447546   46.549    0.000  775.331    0.000 wrapper.py:19(observe)
              108447546  198.022    0.000  728.782    0.000 libenv.py:344(observe)
                7795029  114.574    0.000  655.906    0.000 optimizer.py:166(zero_grad)
               77950290  636.426    0.000  636.426    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   2707    1.000    0.000  621.976    0.230 agent.py:157(update_target_network)
                2599342    6.603    0.000  571.417    0.000 agent.py:249(avoid_similar_state)
              162593326  163.256    0.000  530.376    0.000 libenv.py:281(_maybe_copy_dict)
               77950290  525.353    0.000  525.353    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               77950290  505.343    0.000  505.343    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              487782685  450.584    0.000  450.584    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7795029   13.526    0.000  430.886    0.000 loss.py:444(forward)
                7795029   54.328    0.000  417.360    0.000 functional.py:2621(mse_loss)
              403024177  415.589    0.000  415.589    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               54145780   42.858    0.000  395.712    0.000 wrapper.py:22(get_info)
               77950290  370.806    0.000  370.806    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               63125851  366.963    0.000  366.963    0.000 {method 't' of 'torch._C._TensorBase' objects}
               11625399  134.897    0.000  354.625    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               54145780  183.543    0.000  352.853    0.000 libenv.py:363(get_info)
               51986840  350.540    0.000  350.540    0.000 memory.py:17(inner)
               36814421  315.891    0.000  341.827    0.000 module.py:774(__setattr__)
                   2707   93.611    0.035  334.679    0.124 memory.py:45(update_distribution)
                2598343  259.943    0.000  334.478    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               56749537  329.475    0.000  329.475    0.000 {built-in method numpy.array}
               15590058  300.233    0.000  300.233    0.000 {built-in method gather}
                2599342  219.951    0.000  288.029    0.000 agent.py:149(convert_values)
              389751558  232.840    0.000  269.677    0.000 tensor.py:725(grad)
               60197673  265.177    0.000  265.177    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               25849281   22.947    0.000  260.572    0.000 <__array_function__ internals>:2(prod)
                   5414  232.022    0.043  259.944    0.048 {built-in method _pickle.loads}
                8121867   14.822    0.000  237.613    0.000 functional.py:68(split)
               54145780  237.173    0.000  237.173    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25849321   19.072    0.000  233.474    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7795029  231.931    0.000  231.931    0.000 {built-in method torch._C._nn.mse_loss}
                2805072  231.079    0.000  231.079    0.000 {built-in method tensor}
                8121867   14.044    0.000  221.669    0.000 tensor.py:367(split)
                7903975   15.052    0.000  220.331    0.000 pooling.py:156(forward)
               25849281   29.593    0.000  214.402    0.000 fromnumeric.py:2881(prod)
                8121867  205.936    0.000  205.936    0.000 {function Tensor.split at 0x7fc351cee9d0}
                7903975   12.505    0.000  205.279    0.000 _jit_internal.py:237(fn)
                2598343  196.569    0.000  196.569    0.000 memory.py:43(<listcomp>)
                7798026  196.087    0.000  196.087    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2707289   28.706    0.000  192.166    0.000 environments.py:86(<listcomp>)
                7903975   14.016    0.000  191.612    0.000 functional.py:564(_max_pool2d)
               31615912  166.881    0.000  186.120    0.000 __init__.py:66(is_acceptable)
              279243757  185.820    0.000  185.935    0.000 module.py:758(__getattr__)
                2707289   19.414    0.000  185.605    0.000 collector.py:8(collect)
               25849281   57.594    0.000  184.809    0.000 fromnumeric.py:70(_wrapreduction)
                7903975  176.640    0.000  176.640    0.000 {built-in method max_pool2d}
               15591057  172.766    0.000  172.766    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                5414579  164.873    0.000  164.874    0.000 {built-in method builtins.sum}
              284222256  164.076    0.000  164.076    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 8557627: <BIGFISH_U_S_0_0.05returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0_0.05returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:47 2020
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Dec 15 05:06:24 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec 15 05:06:24 2020
Terminated at Wed Dec 16 04:01:58 2020
Results reported at Wed Dec 16 04:01:58 2020

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

    CPU time :                                   87220.00 sec.
    Max Memory :                                 54157 MB
    Average Memory :                             53433.05 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7283.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82534 sec.
    Turnaround time :                            388811 sec.

The output (if any) is above this job summary.

