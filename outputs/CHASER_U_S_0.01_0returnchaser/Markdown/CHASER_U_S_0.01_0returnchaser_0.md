
    Name :                      CHASER_U_S_0.01_0returnchaser-0
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
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      13911954401 function calls (13682341731 primitive calls) in 82514.27 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82514.268 82514.268 {built-in method builtins.exec}
                      1    0.025    0.025 82514.268 82514.268 <string>:1(<module>)
                      1  501.454  501.454 82514.240 82514.240 main.py:92(main)
                2336781  247.986    0.000 56402.505    0.024 agent.py:84(learn)
                2243827  957.154    0.000 55614.155    0.025 agent.py:99(TD_learn)
                2243827  158.208    0.000 24506.787    0.011 memory.py:35(sample_distribution)
                2243827  261.620    0.000 23743.382    0.011 helpers.py:15(stack)
        245406792/15800742 1062.878    0.000 16653.595    0.001 module.py:715(_call_impl)
                6824435  222.135    0.000 15401.063    0.002 agent.py:231(forward)
               22718239 12195.699    0.001 12195.718    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20473305 10928.846    0.001 10928.846    0.001 {built-in method cat}
               36367001  304.362    0.000 10753.672    0.000 container.py:115(forward)
                6731481   44.907    0.000 9557.156    0.001 grad_mode.py:23(decorate_context)
                6731481  284.027    0.000 9438.613    0.001 adam.py:55(step)
                2336781   64.756    0.000 9220.259    0.004 environments.py:83(step)
                2336781  214.278    0.000 8864.909    0.004 agent.py:70(chooseMulti)
                6731481 1759.867    0.000 8118.171    0.001 functional.py:53(adam)
                2244826   96.485    0.000 7342.776    0.003 agent.py:58(rememberMulti)
                2244826  292.993    0.000 6861.534    0.003 agent.py:62(<listcomp>)
              304911922 6674.499    0.000 6674.499    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6731481   48.847    0.000 6455.743    0.001 tensor.py:181(backward)
                6731481   31.173    0.000 6406.896    0.001 __init__.py:68(backward)
                6731481 6191.601    0.001 6191.601    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2336781   65.644    0.000 5771.636    0.002 environments.py:85(<listcomp>)
               47103015 1347.860    0.000 5756.825    0.000 helpers.py:8(clean)
               53834496 4981.636    0.000 4981.636    0.000 {built-in method as_tensor}
               40946610   71.050    0.000 3957.980    0.000 conv.py:422(forward)
               40946610   83.840    0.000 3852.076    0.000 conv.py:414(_conv_forward)
               40946610 3753.699    0.000 3753.699    0.000 {built-in method conv2d}
               54505523  121.629    0.000 3419.087    0.000 linear.py:92(forward)
               54505523  320.202    0.000 3241.645    0.000 functional.py:1669(linear)
                2336781   49.032    0.000 3135.942    0.001 environments.py:84(<listcomp>)
               46735620  183.443    0.000 3086.910    0.000 interop.py:274(step)
                6824441  428.346    0.000 2641.984    0.000 rnn.py:110(flatten_parameters)
               47771045 1924.921    0.000 1924.921    0.000 {built-in method addmm}
              471203778 1216.286    0.000 1918.250    0.000 tensor.py:933(grad)
                2244826  102.978    0.000 1881.635    0.001 agent.py:82(<listcomp>)
                6731481  191.466    0.000 1864.100    0.000 optimizer.py:167(zero_grad)
                6824435   78.416    0.000 1810.167    0.000 rnn.py:555(forward)
               86382872   77.140    0.000 1778.972    0.000 activation.py:713(forward)
              134629620 1739.309    0.000 1739.309    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6824438 1712.311    0.000 1712.311    0.000 {built-in method _cudnn_rnn_flatten_weight}
               86382872  111.166    0.000 1701.832    0.000 functional.py:1292(leaky_relu)
                6824435 1636.992    0.000 1636.992    0.000 {built-in method lstm}
               86382872 1580.447    0.000 1580.447    0.000 {built-in method torch._C._nn.leaky_relu}
               46735620   21.717    0.000 1569.854    0.000 wrapper.py:25(act)
               46735620   69.246    0.000 1548.137    0.000 env.py:197(act)
               44896520  151.444    0.000 1472.675    0.000 exploration.py:34(epsilonGreedy)
               46735620 1432.439    0.000 1436.637    0.000 libenv.py:352(act)
              134629620 1435.491    0.000 1435.491    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              593024357  328.760    0.000  902.423    0.000 overrides.py:1073(has_torch_function)
               67314810  890.333    0.000  890.333    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67314810  828.491    0.000  828.491    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               93838635   73.632    0.000  824.701    0.000 extract_dict_ob.py:9(observe)
               67314810  760.053    0.000  760.053    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               93838635   39.200    0.000  751.070    0.000 wrapper.py:19(observe)
               93838635  189.834    0.000  711.870    0.000 libenv.py:344(observe)
               67314810  681.168    0.000  681.168    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2244826    6.403    0.000  644.721    0.000 agent.py:249(avoid_similar_state)
              660992866  229.191    0.000  551.436    0.000 {built-in method builtins.any}
              346279294  544.982    0.000  544.982    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                   2336    0.922    0.000  540.365    0.231 agent.py:157(update_target_network)
               54505523  522.946    0.000  522.946    0.000 {method 't' of 'torch._C._TensorBase' objects}
               67314810  520.083    0.000  520.083    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              140574255  148.700    0.000  508.793    0.000 libenv.py:281(_maybe_copy_dict)
                6731481   13.999    0.000  457.596    0.000 loss.py:445(forward)
              421725101  451.338    0.000  451.338    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6731481   46.085    0.000  443.597    0.000 functional.py:2637(mse_loss)
               11270297  163.542    0.000  411.933    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               31787229  360.794    0.000  387.163    0.000 module.py:781(__setattr__)
                7010343   13.009    0.000  383.602    0.000 functional.py:74(split)
               13462962  374.647    0.000  374.647    0.000 {built-in method gather}
                7010343   30.720    0.000  369.674    0.000 tensor.py:460(split)
               46735620   40.578    0.000  363.473    0.000 wrapper.py:22(get_info)
                2243827  263.252    0.000  339.218    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                7010343  337.292    0.000  337.292    0.000 {function Tensor.split at 0x7fdd37ea1d30}
               51979837  334.639    0.000  334.639    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               44896520  325.932    0.000  325.932    0.000 memory.py:17(inner)
               46735620  171.465    0.000  322.895    0.000 libenv.py:363(get_info)
             1240554237  253.952    0.000  317.280    0.000 overrides.py:1086(<genexpr>)
               46735620  317.203    0.000  317.203    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24784561   24.404    0.000  291.027    0.000 <__array_function__ internals>:2(prod)
               48984119  290.953    0.000  290.953    0.000 {built-in method numpy.array}
                   2336   81.640    0.035  285.682    0.122 memory.py:45(update_distribution)
                2244826  278.299    0.000  284.918    0.000 agent.py:149(convert_values)
                6731481  282.925    0.000  282.925    0.000 {built-in method torch._C._nn.mse_loss}
                6824435   16.267    0.000  265.421    0.000 pooling.py:152(forward)
               24784601   19.187    0.000  262.515    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6824435   12.289    0.000  249.154    0.000 _jit_internal.py:257(fn)
                2336781   29.130    0.000  247.926    0.000 environments.py:86(<listcomp>)
               24784561   31.584    0.000  243.328    0.000 fromnumeric.py:2881(prod)
                6734478  240.204    0.000  240.204    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6824435   11.898    0.000  235.670    0.000 functional.py:574(_max_pool2d)
                   4672  202.557    0.043  229.310    0.049 {built-in method _pickle.loads}
                6824435  223.029    0.000  223.029    0.000 {built-in method max_pool2d}
               13463961  220.061    0.000  220.061    0.000 {method 'type' of 'torch._C._TensorBase' objects}
               46735640   33.829    0.000  218.800    0.000 environments.py:89(reset)
               24784561   56.246    0.000  211.744    0.000 fromnumeric.py:70(_wrapreduction)
               27297752  184.190    0.000  204.835    0.000 __init__.py:67(is_acceptable)
                2422360  200.640    0.000  200.640    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8557117: <CHASER_U_S_0.01_0returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0.01_0returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:12 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Dec 13 15:34:50 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Dec 13 15:34:50 2020
Terminated at Mon Dec 14 14:30:09 2020
Results reported at Mon Dec 14 14:30:09 2020

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

    CPU time :                                   84066.00 sec.
    Max Memory :                                 55055 MB
    Average Memory :                             54348.33 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6385.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82519 sec.
    Turnaround time :                            256917 sec.

The output (if any) is above this job summary.

