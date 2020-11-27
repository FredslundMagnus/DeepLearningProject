Fontconfig warning: ignoring iso_8859_1: not a valid region tag

    Name :                      NoNormalizationNoUncertainty-0
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
    Reward normalization :      0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      12429553100 function calls (12228029202 primitive calls) in 86115.17 seconds

##    Ordered by: cumulative time
   List reduced from 1340 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 86115.170 86115.170 {built-in method builtins.exec}
                      1    0.048    0.048 86115.170 86115.170 <string>:1(<module>)
                      1  329.949  329.949 86115.121 86115.121 main.py:11(main)
                2099517   84.654    0.000 59965.088    0.029 agent.py:50(learn)
                2099017  326.085    0.000 59307.354    0.028 agent.py:60(TD_learn)
                2099017 17224.670    0.008 40770.348    0.019 memory.py:31(sample)
                2099017  313.240    0.000 22896.589    0.011 helpers.py:12(stack)
        212013217/10495585  865.516    0.000 12828.249    0.001 module.py:715(_call_impl)
                8396568  183.598    0.000 12606.438    0.002 agent.py:138(forward)
              282807911 12470.469    0.000 12470.469    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2099517   34.343    0.000 12327.475    0.006 agent.py:44(chooseMulti)
               18892719 11282.615    0.001 11282.626    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               18892653 10912.307    0.001 10912.307    0.001 {built-in method cat}
                2099517   79.803    0.000 8624.602    0.004 agent.py:48(<listcomp>)
               41990340  120.613    0.000 8347.683    0.000 exploration.py:33(epsilonGreedy)
                2099517   58.551    0.000 7986.164    0.004 environments.py:73(step)
               33586272  227.045    0.000 7831.798    0.000 container.py:115(forward)
                2099517    6.112    0.000 5342.388    0.003 agent.py:35(rememberMulti)
                2099517  186.207    0.000 5336.275    0.003 agent.py:36(<listcomp>)
                2099517   48.448    0.000 5003.487    0.002 environments.py:75(<listcomp>)
               42194968 1295.308    0.000 4983.091    0.000 helpers.py:8(clean)
               48492019 4188.607    0.000 4188.607    0.000 {built-in method as_tensor}
                2099017   17.765    0.000 3909.801    0.002 grad_mode.py:23(decorate_context)
               50379408   87.538    0.000 3908.945    0.000 conv.py:422(forward)
                2099017  140.814    0.000 3868.095    0.002 adam.py:55(step)
               50379408   95.649    0.000 3784.141    0.000 conv.py:414(_conv_forward)
               50379408 3668.629    0.000 3668.629    0.000 {built-in method conv2d}
                2099017   18.595    0.000 3239.636    0.002 tensor.py:181(backward)
                2099017   12.176    0.000 3221.041    0.002 __init__.py:68(backward)
                2099017  713.517    0.000 3179.141    0.002 functional.py:53(adam)
                2099017 3150.706    0.002 3150.706    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2099517   44.741    0.000 2758.443    0.001 environments.py:74(<listcomp>)
               41990340  153.342    0.000 2713.702    0.000 interop.py:274(step)
                8396574  424.201    0.000 2300.863    0.000 rnn.py:110(flatten_parameters)
                8396568   87.668    0.000 1816.161    0.000 rnn.py:555(forward)
                8396568 1622.536    0.000 1622.536    0.000 {built-in method lstm}
               41990340   20.287    0.000 1458.137    0.000 wrapper.py:25(act)
               41990340   55.158    0.000 1437.850    0.000 env.py:197(act)
                8396571 1387.651    0.000 1387.651    0.000 {built-in method _cudnn_rnn_flatten_weight}
               41990340 1351.250    0.000 1355.441    0.000 libenv.py:352(act)
               25189704   59.990    0.000 1312.039    0.000 linear.py:92(forward)
               75569112   71.895    0.000 1297.852    0.000 activation.py:713(forward)
               75569112  106.254    0.000 1225.956    0.000 functional.py:1292(leaky_relu)
               25189704  102.333    0.000 1225.877    0.000 functional.py:1669(linear)
               75569112 1108.821    0.000 1108.821    0.000 {built-in method torch._C._nn.leaky_relu}
              264476208  573.742    0.000  975.265    0.000 tensor.py:933(grad)
                2099017   85.875    0.000  853.482    0.000 optimizer.py:167(zero_grad)
               25189704  816.920    0.000  816.920    0.000 {built-in method addmm}
               84185308   65.176    0.000  673.718    0.000 extract_dict_ob.py:9(observe)
               75564612  640.994    0.000  640.994    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2099017  288.228    0.000  639.637    0.000 random.py:315(sample)
               84185308   37.411    0.000  608.542    0.000 wrapper.py:19(observe)
                   4199    0.977    0.000  573.081    0.136 agent.py:92(update_target_network)
               84185308  153.390    0.000  571.131    0.000 libenv.py:344(observe)
               75564612  541.346    0.000  541.346    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   4199  142.145    0.034  513.098    0.122 memory.py:45(update_distribution)
              327448392  173.995    0.000  504.623    0.000 overrides.py:1073(has_torch_function)
               41998738  437.778    0.000  437.778    0.000 {built-in method numpy.array}
              126175648  129.458    0.000  412.567    0.000 libenv.py:281(_maybe_copy_dict)
               33587441  344.217    0.000  368.501    0.000 module.py:781(__setattr__)
               37782306  357.445    0.000  357.445    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11124469  136.215    0.000  353.796    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              378531143  351.047    0.000  351.047    0.000 {method 'copy' of 'numpy.ndarray' objects}
               37782306  328.422    0.000  328.422    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              356836154  127.695    0.000  315.080    0.000 {built-in method builtins.any}
               37782306  312.352    0.000  312.352    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               41990340   32.438    0.000  305.151    0.000 wrapper.py:22(get_info)
                6298551   10.998    0.000  297.512    0.000 functional.py:74(split)
                6298551   26.736    0.000  285.614    0.000 tensor.py:460(split)
              537490394  180.310    0.000  275.756    0.000 random.py:250(_randbelow_with_getrandbits)
               41990340  141.168    0.000  272.713    0.000 libenv.py:363(get_info)
               37782306  271.891    0.000  271.891    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              292893780  269.831    0.000  269.831    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                6298551  257.644    0.000  257.644    0.000 {function Tensor.split at 0x7f53ff600d30}
                8396568   16.616    0.000  255.299    0.000 pooling.py:152(forward)
               41990340  252.921    0.000  252.921    0.000 memory.py:17(inner)
                8396568   14.346    0.000  238.683    0.000 _jit_internal.py:257(fn)
                8396568   14.414    0.000  222.906    0.000 functional.py:574(_max_pool2d)
               22249078   18.416    0.000  217.583    0.000 <__array_function__ internals>:2(prod)
                8396568  207.215    0.000  207.215    0.000 {built-in method max_pool2d}
               41990340  197.116    0.000  197.116    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37782306  196.100    0.000  196.100    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               22249118   15.137    0.000  195.620    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               33586284  168.226    0.000  190.989    0.000 __init__.py:67(is_acceptable)
              680086488  150.738    0.000  185.610    0.000 overrides.py:1086(<genexpr>)
               25189704  184.606    0.000  184.606    0.000 {method 't' of 'torch._C._TensorBase' objects}
               22249078   23.280    0.000  180.484    0.000 fromnumeric.py:2881(prod)
                2099517   23.849    0.000  165.683    0.000 environments.py:76(<listcomp>)
               22249078   44.568    0.000  157.203    0.000 fromnumeric.py:70(_wrapreduction)
              201727999  147.856    0.000  147.976    0.000 module.py:765(__getattr__)
                2099517   14.084    0.000  144.848    0.000 collector.py:7(collect)
               41990360   25.777    0.000  141.846    0.000 environments.py:79(reset)
                2099017    6.920    0.000  136.875    0.000 loss.py:445(forward)
                2099017   17.110    0.000  129.956    0.000 functional.py:2637(mse_loss)
                4199035  129.774    0.000  129.775    0.000 {built-in method builtins.sum}
               20991170  126.161    0.000  126.161    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              168370616   44.999    0.000  122.814    0.000 libenv.py:271(_maybe_copy_ndarray)
              212013217  120.268    0.000  120.268    0.000 {built-in method torch._C._get_tracing_state}
               37782480   46.461    0.000  103.300    0.000 tensor.py:596(__hash__)
                4198034  101.692    0.000  101.692    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8423607: <NoNormalizationNoUncertainty_0> in cluster <dcc> Done

Job <NoNormalizationNoUncertainty_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue Nov 24 20:27:38 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Nov 24 20:27:39 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 20:27:39 2020
Terminated at Wed Nov 25 20:22:59 2020
Results reported at Wed Nov 25 20:22:59 2020

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

    CPU time :                                   90740.00 sec.
    Max Memory :                                 56712 MB
    Average Memory :                             56012.49 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4728.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86131 sec.
    Turnaround time :                            86121 sec.

The output (if any) is above this job summary.

