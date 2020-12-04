[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Fepsintosoftmax_stateUncertainty0and0bigfish-0
    Discount :                  0.995
    Environment :               bigfish
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
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      10536180868 function calls (10311224209 primitive calls) in 82549.61 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82549.609 82549.609 {built-in method builtins.exec}
                      1    0.040    0.040 82549.609 82549.609 <string>:1(<module>)
                      1  498.690  498.690 82549.568 82549.568 main.py:92(main)
                2227545  191.065    0.000 52201.752    0.023 agent.py:86(learn)
                2227045  810.144    0.000 51211.140    0.023 agent.py:96(TD_learn)
                2227045  144.659    0.000 24142.270    0.011 memory.py:35(sample_distribution)
                2227045  257.312    0.000 23457.815    0.011 helpers.py:15(stack)
        240540360/15590315 1055.508    0.000 15422.370    0.001 module.py:710(_call_impl)
                2227545  207.913    0.000 14425.122    0.006 agent.py:74(chooseMulti)
                6681635  210.361    0.000 14230.248    0.002 agent.py:212(forward)
               22272558 12254.875    0.001 12254.924    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20044905 10855.623    0.001 10855.623    0.001 {built-in method cat}
               35635720  294.867    0.000 9953.839    0.000 container.py:115(forward)
              300672180 8506.667    0.000 8506.667    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6681135   39.090    0.000 8225.854    0.001 grad_mode.py:12(decorate_context)
                2227545   61.613    0.000 8143.873    0.004 environments.py:83(step)
                6681135 1956.181    0.000 8140.128    0.001 adam.py:51(step)
                2227545  141.340    0.000 8093.891    0.004 agent.py:84(<listcomp>)
               44550900 1320.813    0.000 7589.867    0.000 exploration.py:40(epsintosoftmax)
                2227545   93.748    0.000 7078.111    0.003 agent.py:62(rememberMulti)
                2227545  277.509    0.000 6627.226    0.003 agent.py:66(<listcomp>)
                6681135   30.599    0.000 6083.530    0.001 tensor.py:155(backward)
                6681135   35.246    0.000 6052.931    0.001 __init__.py:57(backward)
                6681135 5849.063    0.001 5849.063    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2227545   59.729    0.000 5195.466    0.002 environments.py:85(<listcomp>)
               44775267 1253.022    0.000 5165.790    0.000 helpers.py:8(clean)
               51456402 4352.221    0.000 4352.221    0.000 {built-in method as_tensor}
               40089810   71.226    0.000 3643.967    0.000 conv.py:418(forward)
               40089810   85.250    0.000 3538.795    0.000 conv.py:410(_conv_forward)
               40089810 3439.438    0.000 3439.438    0.000 {built-in method conv2d}
               53454080  111.925    0.000 3079.262    0.000 linear.py:90(forward)
               53454080  311.372    0.000 2913.240    0.000 functional.py:1655(linear)
                2227545   46.732    0.000 2683.013    0.001 environments.py:84(<listcomp>)
               44550900  176.095    0.000 2636.280    0.000 interop.py:274(step)
               44550900 1702.201    0.000 2534.519    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6681641  365.602    0.000 2287.573    0.000 rnn.py:109(flatten_parameters)
                6681635   82.245    0.000 1762.889    0.000 rnn.py:550(forward)
               46771445 1741.071    0.000 1741.071    0.000 {built-in method addmm}
               84634710   76.810    0.000 1666.372    0.000 activation.py:653(forward)
              133622700 1626.859    0.000 1626.859    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               84634710  112.427    0.000 1589.562    0.000 functional.py:1277(leaky_relu)
                6681635 1587.256    0.000 1587.256    0.000 {built-in method lstm}
                6681638 1484.464    0.000 1484.464    0.000 {built-in method _cudnn_rnn_flatten_weight}
               84634710 1466.497    0.000 1466.497    0.000 {built-in method torch._C._nn.leaky_relu}
              133622700 1409.191    0.000 1409.191    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               44550900   19.665    0.000 1178.793    0.000 wrapper.py:25(act)
               44550900   65.251    0.000 1159.129    0.000 env.py:197(act)
               44550900 1051.536    0.000 1055.557    0.000 libenv.py:352(act)
               66811350  894.247    0.000  894.247    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6681135  124.765    0.000  812.082    0.000 optimizer.py:166(zero_grad)
                   4455    1.559    0.000  799.547    0.179 agent.py:139(update_target_network)
               89326167   69.728    0.000  789.428    0.000 extract_dict_ob.py:9(observe)
               66811350  756.349    0.000  756.349    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89326167   36.651    0.000  719.700    0.000 wrapper.py:19(observe)
               33299952   67.269    0.000  708.729    0.000 functional.py:1465(softmax)
               89326167  177.905    0.000  683.049    0.000 libenv.py:344(observe)
               66811350  650.552    0.000  650.552    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               58029033   63.123    0.000  643.714    0.000 <__array_function__ internals>:2(prod)
               33299952  635.969    0.000  635.969    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               66811350  632.123    0.000  632.123    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2227545    5.979    0.000  589.115    0.000 agent.py:230(avoid_similar_state)
               58029073   46.115    0.000  568.183    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              333630662  557.629    0.000  557.629    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               58029033   72.986    0.000  522.068    0.000 fromnumeric.py:2881(prod)
               66811350  498.053    0.000  498.053    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              133877067  143.067    0.000  496.688    0.000 libenv.py:281(_maybe_copy_dict)
                   4455  144.276    0.032  483.662    0.109 memory.py:45(update_distribution)
                6681135   15.828    0.000  453.343    0.000 loss.py:444(forward)
               58029033  135.476    0.000  449.082    0.000 fromnumeric.py:70(_wrapreduction)
              401635656  441.275    0.000  441.275    0.000 {method 'copy' of 'numpy.ndarray' objects}
               53454080  437.682    0.000  437.682    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6681135   56.263    0.000  437.515    0.000 functional.py:2621(mse_loss)
               46786855  415.603    0.000  415.603    0.000 {built-in method numpy.array}
               31182465  339.128    0.000  363.745    0.000 module.py:774(__setattr__)
               44550900  362.684    0.000  362.684    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               44550900   38.531    0.000  354.903    0.000 wrapper.py:22(get_info)
               44550900  345.879    0.000  345.879    0.000 memory.py:17(inner)
               44550900  165.393    0.000  316.372    0.000 libenv.py:363(get_info)
                2227545  250.038    0.000  279.226    0.000 agent.py:131(convert_values)
                2227045  217.089    0.000  276.201    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               60260533  275.670    0.000  275.670    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                   8910  219.266    0.025  267.213    0.030 {built-in method _pickle.loads}
                6682635   12.850    0.000  263.178    0.000 functional.py:68(split)
              334056858  228.105    0.000  261.181    0.000 tensor.py:725(grad)
                6681135  259.361    0.000  259.361    0.000 {built-in method torch._C._nn.mse_loss}
               40088810  252.280    0.000  252.280    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6681635   22.399    0.000  249.838    0.000 pooling.py:156(forward)
                6682635   13.296    0.000  249.575    0.000 tensor.py:367(split)
                8908180  240.984    0.000  240.984    0.000 {built-in method gather}
                6682635  234.837    0.000  234.837    0.000 {function Tensor.split at 0x7f0cf6dbb940}
                6681635   11.990    0.000  227.440    0.000 _jit_internal.py:237(fn)
                6681635   13.680    0.000  214.337    0.000 functional.py:564(_max_pool2d)
                6682635  210.429    0.000  210.429    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2566123  205.186    0.000  205.186    0.000 {built-in method tensor}
                2227545   25.932    0.000  203.782    0.000 environments.py:86(<listcomp>)
               26726552  179.585    0.000  200.094    0.000 __init__.py:66(is_acceptable)
                6681635  199.848    0.000  199.848    0.000 {built-in method max_pool2d}
               44550920   32.042    0.000  177.896    0.000 environments.py:89(reset)
              240540360  175.871    0.000  175.871    0.000 {built-in method torch._C._get_tracing_state}
                2227045  172.610    0.000  172.610    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8467079: <Fepsintosoftmax_stateUncertainty0and0bigfish_0> in cluster <dcc> Done

Job <Fepsintosoftmax_stateUncertainty0and0bigfish_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Dec  3 01:03:41 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Dec  3 01:31:37 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 01:31:37 2020
Terminated at Fri Dec  4 00:27:49 2020
Results reported at Fri Dec  4 00:27:49 2020

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

    CPU time :                                   84901.00 sec.
    Max Memory :                                 53906 MB
    Average Memory :                             53175.67 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7534.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82575 sec.
    Turnaround time :                            84248 sec.

The output (if any) is above this job summary.

