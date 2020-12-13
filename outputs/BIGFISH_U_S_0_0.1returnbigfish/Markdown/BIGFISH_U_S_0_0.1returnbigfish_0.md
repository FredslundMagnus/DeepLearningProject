[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0_0.1returnbigfish-0
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
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      9208627612 function calls (8996973156 primitive calls) in 82513.75 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82513.747 82513.747 {built-in method builtins.exec}
                      1    0.022    0.022 82513.747 82513.747 <string>:1(<module>)
                      1  552.674  552.674 82513.724 82513.724 main.py:92(main)
                2154880  261.511    0.000 57025.233    0.026 agent.py:84(learn)
                2067923  883.752    0.000 56208.246    0.027 agent.py:99(TD_learn)
                2067923  159.757    0.000 29123.272    0.014 memory.py:35(sample_distribution)
                2067923  316.242    0.000 28377.760    0.014 helpers.py:15(stack)
               18872178 16271.642    0.001 16271.642    0.001 {built-in method cat}
        226211259/14563417 1012.037    0.000 15283.830    0.001 module.py:710(_call_impl)
                6290726  206.605    0.000 14120.964    0.002 agent.py:231(forward)
               20941208 11543.271    0.001 11543.273    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               33522552  288.009    0.000 9801.466    0.000 container.py:115(forward)
                2154880  204.042    0.000 9275.136    0.004 agent.py:70(chooseMulti)
                2154880   66.206    0.000 8308.850    0.004 environments.py:83(step)
                6203769   37.624    0.000 8014.853    0.001 grad_mode.py:12(decorate_context)
                6203769 1914.279    0.000 7930.535    0.001 adam.py:51(step)
              280333757 7475.996    0.000 7475.996    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2068922   90.858    0.000 7181.463    0.003 agent.py:58(rememberMulti)
                2068922  275.991    0.000 6732.736    0.003 agent.py:62(<listcomp>)
                6203769   39.130    0.000 6136.246    0.001 tensor.py:155(backward)
                6203769   36.138    0.000 6097.116    0.001 __init__.py:57(backward)
                6203769 5891.905    0.001 5891.905    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2154880   61.961    0.000 5267.745    0.002 environments.py:85(<listcomp>)
               43455888 1308.558    0.000 5255.610    0.000 helpers.py:8(clean)
               49659657 4540.675    0.000 4540.675    0.000 {built-in method as_tensor}
               37744356   68.968    0.000 3643.434    0.000 conv.py:418(forward)
               37744356   82.465    0.000 3542.142    0.000 conv.py:410(_conv_forward)
               37744356 3445.324    0.000 3445.324    0.000 {built-in method conv2d}
               50241848  106.112    0.000 3030.443    0.000 linear.py:90(forward)
               50241848  296.619    0.000 2872.817    0.000 functional.py:1655(linear)
                2068922   97.461    0.000 2795.132    0.001 agent.py:82(<listcomp>)
                2154880   48.140    0.000 2737.445    0.001 environments.py:84(<listcomp>)
               43097600  178.237    0.000 2689.305    0.000 interop.py:274(step)
               41378440  135.855    0.000 2427.562    0.000 exploration.py:34(epsilonGreedy)
                6290732  349.224    0.000 2240.716    0.000 rnn.py:109(flatten_parameters)
                6290726   76.141    0.000 1865.783    0.000 rnn.py:550(forward)
               44035082 1720.336    0.000 1720.336    0.000 {built-in method addmm}
                6290726 1696.578    0.000 1696.578    0.000 {built-in method lstm}
               79626556   75.487    0.000 1620.505    0.000 activation.py:653(forward)
              124075380 1559.155    0.000 1559.155    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               79626556  104.741    0.000 1545.018    0.000 functional.py:1277(leaky_relu)
                6290729 1453.488    0.000 1453.488    0.000 {built-in method _cudnn_rnn_flatten_weight}
               79626556 1429.773    0.000 1429.773    0.000 {built-in method torch._C._nn.leaky_relu}
              124075380 1367.896    0.000 1367.896    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               43097600   20.707    0.000 1191.522    0.000 wrapper.py:25(act)
               43097600   67.656    0.000 1170.815    0.000 env.py:197(act)
               43097600 1059.539    0.000 1063.608    0.000 libenv.py:352(act)
               62037690  909.398    0.000  909.398    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               86553488   72.343    0.000  815.891    0.000 extract_dict_ob.py:9(observe)
                6203769  120.584    0.000  772.696    0.000 optimizer.py:166(zero_grad)
               86553488   38.806    0.000  743.548    0.000 wrapper.py:19(observe)
               62037690  731.306    0.000  731.306    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               86553488  177.984    0.000  704.743    0.000 libenv.py:344(observe)
               62037690  626.780    0.000  626.780    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               62037690  612.198    0.000  612.198    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2068922    5.604    0.000  575.956    0.000 agent.py:249(avoid_similar_state)
                   2154    1.003    0.000  555.476    0.258 agent.py:157(update_target_network)
              318471104  536.666    0.000  536.666    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              129651088  147.118    0.000  516.170    0.000 libenv.py:281(_maybe_copy_dict)
               62037690  472.964    0.000  472.964    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              388955418  461.961    0.000  461.961    0.000 {method 'copy' of 'numpy.ndarray' objects}
               50241848  445.712    0.000  445.712    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6203769   12.935    0.000  441.943    0.000 loss.py:444(forward)
               41378440  435.713    0.000  435.713    0.000 memory.py:17(inner)
                6203769   53.077    0.000  429.008    0.000 functional.py:2621(mse_loss)
               29300585  375.382    0.000  398.162    0.000 module.py:774(__setattr__)
               11096676  155.169    0.000  393.638    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               43097600   39.971    0.000  366.112    0.000 wrapper.py:22(get_info)
               12407538  331.996    0.000  331.996    0.000 {built-in method gather}
               43097600  170.232    0.000  326.141    0.000 libenv.py:363(get_info)
                2067923  234.473    0.000  306.269    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               47910057  304.902    0.000  304.902    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   2154   88.360    0.041  295.766    0.137 memory.py:45(update_distribution)
               45169831  287.770    0.000  287.770    0.000 {built-in method numpy.array}
               43097600  280.011    0.000  280.011    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24261415   23.605    0.000  277.936    0.000 <__array_function__ internals>:2(prod)
                2068922  256.331    0.000  275.700    0.000 agent.py:149(convert_values)
                6203769  255.682    0.000  255.682    0.000 {built-in method torch._C._nn.mse_loss}
              310188558  222.385    0.000  253.565    0.000 tensor.py:725(grad)
               24261455   18.455    0.000  250.324    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6464640   11.600    0.000  241.287    0.000 functional.py:68(split)
                6290726   16.274    0.000  238.168    0.000 pooling.py:156(forward)
                2154880   24.529    0.000  237.453    0.000 environments.py:86(<listcomp>)
                   4308  209.133    0.049  234.015    0.054 {built-in method _pickle.loads}
               24261415   30.275    0.000  231.869    0.000 fromnumeric.py:2881(prod)
                6464640   12.358    0.000  228.811    0.000 tensor.py:367(split)
                6290726   11.140    0.000  221.894    0.000 _jit_internal.py:237(fn)
                6464640  215.021    0.000  215.021    0.000 {function Tensor.split at 0x7f33e25db9d0}
               43097620   33.720    0.000  212.929    0.000 environments.py:89(reset)
                6206766  210.342    0.000  210.342    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               25162916  190.206    0.000  209.873    0.000 __init__.py:66(is_acceptable)
                6290726   12.791    0.000  209.760    0.000 functional.py:564(_max_pool2d)
                2232624  205.628    0.000  205.628    0.000 {built-in method tensor}
               24261415   55.837    0.000  201.594    0.000 fromnumeric.py:70(_wrapreduction)
                6290726  196.195    0.000  196.195    0.000 {built-in method max_pool2d}
               12408537  189.958    0.000  189.958    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                2067923  184.118    0.000  184.118    0.000 memory.py:43(<listcomp>)
              226211259  168.402    0.000  168.402    0.000 {built-in method torch._C._get_tracing_state}
                6203769   39.788    0.000  166.829    0.000 __init__.py:25(_make_grads)
              222249360  158.724    0.000  158.827    0.000 module.py:758(__getattr__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8557621: <BIGFISH_U_S_0_0.1returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0_0.1returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:46 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Dec 11 21:02:30 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 11 21:02:30 2020
Terminated at Sat Dec 12 19:57:50 2020
Results reported at Sat Dec 12 19:57:50 2020

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

    CPU time :                                   88537.00 sec.
    Max Memory :                                 54041 MB
    Average Memory :                             53395.39 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7399.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82521 sec.
    Turnaround time :                            100564 sec.

The output (if any) is above this job summary.

