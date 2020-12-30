
    Name :                      NOPE_final_leaper-0
    Discount :                  0.995
    Environment :               leaper
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


      9953695154 function calls (9802030986 primitive calls) in 64522.67 seconds

##    Ordered by: cumulative time
   List reduced from 1354 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 64522.668 64522.668 {built-in method builtins.exec}
                      1    0.030    0.030 64522.668 64522.668 <string>:1(<module>)
                      1  369.996  369.996 64522.638 64522.638 main.py:91(main)
                1996969  136.710    0.000 42962.404    0.022 agent.py:93(learn)
                1918008  418.789    0.000 42377.608    0.022 agent.py:106(TD_learn)
                1918008  130.926    0.000 21019.462    0.011 memory.py:35(sample_distribution)
                1918008  221.673    0.000 20389.113    0.011 helpers.py:15(stack)
        161326611/9669001  722.506    0.000 11610.159    0.001 module.py:715(_call_impl)
                5832985  154.730    0.000 11221.954    0.002 agent.py:235(forward)
               17499063 10424.678    0.001 10424.692    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               17498955 9377.049    0.001 9377.049    0.001 {built-in method cat}
                1996969   45.405    0.000 7579.509    0.004 agent.py:72(chooseMulti)
                1996969   53.402    0.000 7563.693    0.004 environments.py:83(step)
              259312999 7236.622    0.000 7236.622    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               23331940  203.471    0.000 7020.686    0.000 container.py:115(forward)
                3836016   27.309    0.000 6437.954    0.002 grad_mode.py:23(decorate_context)
                3836016  186.662    0.000 6366.892    0.002 adam.py:55(step)
                1918998    7.903    0.000 5886.196    0.003 agent.py:58(rememberMulti)
                1918998  242.500    0.000 5878.293    0.003 agent.py:63(<listcomp>)
                3836016 1172.031    0.000 5461.976    0.001 functional.py:53(adam)
                1996969   55.375    0.000 4894.086    0.002 environments.py:85(<listcomp>)
               40130985 1147.459    0.000 4865.885    0.000 helpers.py:8(clean)
                3836016   31.214    0.000 4544.691    0.001 tensor.py:181(backward)
                3836016   20.430    0.000 4513.477    0.001 __init__.py:68(backward)
                3836016 4384.456    0.001 4384.456    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               45885009 4220.598    0.000 4220.598    0.000 {built-in method as_tensor}
               34997910   60.575    0.000 3277.870    0.000 conv.py:422(forward)
               34997910   68.080    0.000 3187.173    0.000 conv.py:414(_conv_forward)
               34997910 3105.951    0.000 3105.951    0.000 {built-in method conv2d}
                1919007   87.069    0.000 3051.247    0.002 agent.py:88(<listcomp>)
               38380140  119.989    0.000 2713.383    0.000 exploration.py:34(epsilonGreedy)
                1996969   41.863    0.000 2444.351    0.001 environments.py:84(<listcomp>)
               39939380  153.750    0.000 2402.487    0.000 interop.py:274(step)
                5832991  344.734    0.000 2119.028    0.000 rnn.py:110(flatten_parameters)
                5832985   66.440    0.000 1508.466    0.000 rnn.py:555(forward)
               23331940   51.878    0.000 1436.239    0.000 linear.py:92(forward)
                5832988 1367.245    0.000 1367.245    0.000 {built-in method _cudnn_rnn_flatten_weight}
                5832985 1359.540    0.000 1359.540    0.000 {built-in method lstm}
               23331940   91.204    0.000 1358.876    0.000 functional.py:1669(linear)
              322225452  848.849    0.000 1328.288    0.000 tensor.py:933(grad)
                3836016  123.581    0.000 1274.271    0.000 optimizer.py:167(zero_grad)
               58329850   54.260    0.000 1200.573    0.000 activation.py:713(forward)
               92064384 1166.937    0.000 1166.937    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               58329850   76.449    0.000 1146.313    0.000 functional.py:1292(leaky_relu)
               39939380   17.399    0.000 1122.315    0.000 wrapper.py:25(act)
               39939380   59.058    0.000 1104.916    0.000 env.py:197(act)
               58329850 1062.599    0.000 1062.599    0.000 {built-in method torch._C._nn.leaky_relu}
               39939380 1008.066    0.000 1011.617    0.000 libenv.py:352(act)
               92064384  969.046    0.000  969.046    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               23331940  931.854    0.000  931.854    0.000 {built-in method addmm}
               80070365   63.891    0.000  688.984    0.000 extract_dict_ob.py:9(observe)
               80070365   33.437    0.000  625.093    0.000 wrapper.py:19(observe)
               46032192  596.790    0.000  596.790    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               80070365  159.412    0.000  591.657    0.000 libenv.py:344(observe)
              391589800  209.228    0.000  578.561    0.000 overrides.py:1073(has_torch_function)
               46032192  548.829    0.000  548.829    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               46032192  516.927    0.000  516.927    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46032192  474.901    0.000  474.901    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   1957    0.780    0.000  448.087    0.229 agent.py:161(update_target_network)
              120009745  127.472    0.000  425.120    0.000 libenv.py:281(_maybe_copy_dict)
              287140695  412.890    0.000  412.890    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              360031192  374.391    0.000  374.391    0.000 {method 'copy' of 'numpy.ndarray' objects}
               10944597  144.841    0.000  368.834    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               46032192  354.532    0.000  354.532    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              422593796  141.662    0.000  350.601    0.000 {built-in method builtins.any}
               39939380   33.194    0.000  313.224    0.000 wrapper.py:22(get_info)
               27169791  290.700    0.000  311.218    0.000 module.py:781(__setattr__)
                5990907   10.876    0.000  299.963    0.000 functional.py:74(split)
                5990907   25.600    0.000  288.289    0.000 tensor.py:460(split)
               39939380  146.705    0.000  280.031    0.000 libenv.py:363(get_info)
                3836016    9.487    0.000  275.287    0.000 loss.py:445(forward)
                1918008  212.290    0.000  275.041    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                3836016   28.973    0.000  265.800    0.000 functional.py:2637(mse_loss)
                5990907  261.360    0.000  261.360    0.000 {function Tensor.split at 0x7f45471dbd30}
               38379960  260.857    0.000  260.857    0.000 memory.py:17(inner)
               39939380  260.074    0.000  260.074    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               23807342   22.540    0.000  259.731    0.000 <__array_function__ internals>:2(prod)
               41861302  239.334    0.000  239.334    0.000 {built-in method numpy.array}
                   1957   68.183    0.035  236.645    0.121 memory.py:45(update_distribution)
               23807382   17.525    0.000  233.384    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               23331940  228.995    0.000  228.995    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5832985   15.865    0.000  219.349    0.000 pooling.py:152(forward)
               23807342   29.026    0.000  215.859    0.000 fromnumeric.py:2881(prod)
              806511540  164.698    0.000  206.011    0.000 overrides.py:1086(<genexpr>)
                7672032  205.048    0.000  205.048    0.000 {built-in method gather}
                5832985    9.893    0.000  203.485    0.000 _jit_internal.py:257(fn)
                1919007  172.189    0.000  193.857    0.000 agent.py:152(convert_values)
                5832985   10.746    0.000  192.559    0.000 functional.py:574(_max_pool2d)
                   3914  167.602    0.043  189.978    0.049 {built-in method _pickle.loads}
               23807342   51.653    0.000  186.833    0.000 fromnumeric.py:70(_wrapreduction)
                5832985  181.107    0.000  181.107    0.000 {built-in method max_pool2d}
               27088995  179.152    0.000  179.152    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                1996969   23.654    0.000  171.854    0.000 environments.py:86(<listcomp>)
                3836016  169.620    0.000  169.620    0.000 {built-in method torch._C._nn.mse_loss}
               23331952  141.341    0.000  160.628    0.000 __init__.py:67(is_acceptable)
               39939400   28.214    0.000  148.252    0.000 environments.py:89(reset)
                1918008  146.391    0.000  146.391    0.000 memory.py:43(<listcomp>)
               25727307  138.059    0.000  138.059    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                1996969   14.855    0.000  134.161    0.000 collector.py:8(collect)
               46032408   60.133    0.000  128.824    0.000 tensor.py:596(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 8587605: <NOPE_final_leaper_0> in cluster <dcc> Done

Job <NOPE_final_leaper_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 25 20:01:59 2020
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Dec 25 20:02:01 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 25 20:02:01 2020
Terminated at Sat Dec 26 13:57:32 2020
Results reported at Sat Dec 26 13:57:32 2020

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

    CPU time :                                   66426.00 sec.
    Max Memory :                                 55940 MB
    Average Memory :                             55191.17 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5500.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64594 sec.
    Turnaround time :                            64533 sec.

The output (if any) is above this job summary.

