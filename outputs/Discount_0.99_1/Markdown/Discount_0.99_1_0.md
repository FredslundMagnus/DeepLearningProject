[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
Discount_0.99_1-0 0.99 fruitbot 20.0 200000 100
    Play for :                  1 games.
    Minutes used :              1198 minutes.
    Hours used :                19 hours.

# Profiling


      2310260472 function calls (2249321588 primitive calls) in 71916.71 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 71916.709 71916.709 {built-in method builtins.exec}
                      1    0.022    0.022 71916.709 71916.709 <string>:1(<module>)
                      1  134.627  134.627 71916.686 71916.686 main.py:16(main)
                1075254  157.944    0.000 67504.487    0.063 agent.py:45(learn)
                1075254   90.704    0.000 21634.831    0.020 memory.py:27(sample_distribution)
                1075254  128.147    0.000 21126.947    0.020 helpers.py:12(stack)
        65592294/4659534  401.883    0.000 17419.290    0.004 module.py:710(_call_impl)
                3584280   97.470    0.000 17279.333    0.005 agent.py:94(forward)
                7527126 15307.356    0.002 15307.390    0.002 {method 'to' of 'torch._C._TensorBase' objects}
               10752840   97.615    0.000 14625.668    0.001 container.py:115(forward)
                1075254    8.531    0.000 13274.639    0.012 tensor.py:155(backward)
                1075254    9.617    0.000 13266.108    0.012 __init__.py:57(backward)
                1075254 13219.769    0.012 13219.769    0.012 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1075254    3.681    0.000 12607.007    0.012 memory.py:75(empty_cache)
                1075254 12601.931    0.012 12601.931    0.012 {built-in method torch._C._cuda_emptyCache}
               21505680   29.087    0.000 8513.586    0.000 activation.py:653(forward)
               21505680   47.555    0.000 8484.499    0.000 functional.py:1277(leaky_relu)
               21505680 8432.452    0.000 8432.452    0.000 {built-in method torch._C._nn.leaky_relu}
                7527078 5425.700    0.001 5425.700    0.001 {built-in method cat}
               17921400   43.798    0.000 5211.474    0.000 conv.py:418(forward)
               17921400   47.947    0.000 5148.435    0.000 conv.py:410(_conv_forward)
               17921400 5091.279    0.000 5091.279    0.000 {built-in method conv2d}
                1075254    9.457    0.000 2416.747    0.002 grad_mode.py:12(decorate_context)
                1075254  605.291    0.001 2395.546    0.002 adam.py:51(step)
                 358518    7.530    0.000 1691.127    0.005 agent.py:40(chooseMulti)
                 358518   10.958    0.000 1383.637    0.004 environments.py:73(step)
                3584286  215.758    0.000 1216.341    0.000 rnn.py:109(flatten_parameters)
                3584280   53.751    0.000 1089.581    0.000 rnn.py:550(forward)
               49609033 1003.790    0.000 1003.790    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                 358518   20.181    0.000  976.567    0.003 agent.py:43(<listcomp>)
                3584280  972.853    0.000  972.853    0.000 {built-in method lstm}
                 358518    1.132    0.000  972.002    0.003 agent.py:32(rememberMulti)
                 358518   32.859    0.000  970.870    0.003 agent.py:33(<listcomp>)
                7170360  350.761    0.000  903.678    0.000 exploration.py:28(epsilonGreedy)
               10435275  881.510    0.000  881.510    0.000 {built-in method as_tensor}
                 358518    7.446    0.000  780.926    0.002 environments.py:75(<listcomp>)
                7209513  220.803    0.000  778.150    0.000 helpers.py:8(clean)
                3584283  753.672    0.000  753.672    0.000 {built-in method _cudnn_rnn_flatten_weight}
                 358518    8.723    0.000  562.277    0.002 environments.py:74(<listcomp>)
                7170360   31.177    0.000  553.555    0.000 interop.py:274(step)
               34408128  442.577    0.000  442.577    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               34408128  400.697    0.000  400.697    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7170360    4.111    0.000  299.376    0.000 wrapper.py:25(act)
                3584280   12.898    0.000  299.253    0.000 linear.py:90(forward)
                7170360   10.571    0.000  295.265    0.000 env.py:197(act)
                3584280   26.861    0.000  280.256    0.000 functional.py:1655(linear)
                7170360  278.328    0.000  279.170    0.000 libenv.py:352(act)
               17204064  268.236    0.000  268.236    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               14337995  212.312    0.000  226.174    0.000 module.py:774(__setattr__)
               17204064  225.931    0.000  225.931    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1075254  167.680    0.000  219.971    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                1075254   37.967    0.000  217.408    0.000 optimizer.py:166(zero_grad)
               17204064  190.320    0.000  190.320    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   3585    0.850    0.000  189.962    0.053 agent.py:63(update_target_network)
                3584280  185.168    0.000  185.168    0.000 {built-in method addmm}
               17204064  179.732    0.000  179.732    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   3585   44.987    0.013  153.257    0.043 memory.py:37(update_distribution)
                7170360  152.261    0.000  152.261    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                7170360  144.946    0.000  144.946    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                3584280   12.607    0.000  140.402    0.000 pooling.py:156(forward)
               14379873   12.695    0.000  136.801    0.000 extract_dict_ob.py:9(observe)
                3584280    8.062    0.000  127.794    0.000 _jit_internal.py:237(fn)
               14379873    7.185    0.000  124.106    0.000 wrapper.py:19(observe)
                8252184  123.226    0.000  123.226    0.000 {built-in method numpy.array}
               17204064  120.069    0.000  120.069    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3584280    7.690    0.000  118.931    0.000 functional.py:564(_max_pool2d)
               14379873   31.476    0.000  116.921    0.000 libenv.py:344(observe)
                3584280  110.640    0.000  110.640    0.000 {built-in method max_pool2d}
               14337132   85.921    0.000   99.122    0.000 __init__.py:66(is_acceptable)
               86020368   83.793    0.000   97.760    0.000 tensor.py:725(grad)
                1075254    2.973    0.000   91.700    0.000 loss.py:444(forward)
                1074654   90.378    0.000   90.378    0.000 memory.py:35(<listcomp>)
                1075254   12.801    0.000   88.727    0.000 functional.py:2621(mse_loss)
               21550233   25.157    0.000   84.892    0.000 libenv.py:281(_maybe_copy_dict)
               54907037   75.060    0.000   75.060    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9319068   73.647    0.000   73.647    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               64654284   73.331    0.000   73.331    0.000 {method 'copy' of 'numpy.ndarray' objects}
                2150508   69.303    0.000   69.303    0.000 {built-in method gather}
               61062139   66.274    0.000   66.366    0.000 module.py:758(__getattr__)
                7170360    6.665    0.000   60.787    0.000 wrapper.py:22(get_info)
                1074655   58.343    0.000   58.343    0.000 {built-in method numpy.arange}
               65592294   57.035    0.000   57.035    0.000 {built-in method torch._C._get_tracing_state}
                1075554    2.557    0.000   54.485    0.000 functional.py:68(split)
                7170360   27.765    0.000   54.122    0.000 libenv.py:363(get_info)
                2242368    5.248    0.000   53.893    0.000 <__array_function__ internals>:2(prod)
                7170360   52.708    0.000   52.708    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1075554    2.455    0.000   51.733    0.000 tensor.py:367(split)
                3320607   50.808    0.000   50.808    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                1075254   49.974    0.000   49.974    0.000 {built-in method torch._C._nn.mse_loss}
                1075554   48.995    0.000   48.995    0.000 {function Tensor.split at 0x7f6dafc34790}
                2242408    4.089    0.000   47.849    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7170360   46.752    0.000   46.752    0.000 memory.py:15(inner)
                2242368    6.793    0.000   43.760    0.000 fromnumeric.py:2881(prod)
                3584280   13.802    0.000   42.091    0.000 rnn.py:524(check_forward_args)
                3584280   39.300    0.000   39.300    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 583487   16.311    0.000   39.293    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2242368   11.771    0.000   36.968    0.000 fromnumeric.py:70(_wrapreduction)
              273122016   36.680    0.000   36.680    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1075254    8.686    0.000   36.207    0.000 __init__.py:25(_make_grads)
                1078239    2.949    0.000   35.553    0.000 {method 'sum' of 'numpy.ndarray' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 8273879: <Discount_0.99_1_0> in cluster <dcc> Done

Job <Discount_0.99_1_0> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Sat Nov  7 15:36:09 2020
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov  7 15:53:11 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov  7 15:53:11 2020
Terminated at Sun Nov  8 11:51:54 2020
Results reported at Sun Nov  8 11:51:54 2020

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

    CPU time :                                   33012.00 sec.
    Max Memory :                                 24942 MB
    Average Memory :                             24467.40 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5778.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   71923 sec.
    Turnaround time :                            72945 sec.

The output (if any) is above this job summary.

