[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
Discount_0.995_dist-0 0.995 fruitbot 15.0 200000 100 1.0
    Play for :                  1 games.
    Minutes used :              898 minutes.
    Hours used :                14 hours.

# Profiling


      1731709058 function calls (1686051814 primitive calls) in 53913.77 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 53913.769 53913.769 {built-in method builtins.exec}
                      1    0.018    0.018 53913.769 53913.769 <string>:1(<module>)
                      1   74.176   74.176 53913.750 53913.750 main.py:14(main)
                 805578   83.326    0.000 50961.516    0.063 agent.py:43(learn)
                 805578   48.366    0.000 16256.487    0.020 memory.py:27(sample_distribution)
                 805578   67.342    0.000 15998.444    0.020 helpers.py:12(stack)
        49142058/3490938  209.290    0.000 14341.318    0.004 module.py:710(_call_impl)
                2685360   51.855    0.000 14265.480    0.005 agent.py:92(forward)
                5639394 12857.801    0.002 12857.807    0.002 {method 'to' of 'torch._C._TensorBase' objects}
                8056080   52.152    0.000 12842.988    0.002 container.py:115(forward)
                 805578    1.755    0.000 10065.019    0.012 memory.py:75(empty_cache)
                 805578 10062.604    0.012 10062.604    0.012 {built-in method torch._C._cuda_emptyCache}
                 805578    4.298    0.000 9091.540    0.011 tensor.py:155(backward)
                 805578    5.152    0.000 9087.242    0.011 __init__.py:57(backward)
               16112160   16.083    0.000 9063.896    0.001 activation.py:653(forward)
                 805578 9062.612    0.011 9062.612    0.011 {method 'run_backward' of 'torch._C._EngineBase' objects}
               16112160   24.328    0.000 9047.813    0.001 functional.py:1277(leaky_relu)
               16112160 9020.997    0.001 9020.997    0.001 {built-in method torch._C._nn.leaky_relu}
               13426800   24.818    0.000 3291.356    0.000 conv.py:418(forward)
               13426800   26.362    0.000 3256.080    0.000 conv.py:410(_conv_forward)
               13426800 3224.902    0.000 3224.902    0.000 {built-in method conv2d}
                5639346 2943.781    0.001 2943.781    0.001 {built-in method cat}
                 805578    4.694    0.000 1172.875    0.001 grad_mode.py:12(decorate_context)
                 805578  292.306    0.000 1162.246    0.001 adam.py:51(step)
                 268626    4.823    0.000 1025.617    0.004 agent.py:38(chooseMulti)
                 268626    8.396    0.000 1007.497    0.004 environments.py:73(step)
               37114017  686.138    0.000  686.138    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                 268626    0.858    0.000  677.884    0.003 agent.py:30(rememberMulti)
                 268626   24.445    0.000  677.026    0.003 agent.py:31(<listcomp>)
                2685366  111.484    0.000  651.786    0.000 rnn.py:109(flatten_parameters)
                 268626   12.565    0.000  604.151    0.002 agent.py:41(<listcomp>)
                 268626    5.408    0.000  594.896    0.002 environments.py:75(<listcomp>)
                5398638  168.658    0.000  592.716    0.000 helpers.py:8(clean)
                7815372  590.815    0.000  590.815    0.000 {built-in method as_tensor}
                2685360   28.101    0.000  585.674    0.000 rnn.py:550(forward)
                5372520  214.526    0.000  559.253    0.000 exploration.py:28(epsilonGreedy)
                2685360  523.994    0.000  523.994    0.000 {built-in method lstm}
                2685363  417.291    0.000  417.291    0.000 {built-in method _cudnn_rnn_flatten_weight}
                 268626    5.788    0.000  381.819    0.001 environments.py:74(<listcomp>)
                5372520   20.666    0.000  376.031    0.000 interop.py:274(step)
               25778496  215.476    0.000  215.476    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5372520    2.679    0.000  205.042    0.000 wrapper.py:25(act)
                5372520    7.236    0.000  202.363    0.000 env.py:197(act)
               25778496  191.572    0.000  191.572    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                5372520  190.906    0.000  191.435    0.000 libenv.py:352(act)
                2685360    7.015    0.000  162.611    0.000 linear.py:90(forward)
                2685360   14.001    0.000  152.676    0.000 functional.py:1655(linear)
                   2686    0.541    0.000  134.742    0.050 agent.py:61(update_target_network)
               12889248  131.124    0.000  131.124    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10742315  106.940    0.000  114.556    0.000 module.py:774(__setattr__)
                   2686   32.860    0.012  110.221    0.041 memory.py:37(update_distribution)
                 805578   83.586    0.000  110.035    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               12889248  109.226    0.000  109.226    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 805578   18.526    0.000  107.768    0.000 optimizer.py:166(zero_grad)
                2685360  102.190    0.000  102.190    0.000 {built-in method addmm}
                5372520   94.791    0.000   94.791    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               12889248   92.789    0.000   92.789    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10771158    8.337    0.000   91.750    0.000 extract_dict_ob.py:9(observe)
                5372520   89.290    0.000   89.290    0.000 {method 'std' of 'torch._C._TensorBase' objects}
               12889248   89.254    0.000   89.254    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6182870   87.200    0.000   87.200    0.000 {built-in method numpy.array}
               10771158    5.086    0.000   83.413    0.000 wrapper.py:19(observe)
               10771158   21.078    0.000   78.327    0.000 libenv.py:344(observe)
                2685360    5.561    0.000   76.369    0.000 pooling.py:156(forward)
                2685360    4.284    0.000   70.808    0.000 _jit_internal.py:237(fn)
                2685360    4.196    0.000   66.081    0.000 functional.py:564(_max_pool2d)
                2685360   61.543    0.000   61.543    0.000 {built-in method max_pool2d}
               12889248   60.826    0.000   60.826    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               16143678   17.548    0.000   56.967    0.000 libenv.py:281(_maybe_copy_dict)
                 805578    1.818    0.000   51.149    0.000 loss.py:444(forward)
               41089711   50.301    0.000   50.301    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 804978   49.698    0.000   49.698    0.000 memory.py:35(<listcomp>)
               10741452   43.062    0.000   49.634    0.000 __init__.py:66(is_acceptable)
                 805578    7.660    0.000   49.331    0.000 functional.py:2621(mse_loss)
               48433720   48.861    0.000   48.861    0.000 {method 'copy' of 'numpy.ndarray' objects}
               64446288   39.750    0.000   46.654    0.000 tensor.py:725(grad)
                5372520    4.401    0.000   40.950    0.000 wrapper.py:22(get_info)
                6981876   39.786    0.000   39.786    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               45748135   36.977    0.000   37.033    0.000 module.py:758(__getattr__)
                5372520   18.647    0.000   36.549    0.000 libenv.py:363(get_info)
                1611156   35.912    0.000   35.912    0.000 {built-in method gather}
                 805878    1.549    0.000   34.325    0.000 functional.py:68(split)
                 805878    1.598    0.000   32.657    0.000 tensor.py:367(split)
                5372520   32.334    0.000   32.334    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               49142058   31.546    0.000   31.546    0.000 {built-in method torch._C._get_tracing_state}
                5372520   31.219    0.000   31.219    0.000 memory.py:15(inner)
                1792964    3.096    0.000   30.921    0.000 <__array_function__ internals>:2(prod)
                 805878   30.902    0.000   30.902    0.000 {function Tensor.split at 0x7f9b71d76790}
                 805578   27.396    0.000   27.396    0.000 {built-in method torch._C._nn.mse_loss}
                1793004    2.193    0.000   27.388    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                 493623   11.177    0.000   26.802    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2600628   26.700    0.000   26.700    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                 804979   26.129    0.000   26.129    0.000 {built-in method numpy.arange}
                1792964    3.741    0.000   25.195    0.000 fromnumeric.py:2881(prod)
                2685360    6.881    0.000   22.509    0.000 rnn.py:524(check_forward_args)
                 268626    3.268    0.000   22.388    0.000 environments.py:76(<listcomp>)
              204624312   21.687    0.000   21.687    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1792964    6.712    0.000   21.454    0.000 fromnumeric.py:70(_wrapreduction)
                2685360   20.616    0.000   20.616    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 805578    4.662    0.000   19.197    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 8274471: <Discount_0.995_dist_0> in cluster <dcc> Done

Job <Discount_0.995_dist_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Sat Nov  7 22:13:58 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov  7 22:55:06 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov  7 22:55:06 2020
Terminated at Sun Nov  8 13:53:46 2020
Results reported at Sun Nov  8 13:53:46 2020

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

    CPU time :                                   17957.00 sec.
    Max Memory :                                 24786 MB
    Average Memory :                             24229.98 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5934.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   53919 sec.
    Turnaround time :                            56388 sec.

The output (if any) is above this job summary.

