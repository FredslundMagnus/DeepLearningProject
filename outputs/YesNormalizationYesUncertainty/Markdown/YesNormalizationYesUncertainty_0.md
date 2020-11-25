Traceback (most recent call last):
  File "main.py", line 26, in <module>
    serverRun()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 27, in serverRun
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
  File "main.py", line 23, in main
    agent.learn()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 58, in learn
    self.TD_learn()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 80, in TD_learn
    loss.backward()
  File "/zhome/ea/9/137501/Desktop/DeepAI/project-env/lib/python3.8/site-packages/torch/tensor.py", line 221, in backward
    torch.autograd.backward(self, gradient, retain_graph, create_graph)
  File "/zhome/ea/9/137501/Desktop/DeepAI/project-env/lib/python3.8/site-packages/torch/autograd/__init__.py", line 130, in backward
    Variable._execution_engine.run_backward(
RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.cuda.FloatTensor [160, 128]] is at version 2; expected version 1 instead. Hint: enable anomaly detection to find the operation that failed to compute its gradient, with torch.autograd.set_detect_anomaly(True).

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8423610: <YesNormalizationYesUncertainty_0> in cluster <dcc> Exited

Job <YesNormalizationYesUncertainty_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue Nov 24 20:27:38 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Nov 24 21:12:43 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 21:12:43 2020
Terminated at Tue Nov 24 21:13:01 2020
Results reported at Tue Nov 24 21:13:01 2020

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

    CPU time :                                   10.53 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   20 sec.
    Turnaround time :                            2723 sec.

The output (if any) is above this job summary.


    Name :                      YesNormalizationYesUncertainty-0
    Discount :                  0.995
    Environment :               fruitbot
    Hours :                     24
    Memory :                    500000
    Update every :              500
    Use distribution :          0
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      1
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      12085316250 function calls (11900120355 primitive calls) in 85916.85 seconds

##    Ordered by: cumulative time
   List reduced from 1353 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 86118.579 86118.579 {built-in method builtins.exec}
                      1    0.045    0.045 86118.579 86118.579 <string>:1(<module>)
                      1  367.781  367.781 86118.532 86118.532 main.py:11(main)
                1929433   94.528    0.000 65848.808    0.034 agent.py:49(learn)
                1928933  440.096    0.000 64320.208    0.033 agent.py:59(TD_learn)
                1928933 16475.314    0.009 40438.197    0.021 memory.py:31(sample)
                1928933  507.785    0.000 23293.522    0.012 helpers.py:12(stack)
        194834733/9645165  858.054    0.000 14729.750    0.002 module.py:715(_call_impl)
                7716232  237.591    0.000 14488.894    0.002 agent.py:139(forward)
               21219763 11302.911    0.001 11302.911    0.001 {built-in method cat}
               17361963 10979.726    0.001 10979.795    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               30864928  246.001    0.000 8666.360    0.000 container.py:115(forward)
                1929433   55.839    0.000 7920.136    0.004 environments.py:73(step)
                1929433    6.394    0.000 6072.162    0.003 agent.py:34(rememberMulti)
                1929433  253.643    0.000 6065.769    0.003 agent.py:35(<listcomp>)
                1928933   18.041    0.000 5990.817    0.003 grad_mode.py:23(decorate_context)
                1928933  165.431    0.000 5949.814    0.003 adam.py:55(step)
              259162866 5846.813    0.000 5846.813    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1929433   42.237    0.000 5749.602    0.003 agent.py:43(chooseMulti)
                1928933 1102.186    0.001 5128.371    0.003 functional.py:53(adam)
                1929433   49.732    0.000 4871.808    0.003 environments.py:75(<listcomp>)
               38846110 1163.348    0.000 4859.603    0.000 helpers.py:8(clean)
               44632909 4402.565    0.000 4402.565    0.000 {built-in method as_tensor}
               46297392   82.387    0.000 4372.735    0.000 conv.py:422(forward)
               46297392   90.958    0.000 4254.921    0.000 conv.py:414(_conv_forward)
                1928933   23.830    0.000 4247.327    0.002 tensor.py:181(backward)
                1928933   14.832    0.000 4223.497    0.002 __init__.py:68(backward)
               46297392 4147.794    0.000 4147.794    0.000 {built-in method conv2d}
                1928933 4145.686    0.002 4145.686    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7716238  466.628    0.000 2855.532    0.000 rnn.py:110(flatten_parameters)
                1929433   43.098    0.000 2802.185    0.001 environments.py:74(<listcomp>)
               38588660  155.154    0.000 2759.087    0.000 interop.py:274(step)
                7716232   92.323    0.000 2023.603    0.000 rnn.py:555(forward)
                7716235 1852.663    0.000 1852.663    0.000 {built-in method _cudnn_rnn_flatten_weight}
                7716232 1821.371    0.000 1821.371    0.000 {built-in method lstm}
                1929433   91.791    0.000 1615.489    0.001 agent.py:47(<listcomp>)
               23148696   55.266    0.000 1483.067    0.000 linear.py:92(forward)
               38588660   18.447    0.000 1479.027    0.000 wrapper.py:25(act)
               38588660   59.102    0.000 1460.580    0.000 env.py:197(act)
               69446088   67.840    0.000 1443.155    0.000 activation.py:713(forward)
               23148696   99.917    0.000 1404.162    0.000 functional.py:1669(linear)
               69446088   94.336    0.000 1375.315    0.000 functional.py:1292(leaky_relu)
               38588660 1362.768    0.000 1366.260    0.000 libenv.py:352(act)
               69446088 1271.961    0.000 1271.961    0.000 {built-in method torch._C._nn.leaky_relu}
               38588660  131.840    0.000 1264.999    0.000 exploration.py:33(epsilonGreedy)
              297055748  770.274    0.000 1217.188    0.000 tensor.py:933(grad)
                1928933  115.941    0.000 1178.249    0.001 optimizer.py:167(zero_grad)
               84873052 1086.479    0.000 1086.479    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               23148696  956.734    0.000  956.734    0.000 {built-in method addmm}
               84873052  917.537    0.000  917.537    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   3858    0.131    0.000  885.940    0.230 memory.py:25(average_reward)
               77434770   63.869    0.000  686.758    0.000 extract_dict_ob.py:9(observe)
              389651592  263.188    0.000  662.255    0.000 {built-in method builtins.any}
               38603994  655.752    0.000  655.752    0.000 {built-in method numpy.array}
                1928933  307.358    0.000  653.881    0.000 random.py:315(sample)
               77434770   32.405    0.000  622.890    0.000 wrapper.py:19(observe)
               77434770  161.300    0.000  590.485    0.000 libenv.py:344(observe)
               42436526  572.179    0.000  572.179    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              362641148  204.947    0.000  551.666    0.000 overrides.py:1073(has_torch_function)
                   3858    1.031    0.000  548.132    0.142 agent.py:93(update_target_network)
               42436526  517.603    0.000  517.603    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   3858  134.879    0.035  489.804    0.127 memory.py:45(update_distribution)
               42436526  485.899    0.000  485.899    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               21919497   15.422    0.000  447.539    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                3862676  441.528    0.000  441.528    0.000 {built-in method builtins.sum}
               42436526  431.717    0.000  431.717    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              116023430  128.087    0.000  417.614    0.000 libenv.py:281(_maybe_copy_dict)
              277937836  413.304    0.000  413.304    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               30866097  385.432    0.000  408.192    0.000 module.py:781(__setattr__)
               10957754  154.157    0.000  389.755    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              348074148  366.331    0.000  366.331    0.000 {method 'copy' of 'numpy.ndarray' objects}
               42436526  327.828    0.000  327.828    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               38588660   34.366    0.000  312.401    0.000 wrapper.py:22(get_info)
                5788299   10.480    0.000  306.960    0.000 functional.py:74(split)
                5788299   27.546    0.000  295.715    0.000 tensor.py:460(split)
                7716232   18.027    0.000  291.780    0.000 pooling.py:152(forward)
               38588660  148.535    0.000  278.035    0.000 libenv.py:363(get_info)
               38588660  277.443    0.000  277.443    0.000 memory.py:17(inner)
                7716232   13.960    0.000  273.753    0.000 _jit_internal.py:257(fn)
              493937690  173.672    0.000  267.792    0.000 random.py:250(_randbelow_with_getrandbits)
                5788299  266.874    0.000  266.874    0.000 {function Tensor.split at 0x7f83f6574ca0}
               38588660  258.699    0.000  258.699    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7716232   15.761    0.000  258.394    0.000 functional.py:574(_max_pool2d)
                7716232  241.630    0.000  241.630    0.000 {built-in method max_pool2d}
               21915648   18.671    0.000  235.600    0.000 <__array_function__ internals>:2(prod)
               23148696  234.468    0.000  234.468    0.000 {method 't' of 'torch._C._TensorBase' objects}
                   3809    0.024    0.000  234.048    0.061 <__array_function__ internals>:2(std)
                   3809    0.073    0.000  234.004    0.061 fromnumeric.py:3381(std)
                   3809    0.045    0.000  233.931    0.061 _methods.py:232(_std)
                   3809    2.018    0.001  233.885    0.061 _methods.py:176(_var)
                   7618    0.021    0.000  230.523    0.030 _asarray.py:86(asanyarray)
               30864940  189.910    0.000  212.049    0.000 __init__.py:67(is_acceptable)
                7716232  201.610    0.000  201.610    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
               21915648   24.124    0.000  198.113    0.000 fromnumeric.py:2881(prod)
              748430992  155.987    0.000  195.461    0.000 overrides.py:1086(<genexpr>)
                1929433   27.879    0.000  190.304    0.000 environments.py:76(<listcomp>)
               21915648   45.808    0.000  173.989    0.000 fromnumeric.py:70(_wrapreduction)
                5786799  172.656    0.000  172.656    0.000 {built-in method gather}
               38588680   26.305    0.000  162.439    0.000 environments.py:79(reset)
               19290330  153.171    0.000  153.171    0.000 {method 'view' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8423733: <YesNormalizationYesUncertainty_0> in cluster <dcc> Done

Job <YesNormalizationYesUncertainty_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue Nov 24 22:01:07 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Nov 24 22:19:17 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 22:19:17 2020
Terminated at Wed Nov 25 22:14:42 2020
Results reported at Wed Nov 25 22:14:42 2020

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

    CPU time :                                   88243.00 sec.
    Max Memory :                                 56931 MB
    Average Memory :                             56219.91 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4509.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86126 sec.
    Turnaround time :                            87215 sec.

The output (if any) is above this job summary.

