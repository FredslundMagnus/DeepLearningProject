[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
Discount_0.95_1-0 0.95 fruitbot 20.0 200000 100
    Play for :                  1 games.
    Minutes used :              1198 minutes.
    Hours used :                19 hours.

# Profiling


      2013074422 function calls (1960000758 primitive calls) in 71910.97 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 71910.974 71910.974 {built-in method builtins.exec}
                      1    0.021    0.021 71910.974 71910.974 <string>:1(<module>)
                      1   94.933   94.933 71910.952 71910.952 main.py:16(main)
                 936456  115.312    0.000 68150.305    0.073 agent.py:45(learn)
        57125616/4058076  254.026    0.000 18890.785    0.005 module.py:710(_call_impl)
                3121620   64.848    0.000 18792.828    0.006 agent.py:94(forward)
                 936456   60.588    0.000 17651.871    0.019 memory.py:27(sample_distribution)
                 936456    5.046    0.000 17636.496    0.019 tensor.py:155(backward)
                 936456    6.153    0.000 17631.450    0.019 __init__.py:57(backward)
                 936456 17598.666    0.019 17598.666    0.019 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 936456   79.830    0.000 17321.373    0.018 helpers.py:12(stack)
                9364860   72.803    0.000 16876.081    0.002 container.py:115(forward)
                6555540 13915.841    0.002 13915.858    0.002 {method 'to' of 'torch._C._TensorBase' objects}
                 936456    2.310    0.000 12147.767    0.013 memory.py:75(empty_cache)
                 936456 12144.584    0.013 12144.584    0.013 {built-in method torch._C._cuda_emptyCache}
               18729720   18.315    0.000 11110.073    0.001 activation.py:653(forward)
               18729720   30.824    0.000 11091.759    0.001 functional.py:1277(leaky_relu)
               18729720 11058.397    0.001 11058.397    0.001 {built-in method torch._C._nn.leaky_relu}
               15608100   29.572    0.000 5134.788    0.000 conv.py:418(forward)
               15608100   32.125    0.000 5092.332    0.000 conv.py:410(_conv_forward)
               15608100 5054.678    0.000 5054.678    0.000 {built-in method conv2d}
                6555492 3160.156    0.000 3160.156    0.000 {built-in method cat}
                 936456    6.391    0.000 1799.528    0.002 grad_mode.py:12(decorate_context)
                 936456  423.567    0.000 1786.137    0.002 adam.py:51(step)
                 312252    5.665    0.000 1414.964    0.005 agent.py:40(chooseMulti)
                 312252    9.031    0.000 1171.557    0.004 environments.py:73(step)
                3121626  147.043    0.000  961.748    0.000 rnn.py:109(flatten_parameters)
                 312252    0.917    0.000  899.226    0.003 agent.py:32(rememberMulti)
                 312252   39.069    0.000  898.308    0.003 agent.py:33(<listcomp>)
               43179108  891.172    0.000  891.172    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                 312252   16.997    0.000  795.543    0.003 agent.py:43(<listcomp>)
                6245040  272.760    0.000  734.474    0.000 exploration.py:28(epsilonGreedy)
                3121620   33.637    0.000  727.962    0.000 rnn.py:550(forward)
                9116904  712.870    0.000  712.870    0.000 {built-in method as_tensor}
                6307536  173.320    0.000  676.589    0.000 helpers.py:8(clean)
                 312252    6.039    0.000  675.226    0.002 environments.py:75(<listcomp>)
                3121620  654.101    0.000  654.101    0.000 {built-in method lstm}
                3121623  648.453    0.000  648.453    0.000 {built-in method _cudnn_rnn_flatten_weight}
                 312252    6.920    0.000  454.073    0.001 environments.py:74(<listcomp>)
                6245040   25.670    0.000  447.153    0.000 interop.py:274(step)
               29966592  352.759    0.000  352.759    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               29966592  315.692    0.000  315.692    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6245040    3.059    0.000  242.274    0.000 wrapper.py:25(act)
                6245040    9.542    0.000  239.215    0.000 env.py:197(act)
                6245040  223.120    0.000  223.756    0.000 libenv.py:352(act)
                3121620    8.602    0.000  212.471    0.000 linear.py:90(forward)
                3121620   17.548    0.000  200.294    0.000 functional.py:1655(linear)
               14983296  194.182    0.000  194.182    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 936456   27.507    0.000  179.051    0.000 optimizer.py:166(zero_grad)
               14983296  163.372    0.000  163.372    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   3122    0.616    0.000  149.310    0.048 agent.py:63(update_target_network)
                 936456  110.423    0.000  146.112    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               14983296  145.807    0.000  145.807    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12487355  136.969    0.000  145.439    0.000 module.py:774(__setattr__)
               14983296  141.791    0.000  141.791    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3121620  134.165    0.000  134.165    0.000 {built-in method addmm}
                6245040  129.383    0.000  129.383    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                6245040  127.602    0.000  127.602    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                   3122   37.513    0.012  120.070    0.038 memory.py:37(update_distribution)
               12552576   10.531    0.000  110.025    0.000 extract_dict_ob.py:9(observe)
               14983296  110.020    0.000  110.020    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3121620    6.181    0.000  102.867    0.000 pooling.py:156(forward)
               12552576    5.192    0.000   99.495    0.000 wrapper.py:19(observe)
                3121620    5.230    0.000   96.686    0.000 _jit_internal.py:237(fn)
                7187140   94.977    0.000   94.977    0.000 {built-in method numpy.array}
               12552576   25.525    0.000   94.303    0.000 libenv.py:344(observe)
                3121620    5.097    0.000   90.956    0.000 functional.py:564(_max_pool2d)
                3121620   85.510    0.000   85.510    0.000 {built-in method max_pool2d}
               47736436   79.772    0.000   79.772    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               12486492   61.576    0.000   69.912    0.000 __init__.py:66(is_acceptable)
                 936456    2.027    0.000   66.409    0.000 loss.py:444(forward)
               18797616   20.261    0.000   66.322    0.000 libenv.py:281(_maybe_copy_dict)
                 936456    8.488    0.000   64.382    0.000 functional.py:2621(mse_loss)
               74916528   51.601    0.000   59.555    0.000 tensor.py:725(grad)
               56395970   58.712    0.000   58.712    0.000 {method 'copy' of 'numpy.ndarray' objects}
                 935856   55.349    0.000   55.349    0.000 memory.py:35(<listcomp>)
                8116152   54.585    0.000   54.585    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                1872912   50.503    0.000   50.503    0.000 {built-in method gather}
                6245040    5.008    0.000   48.416    0.000 wrapper.py:22(get_info)
               57125616   45.721    0.000   45.721    0.000 {built-in method torch._C._get_tracing_state}
                6245040   44.073    0.000   44.073    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6245040   22.824    0.000   43.408    0.000 libenv.py:363(get_info)
               53180251   41.538    0.000   41.603    0.000 module.py:758(__getattr__)
                 936756    1.837    0.000   39.591    0.000 functional.py:68(split)
                2008940    3.837    0.000   38.767    0.000 <__array_function__ internals>:2(prod)
                2947918   38.482    0.000   38.482    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                 936456   38.311    0.000   38.311    0.000 {built-in method torch._C._nn.mse_loss}
                 936756    1.793    0.000   37.628    0.000 tensor.py:367(split)
                6245040   37.485    0.000   37.485    0.000 memory.py:15(inner)
                 936756   35.641    0.000   35.641    0.000 {function Tensor.split at 0x7fc37b5de790}
                2008980    2.877    0.000   34.412    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                 312252    3.937    0.000   33.227    0.000 environments.py:76(<listcomp>)
                 536172   14.481    0.000   33.198    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 935857   33.002    0.000   33.002    0.000 {built-in method numpy.arange}
                2008940    4.896    0.000   31.535    0.000 fromnumeric.py:2881(prod)
                6245060    4.439    0.000   29.294    0.000 environments.py:79(reset)
                3121620   29.181    0.000   29.181    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2008940    7.697    0.000   26.639    0.000 fromnumeric.py:70(_wrapreduction)
                 938978    2.322    0.000   26.639    0.000 {method 'sum' of 'numpy.ndarray' objects}
                 936456    5.783    0.000   26.342    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8273878: <Discount_0.95_1_0> in cluster <dcc> Done

Job <Discount_0.95_1_0> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Sat Nov  7 15:36:09 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov  7 15:50:12 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov  7 15:50:12 2020
Terminated at Sun Nov  8 11:48:48 2020
Results reported at Sun Nov  8 11:48:48 2020

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

    CPU time :                                   23765.00 sec.
    Max Memory :                                 24822 MB
    Average Memory :                             24266.29 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5898.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   71917 sec.
    Turnaround time :                            72759 sec.

The output (if any) is above this job summary.

