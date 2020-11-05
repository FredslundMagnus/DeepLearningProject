fruitbot_test-0 0.99 fruitbot 100000.0 100000 3000
    Play for :                  1 games.
    Minutes used :              48 minutes.
    Hours used :                0 hours.

# Profiling


      145620951 function calls (139305850 primitive calls) in 2903.65 seconds

##    Ordered by: cumulative time
   List reduced from 1247 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   78/1    0.000    0.000 2903.653 2903.653 {built-in method builtins.exec}
                      1    0.000    0.000 2903.653 2903.653 <string>:1(<module>)
                      1    9.918    9.918 2903.652 2903.652 main.py:13(main)
                  97000    9.114    0.000 2747.412    0.028 agent.py:33(learn)
                  97000    0.354    0.000 1152.876    0.012 tensor.py:155(backward)
                  97000    0.456    0.000 1152.522    0.012 __init__.py:57(backward)
                  97000 1150.220    0.012 1150.220    0.012 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  97000    0.158    0.000 1097.653    0.011 memory.py:75(empty_cache)
                  97000 1097.421    0.011 1097.421    0.011 {built-in method torch._C._cuda_emptyCache}
         6744000/488000   22.907    0.000  234.685    0.000 module.py:710(_call_impl)
                 391000    2.794    0.000  227.056    0.001 agent.py:82(forward)
                1173000    5.881    0.000  216.870    0.000 container.py:115(forward)
                  97000    1.084    0.000  198.671    0.002 memory.py:25(sample_distribution)
                  97000    3.317    0.000  148.849    0.002 helpers.py:12(stack)
                1564000    2.542    0.000   99.367    0.000 conv.py:418(forward)
                  97000    0.522    0.000   96.232    0.001 grad_mode.py:12(decorate_context)
                1564000    2.539    0.000   95.885    0.000 conv.py:410(_conv_forward)
                  97000   23.841    0.000   95.016    0.001 adam.py:51(step)
                1564000   92.882    0.000   92.882    0.000 {built-in method conv2d}
                 100000    0.615    0.000   87.133    0.001 agent.py:28(choose)
                 682036   83.685    0.000   83.692    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                 582000   69.899    0.000   69.899    0.000 {built-in method cat}
                 197000   51.518    0.000   56.026    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 782000    1.571    0.000   40.189    0.000 linear.py:90(forward)
                 782000    3.117    0.000   37.993    0.000 functional.py:1655(linear)
                1955000    1.530    0.000   27.236    0.000 activation.py:653(forward)
                 782000   26.999    0.000   26.999    0.000 {built-in method addmm}
                1955000    2.259    0.000   25.705    0.000 functional.py:1277(leaky_relu)
                 100000    8.450    0.000   24.788    0.000 exploration.py:19(softmax)
                1955000   23.221    0.000   23.221    0.000 {built-in method torch._C._nn.leaky_relu}
                 782000    1.233    0.000   20.516    0.000 pooling.py:156(forward)
                 782000    1.021    0.000   19.284    0.000 _jit_internal.py:237(fn)
                 782000    1.094    0.000   18.108    0.000 functional.py:564(_max_pool2d)
                2328000   17.588    0.000   17.588    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 392192   17.352    0.000   17.352    0.000 {built-in method as_tensor}
                 782000   16.921    0.000   16.921    0.000 {built-in method max_pool2d}
                2328000   15.763    0.000   15.763    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 700000   14.060    0.000   14.060    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000   12.756   12.756 agent.py:16(__init__)
                      3    0.000    0.000   12.712    4.237 module.py:524(to)
                   51/3    0.000    0.000   12.712    4.237 module.py:352(_apply)
                     36    0.000    0.000   12.711    0.353 module.py:602(convert)
                 100000    0.619    0.000   12.684    0.000 interop.py:274(step)
                1164000   11.020    0.000   11.020    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                  97000    1.618    0.000    9.187    0.000 optimizer.py:166(zero_grad)
                 101192    0.225    0.000    9.098    0.000 helpers.py:8(clean)
                1164000    9.072    0.000    9.072    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1164000    7.418    0.000    7.418    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1164000    7.088    0.000    7.088    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 201192    0.340    0.000    6.428    0.000 extract_dict_ob.py:9(observe)
                 201192    0.113    0.000    6.088    0.000 wrapper.py:19(observe)
                 201192    0.540    0.000    5.976    0.000 libenv.py:344(observe)
                 401192    0.613    0.000    5.967    0.000 libenv.py:281(_maybe_copy_dict)
                1203609    5.536    0.000    5.536    0.000 {method 'copy' of 'numpy.ndarray' objects}
                1164000    5.180    0.000    5.180    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                  97000    0.129    0.000    4.655    0.000 loss.py:444(forward)
                  97000    0.572    0.000    4.526    0.000 functional.py:2621(mse_loss)
                 782000    4.512    0.000    4.512    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 100000    0.083    0.000    4.268    0.000 wrapper.py:25(act)
                 100000    0.223    0.000    4.185    0.000 env.py:197(act)
                 100000    3.845    0.000    3.856    0.000 libenv.py:352(act)
                5820036    3.268    0.000    3.827    0.000 tensor.py:725(grad)
                 194000    3.618    0.000    3.618    0.000 {built-in method gather}
                6744000    3.264    0.000    3.264    0.000 {built-in method torch._C._get_tracing_state}
                5867443    3.219    0.000    3.220    0.000 module.py:758(__getattr__)
                 197007    0.321    0.000    2.944    0.000 <__array_function__ internals>:2(prod)
                      1    0.000    0.000    2.900    2.900 environments.py:62(__getitem__)
                      1    0.000    0.000    2.900    2.900 registration.py:144(make)
                      1    0.000    0.000    2.900    2.900 registration.py:84(make)
                      1    0.000    0.000    2.810    2.810 registration.py:50(make)
                      1    0.000    0.000    2.810    2.810 gym_registration.py:6(make_env)
                      1    0.000    0.000    2.809    2.809 env.py:207(__init__)
                      1    0.000    0.000    2.809    2.809 env.py:71(__init__)
                      1    2.646    2.646    2.808    2.808 libenv.py:64(__init__)
                 200000    0.284    0.000    2.746    0.000 wrapper.py:22(get_info)
                 585000    2.646    0.000    2.646    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                 197009    0.226    0.000    2.575    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                  97000    2.498    0.000    2.498    0.000 {built-in method torch._C._nn.mse_loss}
                 200000    1.405    0.000    2.462    0.000 libenv.py:363(get_info)
               28149000    2.424    0.000    2.424    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 588776    1.955    0.000    2.393    0.000 module.py:774(__setattr__)
                 197007    0.359    0.000    2.349    0.000 fromnumeric.py:2881(prod)
                 782000    0.630    0.000    2.179    0.000 _overrides.py:779(has_torch_function)
                 100000    0.154    0.000    2.030    0.000 interop.py:282(render)
                1758005    0.995    0.000    2.010    0.000 {built-in method builtins.any}
                 197007    0.695    0.000    1.990    0.000 fromnumeric.py:70(_wrapreduction)
                1185000    1.952    0.000    1.952    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
        15635686/15634686    1.830    0.000    1.831    0.000 {built-in method builtins.len}
                  97000    0.368    0.000    1.814    0.000 __init__.py:25(_make_grads)
                 100000    1.758    0.000    1.758    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                 100000    1.745    0.000    1.745    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                 100000    0.191    0.000    1.662    0.000 functional.py:1465(softmax)
                 100000    1.455    0.000    1.455    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                  97000    1.417    0.000    1.417    0.000 {built-in method argmax}
                  97000    1.380    0.000    1.380    0.000 {built-in method ones_like}
                  97000    1.243    0.000    1.243    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                  97000    0.464    0.000    1.176    0.000 functional.py:36(broadcast_tensors)
                1173000    0.809    0.000    1.105    0.000 container.py:107(__iter__)
                 197040    0.953    0.000    0.953    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                 197008    0.310    0.000    0.953    0.000 numerictypes.py:360(issubdtype)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8265943: <fruitbot_test_0> in cluster <dcc> Done

Job <fruitbot_test_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Thu Nov  5 18:50:27 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov  5 19:34:41 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov  5 19:34:41 2020
Terminated at Thu Nov  5 20:23:12 2020
Results reported at Thu Nov  5 20:23:12 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=25G]"
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

    CPU time :                                   834.00 sec.
    Max Memory :                                 11805 MB
    Average Memory :                             7590.58 MB
    Total Requested Memory :                     25600.00 MB
    Delta Memory :                               13795.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   2911 sec.
    Turnaround time :                            5565 sec.

The output (if any) is above this job summary.

