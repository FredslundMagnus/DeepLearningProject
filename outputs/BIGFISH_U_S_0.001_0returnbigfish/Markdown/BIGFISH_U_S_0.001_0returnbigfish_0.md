[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      BIGFISH_U_S_0.001_0returnbigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              1000
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           1000
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0.001
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      10398938671 function calls (10159383194 primitive calls) in 82527.58 seconds

##    Ordered by: cumulative time
   List reduced from 1336 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 82527.578 82527.578 {built-in method builtins.exec}
                      1    0.036    0.036 82527.578 82527.578 <string>:1(<module>)
                      1  525.952  525.952 82527.541 82527.541 main.py:92(main)
                2437956  255.129    0.000 54725.839    0.022 agent.py:84(learn)
                2341004  935.835    0.000 53898.338    0.023 agent.py:99(TD_learn)
                2341004  164.349    0.000 25339.076    0.011 memory.py:35(sample_distribution)
                2341004  288.169    0.000 24555.820    0.010 helpers.py:15(stack)
        256033842/16484979 1094.884    0.000 16152.779    0.001 module.py:710(_call_impl)
                7119964  225.427    0.000 14927.646    0.002 agent.py:231(forward)
               23702003 12809.255    0.001 12809.274    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               21359892 11270.137    0.001 11270.137    0.001 {built-in method cat}
                2437956  216.918    0.000 10936.685    0.004 agent.py:70(chooseMulti)
               37941823  310.802    0.000 10356.028    0.000 container.py:115(forward)
              318503217 8966.899    0.000 8966.899    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2437956   68.699    0.000 8770.834    0.004 environments.py:83(step)
                7023012   40.211    0.000 8523.880    0.001 grad_mode.py:12(decorate_context)
                7023012 2025.316    0.000 8435.656    0.001 adam.py:51(step)
                2342003   97.666    0.000 7370.004    0.003 agent.py:58(rememberMulti)
                2342003  296.773    0.000 6899.372    0.003 agent.py:62(<listcomp>)
                7023012   29.950    0.000 6334.380    0.001 tensor.py:155(backward)
                7023012   35.288    0.000 6304.430    0.001 __init__.py:57(backward)
                7023012 6094.201    0.001 6094.201    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2437956   69.319    0.000 5597.831    0.002 environments.py:85(<listcomp>)
               48904440 1372.275    0.000 5547.530    0.000 helpers.py:8(clean)
               55927452 4734.795    0.000 4734.795    0.000 {built-in method as_tensor}
                2342003  103.980    0.000 4146.160    0.002 agent.py:82(<listcomp>)
               42719784   75.695    0.000 3833.185    0.000 conv.py:418(forward)
               46840060  154.118    0.000 3760.107    0.000 exploration.py:34(epsilonGreedy)
               42719784   87.867    0.000 3721.904    0.000 conv.py:410(_conv_forward)
               42719784 3619.181    0.000 3619.181    0.000 {built-in method conv2d}
               56865757  116.600    0.000 3192.969    0.000 linear.py:90(forward)
               56865757  318.186    0.000 3020.043    0.000 functional.py:1655(linear)
                2437956   50.245    0.000 2913.873    0.001 environments.py:84(<listcomp>)
               48759120  191.455    0.000 2863.627    0.000 interop.py:274(step)
                7119970  381.963    0.000 2431.693    0.000 rnn.py:109(flatten_parameters)
                7119964   84.914    0.000 1892.696    0.000 rnn.py:550(forward)
               49839748 1806.672    0.000 1806.672    0.000 {built-in method addmm}
                7119964 1703.453    0.000 1703.453    0.000 {built-in method lstm}
               90123574   79.352    0.000 1701.763    0.000 activation.py:653(forward)
              140460240 1676.357    0.000 1676.357    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               90123574  111.982    0.000 1622.411    0.000 functional.py:1277(leaky_relu)
                7119967 1576.412    0.000 1576.412    0.000 {built-in method _cudnn_rnn_flatten_weight}
               90123574 1499.134    0.000 1499.134    0.000 {built-in method torch._C._nn.leaky_relu}
              140460240 1478.352    0.000 1478.352    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               48759120   21.061    0.000 1278.187    0.000 wrapper.py:25(act)
               48759120   72.229    0.000 1257.127    0.000 env.py:197(act)
               48759120 1138.457    0.000 1142.748    0.000 libenv.py:352(act)
               70230120  922.910    0.000  922.910    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               97663560   78.038    0.000  840.456    0.000 extract_dict_ob.py:9(observe)
                7023012  130.494    0.000  835.378    0.000 optimizer.py:166(zero_grad)
               70230120  775.457    0.000  775.457    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               97663560   41.885    0.000  762.418    0.000 wrapper.py:19(observe)
               97663560  183.688    0.000  720.533    0.000 libenv.py:344(observe)
               70230120  675.725    0.000  675.725    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               70230120  657.808    0.000  657.808    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2342003    6.343    0.000  606.059    0.000 agent.py:249(avoid_similar_state)
              362138662  575.763    0.000  575.763    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                   2437    0.941    0.000  572.372    0.235 agent.py:157(update_target_network)
              146422680  153.915    0.000  523.914    0.000 libenv.py:281(_maybe_copy_dict)
               70230120  512.878    0.000  512.878    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              439270477  466.480    0.000  466.480    0.000 {method 'copy' of 'numpy.ndarray' objects}
                7023012   13.477    0.000  463.420    0.000 loss.py:444(forward)
               56865757  458.346    0.000  458.346    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7023012   55.636    0.000  449.943    0.000 functional.py:2621(mse_loss)
               11366664  156.673    0.000  398.627    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               33163699  368.038    0.000  392.203    0.000 module.py:774(__setattr__)
               48759120   45.432    0.000  388.572    0.000 wrapper.py:22(get_info)
               46840060  370.935    0.000  370.935    0.000 memory.py:17(inner)
               14046024  349.530    0.000  349.530    0.000 {built-in method gather}
               48759120  180.933    0.000  343.140    0.000 libenv.py:363(get_info)
                2341004  259.867    0.000  338.281    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               54230900  316.575    0.000  316.575    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               51104998  308.726    0.000  308.726    0.000 {built-in method numpy.array}
                   2437   86.768    0.036  305.108    0.125 memory.py:45(update_distribution)
                2342003  269.688    0.000  301.890    0.000 agent.py:149(convert_values)
               48759120  292.447    0.000  292.447    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               25074472   24.514    0.000  285.736    0.000 <__array_function__ internals>:2(prod)
              351150708  234.912    0.000  269.445    0.000 tensor.py:725(grad)
                7023012  267.206    0.000  267.206    0.000 {built-in method torch._C._nn.mse_loss}
                7119964   23.770    0.000  258.966    0.000 pooling.py:156(forward)
               25074512   18.872    0.000  257.122    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                   4874  215.848    0.044  242.316    0.050 {built-in method _pickle.loads}
               25074472   30.946    0.000  238.250    0.000 fromnumeric.py:2881(prod)
                7313868   12.452    0.000  237.781    0.000 functional.py:68(split)
                7119964   12.733    0.000  235.196    0.000 _jit_internal.py:237(fn)
                7313868   13.881    0.000  224.420    0.000 tensor.py:367(split)
                7119964   13.639    0.000  221.280    0.000 functional.py:564(_max_pool2d)
               28479868  195.337    0.000  219.401    0.000 __init__.py:66(is_acceptable)
                7026009  217.743    0.000  217.743    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                2527213  209.050    0.000  209.050    0.000 {built-in method tensor}
                7313868  208.905    0.000  208.905    0.000 {function Tensor.split at 0x7f99a6ef09d0}
               25074472   57.868    0.000  207.304    0.000 fromnumeric.py:70(_wrapreduction)
                7119964  206.788    0.000  206.788    0.000 {built-in method max_pool2d}
               14047023  202.479    0.000  202.479    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                2437956   26.550    0.000  190.432    0.000 environments.py:86(<listcomp>)
              256033842  186.572    0.000  186.572    0.000 {built-in method torch._C._get_tracing_state}
                2341004  186.299    0.000  186.299    0.000 memory.py:43(<listcomp>)
              251548421  174.313    0.000  174.415    0.000 module.py:758(__getattr__)
                7023012   38.367    0.000  172.466    0.000 __init__.py:25(_make_grads)
                2437956   19.153    0.000  164.223    0.000 collector.py:8(collect)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 8557629: <BIGFISH_U_S_0.001_0returnbigfish_0> in cluster <dcc> Done

Job <BIGFISH_U_S_0.001_0returnbigfish_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Fri Dec 11 16:01:47 2020
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Dec 16 04:06:38 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 16 04:06:38 2020
Terminated at Thu Dec 17 03:02:16 2020
Results reported at Thu Dec 17 03:02:16 2020

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

    CPU time :                                   85173.00 sec.
    Max Memory :                                 54116 MB
    Average Memory :                             53402.63 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7324.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82539 sec.
    Turnaround time :                            471629 sec.

The output (if any) is above this job summary.

