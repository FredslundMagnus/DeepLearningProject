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
Subject: Job 8467080: <Fepsintosoftmax_stateUncertainty0.25and0bigfish_0> in cluster <dcc> Exited

Job <Fepsintosoftmax_stateUncertainty0.25and0bigfish_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Dec  3 01:03:41 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Dec  3 09:52:59 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 09:52:59 2020
Terminated at Thu Dec  3 09:53:40 2020
Results reported at Thu Dec  3 09:53:40 2020

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

    CPU time :                                   7.00 sec.
    Max Memory :                                 84 MB
    Average Memory :                             84.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               61356.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   41 sec.
    Turnaround time :                            31799 sec.

The output (if any) is above this job summary.

[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Fepsintosoftmax_stateUncertainty0.25and0bigfish-0
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
    Uncertainty weight :        0.25
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      10875666277 function calls (10643593663 primitive calls) in 82523.48 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82523.480 82523.480 {built-in method builtins.exec}
                      1    0.044    0.044 82523.480 82523.480 <string>:1(<module>)
                      1  425.903  425.903 82523.435 82523.435 main.py:92(main)
                2298000  174.603    0.000 50998.959    0.022 agent.py:86(learn)
                2297500  763.143    0.000 50023.560    0.022 agent.py:96(TD_learn)
                2297500  135.705    0.000 22889.098    0.010 memory.py:35(sample_distribution)
                2297500  228.214    0.000 22215.908    0.010 helpers.py:15(stack)
        248149500/16083500 1049.245    0.000 15232.201    0.001 module.py:710(_call_impl)
                2298000  207.890    0.000 14851.991    0.006 agent.py:74(chooseMulti)
                6893000  209.263    0.000 14033.763    0.002 agent.py:212(forward)
               22977108 11920.737    0.001 11920.771    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               36763000  297.248    0.000 10046.259    0.000 container.py:115(forward)
               20679000 10016.087    0.000 10016.087    0.000 {built-in method cat}
                2298000   61.038    0.000 8858.722    0.004 environments.py:83(step)
              310464780 8649.057    0.000 8649.057    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6892500   38.526    0.000 8643.973    0.001 grad_mode.py:12(decorate_context)
                6892500 2036.173    0.000 8556.862    0.001 adam.py:51(step)
                2298000  146.781    0.000 8316.543    0.004 agent.py:84(<listcomp>)
               45960000 1370.682    0.000 7779.927    0.000 exploration.py:40(epsintosoftmax)
                2298000  100.955    0.000 7192.946    0.003 agent.py:62(rememberMulti)
                2298000  302.249    0.000 6710.501    0.003 agent.py:66(<listcomp>)
                6892500   28.109    0.000 6156.635    0.001 tensor.py:155(backward)
                6892500   32.283    0.000 6128.526    0.001 __init__.py:57(backward)
                6892500 5931.823    0.001 5931.823    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2298000   65.357    0.000 5738.697    0.002 environments.py:85(<listcomp>)
               46374639 1438.704    0.000 5732.967    0.000 helpers.py:8(clean)
               53267139 4680.449    0.000 4680.449    0.000 {built-in method as_tensor}
               41358000   77.383    0.000 3635.780    0.000 conv.py:418(forward)
               41358000   78.368    0.000 3525.812    0.000 conv.py:410(_conv_forward)
               41358000 3433.154    0.000 3433.154    0.000 {built-in method conv2d}
               55145000  117.099    0.000 3131.699    0.000 linear.py:90(forward)
               55145000  325.396    0.000 2960.354    0.000 functional.py:1655(linear)
                2298000   50.041    0.000 2783.121    0.001 environments.py:84(<listcomp>)
               45960000  193.712    0.000 2733.080    0.000 interop.py:274(step)
               45960000 1728.277    0.000 2583.974    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6893006  325.465    0.000 2157.731    0.000 rnn.py:109(flatten_parameters)
               48251000 1759.576    0.000 1759.576    0.000 {built-in method addmm}
              137850000 1698.182    0.000 1698.182    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               87312000   72.591    0.000 1693.818    0.000 activation.py:653(forward)
                6893000   72.387    0.000 1639.752    0.000 rnn.py:550(forward)
               87312000  112.476    0.000 1621.227    0.000 functional.py:1277(leaky_relu)
              137850000 1509.246    0.000 1509.246    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               87312000 1498.008    0.000 1498.008    0.000 {built-in method torch._C._nn.leaky_relu}
                6893000 1479.194    0.000 1479.194    0.000 {built-in method lstm}
                6893003 1441.502    0.000 1441.502    0.000 {built-in method _cudnn_rnn_flatten_weight}
               45960000   22.571    0.000 1192.512    0.000 wrapper.py:25(act)
               45960000   74.615    0.000 1169.940    0.000 env.py:197(act)
               45960000 1048.208    0.000 1052.599    0.000 libenv.py:352(act)
               68925000  952.824    0.000  952.824    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6892500  142.195    0.000  870.839    0.000 optimizer.py:166(zero_grad)
               92334639   79.168    0.000  833.719    0.000 extract_dict_ob.py:9(observe)
                   4596    1.534    0.000  800.797    0.174 agent.py:139(update_target_network)
               68925000  787.262    0.000  787.262    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               92334639   39.667    0.000  754.551    0.000 wrapper.py:19(observe)
               34635840   68.511    0.000  743.717    0.000 functional.py:1465(softmax)
               92334639  192.746    0.000  714.884    0.000 libenv.py:344(observe)
               68925000  684.835    0.000  684.835    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               34635840  669.310    0.000  669.310    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               59581800   62.811    0.000  662.717    0.000 <__array_function__ internals>:2(prod)
               68925000  662.305    0.000  662.305    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2298000    6.444    0.000  623.391    0.000 agent.py:230(avoid_similar_state)
               59581840   49.720    0.000  587.470    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              344099543  572.580    0.000  572.580    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               59581800   75.097    0.000  537.751    0.000 fromnumeric.py:2881(prod)
               68925000  527.975    0.000  527.975    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              138294639  150.730    0.000  503.256    0.000 libenv.py:281(_maybe_copy_dict)
                   4596  139.569    0.030  483.460    0.105 memory.py:45(update_distribution)
               59581800  138.636    0.000  462.654    0.000 fromnumeric.py:70(_wrapreduction)
              414888513  448.537    0.000  448.537    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6892500   12.361    0.000  442.108    0.000 loss.py:444(forward)
               55145000  437.883    0.000  437.883    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6892500   50.910    0.000  429.747    0.000 functional.py:2621(mse_loss)
               48266692  426.704    0.000  426.704    0.000 {built-in method numpy.array}
               45960000  389.835    0.000  389.835    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               45960000   40.442    0.000  372.371    0.000 wrapper.py:22(get_info)
               45960000  174.664    0.000  331.930    0.000 libenv.py:363(get_info)
               45960000  306.053    0.000  306.053    0.000 memory.py:17(inner)
               32168835  281.438    0.000  304.451    0.000 module.py:774(__setattr__)
                2298000  275.060    0.000  304.015    0.000 agent.py:131(convert_values)
              344625108  246.607    0.000  283.272    0.000 tensor.py:725(grad)
               61883896  281.554    0.000  281.554    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                2297500  219.678    0.000  281.442    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                2298000   27.237    0.000  275.867    0.000 environments.py:86(<listcomp>)
                   9192  216.287    0.024  267.023    0.029 {built-in method _pickle.loads}
               41357000  262.140    0.000  262.140    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6894000   11.546    0.000  259.717    0.000 functional.py:68(split)
                6892500  256.002    0.000  256.002    0.000 {built-in method torch._C._nn.mse_loss}
               45960020   41.329    0.000  248.657    0.000 environments.py:89(reset)
                6894000   12.932    0.000  247.319    0.000 tensor.py:367(split)
                9190000  238.247    0.000  238.247    0.000 {built-in method gather}
                6894000  232.874    0.000  232.874    0.000 {function Tensor.split at 0x7f6908f62940}
                6893000   16.055    0.000  232.019    0.000 pooling.py:156(forward)
                2647294  216.689    0.000  216.689    0.000 {built-in method tensor}
                6894000  216.637    0.000  216.637    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6893000   11.289    0.000  215.963    0.000 _jit_internal.py:237(fn)
                6893000   11.713    0.000  203.513    0.000 functional.py:564(_max_pool2d)
                6893000  190.985    0.000  190.985    0.000 {built-in method max_pool2d}
              248149500  189.250    0.000  189.250    0.000 {built-in method torch._C._get_tracing_state}
               27572012  165.970    0.000  183.723    0.000 __init__.py:66(is_acceptable)
                2297500  170.462    0.000  170.462    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 8468488: <Fepsintosoftmax_stateUncertainty0.25and0bigfish_0> in cluster <dcc> Done

Job <Fepsintosoftmax_stateUncertainty0.25and0bigfish_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Thu Dec  3 15:58:35 2020
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Dec  4 03:16:14 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec  4 03:16:14 2020
Terminated at Sat Dec  5 02:11:49 2020
Results reported at Sat Dec  5 02:11:49 2020

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

    CPU time :                                   84700.00 sec.
    Max Memory :                                 53891 MB
    Average Memory :                             53185.31 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7549.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82534 sec.
    Turnaround time :                            123194 sec.

The output (if any) is above this job summary.

