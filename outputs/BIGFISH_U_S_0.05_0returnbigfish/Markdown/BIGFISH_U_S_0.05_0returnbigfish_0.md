[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0.05_0returnbigfish-0
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
    Uncertainty weight :        0.05
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      8888621688 function calls (8684340807 primitive calls) in 82526.20 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82526.196 82526.196 {built-in method builtins.exec}
                      1    0.029    0.029 82526.196 82526.196 <string>:1(<module>)
                      1  592.960  592.960 82526.166 82526.166 main.py:92(main)
                2079143  317.338    0.000 57213.827    0.028 agent.py:84(learn)
                1996184  697.326    0.000 56250.374    0.028 agent.py:99(TD_learn)
                1996184  166.914    0.000 34849.423    0.017 memory.py:35(sample_distribution)
                1996184  309.462    0.000 34108.574    0.017 helpers.py:15(stack)
               18214533 21309.357    0.001 21309.357    0.001 {built-in method cat}
        218331513/14057246  982.744    0.000 13375.006    0.001 module.py:710(_call_impl)
                6071511  194.563    0.000 12381.823    0.002 agent.py:231(forward)
               20211824 12196.765    0.001 12196.801    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2079143  169.617    0.000 10031.759    0.005 agent.py:70(chooseMulti)
              270285002 8744.903    0.000 8744.903    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               32354738  261.766    0.000 8391.222    0.000 container.py:115(forward)
                2079143   66.352    0.000 7888.398    0.004 environments.py:83(step)
                1997183   81.222    0.000 6619.531    0.003 agent.py:58(rememberMulti)
                1997183  192.546    0.000 6182.186    0.003 agent.py:62(<listcomp>)
                5988552   32.545    0.000 5568.193    0.001 grad_mode.py:12(decorate_context)
                5988552 1427.975    0.000 5493.795    0.001 adam.py:51(step)
                2079143   51.775    0.000 5045.777    0.002 environments.py:85(<listcomp>)
               41752065 1364.471    0.000 5017.379    0.000 helpers.py:8(clean)
                5988552   26.363    0.000 4895.170    0.001 tensor.py:155(backward)
                5988552   32.845    0.000 4868.807    0.001 __init__.py:57(backward)
                5988552 4699.731    0.001 4699.731    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               47740617 4269.389    0.000 4269.389    0.000 {built-in method as_tensor}
                1997183   81.217    0.000 4220.190    0.002 agent.py:82(<listcomp>)
               39943660  113.067    0.000 3933.994    0.000 exploration.py:34(epsilonGreedy)
               36429066   67.707    0.000 3127.041    0.000 conv.py:418(forward)
               36429066   79.828    0.000 3026.652    0.000 conv.py:410(_conv_forward)
               36429066 2932.618    0.000 2932.618    0.000 {built-in method conv2d}
                2079143   47.912    0.000 2590.499    0.001 environments.py:84(<listcomp>)
               41582860  165.723    0.000 2542.586    0.000 interop.py:274(step)
               48492126  102.821    0.000 2535.170    0.000 linear.py:90(forward)
               48492126  262.705    0.000 2377.373    0.000 functional.py:1655(linear)
                6071517  340.979    0.000 1893.826    0.000 rnn.py:109(flatten_parameters)
                6071511   77.050    0.000 1863.305    0.000 rnn.py:550(forward)
                6071511 1697.163    0.000 1697.163    0.000 {built-in method lstm}
               42500577 1395.478    0.000 1395.478    0.000 {built-in method addmm}
               76852498   81.810    0.000 1315.762    0.000 activation.py:653(forward)
               76852498  112.958    0.000 1233.952    0.000 functional.py:1277(leaky_relu)
               41582860   20.935    0.000 1119.898    0.000 wrapper.py:25(act)
               76852498 1110.444    0.000 1110.444    0.000 {built-in method torch._C._nn.leaky_relu}
                6071514 1109.105    0.000 1109.105    0.000 {built-in method _cudnn_rnn_flatten_weight}
               41582860   53.971    0.000 1098.964    0.000 env.py:197(act)
              119771040 1024.009    0.000 1024.009    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               41582860 1010.822    0.000 1014.844    0.000 libenv.py:352(act)
              119771040  878.777    0.000  878.777    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               83334925   65.958    0.000  781.036    0.000 extract_dict_ob.py:9(observe)
               83334925   39.106    0.000  715.078    0.000 wrapper.py:19(observe)
               83334925  171.184    0.000  675.972    0.000 libenv.py:344(observe)
                   2079    1.159    0.001  646.115    0.311 agent.py:157(update_target_network)
               59885520  626.654    0.000  626.654    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               59885520  527.645    0.000  527.645    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5988552   93.934    0.000  519.375    0.000 optimizer.py:166(zero_grad)
              124917785  136.331    0.000  507.322    0.000 libenv.py:281(_maybe_copy_dict)
                1997183    5.283    0.000  480.716    0.000 agent.py:249(avoid_similar_state)
              374755434  447.066    0.000  447.066    0.000 {method 'copy' of 'numpy.ndarray' objects}
               39943660  418.392    0.000  418.392    0.000 memory.py:17(inner)
               59885520  418.391    0.000  418.391    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               28280247  386.850    0.000  409.042    0.000 module.py:774(__setattr__)
               59885520  403.813    0.000  403.813    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              307409038  388.800    0.000  388.800    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                5988552   12.920    0.000  382.170    0.000 loss.py:444(forward)
                5988552   50.410    0.000  369.250    0.000 functional.py:2621(mse_loss)
               11019854  138.270    0.000  365.143    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                   2079   94.856    0.046  363.657    0.175 memory.py:45(update_distribution)
               48492126  351.124    0.000  351.124    0.000 {method 't' of 'torch._C._TensorBase' objects}
               41582860   38.512    0.000  342.930    0.000 wrapper.py:22(get_info)
               43583202  340.734    0.000  340.734    0.000 {built-in method numpy.array}
               41582860  156.773    0.000  304.418    0.000 libenv.py:363(get_info)
                1996184  226.122    0.000  295.000    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               59885520  287.039    0.000  287.039    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11977104  269.969    0.000  269.969    0.000 {built-in method gather}
               24036032   23.320    0.000  266.908    0.000 <__array_function__ internals>:2(prod)
                   4158  232.901    0.056  256.321    0.062 {built-in method _pickle.loads}
               24036072   17.765    0.000  239.438    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6237429   11.864    0.000  239.221    0.000 functional.py:68(split)
               46244068  235.556    0.000  235.556    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6237429   12.337    0.000  226.441    0.000 tensor.py:367(split)
                1997183  186.849    0.000  222.454    0.000 agent.py:149(convert_values)
               24036032   30.902    0.000  221.673    0.000 fromnumeric.py:2881(prod)
              299427708  189.909    0.000  218.963    0.000 tensor.py:725(grad)
                6071511   19.604    0.000  216.858    0.000 pooling.py:156(forward)
                2155185  216.288    0.000  216.288    0.000 {built-in method tensor}
                6237429  212.736    0.000  212.736    0.000 {function Tensor.split at 0x7fe43be4e9d0}
               41582860  212.161    0.000  212.161    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24286056  190.769    0.000  211.267    0.000 __init__.py:66(is_acceptable)
                5988552  209.622    0.000  209.622    0.000 {built-in method torch._C._nn.mse_loss}
                6071511   11.728    0.000  197.254    0.000 _jit_internal.py:237(fn)
               24036032   56.319    0.000  190.771    0.000 fromnumeric.py:70(_wrapreduction)
                2079143   24.020    0.000  185.770    0.000 environments.py:86(<listcomp>)
                6071511   13.030    0.000  184.510    0.000 functional.py:564(_max_pool2d)
                1996184  177.384    0.000  177.384    0.000 memory.py:43(<listcomp>)
                5991549  173.835    0.000  173.835    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6071511  170.704    0.000  170.704    0.000 {built-in method max_pool2d}
               41582880   31.085    0.000  161.773    0.000 environments.py:89(reset)
              214507092  159.972    0.000  160.063    0.000 module.py:758(__getattr__)
                2079143   16.185    0.000  149.245    0.000 collector.py:8(collect)
               11978103  147.808    0.000  147.808    0.000 {method 'type' of 'torch._C._TensorBase' objects}
               26034295  142.579    0.000  142.579    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8557626: <BIGFISH_U_S_0.05_0returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0.05_0returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:47 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Dec 14 14:46:09 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec 14 14:46:09 2020
Terminated at Tue Dec 15 13:41:49 2020
Results reported at Tue Dec 15 13:41:49 2020

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

    CPU time :                                   92225.00 sec.
    Max Memory :                                 53965 MB
    Average Memory :                             53311.86 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7475.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82541 sec.
    Turnaround time :                            337202 sec.

The output (if any) is above this job summary.

