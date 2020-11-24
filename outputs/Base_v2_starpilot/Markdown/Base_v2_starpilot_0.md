[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_starpilot-0
    Discount :                  0.995
    Environment :               starpilot
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


      9376578015 function calls (9171275161 primitive calls) in 86137.29 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86137.294 86137.294 {built-in method builtins.exec}
                      1    0.061    0.061 86137.294 86137.294 <string>:1(<module>)
                      1  494.356  494.356 86137.232 86137.232 main.py:11(main)
                2701647   99.385    0.000 51447.796    0.019 agent.py:46(learn)
                2701147  335.051    0.000 50555.482    0.019 agent.py:54(TD_learn)
                2701147  186.254    0.000 29500.556    0.011 memory.py:27(sample_distribution)
                2701147  297.170    0.000 28629.232    0.011 helpers.py:12(stack)
              366501458 18642.530    0.000 18642.530    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2701647   40.387    0.000 18114.718    0.007 agent.py:41(chooseMulti)
        218802907/13506235  942.397    0.000 14981.546    0.001 module.py:710(_call_impl)
               24311877 14915.236    0.001 14915.274    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               10805088  223.114    0.000 14693.016    0.001 agent.py:119(forward)
                2701647  102.412    0.000 13821.185    0.005 agent.py:44(<listcomp>)
               54032940  149.064    0.000 13477.857    0.000 exploration.py:33(epsilonGreedy)
               24311823 13024.499    0.001 13024.499    0.001 {built-in method cat}
                2701647   73.965    0.000 9137.688    0.003 environments.py:73(step)
               32415264  231.716    0.000 8335.266    0.000 container.py:115(forward)
                2701647    8.081    0.000 6723.479    0.002 agent.py:32(rememberMulti)
                2701647  224.622    0.000 6715.398    0.002 agent.py:33(<listcomp>)
                2701647   55.183    0.000 5823.473    0.002 environments.py:75(<listcomp>)
               54270674 1503.544    0.000 5797.831    0.000 helpers.py:8(clean)
               64830528  111.058    0.000 4988.297    0.000 conv.py:418(forward)
               62374115 4981.569    0.000 4981.569    0.000 {built-in method as_tensor}
               64830528  126.053    0.000 4829.037    0.000 conv.py:410(_conv_forward)
               64830528 4680.718    0.000 4680.718    0.000 {built-in method conv2d}
                2701147   15.377    0.000 4096.285    0.002 tensor.py:155(backward)
                2701147   17.843    0.000 4094.989    0.002 grad_mode.py:12(decorate_context)
                2701147   18.243    0.000 4080.908    0.002 __init__.py:57(backward)
                2701147 1032.397    0.000 4056.702    0.002 adam.py:51(step)
                2701147 3995.604    0.001 3995.604    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2701647   53.517    0.000 3032.494    0.001 environments.py:74(<listcomp>)
               54032940  192.995    0.000 2978.978    0.000 interop.py:274(step)
               10805094  512.715    0.000 2910.473    0.000 rnn.py:109(flatten_parameters)
               10805088  118.914    0.000 2674.092    0.000 rnn.py:550(forward)
               10805088 2416.068    0.000 2416.068    0.000 {built-in method lstm}
               10805091 1793.660    0.000 1793.660    0.000 {built-in method _cudnn_rnn_flatten_weight}
               54032940   23.924    0.000 1347.118    0.000 wrapper.py:25(act)
               54032940   66.093    0.000 1323.194    0.000 env.py:197(act)
               75635616   69.676    0.000 1243.775    0.000 activation.py:653(forward)
               54032940 1217.083    0.000 1222.061    0.000 libenv.py:352(act)
               75635616  123.576    0.000 1174.099    0.000 functional.py:1277(leaky_relu)
               75635616 1039.707    0.000 1039.707    0.000 {built-in method torch._C._nn.leaky_relu}
              108303614   80.508    0.000  877.073    0.000 extract_dict_ob.py:9(observe)
              108303614   49.794    0.000  796.565    0.000 wrapper.py:19(observe)
                   5403    1.352    0.000  792.928    0.147 agent.py:81(update_target_network)
               97241292  755.279    0.000  755.279    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              108303614  198.229    0.000  746.771    0.000 libenv.py:344(observe)
                   5403  202.216    0.037  727.587    0.135 memory.py:37(update_distribution)
               10805088   28.597    0.000  679.247    0.000 linear.py:90(forward)
               97241292  660.277    0.000  660.277    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10805088   59.740    0.000  639.889    0.000 functional.py:1655(linear)
               56744893  611.829    0.000  611.829    0.000 {built-in method numpy.array}
              162336554  171.809    0.000  546.988    0.000 libenv.py:281(_maybe_copy_dict)
               43221332  510.046    0.000  539.775    0.000 module.py:774(__setattr__)
              487015065  465.772    0.000  465.772    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48620646  456.808    0.000  456.808    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10805088  425.380    0.000  425.380    0.000 {built-in method addmm}
               54032940   45.176    0.000  404.696    0.000 wrapper.py:22(get_info)
              379531765  393.559    0.000  393.559    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               48620646  389.495    0.000  389.495    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11729122  145.763    0.000  382.542    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2701147   68.187    0.000  376.824    0.000 optimizer.py:166(zero_grad)
               54032940  372.071    0.000  372.071    0.000 memory.py:15(inner)
                2701147  285.234    0.000  370.948    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               54032940  185.116    0.000  359.519    0.000 libenv.py:363(get_info)
               10805088   24.754    0.000  323.876    0.000 pooling.py:156(forward)
               48620646  316.906    0.000  316.906    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48620646  305.093    0.000  305.093    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10805088   17.602    0.000  299.123    0.000 _jit_internal.py:237(fn)
               26159531   24.897    0.000  284.177    0.000 <__array_function__ internals>:2(prod)
               10805088   21.016    0.000  279.731    0.000 functional.py:564(_max_pool2d)
               43220364  234.341    0.000  264.172    0.000 __init__.py:66(is_acceptable)
                8104941   13.891    0.000  261.160    0.000 functional.py:68(split)
               10805088  257.253    0.000  257.253    0.000 {built-in method max_pool2d}
               26159571   19.303    0.000  255.123    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                8104941   14.101    0.000  246.175    0.000 tensor.py:367(split)
               54032940  240.916    0.000  240.916    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               26159531   32.072    0.000  235.821    0.000 fromnumeric.py:2881(prod)
                8104941  230.691    0.000  230.691    0.000 {function Tensor.split at 0x7f4160d28940}
               48620646  210.648    0.000  210.648    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2701147  209.511    0.000  209.511    0.000 memory.py:35(<listcomp>)
                2701647   29.976    0.000  207.756    0.000 environments.py:76(<listcomp>)
               26159531   59.881    0.000  203.749    0.000 fromnumeric.py:70(_wrapreduction)
               54032960   32.142    0.000  177.854    0.000 environments.py:79(reset)
                2701647   16.642    0.000  175.081    0.000 collector.py:7(collect)
                2701147    6.821    0.000  173.833    0.000 loss.py:444(forward)
                2701147   25.866    0.000  167.012    0.000 functional.py:2621(mse_loss)
              243103284  137.178    0.000  160.003    0.000 tensor.py:725(grad)
              216607228   57.535    0.000  159.751    0.000 libenv.py:271(_maybe_copy_ndarray)
               27012470  158.277    0.000  158.277    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                5403295  157.128    0.000  157.128    0.000 {built-in method builtins.sum}
               28866081  155.698    0.000  155.698    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              205513141  151.874    0.000  152.000    0.000 module.py:758(__getattr__)
              218802907  132.987    0.000  132.987    0.000 {built-in method torch._C._get_tracing_state}
                5402294  129.811    0.000  129.811    0.000 {built-in method gather}
                2701147   92.288    0.000   92.288    0.000 {built-in method torch._C._nn.mse_loss}
               10805088   30.249    0.000   92.134    0.000 rnn.py:524(check_forward_args)
               10805088   89.592    0.000   89.592    0.000 {method 't' of 'torch._C._TensorBase' objects}
              907626892   82.523    0.000   82.523    0.000 {method 'values' of 'collections.OrderedDict' objects}
               54270714   38.903    0.000   79.655    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8411694: <Base_v2_starpilot_0> in cluster <dcc> Done

Job <Base_v2_starpilot_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Sun Nov 22 15:16:12 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov 23 09:04:32 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 23 09:04:32 2020
Terminated at Tue Nov 24 09:00:26 2020
Results reported at Tue Nov 24 09:00:26 2020

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

    CPU time :                                   92766.00 sec.
    Max Memory :                                 56652 MB
    Average Memory :                             55886.21 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4788.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86155 sec.
    Turnaround time :                            150254 sec.

The output (if any) is above this job summary.

