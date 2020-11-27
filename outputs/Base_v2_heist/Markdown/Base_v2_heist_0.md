[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_heist-0
    Discount :                  0.995
    Environment :               heist
    Hours :                     24
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      9261181323 function calls (9058362681 primitive calls) in 86120.60 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86120.597 86120.597 {built-in method builtins.exec}
                      1    0.078    0.078 86120.597 86120.597 <string>:1(<module>)
                      1  501.646  501.646 86120.518 86120.518 main.py:12(main)
                2668960  100.561    0.000 52008.039    0.019 agent.py:46(learn)
                2668460  333.640    0.000 51114.279    0.019 agent.py:54(TD_learn)
                2668460  195.099    0.000 29912.832    0.011 memory.py:27(sample_distribution)
                2668460  330.378    0.000 29022.770    0.011 helpers.py:12(stack)
              361964416 18133.645    0.000 18133.645    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2668960   40.664    0.000 17686.631    0.007 agent.py:41(chooseMulti)
        216155260/13342800  936.542    0.000 15012.957    0.001 module.py:710(_call_impl)
               10674340  220.423    0.000 14725.523    0.001 agent.py:119(forward)
               24017694 14722.793    0.001 14722.848    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               24017640 13569.702    0.001 13569.702    0.001 {built-in method cat}
                2668960  101.914    0.000 13366.046    0.005 agent.py:44(<listcomp>)
               53379200  149.912    0.000 13022.508    0.000 exploration.py:33(epsilonGreedy)
                2668960   74.135    0.000 9020.272    0.003 environments.py:73(step)
               32023020  231.953    0.000 8312.600    0.000 container.py:115(forward)
                2668960    8.273    0.000 6700.213    0.003 agent.py:32(rememberMulti)
                2668960  228.175    0.000 6691.940    0.003 agent.py:33(<listcomp>)
                2668960   54.531    0.000 5797.402    0.002 environments.py:75(<listcomp>)
               53440085 1500.855    0.000 5750.503    0.000 helpers.py:8(clean)
               64046040  110.367    0.000 4964.172    0.000 conv.py:418(forward)
               61445465 4941.807    0.000 4941.807    0.000 {built-in method as_tensor}
               64046040  122.027    0.000 4802.912    0.000 conv.py:410(_conv_forward)
               64046040 4658.484    0.000 4658.484    0.000 {built-in method conv2d}
                2668460   17.152    0.000 4185.552    0.002 grad_mode.py:12(decorate_context)
                2668460 1043.770    0.000 4148.067    0.002 adam.py:51(step)
                2668460   15.716    0.000 4120.860    0.002 tensor.py:155(backward)
                2668460   20.466    0.000 4105.144    0.002 __init__.py:57(backward)
                2668460 4017.293    0.002 4017.293    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2668960   52.813    0.000 2976.097    0.001 environments.py:74(<listcomp>)
               10674346  516.630    0.000 2930.197    0.000 rnn.py:109(flatten_parameters)
               53379200  198.576    0.000 2923.284    0.000 interop.py:274(step)
               10674340  120.704    0.000 2695.481    0.000 rnn.py:550(forward)
               10674340 2423.409    0.000 2423.409    0.000 {built-in method lstm}
               10674343 1796.750    0.000 1796.750    0.000 {built-in method _cudnn_rnn_flatten_weight}
               53379200   26.716    0.000 1296.425    0.000 wrapper.py:25(act)
               53379200   65.681    0.000 1269.710    0.000 env.py:197(act)
               74720380   70.036    0.000 1244.199    0.000 activation.py:653(forward)
               74720380  112.305    0.000 1174.163    0.000 functional.py:1277(leaky_relu)
               53379200 1163.644    0.000 1168.742    0.000 libenv.py:352(act)
               74720380 1051.317    0.000 1051.317    0.000 {built-in method torch._C._nn.leaky_relu}
              106819285   78.526    0.000  864.717    0.000 extract_dict_ob.py:9(observe)
                   5337    1.355    0.000  793.199    0.149 agent.py:81(update_target_network)
              106819285   51.042    0.000  786.191    0.000 wrapper.py:19(observe)
               96064560  777.427    0.000  777.427    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              106819285  202.544    0.000  735.149    0.000 libenv.py:344(observe)
                   5337  204.288    0.038  727.710    0.136 memory.py:37(update_distribution)
               96064560  685.408    0.000  685.408    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10674340   29.011    0.000  681.566    0.000 linear.py:90(forward)
               10674340   60.113    0.000  640.823    0.000 functional.py:1655(linear)
               56058334  609.799    0.000  609.799    0.000 {built-in method numpy.array}
               42698340  520.446    0.000  552.625    0.000 module.py:774(__setattr__)
              160198485  168.603    0.000  531.589    0.000 libenv.py:281(_maybe_copy_dict)
               48032280  459.411    0.000  459.411    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              480600792  451.077    0.000  451.077    0.000 {method 'copy' of 'numpy.ndarray' objects}
               10674340  426.649    0.000  426.649    0.000 {built-in method addmm}
              375184986  406.570    0.000  406.570    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               48032280  399.177    0.000  399.177    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               53379200   44.882    0.000  397.999    0.000 wrapper.py:22(get_info)
                2668460   65.671    0.000  385.124    0.000 optimizer.py:166(zero_grad)
               53379200  384.816    0.000  384.816    0.000 memory.py:15(inner)
               11689984  149.092    0.000  382.745    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2668460  288.982    0.000  375.475    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               53379200  182.459    0.000  353.116    0.000 libenv.py:363(get_info)
               10674340   32.881    0.000  333.459    0.000 pooling.py:156(forward)
               48032280  325.027    0.000  325.027    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48032280  314.982    0.000  314.982    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10674340   17.877    0.000  300.578    0.000 _jit_internal.py:237(fn)
               10674340   20.238    0.000  281.038    0.000 functional.py:564(_max_pool2d)
               26048568   24.827    0.000  280.809    0.000 <__array_function__ internals>:2(prod)
               42697372  240.160    0.000  272.435    0.000 __init__.py:66(is_acceptable)
                8006880   13.974    0.000  262.570    0.000 functional.py:68(split)
               10674340  259.465    0.000  259.465    0.000 {built-in method max_pool2d}
               26048608   19.627    0.000  251.733    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                8006880   14.274    0.000  247.521    0.000 tensor.py:367(split)
               53379200  241.623    0.000  241.623    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               26048568   30.981    0.000  232.106    0.000 fromnumeric.py:2881(prod)
                8006880  231.887    0.000  231.887    0.000 {function Tensor.split at 0x7f8798acc940}
               48032280  222.825    0.000  222.825    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2668460  215.957    0.000  215.957    0.000 memory.py:35(<listcomp>)
               26048568   59.259    0.000  201.125    0.000 fromnumeric.py:70(_wrapreduction)
                2668960   17.136    0.000  178.141    0.000 collector.py:7(collect)
                2668460    7.114    0.000  175.786    0.000 loss.py:444(forward)
                2668960   30.077    0.000  172.638    0.000 environments.py:76(<listcomp>)
                2668460   25.467    0.000  168.672    0.000 functional.py:2621(mse_loss)
              240161454  138.507    0.000  161.526    0.000 tensor.py:725(grad)
                5337921  159.688    0.000  159.688    0.000 {built-in method builtins.sum}
              203026289  159.450    0.000  159.576    0.000 module.py:758(__getattr__)
               26685600  156.421    0.000  156.421    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              213638570   55.502    0.000  155.244    0.000 libenv.py:271(_maybe_copy_ndarray)
               28722365  152.082    0.000  152.082    0.000 {method 'reduce' of 'numpy.ufunc' objects}
               53379220   31.287    0.000  142.575    0.000 environments.py:79(reset)
              216155260  131.824    0.000  131.824    0.000 {built-in method torch._C._get_tracing_state}
                5336920  127.696    0.000  127.696    0.000 {built-in method gather}
               10674340   31.779    0.000   98.327    0.000 rnn.py:524(check_forward_args)
                2668460   94.135    0.000   94.135    0.000 {built-in method torch._C._nn.mse_loss}
               10674340   89.235    0.000   89.235    0.000 {method 't' of 'torch._C._TensorBase' objects}
              896644060   85.943    0.000   85.943    0.000 {method 'values' of 'collections.OrderedDict' objects}
               53440125   41.011    0.000   80.374    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8423563: <Base_v2_heist_0> in cluster <dcc> Done

Job <Base_v2_heist_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue Nov 24 19:48:56 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 25 23:28:59 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 25 23:28:59 2020
Terminated at Thu Nov 26 23:24:28 2020
Results reported at Thu Nov 26 23:24:28 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=60G]"
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

    CPU time :                                   92917.00 sec.
    Max Memory :                                 56779 MB
    Average Memory :                             56024.76 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4661.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86130 sec.
    Turnaround time :                            185732 sec.

The output (if any) is above this job summary.

