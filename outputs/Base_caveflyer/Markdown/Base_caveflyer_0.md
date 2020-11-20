[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_caveflyer-0
    Discount :                  0.999
    Environment :               caveflyer
    Hours :                     24
    Memory :                    200000
    Update every :              100
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      9945812468 function calls (9741774792 primitive calls) in 86120.48 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86120.481 86120.481 {built-in method builtins.exec}
                      1    0.014    0.014 86120.481 86120.481 <string>:1(<module>)
                      1  505.912  505.912 86120.466 86120.466 main.py:11(main)
                3000539  108.627    0.000 58552.367    0.020 agent.py:46(learn)
                3000439  428.158    0.000 56871.725    0.019 agent.py:54(TD_learn)
                3000439  194.968    0.000 31528.717    0.011 memory.py:27(sample_distribution)
                3000439  318.949    0.000 30559.389    0.010 helpers.py:12(stack)
        219033847/15002295  965.702    0.000 16930.750    0.001 module.py:710(_call_impl)
               12001856  270.263    0.000 16583.169    0.001 agent.py:117(forward)
               27004299 16190.909    0.001 16190.914    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               27004251 13691.467    0.001 13691.467    0.001 {built-in method cat}
                3000539   82.208    0.000 11078.840    0.004 environments.py:73(step)
               36005568  261.198    0.000 9170.963    0.000 container.py:115(forward)
                3000539    8.804    0.000 8708.616    0.003 agent.py:32(rememberMulti)
                3000539  368.328    0.000 8699.812    0.003 agent.py:33(<listcomp>)
              417575797 8531.574    0.000 8531.574    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3000539   48.553    0.000 7046.862    0.002 agent.py:41(chooseMulti)
                3000539   62.964    0.000 6679.578    0.002 environments.py:75(<listcomp>)
               60100873 1655.517    0.000 6627.598    0.000 helpers.py:8(clean)
                3000439   20.788    0.000 5776.537    0.002 grad_mode.py:12(decorate_context)
                3000439 1363.706    0.000 5733.910    0.002 adam.py:51(step)
               69102190 5708.456    0.000 5708.456    0.000 {built-in method as_tensor}
               60009280  118.426    0.000 5333.479    0.000 conv.py:418(forward)
               60009280  121.834    0.000 5164.333    0.000 conv.py:410(_conv_forward)
               60009280 5019.277    0.000 5019.277    0.000 {built-in method conv2d}
                3000439   18.864    0.000 4872.640    0.002 tensor.py:155(backward)
                3000439   22.727    0.000 4853.776    0.002 __init__.py:57(backward)
                3000439 4745.341    0.002 4745.341    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3000539   64.529    0.000 4097.790    0.001 environments.py:74(<listcomp>)
               60010780  235.562    0.000 4033.261    0.000 interop.py:274(step)
               12001862  565.697    0.000 3677.107    0.000 rnn.py:109(flatten_parameters)
               12001856  131.914    0.000 2838.245    0.000 rnn.py:550(forward)
               12001856 2551.243    0.000 2551.243    0.000 {built-in method lstm}
               12001859 2454.460    0.000 2454.460    0.000 {built-in method _cudnn_rnn_flatten_weight}
                3000539  131.803    0.000 2123.079    0.001 agent.py:44(<listcomp>)
               60010780   27.270    0.000 2066.416    0.000 wrapper.py:25(act)
               60010780   89.215    0.000 2039.145    0.000 env.py:197(act)
               60010780 1890.452    0.000 1896.174    0.000 libenv.py:352(act)
               60010780  206.578    0.000 1639.587    0.000 exploration.py:31(epsilonGreedy)
                  30005    5.689    0.000 1572.015    0.052 agent.py:81(update_target_network)
               72011136   69.916    0.000 1460.117    0.000 activation.py:653(forward)
               72011136  105.244    0.000 1390.201    0.000 functional.py:1277(leaky_relu)
                  30005  408.566    0.014 1304.873    0.043 memory.py:37(update_distribution)
               72011136 1275.367    0.000 1275.367    0.000 {built-in method torch._C._nn.leaky_relu}
               96014048 1141.762    0.000 1141.762    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              120111653   93.734    0.000 1036.905    0.000 extract_dict_ob.py:9(observe)
               63071030 1003.071    0.000 1003.071    0.000 {built-in method numpy.array}
               96014048  996.463    0.000  996.463    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              120111653   53.946    0.000  943.171    0.000 wrapper.py:19(observe)
              120111653  235.705    0.000  889.225    0.000 libenv.py:344(observe)
               12001856   35.055    0.000  827.397    0.000 linear.py:90(forward)
               12001856   66.197    0.000  777.639    0.000 functional.py:1655(linear)
              432397846  662.563    0.000  662.563    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              180122433  192.859    0.000  635.047    0.000 libenv.py:281(_maybe_copy_dict)
               48007024  621.061    0.000  621.061    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3000439   86.534    0.000  571.152    0.000 optimizer.py:166(zero_grad)
              540397304  568.386    0.000  568.386    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48007024  534.056    0.000  534.056    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               12001856  528.759    0.000  528.759    0.000 {built-in method addmm}
               48008299  491.590    0.000  524.175    0.000 module.py:774(__setattr__)
               60010780   55.950    0.000  488.155    0.000 wrapper.py:22(get_info)
               48007024  466.783    0.000  466.783    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48007024  457.324    0.000  457.324    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3000439  337.061    0.000  446.059    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               60010780  229.316    0.000  432.205    0.000 libenv.py:363(get_info)
               60010780  425.761    0.000  425.761    0.000 memory.py:15(inner)
               12001856   29.087    0.000  401.929    0.000 pooling.py:156(forward)
               12001856   19.513    0.000  372.842    0.000 _jit_internal.py:237(fn)
               48007024  353.970    0.000  353.970    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               60010780  351.690    0.000  351.690    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               12001856   21.288    0.000  351.417    0.000 functional.py:564(_max_pool2d)
               12001856  328.669    0.000  328.669    0.000 {built-in method max_pool2d}
                9001617   13.719    0.000  293.569    0.000 functional.py:68(split)
                9001617   14.962    0.000  278.782    0.000 tensor.py:367(split)
               48007436  237.224    0.000  269.701    0.000 __init__.py:66(is_acceptable)
                9001617  262.184    0.000  262.184    0.000 {function Tensor.split at 0x7f1b5aded940}
                3000539   35.526    0.000  219.265    0.000 environments.py:76(<listcomp>)
                3000240  218.737    0.000  218.737    0.000 memory.py:35(<listcomp>)
                3000439    7.522    0.000  216.146    0.000 loss.py:444(forward)
                3000439   30.021    0.000  208.625    0.000 functional.py:2621(mse_loss)
                3000539   21.365    0.000  201.655    0.000 collector.py:7(collect)
              240223306   62.411    0.000  200.344    0.000 libenv.py:271(_maybe_copy_ndarray)
               30004590  200.207    0.000  200.207    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              240035168  161.437    0.000  185.122    0.000 tensor.py:725(grad)
               60010800   38.239    0.000  183.778    0.000 environments.py:79(reset)
                6001079  178.962    0.000  178.962    0.000 {built-in method builtins.sum}
              219033847  166.738    0.000  166.738    0.000 {built-in method torch._C._get_tracing_state}
                6000878  166.355    0.000  166.355    0.000 {built-in method gather}
              205112051  165.045    0.000  165.620    0.000 module.py:758(__getattr__)
                  60010   15.988    0.000  151.877    0.003 {built-in method _pickle.loads}
                3000439  123.063    0.000  123.063    0.000 {built-in method torch._C._nn.mse_loss}
               12001856  114.086    0.000  114.086    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7999905   11.649    0.000  111.370    0.000 <__array_function__ internals>:2(prod)
                  60010   26.238    0.000  109.576    0.002 {built-in method _pickle.dumps}
                1080178    1.194    0.000  102.139    0.000 storage.py:141(_load_from_bytes)
                1080178    5.293    0.000  100.945    0.000 serialization.py:486(load)
               12001856   32.088    0.000  100.330    0.000 rnn.py:524(check_forward_args)
                7999945    8.498    0.000   98.008    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               60100913   47.866    0.000   96.355    0.000 types.py:163(multimap)
                7999905   14.502    0.000   89.510    0.000 fromnumeric.py:2881(prod)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8371226: <Base_caveflyer_0> in cluster <dcc> Done

Job <Base_caveflyer_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:30 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 18 01:36:28 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 18 01:36:28 2020
Terminated at Thu Nov 19 01:31:56 2020
Results reported at Thu Nov 19 01:31:56 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=30G]"
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

    CPU time :                                   87876.00 sec.
    Max Memory :                                 25228 MB
    Average Memory :                             24925.46 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5492.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86128 sec.
    Turnaround time :                            99326 sec.

The output (if any) is above this job summary.

