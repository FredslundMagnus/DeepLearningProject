[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NOPEchaser-0
    Discount :                  0.99
    Environment :               chaser
    Hours :                     12
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
    State difference weight :   0.1
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      7542967543 function calls (7327755594 primitive calls) in 42922.09 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 42922.090 42922.090 {built-in method builtins.exec}
                      1    0.011    0.011 42922.090 42922.090 <string>:1(<module>)
                      1  171.526  171.526 42922.076 42922.076 main.py:92(main)
                1505207  114.147    0.000 17950.243    0.012 agent.py:89(learn)
                1444237  424.375    0.000 17480.922    0.012 agent.py:102(TD_learn)
        257224128/42018799 1149.328    0.000 15317.401    0.000 module.py:710(_call_impl)
                1505207   38.499    0.000 15289.887    0.010 environments.py:83(step)
               30342964 1558.251    0.000 13290.741    0.000 helpers.py:8(clean)
                1505207   42.265    0.000 13227.015    0.009 environments.py:85(<listcomp>)
               46473450  341.664    0.000 12146.304    0.000 container.py:115(forward)
               73866971  167.545    0.000 7158.140    0.000 conv.py:418(forward)
               73866971  152.330    0.000 6918.050    0.000 conv.py:410(_conv_forward)
               73866971 6737.084    0.000 6737.084    0.000 {built-in method conv2d}
                4393681   96.659    0.000 5699.442    0.001 agent.py:231(forward)
                1445227    7.581    0.000 4875.840    0.003 agent.py:58(rememberMulti)
                1445227  301.223    0.000 4853.006    0.003 agent.py:60(<listcomp>)
                1505207  164.253    0.000 4504.426    0.003 agent.py:72(chooseMulti)
                1444237   76.577    0.000 4500.062    0.003 memory.py:35(sample_distribution)
                4332711   23.449    0.000 4322.331    0.001 grad_mode.py:12(decorate_context)
                4332711 1005.783    0.000 4270.246    0.001 adam.py:51(step)
              254327242 4255.920    0.000 4255.920    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1444237  148.355    0.000 4120.856    0.003 helpers.py:15(stack)
               34675675 3369.474    0.000 3369.474    0.000 {built-in method as_tensor}
                4332711   16.859    0.000 2869.395    0.001 tensor.py:155(backward)
                4332711   17.346    0.000 2852.536    0.001 __init__.py:57(backward)
                4332711 2736.866    0.001 2736.866    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               16069517 2495.431    0.000 2495.431    0.000 {built-in method cat}
               97340581   94.163    0.000 2001.189    0.000 activation.py:653(forward)
               97340581  147.869    0.000 1907.026    0.000 functional.py:1277(leaky_relu)
                1505207   28.911    0.000 1801.131    0.001 environments.py:84(<listcomp>)
               30104140  116.409    0.000 1772.220    0.000 interop.py:274(step)
               97340581 1745.117    0.000 1745.117    0.000 {built-in method torch._C._nn.leaky_relu}
               26423053   57.659    0.000 1477.895    0.000 linear.py:90(forward)
               17574834 1400.668    0.000 1400.734    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               26423053  178.037    0.000 1397.837    0.000 functional.py:1655(linear)
                4393687  191.213    0.000 1262.611    0.000 rnn.py:109(flatten_parameters)
                1505207   67.587    0.000 1150.461    0.001 agent.py:87(<listcomp>)
                4393681   41.739    0.000  941.413    0.000 rnn.py:550(forward)
               30104140   14.403    0.000  901.701    0.000 wrapper.py:25(act)
               30104140   98.139    0.000  892.355    0.000 exploration.py:34(epsilonGreedy)
               30104140   47.107    0.000  887.298    0.000 env.py:197(act)
                4393684  876.340    0.000  876.340    0.000 {built-in method _cudnn_rnn_flatten_weight}
                4393681  848.598    0.000  848.598    0.000 {built-in method lstm}
               69323376  833.753    0.000  833.753    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               30104140  810.430    0.000  813.294    0.000 libenv.py:352(act)
                2949443   10.852    0.000  798.278    0.000 agent.py:247(avoid_similar_state)
               21907435  768.854    0.000  768.854    0.000 {built-in method addmm}
               69323376  766.919    0.000  766.919    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              312770974  527.653    0.000  527.653    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               34661688  482.715    0.000  482.715    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               60447104   50.241    0.000  435.744    0.000 extract_dict_ob.py:9(observe)
                4332711   66.349    0.000  430.574    0.000 optimizer.py:166(zero_grad)
               34661688  392.740    0.000  392.740    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               60447104   21.864    0.000  385.503    0.000 wrapper.py:19(observe)
               60447104   91.084    0.000  363.639    0.000 libenv.py:344(observe)
                   1475    0.514    0.000  355.174    0.241 agent.py:157(update_target_network)
               34661688  341.621    0.000  341.621    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               34661688  337.288    0.000  337.288    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               34661688  268.160    0.000  268.160    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4332711    5.954    0.000  255.081    0.000 loss.py:444(forward)
               90551244   81.773    0.000  252.741    0.000 libenv.py:281(_maybe_copy_dict)
                4332711   26.500    0.000  249.127    0.000 functional.py:2621(mse_loss)
                7056664   87.368    0.000  231.416    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               28904540  227.862    0.000  227.862    0.000 memory.py:17(inner)
              271655207  225.194    0.000  225.194    0.000 {method 'copy' of 'numpy.ndarray' objects}
                1505207   16.021    0.000  223.242    0.000 environments.py:86(<listcomp>)
               57809080  222.946    0.000  222.946    0.000 tensor.py:456(<lambda>)
              260114582  222.770    0.000  222.770    0.000 {built-in method torch._C._get_tracing_state}
               30104140   25.330    0.000  216.229    0.000 wrapper.py:22(get_info)
               30104160   18.167    0.000  207.318    0.000 environments.py:89(reset)
               26423053  199.959    0.000  199.959    0.000 {method 't' of 'torch._C._TensorBase' objects}
               30104140  105.345    0.000  190.899    0.000 libenv.py:363(get_info)
               30104140  190.518    0.000  190.518    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               31551327  178.814    0.000  178.814    0.000 {built-in method numpy.array}
                   1475   48.999    0.033  170.819    0.116 memory.py:45(update_distribution)
                1445236  168.332    0.000  170.326    0.000 agent.py:148(convert_values)
                7221185  169.786    0.000  169.786    0.000 {built-in method gather}
                   2950  152.703    0.052  169.093    0.057 {built-in method _pickle.loads}
               15557705   13.931    0.000  166.139    0.000 <__array_function__ internals>:2(prod)
                1444237  126.432    0.000  162.799    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               26179176  157.741    0.000  157.741    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              225616529  154.005    0.000  154.070    0.000 module.py:758(__getattr__)
                4332711  151.953    0.000  151.953    0.000 {built-in method torch._C._nn.mse_loss}
               15557745   11.325    0.000  149.637    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                4515618  147.389    0.000  147.389    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                4515621    6.636    0.000  141.515    0.000 functional.py:68(split)
               15557705   17.194    0.000  138.311    0.000 fromnumeric.py:2881(prod)
                4515621    7.628    0.000  134.249    0.000 tensor.py:367(split)
              173308552  115.946    0.000  134.005    0.000 tensor.py:725(grad)
               20465033  113.053    0.000  126.302    0.000 module.py:774(__setattr__)
                4515621  125.521    0.000  125.521    0.000 {function Tensor.split at 0x7efbcf0579d0}
               15557705   34.319    0.000  121.117    0.000 fromnumeric.py:70(_wrapreduction)
             1075369962  114.386    0.000  114.386    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1505207    8.642    0.000  106.072    0.000 collector.py:8(collect)
                7282154  103.115    0.000  103.115    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                1444237  101.485    0.000  101.485    0.000 memory.py:43(<listcomp>)
                3010415   96.944    0.000   96.945    0.000 {built-in method builtins.sum}
                4332711   18.263    0.000   96.702    0.000 __init__.py:25(_make_grads)
              120894208   32.369    0.000   94.655    0.000 libenv.py:271(_maybe_copy_ndarray)
                1617316   88.457    0.000   88.457    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 8582544: <NOPEchaser_0> in cluster <dcc> Done

Job <NOPEchaser_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Tue Dec 22 15:39:59 2020
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Dec 23 03:36:09 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 23 03:36:09 2020
Terminated at Wed Dec 23 15:31:38 2020
Results reported at Wed Dec 23 15:31:38 2020

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

    CPU time :                                   43666.00 sec.
    Max Memory :                                 10182 MB
    Average Memory :                             10078.76 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               51258.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   42931 sec.
    Turnaround time :                            85899 sec.

The output (if any) is above this job summary.

