Traceback (most recent call last):
  File "main.py", line 107, in <module>
    serverRun()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 31, in serverRun
    showParams(params)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 101, in showParams
    timer = Timer()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 68, in __init__
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
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 83, in chooseMulti
    vals = self.convert_values(vals, uncertainties, avoid_trace)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 137, in convert_values
    return vals + (self.uncertainty_weight * uncertainties * self.uncertainty) + (self.state_difference_weight * state_differences * self.state_difference)
TypeError: only integer tensors of a single element can be converted to an index

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8466077: <Final_stateUncertainty0.25and0bigfish_0> in cluster <dcc> Exited

Job <Final_stateUncertainty0.25and0bigfish_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Wed Dec  2 12:09:14 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec  3 13:32:34 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 13:32:34 2020
Terminated at Thu Dec  3 13:33:15 2020
Results reported at Thu Dec  3 13:33:15 2020

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

    CPU time :                                   11.00 sec.
    Max Memory :                                 679 MB
    Average Memory :                             679.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               60761.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42 sec.
    Turnaround time :                            91441 sec.

The output (if any) is above this job summary.


    Name :                      Final_stateUncertainty0.25and0bigfish-0
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
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0.25
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13821020316 function calls (13593085464 primitive calls) in 82513.17 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82513.170 82513.170 {built-in method builtins.exec}
                      1    0.030    0.030 82513.170 82513.170 <string>:1(<module>)
                      1  502.923  502.923 82513.139 82513.139 main.py:92(main)
                2257032  190.380    0.000 57111.825    0.025 agent.py:86(learn)
                2256532  850.534    0.000 56022.901    0.025 agent.py:96(TD_learn)
                2256532  161.715    0.000 25316.622    0.011 memory.py:35(sample_distribution)
                2256532  308.194    0.000 24553.176    0.011 helpers.py:15(stack)
        243724956/15796724 1116.388    0.000 16480.019    0.001 module.py:715(_call_impl)
                6770096  223.889    0.000 15220.261    0.002 agent.py:212(forward)
               22567428 12279.856    0.001 12279.857    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20310288 11601.690    0.001 11601.690    0.001 {built-in method cat}
               36107512  299.980    0.000 10681.853    0.000 container.py:115(forward)
                6769596   45.091    0.000 9621.402    0.001 grad_mode.py:23(decorate_context)
                6769596  282.475    0.000 9502.380    0.001 adam.py:55(step)
                2257032   62.413    0.000 8706.378    0.004 environments.py:83(step)
                2257032  212.773    0.000 8606.944    0.004 agent.py:74(chooseMulti)
                6769596 1760.028    0.000 8159.144    0.001 functional.py:53(adam)
                2257032   95.912    0.000 7409.488    0.003 agent.py:62(rememberMulti)
                2257032  298.469    0.000 6941.728    0.003 agent.py:66(<listcomp>)
              304768609 6745.129    0.000 6745.129    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6769596   51.217    0.000 6440.575    0.001 tensor.py:181(backward)
                6769596   32.961    0.000 6389.358    0.001 __init__.py:68(backward)
                6769596 6173.878    0.001 6173.878    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2257032   69.664    0.000 5733.356    0.003 environments.py:85(<listcomp>)
               45299093 1325.642    0.000 5685.713    0.000 helpers.py:8(clean)
               52068689 4934.961    0.000 4934.961    0.000 {built-in method as_tensor}
               40620576   71.139    0.000 3860.350    0.000 conv.py:422(forward)
               40620576   84.814    0.000 3755.094    0.000 conv.py:414(_conv_forward)
               40620576 3655.780    0.000 3655.780    0.000 {built-in method conv2d}
               54161768  116.183    0.000 3396.083    0.000 linear.py:92(forward)
               54161768  320.677    0.000 3223.397    0.000 functional.py:1669(linear)
                2257032   47.938    0.000 2728.221    0.001 environments.py:84(<listcomp>)
               45140640  176.230    0.000 2680.283    0.000 interop.py:274(step)
                6770102  416.404    0.000 2532.155    0.000 rnn.py:110(flatten_parameters)
              473871828 1253.074    0.000 1975.673    0.000 tensor.py:933(grad)
               47390672 1913.292    0.000 1913.292    0.000 {built-in method addmm}
                6769596  188.143    0.000 1906.671    0.000 optimizer.py:167(zero_grad)
                2257032  104.369    0.000 1887.299    0.001 agent.py:84(<listcomp>)
                6770096   80.560    0.000 1819.013    0.000 rnn.py:555(forward)
               85755216   79.152    0.000 1789.361    0.000 activation.py:713(forward)
              135391920 1732.422    0.000 1732.422    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               85755216  114.283    0.000 1710.208    0.000 functional.py:1292(leaky_relu)
                6770096 1643.441    0.000 1643.441    0.000 {built-in method lstm}
                6770099 1635.366    0.000 1635.366    0.000 {built-in method _cudnn_rnn_flatten_weight}
               85755216 1584.703    0.000 1584.703    0.000 {built-in method torch._C._nn.leaky_relu}
               45140640  150.084    0.000 1481.872    0.000 exploration.py:34(epsilonGreedy)
              135391920 1445.607    0.000 1445.607    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               45140640   20.186    0.000 1195.542    0.000 wrapper.py:25(act)
               45140640   67.530    0.000 1175.357    0.000 env.py:197(act)
               45140640 1063.545    0.000 1068.066    0.000 libenv.py:352(act)
              595729802  336.482    0.000  922.246    0.000 overrides.py:1073(has_torch_function)
               67695960  902.505    0.000  902.505    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   4514    1.678    0.000  898.544    0.199 agent.py:139(update_target_network)
               67695960  829.444    0.000  829.444    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               90439733   71.885    0.000  796.476    0.000 extract_dict_ob.py:9(observe)
               67695960  771.451    0.000  771.451    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               90439733   37.238    0.000  724.591    0.000 wrapper.py:19(observe)
               67695960  691.247    0.000  691.247    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               90439733  179.664    0.000  687.353    0.000 libenv.py:344(observe)
                2257032    6.582    0.000  649.659    0.000 agent.py:230(avoid_similar_state)
                   4514  159.835    0.035  568.678    0.126 memory.py:45(update_distribution)
              663430786  232.007    0.000  561.505    0.000 {built-in method builtins.any}
               67695960  525.349    0.000  525.349    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               54161768  516.696    0.000  516.696    0.000 {method 't' of 'torch._C._TensorBase' objects}
              338301224  498.285    0.000  498.285    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              135580373  149.767    0.000  497.943    0.000 libenv.py:281(_maybe_copy_dict)
               47406200  490.504    0.000  490.504    0.000 {built-in method numpy.array}
                6769596   13.729    0.000  460.140    0.000 loss.py:445(forward)
                6769596   46.664    0.000  446.411    0.000 functional.py:2637(mse_loss)
              406745633  435.671    0.000  435.671    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11283584  157.082    0.000  402.539    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6771096   13.329    0.000  388.874    0.000 functional.py:74(split)
                6771096   30.896    0.000  374.570    0.000 tensor.py:460(split)
               31595283  348.662    0.000  373.074    0.000 module.py:781(__setattr__)
               45140640   41.381    0.000  363.788    0.000 wrapper.py:22(get_info)
                6771096  342.247    0.000  342.247    0.000 {function Tensor.split at 0x7f225fb97d30}
               45140640  336.955    0.000  336.955    0.000 memory.py:17(inner)
                2256532  249.783    0.000  325.451    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
             1245621372  258.005    0.000  324.340    0.000 overrides.py:1086(<genexpr>)
               45140640  168.510    0.000  322.408    0.000 libenv.py:363(get_info)
               45140640  301.058    0.000  301.058    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2257032  281.265    0.000  288.562    0.000 agent.py:131(convert_values)
               24823840   24.880    0.000  287.440    0.000 <__array_function__ internals>:2(prod)
                6769596  283.718    0.000  283.718    0.000 {built-in method torch._C._nn.mse_loss}
               40619576  278.946    0.000  278.946    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   9028  225.646    0.025  277.322    0.031 {built-in method _pickle.loads}
                9026128  268.239    0.000  268.239    0.000 {built-in method gather}
                6770096   16.761    0.000  258.565    0.000 pooling.py:152(forward)
               24823880   19.110    0.000  258.196    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6770096   12.088    0.000  241.804    0.000 _jit_internal.py:257(fn)
               24823840   31.791    0.000  239.086    0.000 fromnumeric.py:2881(prod)
                6771096  238.796    0.000  238.796    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6770096   13.850    0.000  228.591    0.000 functional.py:574(_max_pool2d)
                6770096  213.852    0.000  213.852    0.000 {built-in method max_pool2d}
               24823840   56.539    0.000  207.295    0.000 fromnumeric.py:70(_wrapreduction)
                2600094  195.493    0.000  195.493    0.000 {built-in method tensor}
               67696206   88.747    0.000  191.764    0.000 tensor.py:596(__hash__)
                2256532  187.184    0.000  187.184    0.000 memory.py:43(<listcomp>)
               27080396  165.397    0.000  186.116    0.000 __init__.py:67(is_acceptable)
                2257032   29.701    0.000  182.388    0.000 environments.py:86(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8468282: <Final_stateUncertainty0.25and0bigfish_0> in cluster <dcc> Done

Job <Final_stateUncertainty0.25and0bigfish_0> was submitted from host <n-62-27-20> by user <s183914> in cluster <dcc> at Thu Dec  3 15:35:43 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec  3 15:36:50 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 15:36:50 2020
Terminated at Fri Dec  4 14:32:10 2020
Results reported at Fri Dec  4 14:32:10 2020

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

    CPU time :                                   84532.00 sec.
    Max Memory :                                 54610 MB
    Average Memory :                             53909.58 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6830.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82521 sec.
    Turnaround time :                            82587 sec.

The output (if any) is above this job summary.

