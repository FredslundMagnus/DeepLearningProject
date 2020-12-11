
    Name :                      BIGFISH_U_S_0_0.1bigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              1000
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           1000
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13323297783 function calls (13102907493 primitive calls) in 82513.65 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82513.648 82513.648 {built-in method builtins.exec}
                      1    0.072    0.072 82513.648 82513.648 <string>:1(<module>)
                      1  457.594  457.594 82513.575 82513.575 main.py:92(main)
                2242739  178.166    0.000 55740.080    0.025 agent.py:84(learn)
                2153783  743.335    0.000 55000.584    0.026 agent.py:99(TD_learn)
                2153783  151.406    0.000 24137.093    0.011 memory.py:35(sample_distribution)
                2153783  269.017    0.000 23390.852    0.011 helpers.py:15(stack)
        235550106/15166436 1050.498    0.000 16514.834    0.001 module.py:715(_call_impl)
                6550305  218.613    0.000 15257.544    0.002 agent.py:216(forward)
               21805805 11492.710    0.001 11492.757    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               19650915 11347.392    0.001 11347.392    0.001 {built-in method cat}
               34906307  298.537    0.000 10836.278    0.000 container.py:115(forward)
                6461349   42.440    0.000 9993.067    0.002 grad_mode.py:23(decorate_context)
                6461349  282.970    0.000 9876.057    0.002 adam.py:55(step)
                2242739   67.232    0.000 9575.525    0.004 environments.py:83(step)
                2242739  214.118    0.000 8977.102    0.004 agent.py:70(chooseMulti)
                6461349 1825.249    0.000 8513.969    0.001 functional.py:53(adam)
                2154782  104.490    0.000 7562.176    0.004 agent.py:58(rememberMulti)
                2154782  313.748    0.000 7044.059    0.003 agent.py:62(<listcomp>)
              292253360 6820.397    0.000 6820.397    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6461349   47.533    0.000 6511.286    0.001 tensor.py:181(backward)
                6461349   28.521    0.000 6463.753    0.001 __init__.py:68(backward)
                2242739   69.185    0.000 6374.993    0.003 environments.py:85(<listcomp>)
               45061030 1541.135    0.000 6339.088    0.000 helpers.py:8(clean)
                6461349 6251.468    0.001 6251.468    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               51522379 5307.703    0.000 5307.703    0.000 {built-in method as_tensor}
               39301830   76.401    0.000 3929.594    0.000 conv.py:422(forward)
               39301830   79.066    0.000 3818.909    0.000 conv.py:414(_conv_forward)
               39301830 3723.011    0.000 3723.011    0.000 {built-in method conv2d}
               52316481  120.957    0.000 3457.459    0.000 linear.py:92(forward)
               52316481  324.802    0.000 3277.841    0.000 functional.py:1669(linear)
                2242739   51.364    0.000 2905.345    0.001 environments.py:84(<listcomp>)
               44854780  193.057    0.000 2853.981    0.000 interop.py:274(step)
                6550311  401.190    0.000 2479.255    0.000 rnn.py:110(flatten_parameters)
              452294538 1268.411    0.000 2026.675    0.000 tensor.py:933(grad)
                6461349  183.924    0.000 1971.916    0.000 optimizer.py:167(zero_grad)
               45852135 1937.938    0.000 1937.938    0.000 {built-in method addmm}
                2154782  108.005    0.000 1887.997    0.001 agent.py:82(<listcomp>)
               82913224   75.982    0.000 1841.993    0.000 activation.py:713(forward)
              129226980 1809.178    0.000 1809.178    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6550305   77.509    0.000 1773.668    0.000 rnn.py:555(forward)
               82913224  118.919    0.000 1766.012    0.000 functional.py:1292(leaky_relu)
                6550308 1646.298    0.000 1646.298    0.000 {built-in method _cudnn_rnn_flatten_weight}
               82913224 1636.045    0.000 1636.045    0.000 {built-in method torch._C._nn.leaky_relu}
                6550305 1605.454    0.000 1605.454    0.000 {built-in method lstm}
              129226980 1513.634    0.000 1513.634    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               43095640  159.067    0.000 1464.319    0.000 exploration.py:34(epsilonGreedy)
               44854780   22.374    0.000 1262.073    0.000 wrapper.py:25(act)
               44854780   78.363    0.000 1239.698    0.000 env.py:197(act)
               44854780 1113.048    0.000 1117.517    0.000 libenv.py:352(act)
              569224755  350.539    0.000  970.006    0.000 overrides.py:1073(has_torch_function)
               64613490  942.103    0.000  942.103    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               64613490  869.346    0.000  869.346    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89915810   77.954    0.000  846.229    0.000 extract_dict_ob.py:9(observe)
               64613490  806.037    0.000  806.037    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               89915810   40.469    0.000  768.276    0.000 wrapper.py:19(observe)
               89915810  194.355    0.000  727.807    0.000 libenv.py:344(observe)
               64613490  723.899    0.000  723.899    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2154782    7.453    0.000  665.639    0.000 agent.py:234(avoid_similar_state)
              634463958  245.716    0.000  594.972    0.000 {built-in method builtins.any}
                   2242    0.926    0.000  561.329    0.250 agent.py:142(update_target_network)
               64613490  559.150    0.000  559.150    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              134770590  161.259    0.000  524.379    0.000 libenv.py:281(_maybe_copy_dict)
               52316481  522.470    0.000  522.470    0.000 {method 't' of 'torch._C._TensorBase' objects}
              327932794  522.369    0.000  522.369    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                6461349   12.614    0.000  457.962    0.000 loss.py:445(forward)
              404314012  457.551    0.000  457.551    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6461349   45.299    0.000  445.347    0.000 functional.py:2637(mse_loss)
               11181854  165.582    0.000  417.247    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               44854780   42.951    0.000  392.913    0.000 wrapper.py:22(get_info)
                6728217   13.627    0.000  392.491    0.000 functional.py:74(split)
                6728217   31.961    0.000  377.899    0.000 tensor.py:460(split)
               44854780  181.383    0.000  349.962    0.000 libenv.py:363(get_info)
             1190765991  276.483    0.000  344.428    0.000 overrides.py:1086(<genexpr>)
                6728217  344.272    0.000  344.272    0.000 {function Tensor.split at 0x7fb5939f4d30}
               30510621  307.334    0.000  329.657    0.000 module.py:781(__setattr__)
                2153783  254.705    0.000  329.650    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               43095640  328.812    0.000  328.812    0.000 memory.py:17(inner)
               44854780  327.400    0.000  327.400    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               47013047  315.469    0.000  315.469    0.000 {built-in method numpy.array}
                   2242   83.777    0.037  307.488    0.137 memory.py:45(update_distribution)
               24517631   24.815    0.000  293.930    0.000 <__array_function__ internals>:2(prod)
               39123918  286.266    0.000  286.266    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2154782  283.618    0.000  284.011    0.000 agent.py:134(convert_values)
                6461349  283.682    0.000  283.682    0.000 {built-in method torch._C._nn.mse_loss}
                8615132  267.263    0.000  267.263    0.000 {built-in method gather}
               24517671   19.011    0.000  264.437    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6550305   19.735    0.000  260.281    0.000 pooling.py:152(forward)
               24517631   32.001    0.000  245.426    0.000 fromnumeric.py:2881(prod)
                6464346  243.154    0.000  243.154    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6550305   11.848    0.000  240.546    0.000 _jit_internal.py:257(fn)
                2242739   30.518    0.000  227.955    0.000 environments.py:86(<listcomp>)
                6550305   12.358    0.000  227.549    0.000 functional.py:574(_max_pool2d)
                   4484  198.866    0.044  226.877    0.051 {built-in method _pickle.loads}
                2325172  214.476    0.000  214.476    0.000 {built-in method tensor}
                6550305  214.319    0.000  214.319    0.000 {built-in method max_pool2d}
               24517631   61.571    0.000  213.425    0.000 fromnumeric.py:70(_wrapreduction)
               44854800   39.830    0.000  197.443    0.000 environments.py:89(reset)
               64613736   86.795    0.000  195.310    0.000 tensor.py:596(__hash__)
                2242739   17.863    0.000  182.874    0.000 collector.py:8(collect)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 8552384: <BIGFISH_U_S_0_0.1bigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0_0.1bigfish_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Tue Dec  8 22:26:38 2020
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec 10 01:23:00 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec 10 01:23:00 2020
Terminated at Fri Dec 11 00:18:20 2020
Results reported at Fri Dec 11 00:18:20 2020

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

    CPU time :                                   84428.00 sec.
    Max Memory :                                 54678 MB
    Average Memory :                             54004.62 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6762.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82615 sec.
    Turnaround time :                            179502 sec.

The output (if any) is above this job summary.

