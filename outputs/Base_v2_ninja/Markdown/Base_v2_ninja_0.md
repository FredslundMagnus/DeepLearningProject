[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_ninja-0
    Discount :                  0.995
    Environment :               ninja
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


      9322505809 function calls (9118358535 primitive calls) in 86118.05 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86118.051 86118.051 {built-in method builtins.exec}
                      1    0.042    0.042 86118.051 86118.051 <string>:1(<module>)
                      1  499.212  499.212 86118.008 86118.008 main.py:12(main)
                2686442   99.135    0.000 51516.193    0.019 agent.py:46(learn)
                2685942  333.483    0.000 50633.283    0.019 agent.py:54(TD_learn)
                2685942  191.231    0.000 29556.491    0.011 memory.py:27(sample_distribution)
                2685942  314.507    0.000 28669.227    0.011 helpers.py:12(stack)
              364389445 18447.508    0.000 18447.508    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2686442   40.840    0.000 17932.762    0.007 agent.py:41(chooseMulti)
        217571302/13430210  920.526    0.000 14968.872    0.001 module.py:710(_call_impl)
               10744268  225.294    0.000 14682.060    0.001 agent.py:119(forward)
               24175032 14607.078    0.001 14607.080    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2686442  100.282    0.000 13664.596    0.005 agent.py:44(<listcomp>)
               24174978 13332.534    0.001 13332.534    0.001 {built-in method cat}
               53728840  146.248    0.000 13320.967    0.000 exploration.py:33(epsilonGreedy)
                2686442   71.775    0.000 9286.409    0.003 environments.py:73(step)
               32232804  229.271    0.000 8295.893    0.000 container.py:115(forward)
                2686442    8.302    0.000 6684.472    0.002 agent.py:32(rememberMulti)
                2686442  224.684    0.000 6676.170    0.002 agent.py:33(<listcomp>)
                2686442   51.875    0.000 5775.332    0.002 environments.py:75(<listcomp>)
               53863610 1516.082    0.000 5740.684    0.000 helpers.py:8(clean)
               64465608  110.703    0.000 4970.321    0.000 conv.py:418(forward)
               61921436 4924.385    0.000 4924.385    0.000 {built-in method as_tensor}
               64465608  136.932    0.000 4808.915    0.000 conv.py:410(_conv_forward)
               64465608 4649.747    0.000 4649.747    0.000 {built-in method conv2d}
                2685942   16.098    0.000 4097.495    0.002 tensor.py:155(backward)
                2685942   17.182    0.000 4089.754    0.002 grad_mode.py:12(decorate_context)
                2685942   18.473    0.000 4081.397    0.002 __init__.py:57(backward)
                2685942 1032.697    0.000 4053.061    0.002 adam.py:51(step)
                2685942 3992.864    0.001 3992.864    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2686442   54.765    0.000 3251.507    0.001 environments.py:74(<listcomp>)
               53728840  200.487    0.000 3196.742    0.000 interop.py:274(step)
               10744274  525.291    0.000 2901.145    0.000 rnn.py:109(flatten_parameters)
               10744268  118.816    0.000 2690.914    0.000 rnn.py:550(forward)
               10744268 2432.163    0.000 2432.163    0.000 {built-in method lstm}
               10744271 1758.004    0.000 1758.004    0.000 {built-in method _cudnn_rnn_flatten_weight}
               53728840   24.964    0.000 1555.034    0.000 wrapper.py:25(act)
               53728840   63.435    0.000 1530.070    0.000 env.py:197(act)
               53728840 1427.389    0.000 1432.498    0.000 libenv.py:352(act)
               75209876   79.847    0.000 1241.578    0.000 activation.py:653(forward)
               75209876  110.017    0.000 1161.731    0.000 functional.py:1277(leaky_relu)
               75209876 1041.337    0.000 1041.337    0.000 {built-in method torch._C._nn.leaky_relu}
              107592450   81.210    0.000  876.028    0.000 extract_dict_ob.py:9(observe)
              107592450   47.396    0.000  794.818    0.000 wrapper.py:19(observe)
                   5372    1.326    0.000  783.775    0.146 agent.py:81(update_target_network)
               96693912  754.553    0.000  754.553    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              107592450  198.352    0.000  747.422    0.000 libenv.py:344(observe)
                   5372  198.948    0.037  719.184    0.134 memory.py:37(update_distribution)
               10744268   27.589    0.000  675.626    0.000 linear.py:90(forward)
               96693912  664.101    0.000  664.101    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10744268   60.641    0.000  636.701    0.000 functional.py:1655(linear)
               56425526  608.998    0.000  608.998    0.000 {built-in method numpy.array}
               42978052  513.158    0.000  557.612    0.000 module.py:774(__setattr__)
              161321290  167.695    0.000  546.799    0.000 libenv.py:281(_maybe_copy_dict)
              483969242  467.898    0.000  467.898    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48346956  453.455    0.000  453.455    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10744268  422.492    0.000  422.492    0.000 {built-in method addmm}
               53728840   44.026    0.000  400.929    0.000 wrapper.py:22(get_info)
              377549655  397.060    0.000  397.060    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               48346956  391.781    0.000  391.781    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11712435  150.324    0.000  385.327    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2685942   65.650    0.000  380.949    0.000 optimizer.py:166(zero_grad)
                2685942  288.577    0.000  376.459    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               53728840  367.547    0.000  367.547    0.000 memory.py:15(inner)
               53728840  185.703    0.000  356.902    0.000 libenv.py:363(get_info)
               10744268   26.608    0.000  326.156    0.000 pooling.py:156(forward)
               48346956  314.380    0.000  314.380    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48346956  300.940    0.000  300.940    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10744268   18.240    0.000  299.548    0.000 _jit_internal.py:237(fn)
               26110952   24.812    0.000  282.090    0.000 <__array_function__ internals>:2(prod)
               10744268   19.925    0.000  279.483    0.000 functional.py:564(_max_pool2d)
               42977084  237.988    0.000  267.000    0.000 __init__.py:66(is_acceptable)
                8059326   14.144    0.000  265.580    0.000 functional.py:68(split)
               10744268  258.199    0.000  258.199    0.000 {built-in method max_pool2d}
               26110992   18.894    0.000  253.168    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                8059326   14.683    0.000  250.344    0.000 tensor.py:367(split)
               53728840  243.347    0.000  243.347    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               26110952   32.037    0.000  234.274    0.000 fromnumeric.py:2881(prod)
                8059326  234.223    0.000  234.223    0.000 {function Tensor.split at 0x7f262e7fc940}
                2685942  215.071    0.000  215.071    0.000 memory.py:35(<listcomp>)
               48346956  214.137    0.000  214.137    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               26110952   61.510    0.000  202.237    0.000 fromnumeric.py:70(_wrapreduction)
                2686442   30.624    0.000  187.795    0.000 environments.py:76(<listcomp>)
                2686442   16.954    0.000  175.199    0.000 collector.py:7(collect)
                2685942    6.636    0.000  175.092    0.000 loss.py:444(forward)
                2685942   26.130    0.000  168.456    0.000 functional.py:2621(mse_loss)
              241734834  142.305    0.000  164.996    0.000 tensor.py:725(grad)
              204356321  161.553    0.000  161.677    0.000 module.py:758(__getattr__)
               26860420  160.668    0.000  160.668    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               53728860   31.874    0.000  157.185    0.000 environments.py:79(reset)
              215184900   56.522    0.000  157.149    0.000 libenv.py:271(_maybe_copy_ndarray)
                5372885  157.001    0.000  157.001    0.000 {built-in method builtins.sum}
               28802266  150.513    0.000  150.513    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              217571302  135.961    0.000  135.961    0.000 {built-in method torch._C._get_tracing_state}
                5371884  126.872    0.000  126.872    0.000 {built-in method gather}
               10744268   30.426    0.000   93.636    0.000 rnn.py:524(check_forward_args)
                2685942   93.155    0.000   93.155    0.000 {built-in method torch._C._nn.mse_loss}
               10744268   88.926    0.000   88.926    0.000 {method 't' of 'torch._C._TensorBase' objects}
              902518012   85.430    0.000   85.430    0.000 {method 'values' of 'collections.OrderedDict' objects}
               53863650   39.721    0.000   80.798    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8423566: <Base_v2_ninja_0> in cluster <dcc> Done

Job <Base_v2_ninja_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue Nov 24 19:48:57 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Nov 27 01:44:32 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 01:44:32 2020
Terminated at Sat Nov 28 01:39:56 2020
Results reported at Sat Nov 28 01:39:56 2020

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

    CPU time :                                   93309.00 sec.
    Max Memory :                                 56606 MB
    Average Memory :                             55866.37 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4834.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86124 sec.
    Turnaround time :                            280259 sec.

The output (if any) is above this job summary.

