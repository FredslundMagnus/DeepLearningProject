
    Name :                      Uncertainty0.1state_difference0dodgeball-0
    Discount :                  0.995
    Environment :               dodgeball
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsilonGreedy
    Hidden size :               40
    Uncertainty weight :        0.1
    State difference :          1
    State difference weight :   0
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12030053803 function calls (11832268360 primitive calls) in 82529.36 seconds

##    Ordered by: cumulative time
   List reduced from 1356 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.001    0.000 82529.365 82529.365 {built-in method builtins.exec}
                      1    0.031    0.031 82529.365 82529.365 <string>:1(<module>)
                      1  563.130  563.130 82529.332 82529.332 main.py:92(main)
                1958523  240.284    0.000 57535.753    0.029 agent.py:86(learn)
                1958023  664.479    0.000 56349.877    0.029 agent.py:96(TD_learn)
                1958023  153.518    0.000 32835.700    0.017 memory.py:35(sample_distribution)
                1958023  293.324    0.000 32111.213    0.016 helpers.py:15(stack)
               17623707 19647.841    0.001 19647.841    0.001 {built-in method cat}
        211485984/13707161  995.775    0.000 13734.227    0.001 module.py:715(_call_impl)
                5874569  190.405    0.000 12703.280    0.002 agent.py:212(forward)
               19582338 11788.713    0.001 11788.734    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                1958523  167.428    0.000 9018.334    0.005 agent.py:74(chooseMulti)
               31331368  242.823    0.000 8708.283    0.000 container.py:115(forward)
                1958523   64.570    0.000 8446.146    0.004 environments.py:83(step)
              263270520 7892.565    0.000 7892.565    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                1958523   83.229    0.000 6787.995    0.003 agent.py:62(rememberMulti)
                5874069   41.782    0.000 6651.180    0.001 grad_mode.py:23(decorate_context)
                5874069  257.138    0.000 6540.666    0.001 adam.py:55(step)
                1958523  215.894    0.000 6370.741    0.003 agent.py:66(<listcomp>)
                5874069 1245.802    0.000 5371.913    0.001 functional.py:53(adam)
               40275212 1346.707    0.000 5274.563    0.000 helpers.py:8(clean)
                1958523   53.463    0.000 5162.502    0.003 environments.py:85(<listcomp>)
                5874069   44.209    0.000 4982.498    0.001 tensor.py:181(backward)
                5874069   31.165    0.000 4938.289    0.001 __init__.py:68(backward)
                5874069 4760.253    0.001 4760.253    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               46149281 4494.404    0.000 4494.404    0.000 {built-in method as_tensor}
               35247414   66.838    0.000 3228.884    0.000 conv.py:422(forward)
                1958523   76.890    0.000 3217.074    0.002 agent.py:84(<listcomp>)
               35247414   85.504    0.000 3128.622    0.000 conv.py:414(_conv_forward)
               35247414 3028.756    0.000 3028.756    0.000 {built-in method conv2d}
               39170460  114.119    0.000 2929.140    0.000 exploration.py:34(epsilonGreedy)
                1958523   44.616    0.000 2819.449    0.001 environments.py:84(<listcomp>)
               39170460  154.001    0.000 2774.833    0.000 interop.py:274(step)
               46997552  103.405    0.000 2712.124    0.000 linear.py:92(forward)
               46997552  268.918    0.000 2554.591    0.000 functional.py:1669(linear)
                5874575  372.082    0.000 1978.628    0.000 rnn.py:110(flatten_parameters)
                5874569   76.328    0.000 1816.387    0.000 rnn.py:555(forward)
                5874569 1653.407    0.000 1653.407    0.000 {built-in method lstm}
              411184938  957.896    0.000 1622.724    0.000 tensor.py:933(grad)
               41121983 1474.104    0.000 1474.104    0.000 {built-in method addmm}
               39170460   19.777    0.000 1413.171    0.000 wrapper.py:25(act)
                5874069  139.211    0.000 1401.664    0.000 optimizer.py:167(zero_grad)
               39170460   55.573    0.000 1393.394    0.000 env.py:197(act)
               74411874   74.118    0.000 1364.566    0.000 activation.py:713(forward)
               39170460 1305.643    0.000 1309.540    0.000 libenv.py:352(act)
               74411874  109.666    0.000 1290.448    0.000 functional.py:1292(leaky_relu)
               74411874 1170.888    0.000 1170.888    0.000 {built-in method torch._C._nn.leaky_relu}
                5874572 1154.962    0.000 1154.962    0.000 {built-in method _cudnn_rnn_flatten_weight}
              117481380 1080.199    0.000 1080.199    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   3917    2.100    0.001  945.592    0.241 agent.py:139(update_target_network)
              117481380  895.744    0.000  895.744    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              516923426  283.739    0.000  844.121    0.000 overrides.py:1073(has_torch_function)
               79445672   64.159    0.000  803.732    0.000 extract_dict_ob.py:9(observe)
               79445672   38.638    0.000  739.572    0.000 wrapper.py:19(observe)
               79445672  181.799    0.000  700.935    0.000 libenv.py:344(observe)
                   3917  155.675    0.040  609.181    0.156 memory.py:45(update_distribution)
               58740690  606.680    0.000  606.680    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               58740690  571.488    0.000  571.488    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              575669140  213.858    0.000  535.051    0.000 {built-in method builtins.any}
                1958523    5.503    0.000  519.988    0.000 agent.py:230(avoid_similar_state)
               41136317  519.167    0.000  519.167    0.000 {built-in method numpy.array}
              118616132  135.346    0.000  513.570    0.000 libenv.py:281(_maybe_copy_dict)
               58740690  501.870    0.000  501.870    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              355852313  455.733    0.000  455.733    0.000 {method 'copy' of 'numpy.ndarray' objects}
               58740690  449.534    0.000  449.534    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               39170460  415.203    0.000  415.203    0.000 memory.py:17(inner)
                5875569   13.209    0.000  400.810    0.000 functional.py:74(split)
                1958523   26.535    0.000  399.624    0.000 environments.py:86(<listcomp>)
               46997552  397.342    0.000  397.342    0.000 {method 't' of 'torch._C._TensorBase' objects}
               27416157  369.442    0.000  392.705    0.000 module.py:781(__setattr__)
                5875569   27.732    0.000  386.778    0.000 tensor.py:460(split)
                5874069   12.988    0.000  382.904    0.000 loss.py:445(forward)
               39170480   36.385    0.000  373.093    0.000 environments.py:89(reset)
                5874069   44.903    0.000  369.916    0.000 functional.py:2637(mse_loss)
               10981458  143.510    0.000  367.635    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                5875569  357.696    0.000  357.696    0.000 {function Tensor.split at 0x7f18c79c7d30}
              290432902  330.263    0.000  330.263    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               39170460   36.861    0.000  321.726    0.000 wrapper.py:22(get_info)
             1080844404  256.267    0.000  316.349    0.000 overrides.py:1086(<genexpr>)
               58740690  316.112    0.000  316.112    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1958023  224.458    0.000  293.486    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               39170460  144.925    0.000  284.865    0.000 libenv.py:363(get_info)
                   7834  233.793    0.030  281.812    0.036 {built-in method _pickle.loads}
               23921079   24.289    0.000  263.361    0.000 <__array_function__ internals>:2(prod)
               23921119   18.222    0.000  234.644    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                5874569   17.551    0.000  227.660    0.000 pooling.py:152(forward)
                1958523  200.993    0.000  226.584    0.000 agent.py:131(convert_values)
                5874069  223.393    0.000  223.393    0.000 {built-in method torch._C._nn.mse_loss}
               23921079   29.715    0.000  216.422    0.000 fromnumeric.py:2881(prod)
                7832092  215.439    0.000  215.439    0.000 {built-in method gather}
               39170460  211.044    0.000  211.044    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                5874569   11.538    0.000  210.110    0.000 _jit_internal.py:257(fn)
               35246414  206.376    0.000  206.376    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                5874569   13.833    0.000  197.546    0.000 functional.py:574(_max_pool2d)
                5875569  192.947    0.000  192.947    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
               23921079   54.996    0.000  186.707    0.000 fromnumeric.py:70(_wrapreduction)
                2256213  183.960    0.000  183.960    0.000 {built-in method tensor}
                5874569  182.952    0.000  182.952    0.000 {built-in method max_pool2d}
               23498288  159.376    0.000  180.489    0.000 __init__.py:67(is_acceptable)
                1958023  179.843    0.000  179.843    0.000 memory.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8483548: <Uncertainty0.1state_difference0dodgeball_0> in cluster <dcc> Done

Job <Uncertainty0.1state_difference0dodgeball_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Dec  6 01:18:08 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Dec  7 11:57:35 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Dec  7 11:57:35 2020
Terminated at Tue Dec  8 10:53:19 2020
Results reported at Tue Dec  8 10:53:19 2020

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

    CPU time :                                   91095.00 sec.
    Max Memory :                                 54609 MB
    Average Memory :                             54010.32 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6831.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82571 sec.
    Turnaround time :                            207311 sec.

The output (if any) is above this job summary.

