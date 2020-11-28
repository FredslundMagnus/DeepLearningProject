[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_miner-0
    Discount :                  0.995
    Environment :               miner
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


      9404786266 function calls (9198789380 primitive calls) in 86141.47 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86141.465 86141.465 {built-in method builtins.exec}
                      1    0.046    0.046 86141.465 86141.465 <string>:1(<module>)
                      1  450.102  450.102 86141.418 86141.418 main.py:12(main)
                2710779   94.500    0.000 50658.701    0.019 agent.py:46(learn)
                2710279  310.766    0.000 49763.167    0.018 agent.py:54(TD_learn)
                2710279  186.083    0.000 28550.196    0.011 memory.py:27(sample_distribution)
                2710279  265.866    0.000 27669.377    0.010 helpers.py:12(stack)
              367774292 18565.807    0.000 18565.807    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2710779   39.811    0.000 18119.474    0.007 agent.py:41(chooseMulti)
        219542599/13551895  925.291    0.000 14877.357    0.001 module.py:710(_call_impl)
               10841616  218.874    0.000 14599.004    0.001 agent.py:119(forward)
               24394065 14396.786    0.001 14396.825    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2710779  103.180    0.000 13748.040    0.005 agent.py:44(<listcomp>)
               54215580  156.917    0.000 13393.758    0.000 exploration.py:33(epsilonGreedy)
               24394011 12670.336    0.001 12670.336    0.001 {built-in method cat}
                2710779   76.220    0.000 9903.930    0.004 environments.py:73(step)
               32524848  233.612    0.000 8452.307    0.000 container.py:115(forward)
                2710779    8.125    0.000 6763.403    0.002 agent.py:32(rememberMulti)
                2710779  256.168    0.000 6755.278    0.002 agent.py:33(<listcomp>)
                2710779   57.776    0.000 6434.680    0.002 environments.py:75(<listcomp>)
               54305275 1743.668    0.000 6389.420    0.000 helpers.py:8(clean)
               62436112 5269.343    0.000 5269.343    0.000 {built-in method as_tensor}
               65049696  117.046    0.000 5052.501    0.000 conv.py:418(forward)
               65049696  123.677    0.000 4886.427    0.000 conv.py:410(_conv_forward)
               65049696 4739.163    0.000 4739.163    0.000 {built-in method conv2d}
                2710279   16.407    0.000 4336.955    0.002 grad_mode.py:12(decorate_context)
                2710279 1091.917    0.000 4301.704    0.002 adam.py:51(step)
                2710279   15.295    0.000 4234.678    0.002 tensor.py:155(backward)
                2710279   18.247    0.000 4219.383    0.002 __init__.py:57(backward)
                2710279 4132.982    0.002 4132.982    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2710779   58.442    0.000 3198.420    0.001 environments.py:74(<listcomp>)
               54215580  203.048    0.000 3139.978    0.000 interop.py:274(step)
               10841622  484.872    0.000 2761.163    0.000 rnn.py:109(flatten_parameters)
               10841616  113.102    0.000 2617.229    0.000 rnn.py:550(forward)
               10841616 2365.456    0.000 2365.456    0.000 {built-in method lstm}
               10841619 1718.848    0.000 1718.848    0.000 {built-in method _cudnn_rnn_flatten_weight}
               54215580   28.193    0.000 1448.793    0.000 wrapper.py:25(act)
               54215580   71.963    0.000 1420.600    0.000 env.py:197(act)
               54215580 1305.330    0.000 1310.677    0.000 libenv.py:352(act)
               75891312   70.414    0.000 1277.897    0.000 activation.py:653(forward)
               75891312  109.318    0.000 1207.483    0.000 functional.py:1277(leaky_relu)
               75891312 1087.081    0.000 1087.081    0.000 {built-in method torch._C._nn.leaky_relu}
              108520855   83.103    0.000  894.214    0.000 extract_dict_ob.py:9(observe)
              108520855   50.839    0.000  811.111    0.000 wrapper.py:19(observe)
                   5421    1.276    0.000  801.034    0.148 agent.py:81(update_target_network)
               97570044  791.094    0.000  791.094    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              108520855  208.546    0.000  760.272    0.000 libenv.py:344(observe)
                   5421  198.809    0.037  732.330    0.135 memory.py:37(update_distribution)
               97570044  703.312    0.000  703.312    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10841616   28.442    0.000  675.978    0.000 linear.py:90(forward)
               10841616   55.932    0.000  636.055    0.000 functional.py:1655(linear)
               56936701  626.336    0.000  626.336    0.000 {built-in method numpy.array}
              162736435  173.322    0.000  552.859    0.000 libenv.py:281(_maybe_copy_dict)
               43367444  468.838    0.000  498.439    0.000 module.py:774(__setattr__)
               48785022  493.067    0.000  493.067    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              488214726  472.607    0.000  472.607    0.000 {method 'copy' of 'numpy.ndarray' objects}
               10841616  430.172    0.000  430.172    0.000 {built-in method addmm}
               54215580   46.569    0.000  419.842    0.000 wrapper.py:22(get_info)
                2710279   75.432    0.000  410.695    0.000 optimizer.py:166(zero_grad)
               48785022  410.161    0.000  410.161    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              381146337  389.857    0.000  389.857    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                2710279  296.210    0.000  384.275    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               11734768  147.865    0.000  384.012    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               54215580  191.372    0.000  373.273    0.000 libenv.py:363(get_info)
               54215580  362.871    0.000  362.871    0.000 memory.py:15(inner)
               48785022  336.112    0.000  336.112    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48785022  324.215    0.000  324.215    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10841616   21.013    0.000  323.001    0.000 pooling.py:156(forward)
               10841616   18.118    0.000  301.988    0.000 _jit_internal.py:237(fn)
               26179955   25.234    0.000  284.317    0.000 <__array_function__ internals>:2(prod)
               10841616   19.809    0.000  282.095    0.000 functional.py:564(_max_pool2d)
               10841616  260.759    0.000  260.759    0.000 {built-in method max_pool2d}
                8132337   13.763    0.000  260.721    0.000 functional.py:68(split)
               26179995   19.391    0.000  254.458    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               54215580  251.103    0.000  251.103    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               43366476  220.693    0.000  248.362    0.000 __init__.py:66(is_acceptable)
                8132337   14.145    0.000  245.835    0.000 tensor.py:367(split)
               26179955   33.022    0.000  235.067    0.000 fromnumeric.py:2881(prod)
                8132337  230.154    0.000  230.154    0.000 {function Tensor.split at 0x7fb7d3804940}
               48785022  225.915    0.000  225.915    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2710279  207.688    0.000  207.688    0.000 memory.py:35(<listcomp>)
               26179955   61.196    0.000  202.045    0.000 fromnumeric.py:70(_wrapreduction)
                2710779   17.677    0.000  198.877    0.000 collector.py:7(collect)
                2710779   33.142    0.000  194.611    0.000 environments.py:76(<listcomp>)
                5421559  179.890    0.000  179.890    0.000 {built-in method builtins.sum}
              243925164  156.486    0.000  179.833    0.000 tensor.py:725(grad)
                2710279    6.388    0.000  175.643    0.000 loss.py:444(forward)
                2710279   23.510    0.000  169.254    0.000 functional.py:2621(mse_loss)
               27103790  164.703    0.000  164.703    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              217041710   57.841    0.000  163.576    0.000 libenv.py:271(_maybe_copy_ndarray)
               54215600   34.632    0.000  161.506    0.000 environments.py:79(reset)
              206207893  151.997    0.000  152.128    0.000 module.py:758(__getattr__)
               28895655  148.638    0.000  148.638    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              219542599  139.945    0.000  139.945    0.000 {built-in method torch._C._get_tracing_state}
                5420558  127.498    0.000  127.498    0.000 {built-in method gather}
              910695244   97.435    0.000   97.435    0.000 {method 'values' of 'collections.OrderedDict' objects}
                2710279   96.260    0.000   96.260    0.000 {built-in method torch._C._nn.mse_loss}
               10841616   31.809    0.000   92.654    0.000 rnn.py:524(check_forward_args)
               10841616   86.741    0.000   86.741    0.000 {method 't' of 'torch._C._TensorBase' objects}
               54305315   41.597    0.000   84.879    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 8423565: <Base_v2_miner_0> in cluster <dcc> Done

Job <Base_v2_miner_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue Nov 24 19:48:57 2020
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Nov 27 01:22:10 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 01:22:10 2020
Terminated at Sat Nov 28 01:18:08 2020
Results reported at Sat Nov 28 01:18:08 2020

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

    CPU time :                                   92574.00 sec.
    Max Memory :                                 56791 MB
    Average Memory :                             56013.13 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4649.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86159 sec.
    Turnaround time :                            278951 sec.

The output (if any) is above this job summary.

