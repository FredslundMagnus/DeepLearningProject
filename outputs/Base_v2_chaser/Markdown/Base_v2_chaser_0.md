[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_chaser-0
    Discount :                  0.995
    Environment :               chaser
    Hours :                     24
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      9119131443 function calls (8919630809 primitive calls) in 86120.19 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86120.189 86120.189 {built-in method builtins.exec}
                      1    0.032    0.032 86120.189 86120.189 <string>:1(<module>)
                      1  491.264  491.264 86120.154 86120.154 main.py:11(main)
                2625302  100.134    0.000 53978.295    0.021 agent.py:46(learn)
                2624802  385.596    0.000 53142.449    0.020 agent.py:54(TD_learn)
                2624802  187.512    0.000 28284.405    0.011 memory.py:27(sample_distribution)
                2624802  313.023    0.000 27409.485    0.010 helpers.py:12(stack)
        212618962/13124510  909.563    0.000 16639.983    0.001 module.py:710(_call_impl)
               10499708  234.235    0.000 16331.760    0.002 agent.py:119(forward)
              355891746 14264.617    0.000 14264.617    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               23624772 14197.629    0.001 14197.631    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2625302   44.392    0.000 13695.565    0.005 agent.py:41(chooseMulti)
               23624718 12548.041    0.001 12548.041    0.001 {built-in method cat}
                2625302   72.260    0.000 9958.462    0.004 environments.py:73(step)
               31499124  255.795    0.000 9315.954    0.000 container.py:115(forward)
                2625302  130.996    0.000 8903.357    0.003 agent.py:44(<listcomp>)
               52506040  183.456    0.000 8443.463    0.000 exploration.py:33(epsilonGreedy)
                2625302    8.361    0.000 7795.286    0.003 agent.py:32(rememberMulti)
                2625302  335.170    0.000 7786.925    0.003 agent.py:33(<listcomp>)
                2625302   55.415    0.000 6073.369    0.002 environments.py:75(<listcomp>)
               52924599 1494.982    0.000 6073.159    0.000 helpers.py:8(clean)
                2624802   17.487    0.000 5684.138    0.002 grad_mode.py:12(decorate_context)
                2624802 1352.301    0.001 5646.743    0.002 adam.py:51(step)
               62998248  105.058    0.000 5572.576    0.000 conv.py:418(forward)
               62998248  122.186    0.000 5418.017    0.000 conv.py:410(_conv_forward)
               62998248 5274.925    0.000 5274.925    0.000 {built-in method conv2d}
               60799005 5254.775    0.000 5254.775    0.000 {built-in method as_tensor}
                2624802   15.979    0.000 4801.156    0.002 tensor.py:155(backward)
                2624802   18.905    0.000 4785.176    0.002 __init__.py:57(backward)
                2624802 4690.155    0.002 4690.155    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2625302   55.648    0.000 3519.168    0.001 environments.py:74(<listcomp>)
               10499714  540.856    0.000 3499.577    0.000 rnn.py:109(flatten_parameters)
               52506040  206.595    0.000 3463.520    0.000 interop.py:274(step)
               10499708  114.278    0.000 2708.453    0.000 rnn.py:550(forward)
               10499708 2452.118    0.000 2452.118    0.000 {built-in method lstm}
               10499711 2312.531    0.000 2312.531    0.000 {built-in method _cudnn_rnn_flatten_weight}
               52506040   24.103    0.000 1754.140    0.000 wrapper.py:25(act)
               52506040   78.591    0.000 1730.037    0.000 env.py:197(act)
               52506040 1600.276    0.000 1605.069    0.000 libenv.py:352(act)
               73497956   66.425    0.000 1489.709    0.000 activation.py:653(forward)
               73497956  109.944    0.000 1423.284    0.000 functional.py:1277(leaky_relu)
               73497956 1304.005    0.000 1304.005    0.000 {built-in method torch._C._nn.leaky_relu}
               94492872 1122.322    0.000 1122.322    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               94492872  988.049    0.000  988.049    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              105430639   88.398    0.000  923.135    0.000 extract_dict_ob.py:9(observe)
              105430639   49.105    0.000  834.736    0.000 wrapper.py:19(observe)
              105430639  212.405    0.000  785.631    0.000 libenv.py:344(observe)
               10499708   30.574    0.000  758.012    0.000 linear.py:90(forward)
                   5250    1.249    0.000  735.712    0.140 agent.py:81(update_target_network)
               10499708   60.207    0.000  716.108    0.000 functional.py:1655(linear)
                   5250  189.424    0.036  670.176    0.128 memory.py:37(update_distribution)
               47246436  613.398    0.000  613.398    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              368178678  611.711    0.000  611.711    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               55141342  576.566    0.000  576.566    0.000 {built-in method numpy.array}
              157936679  170.978    0.000  562.491    0.000 libenv.py:281(_maybe_copy_dict)
                2624802   86.238    0.000  555.789    0.000 optimizer.py:166(zero_grad)
               41999812  509.905    0.000  540.320    0.000 module.py:774(__setattr__)
               47246436  524.361    0.000  524.361    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              473815287  495.145    0.000  495.145    0.000 {method 'copy' of 'numpy.ndarray' objects}
               10499708  485.809    0.000  485.809    0.000 {built-in method addmm}
               47246436  453.431    0.000  453.431    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47246436  443.103    0.000  443.103    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11650534  165.292    0.000  416.400    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               52506040   46.705    0.000  416.106    0.000 wrapper.py:22(get_info)
               52506040  404.519    0.000  404.519    0.000 memory.py:15(inner)
                2624802  288.472    0.000  378.719    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               52506040  191.854    0.000  369.400    0.000 libenv.py:363(get_info)
               10499708   24.906    0.000  363.713    0.000 pooling.py:156(forward)
               47246436  341.761    0.000  341.761    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10499708   17.533    0.000  338.807    0.000 _jit_internal.py:237(fn)
               52506040  328.898    0.000  328.898    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               10499708   19.889    0.000  319.603    0.000 functional.py:564(_max_pool2d)
               25926010   27.112    0.000  301.906    0.000 <__array_function__ internals>:2(prod)
               41998844  268.371    0.000  299.561    0.000 __init__.py:66(is_acceptable)
               10499708  298.521    0.000  298.521    0.000 {built-in method max_pool2d}
                2625302   33.244    0.000  293.664    0.000 environments.py:76(<listcomp>)
                7875906   12.759    0.000  270.693    0.000 functional.py:68(split)
               25926050   20.156    0.000  270.472    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               52506060   39.623    0.000  260.434    0.000 environments.py:79(reset)
                7875906   14.023    0.000  256.990    0.000 tensor.py:367(split)
               25926010   32.798    0.000  250.315    0.000 fromnumeric.py:2881(prod)
                7875906  241.508    0.000  241.508    0.000 {function Tensor.split at 0x7f46349e6940}
               25926010   60.851    0.000  217.517    0.000 fromnumeric.py:70(_wrapreduction)
                2624802  203.557    0.000  203.557    0.000 memory.py:35(<listcomp>)
                2624802    6.794    0.000  196.292    0.000 loss.py:444(forward)
               26249020  194.252    0.000  194.252    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2624802   26.032    0.000  189.498    0.000 functional.py:2621(mse_loss)
              236232234  158.578    0.000  182.282    0.000 tensor.py:725(grad)
                2625302   17.550    0.000  174.152    0.000 collector.py:7(collect)
              210861278   55.369    0.000  170.749    0.000 libenv.py:271(_maybe_copy_ndarray)
               28556062  166.991    0.000  166.991    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              212618962  164.792    0.000  164.792    0.000 {built-in method torch._C._get_tracing_state}
                5250605  155.457    0.000  155.457    0.000 {built-in method builtins.sum}
              199704801  153.162    0.000  153.282    0.000 module.py:758(__getattr__)
                5249604  149.645    0.000  149.645    0.000 {built-in method gather}
                2624802  113.113    0.000  113.113    0.000 {built-in method torch._C._nn.mse_loss}
               10499708  109.150    0.000  109.150    0.000 {method 't' of 'torch._C._TensorBase' objects}
               10499708   31.793    0.000   93.166    0.000 rnn.py:524(check_forward_args)
               52924639   40.003    0.000   82.578    0.000 types.py:163(multimap)
              881974972   79.733    0.000   79.733    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8411693: <Base_v2_chaser_0> in cluster <dcc> Done

Job <Base_v2_chaser_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Sun Nov 22 15:16:12 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Nov 22 19:32:53 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 22 19:32:53 2020
Terminated at Mon Nov 23 19:28:22 2020
Results reported at Mon Nov 23 19:28:22 2020

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

    CPU time :                                   90690.00 sec.
    Max Memory :                                 57127 MB
    Average Memory :                             56351.01 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4313.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86129 sec.
    Turnaround time :                            101530 sec.

The output (if any) is above this job summary.

  File "main.py", line 10
    if 12321 ===!! asdasd:
               ^
SyntaxError: invalid syntax

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 8416078: <Base_v2_chaser_0> in cluster <dcc> Exited

Job <Base_v2_chaser_0> was submitted from host <n-62-27-20> by user <s183914> in cluster <dcc> at Mon Nov 23 22:15:25 2020
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Nov 23 23:51:44 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 23 23:51:44 2020
Terminated at Mon Nov 23 23:51:46 2020
Results reported at Mon Nov 23 23:51:46 2020

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.19 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   2 sec.
    Turnaround time :                            5781 sec.

The output (if any) is above this job summary.

