
    Name :                      YesNormalizationNoUncertainty-0
    Discount :                  0.995
    Environment :               fruitbot
    Hours :                     24
    Memory :                    500000
    Update every :              500
    Use distribution :          0
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      1
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      11864278204 function calls (11672036642 primitive calls) in 85918.85 seconds

##    Ordered by: cumulative time
   List reduced from 1351 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 86114.320 86114.320 {built-in method builtins.exec}
                      1    0.060    0.060 86114.320 86114.320 <string>:1(<module>)
                      1  329.088  329.088 86114.259 86114.259 main.py:11(main)
                2002826   87.117    0.000 63433.201    0.032 agent.py:50(learn)
                2002326  395.150    0.000 61907.256    0.031 agent.py:60(TD_learn)
                2002326 16559.654    0.008 39561.315    0.020 memory.py:31(sample)
                2002326  340.417    0.000 22364.987    0.011 helpers.py:12(stack)
        202247426/10012130  866.650    0.000 14734.326    0.001 module.py:715(_call_impl)
                8009804  199.865    0.000 14497.206    0.002 agent.py:138(forward)
               18022500 10921.114    0.001 10921.157    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               18022434 10688.073    0.001 10688.073    0.001 {built-in method cat}
               32039216  251.869    0.000 9032.049    0.000 container.py:115(forward)
                2002826   59.313    0.000 8572.312    0.004 environments.py:73(step)
              269363186 7502.944    0.000 7502.944    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2002826   36.536    0.000 7335.781    0.004 agent.py:44(chooseMulti)
                2002826    6.539    0.000 6275.291    0.003 agent.py:35(rememberMulti)
                2002826  275.555    0.000 6268.751    0.003 agent.py:36(<listcomp>)
                2002826   47.313    0.000 5381.044    0.003 environments.py:75(<listcomp>)
               40279517 1308.943    0.000 5367.973    0.000 helpers.py:8(clean)
                2002326   16.925    0.000 5266.654    0.003 grad_mode.py:23(decorate_context)
                2002326  145.530    0.000 5225.881    0.003 adam.py:55(step)
               46286495 4595.145    0.000 4595.145    0.000 {built-in method as_tensor}
               48058824   89.065    0.000 4512.139    0.000 conv.py:422(forward)
                2002326  969.596    0.000 4501.488    0.002 functional.py:53(adam)
               48058824   89.345    0.000 4386.718    0.000 conv.py:414(_conv_forward)
               48058824 4280.924    0.000 4280.924    0.000 {built-in method conv2d}
                2002326   20.764    0.000 3938.408    0.002 tensor.py:181(backward)
                2002326   12.524    0.000 3917.644    0.002 __init__.py:68(backward)
                2002326 3840.590    0.002 3840.590    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2002826   97.628    0.000 3123.339    0.002 agent.py:48(<listcomp>)
                2002826   46.504    0.000 2930.671    0.001 environments.py:74(<listcomp>)
               40056520  167.510    0.000 2884.167    0.000 interop.py:274(step)
                8009810  460.639    0.000 2864.612    0.000 rnn.py:110(flatten_parameters)
               40056520  143.157    0.000 2754.559    0.000 exploration.py:33(epsilonGreedy)
                8009804   85.298    0.000 1909.817    0.000 rnn.py:555(forward)
                8009807 1899.064    0.000 1899.064    0.000 {built-in method _cudnn_rnn_flatten_weight}
                8009804 1716.953    0.000 1716.953    0.000 {built-in method lstm}
               72088236   69.781    0.000 1577.366    0.000 activation.py:713(forward)
               40056520   22.203    0.000 1534.217    0.000 wrapper.py:25(act)
               24029412   54.212    0.000 1531.172    0.000 linear.py:92(forward)
               40056520   65.633    0.000 1512.014    0.000 env.py:197(act)
               72088236  106.218    0.000 1507.585    0.000 functional.py:1292(leaky_relu)
               24029412  103.187    0.000 1452.051    0.000 functional.py:1669(linear)
               40056520 1403.579    0.000 1407.654    0.000 libenv.py:352(act)
               72088236 1392.260    0.000 1392.260    0.000 {built-in method torch._C._nn.leaky_relu}
              252293142  690.048    0.000 1090.117    0.000 tensor.py:933(grad)
                2002326  103.923    0.000 1059.692    0.001 optimizer.py:167(zero_grad)
               24029412  990.195    0.000  990.195    0.000 {built-in method addmm}
               72083736  946.093    0.000  946.093    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   4005    0.126    0.000  886.452    0.221 memory.py:25(average_reward)
               72083736  795.902    0.000  795.902    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               80336037   71.925    0.000  716.296    0.000 extract_dict_ob.py:9(observe)
               40072442  649.009    0.000  649.009    0.000 {built-in method numpy.array}
               80336037   35.876    0.000  644.370    0.000 wrapper.py:19(observe)
              340402689  267.309    0.000  642.852    0.000 {built-in method builtins.any}
                2002326  280.226    0.000  624.824    0.000 random.py:315(sample)
               80336037  163.019    0.000  608.494    0.000 libenv.py:344(observe)
                   4005    0.963    0.000  552.376    0.138 agent.py:92(update_target_network)
              312364596  180.862    0.000  502.573    0.000 overrides.py:1073(has_torch_function)
               36041868  502.100    0.000  502.100    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   4005  136.496    0.034  490.154    0.122 memory.py:45(update_distribution)
                4009609  460.643    0.000  460.644    0.000 {built-in method builtins.sum}
               36041868  460.437    0.000  460.437    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               22069044   16.186    0.000  441.242    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              120392557  132.384    0.000  435.096    0.000 libenv.py:281(_maybe_copy_dict)
               36041868  428.304    0.000  428.304    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              278928862  414.062    0.000  414.062    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11032454  153.861    0.000  393.783    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               36041868  385.854    0.000  385.854    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              361181676  383.744    0.000  383.744    0.000 {method 'copy' of 'numpy.ndarray' objects}
               32040385  343.504    0.000  366.402    0.000 module.py:781(__setattr__)
               40056520   36.676    0.000  331.923    0.000 wrapper.py:22(get_info)
                6008478   10.458    0.000  300.798    0.000 functional.py:74(split)
                8009804   17.007    0.000  295.501    0.000 pooling.py:152(forward)
               40056520  156.494    0.000  295.247    0.000 libenv.py:363(get_info)
               36041868  292.431    0.000  292.431    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6008478   26.699    0.000  289.567    0.000 tensor.py:460(split)
                8009804   13.482    0.000  278.494    0.000 _jit_internal.py:257(fn)
              512731011  176.892    0.000  271.419    0.000 random.py:250(_randbelow_with_getrandbits)
               40056520  271.152    0.000  271.152    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8009804   15.153    0.000  263.651    0.000 functional.py:574(_max_pool2d)
                6008478  261.477    0.000  261.477    0.000 {function Tensor.split at 0x7f0c73e6bca0}
               40056520  260.661    0.000  260.661    0.000 memory.py:17(inner)
                8009804  247.536    0.000  247.536    0.000 {built-in method max_pool2d}
               22065048   18.963    0.000  239.924    0.000 <__array_function__ internals>:2(prod)
               24029412  238.136    0.000  238.136    0.000 {method 't' of 'torch._C._TensorBase' objects}
                   3956    0.023    0.000  223.874    0.057 <__array_function__ internals>:2(std)
                   3956    0.080    0.000  223.829    0.057 fromnumeric.py:3381(std)
                   3956    0.048    0.000  223.748    0.057 _methods.py:232(_std)
                   3956    2.147    0.001  223.698    0.057 _methods.py:176(_var)
                   7912    0.020    0.000  220.134    0.028 _asarray.py:86(asanyarray)
                2002826   26.670    0.000  201.283    0.000 environments.py:76(<listcomp>)
               22065048   24.168    0.000  201.228    0.000 fromnumeric.py:2881(prod)
               32039228  173.299    0.000  195.665    0.000 __init__.py:67(is_acceptable)
              648758604  142.572    0.000  178.439    0.000 overrides.py:1086(<genexpr>)
               22065048   46.626    0.000  177.060    0.000 fromnumeric.py:70(_wrapreduction)
               40056540   31.146    0.000  174.621    0.000 environments.py:79(reset)
               20024260  159.897    0.000  159.897    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2002326    5.026    0.000  152.081    0.000 loss.py:445(forward)
                2002826   13.690    0.000  150.101    0.000 collector.py:7(collect)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 8423608: <YesNormalizationNoUncertainty_0> in cluster <dcc> Done

Job <YesNormalizationNoUncertainty_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue Nov 24 20:27:38 2020
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Nov 24 20:59:10 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 20:59:10 2020
Terminated at Wed Nov 25 20:54:29 2020
Results reported at Wed Nov 25 20:54:29 2020

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

    CPU time :                                   87866.00 sec.
    Max Memory :                                 56695 MB
    Average Memory :                             56001.44 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4745.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86120 sec.
    Turnaround time :                            88011 sec.

The output (if any) is above this job summary.

