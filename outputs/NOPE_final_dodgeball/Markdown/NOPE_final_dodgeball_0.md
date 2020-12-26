[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NOPE_final_dodgeball-0
    Discount :                  0.995
    Environment :               dodgeball
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


      7504793640 function calls (7347934314 primitive calls) in 64521.93 seconds

##    Ordered by: cumulative time
   List reduced from 1329 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 64521.931 64521.931 {built-in method builtins.exec}
                      1    0.026    0.026 64521.931 64521.931 <string>:1(<module>)
                      1  443.645  443.645 64521.904 64521.904 main.py:91(main)
                2066239  174.739    0.000 41440.380    0.020 agent.py:93(learn)
                1983280  356.512    0.000 40721.246    0.021 agent.py:106(TD_learn)
                1983280  149.998    0.000 24030.850    0.012 memory.py:35(sample_distribution)
                1983280  276.653    0.000 23317.796    0.012 helpers.py:15(stack)
               18098505 11380.144    0.001 11380.154    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               18098397 11316.459    0.001 11316.459    0.001 {built-in method cat}
        166852133/9999359  769.174    0.000 10593.386    0.001 module.py:710(_call_impl)
                6032799  159.713    0.000 10216.288    0.002 agent.py:235(forward)
                2066239   47.305    0.000 9446.069    0.005 agent.py:72(chooseMulti)
              268468659 9065.499    0.000 9065.499    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2066239   62.596    0.000 7662.981    0.004 environments.py:83(step)
               24131196  186.321    0.000 6200.354    0.000 container.py:115(forward)
                1984270    9.551    0.000 5348.723    0.003 agent.py:58(rememberMulti)
                1984270  179.805    0.000 5339.171    0.003 agent.py:63(<listcomp>)
                1984279   74.617    0.000 5162.736    0.003 agent.py:88(<listcomp>)
               39685580  103.675    0.000 4901.800    0.000 exploration.py:34(epsilonGreedy)
                2066239   52.446    0.000 4599.412    0.002 environments.py:85(<listcomp>)
               41636505 1262.995    0.000 4587.125    0.000 helpers.py:8(clean)
                3966560   23.822    0.000 4227.916    0.001 grad_mode.py:12(decorate_context)
                3966560 1068.237    0.000 4174.490    0.001 adam.py:51(step)
               47586345 3910.501    0.000 3910.501    0.000 {built-in method as_tensor}
                3966560   20.084    0.000 3859.060    0.001 tensor.py:155(backward)
                3966560   23.935    0.000 3838.976    0.001 __init__.py:57(backward)
                3966560 3719.810    0.001 3719.810    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               36196794   68.481    0.000 2925.888    0.000 conv.py:418(forward)
               36196794   80.863    0.000 2826.414    0.000 conv.py:410(_conv_forward)
                2066239   44.674    0.000 2793.918    0.001 environments.py:84(<listcomp>)
               41324780  164.685    0.000 2749.244    0.000 interop.py:274(step)
               36196794 2731.168    0.000 2731.168    0.000 {built-in method conv2d}
                6032805  331.693    0.000 1772.858    0.000 rnn.py:109(flatten_parameters)
                6032799   80.351    0.000 1665.100    0.000 rnn.py:550(forward)
                6032799 1494.320    0.000 1494.320    0.000 {built-in method lstm}
               41324780   20.777    0.000 1387.365    0.000 wrapper.py:25(act)
               41324780   53.018    0.000 1366.588    0.000 env.py:197(act)
               41324780 1280.206    0.000 1284.276    0.000 libenv.py:352(act)
               24131196   53.642    0.000 1196.429    0.000 linear.py:90(forward)
               24131196   97.025    0.000 1114.746    0.000 functional.py:1655(linear)
                6032802 1035.916    0.000 1035.916    0.000 {built-in method _cudnn_rnn_flatten_weight}
               60327990   63.737    0.000  984.663    0.000 activation.py:653(forward)
               60327990   87.511    0.000  920.926    0.000 functional.py:1277(leaky_relu)
               60327990  824.971    0.000  824.971    0.000 {built-in method torch._C._nn.leaky_relu}
               95197440  773.539    0.000  773.539    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24131196  749.024    0.000  749.024    0.000 {built-in method addmm}
               82961285   66.418    0.000  735.892    0.000 extract_dict_ob.py:9(observe)
               95197440  680.881    0.000  680.881    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               82961285   38.074    0.000  669.475    0.000 wrapper.py:19(observe)
               82961285  164.981    0.000  631.400    0.000 libenv.py:344(observe)
                   2025    0.945    0.000  544.395    0.269 agent.py:161(update_target_network)
               47598720  474.790    0.000  474.790    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              124286065  141.222    0.000  465.732    0.000 libenv.py:281(_maybe_copy_dict)
               47598720  398.835    0.000  398.835    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              372860220  395.897    0.000  395.897    0.000 {method 'copy' of 'numpy.ndarray' objects}
                3966560   72.530    0.000  395.670    0.000 optimizer.py:166(zero_grad)
               11008287  137.478    0.000  357.303    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               28099591  320.674    0.000  343.574    0.000 module.py:774(__setattr__)
              297072567  341.999    0.000  341.999    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               41324780   36.992    0.000  329.023    0.000 wrapper.py:22(get_info)
               47598720  323.661    0.000  323.661    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47598720  310.306    0.000  310.306    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               43312110  302.001    0.000  302.001    0.000 {built-in method numpy.array}
                1983280  229.435    0.000  297.886    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   2025   74.983    0.037  296.637    0.146 memory.py:45(update_distribution)
               41324780  151.152    0.000  292.030    0.000 libenv.py:363(get_info)
               39685400  288.991    0.000  288.991    0.000 memory.py:17(inner)
                3966560    9.871    0.000  260.204    0.000 loss.py:444(forward)
               23999994   23.194    0.000  259.067    0.000 <__array_function__ internals>:2(prod)
                3966560   37.386    0.000  250.333    0.000 functional.py:2621(mse_loss)
               24000034   17.551    0.000  232.045    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                   4050  203.932    0.050  225.843    0.056 {built-in method _pickle.loads}
               47598720  223.059    0.000  223.059    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               23999994   29.096    0.000  214.494    0.000 fromnumeric.py:2881(prod)
                6198717   11.366    0.000  211.252    0.000 functional.py:68(split)
                2066239   23.689    0.000  207.055    0.000 environments.py:86(<listcomp>)
                6032799   16.788    0.000  200.166    0.000 pooling.py:156(forward)
                6198717   11.534    0.000  199.019    0.000 tensor.py:367(split)
               41324780  193.129    0.000  193.129    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1984279  145.183    0.000  190.136    0.000 agent.py:152(convert_values)
                6198717  186.164    0.000  186.164    0.000 {function Tensor.split at 0x7fae93ec29d0}
               23999994   54.476    0.000  185.398    0.000 fromnumeric.py:70(_wrapreduction)
               41324800   31.114    0.000  183.381    0.000 environments.py:89(reset)
                6032799   11.629    0.000  183.378    0.000 _jit_internal.py:237(fn)
               24131208  162.727    0.000  182.904    0.000 __init__.py:66(is_acceptable)
                1983280  174.976    0.000  174.976    0.000 memory.py:43(<listcomp>)
                6032799   13.694    0.000  170.689    0.000 functional.py:564(_max_pool2d)
                7933120  167.665    0.000  167.665    0.000 {built-in method gather}
              237993708  139.787    0.000  163.188    0.000 tensor.py:725(grad)
               24131196  162.114    0.000  162.114    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6032799  156.150    0.000  156.150    0.000 {built-in method max_pool2d}
                2066239   16.990    0.000  153.536    0.000 collector.py:8(collect)
               28014797  142.568    0.000  142.568    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                3966560  138.372    0.000  138.372    0.000 {built-in method torch._C._nn.mse_loss}
                4132479  135.408    0.000  135.408    0.000 {built-in method builtins.sum}
               25985299  134.517    0.000  134.517    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              165922570   46.165    0.000  128.468    0.000 libenv.py:271(_maybe_copy_ndarray)
              157015401  126.193    0.000  126.284    0.000 module.py:758(__getattr__)
              166852133  102.938    0.000  102.938    0.000 {built-in method torch._C._get_tracing_state}
                3966560   23.474    0.000   93.819    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8587063: <NOPE_final_dodgeball_0> in cluster <dcc> Done

Job <NOPE_final_dodgeball_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Thu Dec 24 13:34:59 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Dec 25 23:28:42 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec 25 23:28:42 2020
Terminated at Sat Dec 26 17:24:13 2020
Results reported at Sat Dec 26 17:24:13 2020

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

    CPU time :                                   68301.00 sec.
    Max Memory :                                 55749 MB
    Average Memory :                             55038.39 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5691.00 MB
    Max Swap :                                   2 MB
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64540 sec.
    Turnaround time :                            186554 sec.

The output (if any) is above this job summary.

