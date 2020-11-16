[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
    Name :                      Test_1-0
    Discount :                  0.995
    Environment :               fruitbot
    Hours :                     1.0
    Memory :                    200000
    Update every :              100
    Use distribution :          0.0
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              55 minutes.
    Hours used :                0 hours.

# Profiling


      407332524 function calls (400201314 primitive calls) in 3344.25 seconds

##    Ordered by: cumulative time
   List reduced from 1307 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 3344.245 3344.245 {built-in method builtins.exec}
                      1    0.005    0.005 3344.245 3344.245 <string>:1(<module>)
                      1    6.852    6.852 3344.239 3344.239 main.py:11(main)
                  50984    8.960    0.000 2836.459    0.056 agent.py:46(learn)
                 152652   22.156    0.000 2802.719    0.018 agent.py:54(TD_learn)
                 152652  519.806    0.003 2035.420    0.013 memory.py:23(sample)
                 152652   19.679    0.000 1472.516    0.010 helpers.py:12(stack)
                1068864  722.222    0.001  722.222    0.001 {built-in method cat}
                1068906  718.384    0.001  718.448    0.001 {method 'to' of 'torch._C._TensorBase' objects}
         7786752/661592   34.638    0.000  473.886    0.001 module.py:710(_call_impl)
                 508940    6.382    0.000  457.192    0.001 agent.py:111(forward)
                1526820    8.623    0.000  302.886    0.000 container.py:115(forward)
                  50984    1.498    0.000  184.775    0.004 environments.py:73(step)
                2035760    3.512    0.000  173.983    0.000 conv.py:418(forward)
                6635163  169.223    0.000  169.223    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2035760    4.682    0.000  168.845    0.000 conv.py:410(_conv_forward)
                2035760  163.390    0.000  163.390    0.000 {built-in method conv2d}
                 152652    0.983    0.000  140.363    0.001 grad_mode.py:12(decorate_context)
                  50984    0.899    0.000  138.238    0.003 agent.py:41(chooseMulti)
                 152652   35.617    0.000  138.226    0.001 adam.py:51(step)
                 152652    1.023    0.000  137.499    0.001 tensor.py:155(backward)
                 152652    1.141    0.000  136.476    0.001 __init__.py:57(backward)
                 508946   25.548    0.000  134.599    0.000 rnn.py:109(flatten_parameters)
                 152652  131.389    0.001  131.389    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  50984    0.153    0.000  130.288    0.003 agent.py:32(rememberMulti)
                  50984    4.620    0.000  130.135    0.003 agent.py:33(<listcomp>)
                1490007  112.433    0.000  112.433    0.000 {built-in method as_tensor}
                1032051   29.010    0.000  104.241    0.000 helpers.py:8(clean)
                  50984    1.040    0.000  103.875    0.002 environments.py:75(<listcomp>)
                 508943   80.934    0.000   80.934    0.000 {built-in method _cudnn_rnn_flatten_weight}
                  50984    2.064    0.000   79.311    0.002 agent.py:44(<listcomp>)
                  50984    1.111    0.000   73.961    0.001 environments.py:74(<listcomp>)
                1019680    3.939    0.000   72.850    0.000 interop.py:274(step)
                1019680    2.617    0.000   72.763    0.000 exploration.py:31(epsilonGreedy)
                 152652   18.621    0.000   42.232    0.000 random.py:315(sample)
                1019680    0.502    0.000   40.412    0.000 wrapper.py:25(act)
                2544700    2.558    0.000   40.092    0.000 activation.py:653(forward)
                1019680    1.299    0.000   39.909    0.000 env.py:197(act)
                1019680   37.788    0.000   37.886    0.000 libenv.py:352(act)
                2544700    3.755    0.000   37.534    0.000 functional.py:1277(leaky_relu)
                2544700   33.423    0.000   33.423    0.000 {built-in method torch._C._nn.leaky_relu}
                 508940    1.325    0.000   32.102    0.000 linear.py:90(forward)
                 508940    3.030    0.000   30.192    0.000 functional.py:1655(linear)
                3053040   25.024    0.000   25.024    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                    509    0.082    0.000   24.780    0.049 agent.py:81(update_target_network)
                      1    0.000    0.000   21.972   21.972 environments.py:69(__init__)
                      1    0.000    0.000   21.949   21.949 environments.py:70(<listcomp>)
                     20    0.000    0.000   21.949    1.097 environments.py:63(create)
                     20    0.000    0.000   21.949    1.097 registration.py:144(make)
                     20    0.000    0.000   21.949    1.097 registration.py:84(make)
                3053040   21.679    0.000   21.679    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000   21.153   21.153 agent.py:17(__init__)
                      3    0.000    0.000   21.083    7.028 module.py:524(to)
                   48/3    0.001    0.000   21.083    7.028 module.py:352(_apply)
                     42    0.000    0.000   20.925    0.498 module.py:602(convert)
                     20    0.000    0.000   20.670    1.034 registration.py:50(make)
                     20    0.000    0.000   20.668    1.033 gym_registration.py:6(make_env)
                     20    0.000    0.000   20.663    1.033 env.py:207(__init__)
                     20    0.000    0.000   20.663    1.033 env.py:71(__init__)
                     20   19.751    0.988   20.567    1.028 libenv.py:64(__init__)
                 508940   19.963    0.000   19.963    0.000 {built-in method addmm}
                    509    5.379    0.011   19.545    0.038 memory.py:37(update_distribution)
               30556417   11.971    0.000   18.424    0.000 random.py:250(_randbelow_with_getrandbits)
                2051731    1.540    0.000   17.804    0.000 extract_dict_ob.py:9(observe)
                2051731    0.966    0.000   16.264    0.000 wrapper.py:19(observe)
                1526520   15.787    0.000   15.787    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 508940    1.336    0.000   15.757    0.000 pooling.py:156(forward)
                1020698   15.683    0.000   15.683    0.000 {built-in method numpy.array}
                2051731    4.015    0.000   15.298    0.000 libenv.py:344(observe)
                 508940    0.902    0.000   14.421    0.000 _jit_internal.py:237(fn)
                 502597    5.347    0.000   14.375    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 152652    2.600    0.000   13.447    0.000 optimizer.py:166(zero_grad)
                 508940    0.983    0.000   13.439    0.000 functional.py:564(_max_pool2d)
                1526520   13.422    0.000   13.422    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 508940   12.387    0.000   12.387    0.000 {built-in method max_pool2d}
                3071411    3.344    0.000   11.315    0.000 libenv.py:281(_maybe_copy_dict)
                2035772    9.448    0.000   10.860    0.000 __init__.py:66(is_acceptable)
                1526520   10.829    0.000   10.829    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 152652    0.388    0.000   10.778    0.000 loss.py:444(forward)
                1526520   10.493    0.000   10.493    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 152652    1.648    0.000   10.390    0.000 functional.py:2621(mse_loss)
                9214742    9.796    0.000    9.796    0.000 {method 'copy' of 'numpy.ndarray' objects}
                1005334    0.782    0.000    9.031    0.000 <__array_function__ internals>:2(prod)
                7373721    8.435    0.000    8.435    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1005374    0.589    0.000    8.101    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                1019680    0.834    0.000    7.764    0.000 wrapper.py:22(get_info)
                1005334    0.967    0.000    7.513    0.000 fromnumeric.py:2881(prod)
                1526520    7.074    0.000    7.074    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 305304    7.060    0.000    7.060    0.000 {built-in method gather}
                1019680    3.470    0.000    6.930    0.000 libenv.py:363(get_info)
                 152952    0.274    0.000    6.869    0.000 functional.py:68(split)
                 152952    0.279    0.000    6.574    0.000 tensor.py:367(split)
                1005334    1.919    0.000    6.545    0.000 fromnumeric.py:70(_wrapreduction)
                1018650    5.615    0.000    6.515    0.000 module.py:774(__setattr__)
                8853858    5.541    0.000    6.372    0.000 tensor.py:725(grad)
                 152952    6.264    0.000    6.264    0.000 {function Tensor.split at 0x7fdb2abe0940}
                7141737    5.829    0.000    5.839    0.000 module.py:758(__getattr__)
                  50984    0.613    0.000    5.442    0.000 environments.py:76(<listcomp>)
                 152652    5.401    0.000    5.401    0.000 {built-in method torch._C._nn.mse_loss}
                1019700    0.874    0.000    4.852    0.000 environments.py:79(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8281939: <Test_1_0> in cluster <dcc> Done

Job <Test_1_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Wed Nov 11 07:44:32 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov 12 08:23:27 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov 12 08:23:27 2020
Terminated at Thu Nov 12 09:19:34 2020
Results reported at Thu Nov 12 09:19:34 2020

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

    CPU time :                                   3425.00 sec.
    Max Memory :                                 23074 MB
    Average Memory :                             20447.39 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               7646.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   3368 sec.
    Turnaround time :                            92102 sec.

The output (if any) is above this job summary.

