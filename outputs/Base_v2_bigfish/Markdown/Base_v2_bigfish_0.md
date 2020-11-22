[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_bigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     24
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      9405514548 function calls (9199660922 primitive calls) in 86135.97 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86135.965 86135.965 {built-in method builtins.exec}
                      1    0.043    0.043 86135.965 86135.965 <string>:1(<module>)
                      1  497.249  497.249 86135.921 86135.921 main.py:11(main)
                2708894   98.461    0.000 51446.185    0.019 agent.py:46(learn)
                2708394  335.330    0.000 50567.006    0.019 agent.py:54(TD_learn)
                2708394  190.612    0.000 29368.535    0.011 memory.py:27(sample_distribution)
                2708394  310.886    0.000 28490.291    0.011 helpers.py:12(stack)
              367515068 18601.685    0.000 18601.685    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2708894   40.950    0.000 18093.587    0.007 agent.py:41(chooseMulti)
        219389914/13542470  929.315    0.000 15010.571    0.001 module.py:710(_call_impl)
               24377100 14732.944    0.001 14732.981    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               10834076  229.739    0.000 14719.894    0.001 agent.py:119(forward)
                2708894  101.334    0.000 13813.760    0.005 agent.py:44(<listcomp>)
               54177880  155.278    0.000 13468.344    0.000 exploration.py:33(epsilonGreedy)
               24377046 13055.335    0.001 13055.335    0.001 {built-in method cat}
                2708894   74.934    0.000 9172.254    0.003 environments.py:73(step)
               32502228  237.533    0.000 8348.048    0.000 container.py:115(forward)
                2708894    7.795    0.000 6709.075    0.002 agent.py:32(rememberMulti)
                2708894  227.871    0.000 6701.280    0.002 agent.py:33(<listcomp>)
               54628404 1530.278    0.000 5878.222    0.000 helpers.py:8(clean)
                2708894   52.959    0.000 5874.629    0.002 environments.py:75(<listcomp>)
               62753586 5034.952    0.000 5034.952    0.000 {built-in method as_tensor}
               65004456  113.733    0.000 4999.525    0.000 conv.py:418(forward)
               65004456  129.514    0.000 4835.715    0.000 conv.py:410(_conv_forward)
               65004456 4683.273    0.000 4683.273    0.000 {built-in method conv2d}
                2708394   16.523    0.000 4154.378    0.002 grad_mode.py:12(decorate_context)
                2708394 1058.941    0.000 4118.028    0.002 adam.py:51(step)
                2708394   15.501    0.000 4105.994    0.002 tensor.py:155(backward)
                2708394   19.401    0.000 4090.493    0.002 __init__.py:57(backward)
                2708394 4002.456    0.001 4002.456    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2708894   55.442    0.000 2966.867    0.001 environments.py:74(<listcomp>)
               54177880  197.693    0.000 2911.425    0.000 interop.py:274(step)
               10834082  511.896    0.000 2900.149    0.000 rnn.py:109(flatten_parameters)
               10834076  117.505    0.000 2685.942    0.000 rnn.py:550(forward)
               10834076 2427.058    0.000 2427.058    0.000 {built-in method lstm}
               10834079 1781.089    0.000 1781.089    0.000 {built-in method _cudnn_rnn_flatten_weight}
               54177880   28.623    0.000 1250.808    0.000 wrapper.py:25(act)
               75838532   69.795    0.000 1237.676    0.000 activation.py:653(forward)
               54177880   65.416    0.000 1222.186    0.000 env.py:197(act)
               75838532  110.606    0.000 1167.881    0.000 functional.py:1277(leaky_relu)
               54177880 1116.587    0.000 1121.827    0.000 libenv.py:352(act)
               75838532 1046.683    0.000 1046.683    0.000 {built-in method torch._C._nn.leaky_relu}
              108806284   82.471    0.000  901.350    0.000 extract_dict_ob.py:9(observe)
              108806284   48.288    0.000  818.878    0.000 wrapper.py:19(observe)
                   5417    1.321    0.000  780.719    0.144 agent.py:81(update_target_network)
              108806284  206.097    0.000  770.590    0.000 libenv.py:344(observe)
               97502184  763.295    0.000  763.295    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   5417  199.271    0.037  715.540    0.132 memory.py:37(update_distribution)
               10834076   28.407    0.000  680.244    0.000 linear.py:90(forward)
               97502184  671.063    0.000  671.063    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10834076   58.760    0.000  640.333    0.000 functional.py:1655(linear)
               56897108  602.391    0.000  602.391    0.000 {built-in method numpy.array}
              162984164  175.356    0.000  563.121    0.000 libenv.py:281(_maybe_copy_dict)
               43337284  524.184    0.000  555.291    0.000 module.py:774(__setattr__)
              488957909  478.391    0.000  478.391    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48751092  462.360    0.000  462.360    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10834076  425.413    0.000  425.413    0.000 {built-in method addmm}
               54177880   45.728    0.000  409.420    0.000 wrapper.py:22(get_info)
              380156030  395.612    0.000  395.612    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               48751092  389.907    0.000  389.907    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11730092  148.175    0.000  383.536    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2708394   67.121    0.000  383.471    0.000 optimizer.py:166(zero_grad)
               54177880  374.510    0.000  374.510    0.000 memory.py:15(inner)
                2708394  288.681    0.000  373.966    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               54177880  187.976    0.000  363.692    0.000 libenv.py:363(get_info)
               10834076   28.383    0.000  331.012    0.000 pooling.py:156(forward)
               48751092  322.004    0.000  322.004    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48751092  305.468    0.000  305.468    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10834076   18.288    0.000  302.630    0.000 _jit_internal.py:237(fn)
               10834076   19.916    0.000  282.609    0.000 functional.py:564(_max_pool2d)
               26168718   24.952    0.000  282.031    0.000 <__array_function__ internals>:2(prod)
                8126682   14.290    0.000  266.711    0.000 functional.py:68(split)
               43336316  232.813    0.000  263.796    0.000 __init__.py:66(is_acceptable)
               10834076  261.292    0.000  261.292    0.000 {built-in method max_pool2d}
                2708894   31.789    0.000  255.825    0.000 environments.py:76(<listcomp>)
               26168758   19.285    0.000  252.945    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                8126682   14.425    0.000  251.329    0.000 tensor.py:367(split)
               54177880  244.082    0.000  244.082    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8126682  235.487    0.000  235.487    0.000 {function Tensor.split at 0x7efbc805a940}
               26168718   31.212    0.000  233.660    0.000 fromnumeric.py:2881(prod)
               54177900   33.225    0.000  224.074    0.000 environments.py:79(reset)
               48751092  214.610    0.000  214.610    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2708394  213.704    0.000  213.704    0.000 memory.py:35(<listcomp>)
               26168718   59.668    0.000  202.448    0.000 fromnumeric.py:70(_wrapreduction)
                2708894   18.036    0.000  176.314    0.000 collector.py:7(collect)
                2708394    6.931    0.000  176.133    0.000 loss.py:444(forward)
                2708394   25.869    0.000  169.201    0.000 functional.py:2621(mse_loss)
              243755514  142.803    0.000  166.283    0.000 tensor.py:725(grad)
               27084940  162.111    0.000  162.111    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              217612568   57.502    0.000  160.315    0.000 libenv.py:271(_maybe_copy_ndarray)
                5417789  157.103    0.000  157.103    0.000 {built-in method builtins.sum}
              206064473  155.299    0.000  155.428    0.000 module.py:758(__getattr__)
               28882529  152.230    0.000  152.230    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              219389914  132.387    0.000  132.387    0.000 {built-in method torch._C._get_tracing_state}
                5416788  128.870    0.000  128.870    0.000 {built-in method gather}
                2708394   94.853    0.000   94.853    0.000 {built-in method torch._C._nn.mse_loss}
               10834076   30.108    0.000   92.895    0.000 rnn.py:524(check_forward_args)
               10834076   90.119    0.000   90.119    0.000 {method 't' of 'torch._C._TensorBase' objects}
               54628444   43.270    0.000   85.967    0.000 types.py:163(multimap)
              910061884   84.381    0.000   84.381    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8410443: <Base_v2_bigfish_0> in cluster <dcc> Done

Job <Base_v2_bigfish_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Sat Nov 21 14:15:16 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov 21 14:28:53 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 21 14:28:53 2020
Terminated at Sun Nov 22 14:24:51 2020
Results reported at Sun Nov 22 14:24:51 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=80G]"
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

    CPU time :                                   93089.00 sec.
    Max Memory :                                 56729 MB
    Average Memory :                             55958.45 MB
    Total Requested Memory :                     81920.00 MB
    Delta Memory :                               25191.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86158 sec.
    Turnaround time :                            86975 sec.

The output (if any) is above this job summary.

