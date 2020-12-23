[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/agent.py:152: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  if state_differences is not 0:

    Name :                      NOPEfruitbot-0
    Discount :                  0.99
    Environment :               fruitbot
    Hours :                     12
    Memory :                    500000
    Update every :              1000
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           1000
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0.1
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      7461191929 function calls (7248523553 primitive calls) in 42942.84 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 42942.837 42942.837 {built-in method builtins.exec}
                      1    0.018    0.018 42942.837 42942.837 <string>:1(<module>)
                      1  172.370  172.370 42942.818 42942.818 main.py:92(main)
                1489872  114.283    0.000 18017.153    0.012 agent.py:89(learn)
                1430901  425.100    0.000 17549.612    0.012 agent.py:102(TD_learn)
        254158846/41497090 1188.314    0.000 15308.471    0.000 module.py:710(_call_impl)
                1489872   38.093    0.000 15231.875    0.010 environments.py:83(step)
               29931941 1539.585    0.000 13179.853    0.000 helpers.py:8(clean)
                1489872   43.332    0.000 13163.232    0.009 environments.py:85(<listcomp>)
               45907735  360.707    0.000 12114.206    0.000 container.py:115(forward)
               72918904  163.592    0.000 7083.254    0.000 conv.py:418(forward)
               72918904  150.303    0.000 6847.517    0.000 conv.py:410(_conv_forward)
               72918904 6668.427    0.000 6668.427    0.000 {built-in method conv2d}
                4351674   96.649    0.000 5728.949    0.001 agent.py:231(forward)
                1431891    7.292    0.000 4851.501    0.003 agent.py:58(rememberMulti)
                1431891  296.074    0.000 4829.344    0.003 agent.py:60(<listcomp>)
                1430901   77.360    0.000 4618.524    0.003 memory.py:35(sample_distribution)
                1489872  164.026    0.000 4517.787    0.003 agent.py:72(chooseMulti)
                4292703   23.254    0.000 4283.280    0.001 grad_mode.py:12(decorate_context)
              251913600 4242.107    0.000 4242.107    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1430901  153.744    0.000 4239.760    0.003 helpers.py:15(stack)
                4292703  998.316    0.000 4232.721    0.001 adam.py:51(step)
               34224644 3326.168    0.000 3326.168    0.000 {built-in method as_tensor}
                4292703   16.583    0.000 2844.895    0.001 tensor.py:155(backward)
                4292703   17.775    0.000 2828.312    0.001 __init__.py:57(backward)
                4292703 2712.703    0.001 2712.703    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               15916824 2616.322    0.000 2616.322    0.000 {built-in method cat}
               96167144   90.515    0.000 2007.724    0.000 activation.py:653(forward)
               96167144  144.273    0.000 1917.209    0.000 functional.py:1277(leaky_relu)
                1489872   30.500    0.000 1858.863    0.001 environments.py:84(<listcomp>)
               29797440  115.657    0.000 1828.363    0.000 interop.py:274(step)
               96167144 1758.744    0.000 1758.744    0.000 {built-in method torch._C._nn.leaky_relu}
               26169012   56.254    0.000 1477.514    0.000 linear.py:90(forward)
               26169012  179.592    0.000 1399.310    0.000 functional.py:1655(linear)
               17406806 1391.584    0.000 1391.587    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                4351680  196.610    0.000 1265.222    0.000 rnn.py:109(flatten_parameters)
                1489872   68.359    0.000 1148.629    0.001 agent.py:87(<listcomp>)
               29797440   14.539    0.000  953.246    0.000 wrapper.py:25(act)
                4351674   42.272    0.000  949.494    0.000 rnn.py:550(forward)
               29797440   46.208    0.000  938.707    0.000 env.py:197(act)
               29797440   97.230    0.000  890.240    0.000 exploration.py:34(epsilonGreedy)
                4351677  872.260    0.000  872.260    0.000 {built-in method _cudnn_rnn_flatten_weight}
               29797440  862.817    0.000  865.643    0.000 libenv.py:352(act)
                4351674  856.463    0.000  856.463    0.000 {built-in method lstm}
               68683248  835.348    0.000  835.348    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2920772   11.109    0.000  807.335    0.000 agent.py:247(avoid_similar_state)
               21699399  768.284    0.000  768.284    0.000 {built-in method addmm}
               68683248  752.556    0.000  752.556    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              309828950  516.781    0.000  516.781    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               34341624  476.633    0.000  476.633    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               59729381   49.762    0.000  435.802    0.000 extract_dict_ob.py:9(observe)
                4292703   65.485    0.000  429.921    0.000 optimizer.py:166(zero_grad)
               34341624  388.650    0.000  388.650    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               59729381   23.571    0.000  386.040    0.000 wrapper.py:19(observe)
               59729381   89.785    0.000  362.469    0.000 libenv.py:344(observe)
                   1460    0.530    0.000  353.258    0.242 agent.py:157(update_target_network)
               34341624  338.489    0.000  338.489    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               34341624  331.154    0.000  331.154    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               34341624  266.648    0.000  266.648    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               89526821   82.850    0.000  254.388    0.000 libenv.py:281(_maybe_copy_dict)
                4292703    6.039    0.000  254.108    0.000 loss.py:444(forward)
                4292703   26.300    0.000  248.069    0.000 functional.py:2621(mse_loss)
                7029441   86.671    0.000  229.965    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               28637820  228.389    0.000  228.389    0.000 memory.py:17(inner)
              268581923  225.415    0.000  225.415    0.000 {method 'copy' of 'numpy.ndarray' objects}
               57275640  222.842    0.000  222.842    0.000 tensor.py:456(<lambda>)
               29797440   24.696    0.000  215.823    0.000 wrapper.py:22(get_info)
              257022628  214.186    0.000  214.186    0.000 {built-in method torch._C._get_tracing_state}
               26169012  198.694    0.000  198.694    0.000 {method 't' of 'torch._C._TensorBase' objects}
               29797440  105.585    0.000  191.127    0.000 libenv.py:363(get_info)
               29797440  190.029    0.000  190.029    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               31231261  182.081    0.000  182.081    0.000 {built-in method numpy.array}
                1489872   16.850    0.000  171.687    0.000 environments.py:86(<listcomp>)
                1431900  167.787    0.000  169.771    0.000 agent.py:148(convert_values)
                   1460   48.640    0.033  169.347    0.116 memory.py:45(update_distribution)
                   2920  152.095    0.052  168.593    0.058 {built-in method _pickle.loads}
                7154505  168.128    0.000  168.128    0.000 {built-in method gather}
               15489923   13.715    0.000  165.224    0.000 <__array_function__ internals>:2(prod)
                1430901  124.879    0.000  161.069    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               25933131  156.453    0.000  156.453    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              222972407  155.313    0.000  155.380    0.000 module.py:758(__getattr__)
               29797460   18.302    0.000  154.955    0.000 environments.py:89(reset)
                4292703  150.334    0.000  150.334    0.000 {built-in method torch._C._nn.mse_loss}
               15489963   11.341    0.000  148.834    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                4469613  147.024    0.000  147.024    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                4469616    6.661    0.000  139.434    0.000 functional.py:68(split)
               15489923   17.534    0.000  137.493    0.000 fromnumeric.py:2881(prod)
              171708232  116.776    0.000  136.684    0.000 tensor.py:725(grad)
                4469616    7.335    0.000  132.227    0.000 tensor.py:367(split)
               20270333  110.358    0.000  124.751    0.000 module.py:774(__setattr__)
                4469616  123.903    0.000  123.903    0.000 {function Tensor.split at 0x7f83529069d0}
               15489923   33.832    0.000  119.959    0.000 fromnumeric.py:70(_wrapreduction)
             1062543119  114.607    0.000  114.607    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1489872    8.159    0.000  107.193    0.000 collector.py:8(collect)
                7213475  102.860    0.000  102.860    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                1430901  102.351    0.000  102.351    0.000 memory.py:43(<listcomp>)
                2979745   98.545    0.000   98.545    0.000 {built-in method builtins.sum}
                4292703   17.800    0.000   96.302    0.000 __init__.py:25(_make_grads)
              119458762   31.636    0.000   93.315    0.000 libenv.py:271(_maybe_copy_ndarray)
        570653821/570652821   88.517    0.000   88.524    0.000 {built-in method builtins.len}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 8582542: <NOPEfruitbot_0> in cluster <dcc> Done

Job <NOPEfruitbot_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Tue Dec 22 15:39:59 2020
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Dec 22 15:40:00 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec 22 15:40:00 2020
Terminated at Wed Dec 23 03:36:07 2020
Results reported at Wed Dec 23 03:36:07 2020

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

    CPU time :                                   43794.00 sec.
    Max Memory :                                 10180 MB
    Average Memory :                             10073.32 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               51260.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   43034 sec.
    Turnaround time :                            42968 sec.

The output (if any) is above this job summary.

