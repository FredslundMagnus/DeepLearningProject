test_3-0 MME 0.12 0.3 0.0001 0.0
    Play for :                  1 games.
    Minutes used :              57 minutes.
    Hours used :                0 hours.

# Profiling


      135852342 function calls (130701927 primitive calls) in 3448.91 seconds

##    Ordered by: cumulative time
   List reduced from 1291 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   84/1    0.001    0.000 3448.912 3448.912 {built-in method builtins.exec}
                      1    0.000    0.000 3448.912 3448.912 <string>:1(<module>)
                      1   13.369   13.369 3448.912 3448.912 main.py:12(main)
                 105358    9.484    0.000 3281.876    0.031 agent.py:33(learn)
         5648974/531790   20.957    0.000 1538.106    0.003 module.py:710(_call_impl)
                 426432    2.543    0.000 1529.884    0.004 agent.py:99(forward)
                 852864    5.778    0.000 1520.512    0.002 container.py:115(forward)
                1705728    1.453    0.000 1334.533    0.001 activation.py:653(forward)
                1705728    2.455    0.000 1333.080    0.001 functional.py:1277(leaky_relu)
                1705728 1330.388    0.001 1330.388    0.001 {built-in method torch._C._nn.leaky_relu}
                 105358    0.243    0.000 1261.911    0.012 memory.py:75(empty_cache)
                 105358 1261.586    0.012 1261.586    0.012 {built-in method torch._C._cuda_emptyCache}
                 105358    1.142    0.000  215.018    0.002 memory.py:25(sample_distribution)
                 105358    0.378    0.000  193.868    0.002 tensor.py:155(backward)
                 105358    0.418    0.000  193.490    0.002 __init__.py:57(backward)
                 105358  191.083    0.002  191.083    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 105358    3.413    0.000  157.732    0.001 helpers.py:11(stack)
                1705728    3.042    0.000  112.601    0.000 conv.py:418(forward)
                1705728    2.962    0.000  108.484    0.000 conv.py:410(_conv_forward)
                1705728  104.987    0.000  104.987    0.000 {built-in method conv2d}
                 105358    0.521    0.000  101.967    0.001 grad_mode.py:12(decorate_context)
                 105358   24.984    0.000  100.745    0.001 adam.py:51(step)
                 742542   91.087    0.000   91.181    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                 110358    0.813    0.000   87.426    0.001 agent.py:28(choose)
                 632148   72.825    0.000   72.825    0.000 {built-in method cat}
                 215716   59.212    0.000   64.106    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 852864    1.895    0.000   45.792    0.000 linear.py:90(forward)
                 852864    3.560    0.000   43.216    0.000 functional.py:1655(linear)
                 852864   30.658    0.000   30.658    0.000 {built-in method addmm}
                 110358    8.690    0.000   26.282    0.000 exploration.py:19(softmax)
                 427432   18.999    0.000   18.999    0.000 {built-in method as_tensor}
                2528592   18.926    0.000   18.926    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2528592   16.766    0.000   16.766    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 772506   15.444    0.000   15.444    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                 110358    0.677    0.000   13.547    0.000 interop.py:274(step)
                      1    0.000    0.000   12.858   12.858 agent.py:16(__init__)
                      3    0.000    0.000   12.841    4.280 module.py:524(to)
                   39/3    0.000    0.000   12.841    4.280 module.py:352(_apply)
                     36    0.000    0.000   12.840    0.357 module.py:602(convert)
                1264296   11.693    0.000   11.693    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 111358    0.243    0.000   10.086    0.000 helpers.py:7(clean)
                 105358    1.675    0.000    9.585    0.000 optimizer.py:166(zero_grad)
                1264296    9.469    0.000    9.469    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1264296    8.011    0.000    8.011    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1264296    7.587    0.000    7.587    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 442432    0.856    0.000    6.812    0.000 libenv.py:281(_maybe_copy_dict)
                 221716    0.356    0.000    6.792    0.000 extract_dict_ob.py:9(observe)
                 221716    0.127    0.000    6.436    0.000 wrapper.py:19(observe)
                 221716    0.531    0.000    6.309    0.000 libenv.py:344(observe)
                1327318    6.136    0.000    6.136    0.000 {method 'copy' of 'numpy.ndarray' objects}
                1264296    5.521    0.000    5.521    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 852864    5.182    0.000    5.182    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 105358    0.140    0.000    4.875    0.000 loss.py:444(forward)
                 105358    0.577    0.000    4.735    0.000 functional.py:2621(mse_loss)
                 110358    0.075    0.000    4.584    0.000 wrapper.py:25(act)
                 110358    0.230    0.000    4.509    0.000 env.py:197(act)
                 220716    0.552    0.000    4.383    0.000 wrapper.py:22(get_info)
                 110358    4.151    0.000    4.163    0.000 libenv.py:352(act)
                 210716    4.002    0.000    4.002    0.000 {built-in method gather}
                6321516    3.252    0.000    3.838    0.000 tensor.py:725(grad)
                 220716    2.161    0.000    3.831    0.000 libenv.py:363(get_info)
                 110358    0.255    0.000    3.678    0.000 interop.py:282(render)
                5971370    3.329    0.000    3.330    0.000 module.py:758(__getattr__)
                5648974    3.215    0.000    3.215    0.000 {built-in method torch._C._get_tracing_state}
                 637148    3.207    0.000    3.207    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                 642759    2.556    0.000    3.131    0.000 module.py:774(__setattr__)
                 215723    0.335    0.000    3.120    0.000 <__array_function__ internals>:2(prod)
                      1    0.000    0.000    2.819    2.819 environments.py:48(__getattribute__)
                      1    0.000    0.000    2.819    2.819 registration.py:144(make)
                      1    0.000    0.000    2.819    2.819 registration.py:84(make)
                 215725    0.244    0.000    2.733    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                      1    0.000    0.000    2.661    2.661 registration.py:50(make)
                      1    0.000    0.000    2.661    2.661 gym_registration.py:6(make_env)
                      1    0.000    0.000    2.661    2.661 env.py:207(__init__)
                      1    0.000    0.000    2.661    2.661 env.py:71(__init__)
                      1    2.492    2.492    2.658    2.658 libenv.py:64(__init__)
                 105358    2.628    0.000    2.628    0.000 {built-in method torch._C._nn.mse_loss}
                 215723    0.386    0.000    2.489    0.000 fromnumeric.py:2881(prod)
                 852864    0.726    0.000    2.487    0.000 _overrides.py:779(has_torch_function)
                1916449    1.099    0.000    2.254    0.000 {built-in method builtins.any}
               23448760    2.128    0.000    2.128    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 215723    0.733    0.000    2.103    0.000 fromnumeric.py:70(_wrapreduction)
                1299296    2.080    0.000    2.080    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 105358    0.396    0.000    1.955    0.000 __init__.py:25(_make_grads)
                 110358    1.918    0.000    1.918    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                 110358    1.864    0.000    1.864    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                 110358    0.200    0.000    1.769    0.000 functional.py:1465(softmax)
                 105358    1.644    0.000    1.644    0.000 {built-in method argmax}
        12780686/12779686    1.635    0.000    1.635    0.000 {built-in method builtins.len}
                 110358    1.551    0.000    1.551    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 105358    1.482    0.000    1.482    0.000 {built-in method ones_like}
                 105358    1.293    0.000    1.293    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                 105358    0.481    0.000    1.237    0.000 functional.py:36(broadcast_tensors)
                2558592    0.645    0.000    1.087    0.000 _overrides.py:792(<genexpr>)
                 215724    0.343    0.000    1.061    0.000 numerictypes.py:360(issubdtype)
                8029117    1.029    0.000    1.029    0.000 {built-in method builtins.hasattr}
                 215745    1.025    0.000    1.025    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                 852864    0.765    0.000    1.011    0.000 container.py:107(__iter__)
                 105358    0.945    0.000    0.945    0.000 memory.py:26(<listcomp>)
                 105358    0.768    0.000    0.768    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8253841: <test_3_0> in cluster <dcc> Done

Job <test_3_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Mon Nov  2 19:39:34 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 19:51:27 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 19:51:27 2020
Terminated at Mon Nov  2 20:49:02 2020
Results reported at Mon Nov  2 20:49:02 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=20G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 60
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   936.00 sec.
    Max Memory :                                 12174 MB
    Average Memory :                             8215.54 MB
    Total Requested Memory :                     20480.00 MB
    Delta Memory :                               8306.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   3456 sec.
    Turnaround time :                            4168 sec.

The output (if any) is above this job summary.

