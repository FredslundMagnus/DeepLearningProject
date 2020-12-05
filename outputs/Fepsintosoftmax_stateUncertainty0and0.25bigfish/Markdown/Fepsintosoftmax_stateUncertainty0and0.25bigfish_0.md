Traceback (most recent call last):
  File "main.py", line 107, in <module>
    serverRun()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 31, in serverRun
    showParams(params)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 101, in showParams
    timer = Timer()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 68, in __init__
    cProfile.run("main()", 'stats')
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.2/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 1, in <module>
  File "main.py", line 100, in main
    act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/agent.py", line 83, in chooseMulti
    vals = self.convert_values(vals, uncertainties, avoid_trace)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/agent.py", line 137, in convert_values
    return vals + (self.uncertainty_weight * uncertainties * self.uncertainty) + (self.state_difference_weight * state_differences * self.state_difference)
TypeError: only integer tensors of a single element can be converted to an index

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8467081: <Fepsintosoftmax_stateUncertainty0and0.25bigfish_0> in cluster <dcc> Exited

Job <Fepsintosoftmax_stateUncertainty0and0.25bigfish_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Dec  3 01:03:41 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Dec  3 09:53:41 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 09:53:41 2020
Terminated at Thu Dec  3 09:54:03 2020
Results reported at Thu Dec  3 09:54:03 2020

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

    CPU time :                                   6.00 sec.
    Max Memory :                                 1339 MB
    Average Memory :                             1339.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               60101.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   22 sec.
    Turnaround time :                            31822 sec.

The output (if any) is above this job summary.

[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Fepsintosoftmax_stateUncertainty0and0.25bigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsintosoftmax
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.25
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      8695689612 function calls (8509727942 primitive calls) in 82520.35 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82520.349 82520.349 {built-in method builtins.exec}
                      1    0.037    0.037 82520.349 82520.349 <string>:1(<module>)
                      1  597.111  597.111 82520.311 82520.311 main.py:92(main)
                1841456  220.148    0.000 55074.279    0.030 agent.py:86(learn)
                1840956  608.313    0.000 53974.821    0.029 agent.py:96(TD_learn)
                1840956  148.608    0.000 34339.936    0.019 memory.py:35(sample_distribution)
                1840956  310.720    0.000 33675.228    0.018 helpers.py:15(stack)
               16570104 21636.001    0.001 21636.001    0.001 {built-in method cat}
                1841456  156.739    0.000 13428.629    0.007 agent.py:74(chooseMulti)
        198842748/12887692  926.188    0.000 12307.509    0.001 module.py:710(_call_impl)
               18411668 11571.362    0.001 11571.367    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                5523368  181.496    0.000 11381.110    0.002 agent.py:212(forward)
              246993499 9231.185    0.000 9231.185    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1841456  110.151    0.000 8262.191    0.004 agent.py:84(<listcomp>)
               36829120  956.833    0.000 7855.696    0.000 exploration.py:40(epsintosoftmax)
               29458296  225.734    0.000 7741.766    0.000 container.py:115(forward)
                1841456   58.805    0.000 7104.577    0.004 environments.py:83(step)
                1841456   74.911    0.000 6161.685    0.003 agent.py:62(rememberMulti)
                1841456  183.815    0.000 5745.645    0.003 agent.py:66(<listcomp>)
                5522868   31.525    0.000 5137.532    0.001 grad_mode.py:12(decorate_context)
                5522868 1305.370    0.000 5067.802    0.001 adam.py:51(step)
                1841456   48.695    0.000 4543.519    0.002 environments.py:85(<listcomp>)
               37011565 1225.009    0.000 4520.488    0.000 helpers.py:8(clean)
                5522868   24.930    0.000 4468.112    0.001 tensor.py:155(backward)
                5522868   30.596    0.000 4443.182    0.001 __init__.py:57(backward)
                5522868 4287.370    0.001 4287.370    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               42534433 3737.008    0.000 3737.008    0.000 {built-in method as_tensor}
               33140208   61.358    0.000 2880.778    0.000 conv.py:418(forward)
               33140208   71.929    0.000 2786.022    0.000 conv.py:410(_conv_forward)
               33140208 2700.451    0.000 2700.451    0.000 {built-in method conv2d}
               44187944   95.000    0.000 2356.932    0.000 linear.py:90(forward)
                1841456   41.234    0.000 2325.600    0.001 environments.py:84(<listcomp>)
               36829120  148.650    0.000 2284.366    0.000 interop.py:274(step)
               44187944  241.934    0.000 2210.100    0.000 functional.py:1655(linear)
               36829120 1317.080    0.000 1984.307    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                5523374  309.541    0.000 1722.583    0.000 rnn.py:109(flatten_parameters)
                5523368   72.008    0.000 1699.864    0.000 rnn.py:550(forward)
                5523368 1546.733    0.000 1546.733    0.000 {built-in method lstm}
               38663576 1289.072    0.000 1289.072    0.000 {built-in method addmm}
               69963328   65.878    0.000 1198.837    0.000 activation.py:653(forward)
               69963328   97.467    0.000 1132.960    0.000 functional.py:1277(leaky_relu)
               69963328 1025.576    0.000 1025.576    0.000 {built-in method torch._C._nn.leaky_relu}
                5523371 1017.708    0.000 1017.708    0.000 {built-in method _cudnn_rnn_flatten_weight}
               36829120   18.559    0.000  998.300    0.000 wrapper.py:25(act)
               36829120   47.825    0.000  979.741    0.000 env.py:197(act)
              110457360  947.584    0.000  947.584    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               36829120  902.145    0.000  905.827    0.000 libenv.py:352(act)
                   3682    2.082    0.001  879.310    0.239 agent.py:139(update_target_network)
              110457360  815.784    0.000  815.784    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               73840685   56.480    0.000  709.645    0.000 extract_dict_ob.py:9(observe)
               73840685   33.027    0.000  653.165    0.000 wrapper.py:19(observe)
               73840685  150.623    0.000  620.137    0.000 libenv.py:344(observe)
               55228680  577.424    0.000  577.424    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   3682  148.457    0.040  539.766    0.147 memory.py:45(update_distribution)
               49535802   51.515    0.000  520.159    0.000 <__array_function__ internals>:2(prod)
               25963534   52.524    0.000  504.919    0.000 functional.py:1465(softmax)
                5522868   88.215    0.000  486.863    0.000 optimizer.py:166(zero_grad)
               55228680  483.028    0.000  483.028    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              110669805  122.013    0.000  474.849    0.000 libenv.py:281(_maybe_copy_dict)
               49535842   39.533    0.000  459.675    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               38677440  459.450    0.000  459.450    0.000 {built-in method numpy.array}
                1841456    4.988    0.000  450.948    0.000 agent.py:230(avoid_similar_state)
               25963534  447.750    0.000  447.750    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               36829120  420.720    0.000  420.720    0.000 memory.py:17(inner)
               49535802   61.410    0.000  420.142    0.000 fromnumeric.py:2881(prod)
              332013097  419.747    0.000  419.747    0.000 {method 'copy' of 'numpy.ndarray' objects}
               25777219  376.078    0.000  397.892    0.000 module.py:774(__setattr__)
               55228680  392.748    0.000  392.748    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               55228680  376.371    0.000  376.371    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              274244490  370.625    0.000  370.625    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               49535802  119.470    0.000  358.733    0.000 fromnumeric.py:70(_wrapreduction)
                5522868   12.168    0.000  350.877    0.000 loss.py:444(forward)
                5522868   46.804    0.000  338.709    0.000 functional.py:2621(mse_loss)
               44187944  332.457    0.000  332.457    0.000 {method 't' of 'torch._C._TensorBase' objects}
               36829120   33.746    0.000  304.477    0.000 wrapper.py:22(get_info)
               36829120  296.344    0.000  296.344    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                   7364  248.227    0.034  289.907    0.039 {built-in method _pickle.loads}
                5524368   11.000    0.000  283.204    0.000 functional.py:68(split)
                5524368   11.663    0.000  271.415    0.000 tensor.py:367(split)
               36829120  137.865    0.000  270.731    0.000 libenv.py:363(get_info)
               55228680  266.031    0.000  266.031    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5524368  258.609    0.000  258.609    0.000 {function Tensor.split at 0x7fdeebcc5940}
                1840956  187.219    0.000  237.914    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                1841456  176.452    0.000  220.681    0.000 agent.py:131(convert_values)
                2121286  217.831    0.000  217.831    0.000 {built-in method tensor}
               51380440  210.373    0.000  210.373    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              276143508  176.099    0.000  204.046    0.000 tensor.py:725(grad)
                5523368   18.576    0.000  200.965    0.000 pooling.py:156(forward)
                5522868  192.247    0.000  192.247    0.000 {built-in method torch._C._nn.mse_loss}
               33139208  190.256    0.000  190.256    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               22093484  167.280    0.000  185.998    0.000 __init__.py:66(is_acceptable)
                7363824  183.994    0.000  183.994    0.000 {built-in method gather}
                1840956  182.687    0.000  182.687    0.000 memory.py:43(<listcomp>)
                5523368   10.206    0.000  182.389    0.000 _jit_internal.py:237(fn)
                1841456   20.968    0.000  176.653    0.000 environments.py:86(<listcomp>)
                5523368   12.482    0.000  171.181    0.000 functional.py:564(_max_pool2d)
                5524368  164.318    0.000  164.318    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                5523368  157.881    0.000  157.881    0.000 {built-in method max_pool2d}
              195456524  156.012    0.000  156.177    0.000 module.py:758(__getattr__)
               36829140   30.257    0.000  155.702    0.000 environments.py:89(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8468489: <Fepsintosoftmax_stateUncertainty0and0.25bigfish_0> in cluster <dcc> Done

Job <Fepsintosoftmax_stateUncertainty0and0.25bigfish_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Thu Dec  3 15:58:38 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Dec  4 04:12:29 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec  4 04:12:29 2020
Terminated at Sat Dec  5 03:07:59 2020
Results reported at Sat Dec  5 03:07:59 2020

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

    CPU time :                                   92720.00 sec.
    Max Memory :                                 53721 MB
    Average Memory :                             53101.23 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7719.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82530 sec.
    Turnaround time :                            126561 sec.

The output (if any) is above this job summary.

