
    Name :                      NOPE_final_plunder-0
    Discount :                  0.995
    Environment :               plunder
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


      10010756273 function calls (9858171913 primitive calls) in 64515.72 seconds

##    Ordered by: cumulative time
   List reduced from 1354 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 64515.715 64515.715 {built-in method builtins.exec}
                      1    0.026    0.026 64515.715 64515.715 <string>:1(<module>)
                      1  322.499  322.499 64515.688 64515.688 main.py:91(main)
                2010099  128.991    0.000 42607.363    0.021 agent.py:93(learn)
                1929139  406.436    0.000 42030.265    0.022 agent.py:106(TD_learn)
                1929139  126.205    0.000 20256.863    0.011 memory.py:35(sample_distribution)
                1929139  212.335    0.000 19637.745    0.010 helpers.py:15(stack)
        162304457/9726655  719.318    0.000 11597.716    0.001 module.py:715(_call_impl)
                5868377  156.374    0.000 11221.425    0.002 agent.py:235(forward)
               17605239 10064.168    0.001 10064.237    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               17605131 9044.097    0.001 9044.097    0.001 {built-in method cat}
                2010099   54.393    0.000 8118.247    0.004 environments.py:83(step)
               23473508  207.232    0.000 7178.728    0.000 container.py:115(forward)
                2010099   44.199    0.000 7161.533    0.004 agent.py:72(chooseMulti)
                3858278   26.925    0.000 6851.614    0.002 grad_mode.py:23(decorate_context)
                3858278  188.532    0.000 6780.407    0.002 adam.py:55(step)
              260900339 6771.817    0.000 6771.817    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1930129    8.126    0.000 6132.830    0.003 agent.py:58(rememberMulti)
                1930129  267.286    0.000 6124.704    0.003 agent.py:63(<listcomp>)
                3858278 1255.019    0.000 5838.756    0.002 functional.py:53(adam)
                2010099   65.027    0.000 5452.116    0.003 environments.py:85(<listcomp>)
               40276204 1286.041    0.000 5398.776    0.000 helpers.py:8(clean)
                3858278   33.936    0.000 4687.453    0.001 tensor.py:181(backward)
                3858278   19.683    0.000 4653.516    0.001 __init__.py:68(backward)
               46063621 4552.432    0.000 4552.432    0.000 {built-in method as_tensor}
                3858278 4525.272    0.001 4525.272    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               35210262   66.309    0.000 3320.860    0.000 conv.py:422(forward)
               35210262   67.843    0.000 3226.572    0.000 conv.py:414(_conv_forward)
               35210262 3145.162    0.000 3145.162    0.000 {built-in method conv2d}
                2010099   44.699    0.000 2459.994    0.001 environments.py:84(<listcomp>)
                1930138   93.123    0.000 2427.223    0.001 agent.py:88(<listcomp>)
               40201980  167.062    0.000 2415.295    0.000 interop.py:274(step)
               38602760  127.680    0.000 2062.937    0.000 exploration.py:34(epsilonGreedy)
                5868383  330.982    0.000 2056.039    0.000 rnn.py:110(flatten_parameters)
               23473508   54.575    0.000 1479.658    0.000 linear.py:92(forward)
              324095460  908.269    0.000 1429.535    0.000 tensor.py:933(grad)
                5868377   63.616    0.000 1407.085    0.000 rnn.py:555(forward)
               23473508   94.518    0.000 1398.510    0.000 functional.py:1669(linear)
                3858278  139.779    0.000 1391.727    0.000 optimizer.py:167(zero_grad)
                5868380 1365.923    0.000 1365.923    0.000 {built-in method _cudnn_rnn_flatten_weight}
                5868377 1269.562    0.000 1269.562    0.000 {built-in method lstm}
               58683770   53.922    0.000 1258.982    0.000 activation.py:713(forward)
               92598672 1235.631    0.000 1235.631    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               58683770   84.612    0.000 1205.060    0.000 functional.py:1292(leaky_relu)
               58683770 1112.340    0.000 1112.340    0.000 {built-in method torch._C._nn.leaky_relu}
               40201980   20.026    0.000 1073.344    0.000 wrapper.py:25(act)
               40201980   66.124    0.000 1053.317    0.000 env.py:197(act)
               92598672 1038.613    0.000 1038.613    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               23473508  962.714    0.000  962.714    0.000 {built-in method addmm}
               40201980  945.870    0.000  949.773    0.000 libenv.py:352(act)
               80478184   72.245    0.000  704.340    0.000 extract_dict_ob.py:9(observe)
               46299336  668.567    0.000  668.567    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               80478184   34.656    0.000  632.096    0.000 wrapper.py:19(observe)
              393868520  227.537    0.000  622.227    0.000 overrides.py:1073(has_torch_function)
               80478184  159.644    0.000  597.439    0.000 libenv.py:344(observe)
               46299336  588.878    0.000  588.878    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               46299336  547.131    0.000  547.131    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46299336  487.147    0.000  487.147    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   1970    0.751    0.000  448.106    0.227 agent.py:161(update_target_network)
              120680164  131.473    0.000  425.569    0.000 libenv.py:281(_maybe_copy_dict)
              289191458  424.658    0.000  424.658    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               46299336  379.266    0.000  379.266    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              362042462  375.522    0.000  375.522    0.000 {method 'copy' of 'numpy.ndarray' objects}
              425058608  148.792    0.000  373.786    0.000 {built-in method builtins.any}
               10955801  144.624    0.000  371.358    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               40201980   36.587    0.000  331.130    0.000 wrapper.py:22(get_info)
                6030297   11.509    0.000  309.866    0.000 functional.py:74(split)
                6030297   27.777    0.000  297.455    0.000 tensor.py:460(split)
               40201980  155.982    0.000  294.543    0.000 libenv.py:363(get_info)
               40201980  281.321    0.000  281.321    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                3858278    8.695    0.000  274.374    0.000 loss.py:445(forward)
                1929139  210.241    0.000  271.424    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                6030297  268.298    0.000  268.298    0.000 {function Tensor.split at 0x7fae6b0cad30}
               38602580  267.754    0.000  267.754    0.000 memory.py:17(inner)
                3858278   27.180    0.000  265.679    0.000 functional.py:2637(mse_loss)
               23840881   22.340    0.000  261.385    0.000 <__array_function__ internals>:2(prod)
               27333621  238.645    0.000  257.453    0.000 module.py:781(__setattr__)
               42135059  244.407    0.000  244.407    0.000 {built-in method numpy.array}
                   1970   67.048    0.034  235.126    0.119 memory.py:45(update_distribution)
               23840921   17.887    0.000  234.976    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               23473508  229.739    0.000  229.739    0.000 {method 't' of 'torch._C._TensorBase' objects}
              811210548  178.671    0.000  222.089    0.000 overrides.py:1086(<genexpr>)
               23840881   30.080    0.000  217.089    0.000 fromnumeric.py:2881(prod)
                5868377   10.804    0.000  212.145    0.000 pooling.py:152(forward)
                7716556  207.035    0.000  207.035    0.000 {built-in method gather}
                5868377    9.914    0.000  201.341    0.000 _jit_internal.py:257(fn)
                1930138  181.789    0.000  195.694    0.000 agent.py:152(convert_values)
                5868377   10.701    0.000  190.440    0.000 functional.py:574(_max_pool2d)
                   3940  166.268    0.042  190.198    0.048 {built-in method _pickle.loads}
               23840881   53.118    0.000  187.010    0.000 fromnumeric.py:70(_wrapreduction)
               27250826  185.222    0.000  185.222    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                5868377  178.903    0.000  178.903    0.000 {built-in method max_pool2d}
                3858278  171.215    0.000  171.215    0.000 {built-in method torch._C._nn.mse_loss}
                2010099   15.053    0.000  153.743    0.000 collector.py:8(collect)
                2010099   23.120    0.000  151.743    0.000 environments.py:86(<listcomp>)
                1929139  146.607    0.000  146.607    0.000 memory.py:43(<listcomp>)
               23473520  124.946    0.000  140.771    0.000 __init__.py:67(is_acceptable)
                4020199  137.817    0.000  137.818    0.000 {built-in method builtins.sum}
              160956368   44.335    0.000  136.299    0.000 libenv.py:271(_maybe_copy_ndarray)
               25771990  134.395    0.000  134.395    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 8587609: <NOPE_final_plunder_0> in cluster <dcc> Done

Job <NOPE_final_plunder_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 25 20:02:01 2020
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec 26 04:27:34 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec 26 04:27:34 2020
Terminated at Sat Dec 26 22:22:54 2020
Results reported at Sat Dec 26 22:22:54 2020

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

    CPU time :                                   66347.00 sec.
    Max Memory :                                 55950 MB
    Average Memory :                             55211.37 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5490.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64574 sec.
    Turnaround time :                            94853 sec.

The output (if any) is above this job summary.

