
    Name :                      Uncertainty0state_difference0softepsdodgeball-0
    Discount :                  0.995
    Environment :               dodgeball
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13861473926 function calls (13645543025 primitive calls) in 82525.47 seconds

##    Ordered by: cumulative time
   List reduced from 1358 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82525.469 82525.469 {built-in method builtins.exec}
                      1    0.046    0.046 82525.469 82525.469 <string>:1(<module>)
                      1  466.289  466.289 82525.422 82525.422 main.py:92(main)
                2138181  177.411    0.000 53801.409    0.025 agent.py:86(learn)
                2137681  810.290    0.000 52861.484    0.025 agent.py:96(TD_learn)
                2137681  134.239    0.000 23724.638    0.011 memory.py:35(sample_distribution)
                2137681  253.146    0.000 23077.098    0.011 helpers.py:15(stack)
        230889048/14964767  998.767    0.000 15605.332    0.001 module.py:715(_call_impl)
                6413543  212.300    0.000 14423.904    0.002 agent.py:212(forward)
                2138181  204.040    0.000 12530.848    0.006 agent.py:74(chooseMulti)
               21378918 11783.582    0.001 11783.600    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               19240629 10797.541    0.001 10797.541    0.001 {built-in method cat}
               34205896  286.561    0.000 10120.959    0.000 container.py:115(forward)
                6413043   41.948    0.000 9168.535    0.001 grad_mode.py:23(decorate_context)
                6413043  271.275    0.000 9053.785    0.001 adam.py:55(step)
                2138181   58.968    0.000 8572.386    0.004 environments.py:83(step)
                6413043 1684.297    0.000 7776.245    0.001 functional.py:53(adam)
                2138181   90.822    0.000 6978.382    0.003 agent.py:62(rememberMulti)
              288247565 6592.861    0.000 6592.861    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2138181  281.004    0.000 6536.248    0.003 agent.py:66(<listcomp>)
                2138181  140.214    0.000 6135.172    0.003 agent.py:84(<listcomp>)
                6413043   47.192    0.000 6099.775    0.001 tensor.py:181(backward)
                6413043   30.661    0.000 6052.583    0.001 __init__.py:68(backward)
                6413043 5849.303    0.001 5849.303    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               42763620 1278.536    0.000 5604.453    0.000 exploration.py:40(epsintosoftmax)
                2138181   63.471    0.000 5420.926    0.003 environments.py:85(<listcomp>)
               43054303 1244.495    0.000 5398.526    0.000 helpers.py:8(clean)
               49467346 4608.083    0.000 4608.083    0.000 {built-in method as_tensor}
               38481258   74.996    0.000 3710.928    0.000 conv.py:422(forward)
               38481258   85.136    0.000 3603.428    0.000 conv.py:414(_conv_forward)
               38481258 3504.759    0.000 3504.759    0.000 {built-in method conv2d}
               51309344  113.069    0.000 3213.513    0.000 linear.py:92(forward)
               51309344  300.602    0.000 3046.490    0.000 functional.py:1669(linear)
                2138181   45.740    0.000 2886.572    0.001 environments.py:84(<listcomp>)
               42763620  168.753    0.000 2840.832    0.000 interop.py:274(step)
               42763620 1647.520    0.000 2461.244    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6413549  395.195    0.000 2398.340    0.000 rnn.py:110(flatten_parameters)
              448913118 1182.957    0.000 1865.000    0.000 tensor.py:933(grad)
               44894801 1804.666    0.000 1804.666    0.000 {built-in method addmm}
                6413043  179.140    0.000 1795.574    0.000 optimizer.py:167(zero_grad)
                6413543   78.335    0.000 1718.909    0.000 rnn.py:555(forward)
               81238878   72.468    0.000 1686.026    0.000 activation.py:713(forward)
              128260860 1657.964    0.000 1657.964    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               81238878  108.913    0.000 1613.559    0.000 functional.py:1292(leaky_relu)
                6413543 1552.318    0.000 1552.318    0.000 {built-in method lstm}
                6413546 1547.871    0.000 1547.871    0.000 {built-in method _cudnn_rnn_flatten_weight}
               81238878 1495.229    0.000 1495.229    0.000 {built-in method torch._C._nn.leaky_relu}
               42763620   18.475    0.000 1436.146    0.000 wrapper.py:25(act)
               42763620   65.537    0.000 1417.671    0.000 env.py:197(act)
              128260860 1374.420    0.000 1374.420    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               42763620 1310.036    0.000 1314.387    0.000 libenv.py:352(act)
              564353138  319.875    0.000  873.393    0.000 overrides.py:1073(has_torch_function)
               64130430  857.268    0.000  857.268    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               64130430  793.375    0.000  793.375    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               85817923   70.419    0.000  765.981    0.000 extract_dict_ob.py:9(observe)
                   4276    1.555    0.000  762.514    0.178 agent.py:139(update_target_network)
               31601699   65.049    0.000  738.433    0.000 functional.py:1479(softmax)
               64130430  730.672    0.000  730.672    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               85817923   37.029    0.000  695.562    0.000 wrapper.py:19(observe)
               31601699  668.028    0.000  668.028    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               85817923  176.426    0.000  658.533    0.000 libenv.py:344(observe)
               64130430  654.961    0.000  654.961    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               56063362   61.265    0.000  625.414    0.000 <__array_function__ internals>:2(prod)
                2138181    6.140    0.000  609.634    0.000 agent.py:230(avoid_similar_state)
               56063402   46.484    0.000  552.600    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              628488592  218.261    0.000  532.850    0.000 {built-in method builtins.any}
               56063362   72.524    0.000  506.116    0.000 fromnumeric.py:2881(prod)
               51309344  495.787    0.000  495.787    0.000 {method 't' of 'torch._C._TensorBase' objects}
               64130430  494.332    0.000  494.332    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              319732955  473.702    0.000  473.702    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              128581543  140.054    0.000  473.270    0.000 libenv.py:281(_maybe_copy_dict)
                   4276  136.442    0.032  455.432    0.107 memory.py:45(update_distribution)
                6413043   14.411    0.000  435.024    0.000 loss.py:445(forward)
               56063362  134.570    0.000  433.592    0.000 fromnumeric.py:70(_wrapreduction)
                6413043   44.643    0.000  420.613    0.000 functional.py:2637(mse_loss)
              385748905  414.731    0.000  414.731    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6414543   13.140    0.000  405.205    0.000 functional.py:74(split)
                6414543   30.531    0.000  391.285    0.000 tensor.py:460(split)
               44909853  390.582    0.000  390.582    0.000 {built-in method numpy.array}
               42763620  390.506    0.000  390.506    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6414543  359.337    0.000  359.337    0.000 {function Tensor.split at 0x7fca13c6cca0}
               29931369  330.380    0.000  355.405    0.000 module.py:781(__setattr__)
               42763620   37.705    0.000  340.367    0.000 wrapper.py:22(get_info)
             1180015620  246.937    0.000  309.839    0.000 overrides.py:1086(<genexpr>)
               42763620  159.258    0.000  302.662    0.000 libenv.py:363(get_info)
               42763620  298.498    0.000  298.498    0.000 memory.py:17(inner)
                6413043  267.092    0.000  267.092    0.000 {built-in method torch._C._nn.mse_loss}
                2138181  258.329    0.000  266.059    0.000 agent.py:131(convert_values)
               38480258  263.905    0.000  263.905    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2137681  206.643    0.000  262.243    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               58205319  259.356    0.000  259.356    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                   8552  207.510    0.024  256.542    0.030 {built-in method _pickle.loads}
                8550724  256.322    0.000  256.322    0.000 {built-in method gather}
                6413543   18.642    0.000  248.838    0.000 pooling.py:152(forward)
                6413543   11.789    0.000  230.195    0.000 _jit_internal.py:257(fn)
                6414543  223.464    0.000  223.464    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6413543   13.045    0.000  217.385    0.000 functional.py:574(_max_pool2d)
                2138181   25.850    0.000  205.919    0.000 environments.py:86(<listcomp>)
                6413543  203.629    0.000  203.629    0.000 {built-in method max_pool2d}
                2463155  184.009    0.000  184.009    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8483550: <Uncertainty0state_difference0softepsdodgeball_0> in cluster <dcc> Done

Job <Uncertainty0state_difference0softepsdodgeball_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec  6 01:18:09 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Dec  8 12:57:07 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec  8 12:57:07 2020
Terminated at Wed Dec  9 11:52:44 2020
Results reported at Wed Dec  9 11:52:44 2020

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

    CPU time :                                   84087.00 sec.
    Max Memory :                                 54706 MB
    Average Memory :                             54067.64 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6734.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82537 sec.
    Turnaround time :                            297275 sec.

The output (if any) is above this job summary.

