[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NoDist-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    200000
    Update every :              100
    Use distribution :          0.0
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      12111400657 function calls (11923809785 primitive calls) in 86138.54 seconds

##    Ordered by: cumulative time
   List reduced from 1314 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86138.543 86138.543 {built-in method builtins.exec}
                      1    0.037    0.037 86138.543 86138.543 <string>:1(<module>)
                      1  470.572  470.572 86138.504 86138.504 main.py:9(main)
                2758674  100.450    0.000 62523.537    0.023 agent.py:46(learn)
                2758574  331.292    0.000 60788.181    0.022 agent.py:54(TD_learn)
                2758574 9627.712    0.003 41242.886    0.015 memory.py:23(sample)
                2758574  368.074    0.000 30666.637    0.011 helpers.py:12(stack)
               24827514 15758.608    0.001 15758.650    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               24827466 14082.415    0.001 14082.415    0.001 {built-in method cat}
        201377702/13792970  907.287    0.000 13887.807    0.001 module.py:710(_call_impl)
               11034396  221.426    0.000 13594.861    0.001 agent.py:117(forward)
                2758674   78.028    0.000 10017.078    0.004 environments.py:73(step)
               33103188  215.848    0.000 7432.517    0.000 container.py:115(forward)
              385715068 7262.860    0.000 7262.860    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2758674    8.514    0.000 7153.632    0.003 agent.py:32(rememberMulti)
                2758674  242.584    0.000 7145.117    0.003 agent.py:33(<listcomp>)
                2758674   56.188    0.000 5872.579    0.002 environments.py:75(<listcomp>)
               55324939 1629.186    0.000 5834.234    0.000 helpers.py:8(clean)
                2758674   40.634    0.000 5731.201    0.002 agent.py:41(chooseMulti)
               63600661 4974.660    0.000 4974.660    0.000 {built-in method as_tensor}
               55171980   94.011    0.000 4298.597    0.000 conv.py:418(forward)
               55171980  117.341    0.000 4162.127    0.000 conv.py:410(_conv_forward)
               55171980 4025.019    0.000 4025.019    0.000 {built-in method conv2d}
                2758674   60.443    0.000 3865.673    0.001 environments.py:74(<listcomp>)
                2758574   15.995    0.000 3838.110    0.001 grad_mode.py:12(decorate_context)
               55173480  207.989    0.000 3805.230    0.000 interop.py:274(step)
                2758574  968.285    0.000 3801.896    0.001 adam.py:51(step)
                2758574   14.581    0.000 3747.843    0.001 tensor.py:155(backward)
                2758574   19.891    0.000 3733.262    0.001 __init__.py:57(backward)
                2758574 3642.415    0.001 3642.415    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11034402  510.576    0.000 2822.379    0.000 rnn.py:109(flatten_parameters)
               11034396  117.910    0.000 2540.871    0.000 rnn.py:550(forward)
               11034396 2270.827    0.000 2270.827    0.000 {built-in method lstm}
               55173480   26.921    0.000 2039.350    0.000 wrapper.py:25(act)
               55173480   78.281    0.000 2012.429    0.000 env.py:197(act)
               55173480 1886.770    0.000 1893.113    0.000 libenv.py:352(act)
               11034399 1713.792    0.000 1713.792    0.000 {built-in method _cudnn_rnn_flatten_weight}
                2758674   98.426    0.000 1677.679    0.001 agent.py:44(<listcomp>)
                  27586    5.556    0.000 1634.906    0.059 agent.py:81(update_target_network)
                  27586  382.558    0.014 1392.472    0.050 memory.py:37(update_distribution)
               55173480  159.095    0.000 1343.856    0.000 exploration.py:31(epsilonGreedy)
               55228652 1099.418    0.000 1099.418    0.000 {built-in method numpy.array}
               66206376   60.510    0.000 1094.392    0.000 activation.py:653(forward)
               66206376  102.345    0.000 1033.883    0.000 functional.py:1277(leaky_relu)
              110498419   84.339    0.000  940.992    0.000 extract_dict_ob.py:9(observe)
                2758574  384.433    0.000  934.807    0.000 random.py:315(sample)
               66206376  921.897    0.000  921.897    0.000 {built-in method torch._C._nn.leaky_relu}
              110498419   47.847    0.000  856.653    0.000 wrapper.py:19(observe)
              110498419  214.228    0.000  808.805    0.000 libenv.py:344(observe)
               88274368  694.661    0.000  694.661    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11034396   29.498    0.000  680.622    0.000 linear.py:90(forward)
               11034396   63.354    0.000  638.491    0.000 functional.py:1655(linear)
               88274368  618.621    0.000  618.621    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              165671899  177.383    0.000  587.290    0.000 libenv.py:281(_maybe_copy_dict)
              497043283  507.491    0.000  507.491    0.000 {method 'copy' of 'numpy.ndarray' objects}
               44138459  455.217    0.000  489.287    0.000 module.py:774(__setattr__)
              706651738  293.486    0.000  443.314    0.000 random.py:250(_randbelow_with_getrandbits)
               55173480   55.912    0.000  439.198    0.000 wrapper.py:22(get_info)
               44137184  431.440    0.000  431.440    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11034396  420.606    0.000  420.606    0.000 {built-in method addmm}
              399205060  411.725    0.000  411.725    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               55173480  201.469    0.000  383.286    0.000 libenv.py:363(get_info)
               44137184  361.074    0.000  361.074    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2758574   66.418    0.000  356.842    0.000 optimizer.py:166(zero_grad)
               55173480  345.945    0.000  345.945    0.000 memory.py:15(inner)
               11034396   26.592    0.000  331.576    0.000 pooling.py:156(forward)
               11034396   19.728    0.000  304.984    0.000 _jit_internal.py:237(fn)
               44137184  301.163    0.000  301.163    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               44137184  291.656    0.000  291.656    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11034396   21.781    0.000  283.301    0.000 functional.py:564(_max_pool2d)
               11034396  259.909    0.000  259.909    0.000 {built-in method max_pool2d}
                8276022   13.330    0.000  258.081    0.000 functional.py:68(split)
                8276022   13.653    0.000  243.680    0.000 tensor.py:367(split)
               44137596  205.637    0.000  237.561    0.000 __init__.py:66(is_acceptable)
               55173480  235.397    0.000  235.397    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8276022  228.647    0.000  228.647    0.000 {function Tensor.split at 0x7f568202a940}
                2758674   31.530    0.000  200.798    0.000 environments.py:76(<listcomp>)
                2758674   19.411    0.000  198.076    0.000 collector.py:7(collect)
               44137184  196.211    0.000  196.211    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5517349  177.309    0.000  177.309    0.000 {built-in method builtins.sum}
                2758574    6.202    0.000  175.227    0.000 loss.py:444(forward)
              220996838   61.530    0.000  170.908    0.000 libenv.py:271(_maybe_copy_ndarray)
               55173500   36.252    0.000  169.340    0.000 environments.py:79(reset)
                2758574   25.917    0.000  169.025    0.000 functional.py:2621(mse_loss)
              220685968  134.951    0.000  156.187    0.000 tensor.py:725(grad)
              188578147  154.690    0.000  155.244    0.000 module.py:758(__getattr__)
               27585940  151.090    0.000  151.090    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                  55172   14.569    0.000  135.022    0.002 {built-in method _pickle.loads}
              201377702  129.230    0.000  129.230    0.000 {built-in method torch._C._get_tracing_state}
                5517148  129.067    0.000  129.067    0.000 {built-in method gather}
              926619012  106.125    0.000  106.125    0.000 {method 'getrandbits' of '_random.Random' objects}
               11034396   37.028    0.000  102.671    0.000 rnn.py:524(check_forward_args)
                  55172   24.722    0.000  101.856    0.002 {built-in method _pickle.dumps}
                2758574   93.687    0.000   93.687    0.000 {built-in method torch._C._nn.mse_loss}
                 993094    1.123    0.000   93.277    0.000 storage.py:141(_load_from_bytes)
                 993094    4.955    0.000   92.154    0.000 serialization.py:486(load)
               11034396   88.189    0.000   88.189    0.000 {method 't' of 'torch._C._TensorBase' objects}
              368594134   74.538    0.000   87.388    0.000 {built-in method builtins.isinstance}
              838613996   87.047    0.000   87.047    0.000 {method 'values' of 'collections.OrderedDict' objects}
               55324979   41.617    0.000   83.953    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8366040: <NoDist_0> in cluster <dcc> Done

Job <NoDist_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Nov 16 19:52:14 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov 16 19:52:15 2020
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

    CPU time :                                   87801.00 sec.
    Max Memory :                                 25347 MB
    Average Memory :                             25074.98 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5373.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86195 sec.
    Turnaround time :                            86160 sec.

The output (if any) is above this job summary.

