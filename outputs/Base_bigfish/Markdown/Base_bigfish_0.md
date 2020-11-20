[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_bigfish-0
    Discount :                  0.999
    Environment :               bigfish
    Hours :                     24
    Memory :                    200000
    Update every :              100
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      9943152394 function calls (9739192918 primitive calls) in 86118.74 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86118.740 86118.740 {built-in method builtins.exec}
                      1    0.012    0.012 86118.739 86118.739 <string>:1(<module>)
                      1  556.185  556.185 86118.726 86118.726 main.py:11(main)
                2999389  130.031    0.000 60239.117    0.020 agent.py:46(learn)
                2999289  392.627    0.000 57977.588    0.019 agent.py:54(TD_learn)
                2999289  210.834    0.000 35977.877    0.012 memory.py:27(sample_distribution)
                2999289  328.267    0.000 34952.846    0.012 helpers.py:12(stack)
               26993949 17880.897    0.001 17880.905    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               26993901 16197.109    0.001 16197.109    0.001 {built-in method cat}
        218949897/14996545 1013.558    0.000 15775.249    0.001 module.py:710(_call_impl)
               11997256  258.333    0.000 15440.776    0.001 agent.py:117(forward)
                2999389   93.769    0.000 10511.414    0.004 environments.py:73(step)
               35991768  249.354    0.000 8351.104    0.000 container.py:115(forward)
              417415877 7954.767    0.000 7954.767    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2999389   10.021    0.000 7937.461    0.003 agent.py:32(rememberMulti)
                2999389  268.988    0.000 7927.440    0.003 agent.py:33(<listcomp>)
                2999389   59.937    0.000 6652.587    0.002 environments.py:75(<listcomp>)
                2999389   50.811    0.000 6626.683    0.002 agent.py:41(chooseMulti)
               60135796 1819.634    0.000 6611.208    0.000 helpers.py:8(clean)
               69133663 5684.464    0.000 5684.464    0.000 {built-in method as_tensor}
               59986280  106.371    0.000 4802.980    0.000 conv.py:418(forward)
               59986280  133.288    0.000 4646.892    0.000 conv.py:410(_conv_forward)
               59986280 4491.100    0.000 4491.100    0.000 {built-in method conv2d}
                2999289   19.274    0.000 4267.342    0.001 grad_mode.py:12(decorate_context)
                2999289   17.813    0.000 4245.604    0.001 tensor.py:155(backward)
                2999289   21.530    0.000 4227.791    0.001 __init__.py:57(backward)
                2999289 1078.632    0.000 4222.164    0.001 adam.py:51(step)
                2999289 4126.496    0.001 4126.496    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2999389   66.546    0.000 3527.208    0.001 environments.py:74(<listcomp>)
               59987780  228.835    0.000 3460.662    0.000 interop.py:274(step)
               11997262  568.727    0.000 3213.234    0.000 rnn.py:109(flatten_parameters)
               11997256  139.671    0.000 2975.366    0.000 rnn.py:550(forward)
               11997256 2665.646    0.000 2665.646    0.000 {built-in method lstm}
                  29993    7.226    0.000 2131.498    0.071 agent.py:81(update_target_network)
               11997259 1938.169    0.000 1938.169    0.000 {built-in method _cudnn_rnn_flatten_weight}
                2999389  111.984    0.000 1876.274    0.001 agent.py:44(<listcomp>)
                  29993  460.932    0.015 1856.093    0.062 memory.py:37(update_distribution)
               59987780   29.803    0.000 1541.163    0.000 wrapper.py:25(act)
               59987780   80.738    0.000 1511.360    0.000 env.py:197(act)
               59987780  174.994    0.000 1502.165    0.000 exploration.py:31(epsilonGreedy)
               63046856 1494.329    0.000 1494.329    0.000 {built-in method numpy.array}
               59987780 1380.924    0.000 1386.806    0.000 libenv.py:352(act)
               71983536   80.865    0.000 1238.126    0.000 activation.py:653(forward)
               71983536  119.042    0.000 1157.260    0.000 functional.py:1277(leaky_relu)
               71983536 1027.230    0.000 1027.230    0.000 {built-in method torch._C._nn.leaky_relu}
              120123576   90.833    0.000 1026.510    0.000 extract_dict_ob.py:9(observe)
              120123576   54.490    0.000  935.677    0.000 wrapper.py:19(observe)
              120123576  231.020    0.000  881.187    0.000 libenv.py:344(observe)
               11997256   35.337    0.000  783.251    0.000 linear.py:90(forward)
               95977248  779.382    0.000  779.382    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11997256   72.073    0.000  733.752    0.000 functional.py:1655(linear)
               95977248  681.683    0.000  681.683    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              180111356  192.761    0.000  645.315    0.000 libenv.py:281(_maybe_copy_dict)
               47989899  532.653    0.000  570.461    0.000 module.py:774(__setattr__)
              540364061  563.090    0.000  563.090    0.000 {method 'copy' of 'numpy.ndarray' objects}
              432116330  507.660    0.000  507.660    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11997256  481.400    0.000  481.400    0.000 {built-in method addmm}
               47988624  480.288    0.000  480.288    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               59987780   53.392    0.000  469.688    0.000 wrapper.py:22(get_info)
                2999289  343.483    0.000  456.466    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               59987780  216.397    0.000  416.296    0.000 libenv.py:363(get_info)
               59987780  408.332    0.000  408.332    0.000 memory.py:15(inner)
                2999289   74.401    0.000  400.942    0.000 optimizer.py:166(zero_grad)
               47988624  398.687    0.000  398.687    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11997256   30.909    0.000  382.770    0.000 pooling.py:156(forward)
               11997256   22.483    0.000  351.861    0.000 _jit_internal.py:237(fn)
               47988624  335.803    0.000  335.803    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11997256   26.584    0.000  327.204    0.000 functional.py:564(_max_pool2d)
               47988624  317.999    0.000  317.999    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8998167   15.462    0.000  299.102    0.000 functional.py:68(split)
               11997256  298.996    0.000  298.996    0.000 {built-in method max_pool2d}
               47989036  248.524    0.000  283.077    0.000 __init__.py:66(is_acceptable)
                8998167   16.062    0.000  282.408    0.000 tensor.py:367(split)
                8998167  264.776    0.000  264.776    0.000 {function Tensor.split at 0x7f6b7dcba940}
               59987780  262.125    0.000  262.125    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2999389   37.651    0.000  237.850    0.000 environments.py:76(<listcomp>)
                2999090  233.152    0.000  233.152    0.000 memory.py:35(<listcomp>)
                2999389   21.535    0.000  221.139    0.000 collector.py:7(collect)
               47988624  220.016    0.000  220.016    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               59987800   41.244    0.000  200.218    0.000 environments.py:79(reset)
                2999289    7.303    0.000  198.981    0.000 loss.py:444(forward)
                5998779  197.855    0.000  197.855    0.000 {built-in method builtins.sum}
                2999289   30.384    0.000  191.678    0.000 functional.py:2621(mse_loss)
              240247152   66.463    0.000  186.860    0.000 libenv.py:271(_maybe_copy_ndarray)
              239943168  150.891    0.000  174.811    0.000 tensor.py:725(grad)
              205033419  173.993    0.000  174.617    0.000 module.py:758(__getattr__)
               29993090  171.490    0.000  171.490    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                  59986   17.472    0.000  153.493    0.003 {built-in method _pickle.loads}
                5998578  146.566    0.000  146.566    0.000 {built-in method gather}
              218949897  139.671    0.000  139.671    0.000 {built-in method torch._C._get_tracing_state}
                  59986   28.586    0.000  114.686    0.002 {built-in method _pickle.dumps}
               11997256   38.089    0.000  114.190    0.000 rnn.py:524(check_forward_args)
                7996595   11.728    0.000  111.790    0.000 <__array_function__ internals>:2(prod)
                2999289  105.355    0.000  105.355    0.000 {built-in method torch._C._nn.mse_loss}
                1079746    1.283    0.000  105.204    0.000 storage.py:141(_load_from_bytes)
                1079746    5.500    0.000  103.921    0.000 serialization.py:486(load)
               11997256  101.934    0.000  101.934    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7996635    8.646    0.000   98.228    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               11025678   96.350    0.000   96.350    0.000 {method 'reduce' of 'numpy.ufunc' objects}
               60135836   45.795    0.000   93.298    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8371224: <Base_bigfish_0> in cluster <dcc> Done

Job <Base_bigfish_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:30 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Nov 17 22:46:58 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 17 22:46:58 2020
Terminated at Wed Nov 18 22:42:25 2020
Results reported at Wed Nov 18 22:42:25 2020

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

    CPU time :                                   88111.00 sec.
    Max Memory :                                 25310 MB
    Average Memory :                             25000.35 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5410.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86128 sec.
    Turnaround time :                            89155 sec.

The output (if any) is above this job summary.

