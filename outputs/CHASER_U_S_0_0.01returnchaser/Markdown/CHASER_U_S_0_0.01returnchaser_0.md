
    Name :                      CHASER_U_S_0_0.01returnchaser-0
    Discount :                  0.995
    Environment :               chaser
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.01
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11647180896 function calls (11455307222 primitive calls) in 82531.76 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82531.764 82531.764 {built-in method builtins.exec}
                      1    0.017    0.017 82531.764 82531.764 <string>:1(<module>)
                      1  612.273  612.273 82531.742 82531.742 main.py:92(main)
                1953568  344.832    0.000 57375.099    0.029 agent.py:84(learn)
                1874607  708.636    0.000 56440.274    0.030 agent.py:99(TD_learn)
                1874607  156.921    0.000 33078.014    0.018 memory.py:35(sample_distribution)
                1874607  294.821    0.000 32357.343    0.017 helpers.py:15(stack)
               17108346 20172.742    0.001 20172.742    0.001 {built-in method cat}
        205069263/13202209  964.021    0.000 13735.412    0.001 module.py:715(_call_impl)
                5702782  192.519    0.000 12723.253    0.002 agent.py:231(forward)
               18984060 11444.857    0.001 11444.907    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                1953568  169.753    0.000 9411.121    0.005 agent.py:70(chooseMulti)
               30389516  242.239    0.000 8599.043    0.000 container.py:115(forward)
                1953568   66.488    0.000 8272.457    0.004 environments.py:83(step)
              253298948 7885.420    0.000 7885.420    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1875606   82.791    0.000 6682.582    0.004 agent.py:58(rememberMulti)
                5623821   40.963    0.000 6500.659    0.001 grad_mode.py:23(decorate_context)
                5623821  245.916    0.000 6392.843    0.001 adam.py:55(step)
                1875606  207.699    0.000 6231.947    0.003 agent.py:62(<listcomp>)
                5623821 1218.611    0.000 5256.778    0.001 functional.py:53(adam)
                1953568   58.963    0.000 5122.297    0.003 environments.py:85(<listcomp>)
               39369237 1327.382    0.000 5107.618    0.000 helpers.py:8(clean)
                5623821   43.007    0.000 4831.292    0.001 tensor.py:181(backward)
                5623821   30.061    0.000 4788.285    0.001 __init__.py:68(backward)
                5623821 4614.073    0.001 4614.073    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               44993058 4417.156    0.000 4417.156    0.000 {built-in method as_tensor}
                1875606   80.252    0.000 3372.890    0.002 agent.py:82(<listcomp>)
               34216692   65.114    0.000 3194.569    0.000 conv.py:422(forward)
               34216692   80.712    0.000 3097.957    0.000 conv.py:414(_conv_forward)
               37512120  114.883    0.000 3077.533    0.000 exploration.py:34(epsilonGreedy)
               34216692 3002.750    0.000 3002.750    0.000 {built-in method conv2d}
                1953568   44.627    0.000 2854.151    0.001 environments.py:84(<listcomp>)
               39071360  157.806    0.000 2809.524    0.000 interop.py:274(step)
               45546292  108.626    0.000 2683.578    0.000 linear.py:92(forward)
               45546292  259.899    0.000 2522.004    0.000 functional.py:1669(linear)
                5702788  388.180    0.000 2088.059    0.000 rnn.py:110(flatten_parameters)
                5702782   77.067    0.000 1839.522    0.000 rnn.py:555(forward)
                5702782 1673.107    0.000 1673.107    0.000 {built-in method lstm}
              393667578  952.109    0.000 1592.683    0.000 tensor.py:933(grad)
               39919474 1455.724    0.000 1455.724    0.000 {built-in method addmm}
               39071360   19.182    0.000 1412.983    0.000 wrapper.py:25(act)
               39071360   53.853    0.000 1393.800    0.000 env.py:197(act)
                5623821  125.465    0.000 1366.380    0.000 optimizer.py:167(zero_grad)
               72184596   75.553    0.000 1346.259    0.000 activation.py:713(forward)
               39071360 1304.148    0.000 1308.137    0.000 libenv.py:352(act)
               72184596  103.050    0.000 1270.705    0.000 functional.py:1292(leaky_relu)
                5702785 1212.442    0.000 1212.442    0.000 {built-in method _cudnn_rnn_flatten_weight}
               72184596 1157.999    0.000 1157.999    0.000 {built-in method torch._C._nn.leaky_relu}
              112476420 1068.593    0.000 1068.593    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              112476420  881.942    0.000  881.942    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              495452326  273.757    0.000  812.704    0.000 overrides.py:1073(has_torch_function)
               78440597   62.387    0.000  782.645    0.000 extract_dict_ob.py:9(observe)
               78440597   37.162    0.000  720.257    0.000 wrapper.py:19(observe)
               78440597  162.798    0.000  683.096    0.000 libenv.py:344(observe)
               56238210  593.935    0.000  593.935    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   1953    1.193    0.001  589.993    0.302 agent.py:157(update_target_network)
               56238210  554.296    0.000  554.296    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              117511957  136.730    0.000  517.210    0.000 libenv.py:281(_maybe_copy_dict)
              552246284  205.606    0.000  514.625    0.000 {built-in method builtins.any}
                1875606    5.836    0.000  508.433    0.000 agent.py:249(avoid_similar_state)
               56238210  489.274    0.000  489.274    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              352537824  459.727    0.000  459.727    0.000 {method 'copy' of 'numpy.ndarray' objects}
               37512120  452.468    0.000  452.468    0.000 memory.py:17(inner)
               56238210  431.108    0.000  431.108    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               26562177  403.860    0.000  427.116    0.000 module.py:781(__setattr__)
               45546292  402.499    0.000  402.499    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5860704   12.382    0.000  401.763    0.000 functional.py:74(split)
                5860704   28.654    0.000  388.482    0.000 tensor.py:460(split)
              287926917  382.739    0.000  382.739    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                5623821   12.890    0.000  373.143    0.000 loss.py:445(forward)
               10901514  139.440    0.000  366.350    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                5623821   43.341    0.000  360.254    0.000 functional.py:2637(mse_loss)
                5860704  358.511    0.000  358.511    0.000 {function Tensor.split at 0x7f1b830d1d30}
               39071360   36.419    0.000  331.428    0.000 wrapper.py:22(get_info)
                   1953   83.798    0.043  311.742    0.160 memory.py:45(update_distribution)
               56238210  311.146    0.000  311.146    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1036450944  243.672    0.000  303.994    0.000 overrides.py:1086(<genexpr>)
               40949873  298.870    0.000  298.870    0.000 {built-in method numpy.array}
               39071360  148.667    0.000  295.008    0.000 libenv.py:363(get_info)
               11247642  292.412    0.000  292.412    0.000 {built-in method gather}
                1874607  217.700    0.000  286.725    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               23677775   24.614    0.000  267.337    0.000 <__array_function__ internals>:2(prod)
                   3906  227.565    0.058  251.499    0.064 {built-in method _pickle.loads}
               43431805  248.038    0.000  248.038    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               23677815   18.785    0.000  238.528    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                5702782   18.788    0.000  230.117    0.000 pooling.py:152(forward)
                1953568   23.541    0.000  229.521    0.000 environments.py:86(<listcomp>)
                1875606  201.927    0.000  229.265    0.000 agent.py:149(convert_values)
               39071360  223.083    0.000  223.083    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               23677775   30.465    0.000  219.743    0.000 fromnumeric.py:2881(prod)
                2024032  215.790    0.000  215.790    0.000 {built-in method tensor}
                5623821  215.561    0.000  215.561    0.000 {built-in method torch._C._nn.mse_loss}
                5702782   11.537    0.000  211.329    0.000 _jit_internal.py:257(fn)
               22811140  189.677    0.000  209.416    0.000 __init__.py:67(is_acceptable)
               39071380   33.384    0.000  206.030    0.000 environments.py:89(reset)
                5702782   11.998    0.000  198.758    0.000 functional.py:574(_max_pool2d)
                5626818  191.482    0.000  191.482    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               23677775   57.152    0.000  189.278    0.000 fromnumeric.py:70(_wrapreduction)
                5702782  185.983    0.000  185.983    0.000 {built-in method max_pool2d}
                1874607  176.069    0.000  176.069    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8557118: <CHASER_U_S_0_0.01returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0_0.01returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:12 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Dec 13 15:50:18 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec 13 15:50:18 2020
Terminated at Mon Dec 14 14:46:08 2020
Results reported at Mon Dec 14 14:46:08 2020

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

    CPU time :                                   91741.00 sec.
    Max Memory :                                 55034 MB
    Average Memory :                             54338.92 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6406.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82550 sec.
    Turnaround time :                            257876 sec.

The output (if any) is above this job summary.

