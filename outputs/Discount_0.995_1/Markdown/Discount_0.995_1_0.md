[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
Discount_0.995_1-0 0.995 fruitbot 20.0 200000 100
    Play for :                  1 games.
    Minutes used :              1198 minutes.
    Hours used :                19 hours.

# Profiling


      2210158368 function calls (2151870294 primitive calls) in 71916.55 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 71916.551 71916.551 {built-in method builtins.exec}
                      1    0.020    0.020 71916.551 71916.551 <string>:1(<module>)
                      1  121.545  121.545 71916.530 71916.530 main.py:16(main)
                1028475  155.393    0.000 67810.264    0.066 agent.py:45(learn)
                1028475   83.873    0.000 21741.141    0.021 memory.py:27(sample_distribution)
                1028475  105.730    0.000 21269.482    0.021 helpers.py:12(stack)
        62738775/4456825  381.539    0.000 17808.889    0.004 module.py:710(_call_impl)
                3428350   98.477    0.000 17669.782    0.005 agent.py:94(forward)
                7199673 16391.050    0.002 16391.079    0.002 {method 'to' of 'torch._C._TensorBase' objects}
               10285050   98.435    0.000 15107.275    0.001 container.py:115(forward)
                1028475    7.609    0.000 13584.511    0.013 tensor.py:155(backward)
                1028475    9.138    0.000 13576.902    0.013 __init__.py:57(backward)
                1028475 13531.746    0.013 13531.746    0.013 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1028475    3.316    0.000 12184.863    0.012 memory.py:75(empty_cache)
                1028475 12180.250    0.012 12180.250    0.012 {built-in method torch._C._cuda_emptyCache}
               20570100   28.913    0.000 8637.516    0.000 activation.py:653(forward)
               20570100   42.510    0.000 8608.603    0.000 functional.py:1277(leaky_relu)
               20570100 8561.810    0.000 8561.810    0.000 {built-in method torch._C._nn.leaky_relu}
               17141750   43.461    0.000 5591.599    0.000 conv.py:418(forward)
               17141750   48.065    0.000 5529.977    0.000 conv.py:410(_conv_forward)
               17141750 5472.946    0.000 5472.946    0.000 {built-in method conv2d}
                7199625 4511.566    0.001 4511.566    0.001 {built-in method cat}
                1028475    9.017    0.000 2322.359    0.002 grad_mode.py:12(decorate_context)
                1028475  581.092    0.001 2301.914    0.002 adam.py:51(step)
                 342925    6.945    0.000 1569.943    0.005 agent.py:40(chooseMulti)
                 342925   10.220    0.000 1296.898    0.004 environments.py:73(step)
                3428356  211.904    0.000 1189.182    0.000 rnn.py:109(flatten_parameters)
                3428350   53.145    0.000 1036.433    0.000 rnn.py:550(forward)
               47440565  925.448    0.000  925.448    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3428350  917.824    0.000  917.824    0.000 {built-in method lstm}
                 342925   18.855    0.000  911.155    0.003 agent.py:43(<listcomp>)
                 342925    1.016    0.000  894.390    0.003 agent.py:32(rememberMulti)
                 342925   31.714    0.000  893.375    0.003 agent.py:33(<listcomp>)
                6858500  327.027    0.000  844.296    0.000 exploration.py:28(epsilonGreedy)
                9992751  835.920    0.000  835.920    0.000 {built-in method as_tensor}
                3428353  741.946    0.000  741.946    0.000 {built-in method _cudnn_rnn_flatten_weight}
                 342925    6.658    0.000  727.881    0.002 environments.py:75(<listcomp>)
                6907326  204.256    0.000  726.854    0.000 helpers.py:8(clean)
                 342925    8.508    0.000  529.629    0.002 environments.py:74(<listcomp>)
                6858500   29.640    0.000  521.121    0.000 interop.py:274(step)
               32911200  421.969    0.000  421.969    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               32911200  385.213    0.000  385.213    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3428350   12.924    0.000  291.002    0.000 linear.py:90(forward)
                6858500    4.106    0.000  284.343    0.000 wrapper.py:25(act)
                6858500   10.443    0.000  280.237    0.000 env.py:197(act)
                3428350   27.597    0.000  272.816    0.000 functional.py:1655(linear)
                6858500  263.902    0.000  264.670    0.000 libenv.py:352(act)
               16455600  260.856    0.000  260.856    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               13714275  206.143    0.000  219.747    0.000 module.py:774(__setattr__)
               16455600  215.352    0.000  215.352    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1028475  159.134    0.000  209.185    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                1028475   36.094    0.000  206.531    0.000 optimizer.py:166(zero_grad)
                   3429    0.773    0.000  184.922    0.054 agent.py:63(update_target_network)
               16455600  183.681    0.000  183.681    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3428350  178.675    0.000  178.675    0.000 {built-in method addmm}
               16455600  173.811    0.000  173.811    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   3429   42.787    0.012  151.176    0.044 memory.py:37(update_distribution)
                6858500  141.579    0.000  141.579    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                6858500  136.416    0.000  136.416    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                3428350   10.744    0.000  136.134    0.000 pooling.py:156(forward)
               13765826   11.947    0.000  127.150    0.000 extract_dict_ob.py:9(observe)
                3428350    7.988    0.000  125.389    0.000 _jit_internal.py:237(fn)
                7893233  122.356    0.000  122.356    0.000 {built-in method numpy.array}
                3428350    7.910    0.000  116.596    0.000 functional.py:564(_max_pool2d)
               13765826    7.273    0.000  115.203    0.000 wrapper.py:19(observe)
               16455600  115.172    0.000  115.172    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3428350  108.104    0.000  108.104    0.000 {built-in method max_pool2d}
               13765826   28.884    0.000  107.930    0.000 libenv.py:344(observe)
               13713412   81.897    0.000   94.148    0.000 __init__.py:66(is_acceptable)
               82278048   78.222    0.000   91.664    0.000 tensor.py:725(grad)
                1028475    2.828    0.000   90.038    0.000 loss.py:444(forward)
                1028475   12.645    0.000   87.210    0.000 functional.py:2621(mse_loss)
                1027875   81.214    0.000   81.214    0.000 memory.py:35(<listcomp>)
               20624326   23.746    0.000   78.261    0.000 libenv.py:281(_maybe_copy_dict)
                8913650   71.846    0.000   71.846    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               52485328   70.919    0.000   70.919    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               61876407   67.207    0.000   67.207    0.000 {method 'copy' of 'numpy.ndarray' objects}
                2056950   67.044    0.000   67.044    0.000 {built-in method gather}
               58405713   62.721    0.000   62.811    0.000 module.py:758(__getattr__)
                6858500    6.564    0.000   56.625    0.000 wrapper.py:22(get_info)
               62738775   56.108    0.000   56.108    0.000 {built-in method torch._C._get_tracing_state}
                2166485    4.944    0.000   51.745    0.000 <__array_function__ internals>:2(prod)
                1027876   51.383    0.000   51.383    0.000 {built-in method numpy.arange}
                6858500   25.941    0.000   50.061    0.000 libenv.py:363(get_info)
                1028475   48.711    0.000   48.711    0.000 {built-in method torch._C._nn.mse_loss}
                1028775    2.268    0.000   48.357    0.000 functional.py:68(split)
                6858500   48.003    0.000   48.003    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                3197789   47.463    0.000   47.463    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                2166525    3.900    0.000   46.047    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                1028775    2.320    0.000   45.910    0.000 tensor.py:367(split)
                1028775   43.337    0.000   43.337    0.000 {function Tensor.split at 0x7f10ddad6790}
                2166485    6.898    0.000   42.147    0.000 fromnumeric.py:2881(prod)
                3428350   13.307    0.000   41.110    0.000 rnn.py:524(check_forward_args)
              261240150   39.509    0.000   39.509    0.000 {method 'values' of 'collections.OrderedDict' objects}
                6858500   38.848    0.000   38.848    0.000 memory.py:15(inner)
                3428350   38.045    0.000   38.045    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 568935   15.835    0.000   37.972    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                1028475    9.035    0.000   35.516    0.000 __init__.py:25(_make_grads)
                2166485   11.135    0.000   35.249    0.000 fromnumeric.py:70(_wrapreduction)
        162323106/162322106   33.405    0.000   33.416    0.000 {built-in method builtins.len}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8273880: <Discount_0.995_1_0> in cluster <dcc> Done

Job <Discount_0.995_1_0> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Sat Nov  7 15:36:09 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov  7 16:23:40 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov  7 16:23:40 2020
Terminated at Sun Nov  8 12:22:23 2020
Results reported at Sun Nov  8 12:22:23 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=30G]"
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

    CPU time :                                   31011.00 sec.
    Max Memory :                                 24917 MB
    Average Memory :                             24413.38 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5803.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   71922 sec.
    Turnaround time :                            74774 sec.

The output (if any) is above this job summary.

