[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
bigfish_normalised-0 0.99 bigfish 1000000 200000 3000
    Play for :                  1 games.
    Minutes used :              152 minutes.
    Hours used :                2 hours.

# Profiling


      1485650868 function calls (1421236567 primitive calls) in 9145.58 seconds

##    Ordered by: cumulative time
   List reduced from 1253 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   78/1    0.000    0.000 9145.585 9145.585 {built-in method builtins.exec}
                      1    0.011    0.011 9145.585 9145.585 <string>:1(<module>)
                      1  109.673  109.673 9145.573 9145.573 main.py:14(main)
                 997000  103.672    0.000 7497.558    0.008 agent.py:34(learn)
                 997000   13.262    0.000 3289.739    0.003 memory.py:25(sample_distribution)
        68844000/4988000  250.060    0.000 2753.079    0.001 module.py:710(_call_impl)
                3991000   34.213    0.000 2669.392    0.001 agent.py:82(forward)
               11973000   65.990    0.000 2499.993    0.000 container.py:115(forward)
                1997000 1729.196    0.001 1779.235    0.001 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 997000   33.576    0.000 1569.688    0.002 helpers.py:12(stack)
               15964000   29.803    0.000 1213.516    0.000 conv.py:418(forward)
               15964000   26.896    0.000 1173.599    0.000 conv.py:410(_conv_forward)
               15964000 1141.950    0.000 1141.950    0.000 {built-in method conv2d}
                 997000    5.186    0.000 1030.865    0.001 grad_mode.py:12(decorate_context)
                 997000  258.179    0.000 1018.443    0.001 adam.py:51(step)
                1000000    6.132    0.000  939.295    0.001 agent.py:29(choose)
                 997000    3.869    0.000  778.264    0.001 tensor.py:155(backward)
                 997000    4.496    0.000  774.395    0.001 __init__.py:57(backward)
                 997000  750.170    0.001  750.170    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                6982036  745.529    0.000  745.535    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                5982000  740.396    0.000  740.396    0.000 {built-in method cat}
                7982000   16.303    0.000  433.612    0.000 linear.py:90(forward)
                7982000   34.679    0.000  410.752    0.000 functional.py:1655(linear)
               19955000   15.954    0.000  313.272    0.000 activation.py:653(forward)
               19955000   24.567    0.000  297.318    0.000 functional.py:1277(leaky_relu)
                7982000  288.174    0.000  288.174    0.000 {built-in method addmm}
               19955000  270.289    0.000  270.289    0.000 {built-in method torch._C._nn.leaky_relu}
                1000000   82.622    0.000  257.881    0.000 exploration.py:19(softmax)
                7982000   12.787    0.000  215.613    0.000 pooling.py:156(forward)
                3998505  204.160    0.000  204.160    0.000 {built-in method as_tensor}
                7982000   10.845    0.000  202.825    0.000 _jit_internal.py:237(fn)
                7982000   12.929    0.000  190.221    0.000 functional.py:564(_max_pool2d)
               23928000  186.576    0.000  186.576    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1000000    6.641    0.000  182.991    0.000 interop.py:274(step)
                7982000  176.244    0.000  176.244    0.000 {built-in method max_pool2d}
               23928000  167.754    0.000  167.754    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7000000  158.356    0.000  158.356    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1007505   47.546    0.000  157.189    0.000 helpers.py:8(clean)
                2007505    4.006    0.000  127.946    0.000 extract_dict_ob.py:9(observe)
                2007505    1.260    0.000  123.940    0.000 wrapper.py:19(observe)
                2007505    5.326    0.000  122.680    0.000 libenv.py:344(observe)
                4007505    6.039    0.000  122.498    0.000 libenv.py:281(_maybe_copy_dict)
               12022848  118.505    0.000  118.505    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11964000  118.276    0.000  118.276    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11964000   96.181    0.000   96.181    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 997000   17.263    0.000   96.127    0.000 optimizer.py:166(zero_grad)
                4991000   81.192    0.000   81.192    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               11964000   79.270    0.000   79.270    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11964000   75.565    0.000   75.565    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11964000   54.101    0.000   54.101    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7982000   51.869    0.000   51.869    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 997000    1.465    0.000   50.709    0.000 loss.py:444(forward)
                 997000    6.447    0.000   49.243    0.000 functional.py:2621(mse_loss)
               59820036   36.253    0.000   42.522    0.000 tensor.py:725(grad)
                1994000   41.055    0.000   41.055    0.000 {built-in method gather}
               68844000   35.861    0.000   35.861    0.000 {built-in method torch._C._get_tracing_state}
               59887843   34.492    0.000   34.501    0.000 module.py:758(__getattr__)
                1000000    0.795    0.000   33.925    0.000 wrapper.py:25(act)
                1000000    2.629    0.000   33.130    0.000 env.py:197(act)
                1997007    3.858    0.000   33.000    0.000 <__array_function__ internals>:2(prod)
                1000000   29.167    0.000   29.298    0.000 libenv.py:352(act)
                1997009    2.419    0.000   28.560    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                2000000    3.091    0.000   28.023    0.000 wrapper.py:22(get_info)
                 997000   27.115    0.000   27.115    0.000 {built-in method torch._C._nn.mse_loss}
              287349000   26.378    0.000   26.378    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1997007    3.949    0.000   26.141    0.000 fromnumeric.py:2881(prod)
                5988776   20.665    0.000   25.199    0.000 module.py:774(__setattr__)
                2000000   14.418    0.000   24.932    0.000 libenv.py:363(get_info)
                7982000    6.466    0.000   23.413    0.000 _overrides.py:779(has_torch_function)
                1997007    7.549    0.000   22.193    0.000 fromnumeric.py:70(_wrapreduction)
               17958005   10.818    0.000   21.842    0.000 {built-in method builtins.any}
               11985000   21.168    0.000   21.168    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1000000    1.495    0.000   20.172    0.000 interop.py:282(render)
        159635986/159634986   19.943    0.000   19.944    0.000 {built-in method builtins.len}
                 997000    4.140    0.000   19.390    0.000 __init__.py:25(_make_grads)
                1000000   19.288    0.000   19.288    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1000000    2.452    0.000   18.808    0.000 functional.py:1465(softmax)
                1000000   18.791    0.000   18.791    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                1000000   16.197    0.000   16.197    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 997000   15.795    0.000   15.795    0.000 {built-in method argmax}
                      1    0.003    0.003   14.659   14.659 agent.py:16(__init__)
                      3    0.000    0.000   14.621    4.874 module.py:524(to)
                   51/3    0.001    0.000   14.621    4.874 module.py:352(_apply)
                     36    0.000    0.000   14.620    0.406 module.py:602(convert)
                 997000   14.441    0.000   14.441    0.000 {built-in method ones_like}
                 997000   13.250    0.000   13.250    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                    333    0.043    0.000   13.059    0.039 agent.py:53(update_target_network)
                 997000    5.011    0.000   12.508    0.000 functional.py:36(broadcast_tensors)
               11973000    8.667    0.000   11.960    0.000 container.py:107(__iter__)
                 997000   11.862    0.000   11.862    0.000 memory.py:26(<listcomp>)
                    333    3.535    0.011   11.353    0.034 memory.py:28(update_distribution)
                1997340   10.917    0.000   10.917    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                1000666   10.880    0.000   10.880    0.000 {built-in method numpy.array}
               75799110   10.617    0.000   10.617    0.000 {built-in method builtins.hasattr}
                1997008    3.351    0.000   10.437    0.000 numerictypes.py:360(issubdtype)
               23946000    5.977    0.000   10.322    0.000 _overrides.py:792(<genexpr>)
                1000000    9.608    0.000    9.608    0.000 memory.py:13(inner)
                1994000    9.209    0.000    9.209    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                 997000    7.922    0.000    7.922    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3994016    4.708    0.000    6.835    0.000 numerictypes.py:286(issubclass_)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8266217: <bigfish_normalised_0> in cluster <dcc> Done

Job <bigfish_normalised_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Thu Nov  5 21:40:32 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov  5 22:07:50 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov  5 22:07:50 2020
Terminated at Fri Nov  6 00:40:23 2020
Results reported at Fri Nov  6 00:40:23 2020

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

    CPU time :                                   9503.00 sec.
    Max Memory :                                 25269 MB
    Average Memory :                             22324.53 MB
    Total Requested Memory :                     25600.00 MB
    Delta Memory :                               331.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   9153 sec.
    Turnaround time :                            10791 sec.

The output (if any) is above this job summary.

