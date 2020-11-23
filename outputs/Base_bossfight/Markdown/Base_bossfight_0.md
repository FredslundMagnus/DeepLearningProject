[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_bossfight-0
    Discount :                  0.999
    Environment :               bossfight
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


      10515720604 function calls (10299972376 primitive calls) in 86116.82 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86116.824 86116.824 {built-in method builtins.exec}
                      1    0.023    0.023 86116.824 86116.824 <string>:1(<module>)
                      1  503.641  503.641 86116.800 86116.800 main.py:11(main)
                3172753  106.561    0.000 58120.793    0.018 agent.py:46(learn)
                3172653  361.545    0.000 56254.351    0.018 agent.py:54(TD_learn)
                3172653  207.106    0.000 34013.822    0.011 memory.py:27(sample_distribution)
                3172653  335.908    0.000 32987.749    0.010 helpers.py:12(stack)
               28554225 16615.953    0.001 16616.021    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               28554177 15706.372    0.001 15706.372    0.001 {built-in method cat}
        231605469/15863365 1002.931    0.000 15667.243    0.001 module.py:710(_call_impl)
               12690712  251.691    0.000 15336.878    0.001 agent.py:117(forward)
                3172753   89.894    0.000 12468.420    0.004 environments.py:73(step)
               38072136  246.979    0.000 8517.309    0.000 container.py:115(forward)
              441686991 8173.934    0.000 8173.934    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3172753    9.780    0.000 8029.017    0.003 agent.py:32(rememberMulti)
                3172753  271.523    0.000 8019.237    0.003 agent.py:33(<listcomp>)
                3172753   64.047    0.000 7197.724    0.002 environments.py:75(<listcomp>)
               63612666 2012.425    0.000 7153.724    0.000 helpers.py:8(clean)
                3172753   47.521    0.000 6739.691    0.002 agent.py:41(chooseMulti)
               73130625 5827.029    0.000 5827.029    0.000 {built-in method as_tensor}
                3172753   69.629    0.000 4943.161    0.002 environments.py:74(<listcomp>)
               63453560  116.190    0.000 4927.346    0.000 conv.py:418(forward)
               63455060  249.182    0.000 4873.533    0.000 interop.py:274(step)
               63453560  123.826    0.000 4766.161    0.000 conv.py:410(_conv_forward)
               63453560 4619.130    0.000 4619.130    0.000 {built-in method conv2d}
                3172653   19.718    0.000 4520.983    0.001 grad_mode.py:12(decorate_context)
                3172653 1137.761    0.000 4478.472    0.001 adam.py:51(step)
                3172653   18.133    0.000 4380.629    0.001 tensor.py:155(backward)
                3172653   22.400    0.000 4362.496    0.001 __init__.py:57(backward)
                3172653 4260.030    0.001 4260.030    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               12690718  538.133    0.000 3079.530    0.000 rnn.py:109(flatten_parameters)
               12690712  131.849    0.000 2843.853    0.000 rnn.py:550(forward)
               63455060   33.898    0.000 2804.724    0.000 wrapper.py:25(act)
               63455060   82.794    0.000 2770.826    0.000 env.py:197(act)
               63455060 2636.325    0.000 2643.608    0.000 libenv.py:352(act)
               12690712 2553.972    0.000 2553.972    0.000 {built-in method lstm}
                3172753  115.833    0.000 2015.803    0.001 agent.py:44(<listcomp>)
               12690715 1937.292    0.000 1937.292    0.000 {built-in method _cudnn_rnn_flatten_weight}
                  31727    6.054    0.000 1759.881    0.055 agent.py:81(update_target_network)
               63455060  177.444    0.000 1624.899    0.000 exploration.py:31(epsilonGreedy)
                  31727  434.758    0.014 1472.441    0.046 memory.py:37(update_distribution)
               76144272   73.347    0.000 1287.935    0.000 activation.py:653(forward)
               76144272  118.204    0.000 1214.588    0.000 functional.py:1277(leaky_relu)
               66690968 1144.154    0.000 1144.154    0.000 {built-in method numpy.array}
              127067726   97.016    0.000 1113.035    0.000 extract_dict_ob.py:9(observe)
               76144272 1084.992    0.000 1084.992    0.000 {built-in method torch._C._nn.leaky_relu}
              127067726   58.879    0.000 1016.020    0.000 wrapper.py:19(observe)
              127067726  274.827    0.000  957.141    0.000 libenv.py:344(observe)
              101524896  815.658    0.000  815.658    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12690712   32.841    0.000  771.486    0.000 linear.py:90(forward)
               12690712   67.886    0.000  724.855    0.000 functional.py:1655(linear)
              101524896  724.195    0.000  724.195    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              190522786  208.087    0.000  669.148    0.000 libenv.py:281(_maybe_copy_dict)
              571600085  579.430    0.000  579.430    0.000 {method 'copy' of 'numpy.ndarray' objects}
               50763723  483.387    0.000  517.600    0.000 module.py:774(__setattr__)
               50762448  505.352    0.000  505.352    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               63455060   55.628    0.000  499.138    0.000 wrapper.py:22(get_info)
               12690712  484.392    0.000  484.392    0.000 {built-in method addmm}
              457235084  470.273    0.000  470.273    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                3172653  350.442    0.000  461.819    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               63455060  227.502    0.000  443.510    0.000 libenv.py:363(get_info)
               50762448  431.012    0.000  431.012    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3172653   79.681    0.000  429.120    0.000 optimizer.py:166(zero_grad)
               63455060  428.472    0.000  428.472    0.000 memory.py:15(inner)
               12690712   26.341    0.000  370.035    0.000 pooling.py:156(forward)
               50762448  357.581    0.000  357.581    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12690712   20.944    0.000  343.694    0.000 _jit_internal.py:237(fn)
               50762448  338.710    0.000  338.710    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               12690712   23.435    0.000  320.653    0.000 functional.py:564(_max_pool2d)
                9518259   15.231    0.000  301.869    0.000 functional.py:68(split)
               12690712  295.290    0.000  295.290    0.000 {built-in method max_pool2d}
                9518259   16.106    0.000  285.289    0.000 tensor.py:367(split)
               63455060  275.071    0.000  275.071    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9518259  267.530    0.000  267.530    0.000 {function Tensor.split at 0x7fea62a78940}
                3172454  244.654    0.000  244.654    0.000 memory.py:35(<listcomp>)
               50762860  208.499    0.000  241.350    0.000 __init__.py:66(is_acceptable)
                3172753   38.447    0.000  237.641    0.000 environments.py:76(<listcomp>)
               50762448  235.132    0.000  235.132    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3172753   22.240    0.000  232.164    0.000 collector.py:7(collect)
                3172653    9.077    0.000  208.969    0.000 loss.py:444(forward)
                6345507  208.463    0.000  208.464    0.000 {built-in method builtins.sum}
              254135452   75.069    0.000  207.048    0.000 libenv.py:271(_maybe_copy_ndarray)
                3172653   30.302    0.000  199.893    0.000 functional.py:2621(mse_loss)
               63455080   42.238    0.000  199.230    0.000 environments.py:79(reset)
              253812288  170.568    0.000  196.551    0.000 tensor.py:725(grad)
               31726730  180.510    0.000  180.510    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              216884595  163.507    0.000  164.169    0.000 module.py:758(__getattr__)
                  63454   17.394    0.000  161.967    0.003 {built-in method _pickle.loads}
              231605469  145.264    0.000  145.264    0.000 {built-in method torch._C._get_tracing_state}
                6345306  142.857    0.000  142.857    0.000 {built-in method gather}
                  63454   29.120    0.000  119.419    0.002 {built-in method _pickle.dumps}
                1142170    1.367    0.000  111.500    0.000 storage.py:141(_load_from_bytes)
                3172653  111.143    0.000  111.143    0.000 {built-in method torch._C._nn.mse_loss}
                8169651   11.665    0.000  110.177    0.000 <__array_function__ internals>:2(prod)
                1142170    5.972    0.000  110.133    0.000 serialization.py:486(load)
               12690712   33.261    0.000  104.604    0.000 rnn.py:524(check_forward_args)
              964494012  102.856    0.000  102.856    0.000 {method 'values' of 'collections.OrderedDict' objects}
               63612706   49.794    0.000   99.680    0.000 types.py:163(multimap)
               12690712   97.334    0.000   97.334    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8169691    8.636    0.000   96.738    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 8371225: <Base_bossfight_0> in cluster <dcc> Done

Job <Base_bossfight_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:30 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 18 01:04:34 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 18 01:04:34 2020
Terminated at Thu Nov 19 00:59:57 2020
Results reported at Thu Nov 19 00:59:57 2020

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

    CPU time :                                   88551.00 sec.
    Max Memory :                                 24569 MB
    Average Memory :                             24253.16 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               6151.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86123 sec.
    Turnaround time :                            97407 sec.

The output (if any) is above this job summary.

