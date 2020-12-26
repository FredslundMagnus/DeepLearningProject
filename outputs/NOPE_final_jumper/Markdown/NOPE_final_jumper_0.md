
    Name :                      NOPE_final_jumper-0
    Discount :                  0.995
    Environment :               jumper
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


      9798982840 function calls (9649683632 primitive calls) in 64524.29 seconds

##    Ordered by: cumulative time
   List reduced from 1354 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 64524.288 64524.288 {built-in method builtins.exec}
                      1    0.025    0.025 64524.288 64524.288 <string>:1(<module>)
                      1  366.447  366.447 64524.263 64524.263 main.py:91(main)
                1966649  134.514    0.000 42306.362    0.022 agent.py:93(learn)
                1887688  418.984    0.000 41730.025    0.022 agent.py:106(TD_learn)
                1887688  129.902    0.000 20698.098    0.011 memory.py:35(sample_distribution)
                1887688  228.499    0.000 20070.690    0.011 helpers.py:15(stack)
        158810051/9517401  733.226    0.000 11490.949    0.001 module.py:715(_call_impl)
                5742025  149.751    0.000 11104.769    0.002 agent.py:235(forward)
               17226183 10192.542    0.001 10192.557    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               17226075 9298.035    0.001 9298.035    0.001 {built-in method cat}
                1966649   54.518    0.000 8287.762    0.004 environments.py:83(step)
                1966649   44.622    0.000 7520.900    0.004 agent.py:72(chooseMulti)
              255095043 7238.658    0.000 7238.658    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               22968100  200.670    0.000 6953.977    0.000 container.py:115(forward)
                3775376   26.791    0.000 6307.168    0.002 grad_mode.py:23(decorate_context)
                3775376  180.590    0.000 6238.133    0.002 adam.py:55(step)
                1888678    8.170    0.000 5880.405    0.003 agent.py:58(rememberMulti)
                1888678  249.448    0.000 5872.235    0.003 agent.py:63(<listcomp>)
                3775376 1162.927    0.000 5393.127    0.001 functional.py:53(adam)
                1966649   53.214    0.000 4792.598    0.002 environments.py:85(<listcomp>)
               39444727 1128.364    0.000 4755.244    0.000 helpers.py:8(clean)
                3775376   29.475    0.000 4475.383    0.001 tensor.py:181(backward)
                3775376   19.562    0.000 4445.907    0.001 __init__.py:68(backward)
                3775376 4318.075    0.001 4318.075    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               45107791 4115.520    0.000 4115.520    0.000 {built-in method as_tensor}
                1966649   43.605    0.000 3293.432    0.002 environments.py:84(<listcomp>)
               39332980  161.731    0.000 3249.826    0.000 interop.py:274(step)
               34452150   62.163    0.000 3233.545    0.000 conv.py:422(forward)
               34452150   67.615    0.000 3143.323    0.000 conv.py:414(_conv_forward)
               34452150 3063.377    0.000 3063.377    0.000 {built-in method conv2d}
                1888687   86.567    0.000 3047.047    0.002 agent.py:88(<listcomp>)
               37773740  120.535    0.000 2712.183    0.000 exploration.py:34(epsilonGreedy)
                5742031  346.637    0.000 2104.596    0.000 rnn.py:110(flatten_parameters)
               39332980   18.562    0.000 1923.950    0.000 wrapper.py:25(act)
               39332980   61.459    0.000 1905.388    0.000 env.py:197(act)
               39332980 1803.367    0.000 1806.977    0.000 libenv.py:352(act)
                5742025   68.286    0.000 1487.864    0.000 rnn.py:555(forward)
               22968100   50.510    0.000 1421.331    0.000 linear.py:92(forward)
                5742028 1349.066    0.000 1349.066    0.000 {built-in method _cudnn_rnn_flatten_weight}
               22968100   96.893    0.000 1346.143    0.000 functional.py:1669(linear)
                5742025 1341.213    0.000 1341.213    0.000 {built-in method lstm}
              317131692  771.121    0.000 1242.648    0.000 tensor.py:933(grad)
                3775376  120.956    0.000 1231.782    0.000 optimizer.py:167(zero_grad)
               57420250   51.066    0.000 1182.649    0.000 activation.py:713(forward)
               90609024 1146.219    0.000 1146.219    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57420250   77.686    0.000 1131.583    0.000 functional.py:1292(leaky_relu)
               57420250 1046.098    0.000 1046.098    0.000 {built-in method torch._C._nn.leaky_relu}
               90609024  959.918    0.000  959.918    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               22968100  922.535    0.000  922.535    0.000 {built-in method addmm}
               78777707   66.048    0.000  709.271    0.000 extract_dict_ob.py:9(observe)
               78777707   34.519    0.000  643.222    0.000 wrapper.py:19(observe)
               78777707  158.884    0.000  608.703    0.000 libenv.py:344(observe)
               45304512  593.443    0.000  593.443    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              385404520  207.938    0.000  567.639    0.000 overrides.py:1073(has_torch_function)
               45304512  544.035    0.000  544.035    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               45304512  507.559    0.000  507.559    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               45304512  463.389    0.000  463.389    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   1927    0.742    0.000  441.823    0.229 agent.py:161(update_target_network)
              118110687  128.099    0.000  436.602    0.000 libenv.py:281(_maybe_copy_dict)
              282688295  395.826    0.000  395.826    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              354333988  390.069    0.000  390.069    0.000 {method 'copy' of 'numpy.ndarray' objects}
               10917147  146.606    0.000  372.146    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               45304512  353.307    0.000  353.307    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              415923396  143.050    0.000  343.081    0.000 {built-in method builtins.any}
               39332980   35.136    0.000  319.699    0.000 wrapper.py:22(get_info)
               26745311  279.081    0.000  298.175    0.000 module.py:781(__setattr__)
                5899947   10.760    0.000  297.006    0.000 functional.py:74(split)
                5899947   25.843    0.000  285.440    0.000 tensor.py:460(split)
               39332980  150.409    0.000  284.563    0.000 libenv.py:363(get_info)
                3775376    9.563    0.000  273.960    0.000 loss.py:445(forward)
                1887688  208.886    0.000  272.615    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                3775376   29.810    0.000  264.397    0.000 functional.py:2637(mse_loss)
               23722122   22.671    0.000  262.033    0.000 <__array_function__ internals>:2(prod)
               37773560  259.226    0.000  259.226    0.000 memory.py:17(inner)
                5899947  258.336    0.000  258.336    0.000 {function Tensor.split at 0x7f731ff43d30}
               39332980  257.655    0.000  257.655    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               41224522  243.328    0.000  243.328    0.000 {built-in method numpy.array}
               23722162   17.486    0.000  235.519    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                   1927   66.720    0.035  232.358    0.121 memory.py:45(update_distribution)
               22968100  222.503    0.000  222.503    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5742025   15.969    0.000  220.745    0.000 pooling.py:152(forward)
               23722122   28.306    0.000  218.032    0.000 fromnumeric.py:2881(prod)
                5742025   10.843    0.000  204.776    0.000 _jit_internal.py:257(fn)
                7550752  204.536    0.000  204.536    0.000 {built-in method gather}
              793777140  158.863    0.000  197.055    0.000 overrides.py:1086(<genexpr>)
                5742025   12.027    0.000  193.020    0.000 functional.py:574(_max_pool2d)
                1888687  171.214    0.000  192.779    0.000 agent.py:152(convert_values)
               23722122   53.162    0.000  189.726    0.000 fromnumeric.py:70(_wrapreduction)
                   3854  166.348    0.043  188.315    0.049 {built-in method _pickle.loads}
                5742025  180.237    0.000  180.237    0.000 {built-in method max_pool2d}
               26664515  175.840    0.000  175.840    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                3775376  168.009    0.000  168.009    0.000 {built-in method torch._C._nn.mse_loss}
               22968112  146.960    0.000  164.749    0.000 __init__.py:67(is_acceptable)
                1887688  147.560    0.000  147.560    0.000 memory.py:43(<listcomp>)
                1966649   21.909    0.000  147.215    0.000 environments.py:86(<listcomp>)
               25611737  138.002    0.000  138.002    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                1966649   14.389    0.000  134.423    0.000 collector.py:8(collect)
              157555414   42.265    0.000  133.994    0.000 libenv.py:271(_maybe_copy_ndarray)
               39333000   26.468    0.000  125.336    0.000 environments.py:89(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 8585270: <NOPE_final_jumper_0> in cluster <dcc> Done

Job <NOPE_final_jumper_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Dec 23 18:21:53 2020
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Dec 24 12:43:14 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec 24 12:43:14 2020
Terminated at Fri Dec 25 06:38:48 2020
Results reported at Fri Dec 25 06:38:48 2020

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

    CPU time :                                   66489.00 sec.
    Max Memory :                                 55864 MB
    Average Memory :                             55108.25 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               5576.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   64635 sec.
    Turnaround time :                            130615 sec.

The output (if any) is above this job summary.

