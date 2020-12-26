[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NOPE_final_heist-0
    Discount :                  0.995
    Environment :               heist
    Hours :                     18
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
    State difference :          0
    State difference weight :   0.0
    Minutes used :              1075 minutes.
    Hours used :                17 hours.

# Profiling


      7809342110 function calls (7645885882 primitive calls) in 64522.00 seconds

##    Ordered by: cumulative time
   List reduced from 1329 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 64521.997 64521.997 {built-in method builtins.exec}
                      1    0.061    0.061 64521.997 64521.997 <string>:1(<module>)
                      1  424.112  424.112 64521.934 64521.934 main.py:91(main)
                2153480  152.565    0.000 40667.390    0.019 agent.py:93(learn)
                2066523  355.714    0.000 40005.890    0.019 agent.py:106(TD_learn)
                2066523  152.642    0.000 23302.001    0.011 memory.py:35(sample_distribution)
                2066523  276.201    0.000 22608.724    0.011 helpers.py:15(stack)
               18859686 11271.725    0.001 11271.739    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2153480   43.434    0.000 10907.957    0.005 agent.py:72(chooseMulti)
               18859578 10765.247    0.001 10765.247    0.001 {built-in method cat}
              280121030 10565.434    0.000 10565.434    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
        173869248/10419572  755.248    0.000 10409.211    0.001 module.py:710(_call_impl)
                6286526  168.762    0.000 10037.742    0.002 agent.py:235(forward)
                2153480   59.206    0.000 7170.360    0.003 environments.py:83(step)
                2067522   73.475    0.000 6793.979    0.003 agent.py:88(<listcomp>)
               41350440  107.198    0.000 6535.469    0.000 exploration.py:34(epsilonGreedy)
               25146104  184.446    0.000 6164.770    0.000 container.py:115(forward)
                2067513    9.274    0.000 5179.481    0.003 agent.py:58(rememberMulti)
                2067513  172.384    0.000 5170.207    0.003 agent.py:63(<listcomp>)
                2153480   51.833    0.000 4557.607    0.002 environments.py:85(<listcomp>)
               43116666 1215.553    0.000 4511.621    0.000 helpers.py:8(clean)
                4133046   22.725    0.000 4285.785    0.001 grad_mode.py:12(decorate_context)
                4133046 1085.945    0.000 4234.358    0.001 adam.py:51(step)
                4133046   20.010    0.000 3853.148    0.001 tensor.py:155(backward)
               49316235 3833.977    0.000 3833.977    0.000 {built-in method as_tensor}
                4133046   24.355    0.000 3833.138    0.001 __init__.py:57(backward)
                4133046 3713.170    0.001 3713.170    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               37719156   68.699    0.000 2937.267    0.000 conv.py:418(forward)
               37719156   78.794    0.000 2835.106    0.000 conv.py:410(_conv_forward)
               37719156 2741.611    0.000 2741.611    0.000 {built-in method conv2d}
                2153480   44.882    0.000 2411.457    0.001 environments.py:84(<listcomp>)
               43069600  162.087    0.000 2366.576    0.000 interop.py:274(step)
                6286532  321.286    0.000 1736.312    0.000 rnn.py:109(flatten_parameters)
                6286526   74.745    0.000 1546.284    0.000 rnn.py:550(forward)
                6286526 1384.270    0.000 1384.270    0.000 {built-in method lstm}
               25146104   52.838    0.000 1191.221    0.000 linear.py:90(forward)
               25146104   94.605    0.000 1111.148    0.000 functional.py:1655(linear)
               43069600   20.324    0.000 1036.351    0.000 wrapper.py:25(act)
                6286529 1026.135    0.000 1026.135    0.000 {built-in method _cudnn_rnn_flatten_weight}
               43069600   52.833    0.000 1016.027    0.000 env.py:197(act)
               62865260   57.516    0.000  963.226    0.000 activation.py:653(forward)
               43069600  930.534    0.000  934.688    0.000 libenv.py:352(act)
               62865260   84.526    0.000  905.710    0.000 functional.py:1277(leaky_relu)
               62865260  812.177    0.000  812.177    0.000 {built-in method torch._C._nn.leaky_relu}
               99193104  778.333    0.000  778.333    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               25146104  747.299    0.000  747.299    0.000 {built-in method addmm}
               86186266   64.327    0.000  696.790    0.000 extract_dict_ob.py:9(observe)
               99193104  683.663    0.000  683.663    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               86186266   36.192    0.000  632.463    0.000 wrapper.py:19(observe)
               86186266  166.588    0.000  596.271    0.000 libenv.py:344(observe)
                   2110    0.845    0.000  508.935    0.241 agent.py:161(update_target_network)
               49596552  490.494    0.000  490.494    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              129255866  135.880    0.000  429.399    0.000 libenv.py:281(_maybe_copy_dict)
               49596552  400.114    0.000  400.114    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4133046   69.796    0.000  393.426    0.000 optimizer.py:166(zero_grad)
              387769708  362.483    0.000  362.483    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11091564  132.791    0.000  344.873    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               29280985  312.282    0.000  335.161    0.000 module.py:774(__setattr__)
               49596552  330.960    0.000  330.960    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              310504331  329.872    0.000  329.872    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               43069600   36.464    0.000  324.729    0.000 wrapper.py:22(get_info)
               49596552  320.192    0.000  320.192    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               41350260  291.695    0.000  291.695    0.000 memory.py:17(inner)
               43069600  149.656    0.000  288.265    0.000 libenv.py:363(get_info)
                2066523  218.199    0.000  284.484    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               45140343  281.317    0.000  281.317    0.000 {built-in method numpy.array}
                   2110   76.902    0.036  273.219    0.129 memory.py:45(update_distribution)
                4133046    9.059    0.000  255.893    0.000 loss.py:444(forward)
               24249791   22.278    0.000  249.377    0.000 <__array_function__ internals>:2(prod)
                4133046   35.425    0.000  246.834    0.000 functional.py:2621(mse_loss)
               49596552  223.459    0.000  223.459    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24249831   17.028    0.000  223.418    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                   4220  192.255    0.046  214.017    0.051 {built-in method _pickle.loads}
               24249791   27.308    0.000  206.390    0.000 fromnumeric.py:2881(prod)
                2067522  142.369    0.000  204.176    0.000 agent.py:152(convert_values)
                6460440   10.773    0.000  198.520    0.000 functional.py:68(split)
                6286526   15.448    0.000  194.669    0.000 pooling.py:156(forward)
               43069600  191.806    0.000  191.806    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6460440   11.253    0.000  186.883    0.000 tensor.py:367(split)
                6286526   11.526    0.000  179.221    0.000 _jit_internal.py:237(fn)
               24249791   52.335    0.000  179.082    0.000 fromnumeric.py:70(_wrapreduction)
               25146116  158.422    0.000  177.214    0.000 __init__.py:66(is_acceptable)
                2066523  174.930    0.000  174.930    0.000 memory.py:43(<listcomp>)
                6460440  174.244    0.000  174.244    0.000 {function Tensor.split at 0x7f65f11659d0}
                6286526   12.548    0.000  166.610    0.000 functional.py:564(_max_pool2d)
                8266092  164.901    0.000  164.901    0.000 {built-in method gather}
              247982868  140.374    0.000  163.348    0.000 tensor.py:725(grad)
               25146104  160.174    0.000  160.174    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6286526  153.248    0.000  153.248    0.000 {built-in method max_pool2d}
                2153480   16.584    0.000  146.535    0.000 collector.py:8(collect)
               29192193  143.578    0.000  143.578    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2153480   23.175    0.000  142.089    0.000 environments.py:86(<listcomp>)
                4133046  136.851    0.000  136.851    0.000 {built-in method torch._C._nn.mse_loss}
               26318424  130.659    0.000  130.659    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                4306961  128.961    0.000  128.961    0.000 {built-in method builtins.sum}
              163619103  127.219    0.000  127.313    0.000 module.py:758(__getattr__)
              172372532   46.088    0.000  125.548    0.000 libenv.py:271(_maybe_copy_ndarray)
               43069620   30.337    0.000  118.928    0.000 environments.py:89(reset)
              173869248  102.023    0.000  102.023    0.000 {built-in method torch._C._get_tracing_state}
                4133046   25.314    0.000   94.208    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8587064: <NOPE_final_heist_0> in cluster <dcc> Done

Job <NOPE_final_heist_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Thu Dec 24 13:35:00 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Dec 26 01:25:53 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec 26 01:25:53 2020
Terminated at Sat Dec 26 19:21:24 2020
Results reported at Sat Dec 26 19:21:24 2020

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

    CPU time :                                   68693.00 sec.
    Max Memory :                                 55707 MB
    Average Memory :                             54990.80 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5733.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64532 sec.
    Turnaround time :                            193584 sec.

The output (if any) is above this job summary.

