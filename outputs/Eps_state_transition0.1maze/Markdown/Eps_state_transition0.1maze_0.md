
    Name :                      Eps_state_transition0.1maze-0
    Discount :                  0.995
    Environment :               maze
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13545154080 function calls (13299970104 primitive calls) in 82515.91 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82515.911 82515.911 {built-in method builtins.exec}
                      1    0.121    0.121 82515.911 82515.911 <string>:1(<module>)
                      1  443.350  443.350 82515.787 82515.787 main.py:92(main)
                2427816  181.218    0.000 54320.525    0.022 agent.py:86(learn)
                2427316  689.126    0.000 53199.242    0.022 agent.py:96(TD_learn)
                2427316  150.498    0.000 24681.286    0.010 memory.py:35(sample_distribution)
                2427316  236.762    0.000 23930.741    0.010 helpers.py:15(stack)
        259742312/14564896 1094.773    0.000 17000.633    0.001 module.py:715(_call_impl)
                7282448  229.831    0.000 15832.157    0.002 agent.py:212(forward)
               24275268 12611.247    0.001 12611.315    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               38840056  325.178    0.000 11342.363    0.000 container.py:115(forward)
               21847344 10760.175    0.000 10760.175    0.000 {built-in method cat}
                2427816   65.268    0.000 10164.812    0.004 environments.py:83(step)
                2427816  229.200    0.000 9290.894    0.004 agent.py:74(chooseMulti)
                4854632   32.865    0.000 8526.600    0.002 grad_mode.py:23(decorate_context)
                4854632  230.443    0.000 8439.169    0.002 adam.py:55(step)
                2427816  111.470    0.000 8089.735    0.003 agent.py:62(rememberMulti)
                2427816  334.675    0.000 7558.104    0.003 agent.py:66(<listcomp>)
              328515348 7306.674    0.000 7306.674    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                4854632 1584.236    0.000 7257.912    0.001 functional.py:53(adam)
                2427816   76.424    0.000 6619.107    0.003 environments.py:85(<listcomp>)
               48688862 1539.404    0.000 6563.160    0.000 helpers.py:8(clean)
                4854632   34.415    0.000 5767.608    0.001 tensor.py:181(backward)
                4854632   21.237    0.000 5733.192    0.001 __init__.py:68(backward)
                4854632 5582.466    0.001 5582.466    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               55970810 5572.967    0.000 5572.967    0.000 {built-in method as_tensor}
               43694688   84.798    0.000 4115.366    0.000 conv.py:422(forward)
               43694688   81.337    0.000 3996.782    0.000 conv.py:414(_conv_forward)
               43694688 3900.197    0.000 3900.197    0.000 {built-in method conv2d}
               58260584  126.559    0.000 3613.117    0.000 linear.py:92(forward)
               58260584  347.285    0.000 3429.328    0.000 functional.py:1669(linear)
                2427816   54.007    0.000 3269.230    0.001 environments.py:84(<listcomp>)
               48556320  206.369    0.000 3215.223    0.000 interop.py:274(step)
                7282454  410.648    0.000 2585.568    0.000 rnn.py:110(flatten_parameters)
               50977136 2014.868    0.000 2014.868    0.000 {built-in method addmm}
                2427816  118.017    0.000 2005.321    0.001 agent.py:84(<listcomp>)
               92245008   77.002    0.000 1914.702    0.000 activation.py:713(forward)
               92245008  116.868    0.000 1837.700    0.000 functional.py:1292(leaky_relu)
              407789196 1126.419    0.000 1797.437    0.000 tensor.py:933(grad)
                7282448   76.655    0.000 1741.774    0.000 rnn.py:555(forward)
                4854632  167.437    0.000 1739.063    0.000 optimizer.py:167(zero_grad)
                7282451 1732.166    0.000 1732.166    0.000 {built-in method _cudnn_rnn_flatten_weight}
               92245008 1709.576    0.000 1709.576    0.000 {built-in method torch._C._nn.leaky_relu}
               48556320   23.535    0.000 1600.501    0.000 wrapper.py:25(act)
               48556320   79.511    0.000 1576.967    0.000 env.py:197(act)
                7282448 1573.791    0.000 1573.791    0.000 {built-in method lstm}
               48556320  171.934    0.000 1548.073    0.000 exploration.py:34(epsilonGreedy)
              116511168 1529.890    0.000 1529.890    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               48556320 1446.092    0.000 1451.005    0.000 libenv.py:352(act)
              116511168 1291.053    0.000 1291.053    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   4855    1.696    0.000  940.065    0.194 agent.py:139(update_target_network)
              524305580  315.230    0.000  879.585    0.000 overrides.py:1073(has_torch_function)
               97245182   84.008    0.000  842.415    0.000 extract_dict_ob.py:9(observe)
               58255584  804.826    0.000  804.826    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               97245182   41.564    0.000  758.407    0.000 wrapper.py:19(observe)
               58255584  737.184    0.000  737.184    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               97245182  186.644    0.000  716.842    0.000 libenv.py:344(observe)
                2427816    7.186    0.000  715.432    0.000 agent.py:230(avoid_similar_state)
               58255584  682.261    0.000  682.261    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               58255584  607.978    0.000  607.978    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   4855  165.214    0.034  594.722    0.122 memory.py:45(update_distribution)
              362234229  560.924    0.000  560.924    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               58260584  545.238    0.000  545.238    0.000 {method 't' of 'torch._C._TensorBase' objects}
              592275452  223.061    0.000  542.230    0.000 {built-in method builtins.any}
               50993346  521.614    0.000  521.614    0.000 {built-in method numpy.array}
              145801502  159.090    0.000  516.779    0.000 libenv.py:281(_maybe_copy_dict)
               58255584  480.127    0.000  480.127    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              437409361  452.391    0.000  452.391    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7283448   12.847    0.000  402.744    0.000 functional.py:74(split)
               48556320   44.751    0.000  397.320    0.000 wrapper.py:22(get_info)
               11451729  155.130    0.000  396.222    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7283448   33.839    0.000  388.903    0.000 tensor.py:460(split)
                7283448  353.204    0.000  353.204    0.000 {function Tensor.split at 0x7fcf351d1ca0}
               48556320  186.909    0.000  352.569    0.000 libenv.py:363(get_info)
               48556320  345.188    0.000  345.188    0.000 memory.py:17(inner)
               48556320  339.231    0.000  339.231    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2427316  257.306    0.000  335.347    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                4854632    9.529    0.000  335.275    0.000 loss.py:445(forward)
                4854632   31.830    0.000  325.746    0.000 functional.py:2637(mse_loss)
               33986259  293.078    0.000  316.574    0.000 module.py:781(__setattr__)
             1106871744  248.744    0.000  315.608    0.000 overrides.py:1086(<genexpr>)
                2427816  308.748    0.000  312.706    0.000 agent.py:131(convert_values)
               43693688  297.017    0.000  297.017    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   9710  230.069    0.024  287.122    0.030 {built-in method _pickle.loads}
               25330914   24.600    0.000  283.593    0.000 <__array_function__ internals>:2(prod)
                7283448  259.361    0.000  259.361    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                7282448   14.039    0.000  259.315    0.000 pooling.py:152(forward)
               25330954   19.816    0.000  254.525    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7282448   12.106    0.000  245.276    0.000 _jit_internal.py:257(fn)
               25330914   30.224    0.000  234.709    0.000 fromnumeric.py:2881(prod)
                7282448   11.921    0.000  231.900    0.000 functional.py:574(_max_pool2d)
                7282448  219.127    0.000  219.127    0.000 {built-in method max_pool2d}
                2796794  215.131    0.000  215.131    0.000 {built-in method tensor}
                2427816   31.348    0.000  211.207    0.000 environments.py:86(<listcomp>)
                4854632  209.600    0.000  209.600    0.000 {built-in method torch._C._nn.mse_loss}
               25330914   56.966    0.000  204.485    0.000 fromnumeric.py:70(_wrapreduction)
                7281948  202.195    0.000  202.195    0.000 {built-in method gather}
              259742312  186.507    0.000  186.507    0.000 {built-in method torch._C._get_tracing_state}
                2427816   17.234    0.000  184.741    0.000 collector.py:7(collect)
               48556340   37.445    0.000  179.868    0.000 environments.py:89(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 8482841: <Eps_state_transition0.1maze_0> in cluster <dcc> Done

Job <Eps_state_transition0.1maze_0> was submitted from host <n-62-27-19> by user <s183914> in cluster <dcc> at Sat Dec  5 00:10:43 2020
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec  5 02:11:51 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec  5 02:11:51 2020
Terminated at Sun Dec  6 01:07:12 2020
Results reported at Sun Dec  6 01:07:12 2020

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

    CPU time :                                   83780.00 sec.
    Max Memory :                                 55026 MB
    Average Memory :                             54320.54 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6414.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82520 sec.
    Turnaround time :                            89789 sec.

The output (if any) is above this job summary.

