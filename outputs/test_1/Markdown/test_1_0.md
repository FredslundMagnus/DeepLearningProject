test_1-0 MME 0.12 0.3 0.0001 0.0
    Play for :                  1 games.
    Minutes used :              2 minutes.
    Hours used :                0 hours.

# Profiling


      22814282 function calls (21946475 primitive calls) in 126.79 seconds

##    Ordered by: cumulative time
   List reduced from 1291 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   84/1    0.000    0.000  126.794  126.794 {built-in method builtins.exec}
                      1    0.000    0.000  126.794  126.794 <string>:1(<module>)
                      1    1.511    1.511  126.794  126.794 main.py:12(main)
                  16632    1.460    0.000   83.892    0.005 agent.py:33(learn)
           946496/88160    3.278    0.000   36.275    0.000 module.py:710(_call_impl)
                  71528    0.370    0.000   34.977    0.000 agent.py:99(forward)
                 143056    0.855    0.000   33.593    0.000 container.py:115(forward)
                  16632    0.165    0.000   26.529    0.002 memory.py:25(sample_distribution)
                 121460   24.691    0.000   24.693    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                  16632    0.472    0.000   23.546    0.001 helpers.py:11(stack)
                 286112    0.444    0.000   18.105    0.000 conv.py:418(forward)
                 286112    0.467    0.000   17.497    0.000 conv.py:410(_conv_forward)
                 286112   16.949    0.000   16.949    0.000 {built-in method conv2d}
                  21632    0.126    0.000   16.366    0.001 agent.py:28(choose)
                  16632    0.082    0.000   16.166    0.001 grad_mode.py:12(decorate_context)
                  16632    3.979    0.000   15.973    0.001 adam.py:51(step)
                      1    0.000    0.000   12.603   12.603 agent.py:16(__init__)
                      3    0.000    0.000   12.586    4.195 module.py:524(to)
                   39/3    0.000    0.000   12.586    4.195 module.py:352(_apply)
                     36    0.000    0.000   12.585    0.350 module.py:602(convert)
                  16632    0.061    0.000   11.055    0.001 tensor.py:155(backward)
                  16632    0.069    0.000   10.994    0.001 __init__.py:57(backward)
                  16632   10.614    0.001   10.614    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  99792   10.151    0.000   10.151    0.000 {built-in method cat}
                 143056    0.278    0.000    7.218    0.000 linear.py:90(forward)
                 143056    0.568    0.000    6.831    0.000 functional.py:1655(linear)
                  21632    1.749    0.000    5.167    0.000 exploration.py:19(softmax)
                 143056    4.854    0.000    4.854    0.000 {built-in method addmm}
                  38264    3.555    0.000    4.397    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 286112    0.229    0.000    4.035    0.000 activation.py:653(forward)
                 286112    0.365    0.000    3.806    0.000 functional.py:1277(leaky_relu)
                  71728    3.594    0.000    3.594    0.000 {built-in method as_tensor}
                      1    0.000    0.000    3.454    3.454 environments.py:48(__getattribute__)
                      1    0.000    0.000    3.454    3.454 registration.py:144(make)
                      1    0.000    0.000    3.454    3.454 registration.py:84(make)
                 286112    3.405    0.000    3.405    0.000 {built-in method torch._C._nn.leaky_relu}
                      1    0.000    0.000    3.286    3.286 registration.py:50(make)
                      1    0.000    0.000    3.286    3.286 gym_registration.py:6(make_env)
                      1    0.000    0.000    3.285    3.285 env.py:207(__init__)
                      1    0.000    0.000    3.285    3.285 env.py:71(__init__)
                      1    3.108    3.108    3.282    3.282 libenv.py:64(__init__)
                 151424    3.099    0.000    3.099    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                 399168    2.924    0.000    2.924    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 399168    2.644    0.000    2.644    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                  21632    0.132    0.000    2.397    0.000 interop.py:274(step)
                  21832    0.050    0.000    2.186    0.000 helpers.py:7(clean)
                 199584    1.877    0.000    1.877    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                  16632    0.283    0.000    1.575    0.000 optimizer.py:166(zero_grad)
                 199584    1.537    0.000    1.537    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 199584    1.270    0.000    1.270    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 199584    1.206    0.000    1.206    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                  43464    0.068    0.000    1.076    0.000 extract_dict_ob.py:9(observe)
                  43464    0.025    0.000    1.008    0.000 wrapper.py:19(observe)
                  43464    0.109    0.000    0.983    0.000 libenv.py:344(observe)
                  86728    0.128    0.000    0.980    0.000 libenv.py:281(_maybe_copy_dict)
                 199584    0.892    0.000    0.892    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 260188    0.891    0.000    0.891    0.000 {method 'copy' of 'numpy.ndarray' objects}
                  21632    0.016    0.000    0.887    0.000 wrapper.py:25(act)
                  21632    0.047    0.000    0.871    0.000 env.py:197(act)
                 143056    0.809    0.000    0.809    0.000 {method 't' of 'torch._C._TensorBase' objects}
                  21632    0.799    0.000    0.802    0.000 libenv.py:352(act)
                  16632    0.023    0.000    0.777    0.000 loss.py:444(forward)
                  16632    0.094    0.000    0.754    0.000 functional.py:2621(mse_loss)
                 997956    0.545    0.000    0.638    0.000 tensor.py:725(grad)
                  33264    0.617    0.000    0.617    0.000 {built-in method gather}
                  43264    0.059    0.000    0.544    0.000 wrapper.py:22(get_info)
                  38271    0.058    0.000    0.532    0.000 <__array_function__ internals>:2(prod)
                1001778    0.509    0.000    0.510    0.000 module.py:758(__getattr__)
                  43264    0.270    0.000    0.485    0.000 libenv.py:363(get_info)
                 946496    0.483    0.000    0.483    0.000 {built-in method torch._C._get_tracing_state}
                  38273    0.041    0.000    0.465    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                 104792    0.465    0.000    0.465    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                 110403    0.351    0.000    0.433    0.000 module.py:774(__setattr__)
                  38271    0.066    0.000    0.424    0.000 fromnumeric.py:2881(prod)
                  16632    0.417    0.000    0.417    0.000 {built-in method torch._C._nn.mse_loss}
                 143056    0.110    0.000    0.391    0.000 _overrides.py:779(has_torch_function)
                 234584    0.382    0.000    0.382    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                  21632    0.028    0.000    0.379    0.000 interop.py:282(render)
                  21632    0.370    0.000    0.370    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                  21632    0.367    0.000    0.367    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                 319381    0.173    0.000    0.360    0.000 {built-in method builtins.any}
                  38271    0.124    0.000    0.358    0.000 fromnumeric.py:70(_wrapreduction)
                  21632    0.046    0.000    0.357    0.000 functional.py:1465(softmax)
                      6    0.000    0.000    0.328    0.055 __init__.py:1(<module>)
                3929040    0.324    0.000    0.324    0.000 {method 'values' of 'collections.OrderedDict' objects}
                  21632    0.307    0.000    0.307    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                  16632    0.062    0.000    0.306    0.000 __init__.py:25(_make_grads)
        2133548/2132548    0.255    0.000    0.255    0.000 {built-in method builtins.len}
                  16632    0.239    0.000    0.239    0.000 {built-in method argmax}
                  16632    0.232    0.000    0.232    0.000 {built-in method ones_like}
                   85/7    0.001    0.000    0.223    0.032 <frozen importlib._bootstrap>:986(_find_and_load)
                   84/6    0.000    0.000    0.223    0.037 <frozen importlib._bootstrap>:956(_find_and_load_unlocked)
                   81/5    0.000    0.000    0.217    0.043 <frozen importlib._bootstrap>:650(_load_unlocked)
                  113/6    0.000    0.000    0.210    0.035 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
                  16632    0.210    0.000    0.210    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                   79/4    0.000    0.000    0.203    0.051 <frozen importlib._bootstrap_external>:777(exec_module)
                  16632    0.077    0.000    0.195    0.000 functional.py:36(broadcast_tensors)
                  38272    0.062    0.000    0.187    0.000 numerictypes.py:360(issubdtype)
                 429168    0.102    0.000    0.176    0.000 _overrides.py:792(<genexpr>)
                  38275    0.175    0.000    0.175    0.000 {method 'reduce' of 'numpy.ufunc' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8253820: <test_1_0> in cluster <dcc> Done

Job <test_1_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Mon Nov  2 18:58:12 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 19:09:27 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 19:09:27 2020
Terminated at Mon Nov  2 19:11:42 2020
Results reported at Mon Nov  2 19:11:42 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=10G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 10
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   121.00 sec.
    Max Memory :                                 1225 MB
    Average Memory :                             1225.00 MB
    Total Requested Memory :                     10240.00 MB
    Delta Memory :                               9015.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   135 sec.
    Turnaround time :                            810 sec.

The output (if any) is above this job summary.

