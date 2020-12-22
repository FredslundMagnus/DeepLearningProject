
    Name :                      U_S_0.1_0.1returnbossfight-0
    Discount :                  0.99
    Environment :               bossfight
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


      12532129785 function calls (12347883806 primitive calls) in 82552.26 seconds

##    Ordered by: cumulative time
   List reduced from 1362 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82552.262 82552.262 {built-in method builtins.exec}
                      1    0.059    0.059 82552.262 82552.262 <string>:1(<module>)
                      1  445.433  445.433 82552.201 82552.201 main.py:92(main)
                2149870  190.319    0.000 55488.676    0.026 agent.py:89(learn)
                2063042  610.077    0.000 54792.150    0.027 agent.py:102(TD_learn)
                2063042  155.904    0.000 32290.738    0.016 memory.py:35(sample_distribution)
                2063042  255.675    0.000 31609.865    0.015 helpers.py:15(stack)
               22953946 19457.143    0.001 19457.143    0.001 {built-in method cat}
               25103922 15822.960    0.001 15822.998    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        200917350/16677991  883.350    0.000 12169.748    0.001 module.py:715(_call_impl)
                2149870  214.510    0.000 11005.841    0.005 agent.py:72(chooseMulti)
                6275954  158.848    0.000 10627.727    0.002 agent.py:231(forward)
                2149870   58.381    0.000 8513.208    0.004 environments.py:83(step)
               29316727  230.248    0.000 7561.915    0.000 container.py:115(forward)
                2064033   39.707    0.000 6899.686    0.003 agent.py:58(rememberMulti)
                2064033  247.126    0.000 6645.038    0.003 agent.py:60(<listcomp>)
                6189126   41.224    0.000 6620.210    0.001 grad_mode.py:23(decorate_context)
                6189126  259.841    0.000 6509.279    0.001 adam.py:55(step)
              362127535 6371.488    0.000 6371.488    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6189126 1206.001    0.000 5318.191    0.001 functional.py:53(adam)
                2149870   54.313    0.000 4902.656    0.002 environments.py:85(<listcomp>)
               43343750 1247.672    0.000 4893.771    0.000 helpers.py:8(clean)
                6189126   45.661    0.000 4834.744    0.001 tensor.py:181(backward)
                6189126   30.133    0.000 4789.083    0.001 __init__.py:68(backward)
                6189126 4609.712    0.001 4609.712    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               49532876 4104.465    0.000 4104.465    0.000 {built-in method as_tensor}
                2149870   43.877    0.000 3362.049    0.002 environments.py:84(<listcomp>)
               42997400  157.114    0.000 3318.172    0.000 interop.py:274(step)
               37655724   67.618    0.000 3056.089    0.000 conv.py:422(forward)
               37655724   80.219    0.000 2956.327    0.000 conv.py:414(_conv_forward)
               37655724 2860.574    0.000 2860.574    0.000 {built-in method conv2d}
               37742549   85.005    0.000 2034.821    0.000 linear.py:92(forward)
               42997400   21.742    0.000 1995.559    0.000 wrapper.py:25(act)
               42997400   51.601    0.000 1973.816    0.000 env.py:197(act)
               37742549  229.749    0.000 1907.003    0.000 functional.py:1669(linear)
               42997400 1889.386    0.000 1893.479    0.000 libenv.py:352(act)
                6275960  373.981    0.000 1875.895    0.000 rnn.py:110(flatten_parameters)
              433238928  992.936    0.000 1653.563    0.000 tensor.py:933(grad)
                6275954   76.451    0.000 1620.923    0.000 rnn.py:555(forward)
                6275954 1457.855    0.000 1457.855    0.000 {built-in method lstm}
                2149870   81.767    0.000 1457.848    0.001 agent.py:87(<listcomp>)
                6189126  139.938    0.000 1423.556    0.000 optimizer.py:167(zero_grad)
               71185362   68.835    0.000 1206.659    0.000 activation.py:713(forward)
               42997400  121.617    0.000 1171.679    0.000 exploration.py:34(epsilonGreedy)
               71185362   97.058    0.000 1137.824    0.000 functional.py:1292(leaky_relu)
                6275957 1102.121    0.000 1102.121    0.000 {built-in method _cudnn_rnn_flatten_weight}
              123782520 1088.444    0.000 1088.444    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4212911   16.261    0.000 1066.685    0.000 agent.py:247(avoid_similar_state)
               71185362 1031.612    0.000 1031.612    0.000 {built-in method torch._C._nn.leaky_relu}
               31292942 1029.419    0.000 1029.419    0.000 {built-in method addmm}
              123782520  901.040    0.000  901.040    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              532872983  280.770    0.000  812.035    0.000 overrides.py:1073(has_torch_function)
               86341150   63.862    0.000  726.427    0.000 extract_dict_ob.py:9(observe)
               86341150   37.166    0.000  662.565    0.000 wrapper.py:19(observe)
               86341150  168.153    0.000  625.399    0.000 libenv.py:344(observe)
               61891260  604.722    0.000  604.722    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               61891260  551.892    0.000  551.892    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              582993808  204.574    0.000  509.929    0.000 {built-in method builtins.any}
               61891260  506.383    0.000  506.383    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   2106    0.884    0.000  506.207    0.240 agent.py:157(update_target_network)
              129338550  135.340    0.000  451.503    0.000 libenv.py:281(_maybe_copy_dict)
               61891260  438.502    0.000  438.502    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              402263595  394.186    0.000  394.186    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              388017756  388.513    0.000  388.513    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6189126   13.611    0.000  371.702    0.000 loss.py:445(forward)
                6189126   44.128    0.000  358.091    0.000 functional.py:2637(mse_loss)
               11177191  135.410    0.000  357.064    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6449610   12.218    0.000  343.713    0.000 functional.py:74(split)
               29231735  312.472    0.000  336.758    0.000 module.py:781(__setattr__)
               41280660  336.561    0.000  336.561    0.000 memory.py:17(inner)
                6449610   26.035    0.000  330.620    0.000 tensor.py:460(split)
               61891260  320.880    0.000  320.880    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               42997400   34.558    0.000  320.400    0.000 wrapper.py:22(get_info)
                6449610  303.204    0.000  303.204    0.000 {function Tensor.split at 0x7f2fc2696ca0}
             1103488515  244.437    0.000  300.635    0.000 overrides.py:1086(<genexpr>)
               42997400  150.161    0.000  285.842    0.000 libenv.py:363(get_info)
               37742549  283.882    0.000  283.882    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2063042  216.344    0.000  280.803    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   2106   74.385    0.035  265.640    0.126 memory.py:45(update_distribution)
               45064654  260.389    0.000  260.389    0.000 {built-in method numpy.array}
               24417564   23.174    0.000  258.000    0.000 <__array_function__ internals>:2(prod)
               10315210  232.306    0.000  232.306    0.000 {built-in method gather}
               24417604   17.793    0.000  230.639    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                   4212  194.029    0.046  217.605    0.052 {built-in method _pickle.loads}
                4128066   19.650    0.000  214.941    0.000 tensor.py:576(__iter__)
                6189126  212.907    0.000  212.907    0.000 {built-in method torch._C._nn.mse_loss}
               24417564   28.948    0.000  212.846    0.000 fromnumeric.py:2881(prod)
                6275954   15.769    0.000  212.492    0.000 pooling.py:152(forward)
               42997400  204.402    0.000  204.402    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6275954   11.511    0.000  196.723    0.000 _jit_internal.py:257(fn)
                6449607  196.667    0.000  196.667    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2064042  193.645    0.000  196.433    0.000 agent.py:148(convert_values)
                2149870   22.892    0.000  190.123    0.000 environments.py:86(<listcomp>)
                4128066  188.430    0.000  188.430    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               37395240  187.147    0.000  187.147    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6275954   12.369    0.000  184.146    0.000 functional.py:574(_max_pool2d)
               24417564   54.472    0.000  183.898    0.000 fromnumeric.py:70(_wrapreduction)
               61891506   79.334    0.000  173.366    0.000 tensor.py:596(__hash__)
                6275954  171.054    0.000  171.054    0.000 {built-in method max_pool2d}
               42997420   27.292    0.000  167.244    0.000 environments.py:89(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8578472: <U_S_0.1_0.1returnbossfight_0> in cluster <dcc> Done

Job <U_S_0.1_0.1returnbossfight_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec 20 03:01:51 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Dec 21 08:47:28 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec 21 08:47:28 2020
Terminated at Tue Dec 22 07:43:33 2020
Results reported at Tue Dec 22 07:43:33 2020

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

    CPU time :                                   76944.00 sec.
    Max Memory :                                 56056 MB
    Average Memory :                             55354.03 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5384.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   74051 sec.
    Turnaround time :                            189702 sec.

The output (if any) is above this job summary.

