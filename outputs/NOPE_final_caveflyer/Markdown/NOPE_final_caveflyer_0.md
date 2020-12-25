[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      NOPE_final_caveflyer-0
    Discount :                  0.995
    Environment :               caveflyer
    Hours :                     18
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
    Uncertainty weight :        0.1
    State difference :          0
    State difference weight :   0.0
    Minutes used :              1075 minutes.
    Hours used :                17 hours.

# Profiling


      7832757320 function calls (7668821392 primitive calls) in 64520.12 seconds

##    Ordered by: cumulative time
   List reduced from 1329 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 64520.119 64520.119 {built-in method builtins.exec}
                      1    0.038    0.038 64520.119 64520.119 <string>:1(<module>)
                      1  418.286  418.286 64520.080 64520.080 main.py:91(main)
                2159630  151.467    0.000 40324.837    0.019 agent.py:93(learn)
                2072673  354.421    0.000 39675.264    0.019 agent.py:106(TD_learn)
                2072673  146.023    0.000 23104.863    0.011 memory.py:35(sample_distribution)
                2072673  260.655    0.000 22428.680    0.011 helpers.py:15(stack)
               18915036 11225.690    0.001 11225.744    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2159630   43.528    0.000 11005.141    0.005 agent.py:72(chooseMulti)
              280974719 10689.507    0.000 10689.507    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               18914928 10676.014    0.001 10676.014    0.001 {built-in method cat}
        174379698/10450322  746.870    0.000 10364.165    0.001 module.py:710(_call_impl)
                6304976  158.568    0.000 9990.699    0.002 agent.py:235(forward)
                2159630   58.874    0.000 7439.640    0.003 environments.py:83(step)
                2073672   71.547    0.000 6904.233    0.003 agent.py:88(<listcomp>)
               41473440  102.311    0.000 6651.180    0.000 exploration.py:34(epsilonGreedy)
               25219904  182.632    0.000 6122.848    0.000 container.py:115(forward)
                2073663    8.958    0.000 5166.920    0.002 agent.py:58(rememberMulti)
                2073663  165.022    0.000 5157.962    0.002 agent.py:63(<listcomp>)
                2159630   48.967    0.000 4488.529    0.002 environments.py:85(<listcomp>)
               43288262 1190.817    0.000 4451.467    0.000 helpers.py:8(clean)
                4145346   22.133    0.000 4218.894    0.001 grad_mode.py:12(decorate_context)
                4145346 1064.483    0.000 4168.139    0.001 adam.py:51(step)
                4145346   19.239    0.000 3809.797    0.001 tensor.py:155(backward)
                4145346   23.988    0.000 3790.558    0.001 __init__.py:57(backward)
               49506281 3763.712    0.000 3763.712    0.000 {built-in method as_tensor}
                4145346 3672.925    0.001 3672.925    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               37829856   66.062    0.000 2914.106    0.000 conv.py:418(forward)
               37829856   75.512    0.000 2817.761    0.000 conv.py:410(_conv_forward)
                2159630   44.216    0.000 2746.447    0.001 environments.py:84(<listcomp>)
               37829856 2728.428    0.000 2728.428    0.000 {built-in method conv2d}
               43192600  155.814    0.000 2702.231    0.000 interop.py:274(step)
                6304982  315.781    0.000 1718.820    0.000 rnn.py:109(flatten_parameters)
                6304976   76.520    0.000 1580.301    0.000 rnn.py:550(forward)
                6304976 1418.732    0.000 1418.732    0.000 {built-in method lstm}
               43192600   19.706    0.000 1383.439    0.000 wrapper.py:25(act)
               43192600   52.135    0.000 1363.732    0.000 env.py:197(act)
               43192600 1279.419    0.000 1283.603    0.000 libenv.py:352(act)
               25219904   51.375    0.000 1181.894    0.000 linear.py:90(forward)
               25219904   92.732    0.000 1102.873    0.000 functional.py:1655(linear)
                6304979 1023.987    0.000 1023.987    0.000 {built-in method _cudnn_rnn_flatten_weight}
               63049760   55.619    0.000  963.619    0.000 activation.py:653(forward)
               63049760   83.026    0.000  908.000    0.000 functional.py:1277(leaky_relu)
               63049760  816.762    0.000  816.762    0.000 {built-in method torch._C._nn.leaky_relu}
               99488304  770.957    0.000  770.957    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               25219904  740.485    0.000  740.485    0.000 {built-in method addmm}
               86480862   63.650    0.000  703.455    0.000 extract_dict_ob.py:9(observe)
               99488304  674.790    0.000  674.790    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               86480862   38.587    0.000  639.805    0.000 wrapper.py:19(observe)
               86480862  162.424    0.000  601.218    0.000 libenv.py:344(observe)
                   2116    0.846    0.000  498.107    0.235 agent.py:161(update_target_network)
               49744152  480.098    0.000  480.098    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              129673462  134.672    0.000  438.119    0.000 libenv.py:281(_maybe_copy_dict)
                4145346   72.280    0.000  405.254    0.000 optimizer.py:166(zero_grad)
               49744152  396.607    0.000  396.607    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              389022502  372.185    0.000  372.185    0.000 {method 'copy' of 'numpy.ndarray' objects}
               11098999  130.679    0.000  344.330    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               29367085  310.546    0.000  333.522    0.000 module.py:774(__setattr__)
              311340778  329.657    0.000  329.657    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               49744152  323.879    0.000  323.879    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               43192600   34.332    0.000  321.769    0.000 wrapper.py:22(get_info)
               49744152  317.786    0.000  317.786    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               43192600  149.242    0.000  287.437    0.000 libenv.py:363(get_info)
               41473260  282.990    0.000  282.990    0.000 memory.py:17(inner)
                2072673  213.710    0.000  279.825    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               45269505  269.241    0.000  269.241    0.000 {built-in method numpy.array}
                   2116   75.695    0.036  266.027    0.126 memory.py:45(update_distribution)
                4145346   10.393    0.000  257.926    0.000 loss.py:444(forward)
               24270811   22.411    0.000  249.926    0.000 <__array_function__ internals>:2(prod)
                4145346   36.015    0.000  247.533    0.000 functional.py:2621(mse_loss)
               49744152  231.568    0.000  231.568    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24270851   17.111    0.000  223.778    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                   4232  189.325    0.045  210.765    0.050 {built-in method _pickle.loads}
               24270811   27.705    0.000  206.667    0.000 fromnumeric.py:2881(prod)
                2073672  141.619    0.000  204.607    0.000 agent.py:152(convert_values)
                6478890   11.218    0.000  202.451    0.000 functional.py:68(split)
                6304976   18.125    0.000  194.192    0.000 pooling.py:156(forward)
                6478890   11.850    0.000  190.387    0.000 tensor.py:367(split)
               43192600  187.979    0.000  187.979    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24270811   53.183    0.000  178.962    0.000 fromnumeric.py:70(_wrapreduction)
                6478890  177.140    0.000  177.140    0.000 {function Tensor.split at 0x7f22b6e619d0}
                6304976   11.108    0.000  176.067    0.000 _jit_internal.py:237(fn)
               25219916  155.111    0.000  173.078    0.000 __init__.py:66(is_acceptable)
                2072673  170.892    0.000  170.892    0.000 memory.py:43(<listcomp>)
                8290692  167.220    0.000  167.220    0.000 {built-in method gather}
                6304976   11.144    0.000  163.982    0.000 functional.py:564(_max_pool2d)
               25219904  163.178    0.000  163.178    0.000 {method 't' of 'torch._C._TensorBase' objects}
              248720868  136.365    0.000  158.352    0.000 tensor.py:725(grad)
                6304976  152.053    0.000  152.053    0.000 {built-in method max_pool2d}
                2159630   22.465    0.000  145.790    0.000 environments.py:86(<listcomp>)
               29278293  141.942    0.000  141.942    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2159630   14.419    0.000  140.646    0.000 collector.py:8(collect)
                4145346  137.042    0.000  137.042    0.000 {built-in method torch._C._nn.mse_loss}
               26345600  129.323    0.000  129.323    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                4319261  125.251    0.000  125.251    0.000 {built-in method builtins.sum}
              172961724   45.460    0.000  125.004    0.000 libenv.py:271(_maybe_copy_ndarray)
               43192620   27.076    0.000  123.340    0.000 environments.py:89(reset)
              164099283  122.716    0.000  122.808    0.000 module.py:758(__getattr__)
              174379698   96.480    0.000   96.480    0.000 {built-in method torch._C._get_tracing_state}
                4145346   24.156    0.000   92.286    0.000 __init__.py:25(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8587060: <NOPE_final_caveflyer_0> in cluster <dcc> Done

Job <NOPE_final_caveflyer_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Thu Dec 24 13:34:59 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Dec 24 13:35:01 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec 24 13:35:01 2020
Terminated at Fri Dec 25 07:30:29 2020
Results reported at Fri Dec 25 07:30:29 2020

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

    CPU time :                                   68957.00 sec.
    Max Memory :                                 55538 MB
    Average Memory :                             54813.45 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5902.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64533 sec.
    Turnaround time :                            64530 sec.

The output (if any) is above this job summary.

