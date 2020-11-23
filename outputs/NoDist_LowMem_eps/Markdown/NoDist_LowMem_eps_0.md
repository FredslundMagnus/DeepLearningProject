[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NoDist_LowMem_eps-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    50000
    Update every :              100
    Use distribution :          0
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      12660369277 function calls (12465652345 primitive calls) in 86119.70 seconds

##    Ordered by: cumulative time
   List reduced from 1314 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86119.703 86119.703 {built-in method builtins.exec}
                      1    0.094    0.094 86119.703 86119.703 <string>:1(<module>)
                      1  551.517  551.517 86119.607 86119.607 main.py:11(main)
                2863469  127.713    0.000 60312.465    0.021 agent.py:46(learn)
                2863369  365.676    0.000 59568.801    0.021 agent.py:54(TD_learn)
                2863369 2664.689    0.001 38596.131    0.013 memory.py:23(sample)
                2863369  382.638    0.000 34938.602    0.012 helpers.py:12(stack)
               25770621 17034.695    0.001 17034.695    0.001 {built-in method cat}
               25770669 16987.154    0.001 16987.220    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        209027737/14316945  955.406    0.000 15055.938    0.001 module.py:710(_call_impl)
               11453576  244.282    0.000 14730.651    0.001 agent.py:117(forward)
                2863469   91.238    0.000 10757.386    0.004 environments.py:73(step)
               34360728  227.717    0.000 7952.807    0.000 container.py:115(forward)
                2863469    9.540    0.000 7658.302    0.003 agent.py:32(rememberMulti)
                2863469  259.197    0.000 7648.762    0.003 agent.py:33(<listcomp>)
              394755023 7608.836    0.000 7608.836    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2863469   48.461    0.000 6600.933    0.002 agent.py:41(chooseMulti)
                2863469   57.542    0.000 6381.401    0.002 environments.py:75(<listcomp>)
               57445068 1726.538    0.000 6345.383    0.000 helpers.py:8(clean)
               66035175 5503.449    0.000 5503.449    0.000 {built-in method as_tensor}
               57267880  103.837    0.000 4594.765    0.000 conv.py:418(forward)
               57267880  122.582    0.000 4444.548    0.000 conv.py:410(_conv_forward)
               57267880 4300.963    0.000 4300.963    0.000 {built-in method conv2d}
                2863369   18.155    0.000 4082.844    0.001 tensor.py:155(backward)
                2863369   19.717    0.000 4077.708    0.001 grad_mode.py:12(decorate_context)
                2863369   21.987    0.000 4064.689    0.001 __init__.py:57(backward)
                2863469   64.374    0.000 4048.146    0.001 environments.py:74(<listcomp>)
                2863369 1043.463    0.000 4031.977    0.001 adam.py:51(step)
               57269380  218.754    0.000 3983.772    0.000 interop.py:274(step)
                2863369 3964.837    0.001 3964.837    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11453582  558.759    0.000 3116.050    0.000 rnn.py:109(flatten_parameters)
               11453576  140.503    0.000 2819.719    0.000 rnn.py:550(forward)
               11453576 2513.759    0.000 2513.759    0.000 {built-in method lstm}
               57269380   28.809    0.000 2147.185    0.000 wrapper.py:25(act)
               57269380   71.445    0.000 2118.376    0.000 env.py:197(act)
               57269380 2003.074    0.000 2008.689    0.000 libenv.py:352(act)
                2863469  114.733    0.000 2008.337    0.001 agent.py:44(<listcomp>)
               11453579 1877.996    0.000 1877.996    0.000 {built-in method _cudnn_rnn_flatten_weight}
               57269380  166.320    0.000 1637.787    0.000 exploration.py:31(epsilonGreedy)
               68721456   67.393    0.000 1159.254    0.000 activation.py:653(forward)
               68721456  111.937    0.000 1091.862    0.000 functional.py:1277(leaky_relu)
              114714448   85.055    0.000  987.893    0.000 extract_dict_ob.py:9(observe)
                2863369  392.079    0.000  976.628    0.000 random.py:315(sample)
               68721456  969.538    0.000  969.538    0.000 {built-in method torch._C._nn.leaky_relu}
              114714448   53.228    0.000  902.838    0.000 wrapper.py:19(observe)
              114714448  232.316    0.000  849.610    0.000 libenv.py:344(observe)
               11453576   35.360    0.000  754.846    0.000 linear.py:90(forward)
               91627808  742.588    0.000  742.588    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11453576   70.628    0.000  706.534    0.000 functional.py:1655(linear)
               91627808  649.884    0.000  649.884    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              171983828  184.879    0.000  618.346    0.000 libenv.py:281(_maybe_copy_dict)
                  28634    6.807    0.000  615.951    0.022 agent.py:81(update_target_network)
               45815179  510.704    0.000  544.965    0.000 module.py:774(__setattr__)
              515980118  526.773    0.000  526.773    0.000 {method 'copy' of 'numpy.ndarray' objects}
              408720532  473.223    0.000  473.223    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              734903279  307.174    0.000  463.784    0.000 random.py:250(_randbelow_with_getrandbits)
               11453576  461.199    0.000  461.199    0.000 {built-in method addmm}
               45813904  452.119    0.000  452.119    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               57269380   51.266    0.000  450.036    0.000 wrapper.py:22(get_info)
               57269380  427.968    0.000  427.968    0.000 memory.py:15(inner)
               57269380  210.124    0.000  398.770    0.000 libenv.py:363(get_info)
               45813904  374.527    0.000  374.527    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11453576   33.613    0.000  373.931    0.000 pooling.py:156(forward)
                2863369   64.431    0.000  372.821    0.000 optimizer.py:166(zero_grad)
               57326648  359.859    0.000  359.859    0.000 {built-in method numpy.array}
                  28634   90.281    0.003  353.816    0.012 memory.py:37(update_distribution)
               11453576   21.695    0.000  340.318    0.000 _jit_internal.py:237(fn)
                6130637  134.486    0.000  324.628    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               45813904  317.687    0.000  317.687    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11453576   24.003    0.000  316.412    0.000 functional.py:564(_max_pool2d)
               45813904  306.500    0.000  306.500    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8590407   15.987    0.000  292.895    0.000 functional.py:68(split)
               11453576  290.844    0.000  290.844    0.000 {built-in method max_pool2d}
                8590407   16.119    0.000  275.690    0.000 tensor.py:367(split)
               45814316  231.656    0.000  266.962    0.000 __init__.py:66(is_acceptable)
                8590407  258.029    0.000  258.029    0.000 {function Tensor.split at 0x7f92a9bb2940}
               57269380  255.817    0.000  255.817    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2863469   37.389    0.000  236.601    0.000 environments.py:76(<listcomp>)
                2863469   20.935    0.000  213.031    0.000 collector.py:7(collect)
               45813904  208.658    0.000  208.658    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               57269400   38.635    0.000  199.232    0.000 environments.py:79(reset)
                5726939  190.422    0.000  190.422    0.000 {built-in method builtins.sum}
                2863369    7.654    0.000  190.266    0.000 loss.py:444(forward)
               12261414   15.539    0.000  190.143    0.000 <__array_function__ internals>:2(prod)
                2863369   29.009    0.000  182.612    0.000 functional.py:2621(mse_loss)
               12261454   12.152    0.000  172.309    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              229428896   61.078    0.000  168.586    0.000 libenv.py:271(_maybe_copy_ndarray)
              229069568  140.615    0.000  164.826    0.000 tensor.py:725(grad)
               28633890  162.724    0.000  162.724    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               12261414   19.066    0.000  160.157    0.000 fromnumeric.py:2881(prod)
              195741935  156.939    0.000  157.552    0.000 module.py:758(__getattr__)
                  57268   16.779    0.000  145.262    0.003 {built-in method _pickle.loads}
               12261414   37.682    0.000  141.090    0.000 fromnumeric.py:70(_wrapreduction)
                5726738  138.286    0.000  138.286    0.000 {built-in method gather}
              209027737  135.028    0.000  135.028    0.000 {built-in method torch._C._get_tracing_state}
              963332957  111.692    0.000  111.692    0.000 {method 'getrandbits' of '_random.Random' objects}
               11453576   37.703    0.000  111.602    0.000 rnn.py:524(check_forward_args)
                  57268   27.889    0.000  110.066    0.002 {built-in method _pickle.dumps}
                2863369  100.921    0.000  100.921    0.000 {built-in method torch._C._nn.mse_loss}
               11453576   99.878    0.000   99.878    0.000 {method 't' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 8366149: <NoDist_LowMem_eps_0> in cluster <dcc> Done

Job <NoDist_LowMem_eps_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Mon Nov 16 20:57:20 2020
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Nov 17 20:46:18 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 17 20:46:18 2020
Terminated at Wed Nov 18 20:41:46 2020
Results reported at Wed Nov 18 20:41:46 2020

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

    CPU time :                                   88142.00 sec.
    Max Memory :                                 8487 MB
    Average Memory :                             8252.19 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               22233.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86134 sec.
    Turnaround time :                            171866 sec.

The output (if any) is above this job summary.

