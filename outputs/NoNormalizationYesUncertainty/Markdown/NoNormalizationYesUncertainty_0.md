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
Subject: Job 8423609: <NoNormalizationYesUncertainty_0> in cluster <dcc> Exited

Job <NoNormalizationYesUncertainty_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue Nov 24 20:27:38 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Nov 24 21:12:13 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 21:12:13 2020
Terminated at Tue Nov 24 21:12:41 2020
Results reported at Tue Nov 24 21:12:41 2020

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

    CPU time :                                   12.00 sec.
    Max Memory :                                 1152 MB
    Average Memory :                             1152.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               60288.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   30 sec.
    Turnaround time :                            2703 sec.

The output (if any) is above this job summary.


    Name :                      NoNormalizationYesUncertainty-0
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
    Reward normalization :      0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      11827051409 function calls (11645862074 primitive calls) in 86114.95 seconds

##    Ordered by: cumulative time
   List reduced from 1342 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 86114.946 86114.946 {built-in method builtins.exec}
                      1    0.064    0.064 86114.946 86114.946 <string>:1(<module>)
                      1  339.856  339.856 86114.881 86114.881 main.py:11(main)
                1887698   86.788    0.000 64888.936    0.034 agent.py:49(learn)
                1887198  412.197    0.000 64246.988    0.034 agent.py:59(TD_learn)
                1887198 16736.914    0.009 40115.130    0.021 memory.py:31(sample)
                1887198  415.518    0.000 22731.727    0.012 helpers.py:12(stack)
        190619498/9436490  862.296    0.000 14828.225    0.002 module.py:715(_call_impl)
                7549292  233.367    0.000 14591.333    0.002 agent.py:139(forward)
               20760678 11593.782    0.001 11593.782    0.001 {built-in method cat}
               16986348 10403.018    0.001 10403.031    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               30197168  245.896    0.000 8839.041    0.000 container.py:115(forward)
                1887698   57.065    0.000 8516.759    0.005 environments.py:73(step)
                1887698    6.728    0.000 6282.800    0.003 agent.py:34(rememberMulti)
                1887698  280.163    0.000 6276.072    0.003 agent.py:35(<listcomp>)
                1887198   16.634    0.000 6197.010    0.003 grad_mode.py:23(decorate_context)
                1887198  171.997    0.000 6156.266    0.003 adam.py:55(step)
              253363271 6037.928    0.000 6037.928    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1887698   40.173    0.000 5916.238    0.003 agent.py:43(chooseMulti)
                1887698   50.976    0.000 5315.583    0.003 environments.py:75(<listcomp>)
               38028286 1317.693    0.000 5309.581    0.000 helpers.py:8(clean)
                1887198 1133.846    0.001 5308.533    0.003 functional.py:53(adam)
               43689880 4525.180    0.000 4525.180    0.000 {built-in method as_tensor}
               45295752   85.584    0.000 4441.448    0.000 conv.py:422(forward)
               45295752   92.482    0.000 4318.419    0.000 conv.py:414(_conv_forward)
                1887198   18.791    0.000 4295.450    0.002 tensor.py:181(backward)
                1887198   12.176    0.000 4276.659    0.002 __init__.py:68(backward)
               45295752 4209.662    0.000 4209.662    0.000 {built-in method conv2d}
                1887198 4200.257    0.002 4200.257    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1887698   45.738    0.000 2922.285    0.002 environments.py:74(<listcomp>)
               37753960  166.299    0.000 2876.547    0.000 interop.py:274(step)
                7549298  470.368    0.000 2853.155    0.000 rnn.py:110(flatten_parameters)
                7549292   88.272    0.000 1947.613    0.000 rnn.py:555(forward)
                7549295 1876.724    0.000 1876.724    0.000 {built-in method _cudnn_rnn_flatten_weight}
                7549292 1755.976    0.000 1755.976    0.000 {built-in method lstm}
                1887698   95.488    0.000 1669.595    0.001 agent.py:47(<listcomp>)
               37753960   20.341    0.000 1541.979    0.000 wrapper.py:25(act)
               37753960   63.598    0.000 1521.638    0.000 env.py:197(act)
               22647876   57.253    0.000 1516.750    0.000 linear.py:92(forward)
               67943628   65.944    0.000 1488.499    0.000 activation.py:713(forward)
               22647876  100.156    0.000 1432.707    0.000 functional.py:1669(linear)
               67943628  102.686    0.000 1422.554    0.000 functional.py:1292(leaky_relu)
               37753960 1416.109    0.000 1419.843    0.000 libenv.py:352(act)
               67943628 1310.272    0.000 1310.272    0.000 {built-in method torch._C._nn.leaky_relu}
               37753960  142.096    0.000 1303.430    0.000 exploration.py:33(epsilonGreedy)
              290628558  792.174    0.000 1263.822    0.000 tensor.py:933(grad)
                1887198  119.751    0.000 1236.589    0.001 optimizer.py:167(zero_grad)
               83036712 1122.330    0.000 1122.330    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               22647876  976.329    0.000  976.329    0.000 {built-in method addmm}
               83036712  956.060    0.000  956.060    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               75782246   68.344    0.000  713.672    0.000 extract_dict_ob.py:9(observe)
               75782246   34.849    0.000  645.327    0.000 wrapper.py:19(observe)
                1887198  295.526    0.000  637.153    0.000 random.py:315(sample)
               75782246  160.300    0.000  610.479    0.000 libenv.py:344(observe)
              354794968  209.100    0.000  581.034    0.000 overrides.py:1073(has_torch_function)
               41518356  577.633    0.000  577.633    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   3775    0.990    0.000  555.159    0.147 agent.py:93(update_target_network)
               41518356  539.201    0.000  539.201    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               41518356  510.161    0.000  510.161    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   3775  134.301    0.036  494.343    0.131 memory.py:45(update_distribution)
               41518356  454.436    0.000  454.436    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              113536206  132.381    0.000  440.474    0.000 libenv.py:281(_maybe_copy_dict)
               37761510  433.891    0.000  433.891    0.000 {built-in method numpy.array}
              271687139  433.586    0.000  433.586    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10914449  156.849    0.000  404.547    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              340612393  388.309    0.000  388.309    0.000 {method 'copy' of 'numpy.ndarray' objects}
               30198337  360.682    0.000  383.095    0.000 module.py:781(__setattr__)
              381217264  144.925    0.000  352.481    0.000 {built-in method builtins.any}
               41518356  350.272    0.000  350.272    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               37753960   37.031    0.000  326.110    0.000 wrapper.py:22(get_info)
                5663094   10.302    0.000  307.469    0.000 functional.py:74(split)
                5663094   26.017    0.000  296.333    0.000 tensor.py:460(split)
                7549292   16.057    0.000  292.839    0.000 pooling.py:152(forward)
               37753960  151.357    0.000  289.079    0.000 libenv.py:363(get_info)
                7549292   13.399    0.000  276.782    0.000 _jit_internal.py:257(fn)
               37753960  273.461    0.000  273.461    0.000 memory.py:17(inner)
               37753960  270.677    0.000  270.677    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                5663094  268.897    0.000  268.897    0.000 {function Tensor.split at 0x7f63e7a83ca0}
              483250723  175.235    0.000  267.341    0.000 random.py:250(_randbelow_with_getrandbits)
                7549292   14.577    0.000  262.024    0.000 functional.py:574(_max_pool2d)
               21829038   19.211    0.000  247.701    0.000 <__array_function__ internals>:2(prod)
                7549292  246.462    0.000  246.462    0.000 {built-in method max_pool2d}
               22647876  237.646    0.000  237.646    0.000 {method 't' of 'torch._C._TensorBase' objects}
               21829078   15.120    0.000  224.541    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                1887698   28.412    0.000  221.826    0.000 environments.py:76(<listcomp>)
               21829038   25.790    0.000  209.421    0.000 fromnumeric.py:2881(prod)
              732237812  166.484    0.000  205.854    0.000 overrides.py:1086(<genexpr>)
                7549292  205.402    0.000  205.402    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
               30197180  172.556    0.000  195.266    0.000 __init__.py:67(is_acceptable)
               37753980   32.053    0.000  193.421    0.000 environments.py:79(reset)
               21829038   50.673    0.000  183.631    0.000 fromnumeric.py:70(_wrapreduction)
                5661594  170.728    0.000  170.728    0.000 {built-in method gather}
               18872980  157.349    0.000  157.349    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                1887698   13.574    0.000  151.474    0.000 collector.py:7(collect)
                1887198    6.449    0.000  150.223    0.000 loss.py:445(forward)
              181372170  144.270    0.000  144.381    0.000 module.py:765(__getattr__)
                1887198   17.208    0.000  143.774    0.000 functional.py:2637(mse_loss)
              190619498  142.856    0.000  142.856    0.000 {built-in method torch._C._get_tracing_state}
                3775397  136.885    0.000  136.885    0.000 {built-in method builtins.sum}
              151564492   43.548    0.000  133.323    0.000 libenv.py:271(_maybe_copy_ndarray)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 8423732: <NoNormalizationYesUncertainty_0> in cluster <dcc> Done

Job <NoNormalizationYesUncertainty_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue Nov 24 22:01:07 2020
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Nov 24 22:14:35 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 22:14:35 2020
Terminated at Wed Nov 25 22:09:56 2020
Results reported at Wed Nov 25 22:09:56 2020

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

    CPU time :                                   87908.00 sec.
    Max Memory :                                 56994 MB
    Average Memory :                             56271.67 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4446.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86120 sec.
    Turnaround time :                            86929 sec.

The output (if any) is above this job summary.

