[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/agent.py:152: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  if state_differences is not 0:

    Name :                      NOPEmaze-0
    Discount :                  0.99
    Environment :               maze
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


      8500885222 function calls (8258409121 primitive calls) in 42943.34 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 42943.339 42943.339 {built-in method builtins.exec}
                      1    0.032    0.032 42943.339 42943.339 <string>:1(<module>)
                      1  207.093  207.093 42943.305 42943.305 main.py:92(main)
                1700919  131.185    0.000 17880.241    0.011 agent.py:89(learn)
                1631953  388.228    0.000 17305.082    0.011 agent.py:102(TD_learn)
                1700919   41.908    0.000 15765.090    0.009 environments.py:83(step)
        289772605/47303124 1293.117    0.000 15235.688    0.000 module.py:710(_call_impl)
                1700919   41.850    0.000 13656.605    0.008 environments.py:85(<listcomp>)
               34109569 1799.022    0.000 13652.158    0.000 helpers.py:8(clean)
               52336915  344.990    0.000 11959.128    0.000 container.py:115(forward)
               83113613  182.284    0.000 7089.639    0.000 conv.py:418(forward)
               83113613  176.192    0.000 6825.627    0.000 conv.py:410(_conv_forward)
               83113613 6616.622    0.000 6616.622    0.000 {built-in method conv2d}
                4964825  106.541    0.000 5697.118    0.001 agent.py:231(forward)
                1631953   88.346    0.000 5471.219    0.003 memory.py:35(sample_distribution)
                1631953  184.301    0.000 5027.845    0.003 helpers.py:15(stack)
                1632943    8.293    0.000 4485.385    0.003 agent.py:58(rememberMulti)
                1632943  233.317    0.000 4460.976    0.003 agent.py:60(<listcomp>)
                1700919  152.289    0.000 4437.691    0.003 agent.py:72(chooseMulti)
              287883636 4022.000    0.000 4022.000    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               39005428 3573.209    0.000 3573.209    0.000 {built-in method as_tensor}
                4895859   24.321    0.000 3525.435    0.001 grad_mode.py:12(decorate_context)
                4895859  882.381    0.000 3468.512    0.001 adam.py:51(step)
               18158381 3209.617    0.000 3209.617    0.000 {built-in method cat}
                4895859   17.282    0.000 2689.015    0.001 tensor.py:155(backward)
                4895859   19.826    0.000 2671.734    0.001 __init__.py:57(backward)
                4895859 2555.213    0.001 2555.213    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1700919   30.492    0.000 1932.656    0.001 environments.py:84(<listcomp>)
               34018380  117.023    0.000 1902.163    0.000 interop.py:274(step)
              109638655  108.535    0.000 1840.121    0.000 activation.py:653(forward)
              109638655  172.446    0.000 1731.586    0.000 functional.py:1277(leaky_relu)
              109638655 1542.792    0.000 1542.792    0.000 {built-in method torch._C._nn.leaky_relu}
               19859410 1542.424    0.000 1542.460    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               29857913   63.563    0.000 1425.818    0.000 linear.py:90(forward)
               29857913  178.108    0.000 1336.899    0.000 functional.py:1655(linear)
                4964831  210.269    0.000 1160.943    0.000 rnn.py:109(flatten_parameters)
                1700919   61.922    0.000 1095.204    0.001 agent.py:87(<listcomp>)
                4964825   49.291    0.000 1085.533    0.000 rnn.py:550(forward)
               34018380   15.510    0.000  988.497    0.000 wrapper.py:25(act)
                4964825  979.630    0.000  979.630    0.000 {built-in method lstm}
               34018380   43.490    0.000  972.987    0.000 env.py:197(act)
               34018380  903.672    0.000  907.021    0.000 libenv.py:352(act)
               34018380   91.263    0.000  870.634    0.000 exploration.py:34(epsilonGreedy)
                3332871   12.521    0.000  781.004    0.000 agent.py:247(avoid_similar_state)
                4964828  736.896    0.000  736.896    0.000 {built-in method _cudnn_rnn_flatten_weight}
               24755159  721.772    0.000  721.772    0.000 {built-in method addmm}
               78333744  643.294    0.000  643.294    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               78333744  570.108    0.000  570.108    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               68127949   48.505    0.000  461.430    0.000 extract_dict_ob.py:9(observe)
                   1666    0.639    0.000  443.974    0.266 agent.py:157(update_target_network)
               68127949   24.864    0.000  412.925    0.000 wrapper.py:19(observe)
               39166872  407.209    0.000  407.209    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              354111959  400.855    0.000  400.855    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               68127949   98.881    0.000  388.061    0.000 libenv.py:344(observe)
                4895859   57.930    0.000  335.576    0.000 optimizer.py:166(zero_grad)
               39166872  321.792    0.000  321.792    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               32658860  282.055    0.000  282.055    0.000 memory.py:17(inner)
              102146329   89.310    0.000  276.758    0.000 libenv.py:281(_maybe_copy_dict)
               39166872  264.620    0.000  264.620    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               39166872  258.284    0.000  258.284    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4895859    7.487    0.000  256.940    0.000 loss.py:444(forward)
                4895859   30.470    0.000  249.453    0.000 functional.py:2621(mse_loss)
              306440653  235.491    0.000  235.491    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7454713   85.378    0.000  229.240    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               34018380   25.281    0.000  226.630    0.000 wrapper.py:22(get_info)
                   1666   59.526    0.036  215.263    0.129 memory.py:45(update_distribution)
               35653665  214.683    0.000  214.683    0.000 {built-in method numpy.array}
                   3332  193.389    0.058  211.129    0.063 {built-in method _pickle.loads}
               34018380  109.128    0.000  201.349    0.000 libenv.py:363(get_info)
              293038491  199.246    0.000  199.246    0.000 {built-in method torch._C._get_tracing_state}
               39166872  189.081    0.000  189.081    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1631953  143.906    0.000  184.909    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               29857913  174.712    0.000  174.712    0.000 {method 't' of 'torch._C._TensorBase' objects}
              254233961  174.314    0.000  174.390    0.000 module.py:758(__getattr__)
               65317720  171.659    0.000  171.659    0.000 tensor.py:456(<lambda>)
               16541519   14.783    0.000  168.181    0.000 <__array_function__ internals>:2(prod)
               34018380  162.648    0.000  162.648    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                5102757    7.804    0.000  158.844    0.000 functional.py:68(split)
                8159765  157.333    0.000  157.333    0.000 {built-in method gather}
               16541559   11.437    0.000  150.602    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                5102757    8.021    0.000  150.372    0.000 tensor.py:367(split)
                1632952  143.120    0.000  145.232    0.000 agent.py:148(convert_values)
               23125041  128.509    0.000  144.018    0.000 module.py:774(__setattr__)
              195834472  121.824    0.000  141.691    0.000 tensor.py:725(grad)
                5102754  141.544    0.000  141.544    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                5102757  141.230    0.000  141.230    0.000 {function Tensor.split at 0x7f8043c399d0}
                4895859  140.236    0.000  140.236    0.000 {built-in method torch._C._nn.mse_loss}
               16541519   18.833    0.000  139.165    0.000 fromnumeric.py:2881(prod)
               29582052  137.756    0.000  137.756    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                1700919   16.001    0.000  133.921    0.000 environments.py:86(<listcomp>)
             1211427335  129.391    0.000  129.391    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1631953  126.088    0.000  126.088    0.000 memory.py:43(<listcomp>)
                1700919   10.078    0.000  122.291    0.000 collector.py:8(collect)
               16541519   35.966    0.000  120.331    0.000 fromnumeric.py:70(_wrapreduction)
               34018400   17.020    0.000  118.032    0.000 environments.py:89(reset)
                3401839  111.715    0.000  111.715    0.000 {built-in method builtins.sum}
                1827544   99.364    0.000   99.364    0.000 {built-in method tensor}
                4895859   21.157    0.000   94.988    0.000 __init__.py:25(_make_grads)
              136255898   36.604    0.000   93.439    0.000 libenv.py:271(_maybe_copy_ndarray)
                8228730   91.966    0.000   91.966    0.000 {method 'type' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 8582543: <NOPEmaze_0> in cluster <dcc> Done

Job <NOPEmaze_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Tue Dec 22 15:39:59 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Dec 22 15:40:00 2020
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

    CPU time :                                   44064.00 sec.
    Max Memory :                                 10187 MB
    Average Memory :                             10103.93 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               51253.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   43046 sec.
    Turnaround time :                            42968 sec.

The output (if any) is above this job summary.

