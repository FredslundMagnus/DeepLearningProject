
    Name :                      BIGFISH_U_S_0.1_0bigfish-0
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
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      14041727265 function calls (13809298478 primitive calls) in 82513.95 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82513.953 82513.953 {built-in method builtins.exec}
                      1    0.071    0.071 82513.953 82513.953 <string>:1(<module>)
                      1  501.240  501.240 82513.881 82513.881 main.py:92(main)
                2366029  189.500    0.000 56490.137    0.024 agent.py:84(learn)
                2271076  783.568    0.000 55733.857    0.025 agent.py:99(TD_learn)
                2271076  158.292    0.000 24893.443    0.011 memory.py:35(sample_distribution)
                2271076  264.608    0.000 24133.417    0.011 helpers.py:15(stack)
        248415651/15993484 1079.412    0.000 16707.912    0.001 module.py:715(_call_impl)
                6908181  221.169    0.000 15449.763    0.002 agent.py:216(forward)
               22996726 12439.382    0.001 12439.459    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20724543 11082.657    0.001 11082.657    0.001 {built-in method cat}
               36812980  312.265    0.000 10841.695    0.000 container.py:115(forward)
                6813228   47.435    0.000 9702.856    0.001 grad_mode.py:23(decorate_context)
                6813228  282.476    0.000 9581.030    0.001 adam.py:55(step)
                2366029   63.830    0.000 9023.153    0.004 environments.py:83(step)
                2366029  217.333    0.000 8938.148    0.004 agent.py:70(chooseMulti)
                6813228 1791.873    0.000 8238.032    0.001 functional.py:53(adam)
                2272075   97.690    0.000 7376.683    0.003 agent.py:58(rememberMulti)
                2272075  293.492    0.000 6898.534    0.003 agent.py:62(<listcomp>)
              308681381 6797.646    0.000 6797.646    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6813228   51.387    0.000 6478.876    0.001 tensor.py:181(backward)
                6813228   34.556    0.000 6427.488    0.001 __init__.py:68(backward)
                6813228 6208.987    0.001 6208.987    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2366029   70.789    0.000 5925.434    0.003 environments.py:85(<listcomp>)
               47455890 1375.473    0.000 5873.541    0.000 helpers.py:8(clean)
               54269118 5068.519    0.000 5068.519    0.000 {built-in method as_tensor}
               41449086   75.234    0.000 3964.817    0.000 conv.py:422(forward)
               41449086   85.741    0.000 3855.165    0.000 conv.py:414(_conv_forward)
               41449086 3754.903    0.000 3754.903    0.000 {built-in method conv2d}
               55173492  118.452    0.000 3444.491    0.000 linear.py:92(forward)
               55173492  324.584    0.000 3264.732    0.000 functional.py:1669(linear)
                2366029   49.034    0.000 2855.244    0.001 environments.py:84(<listcomp>)
               47320580  187.927    0.000 2806.211    0.000 interop.py:274(step)
                6908187  423.867    0.000 2580.189    0.000 rnn.py:110(flatten_parameters)
              476926068 1244.483    0.000 1964.724    0.000 tensor.py:933(grad)
               48357267 1942.093    0.000 1942.093    0.000 {built-in method addmm}
                2272075  102.856    0.000 1934.201    0.001 agent.py:82(<listcomp>)
                6813228  186.651    0.000 1896.516    0.000 optimizer.py:167(zero_grad)
                6908181   85.795    0.000 1844.463    0.000 rnn.py:555(forward)
               87442322   74.366    0.000 1801.574    0.000 activation.py:713(forward)
              136264560 1769.088    0.000 1769.088    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               87442322  112.652    0.000 1727.208    0.000 functional.py:1292(leaky_relu)
                6908184 1672.368    0.000 1672.368    0.000 {built-in method _cudnn_rnn_flatten_weight}
                6908181 1664.728    0.000 1664.728    0.000 {built-in method lstm}
               87442322 1604.728    0.000 1604.728    0.000 {built-in method torch._C._nn.leaky_relu}
               45441500  150.793    0.000 1529.275    0.000 exploration.py:34(epsilonGreedy)
              136264560 1450.081    0.000 1450.081    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               47320580   23.037    0.000 1254.878    0.000 wrapper.py:25(act)
               47320580   72.086    0.000 1231.841    0.000 env.py:197(act)
               47320580 1112.595    0.000 1117.615    0.000 libenv.py:352(act)
              600232086  334.765    0.000  923.358    0.000 overrides.py:1073(has_torch_function)
               68132280  907.468    0.000  907.468    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               68132280  837.818    0.000  837.818    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               94776470   75.372    0.000  826.182    0.000 extract_dict_ob.py:9(observe)
               68132280  765.032    0.000  765.032    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               94776470   40.852    0.000  750.811    0.000 wrapper.py:19(observe)
               94776470  184.887    0.000  709.958    0.000 libenv.py:344(observe)
               68132280  690.915    0.000  690.915    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2272075    6.683    0.000  649.949    0.000 agent.py:234(avoid_similar_state)
              669032058  235.079    0.000  567.164    0.000 {built-in method builtins.any}
                   2366    0.941    0.000  566.780    0.240 agent.py:142(update_target_network)
               68132280  530.327    0.000  530.327    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               55173492  523.242    0.000  523.242    0.000 {method 't' of 'torch._C._TensorBase' objects}
              142097050  148.815    0.000  512.669    0.000 libenv.py:281(_maybe_copy_dict)
              346519961  498.914    0.000  498.914    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                6813228   13.731    0.000  463.808    0.000 loss.py:445(forward)
              426293516  455.711    0.000  455.711    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6813228   48.933    0.000  450.077    0.000 functional.py:2637(mse_loss)
               11295156  159.488    0.000  405.777    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7098087   13.366    0.000  400.575    0.000 functional.py:74(split)
                7098087   35.703    0.000  386.364    0.000 tensor.py:460(split)
               32176711  352.893    0.000  376.893    0.000 module.py:781(__setattr__)
               47320580   42.088    0.000  376.814    0.000 wrapper.py:22(get_info)
                7098087  349.039    0.000  349.039    0.000 {function Tensor.split at 0x7f71ba004d30}
               47320580  175.834    0.000  334.726    0.000 libenv.py:363(get_info)
                2271076  252.994    0.000  328.597    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
             1255637664  260.854    0.000  326.953    0.000 overrides.py:1086(<genexpr>)
               45441500  319.883    0.000  319.883    0.000 memory.py:17(inner)
               47320580  313.437    0.000  313.437    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               49596388  311.650    0.000  311.650    0.000 {built-in method numpy.array}
                   2366   87.025    0.037  310.027    0.131 memory.py:45(update_distribution)
               24861528   24.639    0.000  289.099    0.000 <__array_function__ internals>:2(prod)
                6813228  286.483    0.000  286.483    0.000 {built-in method torch._C._nn.mse_loss}
               41259180  281.605    0.000  281.605    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2272075  280.321    0.000  281.044    0.000 agent.py:134(convert_values)
                9084304  269.090    0.000  269.090    0.000 {built-in method gather}
                6908181   16.243    0.000  261.355    0.000 pooling.py:152(forward)
               24861568   19.007    0.000  260.446    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6908181   11.977    0.000  245.111    0.000 _jit_internal.py:257(fn)
               24861528   31.480    0.000  241.438    0.000 fromnumeric.py:2881(prod)
                6816225  237.436    0.000  237.436    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6908181   12.781    0.000  231.878    0.000 functional.py:574(_max_pool2d)
                   4732  203.380    0.043  230.661    0.049 {built-in method _pickle.loads}
                6908181  218.330    0.000  218.330    0.000 {built-in method max_pool2d}
               24861528   57.860    0.000  209.958    0.000 fromnumeric.py:70(_wrapreduction)
                2451889  196.238    0.000  196.238    0.000 {built-in method tensor}
               68132526   88.891    0.000  190.982    0.000 tensor.py:596(__hash__)
               27632736  169.166    0.000  189.261    0.000 __init__.py:67(is_acceptable)
                2271076  181.503    0.000  181.503    0.000 memory.py:43(<listcomp>)
                2366029   28.349    0.000  178.644    0.000 environments.py:86(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8552383: <BIGFISH_U_S_0.1_0bigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0.1_0bigfish_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Tue Dec  8 22:26:38 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec 10 01:02:49 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec 10 01:02:49 2020
Terminated at Thu Dec 10 23:58:10 2020
Results reported at Thu Dec 10 23:58:10 2020

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

    CPU time :                                   84165.00 sec.
    Max Memory :                                 54804 MB
    Average Memory :                             54098.88 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6636.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82522 sec.
    Turnaround time :                            178292 sec.

The output (if any) is above this job summary.

