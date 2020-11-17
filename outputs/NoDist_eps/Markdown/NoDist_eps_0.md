[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NoDist_eps-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    200000
    Update every :              100
    Use distribution :          0
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      11744021848 function calls (11563341476 primitive calls) in 86109.08 seconds

##    Ordered by: cumulative time
   List reduced from 1314 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86109.076 86109.076 {built-in method builtins.exec}
                      1    0.028    0.028 86109.076 86109.076 <string>:1(<module>)
                      1  389.553  389.553 86109.047 86109.047 main.py:11(main)
                2657049   87.295    0.000 60683.615    0.023 agent.py:46(learn)
                2656949  348.803    0.000 59178.383    0.022 agent.py:54(TD_learn)
                2656949 8058.836    0.003 37025.595    0.014 memory.py:23(sample)
                2656949  309.931    0.000 28131.217    0.011 helpers.py:12(stack)
        193959077/13284845  826.649    0.000 14663.017    0.001 module.py:710(_call_impl)
               10627896  222.325    0.000 14371.340    0.001 agent.py:117(forward)
               23912889 14189.077    0.001 14189.080    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               23912841 13330.681    0.001 13330.681    0.001 {built-in method cat}
                2657049   73.442    0.000 10561.811    0.004 environments.py:73(step)
               31883688  233.610    0.000 8074.429    0.000 container.py:115(forward)
                2657049    8.495    0.000 7780.577    0.003 agent.py:32(rememberMulti)
                2657049  351.324    0.000 7772.082    0.003 agent.py:33(<listcomp>)
              366266101 7620.671    0.000 7620.671    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2657049   43.072    0.000 6481.050    0.002 agent.py:41(chooseMulti)
                2657049   66.679    0.000 6441.445    0.002 environments.py:75(<listcomp>)
               53295188 1647.842    0.000 6395.367    0.000 helpers.py:8(clean)
               61266035 5359.463    0.000 5359.463    0.000 {built-in method as_tensor}
                2656949   17.596    0.000 5265.349    0.002 grad_mode.py:12(decorate_context)
                2656949 1241.034    0.000 5227.936    0.002 adam.py:51(step)
               53139480   92.345    0.000 4691.358    0.000 conv.py:418(forward)
               53139480   94.809    0.000 4562.850    0.000 conv.py:410(_conv_forward)
               53139480 4447.967    0.000 4447.967    0.000 {built-in method conv2d}
                2656949   14.971    0.000 4309.354    0.002 tensor.py:155(backward)
                2656949   17.154    0.000 4294.383    0.002 __init__.py:57(backward)
                2656949 4202.000    0.002 4202.000    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2657049   57.290    0.000 3821.666    0.001 environments.py:74(<listcomp>)
               53140980  210.646    0.000 3764.376    0.000 interop.py:274(step)
               10627902  459.618    0.000 3148.327    0.000 rnn.py:109(flatten_parameters)
               10627896  105.961    0.000 2376.892    0.000 rnn.py:550(forward)
               10627899 2155.897    0.000 2155.897    0.000 {built-in method _cudnn_rnn_flatten_weight}
               10627896 2137.211    0.000 2137.211    0.000 {built-in method lstm}
                2657049  123.592    0.000 2090.524    0.001 agent.py:44(<listcomp>)
               53140980   27.108    0.000 2019.498    0.000 wrapper.py:25(act)
               53140980   82.195    0.000 1992.390    0.000 env.py:197(act)
               53140980 1856.025    0.000 1861.487    0.000 libenv.py:352(act)
               53140980  194.030    0.000 1639.339    0.000 exploration.py:31(epsilonGreedy)
                  26570    4.685    0.000 1417.936    0.053 agent.py:81(update_target_network)
               63767376   58.714    0.000 1288.870    0.000 activation.py:653(forward)
               63767376   90.089    0.000 1230.156    0.000 functional.py:1277(leaky_relu)
                  26570  347.456    0.013 1174.426    0.044 memory.py:37(update_distribution)
               63767376 1131.809    0.000 1131.809    0.000 {built-in method torch._C._nn.leaky_relu}
               85022368 1034.682    0.000 1034.682    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              106436168   92.333    0.000  926.105    0.000 extract_dict_ob.py:9(observe)
               85022368  922.659    0.000  922.659    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               53194120  922.478    0.000  922.478    0.000 {built-in method numpy.array}
              106436168   45.467    0.000  833.772    0.000 wrapper.py:19(observe)
                2656949  341.265    0.000  823.952    0.000 random.py:315(sample)
              106436168  213.391    0.000  788.305    0.000 libenv.py:344(observe)
               10627896   28.746    0.000  722.072    0.000 linear.py:90(forward)
               10627896   53.671    0.000  682.452    0.000 functional.py:1655(linear)
               42511184  570.485    0.000  570.485    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              379242470  567.546    0.000  567.546    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              159577148  171.914    0.000  553.322    0.000 libenv.py:281(_maybe_copy_dict)
                2656949   81.421    0.000  520.739    0.000 optimizer.py:166(zero_grad)
              478758014  492.617    0.000  492.617    0.000 {method 'copy' of 'numpy.ndarray' objects}
               42511184  483.008    0.000  483.008    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               10627896  468.027    0.000  468.027    0.000 {built-in method addmm}
               42511184  424.828    0.000  424.828    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               53140980   44.903    0.000  420.597    0.000 wrapper.py:22(get_info)
               42512459  386.130    0.000  414.299    0.000 module.py:774(__setattr__)
               42511184  413.428    0.000  413.428    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              680618613  254.426    0.000  386.511    0.000 random.py:250(_randbelow_with_getrandbits)
               53140980  199.762    0.000  375.694    0.000 libenv.py:363(get_info)
               10627896   25.631    0.000  354.430    0.000 pooling.py:156(forward)
               10627896   17.573    0.000  328.799    0.000 _jit_internal.py:237(fn)
               53140980  327.592    0.000  327.592    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               53140980  327.223    0.000  327.223    0.000 memory.py:15(inner)
               42511184  323.710    0.000  323.710    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10627896   18.455    0.000  309.476    0.000 functional.py:564(_max_pool2d)
                5720759  125.658    0.000  299.673    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               10627896  289.666    0.000  289.666    0.000 {built-in method max_pool2d}
                7971147   12.329    0.000  265.334    0.000 functional.py:68(split)
                7971147   14.040    0.000  252.010    0.000 tensor.py:367(split)
                7971147  236.344    0.000  236.344    0.000 {function Tensor.split at 0x7fbeb3b699d0}
               42511596  198.171    0.000  225.846    0.000 __init__.py:66(is_acceptable)
                2657049   35.417    0.000  225.258    0.000 environments.py:76(<listcomp>)
                2657049   18.132    0.000  198.497    0.000 collector.py:7(collect)
               53141000   40.437    0.000  189.868    0.000 environments.py:79(reset)
                2656949    6.020    0.000  189.159    0.000 loss.py:444(forward)
               26569690  185.359    0.000  185.359    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2656949   24.056    0.000  183.139    0.000 functional.py:2621(mse_loss)
              212872336   58.723    0.000  179.442    0.000 libenv.py:271(_maybe_copy_ndarray)
                5314099  178.951    0.000  178.951    0.000 {built-in method builtins.sum}
               11441658   14.096    0.000  174.017    0.000 <__array_function__ internals>:2(prod)
              212555968  143.747    0.000  166.366    0.000 tensor.py:725(grad)
               11441698   11.241    0.000  157.714    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              193959077  150.210    0.000  150.210    0.000 {built-in method torch._C._get_tracing_state}
               11441658   18.960    0.000  146.474    0.000 fromnumeric.py:2881(prod)
                5313898  142.833    0.000  142.833    0.000 {built-in method gather}
                  53140   14.343    0.000  138.367    0.003 {built-in method _pickle.loads}
              181631071  133.410    0.000  133.963    0.000 module.py:758(__getattr__)
               11441658   33.875    0.000  127.513    0.000 fromnumeric.py:70(_wrapreduction)
                2656949  110.113    0.000  110.113    0.000 {built-in method torch._C._nn.mse_loss}
                  53140   23.800    0.000  100.458    0.002 {built-in method _pickle.dumps}
               10627896   99.369    0.000   99.369    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 956518    1.181    0.000   93.076    0.000 storage.py:141(_load_from_bytes)
                 956518    4.918    0.000   91.895    0.000 serialization.py:486(load)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8366147: <NoDist_eps_0> in cluster <dcc> Done

Job <NoDist_eps_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Mon Nov 16 20:57:20 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov 16 20:57:22 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 16 20:57:22 2020
Terminated at Tue Nov 17 20:52:35 2020
Results reported at Tue Nov 17 20:52:35 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=30G]"
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

    CPU time :                                   87496.00 sec.
    Max Memory :                                 25295 MB
    Average Memory :                             25016.99 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5425.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86114 sec.
    Turnaround time :                            86115 sec.

The output (if any) is above this job summary.

