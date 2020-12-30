
    Name :                      NOPE_final_maze-0
    Discount :                  0.995
    Environment :               maze
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


      10547094001 function calls (10386232073 primitive calls) in 64523.81 seconds

##    Ordered by: cumulative time
   List reduced from 1354 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 64523.809 64523.809 {built-in method builtins.exec}
                      1    0.127    0.127 64523.809 64523.809 <string>:1(<module>)
                      1  391.391  391.391 64523.679 64523.679 main.py:91(main)
                2118887  146.101    0.000 41534.261    0.020 agent.py:93(learn)
                2033929  365.719    0.000 40900.000    0.020 agent.py:106(TD_learn)
                2033929  136.224    0.000 22293.252    0.011 memory.py:35(sample_distribution)
                2033929  215.301    0.000 21640.078    0.011 helpers.py:15(stack)
               18560343 11092.677    0.001 11092.687    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        171109973/10254603  762.375    0.000 10716.031    0.001 module.py:715(_call_impl)
                6186745  155.363    0.000 10341.783    0.002 agent.py:235(forward)
               18560235 9977.679    0.001 9977.679    0.001 {built-in method cat}
                2118887   42.144    0.000 9571.672    0.005 agent.py:72(chooseMulti)
              275551182 9214.160    0.000 9214.160    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2118887   56.717    0.000 7580.395    0.004 environments.py:83(step)
               24746980  188.903    0.000 6413.705    0.000 container.py:115(forward)
                2034928   75.485    0.000 5357.253    0.003 agent.py:88(<listcomp>)
                2034919    8.590    0.000 5274.816    0.003 agent.py:58(rememberMulti)
                2034919  186.149    0.000 5266.225    0.003 agent.py:63(<listcomp>)
                4067858   27.273    0.000 5126.994    0.001 grad_mode.py:23(decorate_context)
               40698560  111.702    0.000 5091.350    0.000 exploration.py:34(epsilonGreedy)
                4067858  192.815    0.000 5054.855    0.001 adam.py:55(step)
                2118887   55.496    0.000 4766.879    0.002 environments.py:85(<listcomp>)
               42487372 1215.721    0.000 4725.903    0.000 helpers.py:8(clean)
                4067858  929.062    0.000 4153.497    0.001 functional.py:53(adam)
               48589159 3992.098    0.000 3992.098    0.000 {built-in method as_tensor}
                4067858   31.131    0.000 3968.996    0.001 tensor.py:181(backward)
                4067858   19.933    0.000 3937.865    0.001 __init__.py:68(backward)
                4067858 3815.150    0.001 3815.150    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               37120470   64.839    0.000 3002.610    0.000 conv.py:422(forward)
               37120470   73.073    0.000 2906.722    0.000 conv.py:414(_conv_forward)
               37120470 2820.033    0.000 2820.033    0.000 {built-in method conv2d}
                2118887   44.152    0.000 2613.421    0.001 environments.py:84(<listcomp>)
               42377740  156.249    0.000 2569.269    0.000 interop.py:274(step)
                6186751  345.170    0.000 1861.245    0.000 rnn.py:110(flatten_parameters)
                6186745   72.414    0.000 1510.091    0.000 rnn.py:555(forward)
                6186745 1350.744    0.000 1350.744    0.000 {built-in method lstm}
               42377740   20.006    0.000 1284.779    0.000 wrapper.py:25(act)
               24746980   52.785    0.000 1276.896    0.000 linear.py:92(forward)
              341700180  757.595    0.000 1272.010    0.000 tensor.py:933(grad)
               42377740   53.098    0.000 1264.773    0.000 env.py:197(act)
               24746980   97.427    0.000 1197.357    0.000 functional.py:1669(linear)
               42377740 1179.382    0.000 1183.478    0.000 libenv.py:352(act)
                4067858  109.012    0.000 1112.772    0.000 optimizer.py:167(zero_grad)
                6186748 1107.770    0.000 1107.770    0.000 {built-in method _cudnn_rnn_flatten_weight}
               61867450   59.651    0.000 1041.909    0.000 activation.py:713(forward)
               61867450   85.611    0.000  982.258    0.000 functional.py:1292(leaky_relu)
               61867450  888.180    0.000  888.180    0.000 {built-in method torch._C._nn.leaky_relu}
               97628592  844.304    0.000  844.304    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24746980  803.966    0.000  803.966    0.000 {built-in method addmm}
               97628592  707.813    0.000  707.813    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               84865112   61.311    0.000  680.922    0.000 extract_dict_ob.py:9(observe)
              415261672  217.117    0.000  620.712    0.000 overrides.py:1073(has_torch_function)
               84865112   35.360    0.000  619.611    0.000 wrapper.py:19(observe)
               84865112  159.893    0.000  584.251    0.000 libenv.py:344(observe)
                   2076    0.804    0.000  488.161    0.235 agent.py:161(update_target_network)
               48814296  473.095    0.000  473.095    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               48814296  430.089    0.000  430.089    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              127242852  133.618    0.000  421.817    0.000 libenv.py:281(_maybe_copy_dict)
               48814296  400.147    0.000  400.147    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              448144392  156.570    0.000  385.378    0.000 {built-in method builtins.any}
              381730632  356.446    0.000  356.446    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48814296  354.436    0.000  354.436    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11057618  134.175    0.000  349.567    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               28816673  300.501    0.000  322.047    0.000 module.py:781(__setattr__)
               42377740   34.368    0.000  320.636    0.000 wrapper.py:22(get_info)
                6356661   11.675    0.000  317.212    0.000 functional.py:74(split)
                6356661   27.526    0.000  304.627    0.000 tensor.py:460(split)
              305301671  297.174    0.000  297.174    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               42377740  149.110    0.000  286.268    0.000 libenv.py:363(get_info)
                2033929  215.721    0.000  280.047    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                6356661  275.776    0.000  275.776    0.000 {function Tensor.split at 0x7f823a0cfd30}
               40698380  274.046    0.000  274.046    0.000 memory.py:17(inner)
                   2076   73.708    0.036  261.606    0.126 memory.py:45(update_distribution)
                4067858    9.393    0.000  258.740    0.000 loss.py:445(forward)
               44415821  256.187    0.000  256.187    0.000 {built-in method numpy.array}
               48814296  254.081    0.000  254.081    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24149305   22.380    0.000  250.996    0.000 <__array_function__ internals>:2(prod)
                4067858   31.229    0.000  249.347    0.000 functional.py:2637(mse_loss)
              855270324  182.010    0.000  225.508    0.000 overrides.py:1086(<genexpr>)
               24149345   17.009    0.000  224.695    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               24149305   28.540    0.000  207.685    0.000 fromnumeric.py:2881(prod)
                   4152  181.878    0.044  204.432    0.049 {built-in method _pickle.loads}
                6186745   13.769    0.000  201.529    0.000 pooling.py:152(forward)
               42377740  197.369    0.000  197.369    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2034928  144.902    0.000  191.820    0.000 agent.py:152(convert_values)
                6186745   10.865    0.000  187.760    0.000 _jit_internal.py:257(fn)
               24746980  183.456    0.000  183.456    0.000 {method 't' of 'torch._C._TensorBase' objects}
               24149305   54.097    0.000  179.145    0.000 fromnumeric.py:70(_wrapreduction)
                8135716  177.274    0.000  177.274    0.000 {built-in method gather}
                6186745   11.518    0.000  175.880    0.000 functional.py:574(_max_pool2d)
                6186745  163.549    0.000  163.549    0.000 {built-in method max_pool2d}
                2033929  158.329    0.000  158.329    0.000 memory.py:43(<listcomp>)
               24746992  139.104    0.000  156.691    0.000 __init__.py:67(is_acceptable)
                4067858  149.164    0.000  149.164    0.000 {built-in method torch._C._nn.mse_loss}
               28729880  145.797    0.000  145.797    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2118887   21.415    0.000  143.378    0.000 environments.py:86(<listcomp>)
                2118887   15.740    0.000  142.403    0.000 collector.py:8(collect)
               48814512   59.721    0.000  132.528    0.000 tensor.py:596(__hash__)
               26185310  126.603    0.000  126.603    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              169730224   47.947    0.000  126.566    0.000 libenv.py:271(_maybe_copy_ndarray)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8587606: <NOPE_final_maze_0> in cluster <dcc> Done

Job <NOPE_final_maze_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 25 20:02:00 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Dec 25 20:02:01 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 25 20:02:01 2020
Terminated at Sat Dec 26 13:57:33 2020
Results reported at Sat Dec 26 13:57:33 2020

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

    CPU time :                                   67354.00 sec.
    Max Memory :                                 56152 MB
    Average Memory :                             55411.55 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5288.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64595 sec.
    Turnaround time :                            64533 sec.

The output (if any) is above this job summary.

