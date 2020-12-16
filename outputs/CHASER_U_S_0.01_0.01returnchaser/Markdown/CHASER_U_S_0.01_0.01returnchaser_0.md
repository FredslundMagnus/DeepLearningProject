
    Name :                      CHASER_U_S_0.01_0.01returnchaser-0
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
    Uncertainty weight :        0.01
    State difference :          1
    State difference weight :   0.01
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11674356617 function calls (11482031675 primitive calls) in 82529.62 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82529.622 82529.622 {built-in method builtins.exec}
                      1    0.016    0.016 82529.622 82529.622 <string>:1(<module>)
                      1  571.707  571.707 82529.602 82529.602 main.py:92(main)
                1958036  271.461    0.000 58082.659    0.030 agent.py:84(learn)
                1879075  689.687    0.000 57227.786    0.030 agent.py:99(TD_learn)
                1879075  156.895    0.000 34054.550    0.018 memory.py:35(sample_distribution)
                1879075  318.064    0.000 33356.939    0.018 helpers.py:15(stack)
               17148558 21886.081    0.001 21886.081    0.001 {built-in method cat}
        205551807/13233485  923.978    0.000 13389.959    0.001 module.py:715(_call_impl)
                5716186  195.765    0.000 12391.882    0.002 agent.py:231(forward)
               19028740 10765.441    0.001 10765.496    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                1958036  161.002    0.000 9353.910    0.005 agent.py:70(chooseMulti)
               30461004  241.203    0.000 8511.276    0.000 container.py:115(forward)
                1958036   63.578    0.000 7972.152    0.004 environments.py:83(step)
              253918475 7893.912    0.000 7893.912    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                5637225   41.377    0.000 6393.229    0.001 grad_mode.py:23(decorate_context)
                1880074   73.342    0.000 6381.471    0.003 agent.py:58(rememberMulti)
                5637225  248.265    0.000 6285.271    0.001 adam.py:55(step)
                1880074  183.711    0.000 5968.744    0.003 agent.py:62(<listcomp>)
                5637225 1193.330    0.000 5176.601    0.001 functional.py:53(adam)
                1958036   55.647    0.000 4975.505    0.003 environments.py:85(<listcomp>)
               39460758 1279.746    0.000 4963.240    0.000 helpers.py:8(clean)
                5637225   50.845    0.000 4921.068    0.001 tensor.py:181(backward)
                5637225   29.342    0.000 4870.223    0.001 __init__.py:68(backward)
                5637225 4698.362    0.001 4698.362    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               45097983 4262.026    0.000 4262.026    0.000 {built-in method as_tensor}
                1880074   80.004    0.000 3623.411    0.002 agent.py:82(<listcomp>)
               37601480  108.701    0.000 3329.060    0.000 exploration.py:34(epsilonGreedy)
               34297116   65.326    0.000 3193.143    0.000 conv.py:422(forward)
               34297116   78.250    0.000 3097.076    0.000 conv.py:414(_conv_forward)
               34297116 3005.037    0.000 3005.037    0.000 {built-in method conv2d}
                1958036   42.462    0.000 2721.338    0.001 environments.py:84(<listcomp>)
               39160720  154.426    0.000 2678.876    0.000 interop.py:274(step)
               45653524  101.127    0.000 2650.891    0.000 linear.py:92(forward)
               45653524  257.911    0.000 2499.154    0.000 functional.py:1669(linear)
                5716192  352.595    0.000 1973.648    0.000 rnn.py:110(flatten_parameters)
                5716186   69.388    0.000 1713.777    0.000 rnn.py:555(forward)
                5716186 1565.387    0.000 1565.387    0.000 {built-in method lstm}
              394605858  915.939    0.000 1531.638    0.000 tensor.py:933(grad)
               40013302 1435.059    0.000 1435.059    0.000 {built-in method addmm}
               39160720   19.525    0.000 1353.289    0.000 wrapper.py:25(act)
               72354380   72.415    0.000 1342.790    0.000 activation.py:713(forward)
               39160720   50.238    0.000 1333.764    0.000 env.py:197(act)
                5637225  133.540    0.000 1323.516    0.000 optimizer.py:167(zero_grad)
               72354380  101.857    0.000 1270.375    0.000 functional.py:1292(leaky_relu)
               39160720 1252.142    0.000 1255.897    0.000 libenv.py:352(act)
                5716189 1189.854    0.000 1189.854    0.000 {built-in method _cudnn_rnn_flatten_weight}
               72354380 1159.050    0.000 1159.050    0.000 {built-in method torch._C._nn.leaky_relu}
              112744500 1060.216    0.000 1060.216    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              112744500  860.154    0.000  860.154    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              496631878  273.527    0.000  792.675    0.000 overrides.py:1073(has_torch_function)
               78621478   61.461    0.000  733.559    0.000 extract_dict_ob.py:9(observe)
               78621478   36.194    0.000  672.099    0.000 wrapper.py:19(observe)
               78621478  156.289    0.000  635.905    0.000 libenv.py:344(observe)
               56372250  614.887    0.000  614.887    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   1958    1.063    0.001  583.411    0.298 agent.py:157(update_target_network)
               56372250  541.945    0.000  541.945    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1880074    5.445    0.000  504.719    0.000 agent.py:249(avoid_similar_state)
              553559876  205.744    0.000  498.528    0.000 {built-in method builtins.any}
               37601480  495.633    0.000  495.633    0.000 memory.py:17(inner)
              117782198  128.466    0.000  482.058    0.000 libenv.py:281(_maybe_copy_dict)
               56372250  475.600    0.000  475.600    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              353348552  424.686    0.000  424.686    0.000 {method 'copy' of 'numpy.ndarray' objects}
               56372250  410.900    0.000  410.900    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               45653524  405.761    0.000  405.761    0.000 {method 't' of 'torch._C._TensorBase' objects}
               26624729  379.904    0.000  402.447    0.000 module.py:781(__setattr__)
                5874108   12.004    0.000  395.182    0.000 functional.py:74(split)
                5874108   26.313    0.000  382.303    0.000 tensor.py:460(split)
              288618078  363.412    0.000  363.412    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                5637225   11.842    0.000  362.779    0.000 loss.py:445(forward)
                5874108  354.660    0.000  354.660    0.000 {function Tensor.split at 0x7ff172925d30}
                5637225   42.555    0.000  350.937    0.000 functional.py:2637(mse_loss)
               10907642  132.657    0.000  347.478    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               39160720   36.271    0.000  318.522    0.000 wrapper.py:22(get_info)
                   1958   90.781    0.046  303.277    0.155 memory.py:45(update_distribution)
               56372250  296.988    0.000  296.988    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1038917280  233.336    0.000  288.334    0.000 overrides.py:1086(<genexpr>)
               11274450  286.262    0.000  286.262    0.000 {built-in method gather}
               39160720  144.601    0.000  282.250    0.000 libenv.py:363(get_info)
               41043711  277.730    0.000  277.730    0.000 {built-in method numpy.array}
                1879075  205.279    0.000  265.066    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   3916  229.102    0.059  252.777    0.065 {built-in method _pickle.loads}
               43534569  251.555    0.000  251.555    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               23694499   22.569    0.000  247.789    0.000 <__array_function__ internals>:2(prod)
                1880074  196.343    0.000  226.781    0.000 agent.py:149(convert_values)
               39160720  221.470    0.000  221.470    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               23694539   16.756    0.000  221.316    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                5716186   18.369    0.000  217.198    0.000 pooling.py:152(forward)
                5637225  212.202    0.000  212.202    0.000 {built-in method torch._C._nn.mse_loss}
                1958036   22.166    0.000  211.731    0.000 environments.py:86(<listcomp>)
               23694499   27.204    0.000  204.560    0.000 fromnumeric.py:2881(prod)
                5716186   10.511    0.000  198.828    0.000 _jit_internal.py:257(fn)
                2028880  196.851    0.000  196.851    0.000 {built-in method tensor}
                5640222  190.892    0.000  190.892    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               39160740   28.727    0.000  189.616    0.000 environments.py:89(reset)
                5716186   10.986    0.000  187.374    0.000 functional.py:574(_max_pool2d)
               22864756  167.995    0.000  185.639    0.000 __init__.py:67(is_acceptable)
                1879075  184.835    0.000  184.835    0.000 memory.py:43(<listcomp>)
               23694499   52.869    0.000  177.356    0.000 fromnumeric.py:70(_wrapreduction)
                5716186  175.675    0.000  175.675    0.000 {built-in method max_pool2d}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8557121: <CHASER_U_S_0.01_0.01returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0.01_0.01returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:12 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Dec 15 15:22:44 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec 15 15:22:44 2020
Terminated at Wed Dec 16 14:18:27 2020
Results reported at Wed Dec 16 14:18:27 2020

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

    CPU time :                                   93470.00 sec.
    Max Memory :                                 54899 MB
    Average Memory :                             54232.11 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6541.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82544 sec.
    Turnaround time :                            429015 sec.

The output (if any) is above this job summary.

