[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Uncertainty0state_difference0.1softepschaser-0
    Discount :                  0.995
    Environment :               chaser
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsintosoftmax
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11896215084 function calls (11642510593 primitive calls) in 82523.97 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82523.968 82523.968 {built-in method builtins.exec}
                      1    0.031    0.031 82523.968 82523.968 <string>:1(<module>)
                      1  478.171  478.171 82523.934 82523.934 main.py:92(main)
                2512177  195.685    0.000 48545.218    0.019 agent.py:86(learn)
                2511677  649.763    0.000 47478.023    0.019 agent.py:96(TD_learn)
                2511677  142.588    0.000 24650.074    0.010 memory.py:35(sample_distribution)
                2511677  210.266    0.000 23954.421    0.010 helpers.py:15(stack)
                2512177  183.645    0.000 17816.289    0.007 agent.py:74(chooseMulti)
        271280616/17582739 1069.420    0.000 13846.944    0.001 module.py:710(_call_impl)
               25118878 12981.229    0.001 12981.235    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                7535531  204.382    0.000 12761.219    0.002 agent.py:212(forward)
              340244800 11962.569    0.000 11962.569    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2512177  141.337    0.000 11810.468    0.005 agent.py:84(<listcomp>)
               50243540 1269.760    0.000 11313.714    0.000 exploration.py:40(epsintosoftmax)
               22606593 10705.562    0.000 10705.562    0.000 {built-in method cat}
                2512177   67.405    0.000 9016.798    0.004 environments.py:83(step)
               40189832  272.908    0.000 8979.574    0.000 container.py:115(forward)
                7535031   37.603    0.000 6549.618    0.001 grad_mode.py:12(decorate_context)
                2512177   90.983    0.000 6467.429    0.003 agent.py:62(rememberMulti)
                7535031 1645.683    0.000 6461.341    0.001 adam.py:51(step)
                2512177  209.310    0.000 6002.180    0.002 agent.py:66(<listcomp>)
                2512177   63.945    0.000 5609.078    0.002 environments.py:85(<listcomp>)
               50658949 1496.880    0.000 5599.589    0.000 helpers.py:8(clean)
                7535031   28.063    0.000 5282.356    0.001 tensor.py:155(backward)
                7535031   33.175    0.000 5254.293    0.001 __init__.py:57(backward)
                7535031 5074.612    0.001 5074.612    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               58193980 4489.362    0.000 4489.362    0.000 {built-in method as_tensor}
               45213186   76.785    0.000 3328.246    0.000 conv.py:418(forward)
               45213186   84.882    0.000 3216.439    0.000 conv.py:410(_conv_forward)
               45213186 3115.233    0.000 3115.233    0.000 {built-in method conv2d}
                2512177   51.564    0.000 3086.000    0.001 environments.py:84(<listcomp>)
               50243540  183.766    0.000 3034.435    0.000 interop.py:274(step)
               60285248  119.632    0.000 2730.070    0.000 linear.py:90(forward)
               60285248  301.491    0.000 2552.639    0.000 functional.py:1655(linear)
               50243540 1695.415    0.000 2543.724    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7535537  334.605    0.000 1920.198    0.000 rnn.py:109(flatten_parameters)
                7535531   74.212    0.000 1624.507    0.000 rnn.py:550(forward)
               50243540   26.516    0.000 1540.231    0.000 wrapper.py:25(act)
               50243540   63.893    0.000 1513.715    0.000 env.py:197(act)
               52748717 1484.311    0.000 1484.311    0.000 {built-in method addmm}
                7535531 1460.048    0.000 1460.048    0.000 {built-in method lstm}
               50243540 1412.790    0.000 1417.602    0.000 libenv.py:352(act)
               95450726   82.629    0.000 1405.899    0.000 activation.py:653(forward)
               95450726  119.582    0.000 1323.270    0.000 functional.py:1277(leaky_relu)
              150700620 1208.708    0.000 1208.708    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                7535534 1191.744    0.000 1191.744    0.000 {built-in method _cudnn_rnn_flatten_weight}
               95450726 1191.515    0.000 1191.515    0.000 {built-in method torch._C._nn.leaky_relu}
              150700620 1054.303    0.000 1054.303    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   5024    1.641    0.000  871.510    0.173 agent.py:139(update_target_network)
              100902489   76.024    0.000  813.338    0.000 extract_dict_ob.py:9(observe)
               75350310  748.085    0.000  748.085    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              100902489   42.646    0.000  737.313    0.000 wrapper.py:19(observe)
              100902489  185.059    0.000  694.668    0.000 libenv.py:344(observe)
               64290703   65.374    0.000  642.701    0.000 <__array_function__ internals>:2(prod)
                7535031  114.358    0.000  630.321    0.000 optimizer.py:166(zero_grad)
               38708194   66.343    0.000  620.134    0.000 functional.py:1465(softmax)
               75350310  611.589    0.000  611.589    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               64290743   52.407    0.000  565.776    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               38708194  547.321    0.000  547.321    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2512177    6.245    0.000  545.978    0.000 agent.py:230(avoid_similar_state)
                   5024  153.441    0.031  531.859    0.106 memory.py:45(update_distribution)
               64290703   76.289    0.000  513.370    0.000 fromnumeric.py:2881(prod)
              151146029  151.233    0.000  500.890    0.000 libenv.py:281(_maybe_copy_dict)
               75350310  496.646    0.000  496.646    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75350310  484.498    0.000  484.498    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               52765265  453.900    0.000  453.900    0.000 {built-in method numpy.array}
              377090678  451.026    0.000  451.026    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               64290703  147.651    0.000  437.081    0.000 fromnumeric.py:70(_wrapreduction)
              453443111  430.038    0.000  430.038    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7535031   13.066    0.000  404.835    0.000 loss.py:444(forward)
                7535031   51.600    0.000  391.769    0.000 functional.py:2621(mse_loss)
               50243540   39.716    0.000  362.537    0.000 wrapper.py:22(get_info)
               50243540  355.418    0.000  355.418    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               75350310  350.974    0.000  350.974    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               60285248  349.117    0.000  349.117    0.000 {method 't' of 'torch._C._TensorBase' objects}
               35167313  305.700    0.000  329.058    0.000 module.py:774(__setattr__)
               50243540  326.518    0.000  326.518    0.000 memory.py:17(inner)
               50243540  169.833    0.000  322.821    0.000 libenv.py:363(get_info)
                  10048  237.086    0.024  287.209    0.029 {built-in method _pickle.loads}
                2511677  224.325    0.000  284.622    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                2512177  213.769    0.000  281.007    0.000 agent.py:131(convert_values)
              376751658  224.781    0.000  259.803    0.000 tensor.py:725(grad)
                7536531   12.363    0.000  256.120    0.000 functional.py:68(split)
                2512177   26.984    0.000  254.316    0.000 environments.py:86(<listcomp>)
               66807404  247.936    0.000  247.936    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                7536531   13.002    0.000  242.786    0.000 tensor.py:367(split)
                7536531  228.288    0.000  228.288    0.000 {function Tensor.split at 0x7f9f22f8f940}
               50243560   34.452    0.000  227.340    0.000 environments.py:89(reset)
                2893999  220.539    0.000  220.539    0.000 {built-in method tensor}
                7535031  219.060    0.000  219.060    0.000 {built-in method torch._C._nn.mse_loss}
               45212186  217.483    0.000  217.483    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                7535531   15.078    0.000  211.505    0.000 pooling.py:156(forward)
               10046708  210.061    0.000  210.061    0.000 {built-in method gather}
                7535531   11.949    0.000  196.427    0.000 _jit_internal.py:237(fn)
                7536531  190.471    0.000  190.471    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               30142136  169.612    0.000  188.636    0.000 __init__.py:66(is_acceptable)
                7535531   13.024    0.000  183.301    0.000 functional.py:564(_max_pool2d)
                2511677  180.072    0.000  180.072    0.000 memory.py:43(<listcomp>)
              266660310  177.825    0.000  178.032    0.000 module.py:758(__getattr__)
                2512177   16.506    0.000  170.222    0.000 collector.py:7(collect)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 8483320: <Uncertainty0state_difference0.1softepschaser_0> in cluster <dcc> Done

Job <Uncertainty0state_difference0.1softepschaser_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Sat Dec  5 16:31:57 2020
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Dec  6 03:26:50 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec  6 03:26:50 2020
Terminated at Mon Dec  7 02:22:23 2020
Results reported at Mon Dec  7 02:22:23 2020

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

    CPU time :                                   86158.00 sec.
    Max Memory :                                 54460 MB
    Average Memory :                             53762.18 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6980.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82533 sec.
    Turnaround time :                            121826 sec.

The output (if any) is above this job summary.

