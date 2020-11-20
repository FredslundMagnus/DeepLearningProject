[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_climber-0
    Discount :                  0.999
    Environment :               climber
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


      10028394070 function calls (9822648846 primitive calls) in 86138.87 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86138.869 86138.869 {built-in method builtins.exec}
                      1    0.012    0.012 86138.869 86138.869 <string>:1(<module>)
                      1  498.047  498.047 86138.856 86138.856 main.py:11(main)
                3025650  107.360    0.000 58516.241    0.019 agent.py:46(learn)
                3025550  433.392    0.000 56832.145    0.019 agent.py:54(TD_learn)
                3025550  191.074    0.000 31370.142    0.010 memory.py:27(sample_distribution)
                3025550  301.881    0.000 30406.541    0.010 helpers.py:12(stack)
        220866950/15127850  959.361    0.000 16980.175    0.001 module.py:710(_call_impl)
               12102300  259.688    0.000 16637.614    0.001 agent.py:117(forward)
               27230298 16283.414    0.001 16283.447    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               27230250 13456.358    0.000 13456.358    0.000 {built-in method cat}
                3025650   81.754    0.000 11025.163    0.004 environments.py:73(step)
               36306900  255.859    0.000 9163.468    0.000 container.py:115(forward)
                3025650    8.851    0.000 8775.685    0.003 agent.py:32(rememberMulti)
                3025650  372.594    0.000 8766.834    0.003 agent.py:33(<listcomp>)
              421092399 8607.836    0.000 8607.836    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3025650   47.250    0.000 7075.073    0.002 agent.py:41(chooseMulti)
                3025650   57.803    0.000 6706.744    0.002 environments.py:75(<listcomp>)
               60587733 1677.971    0.000 6658.130    0.000 helpers.py:8(clean)
                3025550   20.802    0.000 5817.986    0.002 grad_mode.py:12(decorate_context)
                3025550 1372.169    0.000 5773.815    0.002 adam.py:51(step)
               69664383 5722.990    0.000 5722.990    0.000 {built-in method as_tensor}
               60511500  103.657    0.000 5323.761    0.000 conv.py:418(forward)
               60511500  115.186    0.000 5178.377    0.000 conv.py:410(_conv_forward)
               60511500 5043.642    0.000 5043.642    0.000 {built-in method conv2d}
                3025550   18.464    0.000 4912.258    0.002 tensor.py:155(backward)
                3025550   21.041    0.000 4893.794    0.002 __init__.py:57(backward)
                3025550 4785.849    0.002 4785.849    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3025650   66.324    0.000 4026.120    0.001 environments.py:74(<listcomp>)
               60513000  237.586    0.000 3959.795    0.000 interop.py:274(step)
               12102306  565.772    0.000 3701.650    0.000 rnn.py:109(flatten_parameters)
               12102300  130.000    0.000 2877.444    0.000 rnn.py:550(forward)
               12102300 2592.833    0.000 2592.833    0.000 {built-in method lstm}
               12102303 2483.251    0.000 2483.251    0.000 {built-in method _cudnn_rnn_flatten_weight}
                3025650  131.658    0.000 2136.053    0.001 agent.py:44(<listcomp>)
               60513000   26.700    0.000 2011.189    0.000 wrapper.py:25(act)
               60513000   92.200    0.000 1984.490    0.000 env.py:197(act)
               60513000 1832.709    0.000 1838.128    0.000 libenv.py:352(act)
               60513000  212.846    0.000 1658.096    0.000 exploration.py:31(epsilonGreedy)
                  30256    5.731    0.000 1576.736    0.052 agent.py:81(update_target_network)
               72613800   64.275    0.000 1472.503    0.000 activation.py:653(forward)
               72613800  104.958    0.000 1408.228    0.000 functional.py:1277(leaky_relu)
                  30256  407.171    0.013 1311.952    0.043 memory.py:37(update_distribution)
               72613800 1293.540    0.000 1293.540    0.000 {built-in method torch._C._nn.leaky_relu}
               96817600 1144.164    0.000 1144.164    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              121100733   94.463    0.000 1023.870    0.000 extract_dict_ob.py:9(observe)
               63598863 1012.178    0.000 1012.178    0.000 {built-in method numpy.array}
               96817600 1010.300    0.000 1010.300    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              121100733   49.473    0.000  929.407    0.000 wrapper.py:19(observe)
              121100733  227.639    0.000  879.935    0.000 libenv.py:344(observe)
               12102300   33.664    0.000  825.580    0.000 linear.py:90(forward)
               12102300   63.394    0.000  779.623    0.000 functional.py:1655(linear)
              436070723  664.598    0.000  664.598    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              181613733  194.841    0.000  635.506    0.000 libenv.py:281(_maybe_copy_dict)
               48408800  633.703    0.000  633.703    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3025550   87.782    0.000  573.583    0.000 optimizer.py:166(zero_grad)
              544871455  568.316    0.000  568.316    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48408800  530.676    0.000  530.676    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               12102300  530.094    0.000  530.094    0.000 {built-in method addmm}
               48410075  490.637    0.000  525.307    0.000 module.py:774(__setattr__)
               60513000   52.429    0.000  483.925    0.000 wrapper.py:22(get_info)
               48408800  472.718    0.000  472.718    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48408800  455.285    0.000  455.285    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3025550  335.561    0.000  445.439    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               60513000  228.339    0.000  431.496    0.000 libenv.py:363(get_info)
               60513000  420.312    0.000  420.312    0.000 memory.py:15(inner)
               12102300   26.703    0.000  405.075    0.000 pooling.py:156(forward)
               12102300   19.288    0.000  378.372    0.000 _jit_internal.py:237(fn)
               12102300   20.719    0.000  357.180    0.000 functional.py:564(_max_pool2d)
               48408800  354.031    0.000  354.031    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               60513000  346.300    0.000  346.300    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               12102300  334.895    0.000  334.895    0.000 {built-in method max_pool2d}
                9076950   13.912    0.000  290.218    0.000 functional.py:68(split)
                9076950   15.179    0.000  275.203    0.000 tensor.py:367(split)
               48409212  238.055    0.000  273.622    0.000 __init__.py:66(is_acceptable)
                9076950  258.463    0.000  258.463    0.000 {function Tensor.split at 0x7fd5abcc6940}
                3025351  218.023    0.000  218.023    0.000 memory.py:35(<listcomp>)
                3025550    9.238    0.000  215.753    0.000 loss.py:444(forward)
                3025650   33.580    0.000  210.545    0.000 environments.py:76(<listcomp>)
                3025550   28.054    0.000  206.516    0.000 functional.py:2621(mse_loss)
               30255700  202.798    0.000  202.798    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                3025650   20.307    0.000  201.898    0.000 collector.py:7(collect)
              242201466   62.522    0.000  200.755    0.000 libenv.py:271(_maybe_copy_ndarray)
              242044048  162.051    0.000  186.033    0.000 tensor.py:725(grad)
                6051301  180.186    0.000  180.186    0.000 {built-in method builtins.sum}
               60513020   36.507    0.000  177.037    0.000 environments.py:79(reset)
                6051100  166.289    0.000  166.289    0.000 {built-in method gather}
              220866950  165.497    0.000  165.497    0.000 {built-in method torch._C._get_tracing_state}
              206828635  155.830    0.000  156.418    0.000 module.py:758(__getattr__)
                  60512   15.699    0.000  149.542    0.002 {built-in method _pickle.loads}
                3025550  122.859    0.000  122.859    0.000 {built-in method torch._C._nn.mse_loss}
               12102300  116.251    0.000  116.251    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8022892   11.323    0.000  112.841    0.000 <__array_function__ internals>:2(prod)
                  60512   26.421    0.000  109.510    0.002 {built-in method _pickle.dumps}
               12102300   32.463    0.000  101.360    0.000 rnn.py:524(check_forward_args)
                1089214    1.227    0.000  100.326    0.000 storage.py:141(_load_from_bytes)
                8022932    8.293    0.000   99.828    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                1089214    5.200    0.000   99.099    0.000 serialization.py:486(load)
               60587773   44.873    0.000   91.947    0.000 types.py:163(multimap)
                8022892   15.668    0.000   91.536    0.000 fromnumeric.py:2881(prod)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8371228: <Base_climber_0> in cluster <dcc> Done

Job <Base_climber_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:30 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 18 22:08:32 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 18 22:08:32 2020
Terminated at Thu Nov 19 22:04:28 2020
Results reported at Thu Nov 19 22:04:28 2020

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

    CPU time :                                   87773.00 sec.
    Max Memory :                                 25338 MB
    Average Memory :                             25017.59 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5382.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86157 sec.
    Turnaround time :                            173278 sec.

The output (if any) is above this job summary.

