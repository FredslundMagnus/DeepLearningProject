[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0.01_0.01returnbigfish-0
    Discount :                  0.995
    Environment :               bigfish
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


      9917468305 function calls (9689163894 primitive calls) in 82519.24 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82519.242 82519.242 {built-in method builtins.exec}
                      1    0.025    0.025 82519.242 82519.242 <string>:1(<module>)
                      1  485.859  485.859 82519.216 82519.216 main.py:92(main)
                2323828  234.453    0.000 54932.623    0.024 agent.py:84(learn)
                2230874  923.862    0.000 54125.887    0.024 agent.py:99(TD_learn)
                2230874  157.405    0.000 25149.813    0.011 memory.py:35(sample_distribution)
                2230874  321.465    0.000 24361.828    0.011 helpers.py:15(stack)
        244007868/15710071 1134.307    0.000 16159.996    0.001 module.py:710(_call_impl)
                6785576  213.500    0.000 14910.110    0.002 agent.py:231(forward)
               20356728 12014.524    0.001 12014.524    0.001 {built-in method cat}
               22588709 11880.936    0.001 11880.950    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               36159753  307.986    0.000 10571.019    0.000 container.py:115(forward)
                2323828  218.939    0.000 9875.866    0.004 agent.py:70(chooseMulti)
                2323828   69.814    0.000 9483.947    0.004 environments.py:83(step)
                6692622   39.777    0.000 8948.044    0.001 grad_mode.py:12(decorate_context)
                6692622 2118.216    0.000 8859.610    0.001 adam.py:51(step)
              303107558 7747.300    0.000 7747.300    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2231873  106.880    0.000 7531.784    0.003 agent.py:58(rememberMulti)
                2231873  326.410    0.000 7016.240    0.003 agent.py:62(<listcomp>)
                6692622   29.709    0.000 6483.113    0.001 tensor.py:155(backward)
                6692622   35.227    0.000 6453.405    0.001 __init__.py:57(backward)
                6692622 6247.459    0.001 6247.459    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2323828   69.876    0.000 6114.009    0.003 environments.py:85(<listcomp>)
               46630954 1563.596    0.000 6067.528    0.000 helpers.py:8(clean)
               53323576 5027.370    0.000 5027.370    0.000 {built-in method as_tensor}
               40713456   79.985    0.000 3844.612    0.000 conv.py:418(forward)
               40713456   80.027    0.000 3731.815    0.000 conv.py:410(_conv_forward)
               40713456 3636.235    0.000 3636.235    0.000 {built-in method conv2d}
               54194651  123.534    0.000 3274.990    0.000 linear.py:90(forward)
               54194651  338.301    0.000 3094.426    0.000 functional.py:1655(linear)
                2323828   56.372    0.000 3072.625    0.001 environments.py:84(<listcomp>)
               46476560  203.494    0.000 3016.252    0.000 interop.py:274(step)
                2231873  107.849    0.000 2888.520    0.001 agent.py:82(<listcomp>)
               44637460  160.416    0.000 2483.394    0.000 exploration.py:34(epsilonGreedy)
                6785582  358.763    0.000 2316.063    0.000 rnn.py:109(flatten_parameters)
               47499032 1846.366    0.000 1846.366    0.000 {built-in method addmm}
                6785576   76.726    0.000 1813.068    0.000 rnn.py:550(forward)
               85890658   76.733    0.000 1772.559    0.000 activation.py:653(forward)
              133852440 1750.023    0.000 1750.023    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               85890658  125.841    0.000 1695.826    0.000 functional.py:1277(leaky_relu)
                6785576 1642.784    0.000 1642.784    0.000 {built-in method lstm}
               85890658 1558.122    0.000 1558.122    0.000 {built-in method torch._C._nn.leaky_relu}
              133852440 1557.077    0.000 1557.077    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6785579 1532.896    0.000 1532.896    0.000 {built-in method _cudnn_rnn_flatten_weight}
               46476560   22.550    0.000 1337.597    0.000 wrapper.py:25(act)
               46476560   76.499    0.000 1315.047    0.000 env.py:197(act)
               46476560 1186.888    0.000 1191.596    0.000 libenv.py:352(act)
               66926220  986.441    0.000  986.441    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               93107514   80.946    0.000  895.038    0.000 extract_dict_ob.py:9(observe)
                6692622  141.671    0.000  894.065    0.000 optimizer.py:166(zero_grad)
               93107514   41.522    0.000  814.093    0.000 wrapper.py:19(observe)
               66926220  813.034    0.000  813.034    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               93107514  209.908    0.000  772.570    0.000 libenv.py:344(observe)
               66926220  709.039    0.000  709.039    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               66926220  689.575    0.000  689.575    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2231873    6.449    0.000  639.261    0.000 agent.py:249(avoid_similar_state)
              344680731  592.826    0.000  592.826    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                   2323    0.945    0.000  572.283    0.246 agent.py:157(update_target_network)
              139584074  168.356    0.000  549.063    0.000 libenv.py:281(_maybe_copy_dict)
               66926220  543.731    0.000  543.731    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              418754545  484.738    0.000  484.738    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6692622   13.236    0.000  463.180    0.000 loss.py:444(forward)
               54194651  458.232    0.000  458.232    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6692622   55.314    0.000  449.944    0.000 functional.py:2621(mse_loss)
               11260854  163.618    0.000  414.910    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               46476560   43.307    0.000  407.686    0.000 wrapper.py:22(get_info)
               46476560  190.354    0.000  364.380    0.000 libenv.py:363(get_info)
               44637460  356.894    0.000  356.894    0.000 memory.py:17(inner)
               13385244  353.931    0.000  353.931    0.000 {built-in method gather}
               31605887  320.003    0.000  343.457    0.000 module.py:774(__setattr__)
                2230874  264.455    0.000  341.519    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               51681918  326.876    0.000  326.876    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               48712080  320.460    0.000  320.460    0.000 {built-in method numpy.array}
               46476560  308.575    0.000  308.575    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                   2323   84.180    0.036  307.443    0.132 memory.py:45(update_distribution)
                2231873  283.860    0.000  302.457    0.000 agent.py:149(convert_values)
               24752722   24.518    0.000  293.767    0.000 <__array_function__ internals>:2(prod)
              334631208  255.730    0.000  292.696    0.000 tensor.py:725(grad)
                6692622  267.420    0.000  267.420    0.000 {built-in method torch._C._nn.mse_loss}
               24752762   19.374    0.000  264.612    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6785576   15.076    0.000  247.433    0.000 pooling.py:156(forward)
               24752722   31.059    0.000  245.238    0.000 fromnumeric.py:2881(prod)
                6971484   14.057    0.000  239.002    0.000 functional.py:68(split)
                   4646  211.467    0.046  238.836    0.051 {built-in method _pickle.loads}
                6785576   12.459    0.000  232.357    0.000 _jit_internal.py:237(fn)
                2408419  230.186    0.000  230.186    0.000 {built-in method tensor}
                2323828   29.730    0.000  227.499    0.000 environments.py:86(<listcomp>)
                6695619  225.935    0.000  225.935    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6971484   13.810    0.000  223.973    0.000 tensor.py:367(split)
                6785576   13.517    0.000  218.679    0.000 functional.py:564(_max_pool2d)
               24752722   59.783    0.000  214.179    0.000 fromnumeric.py:70(_wrapreduction)
               13386243  208.932    0.000  208.932    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                6971484  208.440    0.000  208.440    0.000 {function Tensor.split at 0x7fe75b5639d0}
                6785576  204.182    0.000  204.182    0.000 {built-in method max_pool2d}
              244007868  200.737    0.000  200.737    0.000 {built-in method torch._C._get_tracing_state}
               46476580   42.188    0.000  197.806    0.000 environments.py:89(reset)
               27142316  177.058    0.000  197.057    0.000 __init__.py:66(is_acceptable)
                2230874  195.743    0.000  195.743    0.000 memory.py:43(<listcomp>)
                2323828   19.409    0.000  184.781    0.000 collector.py:8(collect)
              186215028   53.510    0.000  170.749    0.000 libenv.py:271(_maybe_copy_ndarray)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 8557628: <BIGFISH_U_S_0.01_0.01returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0.01_0.01returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:47 2020
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Dec 15 13:55:50 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Dec 15 13:55:50 2020
Terminated at Wed Dec 16 12:51:17 2020
Results reported at Wed Dec 16 12:51:17 2020

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

    CPU time :                                   85273.00 sec.
    Max Memory :                                 54011 MB
    Average Memory :                             53351.02 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7429.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82527 sec.
    Turnaround time :                            420570 sec.

The output (if any) is above this job summary.

