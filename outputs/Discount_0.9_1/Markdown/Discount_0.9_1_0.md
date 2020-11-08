[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
Discount_0.9_1-0 0.9 fruitbot 20.0 200000 100
    Play for :                  1 games.
    Minutes used :              1198 minutes.
    Hours used :                19 hours.

# Profiling


      2488313233 function calls (2422695609 primitive calls) in 71918.58 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 71918.584 71918.584 {built-in method builtins.exec}
                      1    0.020    0.020 71918.584 71918.584 <string>:1(<module>)
                      1  104.495  104.495 71918.562 71918.562 main.py:16(main)
                1157820  119.449    0.000 67990.554    0.059 agent.py:45(learn)
                1157820    5.795    0.000 23865.214    0.021 tensor.py:155(backward)
                1157820    7.320    0.000 23859.419    0.021 __init__.py:57(backward)
                1157820 23824.399    0.021 23824.399    0.021 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1157820   70.608    0.000 23733.723    0.020 memory.py:27(sample_distribution)
                1157820   87.152    0.000 23362.093    0.020 helpers.py:12(stack)
                8105088 19336.794    0.002 19336.870    0.002 {method 'to' of 'torch._C._TensorBase' objects}
                1157820    2.276    0.000 14012.485    0.012 memory.py:75(empty_cache)
                1157820 14009.248    0.012 14009.248    0.012 {built-in method torch._C._cuda_emptyCache}
        70628820/5017320  286.045    0.000 4712.194    0.001 module.py:710(_call_impl)
                3859500   72.181    0.000 4604.764    0.001 agent.py:94(forward)
                8105040 3748.875    0.000 3748.875    0.000 {built-in method cat}
               11578500   71.833    0.000 2582.811    0.000 container.py:115(forward)
                1157820    6.682    0.000 1594.418    0.001 grad_mode.py:12(decorate_context)
                1157820  397.340    0.000 1579.303    0.001 adam.py:51(step)
               19297500   31.393    0.000 1521.946    0.000 conv.py:418(forward)
               19297500   37.851    0.000 1476.429    0.000 conv.py:410(_conv_forward)
               19297500 1431.584    0.000 1431.584    0.000 {built-in method conv2d}
                 386040    6.806    0.000 1381.570    0.004 agent.py:40(chooseMulti)
                 386040   10.890    0.000 1315.380    0.003 environments.py:73(step)
                3859506  161.053    0.000  940.919    0.000 rnn.py:109(flatten_parameters)
               53433299  913.520    0.000  913.520    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                 386040    1.156    0.000  898.734    0.002 agent.py:32(rememberMulti)
                 386040   31.220    0.000  897.578    0.002 agent.py:33(<listcomp>)
                3859500   38.716    0.000  822.390    0.000 rnn.py:550(forward)
                 386040   16.125    0.000  811.159    0.002 agent.py:43(<listcomp>)
               11282398  786.631    0.000  786.631    0.000 {built-in method as_tensor}
                7808938  208.015    0.000  756.551    0.000 helpers.py:8(clean)
                 386040    7.255    0.000  754.115    0.002 environments.py:75(<listcomp>)
                7720800  291.883    0.000  753.133    0.000 exploration.py:28(epsilonGreedy)
                3859500  737.473    0.000  737.473    0.000 {built-in method lstm}
                3859503  593.735    0.000  593.735    0.000 {built-in method _cudnn_rnn_flatten_weight}
                 386040    7.705    0.000  513.403    0.001 environments.py:74(<listcomp>)
                7720800   28.271    0.000  505.698    0.000 interop.py:274(step)
               23157000   22.624    0.000  392.013    0.000 activation.py:653(forward)
               23157000   33.055    0.000  369.389    0.000 functional.py:1277(leaky_relu)
               23157000  333.206    0.000  333.206    0.000 {built-in method torch._C._nn.leaky_relu}
               37050240  292.985    0.000  292.985    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                7720800    3.707    0.000  275.371    0.000 wrapper.py:25(act)
                7720800    9.588    0.000  271.664    0.000 env.py:197(act)
               37050240  260.751    0.000  260.751    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7720800  256.423    0.000  257.145    0.000 libenv.py:352(act)
                3859500   10.574    0.000  227.568    0.000 linear.py:90(forward)
                3859500   19.768    0.000  212.017    0.000 functional.py:1655(linear)
                   3860    0.751    0.000  186.984    0.048 agent.py:63(update_target_network)
               18525120  178.039    0.000  178.039    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               15438875  163.940    0.000  175.162    0.000 module.py:774(__setattr__)
                1157820  119.012    0.000  158.276    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                   3860   47.616    0.012  154.680    0.040 memory.py:37(update_distribution)
               18525120  148.363    0.000  148.363    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1157820   25.015    0.000  145.085    0.000 optimizer.py:166(zero_grad)
                3859500  141.079    0.000  141.079    0.000 {built-in method addmm}
               18525120  127.887    0.000  127.887    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                7720800  126.259    0.000  126.259    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               15529738   11.042    0.000  125.056    0.000 extract_dict_ob.py:9(observe)
                7720800  121.539    0.000  121.539    0.000 {method 'std' of 'torch._C._TensorBase' objects}
               18525120  120.115    0.000  120.115    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8885740  119.585    0.000  119.585    0.000 {built-in method numpy.array}
               15529738    6.808    0.000  114.014    0.000 wrapper.py:19(observe)
                3859500    8.523    0.000  108.183    0.000 pooling.py:156(forward)
               15529738   28.846    0.000  107.206    0.000 libenv.py:344(observe)
                3859500    6.268    0.000   99.660    0.000 _jit_internal.py:237(fn)
                3859500    6.363    0.000   92.780    0.000 functional.py:564(_max_pool2d)
                3859500   85.970    0.000   85.970    0.000 {built-in method max_pool2d}
               18525120   81.848    0.000   81.848    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               23250538   23.713    0.000   78.205    0.000 libenv.py:281(_maybe_copy_dict)
               15438012   64.853    0.000   74.234    0.000 __init__.py:66(is_acceptable)
                1157820    2.603    0.000   70.668    0.000 loss.py:444(forward)
                1157820   10.460    0.000   68.065    0.000 functional.py:2621(mse_loss)
                1157220   67.607    0.000   67.607    0.000 memory.py:35(<listcomp>)
               69755474   67.234    0.000   67.234    0.000 {method 'copy' of 'numpy.ndarray' objects}
               59046163   66.189    0.000   66.189    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               92625648   52.742    0.000   62.027    0.000 tensor.py:725(grad)
                7720800    6.171    0.000   55.782    0.000 wrapper.py:22(get_info)
               10034640   53.480    0.000   53.480    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               65750779   52.449    0.000   52.528    0.000 module.py:758(__getattr__)
                2315640   49.980    0.000   49.980    0.000 {built-in method gather}
                7720800   25.557    0.000   49.610    0.000 libenv.py:363(get_info)
                1158120    2.075    0.000   45.425    0.000 functional.py:68(split)
                1158120    2.118    0.000   43.196    0.000 tensor.py:367(split)
                2382562    4.232    0.000   42.252    0.000 <__array_function__ internals>:2(prod)
                7720800   41.901    0.000   41.901    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7720800   41.439    0.000   41.439    0.000 memory.py:15(inner)
               70628820   41.343    0.000   41.343    0.000 {built-in method torch._C._get_tracing_state}
                1158120   40.865    0.000   40.865    0.000 {function Tensor.split at 0x7fb0229f6790}
                3543642   38.497    0.000   38.497    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                1157221   38.371    0.000   38.371    0.000 {built-in method numpy.arange}
                1157820   38.030    0.000   38.030    0.000 {built-in method torch._C._nn.mse_loss}
                2382602    3.168    0.000   37.469    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                 386040    4.344    0.000   36.972    0.000 environments.py:76(<listcomp>)
                 612301   14.856    0.000   34.606    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2382562    5.739    0.000   34.302    0.000 fromnumeric.py:2881(prod)
                7720820    4.769    0.000   32.645    0.000 environments.py:79(reset)
                3859500   10.609    0.000   30.996    0.000 rnn.py:524(check_forward_args)
                3859500   28.985    0.000   28.985    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2382562    9.115    0.000   28.563    0.000 fromnumeric.py:70(_wrapreduction)
              294093780   27.868    0.000   27.868    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8273877: <Discount_0.9_1_0> in cluster <dcc> Done

Job <Discount_0.9_1_0> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Sat Nov  7 15:36:09 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov  7 15:49:52 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov  7 15:49:52 2020
Terminated at Sun Nov  8 11:48:40 2020
Results reported at Sun Nov  8 11:48:40 2020

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

    CPU time :                                   24114.00 sec.
    Max Memory :                                 24936 MB
    Average Memory :                             24460.96 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5784.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   71927 sec.
    Turnaround time :                            72751 sec.

The output (if any) is above this job summary.

