[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
Discount_0.995_samp-0 0.995 fruitbot 15.0 200000 100 0.0
    Play for :                  1 games.
    Minutes used :              898 minutes.
    Hours used :                14 hours.

# Profiling


      1687783984 function calls (1655859664 primitive calls) in 53919.96 seconds

##    Ordered by: cumulative time
   List reduced from 1313 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 53919.956 53919.956 {built-in method builtins.exec}
                      1    0.016    0.016 53919.956 53919.956 <string>:1(<module>)
                      1   56.717   56.717 53919.939 53919.939 main.py:14(main)
                 563232   74.399    0.000 51735.112    0.092 agent.py:43(learn)
        34358952/2440772  161.057    0.000 18989.604    0.008 module.py:710(_call_impl)
                1877540   39.587    0.000 18928.592    0.010 agent.py:92(forward)
                5632620   44.915    0.000 17728.972    0.003 container.py:115(forward)
                 563232 1775.780    0.003 17164.624    0.030 memory.py:23(sample)
                 563232   71.232    0.000 15244.756    0.027 helpers.py:12(stack)
                3942972 12966.896    0.003 12966.933    0.003 {method 'to' of 'torch._C._TensorBase' objects}
               11265240   12.069    0.000 12220.260    0.001 activation.py:653(forward)
               11265240   17.929    0.000 12208.191    0.001 functional.py:1277(leaky_relu)
               11265240 12188.388    0.001 12188.388    0.001 {built-in method torch._C._nn.leaky_relu}
                 563232    3.263    0.000 10824.116    0.019 tensor.py:155(backward)
                 563232    4.076    0.000 10820.853    0.019 __init__.py:57(backward)
                 563232 10800.484    0.019 10800.484    0.019 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9387700   18.092    0.000 5118.650    0.001 conv.py:418(forward)
                9387700   19.172    0.000 5089.943    0.001 conv.py:410(_conv_forward)
                9387700 5067.211    0.001 5067.211    0.001 {built-in method conv2d}
                 563232    1.404    0.000 3596.664    0.006 memory.py:75(empty_cache)
                 563232 3594.733    0.006 3594.733    0.006 {built-in method torch._C._cuda_emptyCache}
                3942924 2093.205    0.001 2093.205    0.001 {built-in method cat}
                 563232    3.577    0.000 1085.125    0.002 grad_mode.py:12(decorate_context)
                 563232  254.926    0.000 1077.256    0.002 adam.py:51(step)
                 187844    3.386    0.000  793.831    0.004 agent.py:38(chooseMulti)
                 187844    5.074    0.000  690.638    0.004 environments.py:73(step)
                1877546   91.129    0.000  599.426    0.000 rnn.py:109(flatten_parameters)
                 187844    0.572    0.000  526.870    0.003 agent.py:30(rememberMulti)
                 187844   22.362    0.000  526.299    0.003 agent.py:31(<listcomp>)
               25884575  523.288    0.000  523.288    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                 187844   10.163    0.000  471.155    0.003 agent.py:41(<listcomp>)
                1877540   21.304    0.000  460.496    0.000 rnn.py:550(forward)
                5468224  445.089    0.000  445.089    0.000 {built-in method as_tensor}
                3756880  161.816    0.000  435.070    0.000 exploration.py:28(epsilonGreedy)
                1877540  413.848    0.000  413.848    0.000 {built-in method lstm}
                 187844    3.730    0.000  403.863    0.002 environments.py:75(<listcomp>)
                3778528  103.290    0.000  402.668    0.000 helpers.py:8(clean)
                1877543  399.016    0.000  399.016    0.000 {built-in method _cudnn_rnn_flatten_weight}
                 187844    3.999    0.000  265.501    0.001 environments.py:74(<listcomp>)
                3756880   14.431    0.000  261.502    0.000 interop.py:274(step)
               18023424  212.974    0.000  212.974    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               18023424  190.503    0.000  190.503    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3756880    1.686    0.000  141.607    0.000 wrapper.py:25(act)
                 563232   57.849    0.000  140.793    0.000 random.py:315(sample)
                3756880    5.729    0.000  139.921    0.000 env.py:197(act)
                3756880  130.653    0.000  130.991    0.000 libenv.py:352(act)
                1877540    4.975    0.000  130.558    0.000 linear.py:90(forward)
                1877540   11.122    0.000  123.316    0.000 functional.py:1655(linear)
                9011712  116.113    0.000  116.113    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 563232   16.230    0.000  107.382    0.000 optimizer.py:166(zero_grad)
                9011712   99.102    0.000   99.102    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7511035   87.681    0.000   92.915    0.000 module.py:774(__setattr__)
                9011712   88.640    0.000   88.640    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9011712   85.756    0.000   85.756    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   1878    0.364    0.000   85.435    0.045 agent.py:61(update_target_network)
                1877540   83.065    0.000   83.065    0.000 {built-in method addmm}
                3756880   77.166    0.000   77.166    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                3756880   74.955    0.000   74.955    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                   1878   21.230    0.011   68.666    0.037 memory.py:37(update_distribution)
                9011712   66.439    0.000   66.439    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7535408    6.253    0.000   64.632    0.000 extract_dict_ob.py:9(observe)
              112713459   41.454    0.000   64.400    0.000 random.py:250(_randbelow_with_getrandbits)
                1877540    4.185    0.000   63.772    0.000 pooling.py:156(forward)
                1877540    3.235    0.000   59.588    0.000 _jit_internal.py:237(fn)
                7535408    3.185    0.000   58.379    0.000 wrapper.py:19(observe)
                1877540    3.168    0.000   56.026    0.000 functional.py:564(_max_pool2d)
                7535408   14.854    0.000   55.194    0.000 libenv.py:344(observe)
                3760636   53.907    0.000   53.907    0.000 {built-in method numpy.array}
                1877540   52.630    0.000   52.630    0.000 {built-in method max_pool2d}
               28657479   47.043    0.000   47.043    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7510172   39.484    0.000   44.875    0.000 __init__.py:66(is_acceptable)
                 563232    1.411    0.000   40.312    0.000 loss.py:444(forward)
               11292288   12.021    0.000   39.199    0.000 libenv.py:281(_maybe_copy_dict)
                 563232    5.430    0.000   38.901    0.000 functional.py:2621(mse_loss)
               45058608   30.416    0.000   35.237    0.000 tensor.py:725(grad)
               33878742   34.619    0.000   34.619    0.000 {method 'copy' of 'numpy.ndarray' objects}
                4881544   33.154    0.000   33.154    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                1126464   31.245    0.000   31.245    0.000 {built-in method gather}
               31986107   28.558    0.000   28.595    0.000 module.py:758(__getattr__)
                3756880    2.949    0.000   28.458    0.000 wrapper.py:22(get_info)
               34358952   27.609    0.000   27.609    0.000 {built-in method torch._C._get_tracing_state}
                3756880   25.921    0.000   25.921    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                3756880   13.219    0.000   25.509    0.000 libenv.py:363(get_info)
                 413585    9.849    0.000   23.276    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 563532    1.021    0.000   23.043    0.000 functional.py:68(split)
                 563232   22.869    0.000   22.869    0.000 {built-in method torch._C._nn.mse_loss}
                 563532    1.098    0.000   21.943    0.000 tensor.py:367(split)
                 563532   20.725    0.000   20.725    0.000 {function Tensor.split at 0x7f7470a04790}
                3756880   20.545    0.000   20.545    0.000 memory.py:15(inner)
                1877540   18.232    0.000   18.232    0.000 {method 't' of 'torch._C._TensorBase' objects}
              148645879   16.558    0.000   16.558    0.000 {method 'getrandbits' of '_random.Random' objects}
                 187844    2.262    0.000   16.200    0.000 environments.py:76(<listcomp>)
                 563232    3.706    0.000   16.106    0.000 __init__.py:25(_make_grads)
                1877540    5.329    0.000   16.103    0.000 rnn.py:524(check_forward_args)
        89463211/89462211   14.190    0.000   15.848    0.000 {built-in method builtins.len}
              143068428   14.146    0.000   14.146    0.000 {method 'values' of 'collections.OrderedDict' objects}
               49160134   11.028    0.000   14.061    0.000 {built-in method builtins.isinstance}
                3756900    2.397    0.000   13.954    0.000 environments.py:79(reset)
                1877543    6.801    0.000   13.826    0.000 __init__.py:264(__init__)
                      1    0.000    0.000   13.769   13.769 agent.py:17(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8274473: <Discount_0.995_samp_0> in cluster <dcc> Done

Job <Discount_0.995_samp_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Sat Nov  7 22:13:58 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Nov  8 12:22:41 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sun Nov  8 12:22:41 2020
Terminated at Mon Nov  9 03:21:30 2020
Results reported at Mon Nov  9 03:21:30 2020

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

    CPU time :                                   16795.00 sec.
    Max Memory :                                 24834 MB
    Average Memory :                             24067.36 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5886.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   54022 sec.
    Turnaround time :                            104852 sec.

The output (if any) is above this job summary.

