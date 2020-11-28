[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_dodgeball-0
    Discount :                  0.995
    Environment :               dodgeball
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


      9133781803 function calls (8933902005 primitive calls) in 86128.81 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86128.814 86128.814 {built-in method builtins.exec}
                      1    0.023    0.023 86128.814 86128.814 <string>:1(<module>)
                      1  505.850  505.850 86128.790 86128.790 main.py:12(main)
                2630291  101.664    0.000 52207.366    0.020 agent.py:46(learn)
                2629791  325.459    0.000 51324.225    0.020 agent.py:54(TD_learn)
                2629791  198.421    0.000 30344.820    0.012 memory.py:27(sample_distribution)
                2629791  361.693    0.000 29455.148    0.011 helpers.py:12(stack)
              356581476 17675.187    0.000 17675.187    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2630291   41.191    0.000 17118.608    0.007 agent.py:41(chooseMulti)
        213023071/13149455  923.473    0.000 14794.663    0.001 module.py:710(_call_impl)
               10519664  222.838    0.000 14512.812    0.001 agent.py:119(forward)
               23669673 14361.297    0.001 14361.351    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               23669619 14253.317    0.001 14253.317    0.001 {built-in method cat}
                2630291  100.946    0.000 12867.318    0.005 agent.py:44(<listcomp>)
               52605820  147.190    0.000 12521.783    0.000 exploration.py:33(epsilonGreedy)
                2630291   74.408    0.000 9349.803    0.004 environments.py:73(step)
               31558992  227.429    0.000 8217.834    0.000 container.py:115(forward)
                2630291    8.168    0.000 6741.157    0.003 agent.py:32(rememberMulti)
                2630291  235.928    0.000 6732.989    0.003 agent.py:33(<listcomp>)
                2630291   52.553    0.000 5752.624    0.002 environments.py:75(<listcomp>)
               52901174 1501.981    0.000 5736.940    0.000 helpers.py:8(clean)
               60790547 5007.013    0.000 5007.013    0.000 {built-in method as_tensor}
               63117984  107.173    0.000 4918.378    0.000 conv.py:418(forward)
               63117984  131.114    0.000 4763.975    0.000 conv.py:410(_conv_forward)
               63117984 4610.937    0.000 4610.937    0.000 {built-in method conv2d}
                2629791   18.216    0.000 4146.492    0.002 tensor.py:155(backward)
                2629791   20.499    0.000 4128.276    0.002 __init__.py:57(backward)
                2629791   17.678    0.000 4120.333    0.002 grad_mode.py:12(decorate_context)
                2629791 1045.039    0.000 4084.275    0.002 adam.py:51(step)
                2629791 4039.381    0.002 4039.381    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2630291   55.365    0.000 3300.944    0.001 environments.py:74(<listcomp>)
               52605820  194.447    0.000 3245.579    0.000 interop.py:274(step)
               10519670  511.224    0.000 2853.696    0.000 rnn.py:109(flatten_parameters)
               10519664  115.154    0.000 2668.224    0.000 rnn.py:550(forward)
               10519664 2414.295    0.000 2414.295    0.000 {built-in method lstm}
               10519667 1748.579    0.000 1748.579    0.000 {built-in method _cudnn_rnn_flatten_weight}
               52605820   26.463    0.000 1610.111    0.000 wrapper.py:25(act)
               52605820   65.631    0.000 1583.649    0.000 env.py:197(act)
               52605820 1480.028    0.000 1484.960    0.000 libenv.py:352(act)
               73637648   74.512    0.000 1235.864    0.000 activation.py:653(forward)
               73637648  109.725    0.000 1161.352    0.000 functional.py:1277(leaky_relu)
               73637648 1041.885    0.000 1041.885    0.000 {built-in method torch._C._nn.leaky_relu}
              105506994   81.161    0.000  878.347    0.000 extract_dict_ob.py:9(observe)
              105506994   47.390    0.000  797.186    0.000 wrapper.py:19(observe)
                   5260    1.353    0.000  781.477    0.149 agent.py:81(update_target_network)
               94672476  758.897    0.000  758.897    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              105506994  203.831    0.000  749.797    0.000 libenv.py:344(observe)
                   5260  201.421    0.038  716.550    0.136 memory.py:37(update_distribution)
               10519664   27.230    0.000  669.050    0.000 linear.py:90(forward)
               94672476  661.205    0.000  661.205    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10519664   57.271    0.000  631.204    0.000 functional.py:1655(linear)
               55246131  601.716    0.000  601.716    0.000 {built-in method numpy.array}
              158112814  169.709    0.000  548.554    0.000 libenv.py:281(_maybe_copy_dict)
               42079636  512.856    0.000  542.768    0.000 module.py:774(__setattr__)
               47336238  474.350    0.000  474.350    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              474343702  468.319    0.000  468.319    0.000 {method 'copy' of 'numpy.ndarray' objects}
               10519664  421.068    0.000  421.068    0.000 {built-in method addmm}
               52605820   45.308    0.000  406.398    0.000 wrapper.py:22(get_info)
               52605820  398.640    0.000  398.640    0.000 memory.py:15(inner)
              369139763  394.768    0.000  394.768    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               47336238  388.479    0.000  388.479    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11659264  146.603    0.000  379.897    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2629791   65.150    0.000  372.343    0.000 optimizer.py:166(zero_grad)
                2629791  281.366    0.000  366.897    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               52605820  187.163    0.000  361.091    0.000 libenv.py:363(get_info)
               10519664   24.385    0.000  323.326    0.000 pooling.py:156(forward)
               47336238  316.848    0.000  316.848    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47336238  300.463    0.000  300.463    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10519664   17.672    0.000  298.940    0.000 _jit_internal.py:237(fn)
               25948459   26.073    0.000  279.984    0.000 <__array_function__ internals>:2(prod)
               10519664   19.957    0.000  279.489    0.000 functional.py:564(_max_pool2d)
                7890873   13.983    0.000  267.087    0.000 functional.py:68(split)
               42078668  232.840    0.000  262.462    0.000 __init__.py:66(is_acceptable)
               10519664  258.115    0.000  258.115    0.000 {built-in method max_pool2d}
                7890873   13.322    0.000  252.102    0.000 tensor.py:367(split)
               25948499   18.864    0.000  249.775    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               52605820  244.589    0.000  244.589    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7890873  237.395    0.000  237.395    0.000 {function Tensor.split at 0x7f906de30940}
               25948459   31.004    0.000  230.911    0.000 fromnumeric.py:2881(prod)
                2630291   30.974    0.000  221.827    0.000 environments.py:76(<listcomp>)
                2629791  221.629    0.000  221.629    0.000 memory.py:35(<listcomp>)
               47336238  209.719    0.000  209.719    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               25948459   60.011    0.000  199.907    0.000 fromnumeric.py:70(_wrapreduction)
               52605840   34.029    0.000  190.887    0.000 environments.py:79(reset)
                2630291   18.432    0.000  172.389    0.000 collector.py:7(collect)
                2629791    6.592    0.000  169.408    0.000 loss.py:444(forward)
                2629791   25.008    0.000  162.816    0.000 functional.py:2621(mse_loss)
              236681244  136.642    0.000  158.953    0.000 tensor.py:725(grad)
               26298910  158.785    0.000  158.785    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              211013988   53.385    0.000  154.178    0.000 libenv.py:271(_maybe_copy_ndarray)
              200084365  152.805    0.000  152.931    0.000 module.py:758(__getattr__)
                5260583  152.834    0.000  152.834    0.000 {built-in method builtins.sum}
               28583510  150.099    0.000  150.099    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              213023071  128.394    0.000  128.394    0.000 {built-in method torch._C._get_tracing_state}
                5259582  127.629    0.000  127.629    0.000 {built-in method gather}
               10519664   30.209    0.000   92.067    0.000 rnn.py:524(check_forward_args)
                2629791   91.399    0.000   91.399    0.000 {built-in method torch._C._nn.mse_loss}
               10519664   90.173    0.000   90.173    0.000 {method 't' of 'torch._C._TensorBase' objects}
               52901214   39.804    0.000   80.882    0.000 types.py:163(multimap)
              883651276   78.076    0.000   78.076    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8423562: <Base_v2_dodgeball_0> in cluster <dcc> Done

Job <Base_v2_dodgeball_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue Nov 24 19:48:56 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 25 23:15:19 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 25 23:15:19 2020
Terminated at Thu Nov 26 23:11:00 2020
Results reported at Thu Nov 26 23:11:00 2020

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

    CPU time :                                   93568.00 sec.
    Max Memory :                                 56789 MB
    Average Memory :                             56060.03 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4651.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86140 sec.
    Turnaround time :                            184924 sec.

The output (if any) is above this job summary.

