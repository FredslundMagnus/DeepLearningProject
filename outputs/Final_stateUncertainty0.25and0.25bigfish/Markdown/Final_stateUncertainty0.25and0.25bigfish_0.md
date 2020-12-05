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
Subject: Job 8466080: <Final_stateUncertainty0.25and0.25bigfish_0> in cluster <dcc> Exited

Job <Final_stateUncertainty0.25and0.25bigfish_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Wed Dec  2 12:09:14 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec  3 13:34:17 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 13:34:17 2020
Terminated at Thu Dec  3 13:34:40 2020
Results reported at Thu Dec  3 13:34:40 2020

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

    CPU time :                                   9.00 sec.
    Max Memory :                                 1194 MB
    Average Memory :                             1194.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               60246.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   23 sec.
    Turnaround time :                            91526 sec.

The output (if any) is above this job summary.


    Name :                      Final_stateUncertainty0.25and0.25bigfish-0
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
    State difference weight :   0.25
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14837675397 function calls (14592894250 primitive calls) in 82513.65 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82513.645 82513.645 {built-in method builtins.exec}
                      1    0.046    0.046 82513.645 82513.645 <string>:1(<module>)
                      1  526.154  526.154 82513.599 82513.599 main.py:92(main)
                2423827  205.435    0.000 55092.413    0.023 agent.py:86(learn)
                2423327  765.788    0.000 53896.174    0.022 agent.py:96(TD_learn)
                2423327  166.393    0.000 26868.608    0.011 memory.py:35(sample_distribution)
                2423327  274.760    0.000 26061.969    0.011 helpers.py:15(stack)
        261738816/16964289 1155.813    0.000 15286.490    0.001 module.py:715(_call_impl)
                7270481  222.402    0.000 14112.317    0.002 agent.py:212(forward)
               24235378 13309.973    0.001 13309.975    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               21811443 12099.230    0.001 12099.230    0.001 {built-in method cat}
                2423827  187.502    0.000 11330.334    0.005 agent.py:74(chooseMulti)
               38776232  286.090    0.000 9794.545    0.000 container.py:115(forward)
              327959414 9600.117    0.000 9600.117    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2423827   67.731    0.000 8670.606    0.004 environments.py:83(step)
                7269981   48.521    0.000 7764.483    0.001 grad_mode.py:23(decorate_context)
                7269981  306.645    0.000 7635.767    0.001 adam.py:55(step)
                2423827   88.551    0.000 6705.086    0.003 agent.py:62(rememberMulti)
                2423827  220.551    0.000 6247.601    0.003 agent.py:66(<listcomp>)
                7269981 1411.078    0.000 6234.675    0.001 functional.py:53(adam)
                7269981   51.244    0.000 5752.516    0.001 tensor.py:181(backward)
                7269981   33.386    0.000 5701.272    0.001 __init__.py:68(backward)
                2423827   63.282    0.000 5645.648    0.002 environments.py:85(<listcomp>)
               48905821 1423.230    0.000 5638.725    0.000 helpers.py:8(clean)
                7269981 5495.179    0.001 5495.179    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2423827   89.425    0.000 5076.462    0.002 agent.py:84(<listcomp>)
               56175802 4794.877    0.000 4794.877    0.000 {built-in method as_tensor}
               48476540  132.291    0.000 4757.379    0.000 exploration.py:34(epsilonGreedy)
               43622886   78.229    0.000 3584.187    0.000 conv.py:422(forward)
               43622886   92.134    0.000 3467.407    0.000 conv.py:414(_conv_forward)
               43622886 3359.013    0.000 3359.013    0.000 {built-in method conv2d}
               58164848  124.406    0.000 3050.661    0.000 linear.py:92(forward)
               58164848  312.144    0.000 2864.445    0.000 functional.py:1669(linear)
                2423827   49.781    0.000 2732.843    0.001 environments.py:84(<listcomp>)
               48476540  179.208    0.000 2683.061    0.000 interop.py:274(step)
                7270487  414.731    0.000 2227.092    0.000 rnn.py:110(flatten_parameters)
              508898778 1147.659    0.000 1950.058    0.000 tensor.py:933(grad)
                7270481   85.834    0.000 1860.622    0.000 rnn.py:555(forward)
                7269981  174.973    0.000 1686.633    0.000 optimizer.py:167(zero_grad)
                7270481 1675.214    0.000 1675.214    0.000 {built-in method lstm}
               50893367 1650.444    0.000 1650.444    0.000 {built-in method addmm}
               92093426   85.991    0.000 1534.790    0.000 activation.py:713(forward)
               92093426  121.315    0.000 1448.799    0.000 functional.py:1292(leaky_relu)
                7270484 1322.304    0.000 1322.304    0.000 {built-in method _cudnn_rnn_flatten_weight}
               92093426 1316.206    0.000 1316.206    0.000 {built-in method torch._C._nn.leaky_relu}
              145399620 1274.613    0.000 1274.613    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               48476540   22.080    0.000 1148.084    0.000 wrapper.py:25(act)
               48476540   61.128    0.000 1126.004    0.000 env.py:197(act)
              145399620 1053.055    0.000 1053.055    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               48476540 1026.359    0.000 1031.174    0.000 libenv.py:352(act)
              639763682  342.437    0.000 1026.659    0.000 overrides.py:1073(has_torch_function)
                   4847    1.759    0.000  990.804    0.204 agent.py:139(update_target_network)
               97382361   76.733    0.000  837.442    0.000 extract_dict_ob.py:9(observe)
               97382361   41.938    0.000  760.709    0.000 wrapper.py:19(observe)
               97382361  185.273    0.000  718.771    0.000 libenv.py:344(observe)
               72699810  695.380    0.000  695.380    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              712468516  264.824    0.000  658.208    0.000 {built-in method builtins.any}
               72699810  655.069    0.000  655.069    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   4847  174.109    0.036  641.381    0.132 memory.py:45(update_distribution)
               72699810  593.454    0.000  593.454    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2423827    7.260    0.000  585.011    0.000 agent.py:230(avoid_similar_state)
               50909561  548.271    0.000  548.271    0.000 {built-in method numpy.array}
               72699810  527.509    0.000  527.509    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              145858901  155.859    0.000  525.144    0.000 libenv.py:281(_maybe_copy_dict)
              437581550  459.517    0.000  459.517    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7269981   16.506    0.000  438.398    0.000 loss.py:445(forward)
               58164848  426.843    0.000  426.843    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7269981   52.184    0.000  421.892    0.000 functional.py:2637(mse_loss)
                7271481   15.159    0.000  400.417    0.000 functional.py:74(split)
               11449083  151.913    0.000  393.446    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               33930413  366.743    0.000  392.445    0.000 module.py:781(__setattr__)
             1337692212  314.547    0.000  387.522    0.000 overrides.py:1086(<genexpr>)
                7271481   32.147    0.000  384.268    0.000 tensor.py:460(split)
               48476540   41.259    0.000  378.135    0.000 wrapper.py:22(get_info)
               72699810  373.705    0.000  373.705    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              363452298  364.994    0.000  364.994    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7271481  350.576    0.000  350.576    0.000 {function Tensor.split at 0x7f1538100d30}
                2423327  271.063    0.000  349.030    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               48476540  173.190    0.000  336.876    0.000 libenv.py:363(get_info)
               48476540  333.251    0.000  333.251    0.000 memory.py:17(inner)
                   9694  241.635    0.025  294.225    0.030 {built-in method _pickle.loads}
               25321633   24.465    0.000  285.670    0.000 <__array_function__ internals>:2(prod)
                2423827  227.552    0.000  271.149    0.000 agent.py:131(convert_values)
               25321673   19.078    0.000  256.942    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7269981  250.466    0.000  250.466    0.000 {built-in method torch._C._nn.mse_loss}
                7270481   18.597    0.000  247.262    0.000 pooling.py:152(forward)
                9693308  240.894    0.000  240.894    0.000 {built-in method gather}
               25321633   30.793    0.000  237.865    0.000 fromnumeric.py:2881(prod)
               48476540  229.659    0.000  229.659    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7270481   13.200    0.000  228.664    0.000 _jit_internal.py:257(fn)
               43621886  227.769    0.000  227.769    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2423827   25.487    0.000  224.384    0.000 environments.py:86(<listcomp>)
                7270481   14.115    0.000  214.199    0.000 functional.py:574(_max_pool2d)
                7271481  208.851    0.000  208.851    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               25321633   59.991    0.000  207.071    0.000 fromnumeric.py:70(_wrapreduction)
                2792197  203.779    0.000  203.779    0.000 {built-in method tensor}
               72700056   89.884    0.000  202.142    0.000 tensor.py:596(__hash__)
                7270481  199.231    0.000  199.231    0.000 {built-in method max_pool2d}
               48476560   32.477    0.000  198.901    0.000 environments.py:89(reset)
                2423327  195.334    0.000  195.334    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8468284: <Final_stateUncertainty0.25and0.25bigfish_0> in cluster <dcc> Done

Job <Final_stateUncertainty0.25and0.25bigfish_0> was submitted from host <n-62-27-20> by user <s183914> in cluster <dcc> at Thu Dec  3 15:35:43 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec  3 18:22:49 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 18:22:49 2020
Terminated at Fri Dec  4 17:18:07 2020
Results reported at Fri Dec  4 17:18:07 2020

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

    CPU time :                                   85680.00 sec.
    Max Memory :                                 54710 MB
    Average Memory :                             54053.47 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6730.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82518 sec.
    Turnaround time :                            92544 sec.

The output (if any) is above this job summary.

