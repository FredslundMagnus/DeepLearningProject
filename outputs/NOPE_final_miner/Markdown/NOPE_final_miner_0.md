
    Name :                      NOPE_final_miner-0
    Discount :                  0.995
    Environment :               miner
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


      9889221541 function calls (9738513419 primitive calls) in 64525.24 seconds

##    Ordered by: cumulative time
   List reduced from 1354 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 64525.241 64525.241 {built-in method builtins.exec}
                      1    0.026    0.026 64525.241 64525.241 <string>:1(<module>)
                      1  366.394  366.394 64525.214 64525.214 main.py:91(main)
                1984712  136.025    0.000 43106.164    0.022 agent.py:93(learn)
                1905751  422.541    0.000 42521.341    0.022 agent.py:106(TD_learn)
                1905751  131.832    0.000 21042.500    0.011 memory.py:35(sample_distribution)
                1905751  233.258    0.000 20407.533    0.011 helpers.py:15(stack)
        160309280/9607716  756.925    0.000 11732.667    0.001 module.py:715(_call_impl)
                5796214  154.156    0.000 11334.291    0.002 agent.py:235(forward)
               17388750 10365.130    0.001 10365.184    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               17388642 9436.174    0.001 9436.174    0.001 {built-in method cat}
                1984712   54.248    0.000 7519.611    0.004 environments.py:83(step)
                1984712   43.682    0.000 7479.988    0.004 agent.py:72(chooseMulti)
              257609347 7092.273    0.000 7092.273    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               23184856  211.798    0.000 7090.291    0.000 container.py:115(forward)
                3811502   27.535    0.000 6442.046    0.002 grad_mode.py:23(decorate_context)
                3811502  183.570    0.000 6371.000    0.002 adam.py:55(step)
                1906741    8.207    0.000 5882.626    0.003 agent.py:58(rememberMulti)
                1906741  253.752    0.000 5874.420    0.003 agent.py:63(<listcomp>)
                3811502 1196.761    0.000 5506.484    0.001 functional.py:53(adam)
                1984712   56.901    0.000 4915.586    0.002 environments.py:85(<listcomp>)
               39758056 1157.912    0.000 4867.789    0.000 helpers.py:8(clean)
                3811502   31.206    0.000 4549.677    0.001 tensor.py:181(backward)
                3811502   19.420    0.000 4518.471    0.001 __init__.py:68(backward)
                3811502 4386.291    0.001 4386.291    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               45475309 4220.029    0.000 4220.029    0.000 {built-in method as_tensor}
               34777284   63.368    0.000 3310.290    0.000 conv.py:422(forward)
               34777284   71.240    0.000 3217.555    0.000 conv.py:414(_conv_forward)
               34777284 3133.653    0.000 3133.653    0.000 {built-in method conv2d}
                1906750   87.197    0.000 2917.844    0.002 agent.py:88(<listcomp>)
               38135000  120.471    0.000 2579.540    0.000 exploration.py:34(epsilonGreedy)
                1984712   43.597    0.000 2405.699    0.001 environments.py:84(<listcomp>)
               39694240  152.238    0.000 2362.102    0.000 interop.py:274(step)
                5796220  352.351    0.000 2139.536    0.000 rnn.py:110(flatten_parameters)
                5796214   69.391    0.000 1519.649    0.000 rnn.py:555(forward)
               23184856   50.249    0.000 1446.250    0.000 linear.py:92(forward)
                5796217 1377.552    0.000 1377.552    0.000 {built-in method _cudnn_rnn_flatten_weight}
                5796214 1370.101    0.000 1370.101    0.000 {built-in method lstm}
               23184856   95.283    0.000 1369.218    0.000 functional.py:1669(linear)
              320166276  818.413    0.000 1292.606    0.000 tensor.py:933(grad)
                3811502  131.932    0.000 1289.951    0.000 optimizer.py:167(zero_grad)
               57962140   51.978    0.000 1198.981    0.000 activation.py:713(forward)
               91476048 1163.018    0.000 1163.018    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57962140   77.621    0.000 1147.003    0.000 functional.py:1292(leaky_relu)
               39694240   18.588    0.000 1082.206    0.000 wrapper.py:25(act)
               39694240   57.379    0.000 1063.618    0.000 env.py:197(act)
               57962140 1061.790    0.000 1061.790    0.000 {built-in method torch._C._nn.leaky_relu}
               91476048  976.467    0.000  976.467    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               39694240  966.448    0.000  970.098    0.000 libenv.py:352(act)
               23184856  942.539    0.000  942.539    0.000 {built-in method addmm}
               79452296   62.401    0.000  686.255    0.000 extract_dict_ob.py:9(observe)
               79452296   35.534    0.000  623.854    0.000 wrapper.py:19(observe)
               45738024  603.965    0.000  603.965    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               79452296  158.215    0.000  588.320    0.000 libenv.py:344(observe)
              389089372  208.072    0.000  570.116    0.000 overrides.py:1073(has_torch_function)
               45738024  558.596    0.000  558.596    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               45738024  520.967    0.000  520.967    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               45738024  470.610    0.000  470.610    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   1945    0.758    0.000  448.798    0.231 agent.py:161(update_target_network)
              119146536  124.144    0.000  417.209    0.000 libenv.py:281(_maybe_copy_dict)
              285533280  411.525    0.000  411.525    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10932025  148.552    0.000  373.673    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              357441553  371.868    0.000  371.868    0.000 {method 'copy' of 'numpy.ndarray' objects}
               45738024  364.910    0.000  364.910    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              419897256  141.989    0.000  345.801    0.000 {built-in method builtins.any}
               39694240   35.564    0.000  312.709    0.000 wrapper.py:22(get_info)
                5954136   10.920    0.000  306.369    0.000 functional.py:74(split)
               26998193  284.408    0.000  305.182    0.000 module.py:781(__setattr__)
                5954136   26.457    0.000  294.660    0.000 tensor.py:460(split)
                3811502   10.452    0.000  277.821    0.000 loss.py:445(forward)
                1905751  212.749    0.000  277.184    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               39694240  146.608    0.000  277.146    0.000 libenv.py:363(get_info)
                3811502   30.540    0.000  267.369    0.000 functional.py:2637(mse_loss)
                5954136  266.802    0.000  266.802    0.000 {function Tensor.split at 0x7fc401488d30}
               23769941   21.997    0.000  261.727    0.000 <__array_function__ internals>:2(prod)
               39694240  260.482    0.000  260.482    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               38134820  258.893    0.000  258.893    0.000 memory.py:17(inner)
               41603881  240.091    0.000  240.091    0.000 {built-in method numpy.array}
                   1945   67.920    0.035  236.273    0.121 memory.py:45(update_distribution)
               23769981   17.389    0.000  235.915    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               23184856  227.805    0.000  227.805    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5796214   15.476    0.000  222.253    0.000 pooling.py:152(forward)
               23769941   29.534    0.000  218.525    0.000 fromnumeric.py:2881(prod)
                5796214   10.346    0.000  206.778    0.000 _jit_internal.py:257(fn)
                7623004  205.733    0.000  205.733    0.000 {built-in method gather}
              801363600  161.490    0.000  200.826    0.000 overrides.py:1086(<genexpr>)
                5796214   10.900    0.000  195.338    0.000 functional.py:574(_max_pool2d)
                1906750  173.214    0.000  193.465    0.000 agent.py:152(convert_values)
                   3890  168.792    0.043  191.184    0.049 {built-in method _pickle.loads}
               23769941   52.366    0.000  188.992    0.000 fromnumeric.py:70(_wrapreduction)
                5796214  183.682    0.000  183.682    0.000 {built-in method max_pool2d}
               26917397  177.573    0.000  177.573    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                3811502  167.194    0.000  167.194    0.000 {built-in method torch._C._nn.mse_loss}
               23184868  141.546    0.000  159.989    0.000 __init__.py:67(is_acceptable)
                1905751  150.199    0.000  150.199    0.000 memory.py:43(<listcomp>)
                1984712   22.410    0.000  144.078    0.000 environments.py:86(<listcomp>)
                1984712   14.010    0.000  141.398    0.000 collector.py:8(collect)
               25677637  138.901    0.000  138.901    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              158904592   42.337    0.000  130.663    0.000 libenv.py:271(_maybe_copy_ndarray)
                3969425  126.527    0.000  126.527    0.000 {built-in method builtins.sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8587607: <NOPE_final_miner_0> in cluster <dcc> Done

Job <NOPE_final_miner_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 25 20:02:00 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Dec 26 04:23:56 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Dec 26 04:23:56 2020
Terminated at Sat Dec 26 22:19:30 2020
Results reported at Sat Dec 26 22:19:30 2020

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

    CPU time :                                   66465.00 sec.
    Max Memory :                                 56136 MB
    Average Memory :                             55370.68 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5304.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64607 sec.
    Turnaround time :                            94650 sec.

The output (if any) is above this job summary.

