
    Name :                      NOPEjumper-0
    Discount :                  0.99
    Environment :               jumper
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


      10650135187 function calls (10409558485 primitive calls) in 42925.21 seconds

##    Ordered by: cumulative time
   List reduced from 1358 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 42925.209 42925.209 {built-in method builtins.exec}
                      1    0.019    0.019 42925.209 42925.209 <string>:1(<module>)
                      1  187.522  187.522 42925.189 42925.189 main.py:92(main)
                1685019  117.265    0.000 18728.380    0.011 agent.py:89(learn)
                1618052  386.636    0.000 18231.105    0.011 agent.py:102(TD_learn)
                1685019   37.896    0.000 15154.799    0.009 environments.py:83(step)
        287517053/46946977 1156.055    0.000 14420.131    0.000 module.py:715(_call_impl)
               33868628 1595.783    0.000 12609.727    0.000 helpers.py:8(clean)
                1685019   40.654    0.000 12587.471    0.007 environments.py:85(<listcomp>)
               51935067  328.113    0.000 11276.230    0.000 container.py:115(forward)
               82500625  163.999    0.000 6589.250    0.000 conv.py:422(forward)
               82500625  158.688    0.000 6352.655    0.000 conv.py:414(_conv_forward)
               82500625 6165.710    0.000 6165.710    0.000 {built-in method conv2d}
                4921123   94.667    0.000 5603.025    0.001 agent.py:231(forward)
                1618052   84.347    0.000 5425.029    0.003 memory.py:35(sample_distribution)
                1618052  156.019    0.000 5011.400    0.003 helpers.py:15(stack)
                1685019  148.702    0.000 4367.619    0.003 agent.py:72(chooseMulti)
                1619042   25.357    0.000 4353.508    0.003 agent.py:58(rememberMulti)
                1619042  182.129    0.000 4224.406    0.003 agent.py:60(<listcomp>)
              285382019 4082.906    0.000 4082.906    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                4854156   28.464    0.000 4035.810    0.001 grad_mode.py:23(decorate_context)
                4854156  137.224    0.000 3955.088    0.001 adam.py:55(step)
               38722784 3483.325    0.000 3483.325    0.000 {built-in method as_tensor}
                4854156  723.785    0.000 3256.238    0.001 functional.py:53(adam)
               17999473 3129.814    0.000 3129.814    0.000 {built-in method cat}
                4854156   27.658    0.000 2696.548    0.001 tensor.py:181(backward)
                4854156   16.090    0.000 2668.890    0.001 __init__.py:68(backward)
                4854156 2553.245    0.001 2553.245    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1685019   28.687    0.000 2386.832    0.001 environments.py:84(<listcomp>)
               33700380  116.894    0.000 2358.145    0.000 interop.py:274(step)
              108791257   96.930    0.000 1784.103    0.000 activation.py:713(forward)
              108791257  155.931    0.000 1687.173    0.000 functional.py:1292(leaky_relu)
               19684602 1566.135    0.000 1566.144    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              108791257 1516.213    0.000 1516.213    0.000 {built-in method torch._C._nn.leaky_relu}
               33700380   14.909    0.000 1456.055    0.000 wrapper.py:25(act)
               29593702   63.090    0.000 1445.920    0.000 linear.py:92(forward)
               33700380   43.219    0.000 1441.146    0.000 env.py:197(act)
               33700380 1371.570    0.000 1374.890    0.000 libenv.py:352(act)
               29593702  170.947    0.000 1358.706    0.000 functional.py:1669(linear)
                4921129  215.726    0.000 1183.615    0.000 rnn.py:110(flatten_parameters)
                1685019   58.918    0.000 1060.691    0.001 agent.py:87(<listcomp>)
                4921123   42.639    0.000 1009.917    0.000 rnn.py:555(forward)
              271832848  591.614    0.000 1001.724    0.000 tensor.py:933(grad)
                4921123  914.422    0.000  914.422    0.000 {built-in method lstm}
                4854156   85.088    0.000  873.514    0.000 optimizer.py:167(zero_grad)
               33700380   85.978    0.000  851.504    0.000 exploration.py:34(epsilonGreedy)
                3303070   10.516    0.000  777.780    0.000 agent.py:247(avoid_similar_state)
                4921126  741.545    0.000  741.545    0.000 {built-in method _cudnn_rnn_flatten_weight}
               24538648  731.560    0.000  731.560    0.000 {built-in method addmm}
               77666496  660.011    0.000  660.011    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               77666496  560.361    0.000  560.361    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              340260014  175.769    0.000  514.016    0.000 overrides.py:1073(has_torch_function)
               67569008   51.244    0.000  460.818    0.000 extract_dict_ob.py:9(observe)
               67569008   25.281    0.000  409.574    0.000 wrapper.py:19(observe)
               67569008   95.617    0.000  384.294    0.000 libenv.py:344(observe)
               38833248  380.427    0.000  380.427    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   1652    0.589    0.000  380.010    0.230 agent.py:157(update_target_network)
               38833248  337.104    0.000  337.104    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              379562052  134.738    0.000  327.014    0.000 {built-in method builtins.any}
              350879108  322.861    0.000  322.861    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               38833248  306.291    0.000  306.291    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               38833248  276.346    0.000  276.346    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              101269388   85.665    0.000  274.242    0.000 libenv.py:281(_maybe_copy_dict)
                4854156    7.401    0.000  252.600    0.000 loss.py:445(forward)
                4854156   26.595    0.000  245.199    0.000 functional.py:2637(mse_loss)
               32380840  239.664    0.000  239.664    0.000 memory.py:17(inner)
                5055057    7.951    0.000  238.798    0.000 functional.py:74(split)
              303809816  237.415    0.000  237.415    0.000 {method 'copy' of 'numpy.ndarray' objects}
                5055057   19.368    0.000  230.152    0.000 tensor.py:460(split)
               33700380   24.855    0.000  216.916    0.000 wrapper.py:22(get_info)
                7413750   80.317    0.000  215.920    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                5055057  209.699    0.000  209.699    0.000 {function Tensor.split at 0x7fa3640ced30}
               35321736  204.019    0.000  204.019    0.000 {built-in method numpy.array}
               38833248  203.329    0.000  203.329    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   1652   57.877    0.035  202.390    0.123 memory.py:45(update_distribution)
               29593702  193.420    0.000  193.420    0.000 {method 't' of 'torch._C._TensorBase' objects}
               33700380  104.578    0.000  192.061    0.000 libenv.py:363(get_info)
              710113730  152.492    0.000  188.955    0.000 overrides.py:1086(<genexpr>)
              290755137  178.128    0.000  178.128    0.000 {built-in method torch._C._get_tracing_state}
                1618052  134.446    0.000  172.715    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   3304  142.579    0.043  160.161    0.048 {built-in method _pickle.loads}
              252230132  159.877    0.000  159.950    0.000 module.py:765(__getattr__)
               16445692   14.010    0.000  158.611    0.000 <__array_function__ internals>:2(prod)
                8090260  157.207    0.000  157.207    0.000 {built-in method gather}
               33700380  150.269    0.000  150.269    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                4854156  146.246    0.000  146.246    0.000 {built-in method torch._C._nn.mse_loss}
                1619051  141.640    0.000  143.696    0.000 agent.py:148(convert_values)
                1685019   13.759    0.000  142.600    0.000 environments.py:86(<listcomp>)
               16445732   10.521    0.000  141.957    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                5055054  140.398    0.000  140.398    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               22922445  117.609    0.000  133.330    0.000 module.py:781(__setattr__)
               29325837  132.022    0.000  132.022    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               16445692   17.784    0.000  131.436    0.000 fromnumeric.py:2881(prod)
               33700400   15.430    0.000  128.969    0.000 environments.py:89(reset)
             1202003279  118.363    0.000  118.363    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1618052  114.888    0.000  114.888    0.000 memory.py:43(<listcomp>)
               16445692   34.979    0.000  113.652    0.000 fromnumeric.py:70(_wrapreduction)
                1685019    8.274    0.000  106.341    0.000 collector.py:8(collect)
                3238084   11.891    0.000  103.745    0.000 tensor.py:576(__iter__)
               38833464   46.072    0.000  103.221    0.000 tensor.py:596(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8582541: <NOPEjumper_0> in cluster <dcc> Done

Job <NOPEjumper_0> was submitted from host <n-62-30-7> by user <s183914> in cluster <dcc> at Tue Dec 22 15:37:43 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec 23 06:39:18 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 23 06:39:18 2020
Terminated at Wed Dec 23 18:34:51 2020
Results reported at Wed Dec 23 18:34:51 2020

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

    CPU time :                                   43807.00 sec.
    Max Memory :                                 10282 MB
    Average Memory :                             10192.82 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               51158.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   42990 sec.
    Turnaround time :                            97028 sec.

The output (if any) is above this job summary.

