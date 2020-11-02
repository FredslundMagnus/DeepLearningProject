/zhome/ee/d/137643/.lsbatch/1604335277.8253410.shell: line 14: 94460 Killed                  python main.py $LSB_PROJECT_NAME

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 8253410: <Discount_0.70_0> in cluster <dcc> Exited

Job <Discount_0.70_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Nov  2 17:41:17 2020
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 17:41:19 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 17:41:19 2020
Terminated at Mon Nov  2 17:41:43 2020
Results reported at Mon Nov  2 17:41:43 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=1G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 10
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

TERM_MEMLIMIT: job killed after reaching LSF memory usage limit.
Exited with exit code 137.

Resource usage summary:

    CPU time :                                   3.00 sec.
    Max Memory :                                 1024 MB
    Average Memory :                             717.67 MB
    Total Requested Memory :                     1024.00 MB
    Delta Memory :                               0.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   117 sec.
    Turnaround time :                            26 sec.

The output (if any) is above this job summary.

User defined signal 2

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8253415: <Discount_0.70_0> in cluster <dcc> Exited

Job <Discount_0.70_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Nov  2 17:46:22 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 17:46:24 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 17:46:24 2020
Terminated at Mon Nov  2 17:56:40 2020
Results reported at Mon Nov  2 17:56:40 2020

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

TERM_RUNLIMIT: job killed after reaching LSF run time limit.
Exited with exit code 140.

Resource usage summary:

    CPU time :                                   581.00 sec.
    Max Memory :                                 9868 MB
    Average Memory :                             5793.50 MB
    Total Requested Memory :                     10240.00 MB
    Delta Memory :                               372.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   655 sec.
    Turnaround time :                            618 sec.

The output (if any) is above this job summary.

Discount_0.70-0 MME 0.12 0.3 0.0001 0.0
cuda
    Play for :                  1 games.
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      3154219 function calls (3031228 primitive calls) in 27.68 seconds

##    Ordered by: cumulative time
   List reduced from 1259 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   84/1    0.000    0.000   27.675   27.675 {built-in method builtins.exec}
                      1    0.025    0.025   27.675   27.675 <string>:1(<module>)
                      1    0.307    0.307   27.651   27.651 main.py:14(main)
                  13457   10.105    0.001   10.109    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    9.038    9.038 agent.py:16(__init__)
                      3    0.000    0.000    9.022    3.007 module.py:524(to)
                   39/3    0.000    0.000    9.022    3.007 module.py:352(_apply)
                     36    0.000    0.000    9.021    0.251 module.py:602(convert)
                   1203    0.131    0.000    7.552    0.006 agent.py:33(learn)
           128759/11015    0.512    0.000    6.205    0.001 module.py:710(_call_impl)
                   9812    0.064    0.000    6.056    0.001 agent.py:99(forward)
                  19624    0.149    0.000    5.821    0.000 container.py:115(forward)
                   6203    0.041    0.000    5.756    0.001 agent.py:28(choose)
                  39248    0.071    0.000    3.170    0.000 conv.py:418(forward)
                  39248    0.070    0.000    3.074    0.000 conv.py:410(_conv_forward)
                  39248    2.992    0.000    2.992    0.000 {built-in method conv2d}
                      1    0.000    0.000    2.218    2.218 environments.py:48(__getattribute__)
                      1    0.000    0.000    2.218    2.218 registration.py:144(make)
                      1    0.000    0.000    2.218    2.218 registration.py:84(make)
                      1    0.000    0.000    2.117    2.117 registration.py:50(make)
                      1    0.000    0.000    2.117    2.117 gym_registration.py:6(make_env)
                      1    0.000    0.000    2.117    2.117 env.py:207(__init__)
                      1    0.000    0.000    2.117    2.117 env.py:71(__init__)
                      1    2.008    2.008    2.115    2.115 libenv.py:64(__init__)
                   1203    0.013    0.000    1.936    0.002 memory.py:25(sample_distribution)
                   1203    0.007    0.000    1.797    0.001 grad_mode.py:12(decorate_context)
                   1203    0.412    0.000    1.782    0.001 adam.py:51(step)
                   1203    0.040    0.000    1.766    0.001 helpers.py:11(stack)
                   6203    0.562    0.000    1.715    0.000 exploration.py:19(softmax)
                  19624    0.042    0.000    1.195    0.000 linear.py:90(forward)
                  19624    0.090    0.000    1.137    0.000 functional.py:1655(linear)
                   1203    0.005    0.000    1.052    0.001 tensor.py:155(backward)
                   1203    0.006    0.000    1.047    0.001 __init__.py:57(backward)
                  43421    1.030    0.000    1.030    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                   1203    1.012    0.001    1.012    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                   9862    0.929    0.000    0.929    0.000 {built-in method as_tensor}
                   6253    0.015    0.000    0.823    0.000 helpers.py:7(clean)
                  19624    0.808    0.000    0.808    0.000 {built-in method addmm}
                  39248    0.038    0.000    0.759    0.000 activation.py:653(forward)
                   7218    0.724    0.000    0.724    0.000 {built-in method cat}
                  39248    0.057    0.000    0.722    0.000 functional.py:1277(leaky_relu)
                   7406    0.509    0.000    0.691    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                  39248    0.659    0.000    0.659    0.000 {built-in method torch._C._nn.leaky_relu}
                   6203    0.041    0.000    0.611    0.000 interop.py:274(step)
                  28872    0.352    0.000    0.352    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                  28872    0.321    0.000    0.321    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   6203    0.005    0.000    0.262    0.000 wrapper.py:25(act)
                   6203    0.014    0.000    0.257    0.000 env.py:197(act)
                   6203    0.235    0.000    0.235    0.000 libenv.py:352(act)
                  12456    0.022    0.000    0.207    0.000 extract_dict_ob.py:9(observe)
                  14436    0.201    0.000    0.201    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                      6    0.000    0.000    0.197    0.033 __init__.py:1(<module>)
                  12456    0.008    0.000    0.185    0.000 wrapper.py:19(observe)
                   1203    0.027    0.000    0.179    0.000 optimizer.py:166(zero_grad)
                  12456    0.035    0.000    0.177    0.000 libenv.py:344(observe)
                  14436    0.168    0.000    0.168    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  24862    0.037    0.000    0.166    0.000 libenv.py:281(_maybe_copy_dict)
                  12406    0.014    0.000    0.157    0.000 wrapper.py:22(get_info)
                  19624    0.151    0.000    0.151    0.000 {method 't' of 'torch._C._TensorBase' objects}
                  74587    0.145    0.000    0.145    0.000 {method 'copy' of 'numpy.ndarray' objects}
                  14436    0.144    0.000    0.144    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                  12406    0.082    0.000    0.143    0.000 libenv.py:363(get_info)
                   6203    0.142    0.000    0.142    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                  14436    0.141    0.000    0.141    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   6203    0.140    0.000    0.140    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                   85/7    0.000    0.000    0.140    0.020 <frozen importlib._bootstrap>:986(_find_and_load)
                   84/6    0.000    0.000    0.140    0.023 <frozen importlib._bootstrap>:956(_find_and_load_unlocked)
                   6203    0.014    0.000    0.139    0.000 functional.py:1465(softmax)
                   81/5    0.000    0.000    0.135    0.027 <frozen importlib._bootstrap>:650(_load_unlocked)
                   79/4    0.000    0.000    0.129    0.032 <frozen importlib._bootstrap_external>:777(exec_module)
                  113/6    0.000    0.000    0.126    0.021 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
                   6203    0.124    0.000    0.124    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                   7413    0.012    0.000    0.118    0.000 <__array_function__ internals>:2(prod)
                  49436    0.113    0.000    0.113    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                  14436    0.112    0.000    0.112    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   7415    0.008    0.000    0.103    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                      2    0.000    0.000    0.101    0.050 __init__.py:109(import_module)
                      2    0.000    0.000    0.101    0.050 <frozen importlib._bootstrap>:1002(_gcd_import)
                      1    0.000    0.000    0.101    0.101 registration.py:105(spec)
                   6203    0.008    0.000    0.100    0.000 interop.py:282(render)
                 128759    0.097    0.000    0.097    0.000 {built-in method torch._C._get_tracing_state}
                   7413    0.015    0.000    0.095    0.000 fromnumeric.py:2881(prod)
                      2    0.000    0.000    0.093    0.047 env.py:1(<module>)
                   7413    0.027    0.000    0.080    0.000 fromnumeric.py:70(_wrapreduction)
                   30/5    0.000    0.000    0.079    0.016 {built-in method builtins.__import__}
                  88/21    0.000    0.000    0.078    0.004 <frozen importlib._bootstrap>:1017(_handle_fromlist)
                 137558    0.077    0.000    0.077    0.000 module.py:758(__getattr__)
                  12218    0.076    0.000    0.076    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                  17829    0.060    0.000    0.074    0.000 module.py:774(__setattr__)
                   1203    0.002    0.000    0.070    0.000 loss.py:444(forward)
                   1203    0.008    0.000    0.069    0.000 functional.py:2621(mse_loss)
                     79    0.001    0.000    0.065    0.001 <frozen importlib._bootstrap_external>:849(get_code)
                   2406    0.060    0.000    0.060    0.000 {built-in method gather}
                     79    0.001    0.000    0.058    0.001 <frozen importlib._bootstrap_external>:969(get_data)
                  19624    0.017    0.000    0.057    0.000 _overrides.py:779(has_torch_function)
                  72216    0.048    0.000    0.056    0.000 tensor.py:725(grad)
                      1    0.000    0.000    0.052    0.052 video_recorder.py:1(<module>)
                  41659    0.025    0.000    0.050    0.000 {built-in method builtins.any}
                      1    0.000    0.000    0.049    0.049 __init__.py:8(<module>)
                 534660    0.049    0.000    0.049    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 8253534: <Discount_0.70_0> in cluster <dcc> Done

Job <Discount_0.70_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Nov  2 18:03:31 2020
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov  2 18:03:33 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov  2 18:03:33 2020
Terminated at Mon Nov  2 18:04:04 2020
Results reported at Mon Nov  2 18:04:04 2020

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

    CPU time :                                   23.00 sec.
    Max Memory :                                 2080 MB
    Average Memory :                             2080.00 MB
    Total Requested Memory :                     10240.00 MB
    Delta Memory :                               8160.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   72 sec.
    Turnaround time :                            33 sec.

The output (if any) is above this job summary.

