chaser_test-0 0.99 chaser 100000.0 100000 3000
    Play for :                  1 games.
    Minutes used :              50 minutes.
    Hours used :                0 hours.

# Profiling


      145612657 function calls (139297556 primitive calls) in 3042.88 seconds

##    Ordered by: cumulative time
   List reduced from 1247 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   78/1    0.000    0.000 3042.876 3042.876 {built-in method builtins.exec}
                      1    0.000    0.000 3042.876 3042.876 <string>:1(<module>)
                      1   10.631   10.631 3042.876 3042.876 main.py:13(main)
                  97000   11.050    0.000 2870.717    0.030 agent.py:33(learn)
                  97000    0.392    0.000 1184.683    0.012 tensor.py:155(backward)
                  97000    0.432    0.000 1184.291    0.012 __init__.py:57(backward)
                  97000 1181.587    0.012 1181.587    0.012 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  97000    0.160    0.000 1098.099    0.011 memory.py:75(empty_cache)
                  97000 1097.857    0.011 1097.857    0.011 {built-in method torch._C._cuda_emptyCache}
         6744000/488000   25.076    0.000  282.954    0.001 module.py:710(_call_impl)
                 391000    3.199    0.000  274.173    0.001 agent.py:82(forward)
                1173000    7.478    0.000  262.376    0.000 container.py:115(forward)
                  97000    1.125    0.000  196.471    0.002 memory.py:25(sample_distribution)
                  97000    3.847    0.000  145.740    0.002 helpers.py:12(stack)
                  97000    0.581    0.000  143.992    0.001 grad_mode.py:12(decorate_context)
                  97000   33.357    0.000  142.723    0.001 adam.py:51(step)
                1564000    2.738    0.000  118.809    0.000 conv.py:418(forward)
                1564000    2.665    0.000  115.085    0.000 conv.py:410(_conv_forward)
                1564000  111.966    0.000  111.966    0.000 {built-in method conv2d}
                 100000    0.665    0.000  103.191    0.001 agent.py:28(choose)
                 682036   80.736    0.000   80.745    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                 582000   62.716    0.000   62.716    0.000 {built-in method cat}
                 197000   52.713    0.000   57.697    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 782000    1.633    0.000   48.798    0.000 linear.py:90(forward)
                 782000    3.465    0.000   46.508    0.000 functional.py:1655(linear)
                1955000    1.586    0.000   36.056    0.000 activation.py:653(forward)
                1955000    2.450    0.000   34.470    0.000 functional.py:1277(leaky_relu)
                 782000   33.333    0.000   33.333    0.000 {built-in method addmm}
                1955000   31.794    0.000   31.794    0.000 {built-in method torch._C._nn.leaky_relu}
                 100000    9.277    0.000   28.377    0.000 exploration.py:19(softmax)
                2328000   28.264    0.000   28.264    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2328000   25.591    0.000   25.591    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 782000    1.152    0.000   24.572    0.000 pooling.py:156(forward)
                 782000    1.045    0.000   23.420    0.000 _jit_internal.py:237(fn)
                 782000    1.264    0.000   22.222    0.000 functional.py:564(_max_pool2d)
                 782000   20.865    0.000   20.865    0.000 {built-in method max_pool2d}
                 391815   20.534    0.000   20.534    0.000 {built-in method as_tensor}
                 700000   16.551    0.000   16.551    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1164000   15.826    0.000   15.826    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                  97000    2.168    0.000   14.231    0.000 optimizer.py:166(zero_grad)
                1164000   13.239    0.000   13.239    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 100000    0.658    0.000   12.812    0.000 interop.py:274(step)
                1164000   11.575    0.000   11.575    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1164000   11.271    0.000   11.271    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 100815    0.258    0.000   10.136    0.000 helpers.py:8(clean)
                1164000    8.921    0.000    8.921    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    8.696    8.696 agent.py:16(__init__)
                      3    0.000    0.000    8.675    2.892 module.py:524(to)
                   51/3    0.000    0.000    8.675    2.892 module.py:352(_apply)
                     36    0.000    0.000    8.674    0.241 module.py:602(convert)
                 200815    0.362    0.000    6.372    0.000 extract_dict_ob.py:9(observe)
                 782000    6.147    0.000    6.147    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 200815    0.125    0.000    6.011    0.000 wrapper.py:19(observe)
                 400815    0.654    0.000    5.901    0.000 libenv.py:281(_maybe_copy_dict)
                 200815    0.530    0.000    5.886    0.000 libenv.py:344(observe)
                  97000    0.139    0.000    5.532    0.000 loss.py:444(forward)
                1202478    5.494    0.000    5.494    0.000 {method 'copy' of 'numpy.ndarray' objects}
                  97000    0.593    0.000    5.393    0.000 functional.py:2621(mse_loss)
                 194000    4.647    0.000    4.647    0.000 {built-in method gather}
                5820036    3.859    0.000    4.466    0.000 tensor.py:725(grad)
                6744000    4.459    0.000    4.459    0.000 {built-in method torch._C._get_tracing_state}
                 100000    0.077    0.000    4.255    0.000 wrapper.py:25(act)
                 100000    0.246    0.000    4.177    0.000 env.py:197(act)
                 100000    3.789    0.000    3.801    0.000 libenv.py:352(act)
                 585000    3.525    0.000    3.525    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                5867443    3.388    0.000    3.389    0.000 module.py:758(__getattr__)
                 197007    0.362    0.000    3.250    0.000 <__array_function__ internals>:2(prod)
                  97000    3.237    0.000    3.237    0.000 {built-in method torch._C._nn.mse_loss}
                 200000    0.300    0.000    2.924    0.000 wrapper.py:22(get_info)
                 197009    0.229    0.000    2.827    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                 200000    1.472    0.000    2.625    0.000 libenv.py:363(get_info)
                1185000    2.613    0.000    2.613    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 197007    0.412    0.000    2.597    0.000 fromnumeric.py:2881(prod)
                 588776    2.104    0.000    2.575    0.000 module.py:774(__setattr__)
               28149000    2.514    0.000    2.514    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 100000    2.282    0.000    2.282    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                 100000    2.271    0.000    2.271    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                 782000    0.625    0.000    2.263    0.000 _overrides.py:779(has_torch_function)
                  97000    0.399    0.000    2.239    0.000 __init__.py:25(_make_grads)
                      1    0.000    0.000    2.236    2.236 environments.py:62(__getitem__)
                      1    0.000    0.000    2.236    2.236 registration.py:144(make)
                      1    0.000    0.000    2.236    2.236 registration.py:84(make)
                 100000    0.220    0.000    2.235    0.000 functional.py:1465(softmax)
                 197007    0.687    0.000    2.185    0.000 fromnumeric.py:70(_wrapreduction)
                      1    0.000    0.000    2.157    2.157 registration.py:50(make)
                      1    0.000    0.000    2.157    2.157 gym_registration.py:6(make_env)
                      1    0.000    0.000    2.157    2.157 env.py:207(__init__)
                      1    0.000    0.000    2.157    2.157 env.py:71(__init__)
                      1    2.061    2.061    2.155    2.155 libenv.py:64(__init__)
                1758005    1.038    0.000    2.128    0.000 {built-in method builtins.any}
                 100000    0.149    0.000    2.101    0.000 interop.py:282(render)
                 100000    1.999    0.000    1.999    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
        15635686/15634686    1.971    0.000    1.971    0.000 {built-in method builtins.len}
                  97000    1.864    0.000    1.864    0.000 {built-in method argmax}
                  97000    1.759    0.000    1.759    0.000 {built-in method ones_like}
                  97000    1.638    0.000    1.638    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                  97000    0.480    0.000    1.249    0.000 functional.py:36(broadcast_tensors)
                1173000    0.846    0.000    1.187    0.000 container.py:107(__iter__)
                 197040    1.124    0.000    1.124    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                 197008    0.336    0.000    1.059    0.000 numerictypes.py:360(issubdtype)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8265942: <chaser_test_0> in cluster <dcc> Done

Job <chaser_test_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Thu Nov  5 18:50:27 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov  5 19:05:53 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov  5 19:05:53 2020
Terminated at Thu Nov  5 19:56:41 2020
Results reported at Thu Nov  5 19:56:41 2020

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

    CPU time :                                   960.00 sec.
    Max Memory :                                 12003 MB
    Average Memory :                             7646.04 MB
    Total Requested Memory :                     25600.00 MB
    Delta Memory :                               13597.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   3047 sec.
    Turnaround time :                            3974 sec.

The output (if any) is above this job summary.

