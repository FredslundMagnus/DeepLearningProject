bigfish_test-0 0.99 bigfish 100000.0 100000 3000
    Play for :                  1 games.
    Minutes used :              60 minutes.
    Hours used :                1 hours.

# Profiling


      145612877 function calls (139297776 primitive calls) in 3642.60 seconds

##    Ordered by: cumulative time
   List reduced from 1247 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   78/1    0.000    0.000 3642.601 3642.601 {built-in method builtins.exec}
                      1    0.000    0.000 3642.601 3642.601 <string>:1(<module>)
                      1   10.505   10.505 3642.600 3642.600 main.py:13(main)
                  97000   11.201    0.000 3468.696    0.036 agent.py:33(learn)
                  97000    0.415    0.000 1463.153    0.015 tensor.py:155(backward)
                  97000    0.427    0.000 1462.738    0.015 __init__.py:57(backward)
                  97000 1460.029    0.015 1460.029    0.015 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  97000    0.150    0.000 1409.574    0.015 memory.py:75(empty_cache)
                  97000 1409.340    0.015 1409.340    0.015 {built-in method torch._C._cuda_emptyCache}
         6744000/488000   25.196    0.000  288.649    0.001 module.py:710(_call_impl)
                 391000    3.235    0.000  279.852    0.001 agent.py:82(forward)
                1173000    7.605    0.000  267.946    0.000 container.py:115(forward)
                  97000    1.142    0.000  199.054    0.002 memory.py:25(sample_distribution)
                  97000    3.856    0.000  148.212    0.002 helpers.py:12(stack)
                  97000    0.563    0.000  144.461    0.001 grad_mode.py:12(decorate_context)
                  97000   33.460    0.000  143.158    0.001 adam.py:51(step)
                1564000    2.748    0.000  121.912    0.000 conv.py:418(forward)
                1564000    2.780    0.000  118.208    0.000 conv.py:410(_conv_forward)
                1564000  114.945    0.000  114.945    0.000 {built-in method conv2d}
                 100000    0.693    0.000  104.852    0.001 agent.py:28(choose)
                 682036   81.734    0.000   81.802    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                 582000   64.455    0.000   64.455    0.000 {built-in method cat}
                 197000   52.710    0.000   57.712    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 782000    1.666    0.000   49.145    0.000 linear.py:90(forward)
                 782000    3.412    0.000   46.832    0.000 functional.py:1655(linear)
                1955000    1.779    0.000   37.007    0.000 activation.py:653(forward)
                1955000    2.529    0.000   35.228    0.000 functional.py:1277(leaky_relu)
                 782000   33.771    0.000   33.771    0.000 {built-in method addmm}
                1955000   32.473    0.000   32.473    0.000 {built-in method torch._C._nn.leaky_relu}
                 100000    9.363    0.000   28.540    0.000 exploration.py:19(softmax)
                2328000   28.244    0.000   28.244    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2328000   25.482    0.000   25.482    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 782000    1.276    0.000   25.166    0.000 pooling.py:156(forward)
                 782000    1.105    0.000   23.890    0.000 _jit_internal.py:237(fn)
                 782000    1.271    0.000   22.625    0.000 functional.py:564(_max_pool2d)
                 782000   21.259    0.000   21.259    0.000 {built-in method max_pool2d}
                 391825   20.788    0.000   20.788    0.000 {built-in method as_tensor}
                 700000   16.592    0.000   16.592    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1164000   15.969    0.000   15.969    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                  97000    2.218    0.000   14.594    0.000 optimizer.py:166(zero_grad)
                1164000   13.340    0.000   13.340    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 100000    0.646    0.000   12.021    0.000 interop.py:274(step)
                1164000   11.626    0.000   11.626    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1164000   11.284    0.000   11.284    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 100825    0.253    0.000   10.147    0.000 helpers.py:8(clean)
                      1    0.000    0.000    9.140    9.140 agent.py:16(__init__)
                      3    0.000    0.000    9.116    3.039 module.py:524(to)
                   51/3    0.000    0.000    9.116    3.039 module.py:352(_apply)
                     36    0.000    0.000    9.115    0.253 module.py:602(convert)
                1164000    9.100    0.000    9.100    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 200825    0.362    0.000    6.533    0.000 extract_dict_ob.py:9(observe)
                 200825    0.132    0.000    6.170    0.000 wrapper.py:19(observe)
                 782000    6.102    0.000    6.102    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 200825    0.540    0.000    6.038    0.000 libenv.py:344(observe)
                 400825    0.662    0.000    5.997    0.000 libenv.py:281(_maybe_copy_dict)
                  97000    0.145    0.000    5.588    0.000 loss.py:444(forward)
                1202508    5.566    0.000    5.566    0.000 {method 'copy' of 'numpy.ndarray' objects}
                  97000    0.612    0.000    5.443    0.000 functional.py:2621(mse_loss)
                 194000    4.814    0.000    4.814    0.000 {built-in method gather}
                6744000    4.742    0.000    4.742    0.000 {built-in method torch._C._get_tracing_state}
                5820036    4.068    0.000    4.690    0.000 tensor.py:725(grad)
                 585000    3.510    0.000    3.510    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                5867443    3.393    0.000    3.394    0.000 module.py:758(__getattr__)
                 100000    0.076    0.000    3.342    0.000 wrapper.py:25(act)
                 197007    0.356    0.000    3.284    0.000 <__array_function__ internals>:2(prod)
                  97000    3.269    0.000    3.269    0.000 {built-in method torch._C._nn.mse_loss}
                 100000    0.232    0.000    3.266    0.000 env.py:197(act)
                 200000    0.364    0.000    2.952    0.000 wrapper.py:22(get_info)
                 100000    2.897    0.000    2.908    0.000 libenv.py:352(act)
                 197009    0.233    0.000    2.871    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                 197007    0.411    0.000    2.639    0.000 fromnumeric.py:2881(prod)
                1185000    2.632    0.000    2.632    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 588776    2.106    0.000    2.603    0.000 module.py:774(__setattr__)
                 200000    1.462    0.000    2.588    0.000 libenv.py:363(get_info)
                      1    0.000    0.000    2.549    2.549 environments.py:62(__getitem__)
                      1    0.000    0.000    2.549    2.549 registration.py:144(make)
                      1    0.000    0.000    2.549    2.549 registration.py:84(make)
               28149000    2.530    0.000    2.530    0.000 {method 'values' of 'collections.OrderedDict' objects}
                      1    0.000    0.000    2.445    2.445 registration.py:50(make)
                      1    0.000    0.000    2.445    2.445 gym_registration.py:6(make_env)
                      1    0.000    0.000    2.445    2.445 env.py:207(__init__)
                      1    0.000    0.000    2.445    2.445 env.py:71(__init__)
                      1    2.339    2.339    2.442    2.442 libenv.py:64(__init__)
                 100000    2.304    0.000    2.304    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                 100000    2.293    0.000    2.293    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                 100000    0.233    0.000    2.253    0.000 functional.py:1465(softmax)
                  97000    0.406    0.000    2.248    0.000 __init__.py:25(_make_grads)
                 197007    0.691    0.000    2.228    0.000 fromnumeric.py:70(_wrapreduction)
                 782000    0.635    0.000    2.220    0.000 _overrides.py:779(has_torch_function)
                 100000    0.153    0.000    2.157    0.000 interop.py:282(render)
        15635686/15634686    2.075    0.000    2.075    0.000 {built-in method builtins.len}
                1758005    1.015    0.000    2.062    0.000 {built-in method builtins.any}
                 100000    2.002    0.000    2.002    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                  97000    1.875    0.000    1.875    0.000 {built-in method argmax}
                  97000    1.764    0.000    1.764    0.000 {built-in method ones_like}
                  97000    1.682    0.000    1.682    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                  97000    0.470    0.000    1.238    0.000 functional.py:36(broadcast_tensors)
                1173000    0.841    0.000    1.171    0.000 container.py:107(__iter__)
                 197040    1.134    0.000    1.134    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                1164000    1.056    0.000    1.056    0.000 {method 'detach_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 8265941: <bigfish_test_0> in cluster <dcc> Done

Job <bigfish_test_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Thu Nov  5 18:50:27 2020
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov  5 18:51:41 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov  5 18:51:41 2020
Terminated at Thu Nov  5 19:52:28 2020
Results reported at Thu Nov  5 19:52:28 2020

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

    CPU time :                                   963.00 sec.
    Max Memory :                                 12071 MB
    Average Memory :                             7575.71 MB
    Total Requested Memory :                     25600.00 MB
    Delta Memory :                               13529.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   3649 sec.
    Turnaround time :                            3721 sec.

The output (if any) is above this job summary.

