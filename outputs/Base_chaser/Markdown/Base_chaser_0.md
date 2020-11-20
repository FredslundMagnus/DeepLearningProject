[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_chaser-0
    Discount :                  0.999
    Environment :               chaser
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


      9949447422 function calls (9745490802 primitive calls) in 86118.21 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86118.205 86118.205 {built-in method builtins.exec}
                      1    0.010    0.010 86118.205 86118.205 <string>:1(<module>)
                      1  559.974  559.974 86118.193 86118.193 main.py:11(main)
                2999347  124.705    0.000 59989.675    0.020 agent.py:46(learn)
                2999247  383.290    0.000 57822.390    0.019 agent.py:54(TD_learn)
                2999247  213.422    0.000 35950.918    0.012 memory.py:27(sample_distribution)
                2999247  329.180    0.000 34935.457    0.012 helpers.py:12(stack)
               26993571 17705.331    0.001 17705.371    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               26993523 16449.215    0.001 16449.215    0.001 {built-in method cat}
        218946831/14996335 1032.173    0.000 15660.535    0.001 module.py:710(_call_impl)
               11997088  252.283    0.000 15330.952    0.001 agent.py:117(forward)
                2999347   89.816    0.000 10843.315    0.004 environments.py:73(step)
               35991264  246.828    0.000 8351.262    0.000 container.py:115(forward)
              417407406 7970.284    0.000 7970.284    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2999347    9.800    0.000 7967.762    0.003 agent.py:32(rememberMulti)
                2999347  284.696    0.000 7957.962    0.003 agent.py:33(<listcomp>)
                2999347   51.416    0.000 6526.275    0.002 agent.py:41(chooseMulti)
                2999347   62.673    0.000 6508.956    0.002 environments.py:75(<listcomp>)
               60454562 1763.920    0.000 6502.972    0.000 helpers.py:8(clean)
               69452303 5544.594    0.000 5544.594    0.000 {built-in method as_tensor}
               59985440  109.639    0.000 4797.083    0.000 conv.py:418(forward)
               59985440  125.170    0.000 4641.516    0.000 conv.py:410(_conv_forward)
               59985440 4494.222    0.000 4494.222    0.000 {built-in method conv2d}
                2999247   19.441    0.000 4243.210    0.001 grad_mode.py:12(decorate_context)
                2999247   18.659    0.000 4208.209    0.001 tensor.py:155(backward)
                2999247 1073.778    0.000 4200.128    0.001 adam.py:51(step)
                2999247   21.272    0.000 4189.551    0.001 __init__.py:57(backward)
                2999247 4090.231    0.001 4090.231    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2999347   66.067    0.000 3951.426    0.001 environments.py:74(<listcomp>)
               59986940  226.265    0.000 3885.358    0.000 interop.py:274(step)
               11997094  571.708    0.000 3175.005    0.000 rnn.py:109(flatten_parameters)
               11997088  138.201    0.000 2924.265    0.000 rnn.py:550(forward)
               11997088 2616.092    0.000 2616.092    0.000 {built-in method lstm}
                  29993    6.986    0.000 2042.580    0.068 agent.py:81(update_target_network)
               59986940   28.768    0.000 1963.874    0.000 wrapper.py:25(act)
               59986940   78.744    0.000 1935.106    0.000 env.py:197(act)
               11997091 1923.848    0.000 1923.848    0.000 {built-in method _cudnn_rnn_flatten_weight}
                2999347  115.539    0.000 1858.509    0.001 agent.py:44(<listcomp>)
               59986940 1806.894    0.000 1812.746    0.000 libenv.py:352(act)
                  29993  458.837    0.015 1770.082    0.059 memory.py:37(update_distribution)
               59986940  178.381    0.000 1483.260    0.000 exploration.py:31(epsilonGreedy)
               63045974 1408.964    0.000 1408.964    0.000 {built-in method numpy.array}
               71982528   74.062    0.000 1227.274    0.000 activation.py:653(forward)
               71982528  116.506    0.000 1153.212    0.000 functional.py:1277(leaky_relu)
              120441502   91.599    0.000 1041.507    0.000 extract_dict_ob.py:9(observe)
               71982528 1026.272    0.000 1026.272    0.000 {built-in method torch._C._nn.leaky_relu}
              120441502   55.123    0.000  949.908    0.000 wrapper.py:19(observe)
              120441502  239.531    0.000  894.786    0.000 libenv.py:344(observe)
               95975904  771.722    0.000  771.722    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11997088   34.482    0.000  767.791    0.000 linear.py:90(forward)
               11997088   71.070    0.000  719.879    0.000 functional.py:1655(linear)
               95975904  676.919    0.000  676.919    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              180428442  204.922    0.000  652.997    0.000 libenv.py:281(_maybe_copy_dict)
               47989227  523.665    0.000  560.361    0.000 module.py:774(__setattr__)
              541315319  558.177    0.000  558.177    0.000 {method 'copy' of 'numpy.ndarray' objects}
              431468437  484.131    0.000  484.131    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11997088  476.005    0.000  476.005    0.000 {built-in method addmm}
               47987952  472.489    0.000  472.489    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               59986940   53.126    0.000  469.494    0.000 wrapper.py:22(get_info)
                2999247  336.843    0.000  447.860    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               59986940  213.391    0.000  416.367    0.000 libenv.py:363(get_info)
               59986940  414.674    0.000  414.674    0.000 memory.py:15(inner)
               47987952  401.879    0.000  401.879    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2999247   69.081    0.000  399.417    0.000 optimizer.py:166(zero_grad)
               11997088   40.513    0.000  385.845    0.000 pooling.py:156(forward)
               11997088   21.256    0.000  345.331    0.000 _jit_internal.py:237(fn)
               47987952  330.391    0.000  330.391    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47987952  323.298    0.000  323.298    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11997088   24.233    0.000  322.049    0.000 functional.py:564(_max_pool2d)
               11997088  296.265    0.000  296.265    0.000 {built-in method max_pool2d}
                2999347   38.276    0.000  293.118    0.000 environments.py:76(<listcomp>)
                8998041   14.813    0.000  293.081    0.000 functional.py:68(split)
                8998041   16.542    0.000  277.093    0.000 tensor.py:367(split)
               47988364  231.865    0.000  265.453    0.000 __init__.py:66(is_acceptable)
               59986940  259.710    0.000  259.710    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8998041  259.045    0.000  259.045    0.000 {function Tensor.split at 0x7fb760ea2940}
               59986960   42.245    0.000  254.876    0.000 environments.py:79(reset)
                2999048  232.976    0.000  232.976    0.000 memory.py:35(<listcomp>)
               47987952  222.138    0.000  222.138    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2999347   20.396    0.000  207.054    0.000 collector.py:7(collect)
                2999247    7.740    0.000  197.032    0.000 loss.py:444(forward)
                2999247   29.788    0.000  189.292    0.000 functional.py:2621(mse_loss)
              240883004   65.639    0.000  185.882    0.000 libenv.py:271(_maybe_copy_ndarray)
                5998695  185.117    0.000  185.117    0.000 {built-in method builtins.sum}
              239939808  150.991    0.000  174.629    0.000 tensor.py:725(grad)
               29992670  168.160    0.000  168.160    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              205030563  166.157    0.000  166.764    0.000 module.py:758(__getattr__)
                  59986   17.389    0.000  151.465    0.003 {built-in method _pickle.loads}
                5998494  145.009    0.000  145.009    0.000 {built-in method gather}
              218946831  144.624    0.000  144.624    0.000 {built-in method torch._C._get_tracing_state}
               11997088   39.232    0.000  114.851    0.000 rnn.py:524(check_forward_args)
                  59986   28.402    0.000  114.047    0.002 {built-in method _pickle.dumps}
                8001735   11.672    0.000  109.772    0.000 <__array_function__ internals>:2(prod)
                2999247  106.148    0.000  106.148    0.000 {built-in method torch._C._nn.mse_loss}
                1079746    1.187    0.000  103.717    0.000 storage.py:141(_load_from_bytes)
                1079746    5.485    0.000  102.530    0.000 serialization.py:486(load)
               11997088  100.128    0.000  100.128    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8001775    8.527    0.000   96.295    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               60454602   45.212    0.000   93.560    0.000 types.py:163(multimap)
               11030776   91.059    0.000   91.059    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8371227: <Base_chaser_0> in cluster <dcc> Done

Job <Base_chaser_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:30 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 18 02:16:07 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 18 02:16:07 2020
Terminated at Thu Nov 19 02:11:32 2020
Results reported at Thu Nov 19 02:11:32 2020

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

    CPU time :                                   88056.00 sec.
    Max Memory :                                 25471 MB
    Average Memory :                             25176.97 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5249.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86126 sec.
    Turnaround time :                            101702 sec.

The output (if any) is above this job summary.

