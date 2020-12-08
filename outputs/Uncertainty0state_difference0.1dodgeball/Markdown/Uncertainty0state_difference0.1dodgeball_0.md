
    Name :                      Uncertainty0state_difference0.1dodgeball-0
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
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11111216217 function calls (10928496641 primitive calls) in 82516.07 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82516.067 82516.067 {built-in method builtins.exec}
                      1    0.034    0.034 82516.067 82516.067 <string>:1(<module>)
                      1  577.457  577.457 82516.032 82516.032 main.py:92(main)
                1809356  231.865    0.000 58649.416    0.032 agent.py:86(learn)
                1808856  629.136    0.000 57437.779    0.032 agent.py:96(TD_learn)
                1808856  154.189    0.000 35503.757    0.020 memory.py:35(sample_distribution)
                1808856  315.301    0.000 34805.990    0.019 helpers.py:15(stack)
               16281204 22783.679    0.001 22783.679    0.001 {built-in method cat}
        195375948/12662992  891.396    0.000 12790.279    0.001 module.py:715(_call_impl)
                5427068  177.744    0.000 11833.506    0.002 agent.py:212(forward)
               18090668 11285.841    0.001 11285.843    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                1809356  159.527    0.000 8936.860    0.005 agent.py:74(chooseMulti)
               28944696  225.615    0.000 8090.992    0.000 container.py:115(forward)
              242527874 7983.455    0.000 7983.455    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1809356   60.476    0.000 7720.599    0.004 environments.py:83(step)
                1809356   74.784    0.000 6481.623    0.004 agent.py:62(rememberMulti)
                5426568   36.938    0.000 6155.337    0.001 grad_mode.py:23(decorate_context)
                1809356  194.217    0.000 6078.284    0.003 agent.py:66(<listcomp>)
                5426568  240.549    0.000 6056.381    0.001 adam.py:55(step)
                5426568 1157.403    0.000 4985.340    0.001 functional.py:53(adam)
               36566900 1238.209    0.000 4805.499    0.000 helpers.py:8(clean)
                1809356   50.019    0.000 4799.499    0.003 environments.py:85(<listcomp>)
                5426568   41.342    0.000 4651.343    0.001 tensor.py:181(backward)
                5426568   25.175    0.000 4610.000    0.001 __init__.py:68(backward)
                5426568 4450.417    0.001 4450.417    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               41993468 4153.326    0.000 4153.326    0.000 {built-in method as_tensor}
                1809356   73.780    0.000 3551.458    0.002 agent.py:84(<listcomp>)
               36187120  105.445    0.000 3274.784    0.000 exploration.py:34(epsilonGreedy)
               32562408   60.555    0.000 3003.660    0.000 conv.py:422(forward)
               32562408   79.828    0.000 2912.689    0.000 conv.py:414(_conv_forward)
               32562408 2818.663    0.000 2818.663    0.000 {built-in method conv2d}
                1809356   40.747    0.000 2644.611    0.001 environments.py:84(<listcomp>)
               36187120  144.011    0.000 2603.864    0.000 interop.py:274(step)
               43417544   96.037    0.000 2533.391    0.000 linear.py:92(forward)
               43417544  240.418    0.000 2385.816    0.000 functional.py:1669(linear)
                5427074  339.245    0.000 1828.678    0.000 rnn.py:110(flatten_parameters)
                5427068   70.075    0.000 1734.119    0.000 rnn.py:555(forward)
                5427068 1582.742    0.000 1582.742    0.000 {built-in method lstm}
              379859868  874.334    0.000 1476.408    0.000 tensor.py:933(grad)
               37989476 1378.625    0.000 1378.625    0.000 {built-in method addmm}
               36187120   18.621    0.000 1336.190    0.000 wrapper.py:25(act)
               36187120   48.069    0.000 1317.569    0.000 env.py:197(act)
               68743528   67.420    0.000 1277.797    0.000 activation.py:713(forward)
                5426568  123.708    0.000 1272.194    0.000 optimizer.py:167(zero_grad)
               36187120 1239.930    0.000 1243.518    0.000 libenv.py:352(act)
               68743528   97.230    0.000 1210.377    0.000 functional.py:1292(leaky_relu)
               68743528 1104.108    0.000 1104.108    0.000 {built-in method torch._C._nn.leaky_relu}
                5427071 1074.459    0.000 1074.459    0.000 {built-in method _cudnn_rnn_flatten_weight}
              108531360 1011.656    0.000 1011.656    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   3618    2.203    0.001  979.772    0.271 agent.py:139(update_target_network)
              108531360  833.278    0.000  833.278    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              477543338  259.287    0.000  772.423    0.000 overrides.py:1073(has_torch_function)
               72754020   56.258    0.000  716.626    0.000 extract_dict_ob.py:9(observe)
               72754020   33.339    0.000  660.368    0.000 wrapper.py:19(observe)
                   3618  164.627    0.046  634.965    0.176 memory.py:45(update_distribution)
               72754020  149.567    0.000  627.029    0.000 libenv.py:344(observe)
               54265680  564.637    0.000  564.637    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               38003212  530.332    0.000  530.332    0.000 {built-in method numpy.array}
               54265680  524.671    0.000  524.671    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              531814042  194.850    0.000  487.800    0.000 {built-in method builtins.any}
                1809356    5.170    0.000  482.619    0.000 agent.py:230(avoid_similar_state)
              108941140  123.250    0.000  480.178    0.000 libenv.py:281(_maybe_copy_dict)
               54265680  469.794    0.000  469.794    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               36187120  450.149    0.000  450.149    0.000 memory.py:17(inner)
              326827038  426.121    0.000  426.121    0.000 {method 'copy' of 'numpy.ndarray' objects}
               54265680  406.371    0.000  406.371    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5428068   11.328    0.000  401.157    0.000 functional.py:74(split)
               25327819  371.891    0.000  394.122    0.000 module.py:781(__setattr__)
                5428068   25.555    0.000  389.059    0.000 tensor.py:460(split)
               43417544  383.552    0.000  383.552    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5428068  362.270    0.000  362.270    0.000 {function Tensor.split at 0x7f4a52570d30}
               10836248  132.741    0.000  354.428    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                5426568   11.341    0.000  352.532    0.000 loss.py:445(forward)
                5426568   41.984    0.000  341.191    0.000 functional.py:2637(mse_loss)
              268902695  311.802    0.000  311.802    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               36187120   33.468    0.000  302.935    0.000 wrapper.py:22(get_info)
                   7236  246.917    0.034  290.990    0.040 {built-in method _pickle.loads}
              998504220  227.104    0.000  288.475    0.000 overrides.py:1086(<genexpr>)
               54265680  287.717    0.000  287.717    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               36187120  137.343    0.000  269.467    0.000 libenv.py:363(get_info)
                1808856  206.195    0.000  268.955    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               23481492   23.276    0.000  258.077    0.000 <__array_function__ internals>:2(prod)
               23481532   17.041    0.000  230.649    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                1809356  190.268    0.000  220.068    0.000 agent.py:131(convert_values)
                1809356   21.377    0.000  216.014    0.000 environments.py:86(<listcomp>)
               23481492   28.715    0.000  213.608    0.000 fromnumeric.py:2881(prod)
                5426568  207.857    0.000  207.857    0.000 {built-in method torch._C._nn.mse_loss}
                5427068   15.166    0.000  207.344    0.000 pooling.py:152(forward)
               36187120  202.894    0.000  202.894    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7235424  199.298    0.000  199.298    0.000 {built-in method gather}
               32561408  197.404    0.000  197.404    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               36187140   30.175    0.000  194.641    0.000 environments.py:89(reset)
                2084322  192.321    0.000  192.321    0.000 {built-in method tensor}
                5427068   10.562    0.000  192.178    0.000 _jit_internal.py:257(fn)
               23481492   54.441    0.000  184.893    0.000 fromnumeric.py:70(_wrapreduction)
                1808856  182.175    0.000  182.175    0.000 memory.py:43(<listcomp>)
                5428068  181.830    0.000  181.830    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                5427068   10.983    0.000  180.681    0.000 functional.py:574(_max_pool2d)
                5427068  168.998    0.000  168.998    0.000 {built-in method max_pool2d}
               21708284  147.260    0.000  165.500    0.000 __init__.py:67(is_acceptable)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8483546: <Uncertainty0state_difference0.1dodgeball_0> in cluster <dcc> Done

Job <Uncertainty0state_difference0.1dodgeball_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec  6 01:18:08 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Dec  6 11:09:46 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec  6 11:09:46 2020
Terminated at Mon Dec  7 10:05:12 2020
Results reported at Mon Dec  7 10:05:12 2020

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

    CPU time :                                   93293.00 sec.
    Max Memory :                                 54593 MB
    Average Memory :                             53950.92 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6847.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82528 sec.
    Turnaround time :                            118024 sec.

The output (if any) is above this job summary.

