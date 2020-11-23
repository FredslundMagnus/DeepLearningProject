[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_coinrun-0
    Discount :                  0.999
    Environment :               coinrun
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


      10757330467 function calls (10536585259 primitive calls) in 86130.60 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86130.604 86130.604 {built-in method builtins.exec}
                      1    0.011    0.011 86130.604 86130.604 <string>:1(<module>)
                      1  545.977  545.977 86130.592 86130.592 main.py:11(main)
                3246238  112.836    0.000 58834.343    0.018 agent.py:46(learn)
                3246138  385.765    0.000 56998.839    0.018 agent.py:54(TD_learn)
                3246138  209.021    0.000 34631.581    0.011 memory.py:27(sample_distribution)
                3246138  333.119    0.000 33618.296    0.010 helpers.py:12(stack)
               29215590 17676.985    0.001 17677.034    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        236969874/16230790 1044.284    0.000 15838.422    0.001 module.py:710(_call_impl)
               12984652  253.672    0.000 15499.782    0.001 agent.py:117(forward)
               29215542 15207.281    0.001 15207.281    0.001 {built-in method cat}
                3246238   87.505    0.000 11610.288    0.004 environments.py:73(step)
               38953956  253.945    0.000 8521.643    0.000 container.py:115(forward)
              451972364 8391.766    0.000 8391.766    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3246238    8.830    0.000 7875.011    0.002 agent.py:32(rememberMulti)
                3246238  270.961    0.000 7866.181    0.002 agent.py:33(<listcomp>)
                3246238   47.157    0.000 7020.153    0.002 agent.py:41(chooseMulti)
                3246238   63.752    0.000 6558.420    0.002 environments.py:75(<listcomp>)
               65030090 1749.547    0.000 6506.524    0.000 helpers.py:8(clean)
               74768504 5531.169    0.000 5531.169    0.000 {built-in method as_tensor}
               64923260  103.960    0.000 4922.966    0.000 conv.py:418(forward)
               64923260  125.659    0.000 4773.257    0.000 conv.py:410(_conv_forward)
                3246238   66.282    0.000 4755.638    0.001 environments.py:74(<listcomp>)
               64924760  231.932    0.000 4689.356    0.000 interop.py:274(step)
               64923260 4625.247    0.000 4625.247    0.000 {built-in method conv2d}
                3246138   20.336    0.000 4409.454    0.001 grad_mode.py:12(decorate_context)
                3246138 1101.177    0.000 4365.715    0.001 adam.py:51(step)
                3246138   17.690    0.000 4312.161    0.001 tensor.py:155(backward)
                3246138   21.878    0.000 4294.472    0.001 __init__.py:57(backward)
                3246138 4192.097    0.001 4192.097    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               12984658  554.529    0.000 3172.324    0.000 rnn.py:109(flatten_parameters)
               12984652  139.576    0.000 2899.842    0.000 rnn.py:550(forward)
               64924760   28.408    0.000 2743.407    0.000 wrapper.py:25(act)
               64924760   79.393    0.000 2714.999    0.000 env.py:197(act)
               12984652 2600.461    0.000 2600.461    0.000 {built-in method lstm}
               64924760 2585.385    0.000 2591.556    0.000 libenv.py:352(act)
                3246238  113.611    0.000 2385.150    0.001 agent.py:44(<listcomp>)
               64924760  175.573    0.000 2001.564    0.000 exploration.py:31(epsilonGreedy)
               12984655 1957.127    0.000 1957.127    0.000 {built-in method _cudnn_rnn_flatten_weight}
                  32462    6.169    0.000 1722.668    0.053 agent.py:81(update_target_network)
                  32462  444.359    0.014 1445.802    0.045 memory.py:37(update_distribution)
               77907912   75.663    0.000 1270.613    0.000 activation.py:653(forward)
               77907912  112.744    0.000 1194.950    0.000 functional.py:1277(leaky_relu)
               68235623 1103.961    0.000 1103.961    0.000 {built-in method numpy.array}
               77907912 1071.739    0.000 1071.739    0.000 {built-in method torch._C._nn.leaky_relu}
              129954850   94.037    0.000 1033.417    0.000 extract_dict_ob.py:9(observe)
              129954850   53.382    0.000  939.380    0.000 wrapper.py:19(observe)
              129954850  240.019    0.000  885.998    0.000 libenv.py:344(observe)
              103876416  818.320    0.000  818.320    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12984652   32.386    0.000  774.435    0.000 linear.py:90(forward)
               12984652   67.407    0.000  729.095    0.000 functional.py:1655(linear)
              103876416  708.736    0.000  708.736    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              194879610  197.195    0.000  637.478    0.000 libenv.py:281(_maybe_copy_dict)
               51939483  524.981    0.000  559.944    0.000 module.py:774(__setattr__)
              584671292  553.835    0.000  553.835    0.000 {method 'copy' of 'numpy.ndarray' objects}
               51938208  498.989    0.000  498.989    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              467992434  485.429    0.000  485.429    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               12984652  485.411    0.000  485.411    0.000 {built-in method addmm}
               64924760   56.642    0.000  482.517    0.000 wrapper.py:22(get_info)
                3246138  341.408    0.000  452.349    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               64924760  428.838    0.000  428.838    0.000 memory.py:15(inner)
               64924760  223.418    0.000  425.875    0.000 libenv.py:363(get_info)
               51938208  412.256    0.000  412.256    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3246138   70.266    0.000  407.953    0.000 optimizer.py:166(zero_grad)
               12984652   29.628    0.000  374.975    0.000 pooling.py:156(forward)
               12984652   20.820    0.000  345.347    0.000 _jit_internal.py:237(fn)
               51938208  342.969    0.000  342.969    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               51938208  329.556    0.000  329.556    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               12984652   22.618    0.000  322.363    0.000 functional.py:564(_max_pool2d)
                9738714   14.630    0.000  299.057    0.000 functional.py:68(split)
               12984652  298.100    0.000  298.100    0.000 {built-in method max_pool2d}
                9738714   15.104    0.000  283.241    0.000 tensor.py:367(split)
               64924760  269.976    0.000  269.976    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9738714  266.572    0.000  266.572    0.000 {function Tensor.split at 0x7f9edbe09940}
               51938620  223.540    0.000  259.685    0.000 __init__.py:66(is_acceptable)
                3245939  241.936    0.000  241.936    0.000 memory.py:35(<listcomp>)
               51938208  230.667    0.000  230.667    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3246238   35.924    0.000  208.725    0.000 environments.py:76(<listcomp>)
                3246238   20.755    0.000  207.729    0.000 collector.py:7(collect)
                3246138    8.319    0.000  204.274    0.000 loss.py:444(forward)
                3246138   29.808    0.000  195.954    0.000 functional.py:2621(mse_loss)
              259909700   66.672    0.000  191.162    0.000 libenv.py:271(_maybe_copy_ndarray)
                6492477  185.443    0.000  185.443    0.000 {built-in method builtins.sum}
               32461580  176.783    0.000  176.783    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              259691088  150.495    0.000  174.377    0.000 tensor.py:725(grad)
               64924780   37.992    0.000  172.811    0.000 environments.py:79(reset)
              221908035  164.778    0.000  165.422    0.000 module.py:758(__getattr__)
                  64924   16.755    0.000  155.230    0.002 {built-in method _pickle.loads}
                6492276  145.108    0.000  145.108    0.000 {built-in method gather}
              236969874  139.741    0.000  139.741    0.000 {built-in method torch._C._get_tracing_state}
                  64924   28.311    0.000  115.467    0.002 {built-in method _pickle.dumps}
                3246138  110.194    0.000  110.194    0.000 {built-in method torch._C._nn.mse_loss}
                1168630    1.316    0.000  106.635    0.000 storage.py:141(_load_from_bytes)
                8248190   11.567    0.000  106.257    0.000 <__array_function__ internals>:2(prod)
               12984652   34.118    0.000  105.623    0.000 rnn.py:524(check_forward_args)
                1168630    5.631    0.000  105.319    0.000 serialization.py:486(load)
               12984652  102.153    0.000  102.153    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8248230    8.486    0.000   92.883    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               65030130   47.538    0.000   91.862    0.000 types.py:163(multimap)
              986833452   90.478    0.000   90.478    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8371229: <Base_coinrun_0> in cluster <dcc> Done

Job <Base_coinrun_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:31 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 18 23:38:51 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 18 23:38:51 2020
Terminated at Thu Nov 19 23:34:31 2020
Results reported at Thu Nov 19 23:34:31 2020

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

    CPU time :                                   88670.00 sec.
    Max Memory :                                 25347 MB
    Average Memory :                             25043.68 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5373.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86142 sec.
    Turnaround time :                            178680 sec.

The output (if any) is above this job summary.

