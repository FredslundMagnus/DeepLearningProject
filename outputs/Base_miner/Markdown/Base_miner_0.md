[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_miner-0
    Discount :                  0.999
    Environment :               miner
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


      10946771704 function calls (10722109764 primitive calls) in 86118.55 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86118.551 86118.551 {built-in method builtins.exec}
                      1    0.008    0.008 86118.551 86118.551 <string>:1(<module>)
                      1  549.154  549.154 86118.542 86118.542 main.py:11(main)
                3303837  112.670    0.000 59274.533    0.018 agent.py:46(learn)
                3303737  391.240    0.000 57409.769    0.017 agent.py:54(TD_learn)
                3303737  209.509    0.000 34662.683    0.010 memory.py:27(sample_distribution)
                3303737  314.252    0.000 33626.665    0.010 helpers.py:12(stack)
               29733981 17922.522    0.001 17922.527    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        241174601/16518785 1015.389    0.000 16143.614    0.001 module.py:710(_call_impl)
               13215048  261.004    0.000 15795.451    0.001 agent.py:117(forward)
               29733933 15006.519    0.001 15006.519    0.001 {built-in method cat}
                3303837   87.498    0.000 10724.285    0.003 environments.py:73(step)
              460038151 8755.433    0.000 8755.433    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               39645144  249.314    0.000 8660.348    0.000 container.py:115(forward)
                3303837    9.676    0.000 7924.158    0.002 agent.py:32(rememberMulti)
                3303837  276.348    0.000 7914.482    0.002 agent.py:33(<listcomp>)
                3303837   50.018    0.000 7403.893    0.002 agent.py:41(chooseMulti)
                3303837   63.971    0.000 6668.518    0.002 environments.py:75(<listcomp>)
               66147132 1779.689    0.000 6612.498    0.000 helpers.py:8(clean)
               76058343 5582.738    0.000 5582.738    0.000 {built-in method as_tensor}
               66075240  109.889    0.000 5032.316    0.000 conv.py:418(forward)
               66075240  135.160    0.000 4875.908    0.000 conv.py:410(_conv_forward)
               66075240 4718.512    0.000 4718.512    0.000 {built-in method conv2d}
                3303737   20.486    0.000 4443.676    0.001 grad_mode.py:12(decorate_context)
                3303737   17.666    0.000 4399.949    0.001 tensor.py:155(backward)
                3303737 1121.447    0.000 4399.408    0.001 adam.py:51(step)
                3303737   22.139    0.000 4382.283    0.001 __init__.py:57(backward)
                3303737 4277.792    0.001 4277.792    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3303837   66.260    0.000 3767.635    0.001 environments.py:74(<listcomp>)
               66076740  238.618    0.000 3701.374    0.000 interop.py:274(step)
               13215054  570.618    0.000 3267.384    0.000 rnn.py:109(flatten_parameters)
               13215048  139.150    0.000 2965.551    0.000 rnn.py:550(forward)
                3303837  118.107    0.000 2693.027    0.001 agent.py:44(<listcomp>)
               13215048 2657.182    0.000 2657.182    0.000 {built-in method lstm}
               66076740  176.149    0.000 2297.327    0.000 exploration.py:31(epsilonGreedy)
               13215051 2001.686    0.000 2001.686    0.000 {built-in method _cudnn_rnn_flatten_weight}
                  33038    6.192    0.000 1752.093    0.053 agent.py:81(update_target_network)
               66076740   29.258    0.000 1724.543    0.000 wrapper.py:25(act)
               66076740   78.357    0.000 1695.285    0.000 env.py:197(act)
               66076740 1567.047    0.000 1573.312    0.000 libenv.py:352(act)
                  33038  456.410    0.014 1475.720    0.045 memory.py:37(update_distribution)
               79290288   73.067    0.000 1286.164    0.000 activation.py:653(forward)
               79290288  121.669    0.000 1213.097    0.000 functional.py:1277(leaky_relu)
               69446354 1122.360    0.000 1122.360    0.000 {built-in method numpy.array}
               79290288 1080.640    0.000 1080.640    0.000 {built-in method torch._C._nn.leaky_relu}
              132223872   94.249    0.000 1047.064    0.000 extract_dict_ob.py:9(observe)
              132223872   55.473    0.000  952.815    0.000 wrapper.py:19(observe)
              132223872  242.943    0.000  897.342    0.000 libenv.py:344(observe)
              105719584  810.562    0.000  810.562    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13215048   35.209    0.000  790.965    0.000 linear.py:90(forward)
               13215048   69.610    0.000  742.664    0.000 functional.py:1655(linear)
              105719584  720.650    0.000  720.650    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              198300612  203.123    0.000  651.034    0.000 libenv.py:281(_maybe_copy_dict)
               52861067  530.595    0.000  566.646    0.000 module.py:774(__setattr__)
              594934874  561.025    0.000  561.025    0.000 {method 'copy' of 'numpy.ndarray' objects}
               52859792  498.143    0.000  498.143    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               13215048  490.771    0.000  490.771    0.000 {built-in method addmm}
               66076740   53.679    0.000  484.236    0.000 wrapper.py:22(get_info)
              476416092  470.437    0.000  470.437    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                3303737  352.887    0.000  466.817    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               66076740  223.660    0.000  430.557    0.000 libenv.py:363(get_info)
               52859792  415.907    0.000  415.907    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               66076740  408.995    0.000  408.995    0.000 memory.py:15(inner)
                3303737   69.814    0.000  404.613    0.000 optimizer.py:166(zero_grad)
               13215048   35.139    0.000  391.980    0.000 pooling.py:156(forward)
               13215048   21.124    0.000  356.841    0.000 _jit_internal.py:237(fn)
               52859792  345.734    0.000  345.734    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               13215048   23.847    0.000  333.622    0.000 functional.py:564(_max_pool2d)
               52859792  329.412    0.000  329.412    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13215048  308.109    0.000  308.109    0.000 {built-in method max_pool2d}
                9911511   15.763    0.000  303.838    0.000 functional.py:68(split)
                9911511   16.112    0.000  286.813    0.000 tensor.py:367(split)
               66076740  277.593    0.000  277.593    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               52860204  237.625    0.000  276.126    0.000 __init__.py:66(is_acceptable)
                9911511  268.910    0.000  268.910    0.000 {function Tensor.split at 0x7f2ef0923940}
                3303538  247.046    0.000  247.046    0.000 memory.py:35(<listcomp>)
               52859792  228.475    0.000  228.475    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3303837   20.459    0.000  217.986    0.000 collector.py:7(collect)
                3303737   10.809    0.000  214.417    0.000 loss.py:444(forward)
                3303737   32.137    0.000  203.608    0.000 functional.py:2621(mse_loss)
                3303837   36.320    0.000  200.634    0.000 environments.py:76(<listcomp>)
                6607675  196.027    0.000  196.027    0.000 {built-in method builtins.sum}
              264447744   66.117    0.000  190.062    0.000 libenv.py:271(_maybe_copy_ndarray)
               33037570  177.602    0.000  177.602    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              264299008  150.744    0.000  176.018    0.000 tensor.py:725(grad)
              225845503  167.320    0.000  167.972    0.000 module.py:758(__getattr__)
               66076760   37.899    0.000  164.357    0.000 environments.py:79(reset)
                  66076   16.764    0.000  154.518    0.002 {built-in method _pickle.loads}
                6607474  147.431    0.000  147.431    0.000 {built-in method gather}
              241174601  143.190    0.000  143.190    0.000 {built-in method torch._C._get_tracing_state}
                  66076   28.446    0.000  115.664    0.002 {built-in method _pickle.dumps}
                3303737  112.460    0.000  112.460    0.000 {built-in method torch._C._nn.mse_loss}
               13215048   36.357    0.000  111.535    0.000 rnn.py:524(check_forward_args)
                8301935   11.588    0.000  108.207    0.000 <__array_function__ internals>:2(prod)
                1189366    1.295    0.000  106.553    0.000 storage.py:141(_load_from_bytes)
                1189366    5.538    0.000  105.258    0.000 serialization.py:486(load)
               13215048  103.612    0.000  103.612    0.000 {method 't' of 'torch._C._TensorBase' objects}
               66147172   48.607    0.000   98.985    0.000 types.py:163(multimap)
                8301975    8.383    0.000   94.990    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
             1004343548   90.963    0.000   90.963    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8371236: <Base_miner_0> in cluster <dcc> Done

Job <Base_miner_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:32 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Nov 20 05:40:45 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 20 05:40:45 2020
Terminated at Sat Nov 21 05:36:13 2020
Results reported at Sat Nov 21 05:36:13 2020

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

    CPU time :                                   88530.00 sec.
    Max Memory :                                 25370 MB
    Average Memory :                             25043.88 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5350.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86128 sec.
    Turnaround time :                            286781 sec.

The output (if any) is above this job summary.

