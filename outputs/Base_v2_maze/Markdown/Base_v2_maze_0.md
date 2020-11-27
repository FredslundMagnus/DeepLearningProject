[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_maze-0
    Discount :                  0.995
    Environment :               maze
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


      9230044049 function calls (9027969143 primitive calls) in 86120.40 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86120.396 86120.396 {built-in method builtins.exec}
                      1    0.109    0.109 86120.396 86120.396 <string>:1(<module>)
                      1  480.005  480.005 86120.284 86120.284 main.py:12(main)
                2659174  100.776    0.000 53942.143    0.020 agent.py:46(learn)
                2658674  392.510    0.000 53100.540    0.020 agent.py:54(TD_learn)
                2658674  181.702    0.000 27923.938    0.011 memory.py:27(sample_distribution)
                2658674  290.302    0.000 27055.204    0.010 helpers.py:12(stack)
        215362594/13293870  915.573    0.000 16751.342    0.001 module.py:710(_call_impl)
               10635196  246.552    0.000 16448.597    0.002 agent.py:119(forward)
              360594768 14432.528    0.000 14432.528    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               23929620 14284.102    0.001 14284.109    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2659174   43.689    0.000 13811.563    0.005 agent.py:41(chooseMulti)
               23929566 12112.921    0.001 12112.921    0.001 {built-in method cat}
                2659174   73.100    0.000 9869.797    0.004 environments.py:73(step)
               31905588  267.293    0.000 9444.976    0.000 container.py:115(forward)
                2659174  124.351    0.000 9032.742    0.003 agent.py:44(<listcomp>)
               53183480  181.094    0.000 8586.392    0.000 exploration.py:33(epsilonGreedy)
                2659174    8.281    0.000 7812.029    0.003 agent.py:32(rememberMulti)
                2659174  334.882    0.000 7803.748    0.003 agent.py:33(<listcomp>)
                2659174   55.109    0.000 6117.191    0.002 environments.py:75(<listcomp>)
               53353196 1500.878    0.000 6084.552    0.000 helpers.py:8(clean)
                2658674   17.761    0.000 5784.531    0.002 grad_mode.py:12(decorate_context)
                2658674 1377.791    0.001 5746.042    0.002 adam.py:51(step)
               63811176  110.030    0.000 5659.597    0.000 conv.py:418(forward)
               63811176  125.370    0.000 5502.676    0.000 conv.py:410(_conv_forward)
               63811176 5356.338    0.000 5356.338    0.000 {built-in method conv2d}
               61329218 5269.280    0.000 5269.280    0.000 {built-in method as_tensor}
                2658674   17.523    0.000 4886.069    0.002 tensor.py:155(backward)
                2658674   18.574    0.000 4868.546    0.002 __init__.py:57(backward)
                2658674 4775.213    0.002 4775.213    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10635202  526.697    0.000 3483.582    0.000 rnn.py:109(flatten_parameters)
                2659174   56.628    0.000 3462.091    0.001 environments.py:74(<listcomp>)
               53183480  210.447    0.000 3405.463    0.000 interop.py:274(step)
               10635196  114.003    0.000 2701.615    0.000 rnn.py:550(forward)
               10635196 2442.495    0.000 2442.495    0.000 {built-in method lstm}
               10635199 2328.393    0.000 2328.393    0.000 {built-in method _cudnn_rnn_flatten_weight}
               53183480   24.221    0.000 1691.856    0.000 wrapper.py:25(act)
               53183480   73.365    0.000 1667.636    0.000 env.py:197(act)
               53183480 1544.120    0.000 1548.861    0.000 libenv.py:352(act)
               74446372   69.974    0.000 1508.124    0.000 activation.py:653(forward)
               74446372  111.529    0.000 1438.151    0.000 functional.py:1277(leaky_relu)
               74446372 1316.749    0.000 1316.749    0.000 {built-in method torch._C._nn.leaky_relu}
               95712264 1142.072    0.000 1142.072    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               95712264 1007.524    0.000 1007.524    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              106536676   84.641    0.000  905.248    0.000 extract_dict_ob.py:9(observe)
              106536676   45.390    0.000  820.607    0.000 wrapper.py:19(observe)
              106536676  205.261    0.000  775.217    0.000 libenv.py:344(observe)
               10635196   32.497    0.000  762.353    0.000 linear.py:90(forward)
                   5318    1.251    0.000  740.828    0.139 agent.py:81(update_target_network)
               10635196   59.429    0.000  718.743    0.000 functional.py:1655(linear)
                   5318  190.544    0.036  675.216    0.127 memory.py:37(update_distribution)
               47856132  627.463    0.000  627.463    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              373548746  591.794    0.000  591.794    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               55852790  580.195    0.000  580.195    0.000 {built-in method numpy.array}
                2658674   85.189    0.000  564.541    0.000 optimizer.py:166(zero_grad)
              159720156  171.638    0.000  558.739    0.000 libenv.py:281(_maybe_copy_dict)
               42541764  506.052    0.000  534.886    0.000 module.py:774(__setattr__)
               47856132  530.034    0.000  530.034    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              479165786  494.401    0.000  494.401    0.000 {method 'copy' of 'numpy.ndarray' objects}
               10635196  489.142    0.000  489.142    0.000 {built-in method addmm}
               47856132  458.136    0.000  458.136    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47856132  451.577    0.000  451.577    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               53183480   48.547    0.000  424.082    0.000 wrapper.py:22(get_info)
               11689592  164.377    0.000  420.288    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               53183480  400.310    0.000  400.310    0.000 memory.py:15(inner)
                2658674  294.687    0.000  385.390    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               53183480  194.661    0.000  375.536    0.000 libenv.py:363(get_info)
               10635196   23.948    0.000  366.807    0.000 pooling.py:156(forward)
               47856132  349.226    0.000  349.226    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10635196   16.946    0.000  342.859    0.000 _jit_internal.py:237(fn)
               10635196   19.610    0.000  324.160    0.000 functional.py:564(_max_pool2d)
               53183480  321.999    0.000  321.999    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               26037998   25.547    0.000  307.244    0.000 <__array_function__ internals>:2(prod)
               10635196  303.274    0.000  303.274    0.000 {built-in method max_pool2d}
               42540796  255.115    0.000  284.265    0.000 __init__.py:66(is_acceptable)
               26038038   20.786    0.000  277.551    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7977522   14.095    0.000  268.182    0.000 functional.py:68(split)
               26037998   32.661    0.000  256.766    0.000 fromnumeric.py:2881(prod)
                7977522   14.441    0.000  253.144    0.000 tensor.py:367(split)
                7977522  237.224    0.000  237.224    0.000 {function Tensor.split at 0x7f032427d940}
               26037998   61.207    0.000  224.105    0.000 fromnumeric.py:70(_wrapreduction)
                2659174   29.835    0.000  217.415    0.000 environments.py:76(<listcomp>)
                2658674  198.567    0.000  198.567    0.000 memory.py:35(<listcomp>)
               26587740  195.470    0.000  195.470    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2658674    6.804    0.000  192.312    0.000 loss.py:444(forward)
               53183500   31.733    0.000  187.594    0.000 environments.py:79(reset)
                2658674   25.886    0.000  185.508    0.000 functional.py:2621(mse_loss)
              239280714  157.827    0.000  183.550    0.000 tensor.py:725(grad)
                2659174   17.148    0.000  177.776    0.000 collector.py:7(collect)
              213073352   54.787    0.000  174.942    0.000 libenv.py:271(_maybe_copy_ndarray)
               28701990  172.743    0.000  172.743    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              215362594  163.953    0.000  163.953    0.000 {built-in method torch._C._get_tracing_state}
                5318349  159.425    0.000  159.426    0.000 {built-in method builtins.sum}
                5317348  155.426    0.000  155.426    0.000 {built-in method gather}
              202281793  146.384    0.000  146.499    0.000 module.py:758(__getattr__)
                2658674  111.279    0.000  111.279    0.000 {built-in method torch._C._nn.mse_loss}
               10635196  108.098    0.000  108.098    0.000 {method 't' of 'torch._C._TensorBase' objects}
               10635196   29.972    0.000   92.612    0.000 rnn.py:524(check_forward_args)
              893355964   83.983    0.000   83.983    0.000 {method 'values' of 'collections.OrderedDict' objects}
               53353236   40.603    0.000   83.323    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8423564: <Base_v2_maze_0> in cluster <dcc> Done

Job <Base_v2_maze_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue Nov 24 19:48:57 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 25 23:59:02 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 25 23:59:02 2020
Terminated at Thu Nov 26 23:54:30 2020
Results reported at Thu Nov 26 23:54:30 2020

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

    CPU time :                                   90386.00 sec.
    Max Memory :                                 56997 MB
    Average Memory :                             56235.56 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4443.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86128 sec.
    Turnaround time :                            187533 sec.

The output (if any) is above this job summary.

