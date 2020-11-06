[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
fruitbot_normalised-0 0.99 fruitbot 1000000 200000 3000
    Play for :                  1 games.
    Minutes used :              147 minutes.
    Hours used :                2 hours.

# Profiling


      1485691776 function calls (1421277475 primitive calls) in 8826.89 seconds

##    Ordered by: cumulative time
   List reduced from 1253 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   78/1    0.000    0.000 8826.886 8826.886 {built-in method builtins.exec}
                      1    0.013    0.013 8826.886 8826.886 <string>:1(<module>)
                      1  104.698  104.698 8826.873 8826.873 main.py:14(main)
                 997000   98.649    0.000 7237.220    0.007 agent.py:34(learn)
                 997000   12.207    0.000 3192.274    0.003 memory.py:25(sample_distribution)
        68844000/4988000  242.135    0.000 2633.504    0.001 module.py:710(_call_impl)
                3991000   32.228    0.000 2552.969    0.001 agent.py:82(forward)
               11973000   61.770    0.000 2389.304    0.000 container.py:115(forward)
                1997000 1709.073    0.001 1758.572    0.001 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 997000   31.821    0.000 1491.829    0.001 helpers.py:12(stack)
               15964000   28.098    0.000 1156.602    0.000 conv.py:418(forward)
               15964000   25.751    0.000 1118.675    0.000 conv.py:410(_conv_forward)
               15964000 1088.211    0.000 1088.211    0.000 {built-in method conv2d}
                 997000    5.234    0.000  994.972    0.001 grad_mode.py:12(decorate_context)
                 997000  248.022    0.000  982.885    0.001 adam.py:51(step)
                1000000    6.471    0.000  900.525    0.001 agent.py:29(choose)
                 997000    3.731    0.000  752.663    0.001 tensor.py:155(backward)
                 997000    4.123    0.000  748.932    0.001 __init__.py:57(backward)
                6982036  730.660    0.000  730.717    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                 997000  726.092    0.001  726.092    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5982000  680.492    0.000  680.492    0.000 {built-in method cat}
                7982000   16.093    0.000  415.584    0.000 linear.py:90(forward)
                7982000   32.732    0.000  393.232    0.000 functional.py:1655(linear)
               19955000   15.944    0.000  296.562    0.000 activation.py:653(forward)
               19955000   22.512    0.000  280.618    0.000 functional.py:1277(leaky_relu)
                7982000  276.721    0.000  276.721    0.000 {built-in method addmm}
               19955000  255.714    0.000  255.714    0.000 {built-in method torch._C._nn.leaky_relu}
                1000000   78.934    0.000  246.207    0.000 exploration.py:19(softmax)
                7982000   12.016    0.000  207.982    0.000 pooling.py:156(forward)
                3999966  196.868    0.000  196.868    0.000 {built-in method as_tensor}
                7982000   11.050    0.000  195.966    0.000 _jit_internal.py:237(fn)
                1000000    6.489    0.000  184.711    0.000 interop.py:274(step)
                7982000   13.165    0.000  183.326    0.000 functional.py:564(_max_pool2d)
               23928000  182.372    0.000  182.372    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                7982000  169.121    0.000  169.121    0.000 {built-in method max_pool2d}
               23928000  163.541    0.000  163.541    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1008966   45.463    0.000  152.330    0.000 helpers.py:8(clean)
                7000000  151.990    0.000  151.990    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2008966    3.841    0.000  121.017    0.000 extract_dict_ob.py:9(observe)
                2008966    1.188    0.000  117.176    0.000 wrapper.py:19(observe)
                4008966    6.204    0.000  116.080    0.000 libenv.py:281(_maybe_copy_dict)
                2008966    4.930    0.000  115.988    0.000 libenv.py:344(observe)
               11964000  113.372    0.000  113.372    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               12027231  111.808    0.000  111.808    0.000 {method 'copy' of 'numpy.ndarray' objects}
                 997000   16.915    0.000   95.278    0.000 optimizer.py:166(zero_grad)
               11964000   93.622    0.000   93.622    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4991000   77.806    0.000   77.806    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               11964000   76.204    0.000   76.204    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11964000   72.527    0.000   72.527    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11964000   53.577    0.000   53.577    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7982000   48.683    0.000   48.683    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 997000    1.332    0.000   48.085    0.000 loss.py:444(forward)
                 997000    6.031    0.000   46.753    0.000 functional.py:2621(mse_loss)
                1000000    0.868    0.000   43.149    0.000 wrapper.py:25(act)
                1000000    2.225    0.000   42.281    0.000 env.py:197(act)
                1994000   39.832    0.000   39.832    0.000 {built-in method gather}
               59820036   33.505    0.000   39.161    0.000 tensor.py:725(grad)
                1000000   38.742    0.000   38.871    0.000 libenv.py:352(act)
               68844000   34.610    0.000   34.610    0.000 {built-in method torch._C._get_tracing_state}
               59887843   34.294    0.000   34.303    0.000 module.py:758(__getattr__)
                1997007    3.587    0.000   32.499    0.000 <__array_function__ internals>:2(prod)
                1997009    2.468    0.000   28.343    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                2000000    2.920    0.000   26.896    0.000 wrapper.py:22(get_info)
              287349000   26.705    0.000   26.705    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1997007    3.998    0.000   25.874    0.000 fromnumeric.py:2881(prod)
                 997000   25.716    0.000   25.716    0.000 {built-in method torch._C._nn.mse_loss}
                5988776   20.892    0.000   25.541    0.000 module.py:774(__setattr__)
                2000000   13.706    0.000   23.976    0.000 libenv.py:363(get_info)
                7982000    6.359    0.000   22.634    0.000 _overrides.py:779(has_torch_function)
                1997007    7.393    0.000   21.876    0.000 fromnumeric.py:70(_wrapreduction)
               17958005   10.191    0.000   21.062    0.000 {built-in method builtins.any}
               11985000   20.884    0.000   20.884    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
        159635986/159634986   20.080    0.000   20.081    0.000 {built-in method builtins.len}
                1000000    1.715    0.000   19.550    0.000 interop.py:282(render)
                 997000    3.727    0.000   18.376    0.000 __init__.py:25(_make_grads)
                1000000   18.237    0.000   18.237    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1000000   17.777    0.000   17.777    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                1000000    1.897    0.000   17.407    0.000 functional.py:1465(softmax)
                1000000   15.334    0.000   15.334    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 997000   14.991    0.000   14.991    0.000 {built-in method argmax}
                 997000   13.890    0.000   13.890    0.000 {built-in method ones_like}
                    333    0.043    0.000   12.856    0.039 agent.py:53(update_target_network)
                 997000   12.684    0.000   12.684    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000   12.546   12.546 agent.py:16(__init__)
                      3    0.000    0.000   12.517    4.172 module.py:524(to)
                   51/3    0.000    0.000   12.517    4.172 module.py:352(_apply)
                     36    0.000    0.000   12.516    0.348 module.py:602(convert)
                 997000    4.642    0.000   11.922    0.000 functional.py:36(broadcast_tensors)
               11973000    8.534    0.000   11.720    0.000 container.py:107(__iter__)
                    333    3.434    0.010   11.173    0.034 memory.py:28(update_distribution)
                 997000   10.915    0.000   10.915    0.000 memory.py:26(<listcomp>)
                1000666   10.764    0.000   10.764    0.000 {built-in method numpy.array}
                1997340   10.706    0.000   10.706    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                1997008    3.326    0.000   10.189    0.000 numerictypes.py:360(issubdtype)
               23946000    5.765    0.000   10.184    0.000 _overrides.py:792(<genexpr>)
               75799110   10.079    0.000   10.079    0.000 {built-in method builtins.hasattr}
                1000000    8.880    0.000    8.880    0.000 memory.py:13(inner)
                1994000    8.763    0.000    8.763    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                 997000    7.622    0.000    7.622    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3994000    5.733    0.000    6.810    0.000 getlimits.py:366(__new__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8266219: <fruitbot_normalised_0> in cluster <dcc> Done

Job <fruitbot_normalised_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Thu Nov  5 21:40:33 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov  5 22:51:05 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov  5 22:51:05 2020
Terminated at Fri Nov  6 01:18:20 2020
Results reported at Fri Nov  6 01:18:20 2020

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

    CPU time :                                   9138.00 sec.
    Max Memory :                                 25186 MB
    Average Memory :                             22101.28 MB
    Total Requested Memory :                     25600.00 MB
    Delta Memory :                               414.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   8834 sec.
    Turnaround time :                            13067 sec.

The output (if any) is above this job summary.

