[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_caveflyer-0
    Discount :                  0.995
    Environment :               caveflyer
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


      9399007502 function calls (9193166112 primitive calls) in 86126.71 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86126.712 86126.712 {built-in method builtins.exec}
                      1    0.048    0.048 86126.712 86126.712 <string>:1(<module>)
                      1  481.145  481.145 86126.663 86126.663 main.py:12(main)
                2708733   95.926    0.000 50799.641    0.019 agent.py:46(learn)
                2708233  329.495    0.000 49925.585    0.018 agent.py:54(TD_learn)
                2708233  187.876    0.000 29026.635    0.011 memory.py:27(sample_distribution)
                2708233  278.389    0.000 28161.950    0.010 helpers.py:12(stack)
              367489864 18993.923    0.000 18993.923    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2708733   39.706    0.000 18351.041    0.007 agent.py:41(chooseMulti)
               24375651 14866.663    0.001 14866.680    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        219376873/13541665  912.022    0.000 14777.794    0.001 module.py:710(_call_impl)
               10833432  217.370    0.000 14493.943    0.001 agent.py:119(forward)
                2708733  101.385    0.000 14138.816    0.005 agent.py:44(<listcomp>)
               54174660  149.184    0.000 13796.802    0.000 exploration.py:33(epsilonGreedy)
               24375597 12624.415    0.001 12624.415    0.001 {built-in method cat}
                2708733   73.095    0.000 9534.157    0.004 environments.py:73(step)
               32500296  223.043    0.000 8190.124    0.000 container.py:115(forward)
                2708733    7.941    0.000 6751.829    0.002 agent.py:32(rememberMulti)
                2708733  225.424    0.000 6743.888    0.002 agent.py:33(<listcomp>)
                2708733   53.695    0.000 5792.237    0.002 environments.py:75(<listcomp>)
               54325154 1503.935    0.000 5757.568    0.000 helpers.py:8(clean)
               62449853 4930.380    0.000 4930.380    0.000 {built-in method as_tensor}
               65000592  112.970    0.000 4922.738    0.000 conv.py:418(forward)
               65000592  118.113    0.000 4761.690    0.000 conv.py:410(_conv_forward)
               65000592 4620.617    0.000 4620.617    0.000 {built-in method conv2d}
                2708233   16.819    0.000 4090.440    0.002 grad_mode.py:12(decorate_context)
                2708233   15.863    0.000 4087.682    0.002 tensor.py:155(backward)
                2708233   17.778    0.000 4071.818    0.002 __init__.py:57(backward)
                2708233 1024.266    0.000 4053.794    0.001 adam.py:51(step)
                2708233 3987.615    0.001 3987.615    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2708733   55.000    0.000 3480.045    0.001 environments.py:74(<listcomp>)
               54174660  198.092    0.000 3425.045    0.000 interop.py:274(step)
               10833438  498.247    0.000 2861.229    0.000 rnn.py:109(flatten_parameters)
               10833432  116.776    0.000 2676.067    0.000 rnn.py:550(forward)
               10833432 2409.210    0.000 2409.210    0.000 {built-in method lstm}
               54174660   25.248    0.000 1804.297    0.000 wrapper.py:25(act)
               54174660   64.206    0.000 1779.049    0.000 env.py:197(act)
               10833435 1765.059    0.000 1765.059    0.000 {built-in method _cudnn_rnn_flatten_weight}
               54174660 1675.227    0.000 1680.268    0.000 libenv.py:352(act)
               75834024   63.607    0.000 1206.413    0.000 activation.py:653(forward)
               75834024  106.650    0.000 1142.806    0.000 functional.py:1277(leaky_relu)
               75834024 1026.348    0.000 1026.348    0.000 {built-in method torch._C._nn.leaky_relu}
              108499814   79.777    0.000  863.899    0.000 extract_dict_ob.py:9(observe)
              108499814   46.341    0.000  784.122    0.000 wrapper.py:19(observe)
                   5417    1.300    0.000  778.130    0.144 agent.py:81(update_target_network)
               97496388  756.233    0.000  756.233    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              108499814  197.048    0.000  737.781    0.000 libenv.py:344(observe)
                   5417  200.433    0.037  713.917    0.132 memory.py:37(update_distribution)
               10833432   28.000    0.000  671.458    0.000 linear.py:90(forward)
               97496388  667.962    0.000  667.962    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10833432   58.114    0.000  632.735    0.000 functional.py:1655(linear)
               56893727  599.289    0.000  599.289    0.000 {built-in method numpy.array}
              162674474  164.525    0.000  540.784    0.000 libenv.py:281(_maybe_copy_dict)
               43334708  503.885    0.000  535.710    0.000 module.py:774(__setattr__)
              488028839  463.919    0.000  463.919    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48748194  455.780    0.000  455.780    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10833432  421.321    0.000  421.321    0.000 {built-in method addmm}
               54174660   44.879    0.000  398.954    0.000 wrapper.py:22(get_info)
              380730081  391.754    0.000  391.754    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               48748194  388.746    0.000  388.746    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11732756  148.499    0.000  385.215    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2708233   64.760    0.000  375.829    0.000 optimizer.py:166(zero_grad)
                2708233  284.949    0.000  371.097    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               54174660  366.652    0.000  366.652    0.000 memory.py:15(inner)
               54174660  181.933    0.000  354.075    0.000 libenv.py:363(get_info)
               10833432   30.382    0.000  330.969    0.000 pooling.py:156(forward)
               48748194  317.774    0.000  317.774    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48748194  301.767    0.000  301.767    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10833432   17.620    0.000  300.587    0.000 _jit_internal.py:237(fn)
               26173885   24.741    0.000  285.011    0.000 <__array_function__ internals>:2(prod)
               10833432   21.038    0.000  281.268    0.000 functional.py:564(_max_pool2d)
               43333740  237.085    0.000  264.838    0.000 __init__.py:66(is_acceptable)
                8126199   13.193    0.000  259.878    0.000 functional.py:68(split)
               10833432  258.936    0.000  258.936    0.000 {built-in method max_pool2d}
               26173925   19.527    0.000  256.220    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                8126199   14.995    0.000  245.677    0.000 tensor.py:367(split)
               54174660  240.630    0.000  240.630    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               26173885   32.406    0.000  236.693    0.000 fromnumeric.py:2881(prod)
                8126199  229.321    0.000  229.321    0.000 {function Tensor.split at 0x7f14b0bc7940}
               48748194  213.397    0.000  213.397    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2708233  204.728    0.000  204.728    0.000 memory.py:35(<listcomp>)
               26173885   60.630    0.000  204.287    0.000 fromnumeric.py:70(_wrapreduction)
                2708733   30.040    0.000  188.779    0.000 environments.py:76(<listcomp>)
                2708733   17.080    0.000  177.250    0.000 collector.py:7(collect)
                2708233    6.242    0.000  170.723    0.000 loss.py:444(forward)
                2708233   24.797    0.000  164.480    0.000 functional.py:2621(mse_loss)
              243741024  140.245    0.000  162.897    0.000 tensor.py:725(grad)
                5417467  159.001    0.000  159.001    0.000 {built-in method builtins.sum}
               54174680   30.189    0.000  158.767    0.000 environments.py:79(reset)
               27083330  158.296    0.000  158.296    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              216999628   55.444    0.000  154.940    0.000 libenv.py:271(_maybe_copy_ndarray)
              206052237  154.052    0.000  154.176    0.000 module.py:758(__getattr__)
               28887535  153.805    0.000  153.805    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              219376873  128.375    0.000  128.375    0.000 {built-in method torch._C._get_tracing_state}
                5416466  127.691    0.000  127.691    0.000 {built-in method gather}
               10833432   30.253    0.000   98.983    0.000 rnn.py:524(check_forward_args)
                2708233   91.606    0.000   91.606    0.000 {built-in method torch._C._nn.mse_loss}
               10833432   88.895    0.000   88.895    0.000 {method 't' of 'torch._C._TensorBase' objects}
              910007788   82.443    0.000   82.443    0.000 {method 'values' of 'collections.OrderedDict' objects}
               54325194   40.002    0.000   80.209    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8423560: <Base_v2_caveflyer_0> in cluster <dcc> Done

Job <Base_v2_caveflyer_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue Nov 24 19:48:56 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Nov 24 21:52:32 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 24 21:52:32 2020
Terminated at Wed Nov 25 21:48:09 2020
Results reported at Wed Nov 25 21:48:09 2020

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

    CPU time :                                   92705.00 sec.
    Max Memory :                                 56581 MB
    Average Memory :                             55832.41 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4859.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86138 sec.
    Turnaround time :                            93553 sec.

The output (if any) is above this job summary.

