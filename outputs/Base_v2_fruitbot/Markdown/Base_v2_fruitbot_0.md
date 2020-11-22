[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_fruitbot-0
    Discount :                  0.995
    Environment :               fruitbot
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


      9372434675 function calls (9167222109 primitive calls) in 86121.28 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86121.278 86121.278 {built-in method builtins.exec}
                      1    0.063    0.063 86121.278 86121.278 <string>:1(<module>)
                      1  486.483  486.483 86121.214 86121.214 main.py:11(main)
                2700459   97.459    0.000 50778.421    0.019 agent.py:46(learn)
                2699959  325.352    0.000 49913.407    0.018 agent.py:54(TD_learn)
                2699959  188.243    0.000 29256.800    0.011 memory.py:27(sample_distribution)
                2699959  304.964    0.000 28390.032    0.011 helpers.py:12(stack)
              366338922 19051.850    0.000 19051.850    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2700459   42.097    0.000 18473.823    0.007 agent.py:41(chooseMulti)
               24301185 14683.160    0.001 14683.167    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        218706679/13500295  890.909    0.000 14582.031    0.001 module.py:710(_call_impl)
                2700459  101.153    0.000 14303.901    0.005 agent.py:44(<listcomp>)
               10800336  210.305    0.000 14298.567    0.001 agent.py:119(forward)
               54009180  147.240    0.000 13965.182    0.000 exploration.py:33(epsilonGreedy)
               24301131 13008.605    0.001 13008.605    0.001 {built-in method cat}
                2700459   74.135    0.000 9539.964    0.004 environments.py:73(step)
               32401008  218.680    0.000 8083.483    0.000 container.py:115(forward)
                2700459    8.224    0.000 6646.368    0.002 agent.py:32(rememberMulti)
                2700459  221.706    0.000 6638.144    0.002 agent.py:33(<listcomp>)
                2700459   54.385    0.000 5738.225    0.002 environments.py:75(<listcomp>)
               54244962 1498.572    0.000 5712.945    0.000 helpers.py:8(clean)
               62344839 4891.590    0.000 4891.590    0.000 {built-in method as_tensor}
               64802016  117.026    0.000 4860.791    0.000 conv.py:418(forward)
               64802016  129.784    0.000 4696.667    0.000 conv.py:410(_conv_forward)
               64802016 4542.472    0.000 4542.472    0.000 {built-in method conv2d}
                2699959   15.097    0.000 4067.621    0.002 tensor.py:155(backward)
                2699959   19.839    0.000 4052.524    0.002 __init__.py:57(backward)
                2699959   16.285    0.000 4023.933    0.001 grad_mode.py:12(decorate_context)
                2699959 1012.054    0.000 3987.629    0.001 adam.py:51(step)
                2699959 3967.488    0.001 3967.488    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2700459   55.043    0.000 3521.396    0.001 environments.py:74(<listcomp>)
               54009180  189.081    0.000 3466.354    0.000 interop.py:274(step)
               10800342  495.589    0.000 2818.948    0.000 rnn.py:109(flatten_parameters)
               10800336  118.825    0.000 2646.875    0.000 rnn.py:550(forward)
               10800336 2384.234    0.000 2384.234    0.000 {built-in method lstm}
               54009180   24.477    0.000 1892.900    0.000 wrapper.py:25(act)
               54009180   63.027    0.000 1868.423    0.000 env.py:197(act)
               54009180 1766.804    0.000 1771.747    0.000 libenv.py:352(act)
               10800339 1735.002    0.000 1735.002    0.000 {built-in method _cudnn_rnn_flatten_weight}
               75602352   67.662    0.000 1187.950    0.000 activation.py:653(forward)
               75602352  105.070    0.000 1120.287    0.000 functional.py:1277(leaky_relu)
               75602352 1005.375    0.000 1005.375    0.000 {built-in method torch._C._nn.leaky_relu}
              108254142   75.844    0.000  843.721    0.000 extract_dict_ob.py:9(observe)
              108254142   46.586    0.000  767.876    0.000 wrapper.py:19(observe)
                   5400    1.306    0.000  767.555    0.142 agent.py:81(update_target_network)
               97198524  742.178    0.000  742.178    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              108254142  193.994    0.000  721.290    0.000 libenv.py:344(observe)
                   5400  200.220    0.037  703.487    0.130 memory.py:37(update_distribution)
               10800336   28.920    0.000  670.052    0.000 linear.py:90(forward)
               97198524  655.157    0.000  655.157    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10800336   58.863    0.000  629.969    0.000 functional.py:1655(linear)
               56719939  587.638    0.000  587.638    0.000 {built-in method numpy.array}
               43202324  509.477    0.000  540.246    0.000 module.py:774(__setattr__)
              162263322  162.150    0.000  530.194    0.000 libenv.py:281(_maybe_copy_dict)
              486795366  451.019    0.000  451.019    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48599262  449.405    0.000  449.405    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10800336  416.232    0.000  416.232    0.000 {built-in method addmm}
              379367193  404.684    0.000  404.684    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               54009180   45.247    0.000  387.869    0.000 wrapper.py:22(get_info)
               11725338  144.160    0.000  384.543    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               48599262  382.348    0.000  382.348    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2699959   64.590    0.000  374.189    0.000 optimizer.py:166(zero_grad)
               54009180  370.036    0.000  370.036    0.000 memory.py:15(inner)
                2699959  281.496    0.000  366.890    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               54009180  176.263    0.000  342.622    0.000 libenv.py:363(get_info)
               10800336   25.155    0.000  318.840    0.000 pooling.py:156(forward)
               48599262  310.557    0.000  310.557    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48599262  295.646    0.000  295.646    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10800336   16.622    0.000  293.686    0.000 _jit_internal.py:237(fn)
               26150775   24.745    0.000  288.305    0.000 <__array_function__ internals>:2(prod)
               10800336   19.833    0.000  275.512    0.000 functional.py:564(_max_pool2d)
                8101377   13.114    0.000  260.303    0.000 functional.py:68(split)
               43201356  231.205    0.000  259.665    0.000 __init__.py:66(is_acceptable)
               26150815   18.743    0.000  259.479    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               10800336  254.412    0.000  254.412    0.000 {built-in method max_pool2d}
                8101377   14.242    0.000  246.198    0.000 tensor.py:367(split)
               26150775   32.559    0.000  240.736    0.000 fromnumeric.py:2881(prod)
               54009180  237.566    0.000  237.566    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8101377  230.607    0.000  230.607    0.000 {function Tensor.split at 0x7faeeb04b940}
                2699959  208.857    0.000  208.857    0.000 memory.py:35(<listcomp>)
               26150775   60.141    0.000  208.177    0.000 fromnumeric.py:70(_wrapreduction)
               48599262  208.117    0.000  208.117    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2700459   30.779    0.000  206.207    0.000 environments.py:76(<listcomp>)
               54009200   31.303    0.000  175.443    0.000 environments.py:79(reset)
                2699959    6.153    0.000  172.182    0.000 loss.py:444(forward)
                2700459   16.241    0.000  170.236    0.000 collector.py:7(collect)
                2699959   25.252    0.000  166.028    0.000 functional.py:2621(mse_loss)
              242996364  141.229    0.000  163.034    0.000 tensor.py:725(grad)
               28856134  159.527    0.000  159.527    0.000 {method 'reduce' of 'numpy.ufunc' objects}
               27000590  158.078    0.000  158.078    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                5400919  152.814    0.000  152.814    0.000 {built-in method builtins.sum}
              205422733  151.668    0.000  151.790    0.000 module.py:758(__getattr__)
              216508284   53.035    0.000  147.436    0.000 libenv.py:271(_maybe_copy_ndarray)
              218706679  131.182    0.000  131.182    0.000 {built-in method torch._C._get_tracing_state}
                5399918  125.457    0.000  125.457    0.000 {built-in method gather}
                2699959   92.944    0.000   92.944    0.000 {built-in method torch._C._nn.mse_loss}
               10800336   30.334    0.000   92.285    0.000 rnn.py:524(check_forward_args)
               10800336   88.500    0.000   88.500    0.000 {method 't' of 'torch._C._TensorBase' objects}
              907227724   83.919    0.000   83.919    0.000 {method 'values' of 'collections.OrderedDict' objects}
               54245002   38.311    0.000   77.273    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8410444: <Base_v2_fruitbot_0> in cluster <dcc> Done

Job <Base_v2_fruitbot_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Sat Nov 21 14:15:16 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov 21 14:32:49 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 21 14:32:49 2020
Terminated at Sun Nov 22 14:28:18 2020
Results reported at Sun Nov 22 14:28:18 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=80G]"
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

    CPU time :                                   93061.00 sec.
    Max Memory :                                 56763 MB
    Average Memory :                             56064.53 MB
    Total Requested Memory :                     81920.00 MB
    Delta Memory :                               25157.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86130 sec.
    Turnaround time :                            87182 sec.

The output (if any) is above this job summary.

