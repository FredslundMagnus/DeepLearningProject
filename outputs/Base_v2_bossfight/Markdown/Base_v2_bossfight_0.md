[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_bossfight-0
    Discount :                  0.995
    Environment :               bossfight
    Hours :                     24
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      8982310290 function calls (8785796988 primitive calls) in 86154.81 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86154.807 86154.807 {built-in method builtins.exec}
                      1    0.068    0.068 86154.807 86154.807 <string>:1(<module>)
                      1  511.274  511.274 86154.737 86154.737 main.py:11(main)
                2585995  100.263    0.000 53390.448    0.021 agent.py:46(learn)
                2585495  325.336    0.000 52447.850    0.020 agent.py:54(TD_learn)
                2585495  188.906    0.000 31629.579    0.012 memory.py:27(sample_distribution)
                2585495  336.974    0.000 30754.183    0.012 helpers.py:12(stack)
              350430376 15547.672    0.000 15547.672    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               23270955 15108.458    0.001 15108.458    0.001 {built-in method cat}
               23271009 14894.225    0.001 14894.229    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        209435095/12927975  926.353    0.000 14762.766    0.001 module.py:710(_call_impl)
                2585995   39.557    0.000 14711.561    0.006 agent.py:41(chooseMulti)
               10342480  222.834    0.000 14479.166    0.001 agent.py:119(forward)
                2585995  103.926    0.000 10494.740    0.004 agent.py:44(<listcomp>)
                2585995   72.848    0.000 10322.791    0.004 environments.py:73(step)
               51719900  144.870    0.000 10148.821    0.000 exploration.py:33(epsilonGreedy)
               31027440  227.114    0.000 8224.723    0.000 container.py:115(forward)
                2585995    8.190    0.000 6983.974    0.003 agent.py:32(rememberMulti)
                2585995  225.521    0.000 6975.783    0.003 agent.py:33(<listcomp>)
                2585995   49.542    0.000 5664.318    0.002 environments.py:75(<listcomp>)
               52018848 1521.005    0.000 5652.319    0.000 helpers.py:8(clean)
               62054880  106.387    0.000 4912.867    0.000 conv.py:418(forward)
               59775333 4844.868    0.000 4844.868    0.000 {built-in method as_tensor}
               62054880  144.656    0.000 4757.841    0.000 conv.py:410(_conv_forward)
               62054880 4589.856    0.000 4589.856    0.000 {built-in method conv2d}
                2585995   54.849    0.000 4364.459    0.002 environments.py:74(<listcomp>)
               51719900  205.770    0.000 4309.610    0.000 interop.py:274(step)
                2585495   14.668    0.000 4070.086    0.002 tensor.py:155(backward)
                2585495   18.079    0.000 4055.418    0.002 __init__.py:57(backward)
                2585495   16.476    0.000 4034.785    0.002 grad_mode.py:12(decorate_context)
                2585495 1016.717    0.000 3998.981    0.002 adam.py:51(step)
                2585495 3970.558    0.002 3970.558    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10342486  510.902    0.000 2847.138    0.000 rnn.py:109(flatten_parameters)
               10342480  113.351    0.000 2648.050    0.000 rnn.py:550(forward)
               51719900   25.990    0.000 2600.664    0.000 wrapper.py:25(act)
               51719900   66.589    0.000 2574.674    0.000 env.py:197(act)
               51719900 2468.142    0.000 2473.174    0.000 libenv.py:352(act)
               10342480 2393.899    0.000 2393.899    0.000 {built-in method lstm}
               10342483 1737.795    0.000 1737.795    0.000 {built-in method _cudnn_rnn_flatten_weight}
               72397360   71.488    0.000 1228.998    0.000 activation.py:653(forward)
               72397360  114.557    0.000 1157.510    0.000 functional.py:1277(leaky_relu)
               72397360 1032.488    0.000 1032.488    0.000 {built-in method torch._C._nn.leaky_relu}
              103738748   81.124    0.000  929.519    0.000 extract_dict_ob.py:9(observe)
              103738748   47.711    0.000  848.395    0.000 wrapper.py:19(observe)
                   5171    1.371    0.000  842.335    0.163 agent.py:81(update_target_network)
              103738748  202.190    0.000  800.684    0.000 libenv.py:344(observe)
                   5171  198.729    0.038  777.607    0.150 memory.py:37(update_distribution)
               93077820  744.619    0.000  744.619    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               54315737  666.367    0.000  666.367    0.000 {built-in method numpy.array}
               10342480   27.508    0.000  662.491    0.000 linear.py:90(forward)
               93077820  651.482    0.000  651.482    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10342480   57.106    0.000  624.281    0.000 functional.py:1655(linear)
              155458648  178.356    0.000  587.924    0.000 libenv.py:281(_maybe_copy_dict)
               41370900  509.902    0.000  538.997    0.000 module.py:774(__setattr__)
              466381115  501.201    0.000  501.201    0.000 {method 'copy' of 'numpy.ndarray' objects}
               46538910  455.196    0.000  455.196    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               51719900   45.860    0.000  416.830    0.000 wrapper.py:22(get_info)
               10342480  414.330    0.000  414.330    0.000 {built-in method addmm}
              362759995  396.246    0.000  396.246    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11608924  152.141    0.000  392.823    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               51719900  392.078    0.000  392.078    0.000 memory.py:15(inner)
               46538910  383.563    0.000  383.563    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2585495   66.140    0.000  373.865    0.000 optimizer.py:166(zero_grad)
               51719900  188.071    0.000  370.970    0.000 libenv.py:363(get_info)
                2585495  280.747    0.000  364.733    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               10342480   25.283    0.000  328.900    0.000 pooling.py:156(forward)
               46538910  308.684    0.000  308.684    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10342480   17.682    0.000  303.617    0.000 _jit_internal.py:237(fn)
               46538910  296.425    0.000  296.425    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               25803483   25.408    0.000  287.252    0.000 <__array_function__ internals>:2(prod)
               10342480   21.188    0.000  284.228    0.000 functional.py:564(_max_pool2d)
                7757985   13.889    0.000  264.945    0.000 functional.py:68(split)
               41369932  233.841    0.000  262.710    0.000 __init__.py:66(is_acceptable)
               10342480  261.641    0.000  261.641    0.000 {built-in method max_pool2d}
               25803523   19.441    0.000  257.523    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7757985   13.528    0.000  249.986    0.000 tensor.py:367(split)
               51719900  241.994    0.000  241.994    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25803483   32.202    0.000  238.082    0.000 fromnumeric.py:2881(prod)
                7757985  235.127    0.000  235.127    0.000 {function Tensor.split at 0x7f812d4e4940}
                2585995   30.700    0.000  221.166    0.000 environments.py:76(<listcomp>)
                2585495  218.669    0.000  218.669    0.000 memory.py:35(<listcomp>)
               46538910  208.868    0.000  208.868    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               25803483   60.679    0.000  205.880    0.000 fromnumeric.py:70(_wrapreduction)
               51719920   32.971    0.000  190.506    0.000 environments.py:79(reset)
              207477496   72.915    0.000  176.262    0.000 libenv.py:271(_maybe_copy_ndarray)
                2585995   16.046    0.000  174.980    0.000 collector.py:7(collect)
                2585495    7.228    0.000  173.494    0.000 loss.py:444(forward)
                2585495   25.080    0.000  166.266    0.000 functional.py:2621(mse_loss)
              232694604  141.137    0.000  163.934    0.000 tensor.py:725(grad)
                5171991  157.744    0.000  157.744    0.000 {built-in method builtins.sum}
               25855950  156.782    0.000  156.782    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               28394149  154.744    0.000  154.744    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              196714309  149.433    0.000  149.559    0.000 module.py:758(__getattr__)
              209435095  134.970    0.000  134.970    0.000 {built-in method torch._C._get_tracing_state}
                5170990  128.364    0.000  128.364    0.000 {built-in method gather}
                2585495   93.831    0.000   93.831    0.000 {built-in method torch._C._nn.mse_loss}
               10342480   30.023    0.000   91.477    0.000 rnn.py:524(check_forward_args)
               10342480   89.273    0.000   89.273    0.000 {method 't' of 'torch._C._TensorBase' objects}
              868767820   83.970    0.000   83.970    0.000 {method 'values' of 'collections.OrderedDict' objects}
               52018888   39.877    0.000   81.027    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 8411692: <Base_v2_bossfight_0> in cluster <dcc> Done

Job <Base_v2_bossfight_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Sun Nov 22 15:16:12 2020
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Nov 22 19:22:36 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov 22 19:22:36 2020
Terminated at Mon Nov 23 19:18:55 2020
Results reported at Mon Nov 23 19:18:55 2020

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

    CPU time :                                   92266.00 sec.
    Max Memory :                                 55380 MB
    Average Memory :                             54606.98 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6060.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86178 sec.
    Turnaround time :                            100963 sec.

The output (if any) is above this job summary.

  File "main.py", line 10
    if 12321 ===!! asdasd:
               ^
SyntaxError: invalid syntax

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 8416076: <Base_v2_bossfight_0> in cluster <dcc> Exited

Job <Base_v2_bossfight_0> was submitted from host <n-62-27-20> by user <s183914> in cluster <dcc> at Mon Nov 23 22:15:24 2020
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Nov 23 23:50:54 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 23 23:50:54 2020
Terminated at Mon Nov 23 23:50:57 2020
Results reported at Mon Nov 23 23:50:57 2020

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

    CPU time :                                   0.26 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   3 sec.
    Turnaround time :                            5733 sec.

The output (if any) is above this job summary.

