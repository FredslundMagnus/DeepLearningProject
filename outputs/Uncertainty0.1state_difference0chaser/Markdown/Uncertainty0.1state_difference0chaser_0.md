[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Uncertainty0.1state_difference0chaser-0
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
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      9279298622 function calls (9065126339 primitive calls) in 82516.23 seconds

##    Ordered by: cumulative time
   List reduced from 1331 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82516.235 82516.235 {built-in method builtins.exec}
                      1    0.023    0.023 82516.235 82516.235 <string>:1(<module>)
                      1  612.721  612.721 82516.208 82516.208 main.py:92(main)
                2120769  254.497    0.000 56443.220    0.027 agent.py:86(learn)
                2120269  669.527    0.000 55141.030    0.026 agent.py:96(TD_learn)
                2120269  171.367    0.000 33232.539    0.016 memory.py:35(sample_distribution)
                2120269  314.566    0.000 32454.229    0.015 helpers.py:15(stack)
               19083921 19228.057    0.001 19228.057    0.001 {built-in method cat}
        229008552/14842883 1022.933    0.000 13742.523    0.001 module.py:710(_call_impl)
                6361307  203.191    0.000 12699.128    0.002 agent.py:212(forward)
               21204798 12624.926    0.001 12624.938    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2120769  178.081    0.000 10042.917    0.005 agent.py:74(chooseMulti)
              285826179 8836.178    0.000 8836.178    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               33927304  255.220    0.000 8634.652    0.000 container.py:115(forward)
                2120769   68.935    0.000 8348.506    0.004 environments.py:83(step)
                2120769   86.247    0.000 6898.134    0.003 agent.py:62(rememberMulti)
                2120769  206.623    0.000 6439.618    0.003 agent.py:66(<listcomp>)
                6360807   36.727    0.000 5858.731    0.001 grad_mode.py:12(decorate_context)
                6360807 1505.162    0.000 5778.073    0.001 adam.py:51(step)
                2120769   50.484    0.000 5091.068    0.002 environments.py:85(<listcomp>)
               42758935 1370.352    0.000 5088.735    0.000 helpers.py:8(clean)
                6360807   28.486    0.000 5027.269    0.001 tensor.py:155(backward)
                6360807   34.973    0.000 4998.784    0.001 __init__.py:57(backward)
                6360807 4821.714    0.001 4821.714    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               49119742 4321.600    0.000 4321.600    0.000 {built-in method as_tensor}
                2120769   86.557    0.000 4199.544    0.002 agent.py:84(<listcomp>)
               42415380  118.870    0.000 3893.374    0.000 exploration.py:34(epsilonGreedy)
               38167842   73.273    0.000 3224.127    0.000 conv.py:418(forward)
               38167842   82.895    0.000 3116.140    0.000 conv.py:410(_conv_forward)
               38167842 3018.085    0.000 3018.085    0.000 {built-in method conv2d}
                2120769   50.339    0.000 2938.059    0.001 environments.py:84(<listcomp>)
               42415380  167.924    0.000 2887.720    0.000 interop.py:274(step)
               50891456  110.825    0.000 2633.234    0.000 linear.py:90(forward)
               50891456  274.588    0.000 2465.344    0.000 functional.py:1655(linear)
                6361313  358.126    0.000 2025.848    0.000 rnn.py:109(flatten_parameters)
                6361307   80.802    0.000 1800.654    0.000 rnn.py:550(forward)
                6361307 1627.362    0.000 1627.362    0.000 {built-in method lstm}
               42415380   20.203    0.000 1457.910    0.000 wrapper.py:25(act)
               42415380   55.549    0.000 1437.708    0.000 env.py:197(act)
               44529149 1435.153    0.000 1435.153    0.000 {built-in method addmm}
               42415380 1348.494    0.000 1352.767    0.000 libenv.py:352(act)
               80577222   73.563    0.000 1328.235    0.000 activation.py:653(forward)
               80577222  109.485    0.000 1254.672    0.000 functional.py:1277(leaky_relu)
                6361310 1192.851    0.000 1192.851    0.000 {built-in method _cudnn_rnn_flatten_weight}
               80577222 1134.112    0.000 1134.112    0.000 {built-in method torch._C._nn.leaky_relu}
              127216140 1094.873    0.000 1094.873    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   4241    2.181    0.001 1047.693    0.247 agent.py:139(update_target_network)
              127216140  917.801    0.000  917.801    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               85174315   65.908    0.000  791.354    0.000 extract_dict_ob.py:9(observe)
               85174315   40.150    0.000  725.445    0.000 wrapper.py:19(observe)
               85174315  170.010    0.000  685.296    0.000 libenv.py:344(observe)
                   4241  163.660    0.039  677.015    0.160 memory.py:45(update_distribution)
               63608070  664.293    0.000  664.293    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               44544131  587.977    0.000  587.977    0.000 {built-in method numpy.array}
               63608070  553.737    0.000  553.737    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                6360807  102.013    0.000  552.094    0.000 optimizer.py:166(zero_grad)
              127589695  142.509    0.000  518.032    0.000 libenv.py:281(_maybe_copy_dict)
                2120769    5.517    0.000  511.179    0.000 agent.py:230(avoid_similar_state)
              382773326  451.700    0.000  451.700    0.000 {method 'copy' of 'numpy.ndarray' objects}
               42415380  447.381    0.000  447.381    0.000 memory.py:17(inner)
              316944645  444.116    0.000  444.116    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               63608070  433.546    0.000  433.546    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               63608070  416.391    0.000  416.391    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               29687601  392.622    0.000  416.051    0.000 module.py:774(__setattr__)
                6360807   14.642    0.000  396.604    0.000 loss.py:444(forward)
                6360807   54.637    0.000  381.962    0.000 functional.py:2621(mse_loss)
               11145105  142.141    0.000  370.536    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               50891456  363.455    0.000  363.455    0.000 {method 't' of 'torch._C._TensorBase' objects}
               42415380   38.951    0.000  340.637    0.000 wrapper.py:22(get_info)
                   8482  271.123    0.032  317.772    0.037 {built-in method _pickle.loads}
                2120269  240.899    0.000  315.670    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               63608070  304.867    0.000  304.867    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               42415380  153.605    0.000  301.687    0.000 libenv.py:363(get_info)
               24410619   24.469    0.000  271.122    0.000 <__array_function__ internals>:2(prod)
                6362307   12.574    0.000  252.695    0.000 functional.py:68(split)
                2120769   24.994    0.000  250.444    0.000 environments.py:86(<listcomp>)
               24410659   19.418    0.000  242.492    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6362307   13.554    0.000  239.209    0.000 tensor.py:367(split)
                2120769  202.921    0.000  237.895    0.000 agent.py:131(convert_values)
                2443083  231.487    0.000  231.487    0.000 {built-in method tensor}
               25445240  210.929    0.000  231.029    0.000 __init__.py:66(is_acceptable)
              318040458  195.416    0.000  227.127    0.000 tensor.py:725(grad)
               42415400   31.960    0.000  225.455    0.000 environments.py:89(reset)
                6362307  224.286    0.000  224.286    0.000 {function Tensor.split at 0x7faefab179d0}
               24410619   30.960    0.000  223.074    0.000 fromnumeric.py:2881(prod)
                6361307   18.789    0.000  222.936    0.000 pooling.py:156(forward)
               42415380  219.614    0.000  219.614    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6360807  212.919    0.000  212.919    0.000 {built-in method torch._C._nn.mse_loss}
               38166842  209.776    0.000  209.776    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                8481076  205.588    0.000  205.588    0.000 {built-in method gather}
                6361307   12.333    0.000  204.147    0.000 _jit_internal.py:237(fn)
               24410619   56.543    0.000  192.114    0.000 fromnumeric.py:70(_wrapreduction)
                6361307   13.969    0.000  190.711    0.000 functional.py:564(_max_pool2d)
                2120269  187.823    0.000  187.823    0.000 memory.py:43(<listcomp>)
                6362307  187.564    0.000  187.564    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6361307  175.881    0.000  175.881    0.000 {built-in method max_pool2d}
              225108422  169.241    0.000  169.425    0.000 module.py:758(__getattr__)
                2120769   14.495    0.000  149.201    0.000 collector.py:7(collect)
               26535129  143.871    0.000  143.871    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              229008552  141.802    0.000  141.802    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8483323: <Uncertainty0.1state_difference0chaser_0> in cluster <dcc> Done

Job <Uncertainty0.1state_difference0chaser_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Sat Dec  5 16:31:58 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Dec  7 06:53:49 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec  7 06:53:49 2020
Terminated at Tue Dec  8 05:49:15 2020
Results reported at Tue Dec  8 05:49:15 2020

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

    CPU time :                                   90812.00 sec.
    Max Memory :                                 54347 MB
    Average Memory :                             53655.73 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7093.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82528 sec.
    Turnaround time :                            220637 sec.

The output (if any) is above this job summary.

