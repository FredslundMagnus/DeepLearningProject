[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_plunder-0
    Discount :                  0.999
    Environment :               plunder
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


      10052867427 function calls (9846696319 primitive calls) in 86111.67 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86111.666 86111.666 {built-in method builtins.exec}
                      1    0.013    0.013 86111.666 86111.666 <string>:1(<module>)
                      1  510.727  510.727 86111.652 86111.652 main.py:11(main)
                3031913  108.673    0.000 58817.324    0.019 agent.py:46(learn)
                3031813  436.335    0.000 57131.935    0.019 agent.py:54(TD_learn)
                3031813  195.753    0.000 31538.514    0.010 memory.py:27(sample_distribution)
                3031813  327.191    0.000 30543.507    0.010 helpers.py:12(stack)
        221324149/15159165  953.089    0.000 16998.045    0.001 module.py:710(_call_impl)
               12127352  262.379    0.000 16645.332    0.001 agent.py:117(forward)
               27286665 16184.398    0.001 16184.400    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               27286617 13652.968    0.001 13652.968    0.001 {built-in method cat}
                3031913   83.280    0.000 10712.941    0.004 environments.py:73(step)
               36382056  256.825    0.000 9130.130    0.000 container.py:115(forward)
                3031913    9.049    0.000 8787.546    0.003 agent.py:32(rememberMulti)
                3031913  373.545    0.000 8778.497    0.003 agent.py:33(<listcomp>)
              421968793 8597.709    0.000 8597.709    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3031913   49.203    0.000 7054.114    0.002 agent.py:41(chooseMulti)
                3031913   61.237    0.000 6679.082    0.002 environments.py:75(<listcomp>)
               60902262 1674.820    0.000 6649.648    0.000 helpers.py:8(clean)
                3031813   20.169    0.000 5843.196    0.002 grad_mode.py:12(decorate_context)
                3031813 1377.343    0.000 5801.019    0.002 adam.py:51(step)
               69997701 5721.779    0.000 5721.779    0.000 {built-in method as_tensor}
               60636760  107.135    0.000 5332.541    0.000 conv.py:418(forward)
               60636760  114.438    0.000 5181.784    0.000 conv.py:410(_conv_forward)
               60636760 5047.519    0.000 5047.519    0.000 {built-in method conv2d}
                3031813   17.590    0.000 4971.091    0.002 tensor.py:155(backward)
                3031813   21.073    0.000 4953.501    0.002 __init__.py:57(backward)
                3031813 4842.939    0.002 4842.939    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               12127358  564.910    0.000 3726.377    0.000 rnn.py:109(flatten_parameters)
                3031913   65.737    0.000 3698.887    0.001 environments.py:74(<listcomp>)
               60638260  241.447    0.000 3633.149    0.000 interop.py:274(step)
               12127352  130.669    0.000 2876.365    0.000 rnn.py:550(forward)
               12127352 2585.980    0.000 2585.980    0.000 {built-in method lstm}
               12127355 2497.182    0.000 2497.182    0.000 {built-in method _cudnn_rnn_flatten_weight}
                3031913  126.655    0.000 2123.478    0.001 agent.py:44(<listcomp>)
               60638260   29.236    0.000 1656.206    0.000 wrapper.py:25(act)
               60638260  211.389    0.000 1652.924    0.000 exploration.py:31(epsilonGreedy)
               60638260   86.996    0.000 1626.970    0.000 env.py:197(act)
                  30319    5.740    0.000 1576.716    0.052 agent.py:81(update_target_network)
               60638260 1478.690    0.000 1484.415    0.000 libenv.py:352(act)
               72764112   67.301    0.000 1437.799    0.000 activation.py:653(forward)
               72764112  101.662    0.000 1370.498    0.000 functional.py:1277(leaky_relu)
                  30319  405.997    0.013 1308.084    0.043 memory.py:37(update_distribution)
               72764112 1259.126    0.000 1259.126    0.000 {built-in method torch._C._nn.leaky_relu}
               97018016 1150.966    0.000 1150.966    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              121540522   95.041    0.000 1048.956    0.000 extract_dict_ob.py:9(observe)
               97018016 1019.315    0.000 1019.315    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               63730512 1009.180    0.000 1009.180    0.000 {built-in method numpy.array}
              121540522   51.927    0.000  953.915    0.000 wrapper.py:19(observe)
              121540522  238.410    0.000  901.988    0.000 libenv.py:344(observe)
               12127352   32.850    0.000  829.307    0.000 linear.py:90(forward)
               12127352   64.211    0.000  780.940    0.000 functional.py:1655(linear)
              436599894  677.107    0.000  677.107    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              182178782  199.683    0.000  642.456    0.000 libenv.py:281(_maybe_copy_dict)
               48509008  627.383    0.000  627.383    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3031813   87.791    0.000  575.264    0.000 optimizer.py:166(zero_grad)
              546566665  569.678    0.000  569.678    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48509008  538.804    0.000  538.804    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               48510283  499.172    0.000  533.692    0.000 module.py:774(__setattr__)
               12127352  531.102    0.000  531.102    0.000 {built-in method addmm}
               60638260   55.022    0.000  484.482    0.000 wrapper.py:22(get_info)
               48509008  471.404    0.000  471.404    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3031813  352.148    0.000  466.168    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               48509008  459.014    0.000  459.014    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               60638260  223.282    0.000  429.460    0.000 libenv.py:363(get_info)
               60638260  422.581    0.000  422.581    0.000 memory.py:15(inner)
               12127352   30.200    0.000  409.314    0.000 pooling.py:156(forward)
               12127352   19.729    0.000  379.114    0.000 _jit_internal.py:237(fn)
               12127352   21.095    0.000  357.388    0.000 functional.py:564(_max_pool2d)
               48509008  354.238    0.000  354.238    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               60638260  343.900    0.000  343.900    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               12127352  334.847    0.000  334.847    0.000 {built-in method max_pool2d}
                9095739   13.541    0.000  293.148    0.000 functional.py:68(split)
                9095739   15.336    0.000  278.530    0.000 tensor.py:367(split)
               48509420  240.543    0.000  274.531    0.000 __init__.py:66(is_acceptable)
                9095739  261.613    0.000  261.613    0.000 {function Tensor.split at 0x7f4d29749940}
                3031913   34.595    0.000  251.693    0.000 environments.py:76(<listcomp>)
                3031813   10.215    0.000  224.187    0.000 loss.py:444(forward)
                3031614  221.286    0.000  221.286    0.000 memory.py:35(<listcomp>)
               60638280   37.177    0.000  217.139    0.000 environments.py:79(reset)
                3031813   29.993    0.000  213.972    0.000 functional.py:2621(mse_loss)
                3031913   19.946    0.000  209.220    0.000 collector.py:7(collect)
              243081044   68.703    0.000  207.043    0.000 libenv.py:271(_maybe_copy_ndarray)
               30318330  201.783    0.000  201.783    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6063827  187.828    0.000  187.829    0.000 {built-in method builtins.sum}
              242545088  161.363    0.000  187.215    0.000 tensor.py:725(grad)
              221324149  167.398    0.000  167.398    0.000 {built-in method torch._C._get_tracing_state}
                6063626  166.390    0.000  166.390    0.000 {built-in method gather}
              207256787  161.134    0.000  161.722    0.000 module.py:758(__getattr__)
                  60638   15.985    0.000  152.730    0.003 {built-in method _pickle.loads}
                3031813  127.630    0.000  127.630    0.000 {built-in method torch._C._nn.mse_loss}
               12127352  116.721    0.000  116.721    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8030007   11.500    0.000  114.639    0.000 <__array_function__ internals>:2(prod)
                  60638   26.603    0.000  110.162    0.002 {built-in method _pickle.dumps}
                1091482    1.252    0.000  102.795    0.000 storage.py:141(_load_from_bytes)
               12127352   32.246    0.000  101.577    0.000 rnn.py:524(check_forward_args)
                1091482    5.262    0.000  101.543    0.000 serialization.py:486(load)
                8030047    8.648    0.000  101.393    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               60902302   47.942    0.000   96.387    0.000 types.py:163(multimap)
               11091940   94.334    0.000   94.334    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8371238: <Base_plunder_0> in cluster <dcc> Done

Job <Base_plunder_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:32 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Nov 20 09:04:09 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 20 09:04:09 2020
Terminated at Sat Nov 21 08:59:26 2020
Results reported at Sat Nov 21 08:59:26 2020

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

    CPU time :                                   87808.00 sec.
    Max Memory :                                 25314 MB
    Average Memory :                             25010.09 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5406.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86119 sec.
    Turnaround time :                            298974 sec.

The output (if any) is above this job summary.

