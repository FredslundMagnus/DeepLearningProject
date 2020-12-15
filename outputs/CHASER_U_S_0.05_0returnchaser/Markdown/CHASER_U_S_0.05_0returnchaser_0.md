
    Name :                      CHASER_U_S_0.05_0returnchaser-0
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
    Uncertainty weight :        0.05
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11607366204 function calls (11416168255 primitive calls) in 82529.33 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82529.333 82529.333 {built-in method builtins.exec}
                      1    0.017    0.017 82529.333 82529.333 <string>:1(<module>)
                      1  570.634  570.634 82529.312 82529.312 main.py:92(main)
                1945512  268.422    0.000 58010.424    0.030 agent.py:84(learn)
                1868550  697.276    0.000 57162.268    0.031 agent.py:99(TD_learn)
                1868550  152.781    0.000 34104.333    0.018 memory.py:35(sample_distribution)
                1868550  319.614    0.000 33413.477    0.018 helpers.py:15(stack)
               17047836 21986.010    0.001 21986.010    0.001 {built-in method cat}
        204349140/13157811  930.984    0.000 13260.926    0.001 module.py:715(_call_impl)
                5682612  186.362    0.000 12268.338    0.002 agent.py:231(forward)
               18917493 10715.089    0.001 10715.123    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                1945512  160.772    0.000 9405.249    0.005 agent.py:70(chooseMulti)
               30282609  238.845    0.000 8416.327    0.000 container.py:115(forward)
              252418560 8002.116    0.000 8002.116    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1945512   61.660    0.000 7947.903    0.004 environments.py:83(step)
                1869549   74.348    0.000 6427.804    0.003 agent.py:58(rememberMulti)
                5605650   40.422    0.000 6410.669    0.001 grad_mode.py:23(decorate_context)
                5605650  243.448    0.000 6304.369    0.001 adam.py:55(step)
                1869549  199.342    0.000 6016.872    0.003 agent.py:62(<listcomp>)
                5605650 1214.153    0.000 5207.399    0.001 functional.py:53(adam)
                1945512   53.165    0.000 4951.217    0.003 environments.py:85(<listcomp>)
               39226028 1276.031    0.000 4943.857    0.000 helpers.py:8(clean)
                5605650   48.766    0.000 4897.867    0.001 tensor.py:181(backward)
                5605650   27.529    0.000 4849.101    0.001 __init__.py:68(backward)
                5605650 4680.145    0.001 4680.145    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               44831678 4248.236    0.000 4248.236    0.000 {built-in method as_tensor}
                1869549   79.246    0.000 3714.242    0.002 agent.py:82(<listcomp>)
               37390980  111.278    0.000 3418.442    0.000 exploration.py:34(epsilonGreedy)
               34095672   62.882    0.000 3153.746    0.000 conv.py:422(forward)
               34095672   75.002    0.000 3060.920    0.000 conv.py:414(_conv_forward)
               34095672 2972.128    0.000 2972.128    0.000 {built-in method conv2d}
                1945512   43.063    0.000 2720.402    0.001 environments.py:84(<listcomp>)
               38910240  151.716    0.000 2677.339    0.000 interop.py:274(step)
               45386931   99.601    0.000 2607.107    0.000 linear.py:92(forward)
               45386931  255.352    0.000 2459.652    0.000 functional.py:1669(linear)
                5682618  348.547    0.000 1952.468    0.000 rnn.py:110(flatten_parameters)
                5682612   69.185    0.000 1708.575    0.000 rnn.py:555(forward)
                5682612 1558.829    0.000 1558.829    0.000 {built-in method lstm}
              392395608  912.438    0.000 1521.947    0.000 tensor.py:933(grad)
               39778284 1418.358    0.000 1418.358    0.000 {built-in method addmm}
               38910240   18.900    0.000 1358.381    0.000 wrapper.py:25(act)
               38910240   51.875    0.000 1339.480    0.000 env.py:197(act)
               71930442   71.239    0.000 1332.551    0.000 activation.py:713(forward)
                5605650  128.881    0.000 1306.813    0.000 optimizer.py:167(zero_grad)
               71930442  100.297    0.000 1261.312    0.000 functional.py:1292(leaky_relu)
               38910240 1256.702    0.000 1260.752    0.000 libenv.py:352(act)
                5682615 1180.443    0.000 1180.443    0.000 {built-in method _cudnn_rnn_flatten_weight}
               71930442 1151.283    0.000 1151.283    0.000 {built-in method torch._C._nn.leaky_relu}
              112113000 1070.221    0.000 1070.221    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              112113000  861.974    0.000  861.974    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              493839285  269.704    0.000  779.765    0.000 overrides.py:1073(has_torch_function)
               78136268   61.509    0.000  735.031    0.000 extract_dict_ob.py:9(observe)
               78136268   35.386    0.000  673.522    0.000 wrapper.py:19(observe)
               78136268  157.640    0.000  638.136    0.000 libenv.py:344(observe)
               56056500  606.051    0.000  606.051    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   1945    1.062    0.001  579.734    0.298 agent.py:157(update_target_network)
               56056500  541.017    0.000  541.017    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               37390980  500.728    0.000  500.728    0.000 memory.py:17(inner)
                1869549    5.185    0.000  499.100    0.000 agent.py:249(avoid_similar_state)
              550437540  197.606    0.000  489.851    0.000 {built-in method builtins.any}
              117046508  129.918    0.000  482.416    0.000 libenv.py:281(_maybe_copy_dict)
               56056500  476.404    0.000  476.404    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              351141469  422.688    0.000  422.688    0.000 {method 'copy' of 'numpy.ndarray' objects}
               56056500  418.015    0.000  418.015    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               26469383  376.390    0.000  396.882    0.000 module.py:781(__setattr__)
               45386931  395.024    0.000  395.024    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5836536   12.141    0.000  392.730    0.000 functional.py:74(split)
                5836536   25.470    0.000  379.745    0.000 tensor.py:460(split)
                5605650   11.841    0.000  363.608    0.000 loss.py:445(forward)
              286821781  362.108    0.000  362.108    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                5836536  352.950    0.000  352.950    0.000 {function Tensor.split at 0x7f04f4aefd30}
               10893759  134.574    0.000  352.264    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                5605650   41.948    0.000  351.767    0.000 functional.py:2637(mse_loss)
               38910240   33.801    0.000  316.431    0.000 wrapper.py:22(get_info)
                   1945   90.261    0.046  300.870    0.155 memory.py:45(update_distribution)
               56056500  290.849    0.000  290.849    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1033065501  232.434    0.000  287.592    0.000 overrides.py:1086(<genexpr>)
               11211300  285.011    0.000  285.011    0.000 {built-in method gather}
               38910240  144.165    0.000  282.630    0.000 libenv.py:363(get_info)
               40782680  275.843    0.000  275.843    0.000 {built-in method numpy.array}
                1868550  203.165    0.000  261.952    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               43284498  253.179    0.000  253.179    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                   3890  228.412    0.059  251.733    0.065 {built-in method _pickle.loads}
               23656208   22.506    0.000  250.840    0.000 <__array_function__ internals>:2(prod)
                1869549  197.402    0.000  228.642    0.000 agent.py:149(convert_values)
               23656248   17.675    0.000  224.448    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               38910240  223.614    0.000  223.614    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1945512   21.861    0.000  214.625    0.000 environments.py:86(<listcomp>)
                5605650  213.380    0.000  213.380    0.000 {built-in method torch._C._nn.mse_loss}
                5682612   14.849    0.000  209.424    0.000 pooling.py:152(forward)
               23656208   27.774    0.000  206.773    0.000 fromnumeric.py:2881(prod)
                5682612   10.196    0.000  194.575    0.000 _jit_internal.py:257(fn)
                2017367  194.078    0.000  194.078    0.000 {built-in method tensor}
               38910260   29.791    0.000  192.813    0.000 environments.py:89(reset)
                5608647  188.811    0.000  188.811    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                1868550  187.036    0.000  187.036    0.000 memory.py:43(<listcomp>)
                5682612   11.749    0.000  183.422    0.000 functional.py:574(_max_pool2d)
               22730460  163.404    0.000  180.724    0.000 __init__.py:67(is_acceptable)
               23656208   53.171    0.000  178.999    0.000 fromnumeric.py:70(_wrapreduction)
                5682612  170.956    0.000  170.956    0.000 {built-in method max_pool2d}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8557119: <CHASER_U_S_0.05_0returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0.05_0returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:12 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Dec 14 16:25:48 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec 14 16:25:48 2020
Terminated at Tue Dec 15 15:21:32 2020
Results reported at Tue Dec 15 15:21:32 2020

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

    CPU time :                                   93408.00 sec.
    Max Memory :                                 54931 MB
    Average Memory :                             54311.79 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6509.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82544 sec.
    Turnaround time :                            346400 sec.

The output (if any) is above this job summary.

