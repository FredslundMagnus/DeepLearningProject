[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Dist_LowMem-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    50000.0
    Update every :              100
    Use distribution :          1.0
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      11252567178 function calls (11021044038 primitive calls) in 86115.76 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86115.760 86115.760 {built-in method builtins.exec}
                      1    0.023    0.023 86115.760 86115.760 <string>:1(<module>)
                      1  525.667  525.667 86115.737 86115.737 main.py:9(main)
                3404737  109.669    0.000 58227.357    0.017 agent.py:46(learn)
                3404637  398.380    0.000 57480.079    0.017 agent.py:54(TD_learn)
                3404637  212.986    0.000 34762.521    0.010 memory.py:27(sample_distribution)
                3404637  296.918    0.000 33731.291    0.010 helpers.py:12(stack)
               30642081 18362.838    0.001 18362.912    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        248540301/17023285 1012.067    0.000 15992.253    0.001 module.py:710(_call_impl)
               13618648  268.773    0.000 15639.908    0.001 agent.py:117(forward)
               30642033 14686.040    0.000 14686.040    0.000 {built-in method cat}
                3404737   88.301    0.000 11359.324    0.003 environments.py:73(step)
              476163633 9341.796    0.000 9341.796    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               40855944  252.192    0.000 8591.572    0.000 container.py:115(forward)
                3404737    9.672    0.000 7900.521    0.002 agent.py:32(rememberMulti)
                3404737  268.018    0.000 7890.850    0.002 agent.py:33(<listcomp>)
                3404737   48.665    0.000 7865.468    0.002 agent.py:41(chooseMulti)
                3404737   67.061    0.000 6692.698    0.002 environments.py:75(<listcomp>)
               68285484 1785.919    0.000 6646.328    0.000 helpers.py:8(clean)
               78499395 5594.764    0.000 5594.764    0.000 {built-in method as_tensor}
               68093240  108.973    0.000 4994.721    0.000 conv.py:418(forward)
               68093240  126.278    0.000 4838.878    0.000 conv.py:410(_conv_forward)
               68093240 4689.840    0.000 4689.840    0.000 {built-in method conv2d}
                3404637   20.821    0.000 4479.877    0.001 grad_mode.py:12(decorate_context)
                3404637   18.324    0.000 4440.931    0.001 tensor.py:155(backward)
                3404637 1134.545    0.000 4433.236    0.001 adam.py:51(step)
                3404637   21.909    0.000 4422.607    0.001 __init__.py:57(backward)
                3404737   67.067    0.000 4362.152    0.001 environments.py:74(<listcomp>)
                3404637 4317.080    0.001 4317.080    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               68094740  238.897    0.000 4295.085    0.000 interop.py:274(step)
               13618654  568.564    0.000 3240.224    0.000 rnn.py:109(flatten_parameters)
                3404737  115.647    0.000 3229.443    0.001 agent.py:44(<listcomp>)
               13618648  135.985    0.000 2888.796    0.000 rnn.py:550(forward)
               68094740  177.392    0.000 2848.118    0.000 exploration.py:31(epsilonGreedy)
               13618648 2586.474    0.000 2586.474    0.000 {built-in method lstm}
               68094740   28.661    0.000 2298.950    0.000 wrapper.py:25(act)
               68094740   81.093    0.000 2270.289    0.000 env.py:197(act)
               68094740 2137.458    0.000 2143.738    0.000 libenv.py:352(act)
               13618651 2003.401    0.000 2003.401    0.000 {built-in method _cudnn_rnn_flatten_weight}
               81711888   74.084    0.000 1272.734    0.000 activation.py:653(forward)
               81711888  113.132    0.000 1198.650    0.000 functional.py:1277(leaky_relu)
               81711888 1075.273    0.000 1075.273    0.000 {built-in method torch._C._nn.leaky_relu}
              136380224   99.584    0.000 1068.673    0.000 extract_dict_ob.py:9(observe)
              136380224   54.857    0.000  969.089    0.000 wrapper.py:19(observe)
              136380224  253.896    0.000  914.232    0.000 libenv.py:344(observe)
              108948384  817.934    0.000  817.934    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13618648   33.961    0.000  796.583    0.000 linear.py:90(forward)
               13618648   69.259    0.000  749.083    0.000 functional.py:1655(linear)
              108948384  719.811    0.000  719.811    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              204474964  204.255    0.000  654.316    0.000 libenv.py:281(_maybe_copy_dict)
                  34047    5.898    0.000  637.608    0.019 agent.py:81(update_target_network)
              613458939  555.645    0.000  555.645    0.000 {method 'copy' of 'numpy.ndarray' objects}
               54475467  508.353    0.000  546.364    0.000 module.py:774(__setattr__)
               54474192  499.867    0.000  499.867    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               13618648  496.543    0.000  496.543    0.000 {built-in method addmm}
               68094740   53.094    0.000  488.199    0.000 wrapper.py:22(get_info)
                3404637  354.369    0.000  468.577    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
              492805370  461.468    0.000  461.468    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               68094740  230.384    0.000  435.106    0.000 libenv.py:363(get_info)
               68094740  422.703    0.000  422.703    0.000 memory.py:15(inner)
               54474192  417.052    0.000  417.052    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3404637   69.489    0.000  413.846    0.000 optimizer.py:166(zero_grad)
               71567272  377.106    0.000  377.106    0.000 {built-in method numpy.array}
               13618648   27.823    0.000  372.543    0.000 pooling.py:156(forward)
                  34047   96.155    0.003  360.327    0.011 memory.py:37(update_distribution)
               54474192  353.894    0.000  353.894    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               13618648   20.527    0.000  344.720    0.000 _jit_internal.py:237(fn)
               54474192  333.227    0.000  333.227    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13618648   23.367    0.000  322.055    0.000 functional.py:564(_max_pool2d)
               13618648  297.120    0.000  297.120    0.000 {built-in method max_pool2d}
               10214211   15.362    0.000  289.630    0.000 functional.py:68(split)
               10214211   15.768    0.000  273.063    0.000 tensor.py:367(split)
               68094740  265.679    0.000  265.679    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               54474604  231.485    0.000  264.709    0.000 __init__.py:66(is_acceptable)
               10214211  255.651    0.000  255.651    0.000 {function Tensor.split at 0x7f9fc421f940}
                3404438  238.940    0.000  238.940    0.000 memory.py:35(<listcomp>)
               54474192  236.549    0.000  236.549    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3404737   35.632    0.000  216.173    0.000 environments.py:76(<listcomp>)
                3404737   22.029    0.000  215.236    0.000 collector.py:7(collect)
                3404637    8.311    0.000  213.733    0.000 loss.py:444(forward)
                3404637   33.121    0.000  205.422    0.000 functional.py:2621(mse_loss)
                6809475  191.697    0.000  191.698    0.000 {built-in method builtins.sum}
              272760448   67.684    0.000  190.983    0.000 libenv.py:271(_maybe_copy_ndarray)
               68094760   35.370    0.000  180.573    0.000 environments.py:79(reset)
              272371008  151.979    0.000  178.569    0.000 tensor.py:725(grad)
               34046570  177.866    0.000  177.866    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              232743027  171.164    0.000  171.819    0.000 module.py:758(__getattr__)
                  68094   16.624    0.000  155.287    0.002 {built-in method _pickle.loads}
              248540301  148.949    0.000  148.949    0.000 {built-in method torch._C._get_tracing_state}
                6809274  148.880    0.000  148.880    0.000 {built-in method gather}
                  68094   28.602    0.000  116.097    0.002 {built-in method _pickle.dumps}
                3404637  113.668    0.000  113.668    0.000 {built-in method torch._C._nn.mse_loss}
               13618648   35.093    0.000  108.608    0.000 rnn.py:524(check_forward_args)
                1225690    1.290    0.000  107.074    0.000 storage.py:141(_load_from_bytes)
                1225690    5.714    0.000  105.784    0.000 serialization.py:486(load)
               13618648  103.837    0.000  103.837    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1035017148   96.046    0.000   96.046    0.000 {method 'values' of 'collections.OrderedDict' objects}
               68285524   48.163    0.000   94.074    0.000 types.py:163(multimap)
                1225690    6.452    0.000   88.310    0.000 serialization.py:605(_legacy_load)
               13618651   39.295    0.000   85.669    0.000 __init__.py:264(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8366049: <Dist_LowMem_0> in cluster <dcc> Done

Job <Dist_LowMem_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Nov 16 19:57:02 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov 16 20:45:36 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 16 20:45:36 2020
Terminated at Tue Nov 17 20:40:58 2020
Results reported at Tue Nov 17 20:40:58 2020

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

    CPU time :                                   88308.00 sec.
    Max Memory :                                 8566 MB
    Average Memory :                             8295.88 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               22154.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86121 sec.
    Turnaround time :                            89036 sec.

The output (if any) is above this job summary.

