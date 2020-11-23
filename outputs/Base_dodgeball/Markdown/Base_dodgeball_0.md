[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_dodgeball-0
    Discount :                  0.999
    Environment :               dodgeball
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


      10925117867 function calls (10700994555 primitive calls) in 86130.96 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86130.962 86130.962 {built-in method builtins.exec}
                      1    0.011    0.011 86130.961 86130.961 <string>:1(<module>)
                      1  545.373  545.373 86130.949 86130.949 main.py:11(main)
                3295916  111.981    0.000 58762.192    0.018 agent.py:46(learn)
                3295816  400.009    0.000 56903.495    0.017 agent.py:54(TD_learn)
                3295816  212.171    0.000 34132.546    0.010 memory.py:27(sample_distribution)
                3295816  303.723    0.000 33089.217    0.010 helpers.py:12(stack)
               29662692 17806.359    0.001 17806.362    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        240596368/16479180 1015.066    0.000 16057.149    0.001 module.py:710(_call_impl)
               13183364  260.656    0.000 15706.145    0.001 agent.py:117(forward)
               29662644 14606.253    0.000 14606.253    0.000 {built-in method cat}
                3295916   89.523    0.000 11384.329    0.003 environments.py:73(step)
               39550092  246.492    0.000 8596.697    0.000 container.py:115(forward)
              458928193 8578.584    0.000 8578.584    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3295916    9.994    0.000 7946.971    0.002 agent.py:32(rememberMulti)
                3295916  282.422    0.000 7936.976    0.002 agent.py:33(<listcomp>)
                3295916   48.372    0.000 7232.953    0.002 agent.py:41(chooseMulti)
                3295916   57.937    0.000 6753.862    0.002 environments.py:75(<listcomp>)
               66212773 1835.926    0.000 6729.024    0.000 helpers.py:8(clean)
               76100221 5637.016    0.000 5637.016    0.000 {built-in method as_tensor}
               65916820  109.611    0.000 4982.439    0.000 conv.py:418(forward)
               65916820  132.144    0.000 4826.079    0.000 conv.py:410(_conv_forward)
               65916820 4671.595    0.000 4671.595    0.000 {built-in method conv2d}
                3295816   19.783    0.000 4513.339    0.001 grad_mode.py:12(decorate_context)
                3295816 1146.411    0.000 4470.042    0.001 adam.py:51(step)
                3295816   18.184    0.000 4406.388    0.001 tensor.py:155(backward)
                3295816   24.586    0.000 4388.204    0.001 __init__.py:57(backward)
                3295916   66.034    0.000 4297.356    0.001 environments.py:74(<listcomp>)
                3295816 4280.633    0.001 4280.633    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               65918320  242.548    0.000 4231.321    0.000 interop.py:274(step)
               13183370  584.489    0.000 3269.009    0.000 rnn.py:109(flatten_parameters)
               13183364  139.655    0.000 2936.410    0.000 rnn.py:550(forward)
               13183364 2625.854    0.000 2625.854    0.000 {built-in method lstm}
                3295916  118.707    0.000 2537.439    0.001 agent.py:44(<listcomp>)
               65918320   33.428    0.000 2187.508    0.000 wrapper.py:25(act)
               65918320   85.847    0.000 2154.080    0.000 env.py:197(act)
               65918320  184.961    0.000 2139.936    0.000 exploration.py:31(epsilonGreedy)
               65918320 2015.824    0.000 2022.015    0.000 libenv.py:352(act)
               13183367 1999.452    0.000 1999.452    0.000 {built-in method _cudnn_rnn_flatten_weight}
                  32959    6.112    0.000 1746.715    0.053 agent.py:81(update_target_network)
                  32959  447.409    0.014 1467.058    0.045 memory.py:37(update_distribution)
               79100184   70.755    0.000 1289.944    0.000 activation.py:653(forward)
               79100184  117.553    0.000 1219.189    0.000 functional.py:1277(leaky_relu)
               69279855 1132.069    0.000 1132.069    0.000 {built-in method numpy.array}
              132131093   98.530    0.000 1093.439    0.000 extract_dict_ob.py:9(observe)
               79100184 1090.352    0.000 1090.352    0.000 {built-in method torch._C._nn.leaky_relu}
              132131093   60.783    0.000  994.910    0.000 wrapper.py:19(observe)
              132131093  261.714    0.000  934.127    0.000 libenv.py:344(observe)
              105466112  824.909    0.000  824.909    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13183364   37.255    0.000  798.733    0.000 linear.py:90(forward)
               13183364   71.063    0.000  748.603    0.000 functional.py:1655(linear)
              105466112  725.558    0.000  725.558    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              198049413  207.630    0.000  664.222    0.000 libenv.py:281(_maybe_copy_dict)
              594181198  577.792    0.000  577.792    0.000 {method 'copy' of 'numpy.ndarray' objects}
               52734331  532.202    0.000  569.117    0.000 module.py:774(__setattr__)
               52733056  503.245    0.000  503.245    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               65918320   58.519    0.000  500.671    0.000 wrapper.py:22(get_info)
              474818407  499.323    0.000  499.323    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               13183364  495.500    0.000  495.500    0.000 {built-in method addmm}
                3295816  356.452    0.000  473.340    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               65918320  229.739    0.000  442.152    0.000 libenv.py:363(get_info)
               52733056  420.417    0.000  420.417    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3295816   71.065    0.000  416.588    0.000 optimizer.py:166(zero_grad)
               65918320  406.265    0.000  406.265    0.000 memory.py:15(inner)
               13183364   27.480    0.000  378.554    0.000 pooling.py:156(forward)
               52733056  354.822    0.000  354.822    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               13183364   20.834    0.000  351.074    0.000 _jit_internal.py:237(fn)
               52733056  337.129    0.000  337.129    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13183364   23.630    0.000  328.044    0.000 functional.py:564(_max_pool2d)
               13183364  302.741    0.000  302.741    0.000 {built-in method max_pool2d}
                9887748   15.030    0.000  301.102    0.000 functional.py:68(split)
                9887748   15.933    0.000  284.826    0.000 tensor.py:367(split)
               65918320  278.795    0.000  278.795    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               52733468  235.395    0.000  272.795    0.000 __init__.py:66(is_acceptable)
                9887748  267.283    0.000  267.283    0.000 {function Tensor.split at 0x7f526ad0a940}
                3295916   36.636    0.000  243.587    0.000 environments.py:76(<listcomp>)
                3295617  241.612    0.000  241.612    0.000 memory.py:35(<listcomp>)
               52733056  235.386    0.000  235.386    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3295916   19.760    0.000  221.088    0.000 collector.py:7(collect)
                3295816    8.173    0.000  209.035    0.000 loss.py:444(forward)
               65918340   41.958    0.000  206.984    0.000 environments.py:79(reset)
                3295816   31.108    0.000  200.863    0.000 functional.py:2621(mse_loss)
              264262186   67.868    0.000  200.242    0.000 libenv.py:271(_maybe_copy_ndarray)
                6591833  199.944    0.000  199.944    0.000 {built-in method builtins.sum}
              263665328  154.084    0.000  179.078    0.000 tensor.py:725(grad)
               32958360  176.493    0.000  176.493    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              225304031  166.363    0.000  167.041    0.000 module.py:758(__getattr__)
                  65918   16.854    0.000  156.667    0.002 {built-in method _pickle.loads}
                6591632  149.313    0.000  149.313    0.000 {built-in method gather}
              240596368  144.141    0.000  144.141    0.000 {built-in method torch._C._get_tracing_state}
                  65918   28.856    0.000  116.878    0.002 {built-in method _pickle.dumps}
               13183364   38.531    0.000  114.891    0.000 rnn.py:524(check_forward_args)
                3295816  111.317    0.000  111.317    0.000 {built-in method torch._C._nn.mse_loss}
                8296050   12.278    0.000  110.649    0.000 <__array_function__ internals>:2(prod)
                1186522    1.299    0.000  107.993    0.000 storage.py:141(_load_from_bytes)
                1186522    5.600    0.000  106.694    0.000 serialization.py:486(load)
               13183364  106.059    0.000  106.059    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8296090    8.606    0.000   96.754    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               66212813   49.450    0.000   96.167    0.000 types.py:163(multimap)
             1001935564   95.773    0.000   95.773    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8371230: <Base_dodgeball_0> in cluster <dcc> Done

Job <Base_dodgeball_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:31 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Nov 19 05:09:32 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Nov 19 05:09:32 2020
Terminated at Fri Nov 20 05:05:18 2020
Results reported at Fri Nov 20 05:05:18 2020

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

    CPU time :                                   88136.00 sec.
    Max Memory :                                 25413 MB
    Average Memory :                             25080.85 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5307.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86148 sec.
    Turnaround time :                            198527 sec.

The output (if any) is above this job summary.

