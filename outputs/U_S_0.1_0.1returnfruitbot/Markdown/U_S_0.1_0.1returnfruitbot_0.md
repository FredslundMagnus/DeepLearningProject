
    Name :                      U_S_0.1_0.1returnfruitbot-0
    Discount :                  0.99
    Environment :               fruitbot
    Hours :                     23
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
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13694386970 function calls (13492820812 primitive calls) in 82519.42 seconds

##    Ordered by: cumulative time
   List reduced from 1362 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82519.416 82519.416 {built-in method builtins.exec}
                      1    0.037    0.037 82519.416 82519.416 <string>:1(<module>)
                      1  509.207  509.207 82519.377 82519.377 main.py:92(main)
                2351953  213.184    0.000 53318.364    0.023 agent.py:89(learn)
                2257000  671.434    0.000 52518.708    0.023 agent.py:102(TD_learn)
                2257000  188.734    0.000 27820.823    0.012 memory.py:35(sample_distribution)
                2257000  364.110    0.000 27024.417    0.012 helpers.py:15(stack)
               27463918 17414.895    0.001 17414.929    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        219805443/18245905  993.516    0.000 13466.604    0.001 module.py:715(_call_impl)
               25111859 13403.601    0.001 13403.601    0.001 {built-in method cat}
                2351953  236.946    0.000 12066.334    0.005 agent.py:72(chooseMulti)
                6865953  180.639    0.000 11767.898    0.002 agent.py:231(forward)
                2351953   68.218    0.000 8837.019    0.004 environments.py:83(step)
               32072764  242.061    0.000 8329.396    0.000 container.py:115(forward)
                2257990   45.273    0.000 7608.118    0.003 agent.py:58(rememberMulti)
                2257990  258.466    0.000 7319.193    0.003 agent.py:60(<listcomp>)
                6771000   47.295    0.000 7190.917    0.001 grad_mode.py:23(decorate_context)
                6771000  290.606    0.000 7066.668    0.001 adam.py:55(step)
              397010126 7010.716    0.000 7010.716    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6771000 1307.046    0.000 5770.252    0.001 functional.py:53(adam)
                2351953   63.506    0.000 5369.999    0.002 environments.py:85(<listcomp>)
               47265415 1368.037    0.000 5336.675    0.000 helpers.py:8(clean)
                6771000   51.381    0.000 5315.732    0.001 tensor.py:181(backward)
                6771000   32.342    0.000 5264.352    0.001 __init__.py:68(backward)
                6771000 5067.646    0.001 5067.646    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               54036415 4555.063    0.000 4555.063    0.000 {built-in method as_tensor}
               41195718   72.299    0.000 3375.500    0.000 conv.py:422(forward)
               41195718   91.508    0.000 3267.277    0.000 conv.py:414(_conv_forward)
                2351953   48.618    0.000 3216.045    0.001 environments.py:84(<listcomp>)
               47039060  170.738    0.000 3167.427    0.000 interop.py:274(step)
               41195718 3158.988    0.000 3158.988    0.000 {built-in method conv2d}
               41290668   89.811    0.000 2235.980    0.000 linear.py:92(forward)
               41290668  253.425    0.000 2100.316    0.000 functional.py:1669(linear)
                6865959  416.268    0.000 2087.671    0.000 rnn.py:110(flatten_parameters)
                6865953   86.655    0.000 1812.520    0.000 rnn.py:555(forward)
              473970108 1058.882    0.000 1773.163    0.000 tensor.py:933(grad)
               47039060   21.777    0.000 1723.643    0.000 wrapper.py:25(act)
               47039060   60.273    0.000 1701.866    0.000 env.py:197(act)
                6865953 1626.447    0.000 1626.447    0.000 {built-in method lstm}
               47039060 1605.294    0.000 1609.736    0.000 libenv.py:352(act)
                2351953   87.162    0.000 1572.856    0.001 agent.py:87(<listcomp>)
                6771000  152.835    0.000 1524.047    0.000 optimizer.py:167(zero_grad)
               77877434   73.949    0.000 1326.787    0.000 activation.py:713(forward)
               47039060  128.209    0.000 1262.871    0.000 exploration.py:34(epsilonGreedy)
               77877434  106.583    0.000 1252.838    0.000 functional.py:1292(leaky_relu)
                6865956 1214.690    0.000 1214.690    0.000 {built-in method _cudnn_rnn_flatten_weight}
                4608952   18.342    0.000 1177.567    0.000 agent.py:247(avoid_similar_state)
              135420000 1176.453    0.000 1176.453    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               77877434 1135.944    0.000 1135.944    0.000 {built-in method torch._C._nn.leaky_relu}
               34234812 1132.732    0.000 1132.732    0.000 {built-in method addmm}
              135420000  975.389    0.000  975.389    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              582971022  300.583    0.000  876.219    0.000 overrides.py:1073(has_torch_function)
               94304475   69.635    0.000  786.677    0.000 extract_dict_ob.py:9(observe)
               94304475   38.667    0.000  717.042    0.000 wrapper.py:19(observe)
               94304475  182.081    0.000  678.375    0.000 libenv.py:344(observe)
               67710000  658.037    0.000  658.037    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67710000  601.356    0.000  601.356    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   2304    1.010    0.000  586.472    0.255 agent.py:157(update_target_network)
              637803714  223.918    0.000  552.337    0.000 {built-in method builtins.any}
               67710000  550.583    0.000  550.583    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              141343535  148.505    0.000  492.360    0.000 libenv.py:281(_maybe_copy_dict)
               67710000  479.010    0.000  479.010    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              441226835  440.095    0.000  440.095    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              424032909  420.251    0.000  420.251    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6771000   15.425    0.000  408.607    0.000 loss.py:445(forward)
               45159800  395.861    0.000  395.861    0.000 memory.py:17(inner)
                7055859   13.051    0.000  395.644    0.000 functional.py:74(split)
                6771000   48.002    0.000  393.182    0.000 functional.py:2637(mse_loss)
                7055859   29.500    0.000  381.643    0.000 tensor.py:460(split)
               31979647  355.288    0.000  380.636    0.000 module.py:781(__setattr__)
               11375212  142.573    0.000  365.875    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7055859  350.665    0.000  350.665    0.000 {function Tensor.split at 0x7f7db7cedca0}
               47039060   37.855    0.000  348.656    0.000 wrapper.py:22(get_info)
               67710000  340.970    0.000  340.970    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1207232712  260.272    0.000  322.872    0.000 overrides.py:1086(<genexpr>)
                2257000  242.999    0.000  315.929    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               41290668  313.824    0.000  313.824    0.000 {method 't' of 'torch._C._TensorBase' objects}
               47039060  163.144    0.000  310.802    0.000 libenv.py:363(get_info)
                   2304   84.886    0.037  301.613    0.131 memory.py:45(update_distribution)
               49300668  293.466    0.000  293.466    0.000 {built-in method numpy.array}
               25007564   23.731    0.000  263.703    0.000 <__array_function__ internals>:2(prod)
                   4608  232.665    0.050  258.687    0.056 {built-in method _pickle.loads}
               11285000  257.953    0.000  257.953    0.000 {built-in method gather}
                4515980   21.161    0.000  243.652    0.000 tensor.py:576(__iter__)
                6865953   22.259    0.000  236.528    0.000 pooling.py:152(forward)
               25007604   17.531    0.000  235.695    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6771000  235.246    0.000  235.246    0.000 {built-in method torch._C._nn.mse_loss}
               47039060  222.823    0.000  222.823    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25007564   29.453    0.000  218.164    0.000 fromnumeric.py:2881(prod)
                7055856  217.702    0.000  217.702    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                4515980  215.148    0.000  215.148    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2257999  211.858    0.000  215.013    0.000 agent.py:148(convert_values)
                6865953   12.838    0.000  214.269    0.000 _jit_internal.py:257(fn)
               40910859  206.191    0.000  206.191    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6865953   13.040    0.000  200.256    0.000 functional.py:574(_max_pool2d)
                2257000  197.459    0.000  197.459    0.000 memory.py:43(<listcomp>)
               25007564   55.576    0.000  188.711    0.000 fromnumeric.py:70(_wrapreduction)
               67710246   87.469    0.000  188.038    0.000 tensor.py:596(__hash__)
                6865953  186.319    0.000  186.319    0.000 {built-in method max_pool2d}
                2351953   26.623    0.000  182.757    0.000 environments.py:86(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8575820: <U_S_0.1_0.1returnfruitbot_0> in cluster <dcc> Done

Job <U_S_0.1_0.1returnfruitbot_0> was submitted from host <n-62-30-3> by user <s183914> in cluster <dcc> at Fri Dec 18 16:26:01 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Dec 18 23:12:04 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 18 23:12:04 2020
Terminated at Sat Dec 19 22:07:29 2020
Results reported at Sat Dec 19 22:07:29 2020

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

    CPU time :                                   87002.00 sec.
    Max Memory :                                 56820 MB
    Average Memory :                             56096.84 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4620.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82526 sec.
    Turnaround time :                            106888 sec.

The output (if any) is above this job summary.

