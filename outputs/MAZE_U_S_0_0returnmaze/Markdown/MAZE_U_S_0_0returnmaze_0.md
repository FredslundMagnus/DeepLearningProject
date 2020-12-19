
    Name :                      MAZE_U_S_0_0returnmaze-0
    Discount :                  0.99
    Environment :               maze
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
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13642369055 function calls (13417204662 primitive calls) in 82513.98 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82513.978 82513.978 {built-in method builtins.exec}
                      1    0.154    0.154 82513.978 82513.978 <string>:1(<module>)
                      1  505.087  505.087 82513.819 82513.819 main.py:92(main)
                2291373  243.257    0.000 56588.815    0.025 agent.py:84(learn)
                2200418  946.273    0.000 55806.702    0.025 agent.py:99(TD_learn)
                2200418  156.310    0.000 24791.323    0.011 memory.py:35(sample_distribution)
                2200418  282.375    0.000 24030.705    0.011 helpers.py:15(stack)
        240652653/15494880 1059.175    0.000 16600.723    0.001 module.py:715(_call_impl)
                6692209  217.880    0.000 15349.669    0.002 agent.py:231(forward)
               22278152 12011.716    0.001 12011.717    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20076627 11376.608    0.001 11376.608    0.001 {built-in method cat}
               35662462  304.701    0.000 10728.125    0.000 container.py:115(forward)
                6601254   44.191    0.000 9533.751    0.001 grad_mode.py:23(decorate_context)
                6601254  282.524    0.000 9417.599    0.001 adam.py:55(step)
                2291373   64.460    0.000 9128.497    0.004 environments.py:83(step)
                2291373  213.576    0.000 8763.313    0.004 agent.py:70(chooseMulti)
                6601254 1756.090    0.000 8095.558    0.001 functional.py:53(adam)
                2201417   95.798    0.000 7347.689    0.003 agent.py:58(rememberMulti)
                2201417  286.212    0.000 6873.928    0.003 agent.py:62(<listcomp>)
              298835601 6653.567    0.000 6653.567    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6601254   48.875    0.000 6406.765    0.001 tensor.py:181(backward)
                6601254   33.271    0.000 6357.891    0.001 __init__.py:68(backward)
                6601254 6141.157    0.001 6141.157    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2291373   64.528    0.000 5799.048    0.003 environments.py:85(<listcomp>)
               46049891 1351.958    0.000 5766.435    0.000 helpers.py:8(clean)
               52651145 4989.981    0.000 4989.981    0.000 {built-in method as_tensor}
               40153254   73.305    0.000 3943.112    0.000 conv.py:422(forward)
               40153254   83.591    0.000 3836.695    0.000 conv.py:414(_conv_forward)
               40153254 3737.819    0.000 3737.819    0.000 {built-in method conv2d}
               53449714  118.933    0.000 3406.784    0.000 linear.py:92(forward)
               53449714  319.552    0.000 3230.058    0.000 functional.py:1669(linear)
                2291373   48.666    0.000 3058.281    0.001 environments.py:84(<listcomp>)
               45827460  180.849    0.000 3009.615    0.000 interop.py:274(step)
                6692215  434.653    0.000 2621.960    0.000 rnn.py:110(flatten_parameters)
              462087888 1216.639    0.000 1929.186    0.000 tensor.py:933(grad)
               46845463 1915.627    0.000 1915.627    0.000 {built-in method addmm}
                6601254  187.642    0.000 1864.924    0.000 optimizer.py:167(zero_grad)
                2201417  103.157    0.000 1842.159    0.001 agent.py:82(<listcomp>)
                6692209   79.310    0.000 1817.249    0.000 rnn.py:555(forward)
               84709342   75.428    0.000 1783.267    0.000 activation.py:713(forward)
              132025080 1721.596    0.000 1721.596    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               84709342  118.363    0.000 1707.839    0.000 functional.py:1292(leaky_relu)
                6692212 1703.524    0.000 1703.524    0.000 {built-in method _cudnn_rnn_flatten_weight}
                6692209 1639.992    0.000 1639.992    0.000 {built-in method lstm}
               84709342 1579.049    0.000 1579.049    0.000 {built-in method torch._C._nn.leaky_relu}
               45827460   19.873    0.000 1483.839    0.000 wrapper.py:25(act)
               45827460   67.008    0.000 1463.966    0.000 env.py:197(act)
               44028340  149.555    0.000 1437.281    0.000 exploration.py:34(epsilonGreedy)
              132025080 1430.915    0.000 1430.915    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               45827460 1350.465    0.000 1354.912    0.000 libenv.py:352(act)
              581550388  325.193    0.000  918.569    0.000 overrides.py:1073(has_torch_function)
               66012540  893.695    0.000  893.695    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               66012540  824.145    0.000  824.145    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               91877351   73.409    0.000  821.648    0.000 extract_dict_ob.py:9(observe)
               66012540  761.622    0.000  761.622    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91877351   39.386    0.000  748.239    0.000 wrapper.py:19(observe)
               91877351  193.514    0.000  708.852    0.000 libenv.py:344(observe)
               66012540  682.557    0.000  682.557    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2201417    6.348    0.000  640.666    0.000 agent.py:249(avoid_similar_state)
              648202634  234.321    0.000  572.600    0.000 {built-in method builtins.any}
                   2291    0.919    0.000  538.857    0.235 agent.py:157(update_target_network)
              339668991  520.487    0.000  520.487    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               53449714  518.416    0.000  518.416    0.000 {method 't' of 'torch._C._TensorBase' objects}
               66012540  514.014    0.000  514.014    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              137704811  150.881    0.000  500.893    0.000 libenv.py:281(_maybe_copy_dict)
                6601254   13.407    0.000  460.328    0.000 loss.py:445(forward)
                6601254   47.660    0.000  446.921    0.000 functional.py:2637(mse_loss)
              413116724  442.597    0.000  442.597    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11228073  165.560    0.000  420.656    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               31171507  360.466    0.000  386.107    0.000 module.py:781(__setattr__)
                6874119   13.503    0.000  385.346    0.000 functional.py:74(split)
               13202508  374.093    0.000  374.093    0.000 {built-in method gather}
                6874119   30.524    0.000  370.944    0.000 tensor.py:460(split)
               45827460   40.776    0.000  367.671    0.000 wrapper.py:22(get_info)
                6874119  338.769    0.000  338.769    0.000 {function Tensor.split at 0x7fd2e74ebd30}
               44028340  336.173    0.000  336.173    0.000 memory.py:17(inner)
                2200418  259.215    0.000  335.128    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
             1216550490  268.664    0.000  333.321    0.000 overrides.py:1086(<genexpr>)
               50973434  328.468    0.000  328.468    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               45827460  172.526    0.000  326.895    0.000 libenv.py:363(get_info)
               45827460  312.739    0.000  312.739    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24656704   23.950    0.000  296.608    0.000 <__array_function__ internals>:2(prod)
               48032460  294.062    0.000  294.062    0.000 {built-in method numpy.array}
                6601254  284.463    0.000  284.463    0.000 {built-in method torch._C._nn.mse_loss}
                   2291   80.925    0.035  283.477    0.124 memory.py:45(update_distribution)
                2201417  272.216    0.000  276.426    0.000 agent.py:149(convert_values)
                6692209   17.848    0.000  270.029    0.000 pooling.py:152(forward)
               24656744   19.060    0.000  268.517    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6692209   11.912    0.000  252.181    0.000 _jit_internal.py:257(fn)
               24656704   30.509    0.000  249.457    0.000 fromnumeric.py:2881(prod)
                6692209   13.562    0.000  239.116    0.000 functional.py:574(_max_pool2d)
                6604251  236.644    0.000  236.644    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                   4582  203.125    0.044  229.877    0.050 {built-in method _pickle.loads}
                6692209  224.782    0.000  224.782    0.000 {built-in method max_pool2d}
               24656704   56.910    0.000  218.947    0.000 fromnumeric.py:70(_wrapreduction)
               13203507  218.116    0.000  218.116    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                2291373   28.551    0.000  206.709    0.000 environments.py:86(<listcomp>)
               26768848  175.675    0.000  196.129    0.000 __init__.py:67(is_acceptable)
                2375531  193.727    0.000  193.727    0.000 {built-in method tensor}
               66012786   87.247    0.000  188.592    0.000 tensor.py:596(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8570467: <MAZE_U_S_0_0returnmaze_0> in cluster <dcc> Done

Job <MAZE_U_S_0_0returnmaze_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Dec 16 20:56:12 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec 17 21:20:24 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec 17 21:20:24 2020
Terminated at Fri Dec 18 20:15:41 2020
Results reported at Fri Dec 18 20:15:41 2020

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

    CPU time :                                   84498.00 sec.
    Max Memory :                                 54752 MB
    Average Memory :                             54059.97 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6688.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82518 sec.
    Turnaround time :                            170369 sec.

The output (if any) is above this job summary.

