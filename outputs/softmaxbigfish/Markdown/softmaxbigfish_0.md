
    Name :                      softmaxbigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      0
    Exploration :               softmax
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12436109927 function calls (12211458752 primitive calls) in 82514.10 seconds

##    Ordered by: cumulative time
   List reduced from 1347 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82514.097 82514.097 {built-in method builtins.exec}
                      1    0.036    0.036 82514.097 82514.097 <string>:1(<module>)
                      1  444.859  444.859 82514.060 82514.060 main.py:11(main)
                2340426  104.089    0.000 49474.221    0.021 agent.py:57(learn)
                2339926  384.776    0.000 48784.698    0.021 agent.py:67(TD_learn)
                2339926  151.659    0.000 26983.503    0.012 memory.py:35(sample_distribution)
                2339926  284.107    0.000 26272.495    0.011 helpers.py:12(stack)
                2340426   41.160    0.000 18143.314    0.008 agent.py:51(chooseMulti)
        236345026/11700130 1002.850    0.000 15327.771    0.001 module.py:715(_call_impl)
                9360204  266.263    0.000 15064.481    0.002 agent.py:147(forward)
                2340426  143.318    0.000 13771.433    0.006 agent.py:55(<listcomp>)
              327659640 13247.694    0.000 13247.694    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               46808520 1540.201    0.000 13242.092    0.000 exploration.py:21(softmax)
               21060900 12928.522    0.001 12928.554    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               21060834 12652.903    0.001 12652.903    0.001 {built-in method cat}
               37440816  251.069    0.000 8968.022    0.000 container.py:115(forward)
                2340426   64.833    0.000 8137.971    0.003 environments.py:73(step)
                2340426    7.215    0.000 6139.379    0.003 agent.py:42(rememberMulti)
                2340426  212.706    0.000 6132.165    0.003 agent.py:43(<listcomp>)
                2340426   51.164    0.000 5289.201    0.002 environments.py:75(<listcomp>)
               46948874 1341.065    0.000 5256.378    0.000 helpers.py:8(clean)
               56161224   98.048    0.000 4560.210    0.000 conv.py:422(forward)
               53968652 4458.778    0.000 4458.778    0.000 {built-in method as_tensor}
               56161224  116.594    0.000 4417.234    0.000 conv.py:414(_conv_forward)
                2339926   21.391    0.000 4355.601    0.002 grad_mode.py:23(decorate_context)
                2339926  167.965    0.000 4306.736    0.002 adam.py:55(step)
               56161224 4280.644    0.000 4280.644    0.000 {built-in method conv2d}
                2339926   22.887    0.000 3761.889    0.002 tensor.py:181(backward)
                2339926   15.985    0.000 3739.002    0.002 __init__.py:68(backward)
                2339926 3654.423    0.002 3654.423    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2339926  781.462    0.000 3490.291    0.001 functional.py:53(adam)
               46808520 1980.072    0.000 2820.843    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                9360210  497.626    0.000 2717.577    0.000 rnn.py:110(flatten_parameters)
                2340426   48.822    0.000 2621.589    0.001 environments.py:74(<listcomp>)
               46808520  170.466    0.000 2572.767    0.000 interop.py:274(step)
                9360204  106.035    0.000 2316.522    0.000 rnn.py:555(forward)
                9360204 2087.811    0.000 2087.811    0.000 {built-in method lstm}
                9360207 1638.119    0.000 1638.119    0.000 {built-in method _cudnn_rnn_flatten_weight}
               28080612   65.231    0.000 1508.299    0.000 linear.py:92(forward)
               28080612  117.641    0.000 1413.364    0.000 functional.py:1669(linear)
               84241836   79.008    0.000 1400.485    0.000 activation.py:713(forward)
               84241836  119.646    0.000 1321.477    0.000 functional.py:1292(leaky_relu)
               84241836 1190.476    0.000 1190.476    0.000 {built-in method torch._C._nn.leaky_relu}
              313550150  695.145    0.000 1157.864    0.000 tensor.py:933(grad)
               46808520   23.192    0.000 1127.388    0.000 wrapper.py:25(act)
               46808520   56.939    0.000 1104.196    0.000 env.py:197(act)
               46808520 1012.373    0.000 1016.924    0.000 libenv.py:352(act)
                2339926   95.452    0.000  971.217    0.000 optimizer.py:167(zero_grad)
               28080612  937.704    0.000  937.704    0.000 {built-in method addmm}
               46808520   85.769    0.000  834.352    0.000 functional.py:1479(softmax)
               93757394   72.031    0.000  787.419    0.000 extract_dict_ob.py:9(observe)
               46808520  740.539    0.000  740.539    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               84237336  719.282    0.000  719.282    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               93757394   40.440    0.000  715.389    0.000 wrapper.py:19(observe)
               93757394  184.975    0.000  674.949    0.000 libenv.py:344(observe)
               84237336  596.605    0.000  596.605    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   4680    1.261    0.000  585.434    0.125 agent.py:101(update_target_network)
               49148586   61.993    0.000  579.623    0.000 <__array_function__ internals>:2(prod)
              383749604  199.213    0.000  577.812    0.000 overrides.py:1073(has_torch_function)
                   4680  153.008    0.033  517.491    0.111 memory.py:45(update_distribution)
               49148626   49.035    0.000  507.679    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              140565914  148.835    0.000  487.465    0.000 libenv.py:281(_maybe_copy_dict)
               37441985  451.871    0.000  481.157    0.000 module.py:781(__setattr__)
               49148586   72.203    0.000  458.644    0.000 fromnumeric.py:2881(prod)
               49157806  432.443    0.000  432.443    0.000 {built-in method numpy.array}
              421702422  421.681    0.000  421.681    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7021278   12.050    0.000  398.869    0.000 functional.py:74(split)
               49148586  138.320    0.000  386.441    0.000 fromnumeric.py:70(_wrapreduction)
               46808520  386.022    0.000  386.022    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7021278   30.803    0.000  385.929    0.000 tensor.py:460(split)
               42118668  383.654    0.000  383.654    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               42118668  364.706    0.000  364.706    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              416510092  144.723    0.000  360.269    0.000 {built-in method builtins.any}
               46808520   38.371    0.000  354.752    0.000 wrapper.py:22(get_info)
                7021278  353.830    0.000  353.830    0.000 {function Tensor.split at 0x7ff2589aeca0}
              348438806  351.771    0.000  351.771    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               42118668  334.424    0.000  334.424    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46808520  325.518    0.000  325.518    0.000 memory.py:17(inner)
               46808520  160.738    0.000  316.380    0.000 libenv.py:363(get_info)
                9360204   23.878    0.000  307.337    0.000 pooling.py:152(forward)
               42118668  296.772    0.000  296.772    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9360204   16.266    0.000  283.459    0.000 _jit_internal.py:257(fn)
                2339926  218.912    0.000  275.381    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                9360204   17.313    0.000  265.581    0.000 functional.py:574(_max_pool2d)
                9360204  247.093    0.000  247.093    0.000 {built-in method max_pool2d}
               37440828  195.772    0.000  222.224    0.000 __init__.py:67(is_acceptable)
               28080612  220.908    0.000  220.908    0.000 {method 't' of 'torch._C._TensorBase' objects}
              795579820  170.996    0.000  213.320    0.000 overrides.py:1086(<genexpr>)
                9360204  211.831    0.000  211.831    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
               51493192  210.867    0.000  210.867    0.000 {method 'reduce' of 'numpy.ufunc' objects}
               42118668  205.582    0.000  205.582    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2339926  194.332    0.000  194.332    0.000 memory.py:43(<listcomp>)
               49148606   68.072    0.000  193.566    0.000 numerictypes.py:360(issubdtype)
              224879308  170.812    0.000  170.946    0.000 module.py:765(__getattr__)
                2340426   27.001    0.000  162.348    0.000 environments.py:76(<listcomp>)
                2339926    6.521    0.000  160.031    0.000 loss.py:445(forward)
                2340426   14.084    0.000  154.931    0.000 collector.py:7(collect)
                2339926   19.785    0.000  153.510    0.000 functional.py:2637(mse_loss)
               23400260  149.130    0.000  149.130    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              187514788   49.746    0.000  143.210    0.000 libenv.py:271(_maybe_copy_ndarray)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8447013: <softmaxbigfish_0> in cluster <dcc> Done

Job <softmaxbigfish_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 13:05:38 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Nov 28 06:29:23 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 28 06:29:23 2020
Terminated at Sun Nov 29 05:24:43 2020
Results reported at Sun Nov 29 05:24:43 2020

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

    CPU time :                                   87455.00 sec.
    Max Memory :                                 56941 MB
    Average Memory :                             56185.43 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4499.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82521 sec.
    Turnaround time :                            145145 sec.

The output (if any) is above this job summary.

