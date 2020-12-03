
    Name :                      Final_stateUncertainty0and0bigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      15518572181 function calls (15262354804 primitive calls) in 82550.26 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82550.264 82550.264 {built-in method builtins.exec}
                      1    0.045    0.045 82550.264 82550.264 <string>:1(<module>)
                      1  451.133  451.133 82550.219 82550.219 main.py:92(main)
                2537057  195.675    0.000 53885.405    0.021 agent.py:86(learn)
                2536557  701.816    0.000 52710.962    0.021 agent.py:96(TD_learn)
                2536557  155.012    0.000 25761.140    0.010 memory.py:35(sample_distribution)
                2536557  229.138    0.000 25008.450    0.010 helpers.py:15(stack)
        273967656/17756899 1073.186    0.000 14837.575    0.001 module.py:715(_call_impl)
                7610171  212.252    0.000 13674.148    0.002 agent.py:212(forward)
               25367678 13221.712    0.001 13221.790    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2537057  189.677    0.000 11933.429    0.005 agent.py:74(chooseMulti)
               22830513 11255.498    0.000 11255.498    0.000 {built-in method cat}
              343702420 10311.443    0.000 10311.443    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               40587912  289.060    0.000 9738.290    0.000 container.py:115(forward)
                2537057   66.872    0.000 9123.610    0.004 environments.py:83(step)
                7609671   46.692    0.000 8227.937    0.001 grad_mode.py:23(decorate_context)
                7609671  292.892    0.000 8099.420    0.001 adam.py:55(step)
                2537057   96.012    0.000 6928.320    0.003 agent.py:62(rememberMulti)
                7609671 1503.831    0.000 6686.102    0.001 functional.py:53(adam)
                2537057  250.762    0.000 6444.139    0.003 agent.py:66(<listcomp>)
                2537057   68.642    0.000 6125.243    0.002 environments.py:85(<listcomp>)
               50890098 1538.491    0.000 6076.887    0.000 helpers.py:8(clean)
                7609671   54.409    0.000 5818.850    0.001 tensor.py:181(backward)
                7609671   28.889    0.000 5764.441    0.001 __init__.py:68(backward)
                2537057   92.521    0.000 5591.478    0.002 agent.py:84(<listcomp>)
                7609671 5570.194    0.001 5570.194    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               50741140  138.592    0.000 5257.828    0.000 exploration.py:33(epsilonGreedy)
               58499769 5059.981    0.000 5059.981    0.000 {built-in method as_tensor}
               45661026   78.563    0.000 3575.416    0.000 conv.py:422(forward)
               45661026   91.023    0.000 3461.379    0.000 conv.py:414(_conv_forward)
               45661026 3353.989    0.000 3353.989    0.000 {built-in method conv2d}
               60882368  123.771    0.000 3060.290    0.000 linear.py:92(forward)
               60882368  318.956    0.000 2875.541    0.000 functional.py:1669(linear)
                2537057   51.045    0.000 2756.705    0.001 environments.py:84(<listcomp>)
               50741140  191.677    0.000 2705.660    0.000 interop.py:274(step)
                7610177  363.798    0.000 2037.914    0.000 rnn.py:110(flatten_parameters)
              532677078 1193.173    0.000 2010.434    0.000 tensor.py:933(grad)
                7609671  178.125    0.000 1760.193    0.000 optimizer.py:167(zero_grad)
                7610171   77.095    0.000 1702.516    0.000 rnn.py:555(forward)
               53271197 1660.455    0.000 1660.455    0.000 {built-in method addmm}
               96396166   78.199    0.000 1538.678    0.000 activation.py:713(forward)
                7610171 1534.397    0.000 1534.397    0.000 {built-in method lstm}
               96396166  121.155    0.000 1460.479    0.000 functional.py:1292(leaky_relu)
              152193420 1349.866    0.000 1349.866    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               96396166 1327.199    0.000 1327.199    0.000 {built-in method torch._C._nn.leaky_relu}
                7610174 1254.823    0.000 1254.823    0.000 {built-in method _cudnn_rnn_flatten_weight}
               50741140   24.770    0.000 1177.101    0.000 wrapper.py:25(act)
               50741140   65.052    0.000 1152.331    0.000 env.py:197(act)
              152193420 1129.651    0.000 1129.651    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               50741140 1048.130    0.000 1053.045    0.000 libenv.py:352(act)
              669656402  353.399    0.000 1033.770    0.000 overrides.py:1073(has_torch_function)
                   5074    1.715    0.000  978.767    0.193 agent.py:139(update_target_network)
              101631238   75.029    0.000  809.704    0.000 extract_dict_ob.py:9(observe)
               76096710  793.117    0.000  793.117    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              101631238   46.240    0.000  734.675    0.000 wrapper.py:19(observe)
               76096710  697.732    0.000  697.732    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              101631238  183.215    0.000  688.435    0.000 libenv.py:344(observe)
              745758136  269.919    0.000  655.346    0.000 {built-in method builtins.any}
               76096710  631.900    0.000  631.900    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   5074  172.365    0.034  626.725    0.124 memory.py:45(update_distribution)
                2537057    6.503    0.000  598.070    0.000 agent.py:230(avoid_similar_state)
               76096710  555.750    0.000  555.750    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               53287845  536.212    0.000  536.212    0.000 {built-in method numpy.array}
              152372378  151.029    0.000  499.421    0.000 libenv.py:281(_maybe_copy_dict)
              457122208  431.385    0.000  431.385    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7609671   14.463    0.000  430.646    0.000 loss.py:445(forward)
               60882368  422.763    0.000  422.763    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7609671   48.199    0.000  416.184    0.000 functional.py:2637(mse_loss)
               76096710  409.855    0.000  409.855    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7611171   13.383    0.000  396.909    0.000 functional.py:74(split)
                7611171   32.036    0.000  382.466    0.000 tensor.py:460(split)
             1400195172  302.371    0.000  380.047    0.000 overrides.py:1086(<genexpr>)
               50741140   41.330    0.000  373.722    0.000 wrapper.py:22(get_info)
              381454400  363.887    0.000  363.887    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11561673  137.164    0.000  354.221    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7611171  348.606    0.000  348.606    0.000 {function Tensor.split at 0x7ff746dacca0}
               50741140  174.211    0.000  332.392    0.000 libenv.py:363(get_info)
               50741140  330.880    0.000  330.880    0.000 memory.py:17(inner)
                2536557  250.855    0.000  324.437    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               35515633  298.135    0.000  323.388    0.000 module.py:781(__setattr__)
                  10148  240.318    0.024  294.601    0.029 {built-in method _pickle.loads}
                2537057  220.676    0.000  268.491    0.000 agent.py:131(convert_values)
               25660043   23.162    0.000  256.363    0.000 <__array_function__ internals>:2(prod)
                7609671  250.281    0.000  250.281    0.000 {built-in method torch._C._nn.mse_loss}
               50741140  241.129    0.000  241.129    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               10146228  234.725    0.000  234.725    0.000 {built-in method gather}
                7610171   17.454    0.000  231.859    0.000 pooling.py:152(forward)
               45660026  229.663    0.000  229.663    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               25660083   19.144    0.000  228.955    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7610171   11.783    0.000  214.406    0.000 _jit_internal.py:257(fn)
                2922679  212.380    0.000  212.380    0.000 {built-in method tensor}
                7611171  210.433    0.000  210.433    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               25660043   28.054    0.000  209.810    0.000 fromnumeric.py:2881(prod)
               76096956   91.757    0.000  206.807    0.000 tensor.py:596(__hash__)
                7610171   12.565    0.000  201.414    0.000 functional.py:574(_max_pool2d)
              269301590  187.808    0.000  188.035    0.000 module.py:765(__getattr__)
                7610171  187.884    0.000  187.884    0.000 {built-in method max_pool2d}
                2536557  185.255    0.000  185.255    0.000 memory.py:43(<listcomp>)
               25660043   56.370    0.000  181.756    0.000 fromnumeric.py:70(_wrapreduction)
                2537057   26.169    0.000  174.790    0.000 environments.py:86(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 8466076: <Final_stateUncertainty0and0bigfish_0> in cluster <dcc> Done

Job <Final_stateUncertainty0and0bigfish_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Wed Dec  2 12:09:13 2020
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec  2 12:18:58 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec  2 12:18:58 2020
Terminated at Thu Dec  3 11:15:11 2020
Results reported at Thu Dec  3 11:15:11 2020

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

    CPU time :                                   85504.00 sec.
    Max Memory :                                 54786 MB
    Average Memory :                             54038.92 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6654.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82573 sec.
    Turnaround time :                            83158 sec.

The output (if any) is above this job summary.

