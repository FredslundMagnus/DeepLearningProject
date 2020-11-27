[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_climber-0
    Discount :                  0.995
    Environment :               climber
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


      9055624784 function calls (8857386510 primitive calls) in 86132.80 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86132.800 86132.800 {built-in method builtins.exec}
                      1    0.052    0.052 86132.800 86132.800 <string>:1(<module>)
                      1  507.370  507.370 86132.747 86132.747 main.py:11(main)
                2608692  102.716    0.000 53860.017    0.021 agent.py:46(learn)
                2608192  327.621    0.000 52896.009    0.020 agent.py:54(TD_learn)
                2608192  195.235    0.000 32102.455    0.012 memory.py:27(sample_distribution)
                2608192  328.284    0.000 31207.645    0.012 helpers.py:12(stack)
              353585186 15992.875    0.000 15992.875    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               23475228 15326.112    0.001 15326.112    0.001 {built-in method cat}
                2608692   41.127    0.000 15140.903    0.006 agent.py:41(chooseMulti)
               23475282 15110.727    0.001 15110.741    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        211273552/13041460  919.382    0.000 14664.933    0.001 module.py:710(_call_impl)
               10433268  215.213    0.000 14377.713    0.001 agent.py:119(forward)
                2608692  102.515    0.000 10932.780    0.004 agent.py:44(<listcomp>)
               52173840  147.500    0.000 10586.414    0.000 exploration.py:33(epsilonGreedy)
                2608692   73.000    0.000 9419.061    0.004 environments.py:73(step)
               31299804  232.000    0.000 8142.656    0.000 container.py:115(forward)
                2608692    8.259    0.000 6992.333    0.003 agent.py:32(rememberMulti)
                2608692  226.328    0.000 6984.074    0.003 agent.py:33(<listcomp>)
                2608692   53.540    0.000 5758.878    0.002 environments.py:75(<listcomp>)
               52258148 1533.983    0.000 5716.237    0.000 helpers.py:8(clean)
               60082724 4923.197    0.000 4923.197    0.000 {built-in method as_tensor}
               62599608  109.934    0.000 4862.828    0.000 conv.py:418(forward)
               62599608  122.941    0.000 4704.403    0.000 conv.py:410(_conv_forward)
               62599608 4558.481    0.000 4558.481    0.000 {built-in method conv2d}
                2608192   16.252    0.000 4097.609    0.002 grad_mode.py:12(decorate_context)
                2608192 1030.417    0.000 4061.300    0.002 adam.py:51(step)
                2608192   14.921    0.000 4037.795    0.002 tensor.py:155(backward)
                2608192   19.600    0.000 4022.874    0.002 __init__.py:57(backward)
                2608192 3935.081    0.002 3935.081    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2608692   57.007    0.000 3404.148    0.001 environments.py:74(<listcomp>)
               52173840  197.707    0.000 3347.142    0.000 interop.py:274(step)
               10433274  506.152    0.000 2813.725    0.000 rnn.py:109(flatten_parameters)
               10433268  114.210    0.000 2666.162    0.000 rnn.py:550(forward)
               10433268 2408.264    0.000 2408.264    0.000 {built-in method lstm}
               10433271 1709.192    0.000 1709.192    0.000 {built-in method _cudnn_rnn_flatten_weight}
               52173840   26.514    0.000 1680.202    0.000 wrapper.py:25(act)
               52173840   65.120    0.000 1653.687    0.000 env.py:197(act)
               52173840 1546.693    0.000 1551.640    0.000 libenv.py:352(act)
               73032876   70.580    0.000 1205.265    0.000 activation.py:653(forward)
               73032876  105.813    0.000 1134.685    0.000 functional.py:1277(leaky_relu)
               73032876 1018.293    0.000 1018.293    0.000 {built-in method torch._C._nn.leaky_relu}
              104431988   78.408    0.000  898.976    0.000 extract_dict_ob.py:9(observe)
                   5217    1.448    0.000  861.292    0.165 agent.py:81(update_target_network)
              104431988   53.974    0.000  820.568    0.000 wrapper.py:19(observe)
                   5217  201.213    0.039  795.531    0.152 memory.py:37(update_distribution)
              104431988  207.630    0.000  766.594    0.000 libenv.py:344(observe)
               93894912  753.942    0.000  753.942    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               54792466  680.714    0.000  680.714    0.000 {built-in method numpy.array}
               93894912  666.737    0.000  666.737    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10433268   29.920    0.000  664.670    0.000 linear.py:90(forward)
               10433268   58.332    0.000  622.979    0.000 functional.py:1655(linear)
              156605828  166.441    0.000  564.212    0.000 libenv.py:281(_maybe_copy_dict)
               41734052  519.437    0.000  548.872    0.000 module.py:774(__setattr__)
              469822701  489.085    0.000  489.085    0.000 {method 'copy' of 'numpy.ndarray' objects}
               46947456  458.574    0.000  458.574    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10433268  414.062    0.000  414.062    0.000 {built-in method addmm}
               52173840   44.878    0.000  405.993    0.000 wrapper.py:22(get_info)
              366457570  404.278    0.000  404.278    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11631694  153.001    0.000  395.078    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2608192   72.784    0.000  383.799    0.000 optimizer.py:166(zero_grad)
               46947456  382.456    0.000  382.456    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               52173840  379.315    0.000  379.315    0.000 memory.py:15(inner)
                2608192  289.624    0.000  376.558    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               52173840  183.791    0.000  361.115    0.000 libenv.py:363(get_info)
               10433268   24.562    0.000  322.264    0.000 pooling.py:156(forward)
               46947456  317.427    0.000  317.427    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46947456  308.329    0.000  308.329    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10433268   18.042    0.000  297.702    0.000 _jit_internal.py:237(fn)
               25871720   26.418    0.000  290.644    0.000 <__array_function__ internals>:2(prod)
               10433268   20.286    0.000  277.986    0.000 functional.py:564(_max_pool2d)
                7826076   13.957    0.000  267.340    0.000 functional.py:68(split)
               41733084  232.711    0.000  262.520    0.000 __init__.py:66(is_acceptable)
               25871760   20.136    0.000  259.672    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               10433268  256.348    0.000  256.348    0.000 {built-in method max_pool2d}
                7826076   13.677    0.000  252.341    0.000 tensor.py:367(split)
               52173840  243.851    0.000  243.851    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25871720   33.052    0.000  239.537    0.000 fromnumeric.py:2881(prod)
                7826076  237.299    0.000  237.299    0.000 {function Tensor.split at 0x7fda58ad2940}
                2608192  216.251    0.000  216.251    0.000 memory.py:35(<listcomp>)
               46947456  211.682    0.000  211.682    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               25871720   60.543    0.000  206.485    0.000 fromnumeric.py:70(_wrapreduction)
                2608692   32.422    0.000  183.035    0.000 environments.py:76(<listcomp>)
                2608192    6.994    0.000  175.266    0.000 loss.py:444(forward)
                2608692   17.680    0.000  173.520    0.000 collector.py:7(collect)
                2608192   26.908    0.000  168.273    0.000 functional.py:2621(mse_loss)
              234737334  142.400    0.000  166.344    0.000 tensor.py:725(grad)
               28485129  156.257    0.000  156.257    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              208863976   53.166    0.000  155.813    0.000 libenv.py:271(_maybe_copy_ndarray)
               26082920  154.713    0.000  154.713    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                5217385  154.625    0.000  154.625    0.000 {built-in method builtins.sum}
              198441121  150.745    0.000  150.872    0.000 module.py:758(__getattr__)
               52173860   31.469    0.000  150.642    0.000 environments.py:79(reset)
              211273552  132.048    0.000  132.048    0.000 {built-in method torch._C._get_tracing_state}
                5216384  128.578    0.000  128.578    0.000 {built-in method gather}
                2608192   93.988    0.000   93.988    0.000 {built-in method torch._C._nn.mse_loss}
               10433268   31.088    0.000   92.625    0.000 rnn.py:524(check_forward_args)
              876394012   89.814    0.000   89.814    0.000 {method 'values' of 'collections.OrderedDict' objects}
               10433268   87.768    0.000   87.768    0.000 {method 't' of 'torch._C._TensorBase' objects}
               52258188   38.982    0.000   81.112    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8411695: <Base_v2_climber_0> in cluster <dcc> Done

Job <Base_v2_climber_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Sun Nov 22 15:16:13 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Nov 24 11:04:27 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 11:04:27 2020
Terminated at Wed Nov 25 11:00:16 2020
Results reported at Wed Nov 25 11:00:16 2020

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

    CPU time :                                   92550.00 sec.
    Max Memory :                                 56741 MB
    Average Memory :                             56060.99 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4699.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86220 sec.
    Turnaround time :                            243843 sec.

The output (if any) is above this job summary.

