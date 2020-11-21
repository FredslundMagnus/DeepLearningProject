[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_maze-0
    Discount :                  0.999
    Environment :               maze
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


      10980154124 function calls (10754842852 primitive calls) in 86116.45 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86116.450 86116.450 {built-in method builtins.exec}
                      1    0.030    0.030 86116.450 86116.450 <string>:1(<module>)
                      1  543.083  543.083 86116.418 86116.418 main.py:11(main)
                3313386  114.210    0.000 59331.711    0.018 agent.py:46(learn)
                3313286  392.396    0.000 57455.384    0.017 agent.py:54(TD_learn)
                3313286  211.055    0.000 34429.240    0.010 memory.py:27(sample_distribution)
                3313286  311.037    0.000 33385.770    0.010 helpers.py:12(stack)
               29819922 17893.482    0.001 17893.493    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        241871678/16566530 1025.678    0.000 16252.510    0.001 module.py:710(_call_impl)
               13253244  262.917    0.000 15910.769    0.001 agent.py:117(forward)
               29819874 14788.131    0.000 14788.131    0.000 {built-in method cat}
                3313386   87.844    0.000 11035.929    0.003 environments.py:73(step)
               39759732  252.033    0.000 8738.583    0.000 container.py:115(forward)
              461375298 8340.829    0.000 8340.829    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3313386    9.382    0.000 7897.985    0.002 agent.py:32(rememberMulti)
                3313386  276.852    0.000 7888.604    0.002 agent.py:33(<listcomp>)
                3313386   51.121    0.000 7065.014    0.002 agent.py:41(chooseMulti)
                3313386   63.962    0.000 6661.080    0.002 environments.py:75(<listcomp>)
               66431347 1809.451    0.000 6615.885    0.000 helpers.py:8(clean)
               76371205 5557.689    0.000 5557.689    0.000 {built-in method as_tensor}
               66266220  108.367    0.000 5084.925    0.000 conv.py:418(forward)
               66266220  126.080    0.000 4926.795    0.000 conv.py:410(_conv_forward)
               66266220 4777.642    0.000 4777.642    0.000 {built-in method conv2d}
                3313286   21.438    0.000 4564.873    0.001 grad_mode.py:12(decorate_context)
                3313286 1156.267    0.000 4520.719    0.001 adam.py:51(step)
                3313286   18.324    0.000 4460.522    0.001 tensor.py:155(backward)
                3313286   21.430    0.000 4442.198    0.001 __init__.py:57(backward)
                3313286 4338.626    0.001 4338.626    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3313386   66.962    0.000 4066.406    0.001 environments.py:74(<listcomp>)
               66267720  233.574    0.000 3999.443    0.000 interop.py:274(step)
               13253250  579.853    0.000 3288.939    0.000 rnn.py:109(flatten_parameters)
               13253244  140.851    0.000 2966.093    0.000 rnn.py:550(forward)
               13253244 2658.686    0.000 2658.686    0.000 {built-in method lstm}
                3313386  120.524    0.000 2325.605    0.001 agent.py:44(<listcomp>)
               66267720   30.858    0.000 2030.611    0.000 wrapper.py:25(act)
               13253247 2027.804    0.000 2027.804    0.000 {built-in method _cudnn_rnn_flatten_weight}
               66267720   82.936    0.000 1999.753    0.000 env.py:197(act)
               66267720  178.854    0.000 1927.446    0.000 exploration.py:31(epsilonGreedy)
               66267720 1865.827    0.000 1872.235    0.000 libenv.py:352(act)
                  33133    6.189    0.000 1762.117    0.053 agent.py:81(update_target_network)
                  33133  450.781    0.014 1481.235    0.045 memory.py:37(update_distribution)
               79519464   71.394    0.000 1289.947    0.000 activation.py:653(forward)
               79519464  120.421    0.000 1218.553    0.000 functional.py:1277(leaky_relu)
               69647073 1132.513    0.000 1132.513    0.000 {built-in method numpy.array}
               79519464 1087.231    0.000 1087.231    0.000 {built-in method torch._C._nn.leaky_relu}
              132699067   92.285    0.000 1042.538    0.000 extract_dict_ob.py:9(observe)
              132699067   54.368    0.000  950.253    0.000 wrapper.py:19(observe)
              132699067  241.623    0.000  895.885    0.000 libenv.py:344(observe)
              106025152  832.834    0.000  832.834    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13253244   38.317    0.000  803.876    0.000 linear.py:90(forward)
               13253244   71.206    0.000  752.387    0.000 functional.py:1655(linear)
              106025152  740.251    0.000  740.251    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              198966787  202.406    0.000  652.955    0.000 libenv.py:281(_maybe_copy_dict)
               53013851  533.048    0.000  569.721    0.000 module.py:774(__setattr__)
              596933494  563.272    0.000  563.272    0.000 {method 'copy' of 'numpy.ndarray' objects}
               53012576  512.593    0.000  512.593    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               13253244  499.426    0.000  499.426    0.000 {built-in method addmm}
               66267720   53.026    0.000  494.956    0.000 wrapper.py:22(get_info)
              477614514  480.806    0.000  480.806    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                3313286  357.332    0.000  473.073    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               66267720  231.572    0.000  441.930    0.000 libenv.py:363(get_info)
               53012576  424.121    0.000  424.121    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3313286   72.323    0.000  420.433    0.000 optimizer.py:166(zero_grad)
               66267720  418.619    0.000  418.619    0.000 memory.py:15(inner)
               13253244   30.705    0.000  384.579    0.000 pooling.py:156(forward)
               53012576  354.360    0.000  354.360    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               13253244   20.565    0.000  353.874    0.000 _jit_internal.py:237(fn)
               53012576  340.732    0.000  340.732    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13253244   23.180    0.000  331.111    0.000 functional.py:564(_max_pool2d)
               13253244  306.202    0.000  306.202    0.000 {built-in method max_pool2d}
                9940158   14.504    0.000  300.160    0.000 functional.py:68(split)
                9940158   15.383    0.000  284.440    0.000 tensor.py:367(split)
               66267720  277.635    0.000  277.635    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               53012988  234.009    0.000  268.544    0.000 __init__.py:66(is_acceptable)
                9940158  267.431    0.000  267.431    0.000 {function Tensor.split at 0x7fcb257b1940}
                3313087  245.226    0.000  245.226    0.000 memory.py:35(<listcomp>)
               53012576  236.011    0.000  236.011    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3313386   36.061    0.000  220.599    0.000 environments.py:76(<listcomp>)
                3313386   21.275    0.000  219.026    0.000 collector.py:7(collect)
                3313286    8.299    0.000  207.365    0.000 loss.py:444(forward)
                3313286   30.075    0.000  199.066    0.000 functional.py:2621(mse_loss)
                6626773  196.147    0.000  196.147    0.000 {built-in method builtins.sum}
              265398134   67.093    0.000  191.170    0.000 libenv.py:271(_maybe_copy_ndarray)
               66267740   36.757    0.000  184.594    0.000 environments.py:79(reset)
              265062928  158.291    0.000  183.477    0.000 tensor.py:725(grad)
               33133060  180.593    0.000  180.593    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              226498255  173.407    0.000  174.077    0.000 module.py:758(__getattr__)
                  66266   17.026    0.000  156.826    0.002 {built-in method _pickle.loads}
                6626572  149.167    0.000  149.167    0.000 {built-in method gather}
              241871678  145.046    0.000  145.046    0.000 {built-in method torch._C._get_tracing_state}
                  66266   29.177    0.000  117.867    0.002 {built-in method _pickle.dumps}
               13253244   36.167    0.000  111.412    0.000 rnn.py:524(check_forward_args)
                3313286  110.778    0.000  110.778    0.000 {built-in method torch._C._nn.mse_loss}
                8310910   11.228    0.000  110.235    0.000 <__array_function__ internals>:2(prod)
                1192786    1.315    0.000  108.029    0.000 storage.py:141(_load_from_bytes)
                1192786    5.723    0.000  106.714    0.000 serialization.py:486(load)
               13253244  103.907    0.000  103.907    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1007246444   99.706    0.000   99.706    0.000 {method 'values' of 'collections.OrderedDict' objects}
                8310950    8.739    0.000   97.325    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               66431387   47.642    0.000   93.097    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8371235: <Base_maze_0> in cluster <dcc> Done

Job <Base_maze_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:31 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Nov 20 05:05:20 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 20 05:05:20 2020
Terminated at Sat Nov 21 05:00:44 2020
Results reported at Sat Nov 21 05:00:44 2020

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

    CPU time :                                   88061.00 sec.
    Max Memory :                                 25364 MB
    Average Memory :                             25037.94 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5356.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86126 sec.
    Turnaround time :                            284653 sec.

The output (if any) is above this job summary.

