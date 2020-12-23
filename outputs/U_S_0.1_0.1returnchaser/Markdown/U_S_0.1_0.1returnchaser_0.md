
    Name :                      U_S_0.1_0.1returnchaser-0
    Discount :                  0.99
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
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14138654937 function calls (13930510586 primitive calls) in 82536.53 seconds

##    Ordered by: cumulative time
   List reduced from 1362 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82536.527 82536.527 {built-in method builtins.exec}
                      1    0.046    0.046 82536.527 82536.527 <string>:1(<module>)
                      1  500.047  500.047 82536.478 82536.478 main.py:92(main)
                2428000  216.014    0.000 52847.344    0.022 agent.py:89(learn)
                2331048  677.157    0.000 52046.219    0.022 agent.py:102(TD_learn)
                2331048  178.611    0.000 26708.277    0.011 memory.py:35(sample_distribution)
                2331048  291.766    0.000 25935.973    0.011 helpers.py:15(stack)
               28360490 17847.617    0.001 17847.618    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        226980018/18842287 1001.642    0.000 13647.130    0.001 module.py:715(_call_impl)
                2428000  242.269    0.000 12428.785    0.005 agent.py:72(chooseMulti)
               25932384 12219.868    0.000 12219.868    0.000 {built-in method cat}
                7090096  176.438    0.000 11920.931    0.002 agent.py:231(forward)
                2428000   65.004    0.000 8799.366    0.004 environments.py:83(step)
               33119431  259.395    0.000 8505.500    0.000 container.py:115(forward)
                2332038   45.869    0.000 7759.824    0.003 agent.py:58(rememberMulti)
                6993144   46.110    0.000 7525.266    0.001 grad_mode.py:23(decorate_context)
                2332038  276.055    0.000 7463.348    0.003 agent.py:60(<listcomp>)
                6993144  292.359    0.000 7403.420    0.001 adam.py:55(step)
              410301302 7150.994    0.000 7150.994    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6993144 1379.872    0.000 6059.022    0.001 functional.py:53(adam)
                2428000   62.448    0.000 5518.942    0.002 environments.py:85(<listcomp>)
               48862813 1397.191    0.000 5495.937    0.000 helpers.py:8(clean)
                6993144   50.922    0.000 5421.528    0.001 tensor.py:181(backward)
                6993144   31.126    0.000 5370.606    0.001 __init__.py:68(backward)
                6993144 5175.077    0.001 5175.077    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               55855957 4645.021    0.000 4645.021    0.000 {built-in method as_tensor}
               42540576   75.054    0.000 3444.309    0.000 conv.py:422(forward)
               42540576   87.680    0.000 3333.590    0.000 conv.py:414(_conv_forward)
               42540576 3230.081    0.000 3230.081    0.000 {built-in method conv2d}
                2428000   49.359    0.000 3009.899    0.001 environments.py:84(<listcomp>)
               48560000  178.921    0.000 2960.540    0.000 interop.py:274(step)
               42637525   94.597    0.000 2279.883    0.000 linear.py:92(forward)
               42637525  261.171    0.000 2140.250    0.000 functional.py:1669(linear)
                7090102  417.083    0.000 2125.710    0.000 rnn.py:110(flatten_parameters)
              489520188 1109.299    0.000 1863.561    0.000 tensor.py:933(grad)
                7090096   81.187    0.000 1784.059    0.000 rnn.py:555(forward)
                2428000   88.254    0.000 1630.635    0.001 agent.py:87(<listcomp>)
                7090096 1606.346    0.000 1606.346    0.000 {built-in method lstm}
                6993144  155.879    0.000 1604.225    0.000 optimizer.py:167(zero_grad)
               48560000   23.432    0.000 1479.180    0.000 wrapper.py:25(act)
               48560000   59.113    0.000 1455.748    0.000 env.py:197(act)
               48560000 1358.817    0.000 1363.527    0.000 libenv.py:352(act)
               80419054   73.951    0.000 1354.522    0.000 activation.py:713(forward)
               48560000  131.099    0.000 1303.480    0.000 exploration.py:34(epsilonGreedy)
               80419054  107.430    0.000 1280.571    0.000 functional.py:1292(leaky_relu)
                7090099 1257.419    0.000 1257.419    0.000 {built-in method _cudnn_rnn_flatten_weight}
              139862880 1226.895    0.000 1226.895    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4759047   17.720    0.000 1203.638    0.000 agent.py:247(avoid_similar_state)
               80419054 1163.052    0.000 1163.052    0.000 {built-in method torch._C._nn.leaky_relu}
               35353528 1144.721    0.000 1144.721    0.000 {built-in method addmm}
              139862880 1033.074    0.000 1033.074    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              602089399  312.287    0.000  931.513    0.000 overrides.py:1073(has_torch_function)
               97422813   73.140    0.000  796.238    0.000 extract_dict_ob.py:9(observe)
               97422813   41.322    0.000  723.097    0.000 wrapper.py:19(observe)
               69931440  685.771    0.000  685.771    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               97422813  178.734    0.000  681.776    0.000 libenv.py:344(observe)
               69931440  626.796    0.000  626.796    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              658713236  239.742    0.000  588.723    0.000 {built-in method builtins.any}
                   2380    0.974    0.000  585.112    0.246 agent.py:157(update_target_network)
               69931440  574.615    0.000  574.615    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               69931440  509.354    0.000  509.354    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              145982813  153.576    0.000  502.482    0.000 libenv.py:281(_maybe_copy_dict)
              455783916  467.331    0.000  467.331    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              437950819  428.922    0.000  428.922    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6993144   13.240    0.000  413.073    0.000 loss.py:445(forward)
                6993144   49.037    0.000  399.833    0.000 functional.py:2637(mse_loss)
               46640760  388.541    0.000  388.541    0.000 memory.py:17(inner)
                7284000   13.567    0.000  387.368    0.000 functional.py:74(split)
               33024315  354.274    0.000  380.043    0.000 module.py:781(__setattr__)
                7284000   30.125    0.000  372.829    0.000 tensor.py:460(split)
               11454879  144.737    0.000  372.707    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               48560000   40.991    0.000  368.482    0.000 wrapper.py:22(get_info)
               69931440  365.737    0.000  365.737    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1246816323  269.803    0.000  344.057    0.000 overrides.py:1086(<genexpr>)
                7284000  341.079    0.000  341.079    0.000 {function Tensor.split at 0x7f8287ddcca0}
               48560000  169.724    0.000  327.490    0.000 libenv.py:363(get_info)
               42637525  318.967    0.000  318.967    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2331048  244.524    0.000  317.662    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   2380   83.699    0.035  303.035    0.127 memory.py:45(update_distribution)
               50895808  297.020    0.000  297.020    0.000 {built-in method numpy.array}
               25240946   23.985    0.000  268.629    0.000 <__array_function__ internals>:2(prod)
               11655240  259.877    0.000  259.877    0.000 {built-in method gather}
                   4760  230.213    0.048  256.359    0.054 {built-in method _pickle.loads}
                4664076   21.664    0.000  250.607    0.000 tensor.py:576(__iter__)
               25240986   18.184    0.000  240.482    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               48560000  238.900    0.000  238.900    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6993144  237.487    0.000  237.487    0.000 {built-in method torch._C._nn.mse_loss}
                7090096   16.486    0.000  231.239    0.000 pooling.py:152(forward)
               25240946   30.370    0.000  222.298    0.000 fromnumeric.py:2881(prod)
                4664076  221.700    0.000  221.700    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                7283997  220.441    0.000  220.441    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2332047  216.740    0.000  219.843    0.000 agent.py:148(convert_values)
                7090096   12.572    0.000  214.753    0.000 _jit_internal.py:257(fn)
               42249720  210.419    0.000  210.419    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2428000   27.256    0.000  205.521    0.000 environments.py:86(<listcomp>)
                7090096   13.282    0.000  201.012    0.000 functional.py:574(_max_pool2d)
               69931686   89.753    0.000  196.304    0.000 tensor.py:596(__hash__)
               25240946   58.329    0.000  191.927    0.000 fromnumeric.py:70(_wrapreduction)
                7090096  186.911    0.000  186.911    0.000 {built-in method max_pool2d}
                2331048  184.184    0.000  184.184    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 8578474: <U_S_0.1_0.1returnchaser_0> in cluster <dcc> Done

Job <U_S_0.1_0.1returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec 20 03:01:51 2020
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Dec 22 07:43:25 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec 22 07:43:25 2020
Terminated at Wed Dec 23 06:39:16 2020
Results reported at Wed Dec 23 06:39:16 2020

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

    CPU time :                                   86016.00 sec.
    Max Memory :                                 57211 MB
    Average Memory :                             56422.89 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4229.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82552 sec.
    Turnaround time :                            272245 sec.

The output (if any) is above this job summary.

