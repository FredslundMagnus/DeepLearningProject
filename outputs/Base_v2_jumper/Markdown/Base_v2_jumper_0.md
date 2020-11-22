[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_jumper-0
    Discount :                  0.995
    Environment :               jumper
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


      9061864588 function calls (8863808258 primitive calls) in 86119.98 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86119.982 86119.982 {built-in method builtins.exec}
                      1    0.038    0.038 86119.982 86119.982 <string>:1(<module>)
                      1  472.984  472.984 86119.943 86119.943 main.py:11(main)
                2606298   98.372    0.000 53221.769    0.020 agent.py:46(learn)
                2605798  387.833    0.000 52386.967    0.020 agent.py:54(TD_learn)
                2605798  184.806    0.000 27477.896    0.011 memory.py:27(sample_distribution)
                2605798  279.540    0.000 26620.614    0.010 helpers.py:12(stack)
        211079638/13029490  918.136    0.000 16650.911    0.001 module.py:710(_call_impl)
               10423692  233.641    0.000 16350.764    0.002 agent.py:119(forward)
               23453736 14195.652    0.001 14195.655    0.001 {method 'to' of 'torch._C._TensorBase' objects}
              353250165 13939.755    0.000 13939.755    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2606298   44.170    0.000 13362.677    0.005 agent.py:41(chooseMulti)
               23453682 11763.620    0.001 11763.620    0.001 {built-in method cat}
                2606298   73.444    0.000 11202.949    0.004 environments.py:73(step)
               31271076  257.636    0.000 9373.107    0.000 container.py:115(forward)
                2606298  122.996    0.000 8642.938    0.003 agent.py:44(<listcomp>)
               52125960  177.134    0.000 8199.068    0.000 exploration.py:33(epsilonGreedy)
                2606298    8.316    0.000 7653.295    0.003 agent.py:32(rememberMulti)
                2606298  319.226    0.000 7644.978    0.003 agent.py:33(<listcomp>)
               52929929 1502.917    0.000 6070.812    0.000 helpers.py:8(clean)
                2606298   53.337    0.000 6015.037    0.002 environments.py:75(<listcomp>)
                2605798   17.407    0.000 5674.670    0.002 grad_mode.py:12(decorate_context)
                2605798 1343.366    0.001 5636.633    0.002 adam.py:51(step)
               62542152  111.553    0.000 5617.327    0.000 conv.py:418(forward)
               62542152  120.637    0.000 5458.390    0.000 conv.py:410(_conv_forward)
               62542152 5316.802    0.000 5316.802    0.000 {built-in method conv2d}
               60747323 5259.304    0.000 5259.304    0.000 {built-in method as_tensor}
                2605798   15.425    0.000 4805.214    0.002 tensor.py:155(backward)
                2605798   20.830    0.000 4789.789    0.002 __init__.py:57(backward)
                2606298   58.365    0.000 4755.690    0.002 environments.py:74(<listcomp>)
               52125960  218.147    0.000 4697.326    0.000 interop.py:274(step)
                2605798 4689.542    0.002 4689.542    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10423698  527.371    0.000 3420.343    0.000 rnn.py:109(flatten_parameters)
               52125960   26.572    0.000 2886.521    0.000 wrapper.py:25(act)
               52125960   83.345    0.000 2859.950    0.000 env.py:197(act)
               10423692  115.311    0.000 2753.102    0.000 rnn.py:550(forward)
               52125960 2722.717    0.000 2727.658    0.000 libenv.py:352(act)
               10423692 2500.772    0.000 2500.772    0.000 {built-in method lstm}
               10423695 2269.778    0.000 2269.778    0.000 {built-in method _cudnn_rnn_flatten_weight}
               72965844   65.581    0.000 1505.495    0.000 activation.py:653(forward)
               72965844  107.548    0.000 1439.915    0.000 functional.py:1277(leaky_relu)
               72965844 1322.920    0.000 1322.920    0.000 {built-in method torch._C._nn.leaky_relu}
               93808728 1117.881    0.000 1117.881    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              105055889   91.015    0.000  994.996    0.000 extract_dict_ob.py:9(observe)
               93808728  987.263    0.000  987.263    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              105055889   49.042    0.000  903.981    0.000 wrapper.py:19(observe)
              105055889  227.306    0.000  854.939    0.000 libenv.py:344(observe)
               10423692   27.773    0.000  751.132    0.000 linear.py:90(forward)
                   5212    1.254    0.000  736.430    0.141 agent.py:81(update_target_network)
               10423692   57.883    0.000  713.033    0.000 functional.py:1655(linear)
                   5212  189.690    0.036  671.496    0.129 memory.py:37(update_distribution)
              157181849  178.037    0.000  615.589    0.000 libenv.py:281(_maybe_copy_dict)
               46904364  612.635    0.000  612.635    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               54742182  586.124    0.000  586.124    0.000 {built-in method numpy.array}
              364671257  567.384    0.000  567.384    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                2605798   85.428    0.000  554.730    0.000 optimizer.py:166(zero_grad)
              471550759  548.122    0.000  548.122    0.000 {method 'copy' of 'numpy.ndarray' objects}
               41695748  497.908    0.000  528.738    0.000 module.py:774(__setattr__)
               46904364  521.552    0.000  521.552    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               10423692  484.509    0.000  484.509    0.000 {built-in method addmm}
               46904364  453.949    0.000  453.949    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46904364  446.742    0.000  446.742    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               52125960   47.829    0.000  441.665    0.000 wrapper.py:22(get_info)
               11631555  170.810    0.000  422.199    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               52125960  205.341    0.000  393.836    0.000 libenv.py:363(get_info)
               52125960  383.721    0.000  383.721    0.000 memory.py:15(inner)
                2605798  293.271    0.000  382.115    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               10423692   24.211    0.000  362.057    0.000 pooling.py:156(forward)
                2606298   30.157    0.000  358.778    0.000 environments.py:76(<listcomp>)
               46904364  341.877    0.000  341.877    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10423692   16.973    0.000  337.845    0.000 _jit_internal.py:237(fn)
               52125980   37.992    0.000  328.635    0.000 environments.py:79(reset)
               52125960  320.874    0.000  320.874    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               10423692   18.949    0.000  319.249    0.000 functional.py:564(_max_pool2d)
               25869048   24.791    0.000  300.360    0.000 <__array_function__ internals>:2(prod)
               10423692  299.045    0.000  299.045    0.000 {built-in method max_pool2d}
               41694780  248.535    0.000  280.728    0.000 __init__.py:66(is_acceptable)
               25869088   19.658    0.000  271.281    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7818894   13.055    0.000  266.122    0.000 functional.py:68(split)
                7818894   14.197    0.000  252.139    0.000 tensor.py:367(split)
               25869048   32.150    0.000  251.623    0.000 fromnumeric.py:2881(prod)
                7818894  236.518    0.000  236.518    0.000 {function Tensor.split at 0x7fe9360e8940}
               25869048   59.719    0.000  219.473    0.000 fromnumeric.py:70(_wrapreduction)
               26058980  192.543    0.000  192.543    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2605798  189.442    0.000  189.442    0.000 memory.py:35(<listcomp>)
                2605798    6.356    0.000  188.709    0.000 loss.py:444(forward)
              234521874  159.438    0.000  182.845    0.000 tensor.py:725(grad)
                2605798   24.729    0.000  182.353    0.000 functional.py:2621(mse_loss)
                2606298   17.116    0.000  180.709    0.000 collector.py:7(collect)
              210111778   57.198    0.000  180.612    0.000 libenv.py:271(_maybe_copy_ndarray)
               28480058  169.323    0.000  169.323    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                5212597  162.394    0.000  162.394    0.000 {built-in method builtins.sum}
              211079638  161.065    0.000  161.065    0.000 {built-in method torch._C._get_tracing_state}
                5211596  152.645    0.000  152.645    0.000 {built-in method gather}
              198258977  146.801    0.000  146.922    0.000 module.py:758(__getattr__)
                2605798  109.602    0.000  109.602    0.000 {built-in method torch._C._nn.mse_loss}
               10423692  107.233    0.000  107.233    0.000 {method 't' of 'torch._C._TensorBase' objects}
               10423692   28.548    0.000   89.383    0.000 rnn.py:524(check_forward_args)
               52929969   43.084    0.000   88.396    0.000 types.py:163(multimap)
              875589628   82.894    0.000   82.894    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8410445: <Base_v2_jumper_0> in cluster <dcc> Done

Job <Base_v2_jumper_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Sat Nov 21 14:15:16 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov 21 14:34:23 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 21 14:34:23 2020
Terminated at Sun Nov 22 14:29:49 2020
Results reported at Sun Nov 22 14:29:49 2020

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=80G]"
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

    CPU time :                                   90161.00 sec.
    Max Memory :                                 56460 MB
    Average Memory :                             55750.66 MB
    Total Requested Memory :                     81920.00 MB
    Delta Memory :                               25460.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86126 sec.
    Turnaround time :                            87273 sec.

The output (if any) is above this job summary.

