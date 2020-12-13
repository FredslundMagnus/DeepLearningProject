
    Name :                      CHASER_U_S_0.2_0returnchaser-0
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
    Uncertainty weight :        0.2
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14961409657 function calls (14714287487 primitive calls) in 82528.83 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82528.830 82528.830 {built-in method builtins.exec}
                      1    0.028    0.028 82528.830 82528.830 <string>:1(<module>)
                      1  547.580  547.580 82528.800 82528.800 main.py:92(main)
                2515605  268.198    0.000 54422.855    0.022 agent.py:84(learn)
                2414655  805.354    0.000 53555.879    0.022 agent.py:99(TD_learn)
                2414655  169.828    0.000 26498.121    0.011 memory.py:35(sample_distribution)
                2414655  251.373    0.000 25714.622    0.011 helpers.py:15(stack)
        264120084/17004534 1110.647    0.000 15314.101    0.001 module.py:715(_call_impl)
                7344915  215.584    0.000 14152.541    0.002 agent.py:231(forward)
               24450507 13263.999    0.001 13264.051    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               22034745 11840.853    0.001 11840.853    0.001 {built-in method cat}
                2515605  187.577    0.000 11529.213    0.005 agent.py:70(chooseMulti)
               39140229  290.774    0.000 9849.832    0.000 container.py:115(forward)
              328822401 9473.850    0.000 9473.850    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2515605   70.101    0.000 9181.985    0.004 environments.py:83(step)
                7243965   48.243    0.000 7766.542    0.001 grad_mode.py:23(decorate_context)
                7243965  299.205    0.000 7641.187    0.001 adam.py:55(step)
                2415654   90.383    0.000 6644.864    0.003 agent.py:58(rememberMulti)
                7243965 1435.836    0.000 6258.589    0.001 functional.py:53(adam)
                2415654  224.241    0.000 6182.596    0.003 agent.py:62(<listcomp>)
                2515605   62.483    0.000 5711.861    0.002 environments.py:85(<listcomp>)
               50662118 1444.653    0.000 5694.732    0.000 helpers.py:8(clean)
                7243965   50.995    0.000 5633.310    0.001 tensor.py:181(backward)
                7243965   33.491    0.000 5582.316    0.001 __init__.py:68(backward)
                7243965 5377.333    0.001 5377.333    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2415654   91.704    0.000 5008.466    0.002 agent.py:82(<listcomp>)
               57906083 4830.616    0.000 4830.616    0.000 {built-in method as_tensor}
               48313080  137.771    0.000 4678.124    0.000 exploration.py:34(epsilonGreedy)
               44069490   77.352    0.000 3649.237    0.000 conv.py:422(forward)
               44069490   90.250    0.000 3533.642    0.000 conv.py:414(_conv_forward)
               44069490 3426.418    0.000 3426.418    0.000 {built-in method conv2d}
                2515605   52.289    0.000 3171.561    0.001 environments.py:84(<listcomp>)
               50312100  179.190    0.000 3119.272    0.000 interop.py:274(step)
               58661367  126.491    0.000 3065.818    0.000 linear.py:92(forward)
               58661367  311.031    0.000 2878.010    0.000 functional.py:1669(linear)
                7344921  410.243    0.000 2280.637    0.000 rnn.py:110(flatten_parameters)
              507077658 1151.898    0.000 1934.645    0.000 tensor.py:933(grad)
                7344915   84.563    0.000 1799.820    0.000 rnn.py:555(forward)
               51414405 1672.189    0.000 1672.189    0.000 {built-in method addmm}
                7243965  164.181    0.000 1667.806    0.000 optimizer.py:167(zero_grad)
                7344915 1616.575    0.000 1616.575    0.000 {built-in method lstm}
               50312100   22.559    0.000 1569.038    0.000 wrapper.py:25(act)
               92970288   86.886    0.000 1549.392    0.000 activation.py:713(forward)
               50312100   65.310    0.000 1546.479    0.000 env.py:197(act)
               92970288  118.183    0.000 1462.506    0.000 functional.py:1292(leaky_relu)
               50312100 1440.810    0.000 1446.141    0.000 libenv.py:352(act)
                7344918 1372.797    0.000 1372.797    0.000 {built-in method _cudnn_rnn_flatten_weight}
               92970288 1332.638    0.000 1332.638    0.000 {built-in method torch._C._nn.leaky_relu}
              144879300 1272.634    0.000 1272.634    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              144879300 1059.410    0.000 1059.410    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              638178921  348.375    0.000  999.982    0.000 overrides.py:1073(has_torch_function)
              100974218   74.174    0.000  845.004    0.000 extract_dict_ob.py:9(observe)
              100974218   40.662    0.000  770.830    0.000 wrapper.py:19(observe)
              100974218  187.358    0.000  730.168    0.000 libenv.py:344(observe)
               72439650  703.852    0.000  703.852    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               72439650  659.812    0.000  659.812    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              711328242  262.189    0.000  628.349    0.000 {built-in method builtins.any}
                   2515    0.974    0.000  598.778    0.238 agent.py:157(update_target_network)
               72439650  587.880    0.000  587.880    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2415654    6.748    0.000  580.402    0.000 agent.py:249(avoid_similar_state)
              151286318  159.020    0.000  536.180    0.000 libenv.py:281(_maybe_copy_dict)
               72439650  514.716    0.000  514.716    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              453861469  463.575    0.000  463.575    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7243965   14.204    0.000  432.343    0.000 loss.py:445(forward)
               58661367  427.573    0.000  427.573    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7243965   54.808    0.000  418.138    0.000 functional.py:2637(mse_loss)
              373472431  407.800    0.000  407.800    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7546815   14.258    0.000  397.206    0.000 functional.py:74(split)
               34210805  371.215    0.000  397.038    0.000 module.py:781(__setattr__)
                7546815   32.331    0.000  381.959    0.000 tensor.py:460(split)
               50312100   40.760    0.000  378.330    0.000 wrapper.py:22(get_info)
               11440797  145.491    0.000  377.876    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               72439650  375.985    0.000  375.985    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1335019209  291.235    0.000  360.504    0.000 overrides.py:1086(<genexpr>)
                7546815  347.955    0.000  347.955    0.000 {function Tensor.split at 0x7f4980759d30}
               50312100  174.499    0.000  337.570    0.000 libenv.py:363(get_info)
                2414655  257.017    0.000  334.419    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               48313080  333.557    0.000  333.557    0.000 memory.py:17(inner)
               14487930  323.101    0.000  323.101    0.000 {built-in method gather}
                   2515   90.046    0.036  322.024    0.128 memory.py:45(update_distribution)
               52731785  316.089    0.000  316.089    0.000 {built-in method numpy.array}
               25296389   24.483    0.000  275.344    0.000 <__array_function__ internals>:2(prod)
               55940865  273.438    0.000  273.438    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2415654  223.565    0.000  266.526    0.000 agent.py:149(convert_values)
                   5030  222.619    0.044  249.979    0.050 {built-in method _pickle.loads}
               50312100  246.880    0.000  246.880    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25296429   18.470    0.000  246.342    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7243965  246.051    0.000  246.051    0.000 {built-in method torch._C._nn.mse_loss}
                7344915   16.351    0.000  240.579    0.000 pooling.py:152(forward)
                2515605   27.268    0.000  228.463    0.000 environments.py:86(<listcomp>)
               25296389   31.100    0.000  227.872    0.000 fromnumeric.py:2881(prod)
                7344915   13.463    0.000  224.228    0.000 _jit_internal.py:257(fn)
                7246962  210.433    0.000  210.433    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                7344915   13.840    0.000  209.610    0.000 functional.py:574(_max_pool2d)
                2606792  206.436    0.000  206.436    0.000 {built-in method tensor}
               50312120   32.266    0.000  201.226    0.000 environments.py:89(reset)
               29379672  178.746    0.000  199.473    0.000 __init__.py:67(is_acceptable)
               72439896   87.347    0.000  198.251    0.000 tensor.py:596(__hash__)
               25296389   57.429    0.000  196.772    0.000 fromnumeric.py:70(_wrapreduction)
                7344915  194.912    0.000  194.912    0.000 {built-in method max_pool2d}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8557115: <CHASER_U_S_0.2_0returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0.2_0returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:11 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec 12 14:58:11 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec 12 14:58:11 2020
Terminated at Sun Dec 13 13:53:50 2020
Results reported at Sun Dec 13 13:53:50 2020

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

    CPU time :                                   85500.00 sec.
    Max Memory :                                 55151 MB
    Average Memory :                             54403.14 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6289.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82540 sec.
    Turnaround time :                            168339 sec.

The output (if any) is above this job summary.

