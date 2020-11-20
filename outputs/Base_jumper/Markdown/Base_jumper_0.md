[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_jumper-0
    Discount :                  0.999
    Environment :               jumper
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


      9795389567 function calls (9594557003 primitive calls) in 86116.94 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86116.939 86116.939 {built-in method builtins.exec}
                      1    0.010    0.010 86116.939 86116.939 <string>:1(<module>)
                      1  501.198  501.198 86116.928 86116.928 main.py:11(main)
                2953405  106.314    0.000 57623.131    0.020 agent.py:46(learn)
                2953305  423.250    0.000 55961.395    0.019 agent.py:54(TD_learn)
                2953305  191.618    0.000 30688.094    0.010 memory.py:27(sample_distribution)
                2953305  314.312    0.000 29723.705    0.010 helpers.py:12(stack)
        215593065/14766625  937.664    0.000 16755.229    0.001 module.py:710(_call_impl)
               11813320  249.489    0.000 16417.971    0.001 agent.py:117(forward)
               26580093 15877.445    0.001 15877.495    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               26580045 13139.158    0.000 13139.158    0.000 {built-in method cat}
                2953405   83.899    0.000 12072.333    0.004 environments.py:73(step)
               35439960  260.990    0.000 9044.111    0.000 container.py:115(forward)
                2953405    9.091    0.000 8706.033    0.003 agent.py:32(rememberMulti)
                2953405  372.374    0.000 8696.942    0.003 agent.py:33(<listcomp>)
              410977877 8504.363    0.000 8504.363    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2953405   47.467    0.000 6986.257    0.002 agent.py:41(chooseMulti)
                2953405   60.715    0.000 6618.168    0.002 environments.py:75(<listcomp>)
               59418429 1657.215    0.000 6600.171    0.000 helpers.py:8(clean)
                2953305   19.531    0.000 5783.796    0.002 grad_mode.py:12(decorate_context)
                2953305 1365.015    0.000 5742.092    0.002 adam.py:51(step)
               68278344 5699.682    0.000 5699.682    0.000 {built-in method as_tensor}
               59066600  102.685    0.000 5260.441    0.000 conv.py:418(forward)
               59066600  115.835    0.000 5113.389    0.000 conv.py:410(_conv_forward)
                2953405   66.685    0.000 5103.028    0.002 environments.py:74(<listcomp>)
               59068100  243.972    0.000 5036.343    0.000 interop.py:274(step)
               59066600 4977.859    0.000 4977.859    0.000 {built-in method conv2d}
                2953305   21.802    0.000 4948.373    0.002 tensor.py:155(backward)
                2953305   21.785    0.000 4926.571    0.002 __init__.py:57(backward)
                2953305 4817.110    0.002 4817.110    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11813326  560.705    0.000 3675.444    0.000 rnn.py:109(flatten_parameters)
               59068100   27.280    0.000 3014.980    0.000 wrapper.py:25(act)
               59068100   99.373    0.000 2987.701    0.000 env.py:197(act)
               59068100 2824.313    0.000 2829.907    0.000 libenv.py:352(act)
               11813320  125.642    0.000 2820.498    0.000 rnn.py:550(forward)
               11813320 2533.399    0.000 2533.399    0.000 {built-in method lstm}
               11813323 2449.681    0.000 2449.681    0.000 {built-in method _cudnn_rnn_flatten_weight}
                2953405  127.072    0.000 2103.232    0.001 agent.py:44(<listcomp>)
               59068100  208.137    0.000 1631.717    0.000 exploration.py:31(epsilonGreedy)
                  29534    5.633    0.000 1555.422    0.053 agent.py:81(update_target_network)
               70879920   68.886    0.000 1436.645    0.000 activation.py:653(forward)
               70879920  108.706    0.000 1367.759    0.000 functional.py:1277(leaky_relu)
                  29534  394.036    0.013 1291.679    0.044 memory.py:37(update_distribution)
               70879920 1249.574    0.000 1249.574    0.000 {built-in method torch._C._nn.leaky_relu}
               94505760 1138.848    0.000 1138.848    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              118486529  105.057    0.000 1065.203    0.000 extract_dict_ob.py:9(observe)
               62080274 1014.789    0.000 1014.789    0.000 {built-in method numpy.array}
               94505760  998.192    0.000  998.192    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              118486529   53.505    0.000  960.145    0.000 wrapper.py:19(observe)
              118486529  242.974    0.000  906.640    0.000 libenv.py:344(observe)
               11813320   35.206    0.000  823.158    0.000 linear.py:90(forward)
               11813320   64.140    0.000  775.610    0.000 functional.py:1655(linear)
              425043784  675.324    0.000  675.324    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              177554629  200.812    0.000  647.787    0.000 libenv.py:281(_maybe_copy_dict)
               47252880  641.516    0.000  641.516    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              532693421  577.971    0.000  577.971    0.000 {method 'copy' of 'numpy.ndarray' objects}
                2953305   86.536    0.000  569.436    0.000 optimizer.py:166(zero_grad)
               47252880  528.373    0.000  528.373    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               47254155  488.495    0.000  525.991    0.000 module.py:774(__setattr__)
               11813320  524.306    0.000  524.306    0.000 {built-in method addmm}
               59068100   55.225    0.000  498.571    0.000 wrapper.py:22(get_info)
               47252880  459.980    0.000  459.980    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47252880  454.364    0.000  454.364    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2953305  335.155    0.000  447.066    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               59068100  232.032    0.000  443.346    0.000 libenv.py:363(get_info)
               59068100  426.696    0.000  426.696    0.000 memory.py:15(inner)
               11813320   25.547    0.000  400.702    0.000 pooling.py:156(forward)
               11813320   19.675    0.000  375.155    0.000 _jit_internal.py:237(fn)
               11813320   22.094    0.000  353.611    0.000 functional.py:564(_max_pool2d)
               47252880  349.971    0.000  349.971    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               59068100  344.443    0.000  344.443    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               11813320  330.112    0.000  330.112    0.000 {built-in method max_pool2d}
                8860215   13.024    0.000  291.312    0.000 functional.py:68(split)
                8860215   15.659    0.000  277.199    0.000 tensor.py:367(split)
               47253292  241.440    0.000  273.109    0.000 __init__.py:66(is_acceptable)
                2953405   34.440    0.000  267.238    0.000 environments.py:76(<listcomp>)
                8860215  259.930    0.000  259.930    0.000 {function Tensor.split at 0x7f0fa196a940}
               59068120   40.262    0.000  232.814    0.000 environments.py:79(reset)
                2953106  215.668    0.000  215.668    0.000 memory.py:35(<listcomp>)
                2953305    7.503    0.000  210.580    0.000 loss.py:444(forward)
              236973058   62.866    0.000  205.035    0.000 libenv.py:271(_maybe_copy_ndarray)
                2953405   19.180    0.000  204.175    0.000 collector.py:7(collect)
                2953305   28.464    0.000  203.077    0.000 functional.py:2621(mse_loss)
               29533250  197.880    0.000  197.880    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              236264448  164.253    0.000  189.006    0.000 tensor.py:725(grad)
                5906811  183.745    0.000  183.746    0.000 {built-in method builtins.sum}
              215593065  164.147    0.000  164.147    0.000 {built-in method torch._C._get_tracing_state}
                5906610  161.721    0.000  161.721    0.000 {built-in method gather}
              201889983  158.317    0.000  158.898    0.000 module.py:758(__getattr__)
                  59068   15.603    0.000  149.798    0.003 {built-in method _pickle.loads}
                2953305  119.462    0.000  119.462    0.000 {built-in method torch._C._nn.mse_loss}
               11813320  116.829    0.000  116.829    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7951091   11.886    0.000  112.328    0.000 <__array_function__ internals>:2(prod)
                  59068   26.143    0.000  108.312    0.002 {built-in method _pickle.dumps}
               11813320   32.337    0.000  107.292    0.000 rnn.py:524(check_forward_args)
                1063222    1.263    0.000  100.775    0.000 storage.py:141(_load_from_bytes)
               59418469   49.556    0.000  100.377    0.000 types.py:163(multimap)
                1063222    5.197    0.000   99.512    0.000 serialization.py:486(load)
                7951131    8.451    0.000   98.554    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7951091   15.070    0.000   90.102    0.000 fromnumeric.py:2881(prod)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8371233: <Base_jumper_0> in cluster <dcc> Done

Job <Base_jumper_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:31 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov 19 07:32:05 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov 19 07:32:05 2020
Terminated at Fri Nov 20 07:27:28 2020
Results reported at Fri Nov 20 07:27:28 2020

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

    CPU time :                                   88186.00 sec.
    Max Memory :                                 25258 MB
    Average Memory :                             24959.93 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5462.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86125 sec.
    Turnaround time :                            207057 sec.

The output (if any) is above this job summary.

