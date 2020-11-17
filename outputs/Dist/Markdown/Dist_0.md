[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Dist-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    200000
    Update every :              100
    Use distribution :          1.0
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      10172477489 function calls (9963194157 primitive calls) in 86138.67 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86138.666 86138.666 {built-in method builtins.exec}
                      1    0.036    0.036 86138.666 86138.666 <string>:1(<module>)
                      1  574.651  574.651 86138.629 86138.629 main.py:9(main)
                3077681  113.595    0.000 59519.478    0.019 agent.py:46(learn)
                3077581  377.461    0.000 57632.654    0.019 agent.py:54(TD_learn)
                3077581  221.187    0.000 35611.333    0.012 memory.py:27(sample_distribution)
                3077581  362.175    0.000 34589.725    0.011 helpers.py:12(stack)
               27698577 17060.257    0.001 17060.323    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               27698529 16735.221    0.001 16735.221    0.001 {built-in method cat}
        224665213/15388005  990.029    0.000 15600.960    0.001 module.py:710(_call_impl)
               12310424  248.406    0.000 15273.036    0.001 agent.py:117(forward)
                3077681   86.221    0.000 11188.810    0.004 environments.py:73(step)
               36931272  243.760    0.000 8376.139    0.000 container.py:115(forward)
              430375172 8200.481    0.000 8200.481    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3077681    9.600    0.000 8163.048    0.003 agent.py:32(rememberMulti)
                3077681  262.143    0.000 8153.448    0.003 agent.py:33(<listcomp>)
                3077681   58.801    0.000 6554.954    0.002 environments.py:75(<listcomp>)
               61737059 1794.717    0.000 6517.540    0.000 helpers.py:8(clean)
                3077681   46.251    0.000 6435.538    0.002 agent.py:41(chooseMulti)
               70969802 5522.843    0.000 5522.843    0.000 {built-in method as_tensor}
               61552120  107.463    0.000 4850.537    0.000 conv.py:418(forward)
               61552120  127.972    0.000 4697.664    0.000 conv.py:410(_conv_forward)
               61552120 4547.754    0.000 4547.754    0.000 {built-in method conv2d}
                3077681   65.872    0.000 4323.518    0.001 environments.py:74(<listcomp>)
                3077581   18.797    0.000 4292.378    0.001 grad_mode.py:12(decorate_context)
                3077581   18.049    0.000 4281.073    0.001 tensor.py:155(backward)
                3077581   26.097    0.000 4263.024    0.001 __init__.py:57(backward)
               61553620  230.268    0.000 4257.646    0.000 interop.py:274(step)
                3077581 1092.550    0.000 4250.897    0.001 adam.py:51(step)
                3077581 4158.425    0.001 4158.425    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               12310430  560.531    0.000 3143.532    0.000 rnn.py:109(flatten_parameters)
               12310424  136.436    0.000 2872.725    0.000 rnn.py:550(forward)
               12310424 2573.291    0.000 2573.291    0.000 {built-in method lstm}
               61553620   32.617    0.000 2311.821    0.000 wrapper.py:25(act)
               61553620   76.970    0.000 2279.204    0.000 env.py:197(act)
               61553620 2154.307    0.000 2160.238    0.000 libenv.py:352(act)
               12310427 1933.414    0.000 1933.414    0.000 {built-in method _cudnn_rnn_flatten_weight}
                3077681  109.867    0.000 1853.214    0.001 agent.py:44(<listcomp>)
                  30776    6.504    0.000 1773.229    0.058 agent.py:81(update_target_network)
                  30776  428.845    0.014 1502.461    0.049 memory.py:37(update_distribution)
               61553620  173.279    0.000 1473.839    0.000 exploration.py:31(epsilonGreedy)
               73862544   73.677    0.000 1252.654    0.000 activation.py:653(forward)
               73862544  116.467    0.000 1178.977    0.000 functional.py:1277(leaky_relu)
               64692554 1171.751    0.000 1171.751    0.000 {built-in method numpy.array}
               73862544 1051.183    0.000 1051.183    0.000 {built-in method torch._C._nn.leaky_relu}
              123290679   91.219    0.000 1047.284    0.000 extract_dict_ob.py:9(observe)
              123290679   52.765    0.000  956.065    0.000 wrapper.py:19(observe)
              123290679  233.700    0.000  903.300    0.000 libenv.py:344(observe)
               98482592  783.253    0.000  783.253    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12310424   33.736    0.000  771.063    0.000 linear.py:90(forward)
               12310424   71.172    0.000  723.988    0.000 functional.py:1655(linear)
               98482592  690.084    0.000  690.084    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              184844299  199.111    0.000  666.510    0.000 libenv.py:281(_maybe_copy_dict)
              554563673  576.603    0.000  576.603    0.000 {method 'copy' of 'numpy.ndarray' objects}
               49242571  519.564    0.000  555.764    0.000 module.py:774(__setattr__)
               12310424  478.959    0.000  478.959    0.000 {built-in method addmm}
               49241296  477.680    0.000  477.680    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               61553620   52.328    0.000  475.994    0.000 wrapper.py:22(get_info)
              445396239  466.929    0.000  466.929    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               61553620  458.071    0.000  458.071    0.000 memory.py:15(inner)
                3077581  338.924    0.000  447.677    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               61553620  220.136    0.000  423.666    0.000 libenv.py:363(get_info)
               49241296  402.879    0.000  402.879    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3077581   68.582    0.000  396.395    0.000 optimizer.py:166(zero_grad)
               12310424   29.916    0.000  374.338    0.000 pooling.py:156(forward)
               12310424   20.614    0.000  344.422    0.000 _jit_internal.py:237(fn)
               49241296  335.095    0.000  335.095    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12310424   23.540    0.000  321.815    0.000 functional.py:564(_max_pool2d)
               49241296  321.643    0.000  321.643    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9233043   14.819    0.000  304.920    0.000 functional.py:68(split)
               12310424  296.473    0.000  296.473    0.000 {built-in method max_pool2d}
                9233043   16.109    0.000  288.849    0.000 tensor.py:367(split)
                9233043  271.108    0.000  271.108    0.000 {function Tensor.split at 0x7f1b1c7a6940}
               61553620  269.508    0.000  269.508    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               49241708  219.589    0.000  253.764    0.000 __init__.py:66(is_acceptable)
                3077382  240.081    0.000  240.081    0.000 memory.py:35(<listcomp>)
                3077681   37.098    0.000  224.117    0.000 environments.py:76(<listcomp>)
               49241296  222.578    0.000  222.578    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3077681   20.628    0.000  210.715    0.000 collector.py:7(collect)
                3077581    7.962    0.000  200.107    0.000 loss.py:444(forward)
                3077581   30.447    0.000  192.145    0.000 functional.py:2621(mse_loss)
                6155363  188.675    0.000  188.675    0.000 {built-in method builtins.sum}
               61553640   38.090    0.000  187.066    0.000 environments.py:79(reset)
              246581358   66.660    0.000  186.945    0.000 libenv.py:271(_maybe_copy_ndarray)
               30776010  171.027    0.000  171.027    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              246206528  146.855    0.000  170.702    0.000 tensor.py:725(grad)
              210385463  166.475    0.000  167.100    0.000 module.py:758(__getattr__)
                  61552   16.481    0.000  150.479    0.002 {built-in method _pickle.loads}
                6155162  144.594    0.000  144.594    0.000 {built-in method gather}
              224665213  139.597    0.000  139.597    0.000 {built-in method torch._C._get_tracing_state}
                  61552   28.134    0.000  113.785    0.002 {built-in method _pickle.dumps}
               12310424   36.863    0.000  109.061    0.000 rnn.py:524(check_forward_args)
                3077581  106.242    0.000  106.242    0.000 {built-in method torch._C._nn.mse_loss}
                1107934    1.251    0.000  103.799    0.000 storage.py:141(_load_from_bytes)
                1107934    5.552    0.000  102.549    0.000 serialization.py:486(load)
               12310424   99.701    0.000   99.701    0.000 {method 't' of 'torch._C._TensorBase' objects}
               61737099   47.237    0.000   93.297    0.000 types.py:163(multimap)
              935592124   93.137    0.000   93.137    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1107934    6.204    0.000   85.635    0.000 serialization.py:605(_legacy_load)
               12310427   36.949    0.000   84.086    0.000 __init__.py:264(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 8366039: <Dist_0> in cluster <dcc> Done

Job <Dist_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Nov 16 19:52:14 2020
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov 16 19:52:15 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 16 19:52:15 2020
Terminated at Tue Nov 17 19:48:14 2020
Results reported at Tue Nov 17 19:48:14 2020

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

    CPU time :                                   89007.00 sec.
    Max Memory :                                 25335 MB
    Average Memory :                             25040.54 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5385.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86200 sec.
    Turnaround time :                            86160 sec.

The output (if any) is above this job summary.

