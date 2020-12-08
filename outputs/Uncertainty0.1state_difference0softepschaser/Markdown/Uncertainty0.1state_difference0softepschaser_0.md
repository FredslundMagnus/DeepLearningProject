[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Uncertainty0.1state_difference0softepschaser-0
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
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      9456153906 function calls (9254134852 primitive calls) in 82522.82 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82522.825 82522.825 {built-in method builtins.exec}
                      1    0.023    0.023 82522.825 82522.825 <string>:1(<module>)
                      1  569.871  569.871 82522.797 82522.797 main.py:92(main)
                2000440  220.499    0.000 53579.733    0.027 agent.py:86(learn)
                1999940  636.400    0.000 52481.172    0.026 agent.py:96(TD_learn)
                1999940  142.751    0.000 31675.223    0.016 memory.py:35(sample_distribution)
                1999940  287.079    0.000 31012.735    0.016 helpers.py:15(stack)
               18000960 18582.383    0.001 18582.383    0.001 {built-in method cat}
                2000440  168.146    0.000 13804.705    0.007 agent.py:74(chooseMulti)
        216013020/14000580  990.227    0.000 13014.902    0.001 module.py:710(_call_impl)
                6000320  189.302    0.000 12024.312    0.002 agent.py:212(forward)
               20001508 12003.227    0.001 12003.242    0.001 {method 'to' of 'torch._C._TensorBase' objects}
              269095677 9269.964    0.000 9269.964    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2000440  122.901    0.000 8310.792    0.004 agent.py:84(<listcomp>)
               32002040  235.996    0.000 8199.807    0.000 container.py:115(forward)
                2000440   62.834    0.000 7875.266    0.004 environments.py:83(step)
               40008800 1054.507    0.000 7868.961    0.000 exploration.py:40(epsintosoftmax)
                2000440   78.846    0.000 6527.056    0.003 agent.py:62(rememberMulti)
                2000440  197.852    0.000 6103.266    0.003 agent.py:66(<listcomp>)
                5999820   34.010    0.000 5505.638    0.001 grad_mode.py:12(decorate_context)
                5999820 1400.739    0.000 5428.237    0.001 adam.py:51(step)
                5999820   29.918    0.000 4803.204    0.001 tensor.py:155(backward)
                2000440   50.746    0.000 4792.337    0.002 environments.py:85(<listcomp>)
               40338739 1260.291    0.000 4788.568    0.000 helpers.py:8(clean)
                5999820   35.518    0.000 4773.286    0.001 __init__.py:57(backward)
                5999820 4602.586    0.001 4602.586    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               46338559 3971.107    0.000 3971.107    0.000 {built-in method as_tensor}
               36001920   67.200    0.000 3063.700    0.000 conv.py:418(forward)
               36001920   80.281    0.000 2963.980    0.000 conv.py:410(_conv_forward)
               36001920 2869.500    0.000 2869.500    0.000 {built-in method conv2d}
                2000440   43.907    0.000 2789.917    0.001 environments.py:84(<listcomp>)
               40008800  158.614    0.000 2746.010    0.000 interop.py:274(step)
               48003560  105.375    0.000 2481.370    0.000 linear.py:90(forward)
               48003560  258.770    0.000 2322.119    0.000 functional.py:1655(linear)
               40008800 1417.106    0.000 2149.895    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6000326  342.363    0.000 1899.910    0.000 rnn.py:109(flatten_parameters)
                6000320   76.498    0.000 1687.787    0.000 rnn.py:550(forward)
                6000320 1523.758    0.000 1523.758    0.000 {built-in method lstm}
               40008800   18.957    0.000 1394.352    0.000 wrapper.py:25(act)
               40008800   51.911    0.000 1375.395    0.000 env.py:197(act)
               42002240 1355.073    0.000 1355.073    0.000 {built-in method addmm}
               40008800 1292.199    0.000 1296.058    0.000 libenv.py:352(act)
               76004720   71.662    0.000 1268.305    0.000 activation.py:653(forward)
               76004720  106.839    0.000 1196.643    0.000 functional.py:1277(leaky_relu)
                6000323 1115.352    0.000 1115.352    0.000 {built-in method _cudnn_rnn_flatten_weight}
               76004720 1079.370    0.000 1079.370    0.000 {built-in method torch._C._nn.leaky_relu}
              119996400 1031.114    0.000 1031.114    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   4000    1.934    0.000  878.061    0.220 agent.py:139(update_target_network)
              119996400  865.704    0.000  865.704    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               80347539   61.852    0.000  759.864    0.000 extract_dict_ob.py:9(observe)
               80347539   36.727    0.000  698.012    0.000 wrapper.py:19(observe)
               80347539  168.325    0.000  661.284    0.000 libenv.py:344(observe)
               59998200  622.759    0.000  622.759    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               53034818   57.793    0.000  562.097    0.000 <__array_function__ internals>:2(prod)
                   4000  146.482    0.037  543.248    0.136 memory.py:45(update_distribution)
               28982862   59.632    0.000  528.842    0.000 functional.py:1465(softmax)
               59998200  524.458    0.000  524.458    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5999820   90.745    0.000  513.029    0.000 optimizer.py:166(zero_grad)
               53034858   43.445    0.000  494.468    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              120356339  131.850    0.000  489.459    0.000 libenv.py:281(_maybe_copy_dict)
                2000440    5.081    0.000  478.276    0.000 agent.py:230(avoid_similar_state)
               28982862  464.656    0.000  464.656    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               42016740  460.187    0.000  460.187    0.000 {built-in method numpy.array}
               53034818   66.925    0.000  451.023    0.000 fromnumeric.py:2881(prod)
              361073017  429.990    0.000  429.990    0.000 {method 'copy' of 'numpy.ndarray' objects}
              298436440  425.559    0.000  425.559    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               59998200  408.883    0.000  408.883    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               40008800  406.546    0.000  406.546    0.000 memory.py:17(inner)
               59998200  392.603    0.000  392.603    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               28002995  367.620    0.000  389.784    0.000 module.py:774(__setattr__)
               53034818  128.282    0.000  384.098    0.000 fromnumeric.py:70(_wrapreduction)
                5999820   13.015    0.000  380.813    0.000 loss.py:444(forward)
                5999820   51.434    0.000  367.798    0.000 functional.py:2621(mse_loss)
               48003560  339.401    0.000  339.401    0.000 {method 't' of 'torch._C._TensorBase' objects}
               40008800   35.966    0.000  320.158    0.000 wrapper.py:22(get_info)
               40008800  318.930    0.000  318.930    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               59998200  285.290    0.000  285.290    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               40008800  144.644    0.000  284.192    0.000 libenv.py:363(get_info)
                   8000  239.872    0.030  284.182    0.036 {built-in method _pickle.loads}
                6001320   12.113    0.000  266.371    0.000 functional.py:68(split)
                6001320   12.583    0.000  253.467    0.000 tensor.py:367(split)
                1999940  198.244    0.000  251.575    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                6001320  239.622    0.000  239.622    0.000 {function Tensor.split at 0x7f8af308f940}
                2000440   22.766    0.000  230.176    0.000 environments.py:86(<listcomp>)
                2000440  189.171    0.000  229.974    0.000 agent.py:131(convert_values)
               55038758  221.271    0.000  221.271    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              299991108  187.514    0.000  216.826    0.000 tensor.py:725(grad)
               24001292  193.067    0.000  212.250    0.000 __init__.py:66(is_acceptable)
                2304438  210.503    0.000  210.503    0.000 {built-in method tensor}
                6000320   19.749    0.000  209.346    0.000 pooling.py:156(forward)
               40008820   29.952    0.000  207.430    0.000 environments.py:89(reset)
                5999820  207.238    0.000  207.238    0.000 {built-in method torch._C._nn.mse_loss}
               36000920  201.662    0.000  201.662    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                7999760  193.858    0.000  193.858    0.000 {built-in method gather}
                6000320   11.329    0.000  189.598    0.000 _jit_internal.py:237(fn)
                6000320   12.548    0.000  177.256    0.000 functional.py:564(_max_pool2d)
                1999940  176.305    0.000  176.305    0.000 memory.py:43(<listcomp>)
                6001320  175.102    0.000  175.102    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6000320  163.845    0.000  163.845    0.000 {built-in method max_pool2d}
              212334268  158.863    0.000  159.038    0.000 module.py:758(__getattr__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8483322: <Uncertainty0.1state_difference0softepschaser_0> in cluster <dcc> Done

Job <Uncertainty0.1state_difference0softepschaser_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Sat Dec  5 16:31:57 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Dec  6 04:31:34 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec  6 04:31:34 2020
Terminated at Mon Dec  7 03:27:07 2020
Results reported at Mon Dec  7 03:27:07 2020

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

    CPU time :                                   90326.00 sec.
    Max Memory :                                 54321 MB
    Average Memory :                             53685.98 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7119.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82534 sec.
    Turnaround time :                            125710 sec.

The output (if any) is above this job summary.

