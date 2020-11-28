[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_plunder-0
    Discount :                  0.995
    Environment :               plunder
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


      9333338071 function calls (9128929129 primitive calls) in 86114.62 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86114.625 86114.625 {built-in method builtins.exec}
                      1    0.037    0.037 86114.625 86114.625 <string>:1(<module>)
                      1  389.793  389.793 86114.587 86114.587 main.py:12(main)
                2689885   90.636    0.000 52868.510    0.020 agent.py:46(learn)
                2689385  349.047    0.000 52042.848    0.019 agent.py:54(TD_learn)
                2689385  171.695    0.000 26978.483    0.010 memory.py:27(sample_distribution)
                2689385  272.838    0.000 26140.283    0.010 helpers.py:12(stack)
        217850185/13447425  927.194    0.000 16586.564    0.001 module.py:710(_call_impl)
               10758040  230.790    0.000 16295.578    0.002 agent.py:119(forward)
              364870634 15012.526    0.000 15012.526    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2689885   41.997    0.000 14316.163    0.005 agent.py:41(chooseMulti)
               24206019 13890.128    0.001 13890.178    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               24205965 11674.844    0.000 11674.844    0.000 {built-in method cat}
                2689885   70.563    0.000 10303.347    0.004 environments.py:73(step)
               32274120  262.691    0.000 9597.181    0.000 container.py:115(forward)
                2689885  128.726    0.000 9412.079    0.003 agent.py:44(<listcomp>)
               53797700  183.401    0.000 8933.830    0.000 exploration.py:33(epsilonGreedy)
                2689885    8.222    0.000 8019.940    0.003 agent.py:32(rememberMulti)
                2689885  355.411    0.000 8011.718    0.003 agent.py:33(<listcomp>)
                2689885   64.983    0.000 6748.096    0.003 environments.py:75(<listcomp>)
               53887411 1687.975    0.000 6696.305    0.000 helpers.py:8(clean)
                2689385   17.128    0.000 6082.978    0.002 grad_mode.py:12(decorate_context)
                2689385 1433.652    0.001 6046.256    0.002 adam.py:51(step)
               64548240  117.476    0.000 5719.709    0.000 conv.py:418(forward)
               61955566 5615.050    0.000 5615.050    0.000 {built-in method as_tensor}
               64548240  114.785    0.000 5556.446    0.000 conv.py:410(_conv_forward)
               64548240 5420.339    0.000 5420.339    0.000 {built-in method conv2d}
                2689385   14.391    0.000 4860.907    0.002 tensor.py:155(backward)
                2689385   17.443    0.000 4846.516    0.002 __init__.py:57(backward)
                2689385 4754.274    0.002 4754.274    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10758046  486.067    0.000 3290.993    0.000 rnn.py:109(flatten_parameters)
                2689885   60.714    0.000 3256.562    0.001 environments.py:74(<listcomp>)
               53797700  226.995    0.000 3195.848    0.000 interop.py:274(step)
               10758040  108.568    0.000 2592.641    0.000 rnn.py:550(forward)
               10758040 2348.726    0.000 2348.726    0.000 {built-in method lstm}
               10758043 2254.369    0.000 2254.369    0.000 {built-in method _cudnn_rnn_flatten_weight}
               75306280   69.845    0.000 1579.305    0.000 activation.py:653(forward)
               75306280  119.673    0.000 1509.460    0.000 functional.py:1277(leaky_relu)
               53797700   27.623    0.000 1427.238    0.000 wrapper.py:25(act)
               53797700   88.216    0.000 1399.615    0.000 env.py:197(act)
               75306280 1379.187    0.000 1379.187    0.000 {built-in method torch._C._nn.leaky_relu}
               53797700 1255.054    0.000 1260.156    0.000 libenv.py:352(act)
               96817860 1189.770    0.000 1189.770    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               96817860 1065.843    0.000 1065.843    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              107685111   92.357    0.000  923.905    0.000 extract_dict_ob.py:9(observe)
              107685111   48.378    0.000  831.548    0.000 wrapper.py:19(observe)
              107685111  209.575    0.000  783.170    0.000 libenv.py:344(observe)
               10758040   27.486    0.000  748.556    0.000 linear.py:90(forward)
                   5379    1.223    0.000  735.027    0.137 agent.py:81(update_target_network)
               10758040   56.244    0.000  710.212    0.000 functional.py:1655(linear)
               48408930  666.398    0.000  666.398    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   5379  187.140    0.035  664.529    0.124 memory.py:37(update_distribution)
                2689385   99.226    0.000  613.212    0.000 optimizer.py:166(zero_grad)
              378138177  598.071    0.000  598.071    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               56497843  578.595    0.000  578.595    0.000 {built-in method numpy.array}
               48408930  561.278    0.000  561.278    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              161482811  170.954    0.000  554.337    0.000 libenv.py:281(_maybe_copy_dict)
              484453812  494.532    0.000  494.532    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48408930  489.665    0.000  489.665    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10758040  487.800    0.000  487.800    0.000 {built-in method addmm}
               48408930  475.692    0.000  475.692    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               43033140  427.176    0.000  458.310    0.000 module.py:774(__setattr__)
               53797700   46.405    0.000  430.711    0.000 wrapper.py:22(get_info)
               11713266  158.936    0.000  401.680    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               53797700  201.569    0.000  384.306    0.000 libenv.py:363(get_info)
                2689385  288.041    0.000  373.526    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               48408930  367.230    0.000  367.230    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               53797700  362.997    0.000  362.997    0.000 memory.py:15(inner)
               10758040   20.074    0.000  358.539    0.000 pooling.py:156(forward)
               53797700  349.523    0.000  349.523    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               10758040   16.576    0.000  338.465    0.000 _jit_internal.py:237(fn)
               10758040   19.955    0.000  319.921    0.000 functional.py:564(_max_pool2d)
               10758040  298.593    0.000  298.593    0.000 {built-in method max_pool2d}
               26116057   25.459    0.000  289.797    0.000 <__array_function__ internals>:2(prod)
                8069655   13.109    0.000  265.449    0.000 functional.py:68(split)
               26116097   20.323    0.000  259.690    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               43032172  225.526    0.000  252.175    0.000 __init__.py:66(is_acceptable)
                8069655   14.599    0.000  251.289    0.000 tensor.py:367(split)
               26116057   32.570    0.000  239.367    0.000 fromnumeric.py:2881(prod)
                8069655  235.075    0.000  235.075    0.000 {function Tensor.split at 0x7fa22dfc7940}
                2689885   31.627    0.000  228.126    0.000 environments.py:76(<listcomp>)
              242044704  178.665    0.000  208.595    0.000 tensor.py:725(grad)
               26116057   59.163    0.000  206.798    0.000 fromnumeric.py:70(_wrapreduction)
               26894850  202.553    0.000  202.553    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2689885   18.600    0.000  197.492    0.000 collector.py:7(collect)
               53797720   40.737    0.000  196.508    0.000 environments.py:79(reset)
                2689385  194.805    0.000  194.805    0.000 memory.py:35(<listcomp>)
                2689385    5.520    0.000  190.553    0.000 loss.py:444(forward)
                2689385   24.934    0.000  185.032    0.000 functional.py:2621(mse_loss)
              215370222   58.879    0.000  183.141    0.000 libenv.py:271(_maybe_copy_ndarray)
              217850185  177.689    0.000  177.689    0.000 {built-in method torch._C._get_tracing_state}
                5379771  177.568    0.000  177.568    0.000 {built-in method builtins.sum}
               28810821  156.416    0.000  156.416    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              204618269  149.819    0.000  149.945    0.000 module.py:758(__getattr__)
                5378770  145.061    0.000  145.061    0.000 {built-in method gather}
                2689385  110.010    0.000  110.010    0.000 {built-in method torch._C._nn.mse_loss}
               10758040  104.961    0.000  104.961    0.000 {method 't' of 'torch._C._TensorBase' objects}
              903674860   93.427    0.000   93.427    0.000 {method 'values' of 'collections.OrderedDict' objects}
               53887451   43.536    0.000   89.278    0.000 types.py:163(multimap)
               10758040   25.556    0.000   87.359    0.000 rnn.py:524(check_forward_args)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 8423567: <Base_v2_plunder_0> in cluster <dcc> Done

Job <Base_v2_plunder_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue Nov 24 19:48:57 2020
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Nov 27 01:46:50 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 01:46:50 2020
Terminated at Sat Nov 28 01:42:09 2020
Results reported at Sat Nov 28 01:42:09 2020

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

    CPU time :                                   90702.00 sec.
    Max Memory :                                 56740 MB
    Average Memory :                             56021.48 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4700.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86118 sec.
    Turnaround time :                            280392 sec.

The output (if any) is above this job summary.

