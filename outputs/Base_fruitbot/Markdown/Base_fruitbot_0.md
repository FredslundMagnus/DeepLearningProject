[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_fruitbot-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    200000
    Update every :              100
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      10709285597 function calls (10489565353 primitive calls) in 86111.43 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86111.429 86111.429 {built-in method builtins.exec}
                      1    0.017    0.017 86111.429 86111.429 <string>:1(<module>)
                      1  547.853  547.853 86111.412 86111.412 main.py:11(main)
                3231165  112.602    0.000 59217.652    0.018 agent.py:46(learn)
                3231065  408.008    0.000 57368.312    0.018 agent.py:54(TD_learn)
                3231065  212.973    0.000 34480.984    0.011 memory.py:27(sample_distribution)
                3231065  334.138    0.000 33420.636    0.010 helpers.py:12(stack)
               29079933 17496.822    0.001 17496.835    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        235869545/16155425 1027.214    0.000 16119.654    0.001 module.py:710(_call_impl)
               12924360  260.979    0.000 15763.130    0.001 agent.py:117(forward)
               29079885 15173.492    0.001 15173.492    0.001 {built-in method cat}
                3231165   91.594    0.000 11442.506    0.004 environments.py:73(step)
               38773080  245.035    0.000 8639.496    0.000 container.py:115(forward)
              449863180 8086.665    0.000 8086.665    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3231165    9.441    0.000 7880.181    0.002 agent.py:32(rememberMulti)
                3231165  273.559    0.000 7870.741    0.002 agent.py:33(<listcomp>)
                3231165   47.488    0.000 6783.589    0.002 agent.py:41(chooseMulti)
                3231165   57.268    0.000 6663.037    0.002 environments.py:75(<listcomp>)
               64815457 1813.047    0.000 6627.836    0.000 helpers.py:8(clean)
               74508652 5587.593    0.000 5587.593    0.000 {built-in method as_tensor}
               64621800  112.230    0.000 4994.454    0.000 conv.py:418(forward)
               64621800  127.992    0.000 4833.453    0.000 conv.py:410(_conv_forward)
               64621800 4683.201    0.000 4683.201    0.000 {built-in method conv2d}
                3231065   21.206    0.000 4509.947    0.001 grad_mode.py:12(decorate_context)
                3231065 1128.842    0.000 4466.199    0.001 adam.py:51(step)
                3231165   66.812    0.000 4461.066    0.001 environments.py:74(<listcomp>)
                3231065   17.420    0.000 4458.040    0.001 tensor.py:155(backward)
                3231065   23.834    0.000 4440.621    0.001 __init__.py:57(backward)
               64623300  243.381    0.000 4394.254    0.000 interop.py:274(step)
                3231065 4332.456    0.001 4332.456    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               12924366  574.663    0.000 3273.192    0.000 rnn.py:109(flatten_parameters)
               12924360  145.866    0.000 2944.380    0.000 rnn.py:550(forward)
               12924360 2633.302    0.000 2633.302    0.000 {built-in method lstm}
               64623300   31.639    0.000 2361.827    0.000 wrapper.py:25(act)
               64623300   80.435    0.000 2330.188    0.000 env.py:197(act)
               64623300 2196.221    0.000 2202.464    0.000 libenv.py:352(act)
                3231165  118.613    0.000 2083.843    0.001 agent.py:44(<listcomp>)
               12924363 2030.216    0.000 2030.216    0.000 {built-in method _cudnn_rnn_flatten_weight}
                  32311    6.188    0.000 1736.738    0.054 agent.py:81(update_target_network)
               64623300  176.031    0.000 1686.431    0.000 exploration.py:31(epsilonGreedy)
                  32311  442.112    0.014 1458.569    0.045 memory.py:37(update_distribution)
               77546160   78.266    0.000 1310.158    0.000 activation.py:653(forward)
               77546160  118.140    0.000 1231.892    0.000 functional.py:1277(leaky_relu)
               67918788 1120.236    0.000 1120.236    0.000 {built-in method numpy.array}
               77546160 1102.990    0.000 1102.990    0.000 {built-in method torch._C._nn.leaky_relu}
              129438757   95.012    0.000 1082.069    0.000 extract_dict_ob.py:9(observe)
              129438757   59.210    0.000  987.057    0.000 wrapper.py:19(observe)
              129438757  252.289    0.000  927.847    0.000 libenv.py:344(observe)
              103394080  826.073    0.000  826.073    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12924360   35.825    0.000  788.309    0.000 linear.py:90(forward)
               12924360   68.429    0.000  738.925    0.000 functional.py:1655(linear)
              103394080  733.907    0.000  733.907    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              194062057  206.093    0.000  665.781    0.000 libenv.py:281(_maybe_copy_dict)
              582218482  582.035    0.000  582.035    0.000 {method 'copy' of 'numpy.ndarray' objects}
               51698315  523.782    0.000  561.601    0.000 module.py:774(__setattr__)
               64623300   59.486    0.000  502.697    0.000 wrapper.py:22(get_info)
               51697040  502.171    0.000  502.171    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               12924360  489.443    0.000  489.443    0.000 {built-in method addmm}
                3231065  367.691    0.000  484.381    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
              465634231  476.517    0.000  476.517    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               64623300  229.886    0.000  443.211    0.000 libenv.py:363(get_info)
               51697040  419.953    0.000  419.953    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               64623300  414.312    0.000  414.312    0.000 memory.py:15(inner)
                3231065   70.289    0.000  411.694    0.000 optimizer.py:166(zero_grad)
               12924360   37.258    0.000  390.994    0.000 pooling.py:156(forward)
               51697040  357.933    0.000  357.933    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12924360   21.085    0.000  353.736    0.000 _jit_internal.py:237(fn)
               51697040  342.760    0.000  342.760    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               12924360   24.114    0.000  330.662    0.000 functional.py:564(_max_pool2d)
               12924360  304.771    0.000  304.771    0.000 {built-in method max_pool2d}
                9693495   15.042    0.000  303.688    0.000 functional.py:68(split)
                9693495   15.946    0.000  287.363    0.000 tensor.py:367(split)
               64623300  278.799    0.000  278.799    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9693495  269.743    0.000  269.743    0.000 {function Tensor.split at 0x7efca483c940}
               51697452  227.917    0.000  263.800    0.000 __init__.py:66(is_acceptable)
                3230866  242.551    0.000  242.551    0.000 memory.py:35(<listcomp>)
               51697040  234.114    0.000  234.114    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3231165   38.611    0.000  226.809    0.000 environments.py:76(<listcomp>)
                3231165   21.443    0.000  221.749    0.000 collector.py:7(collect)
                3231065    9.197    0.000  217.641    0.000 loss.py:444(forward)
                3231065   32.110    0.000  208.443    0.000 functional.py:2621(mse_loss)
              258877514   68.755    0.000  202.490    0.000 libenv.py:271(_maybe_copy_ndarray)
                6462331  198.881    0.000  198.881    0.000 {built-in method builtins.sum}
               64623320   40.732    0.000  188.202    0.000 environments.py:79(reset)
               32310850  177.970    0.000  177.970    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              258485248  152.022    0.000  176.410    0.000 tensor.py:725(grad)
              220877635  175.620    0.000  176.295    0.000 module.py:758(__getattr__)
                  64622   16.744    0.000  155.682    0.002 {built-in method _pickle.loads}
                6462130  154.037    0.000  154.037    0.000 {built-in method gather}
              235869545  143.099    0.000  143.099    0.000 {built-in method torch._C._get_tracing_state}
                  64622   28.547    0.000  116.299    0.002 {built-in method _pickle.dumps}
                3231065  115.813    0.000  115.813    0.000 {built-in method torch._C._nn.mse_loss}
                8231045   11.972    0.000  113.384    0.000 <__array_function__ internals>:2(prod)
               12924360   35.872    0.000  110.534    0.000 rnn.py:524(check_forward_args)
                1163194    1.324    0.000  107.452    0.000 storage.py:141(_load_from_bytes)
                1163194    5.671    0.000  106.128    0.000 serialization.py:486(load)
               12924360  104.269    0.000  104.269    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8231085    9.269    0.000   99.685    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               64815497   50.600    0.000   99.146    0.000 types.py:163(multimap)
               11494222   92.166    0.000   92.166    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8371231: <Base_fruitbot_0> in cluster <dcc> Done

Job <Base_fruitbot_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:31 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov 19 06:02:53 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov 19 06:02:53 2020
Terminated at Fri Nov 20 05:58:09 2020
Results reported at Fri Nov 20 05:58:09 2020

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

    CPU time :                                   88298.00 sec.
    Max Memory :                                 25376 MB
    Average Memory :                             25060.76 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5344.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86117 sec.
    Turnaround time :                            201698 sec.

The output (if any) is above this job summary.

