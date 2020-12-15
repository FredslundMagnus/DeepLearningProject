[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0_0.01returnbigfish-0
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.01
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      11182519607 function calls (10924758841 primitive calls) in 82526.44 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82526.439 82526.439 {built-in method builtins.exec}
                      1    0.037    0.037 82526.439 82526.439 <string>:1(<module>)
                      1  568.527  568.527 82526.401 82526.401 main.py:92(main)
                2623669  269.938    0.000 53034.304    0.020 agent.py:84(learn)
                2518721  780.650    0.000 52132.070    0.021 agent.py:99(TD_learn)
                2518721  180.750    0.000 27937.706    0.011 memory.py:35(sample_distribution)
                2518721  325.825    0.000 27112.339    0.011 helpers.py:15(stack)
        275491146/17736994 1131.259    0.000 14814.275    0.001 module.py:710(_call_impl)
               25503161 13843.742    0.001 13843.784    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                7661111  226.673    0.000 13695.309    0.002 agent.py:231(forward)
                2623669  185.215    0.000 13615.131    0.005 agent.py:70(chooseMulti)
               22983333 12721.323    0.001 12721.323    0.001 {built-in method cat}
              343371531 11819.285    0.000 11819.285    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               40825275  281.698    0.000 9366.463    0.000 container.py:115(forward)
                2623669   72.718    0.000 8542.252    0.003 environments.py:83(step)
                2519720   88.282    0.000 7389.677    0.003 agent.py:82(<listcomp>)
               50394400  128.931    0.000 7088.281    0.000 exploration.py:34(epsilonGreedy)
                2519720   88.951    0.000 6565.421    0.003 agent.py:58(rememberMulti)
                7556163   39.926    0.000 6387.859    0.001 grad_mode.py:12(decorate_context)
                7556163 1623.897    0.000 6300.189    0.001 adam.py:51(step)
                2519720  233.356    0.000 6117.786    0.002 agent.py:62(<listcomp>)
                7556163   30.506    0.000 5509.180    0.001 tensor.py:155(backward)
                7556163   38.399    0.000 5478.674    0.001 __init__.py:57(backward)
                2623669   62.998    0.000 5430.305    0.002 environments.py:85(<listcomp>)
               52799404 1427.719    0.000 5406.172    0.000 helpers.py:8(clean)
                7556163 5282.119    0.001 5282.119    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               60355567 4554.674    0.000 4554.674    0.000 {built-in method as_tensor}
               45966666   83.146    0.000 3508.144    0.000 conv.py:418(forward)
               45966666   96.461    0.000 3387.299    0.000 conv.py:410(_conv_forward)
               45966666 3274.090    0.000 3274.090    0.000 {built-in method conv2d}
               61186937  119.551    0.000 2848.160    0.000 linear.py:90(forward)
                2623669   52.460    0.000 2823.626    0.001 environments.py:84(<listcomp>)
               52473380  184.970    0.000 2771.166    0.000 interop.py:274(step)
               61186937  306.033    0.000 2666.475    0.000 functional.py:1655(linear)
                7661117  379.874    0.000 2114.562    0.000 rnn.py:109(flatten_parameters)
                7661111   90.755    0.000 1905.043    0.000 rnn.py:550(forward)
                7661111 1710.536    0.000 1710.536    0.000 {built-in method lstm}
               53627777 1564.887    0.000 1564.887    0.000 {built-in method addmm}
               96972772   81.506    0.000 1435.728    0.000 activation.py:653(forward)
               96972772  126.293    0.000 1354.221    0.000 functional.py:1277(leaky_relu)
                7661114 1260.602    0.000 1260.602    0.000 {built-in method _cudnn_rnn_flatten_weight}
               96972772 1215.376    0.000 1215.376    0.000 {built-in method torch._C._nn.leaky_relu}
               52473380   22.104    0.000 1196.729    0.000 wrapper.py:25(act)
               52473380   60.185    0.000 1174.625    0.000 env.py:197(act)
              151123260 1170.993    0.000 1170.993    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52473380 1076.550    0.000 1081.228    0.000 libenv.py:352(act)
              151123260 1022.211    0.000 1022.211    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              105272784   77.095    0.000  856.400    0.000 extract_dict_ob.py:9(observe)
              105272784   45.752    0.000  779.305    0.000 wrapper.py:19(observe)
              105272784  194.100    0.000  733.553    0.000 libenv.py:344(observe)
               75561630  716.369    0.000  716.369    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   2623    1.040    0.000  632.296    0.241 agent.py:157(update_target_network)
               75561630  604.014    0.000  604.014    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7556163  104.607    0.000  593.083    0.000 optimizer.py:166(zero_grad)
              157746164  160.513    0.000  541.104    0.000 libenv.py:281(_maybe_copy_dict)
                2519720    6.024    0.000  530.455    0.000 agent.py:249(avoid_similar_state)
               75561630  485.807    0.000  485.807    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              473241115  465.050    0.000  465.050    0.000 {method 'copy' of 'numpy.ndarray' objects}
               75561630  460.952    0.000  460.952    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7556163   16.314    0.000  434.459    0.000 loss.py:444(forward)
                7556163   58.965    0.000  418.145    0.000 functional.py:2621(mse_loss)
               35683721  388.098    0.000  415.667    0.000 module.py:774(__setattr__)
              390010585  413.817    0.000  413.817    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               52473380   41.671    0.000  387.623    0.000 wrapper.py:22(get_info)
               61186937  377.031    0.000  377.031    0.000 {method 't' of 'torch._C._TensorBase' objects}
               11543993  144.716    0.000  371.451    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               50394400  365.868    0.000  365.868    0.000 memory.py:17(inner)
               52473380  178.764    0.000  345.951    0.000 libenv.py:363(get_info)
                   2623   95.334    0.036  339.456    0.129 memory.py:45(update_distribution)
                2518721  259.760    0.000  338.679    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               75561630  334.643    0.000  334.643    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               54997347  326.628    0.000  326.628    0.000 {built-in method numpy.array}
               15112326  294.998    0.000  294.998    0.000 {built-in method gather}
                2519720  207.192    0.000  274.549    0.000 agent.py:149(convert_values)
               25606847   24.497    0.000  271.282    0.000 <__array_function__ internals>:2(prod)
                   5246  240.434    0.046  266.889    0.051 {built-in method _pickle.loads}
               58350375  257.725    0.000  257.725    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              377808258  209.577    0.000  243.885    0.000 tensor.py:725(grad)
               25606887   18.287    0.000  242.633    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7871007   14.062    0.000  240.320    0.000 functional.py:68(split)
                7661111   23.965    0.000  238.872    0.000 pooling.py:156(forward)
                7556163  231.059    0.000  231.059    0.000 {built-in method torch._C._nn.mse_loss}
                7871007   14.224    0.000  225.246    0.000 tensor.py:367(split)
               25606847   30.906    0.000  224.346    0.000 fromnumeric.py:2881(prod)
               52473380  220.458    0.000  220.458    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               30644456  195.681    0.000  217.463    0.000 __init__.py:66(is_acceptable)
                2623669   28.176    0.000  215.603    0.000 environments.py:86(<listcomp>)
                7661111   13.074    0.000  214.907    0.000 _jit_internal.py:237(fn)
                2719066  211.579    0.000  211.579    0.000 {built-in method tensor}
                7871007  209.453    0.000  209.453    0.000 {function Tensor.split at 0x7fd7d469c9d0}
                2518721  208.606    0.000  208.606    0.000 memory.py:43(<listcomp>)
                7661111   16.140    0.000  200.662    0.000 functional.py:564(_max_pool2d)
               25606847   58.975    0.000  193.440    0.000 fromnumeric.py:70(_wrapreduction)
              270665171  190.420    0.000  190.532    0.000 module.py:758(__getattr__)
                7559160  187.827    0.000  187.827    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               52473400   34.571    0.000  187.469    0.000 environments.py:89(reset)
                7661111  183.503    0.000  183.503    0.000 {built-in method max_pool2d}
                2623669   18.494    0.000  168.183    0.000 collector.py:8(collect)
               15113325  166.849    0.000  166.849    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                7556163   37.412    0.000  155.409    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8557625: <BIGFISH_U_S_0_0.01returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0_0.01returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:46 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Dec 14 05:02:58 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec 14 05:02:58 2020
Terminated at Tue Dec 15 03:58:34 2020
Results reported at Tue Dec 15 03:58:34 2020

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

    CPU time :                                   87147.00 sec.
    Max Memory :                                 54188 MB
    Average Memory :                             53476.64 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7252.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82537 sec.
    Turnaround time :                            302208 sec.

The output (if any) is above this job summary.

