
    Name :                      Uncertainty0state_difference0.1softepsdodgeball-0
    Discount :                  0.995
    Environment :               dodgeball
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsintosoftmax
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.1
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      15621458886 function calls (15378282629 primitive calls) in 82517.20 seconds

##    Ordered by: cumulative time
   List reduced from 1358 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82517.199 82517.199 {built-in method builtins.exec}
                      1    0.056    0.056 82517.199 82517.199 <string>:1(<module>)
                      1  432.300  432.300 82517.142 82517.142 main.py:92(main)
                2407937  179.067    0.000 50371.342    0.021 agent.py:86(learn)
                2407437  653.868    0.000 49360.608    0.021 agent.py:96(TD_learn)
                2407437  133.464    0.000 24282.199    0.010 memory.py:35(sample_distribution)
                2407437  209.130    0.000 23613.609    0.010 helpers.py:15(stack)
                2407937  176.752    0.000 15899.617    0.007 agent.py:74(chooseMulti)
        260022696/16853059 1042.113    0.000 13978.573    0.001 module.py:715(_call_impl)
                7222811  193.870    0.000 12892.033    0.002 agent.py:212(forward)
               24076478 12460.248    0.001 12460.295    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               21668433 10748.416    0.000 10748.416    0.000 {built-in method cat}
              325748431 10184.988    0.000 10184.988    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2407937  135.069    0.000 9895.262    0.004 agent.py:84(<listcomp>)
               48158740 1288.678    0.000 9392.100    0.000 exploration.py:40(epsintosoftmax)
               38521992  267.651    0.000 9184.374    0.000 container.py:115(forward)
                2407937   62.628    0.000 9078.136    0.004 environments.py:83(step)
                7222311   43.325    0.000 7567.684    0.001 grad_mode.py:23(decorate_context)
                7222311  286.183    0.000 7447.584    0.001 adam.py:55(step)
                2407937   90.660    0.000 6553.849    0.003 agent.py:62(rememberMulti)
                7222311 1382.167    0.000 6117.905    0.001 functional.py:53(adam)
                2407937  214.590    0.000 6100.223    0.003 agent.py:66(<listcomp>)
                2407937   65.005    0.000 5772.054    0.002 environments.py:85(<listcomp>)
               48524506 1457.388    0.000 5757.123    0.000 helpers.py:8(clean)
                7222311   43.920    0.000 5350.007    0.001 tensor.py:181(backward)
                7222311   28.017    0.000 5306.087    0.001 __init__.py:68(backward)
                7222311 5120.930    0.001 5120.930    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               55746817 4688.892    0.000 4688.892    0.000 {built-in method as_tensor}
               43336866   73.696    0.000 3338.482    0.000 conv.py:422(forward)
               43336866   80.405    0.000 3232.251    0.000 conv.py:414(_conv_forward)
               43336866 3136.406    0.000 3136.406    0.000 {built-in method conv2d}
                2407937   47.909    0.000 3029.636    0.001 environments.py:84(<listcomp>)
               48158740  176.212    0.000 2981.727    0.000 interop.py:274(step)
               57783488  123.948    0.000 2885.871    0.000 linear.py:92(forward)
               57783488  300.024    0.000 2700.702    0.000 functional.py:1669(linear)
               48158740 1667.831    0.000 2498.144    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7222817  347.188    0.000 1921.280    0.000 rnn.py:110(flatten_parameters)
              505561878 1108.858    0.000 1874.777    0.000 tensor.py:933(grad)
                7222311  171.987    0.000 1653.896    0.000 optimizer.py:167(zero_grad)
                7222811   71.020    0.000 1609.906    0.000 rnn.py:555(forward)
               50559677 1562.379    0.000 1562.379    0.000 {built-in method addmm}
               48158740   22.567    0.000 1540.816    0.000 wrapper.py:25(act)
               48158740   60.670    0.000 1518.249    0.000 env.py:197(act)
               91489606   74.626    0.000 1465.263    0.000 activation.py:713(forward)
                7222811 1454.187    0.000 1454.187    0.000 {built-in method lstm}
               48158740 1423.074    0.000 1427.669    0.000 libenv.py:352(act)
               91489606  113.789    0.000 1390.636    0.000 functional.py:1292(leaky_relu)
               91489606 1265.494    0.000 1265.494    0.000 {built-in method torch._C._nn.leaky_relu}
              144446220 1235.588    0.000 1235.588    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                7222814 1178.956    0.000 1178.956    0.000 {built-in method _cudnn_rnn_flatten_weight}
              144446220 1052.392    0.000 1052.392    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              635568722  335.174    0.000  973.661    0.000 overrides.py:1073(has_torch_function)
                   4815    1.612    0.000  831.667    0.173 agent.py:139(update_target_network)
               96683246   75.123    0.000  782.056    0.000 extract_dict_ob.py:9(observe)
               96683246   41.004    0.000  706.933    0.000 wrapper.py:19(observe)
               72223110  695.449    0.000  695.449    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               96683246  174.574    0.000  665.930    0.000 libenv.py:344(observe)
               36723751   65.164    0.000  651.721    0.000 functional.py:1479(softmax)
               72223110  640.012    0.000  640.012    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               62001306   63.392    0.000  630.898    0.000 <__array_function__ internals>:2(prod)
              707796856  250.816    0.000  615.604    0.000 {built-in method builtins.any}
               72223110  582.737    0.000  582.737    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               36723751  581.069    0.000  581.069    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2407937    6.245    0.000  560.544    0.000 agent.py:230(avoid_similar_state)
               62001346   50.515    0.000  555.344    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               72223110  507.465    0.000  507.465    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               62001306   74.464    0.000  504.829    0.000 fromnumeric.py:2881(prod)
                   4815  143.972    0.030  501.832    0.104 memory.py:45(update_distribution)
              144841986  148.921    0.000  482.986    0.000 libenv.py:281(_maybe_copy_dict)
               50575807  432.087    0.000  432.087    0.000 {built-in method numpy.array}
               62001306  144.705    0.000  430.366    0.000 fromnumeric.py:70(_wrapreduction)
              434530773  412.333    0.000  412.333    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7223811   13.110    0.000  411.126    0.000 functional.py:74(split)
                7222311   12.540    0.000  399.024    0.000 loss.py:445(forward)
                7223811   30.272    0.000  397.075    0.000 tensor.py:460(split)
               57783488  395.100    0.000  395.100    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7222311   44.817    0.000  386.484    0.000 functional.py:2637(mse_loss)
               72223110  381.641    0.000  381.641    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               48158740  368.092    0.000  368.092    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7223811  365.306    0.000  365.306    0.000 {function Tensor.split at 0x7f9b47df2d30}
             1328920932  290.951    0.000  359.726    0.000 overrides.py:1086(<genexpr>)
              361129995  354.660    0.000  354.660    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               48158740   37.352    0.000  351.031    0.000 wrapper.py:22(get_info)
               48158740  162.230    0.000  313.679    0.000 libenv.py:363(get_info)
               33707953  283.631    0.000  305.890    0.000 module.py:781(__setattr__)
               48158740  303.983    0.000  303.983    0.000 memory.py:17(inner)
                2407437  217.548    0.000  276.030    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   9630  224.752    0.023  275.929    0.029 {built-in method _pickle.loads}
                2407937  216.856    0.000  264.829    0.000 agent.py:131(convert_values)
               64413558  246.013    0.000  246.013    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                7222311  231.444    0.000  231.444    0.000 {built-in method torch._C._nn.mse_loss}
                9629748  220.382    0.000  220.382    0.000 {built-in method gather}
               43335866  215.236    0.000  215.236    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2407937   26.035    0.000  213.819    0.000 environments.py:86(<listcomp>)
                7222811   13.209    0.000  213.459    0.000 pooling.py:152(forward)
                7222811   12.450    0.000  200.251    0.000 _jit_internal.py:257(fn)
                2773875  198.247    0.000  198.247    0.000 {built-in method tensor}
                7223811  196.252    0.000  196.252    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               72223356   85.808    0.000  192.142    0.000 tensor.py:596(__hash__)
               48158760   30.939    0.000  187.796    0.000 environments.py:89(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8483545: <Uncertainty0state_difference0.1softepsdodgeball_0> in cluster <dcc> Done

Job <Uncertainty0state_difference0.1softepsdodgeball_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec  6 01:18:08 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Dec  6 11:05:44 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec  6 11:05:44 2020
Terminated at Mon Dec  7 10:01:08 2020
Results reported at Mon Dec  7 10:01:08 2020

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

    CPU time :                                   85880.00 sec.
    Max Memory :                                 54804 MB
    Average Memory :                             54124.61 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6636.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82523 sec.
    Turnaround time :                            117780 sec.

The output (if any) is above this job summary.

