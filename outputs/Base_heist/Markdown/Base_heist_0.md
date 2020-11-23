[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_heist-0
    Discount :                  0.999
    Environment :               heist
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


      10150310981 function calls (9942055605 primitive calls) in 86117.81 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86117.810 86117.810 {built-in method builtins.exec}
                      1    0.027    0.027 86117.810 86117.810 <string>:1(<module>)
                      1  565.890  565.890 86117.782 86117.782 main.py:11(main)
                3062564  120.959    0.000 60362.116    0.020 agent.py:46(learn)
                3062464  384.210    0.000 58321.604    0.019 agent.py:54(TD_learn)
                3062464  214.982    0.000 36311.670    0.012 memory.py:27(sample_distribution)
                3062464  346.603    0.000 35289.968    0.012 helpers.py:12(stack)
               27562524 17689.412    0.001 17689.484    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               27562476 16788.597    0.001 16788.597    0.001 {built-in method cat}
        223561672/15312420  979.823    0.000 15569.643    0.001 module.py:710(_call_impl)
               12249956  252.311    0.000 15238.229    0.001 agent.py:117(forward)
                3062564   86.664    0.000 10310.437    0.003 environments.py:73(step)
               36749868  241.855    0.000 8309.383    0.000 container.py:115(forward)
                3062564    9.749    0.000 8205.348    0.003 agent.py:32(rememberMulti)
              426259866 8199.370    0.000 8199.370    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3062564  279.676    0.000 8195.600    0.003 agent.py:33(<listcomp>)
                3062564   58.707    0.000 6444.708    0.002 environments.py:75(<listcomp>)
                3062564   46.538    0.000 6439.821    0.002 agent.py:41(chooseMulti)
               61327763 1755.532    0.000 6395.124    0.000 helpers.py:8(clean)
               70515155 5462.829    0.000 5462.829    0.000 {built-in method as_tensor}
               61249780  110.248    0.000 4832.094    0.000 conv.py:418(forward)
               61249780  120.847    0.000 4675.435    0.000 conv.py:410(_conv_forward)
               61249780 4532.590    0.000 4532.590    0.000 {built-in method conv2d}
                3062464   20.570    0.000 4340.152    0.001 grad_mode.py:12(decorate_context)
                3062464 1089.484    0.000 4295.885    0.001 adam.py:51(step)
                3062464   17.267    0.000 4251.228    0.001 tensor.py:155(backward)
                3062464   22.886    0.000 4233.961    0.001 __init__.py:57(backward)
                3062464 4130.653    0.001 4130.653    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3062564   65.451    0.000 3572.967    0.001 environments.py:74(<listcomp>)
               61251280  231.137    0.000 3507.516    0.000 interop.py:274(step)
               12249962  565.407    0.000 3173.851    0.000 rnn.py:109(flatten_parameters)
               12249956  134.120    0.000 2886.337    0.000 rnn.py:550(forward)
               12249956 2590.238    0.000 2590.238    0.000 {built-in method lstm}
               12249959 1932.878    0.000 1932.878    0.000 {built-in method _cudnn_rnn_flatten_weight}
                  30625    6.807    0.000 1919.553    0.063 agent.py:81(update_target_network)
                3062564  109.268    0.000 1854.471    0.001 agent.py:44(<listcomp>)
                  30625  442.044    0.014 1646.585    0.054 memory.py:37(update_distribution)
               61251280   29.365    0.000 1559.425    0.000 wrapper.py:25(act)
               61251280   81.118    0.000 1530.060    0.000 env.py:197(act)
               61251280  169.937    0.000 1486.059    0.000 exploration.py:31(epsilonGreedy)
               61251280 1402.094    0.000 1407.951    0.000 libenv.py:352(act)
               64374795 1302.504    0.000 1302.504    0.000 {built-in method numpy.array}
               73499736   70.911    0.000 1225.882    0.000 activation.py:653(forward)
               73499736  115.975    0.000 1154.970    0.000 functional.py:1277(leaky_relu)
              122579043   93.170    0.000 1047.557    0.000 extract_dict_ob.py:9(observe)
               73499736 1028.518    0.000 1028.518    0.000 {built-in method torch._C._nn.leaky_relu}
              122579043   52.810    0.000  954.387    0.000 wrapper.py:19(observe)
              122579043  238.438    0.000  901.577    0.000 libenv.py:344(observe)
               97998848  801.188    0.000  801.188    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12249956   33.544    0.000  764.045    0.000 linear.py:90(forward)
               12249956   68.323    0.000  717.716    0.000 functional.py:1655(linear)
               97998848  700.181    0.000  700.181    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              183830323  199.493    0.000  653.803    0.000 libenv.py:281(_maybe_copy_dict)
              551521594  564.438    0.000  564.438    0.000 {method 'copy' of 'numpy.ndarray' objects}
               49000699  525.520    0.000  560.387    0.000 module.py:774(__setattr__)
              441419260  490.396    0.000  490.396    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               48999424  490.139    0.000  490.139    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               12249956  475.943    0.000  475.943    0.000 {built-in method addmm}
               61251280   54.800    0.000  475.565    0.000 wrapper.py:22(get_info)
                3062464  345.139    0.000  454.575    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               61251280  426.123    0.000  426.123    0.000 memory.py:15(inner)
               61251280  220.014    0.000  420.766    0.000 libenv.py:363(get_info)
               48999424  407.835    0.000  407.835    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3062464   71.770    0.000  402.259    0.000 optimizer.py:166(zero_grad)
               12249956   28.415    0.000  373.262    0.000 pooling.py:156(forward)
               12249956   21.028    0.000  344.847    0.000 _jit_internal.py:237(fn)
               48999424  331.678    0.000  331.678    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48999424  324.480    0.000  324.480    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               12249956   24.200    0.000  321.685    0.000 functional.py:564(_max_pool2d)
                9187692   14.446    0.000  299.599    0.000 functional.py:68(split)
               12249956  295.789    0.000  295.789    0.000 {built-in method max_pool2d}
                9187692   15.904    0.000  283.967    0.000 tensor.py:367(split)
               48999836  228.055    0.000  266.580    0.000 __init__.py:66(is_acceptable)
                9187692  266.549    0.000  266.549    0.000 {function Tensor.split at 0x7fe90f2c8940}
               61251280  259.144    0.000  259.144    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                3062265  238.618    0.000  238.618    0.000 memory.py:35(<listcomp>)
               48999424  226.470    0.000  226.470    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3062564   20.027    0.000  210.381    0.000 collector.py:7(collect)
                3062564   36.347    0.000  206.098    0.000 environments.py:76(<listcomp>)
                3062464    7.972    0.000  201.730    0.000 loss.py:444(forward)
                3062464   30.657    0.000  193.758    0.000 functional.py:2621(mse_loss)
              245158086   69.145    0.000  190.035    0.000 libenv.py:271(_maybe_copy_ndarray)
                6125129  188.909    0.000  188.909    0.000 {built-in method builtins.sum}
               30624840  171.299    0.000  171.299    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              244997168  147.389    0.000  171.135    0.000 tensor.py:725(grad)
               61251300   38.442    0.000  169.775    0.000 environments.py:79(reset)
              209352071  161.899    0.000  162.532    0.000 module.py:758(__getattr__)
                  61250   16.776    0.000  151.762    0.002 {built-in method _pickle.loads}
                6124928  143.496    0.000  143.496    0.000 {built-in method gather}
              223561672  138.806    0.000  138.806    0.000 {built-in method torch._C._get_tracing_state}
                  61250   28.484    0.000  114.399    0.002 {built-in method _pickle.dumps}
                8060792   11.774    0.000  108.901    0.000 <__array_function__ internals>:2(prod)
               12249956   35.347    0.000  107.751    0.000 rnn.py:524(check_forward_args)
                3062464  107.705    0.000  107.705    0.000 {built-in method torch._C._nn.mse_loss}
                1102498    1.224    0.000  104.391    0.000 storage.py:141(_load_from_bytes)
                1102498    5.396    0.000  103.167    0.000 serialization.py:486(load)
               12249956  100.546    0.000  100.546    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8060832    8.642    0.000   95.436    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               61327803   45.915    0.000   91.529    0.000 types.py:163(multimap)
               12249959   46.138    0.000   90.486    0.000 __init__.py:264(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 8371232: <Base_heist_0> in cluster <dcc> Done

Job <Base_heist_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:31 2020
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov 19 06:14:25 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov 19 06:14:25 2020
Terminated at Fri Nov 20 06:09:51 2020
Results reported at Fri Nov 20 06:09:51 2020

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

    CPU time :                                   88663.00 sec.
    Max Memory :                                 25372 MB
    Average Memory :                             25060.15 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5348.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86127 sec.
    Turnaround time :                            202400 sec.

The output (if any) is above this job summary.

