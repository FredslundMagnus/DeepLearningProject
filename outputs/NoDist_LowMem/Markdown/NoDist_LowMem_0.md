[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NoDist_LowMem-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    50000.0
    Update every :              100
    Use distribution :          0.0
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      12894196490 function calls (12694543574 primitive calls) in 86115.54 seconds

##    Ordered by: cumulative time
   List reduced from 1314 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86115.541 86115.541 {built-in method builtins.exec}
                      1    0.022    0.022 86115.541 86115.541 <string>:1(<module>)
                      1  538.400  538.400 86115.518 86115.518 main.py:9(main)
                2936057  112.237    0.000 60086.373    0.020 agent.py:46(learn)
                2935957  365.321    0.000 59375.622    0.020 agent.py:54(TD_learn)
                2935957 2622.157    0.001 38106.858    0.013 memory.py:23(sample)
                2935957  328.063    0.000 34502.208    0.012 helpers.py:12(stack)
               26423961 16964.695    0.001 16964.703    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               26423913 16768.654    0.001 16768.654    0.001 {built-in method cat}
        214326661/14679885  970.546    0.000 15022.674    0.001 module.py:710(_call_impl)
               11743928  239.708    0.000 14698.833    0.001 agent.py:117(forward)
                2936057   84.015    0.000 11092.903    0.004 environments.py:73(step)
               35231784  235.239    0.000 8045.164    0.000 container.py:115(forward)
              410548061 7976.960    0.000 7976.960    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2936057    8.969    0.000 7948.592    0.003 agent.py:32(rememberMulti)
                2936057  273.185    0.000 7939.623    0.003 agent.py:33(<listcomp>)
                2936057   61.684    0.000 6595.333    0.002 environments.py:75(<listcomp>)
               58883658 1795.419    0.000 6553.554    0.000 helpers.py:8(clean)
                2936057   44.841    0.000 6217.187    0.002 agent.py:41(chooseMulti)
               67691529 5524.745    0.000 5524.745    0.000 {built-in method as_tensor}
               58719640  105.217    0.000 4648.249    0.000 conv.py:418(forward)
               58719640  119.564    0.000 4498.865    0.000 conv.py:410(_conv_forward)
               58719640 4358.328    0.000 4358.328    0.000 {built-in method conv2d}
                2936057   63.681    0.000 4194.474    0.001 environments.py:74(<listcomp>)
                2935957   18.817    0.000 4172.601    0.001 grad_mode.py:12(decorate_context)
                2935957   18.388    0.000 4133.374    0.001 tensor.py:155(backward)
                2935957 1057.563    0.000 4131.823    0.001 adam.py:51(step)
               58721140  230.726    0.000 4130.793    0.000 interop.py:274(step)
                2935957   20.274    0.000 4114.986    0.001 __init__.py:57(backward)
                2935957 4017.249    0.001 4017.249    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11743934  546.882    0.000 3032.561    0.000 rnn.py:109(flatten_parameters)
               11743928  130.757    0.000 2779.375    0.000 rnn.py:550(forward)
               11743928 2492.912    0.000 2492.912    0.000 {built-in method lstm}
               58721140   27.155    0.000 2211.895    0.000 wrapper.py:25(act)
               58721140   77.313    0.000 2184.740    0.000 env.py:197(act)
               58721140 2055.905    0.000 2061.705    0.000 libenv.py:352(act)
               11743931 1857.836    0.000 1857.836    0.000 {built-in method _cudnn_rnn_flatten_weight}
                2936057  108.024    0.000 1811.248    0.001 agent.py:44(<listcomp>)
               58721140  175.254    0.000 1446.683    0.000 exploration.py:31(epsilonGreedy)
               70463568   67.029    0.000 1193.123    0.000 activation.py:653(forward)
               70463568  109.917    0.000 1126.094    0.000 functional.py:1277(leaky_relu)
              117604798   91.493    0.000 1023.341    0.000 extract_dict_ob.py:9(observe)
               70463568 1006.154    0.000 1006.154    0.000 {built-in method torch._C._nn.leaky_relu}
                2935957  388.740    0.000  968.550    0.000 random.py:315(sample)
              117604798   52.774    0.000  931.848    0.000 wrapper.py:19(observe)
              117604798  233.661    0.000  879.074    0.000 libenv.py:344(observe)
               93950624  766.065    0.000  766.065    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11743928   32.539    0.000  742.539    0.000 linear.py:90(forward)
               11743928   66.835    0.000  696.973    0.000 functional.py:1655(linear)
               93950624  660.276    0.000  660.276    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              176325938  191.805    0.000  641.452    0.000 libenv.py:281(_maybe_copy_dict)
                  29360    6.286    0.000  598.513    0.020 agent.py:81(update_target_network)
              529007174  552.431    0.000  552.431    0.000 {method 'copy' of 'numpy.ndarray' objects}
               46976587  499.298    0.000  535.001    0.000 module.py:774(__setattr__)
               58721140   52.818    0.000  472.441    0.000 wrapper.py:22(get_info)
               46975312  470.345    0.000  470.345    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              424902850  470.259    0.000  470.259    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              753533343  313.411    0.000  466.694    0.000 random.py:250(_randbelow_with_getrandbits)
               11743928  459.228    0.000  459.228    0.000 {built-in method addmm}
               58721140  423.255    0.000  423.255    0.000 memory.py:15(inner)
               58721140  219.687    0.000  419.623    0.000 libenv.py:363(get_info)
                2935957   72.622    0.000  400.677    0.000 optimizer.py:166(zero_grad)
               46975312  393.570    0.000  393.570    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11743928   29.231    0.000  358.389    0.000 pooling.py:156(forward)
               58779860  349.901    0.000  349.901    0.000 {built-in method numpy.array}
                  29360   87.191    0.003  334.859    0.011 memory.py:37(update_distribution)
               11743928   20.110    0.000  329.158    0.000 _jit_internal.py:237(fn)
               46975312  323.489    0.000  323.489    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46975312  316.352    0.000  316.352    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11743928   22.301    0.000  307.041    0.000 functional.py:564(_max_pool2d)
               11743928  283.156    0.000  283.156    0.000 {built-in method max_pool2d}
                8808171   13.745    0.000  280.996    0.000 functional.py:68(split)
                8808171   14.207    0.000  266.133    0.000 tensor.py:367(split)
               58721140  256.540    0.000  256.540    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8808171  250.497    0.000  250.497    0.000 {function Tensor.split at 0x7f75b9c33940}
               46975724  214.627    0.000  246.949    0.000 __init__.py:66(is_acceptable)
               46975312  219.103    0.000  219.103    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2936057   34.127    0.000  219.081    0.000 environments.py:76(<listcomp>)
                2936057   20.068    0.000  210.220    0.000 collector.py:7(collect)
                2935957    7.599    0.000  193.079    0.000 loss.py:444(forward)
                5872115  188.779    0.000  188.779    0.000 {built-in method builtins.sum}
                2935957   29.017    0.000  185.480    0.000 functional.py:2621(mse_loss)
               58721160   37.169    0.000  184.995    0.000 environments.py:79(reset)
              235209596   65.543    0.000  183.946    0.000 libenv.py:271(_maybe_copy_ndarray)
              234876608  149.512    0.000  172.310    0.000 tensor.py:725(grad)
               29359770  164.856    0.000  164.856    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              200704055  159.432    0.000  160.032    0.000 module.py:758(__getattr__)
                  58720   16.047    0.000  146.574    0.002 {built-in method _pickle.loads}
                5871914  143.136    0.000  143.136    0.000 {built-in method gather}
              214326661  138.775    0.000  138.775    0.000 {built-in method torch._C._get_tracing_state}
                  58720   27.820    0.000  110.794    0.002 {built-in method _pickle.dumps}
              987787882  106.965    0.000  106.965    0.000 {method 'getrandbits' of '_random.Random' objects}
                2935957  102.850    0.000  102.850    0.000 {built-in method torch._C._nn.mse_loss}
               11743928   33.119    0.000  102.368    0.000 rnn.py:524(check_forward_args)
                1056958    1.212    0.000  101.039    0.000 storage.py:141(_load_from_bytes)
                1056958    5.242    0.000   99.827    0.000 serialization.py:486(load)
               11743928   99.125    0.000   99.125    0.000 {method 't' of 'torch._C._TensorBase' objects}
               58883698   45.262    0.000   91.656    0.000 types.py:163(multimap)
              392296993   77.812    0.000   90.685    0.000 {built-in method builtins.isinstance}
              892538428   87.347    0.000   87.347    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 8366050: <NoDist_LowMem_0> in cluster <dcc> Done

Job <NoDist_LowMem_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Nov 16 19:57:02 2020
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov 16 20:47:20 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 16 20:47:20 2020
Terminated at Tue Nov 17 20:42:41 2020
Results reported at Tue Nov 17 20:42:41 2020

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
    Max Memory :                                 8494 MB
    Average Memory :                             8255.75 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               22226.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86122 sec.
    Turnaround time :                            89139 sec.

The output (if any) is above this job summary.

