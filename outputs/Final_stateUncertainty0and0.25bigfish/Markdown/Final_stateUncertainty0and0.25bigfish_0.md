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
Subject: Job 8466078: <Final_stateUncertainty0and0.25bigfish_0> in cluster <dcc> Exited

Job <Final_stateUncertainty0and0.25bigfish_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Wed Dec  2 12:09:14 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec  3 13:33:17 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 13:33:17 2020
Terminated at Thu Dec  3 13:33:30 2020
Results reported at Thu Dec  3 13:33:30 2020

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
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               61436.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   14 sec.
    Turnaround time :                            91456 sec.

The output (if any) is above this job summary.


    Name :                      Final_stateUncertainty0and0.25bigfish-0
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.25
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14981297197 function calls (14734042762 primitive calls) in 82516.64 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82516.638 82516.638 {built-in method builtins.exec}
                      1    0.048    0.048 82516.638 82516.638 <string>:1(<module>)
                      1  521.902  521.902 82516.589 82516.589 main.py:92(main)
                2448315  205.012    0.000 55060.374    0.022 agent.py:86(learn)
                2447815  758.557    0.000 53870.742    0.022 agent.py:96(TD_learn)
                2447815  164.861    0.000 26795.976    0.011 memory.py:35(sample_distribution)
                2447815  250.519    0.000 26013.880    0.011 helpers.py:15(stack)
        264383520/17135705 1100.397    0.000 15358.275    0.001 module.py:715(_call_impl)
                7343945  225.478    0.000 14194.437    0.002 agent.py:212(forward)
               24480258 13531.505    0.001 13531.508    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               22031835 11851.651    0.001 11851.651    0.001 {built-in method cat}
                2448315  188.477    0.000 11516.862    0.005 agent.py:74(chooseMulti)
               39168040  280.608    0.000 9850.683    0.000 container.py:115(forward)
              331361976 9800.042    0.000 9800.042    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2448315   68.355    0.000 8567.855    0.003 environments.py:83(step)
                7343445   50.307    0.000 7751.073    0.001 grad_mode.py:23(decorate_context)
                7343445  304.915    0.000 7620.827    0.001 adam.py:55(step)
                2448315   87.793    0.000 6667.433    0.003 agent.py:62(rememberMulti)
                7343445 1410.016    0.000 6230.296    0.001 functional.py:53(adam)
                2448315  219.629    0.000 6214.363    0.003 agent.py:66(<listcomp>)
                7343445   48.417    0.000 5749.642    0.001 tensor.py:181(backward)
                7343445   33.670    0.000 5701.224    0.001 __init__.py:68(backward)
                2448315   63.038    0.000 5621.382    0.002 environments.py:85(<listcomp>)
               49151698 1393.800    0.000 5582.364    0.000 helpers.py:8(clean)
                7343445 5494.566    0.001 5494.566    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2448315   89.280    0.000 5277.590    0.002 agent.py:84(<listcomp>)
               48966300  132.282    0.000 4961.723    0.000 exploration.py:34(epsilonGreedy)
               56495143 4770.381    0.000 4770.381    0.000 {built-in method as_tensor}
               44063670   76.457    0.000 3655.146    0.000 conv.py:422(forward)
               44063670   94.459    0.000 3539.746    0.000 conv.py:414(_conv_forward)
               44063670 3428.728    0.000 3428.728    0.000 {built-in method conv2d}
               58752560  122.231    0.000 3070.940    0.000 linear.py:92(forward)
               58752560  310.168    0.000 2885.910    0.000 functional.py:1669(linear)
                2448315   50.601    0.000 2706.716    0.001 environments.py:84(<listcomp>)
               48966300  179.513    0.000 2656.115    0.000 interop.py:274(step)
                7343951  407.420    0.000 2244.503    0.000 rnn.py:110(flatten_parameters)
              514041258 1143.173    0.000 1927.292    0.000 tensor.py:933(grad)
                7343945   84.760    0.000 1862.555    0.000 rnn.py:555(forward)
               51407615 1682.219    0.000 1682.219    0.000 {built-in method addmm}
                7343945 1679.608    0.000 1679.608    0.000 {built-in method lstm}
                7343445  169.385    0.000 1662.860    0.000 optimizer.py:167(zero_grad)
               93023970   80.499    0.000 1537.014    0.000 activation.py:713(forward)
               93023970  116.075    0.000 1456.515    0.000 functional.py:1292(leaky_relu)
                7343948 1343.012    0.000 1343.012    0.000 {built-in method _cudnn_rnn_flatten_weight}
               93023970 1328.965    0.000 1328.965    0.000 {built-in method torch._C._nn.leaky_relu}
              146868900 1270.840    0.000 1270.840    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               48966300   22.571    0.000 1154.333    0.000 wrapper.py:25(act)
               48966300   61.705    0.000 1131.762    0.000 env.py:197(act)
              146868900 1054.132    0.000 1054.132    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               48966300 1032.399    0.000 1037.619    0.000 libenv.py:352(act)
              646228514  347.270    0.000 1002.087    0.000 overrides.py:1073(has_torch_function)
                   4896    1.750    0.000  984.620    0.201 agent.py:139(update_target_network)
               98117998   71.734    0.000  809.348    0.000 extract_dict_ob.py:9(observe)
               98117998   44.716    0.000  737.614    0.000 wrapper.py:19(observe)
               73434450  697.880    0.000  697.880    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               98117998  182.580    0.000  692.898    0.000 libenv.py:344(observe)
               73434450  657.330    0.000  657.330    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   4896  175.666    0.036  637.225    0.130 memory.py:45(update_distribution)
              719667988  261.888    0.000  630.023    0.000 {built-in method builtins.any}
               73434450  592.781    0.000  592.781    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2448315    6.611    0.000  578.877    0.000 agent.py:230(avoid_similar_state)
               51423907  537.883    0.000  537.883    0.000 {built-in method numpy.array}
               73434450  522.733    0.000  522.733    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              147084298  154.503    0.000  510.155    0.000 libenv.py:281(_maybe_copy_dict)
                7343445   14.673    0.000  437.151    0.000 loss.py:445(forward)
              441257790  434.260    0.000  434.260    0.000 {method 'copy' of 'numpy.ndarray' objects}
               58752560  427.275    0.000  427.275    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7343445   49.255    0.000  422.479    0.000 functional.py:2637(mse_loss)
                7344945   13.986    0.000  401.929    0.000 functional.py:74(split)
               34273245  362.572    0.000  390.132    0.000 module.py:781(__setattr__)
                7344945   30.884    0.000  386.980    0.000 tensor.py:460(split)
               11475576  144.890    0.000  376.057    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               73434450  370.518    0.000  370.518    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               48966300   40.239    0.000  366.896    0.000 wrapper.py:22(get_info)
             1351209588  292.044    0.000  362.805    0.000 overrides.py:1086(<genexpr>)
              367709946  359.329    0.000  359.329    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7344945  354.445    0.000  354.445    0.000 {function Tensor.split at 0x7fcd41febd30}
                2447815  258.433    0.000  335.080    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               48966300  331.693    0.000  331.693    0.000 memory.py:17(inner)
               48966300  170.039    0.000  326.656    0.000 libenv.py:363(get_info)
                   9792  240.315    0.025  292.380    0.030 {built-in method _pickle.loads}
               25399107   23.964    0.000  274.252    0.000 <__array_function__ internals>:2(prod)
                2448315  221.891    0.000  267.611    0.000 agent.py:131(convert_values)
                7343445  255.952    0.000  255.952    0.000 {built-in method torch._C._nn.mse_loss}
                7343945   21.981    0.000  251.341    0.000 pooling.py:152(forward)
               25399147   18.750    0.000  246.131    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                9791260  245.391    0.000  245.391    0.000 {built-in method gather}
                7343945   13.298    0.000  229.361    0.000 _jit_internal.py:257(fn)
               25399107   30.779    0.000  227.380    0.000 fromnumeric.py:2881(prod)
               48966300  226.587    0.000  226.587    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               44062670  225.964    0.000  225.964    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                7343945   13.068    0.000  214.741    0.000 functional.py:574(_max_pool2d)
                7344945  208.731    0.000  208.731    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                7343945  200.782    0.000  200.782    0.000 {built-in method max_pool2d}
               73434696   89.085    0.000  200.547    0.000 tensor.py:596(__hash__)
                2820409  200.247    0.000  200.247    0.000 {built-in method tensor}
               25399107   59.382    0.000  196.602    0.000 fromnumeric.py:70(_wrapreduction)
              259880698  192.550    0.000  192.765    0.000 module.py:765(__getattr__)
                2447815  188.210    0.000  188.210    0.000 memory.py:43(<listcomp>)
               29375792  165.099    0.000  186.760    0.000 __init__.py:67(is_acceptable)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8468283: <Final_stateUncertainty0and0.25bigfish_0> in cluster <dcc> Done

Job <Final_stateUncertainty0and0.25bigfish_0> was submitted from host <n-62-27-20> by user <s183914> in cluster <dcc> at Thu Dec  3 15:35:43 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec  3 15:56:33 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 15:56:33 2020
Terminated at Fri Dec  4 14:51:53 2020
Results reported at Fri Dec  4 14:51:53 2020

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

    CPU time :                                   85447.00 sec.
    Max Memory :                                 54710 MB
    Average Memory :                             54030.44 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6730.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82522 sec.
    Turnaround time :                            83770 sec.

The output (if any) is above this job summary.

