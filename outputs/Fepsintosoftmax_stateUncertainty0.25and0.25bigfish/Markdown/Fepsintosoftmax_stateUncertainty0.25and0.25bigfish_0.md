Traceback (most recent call last):
  File "main.py", line 107, in <module>
    serverRun()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 31, in serverRun
    showParams(params)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 101, in showParams
    timer = Timer()
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 68, in __init__
    cProfile.run("main()", 'stats')
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.2/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.2/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 1, in <module>
  File "main.py", line 100, in main
    act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/agent.py", line 83, in chooseMulti
    vals = self.convert_values(vals, uncertainties, avoid_trace)
  File "/zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/agent.py", line 137, in convert_values
    return vals + (self.uncertainty_weight * uncertainties * self.uncertainty) + (self.state_difference_weight * state_differences * self.state_difference)
TypeError: only integer tensors of a single element can be converted to an index

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 8467082: <Fepsintosoftmax_stateUncertainty0.25and0.25bigfish_0> in cluster <dcc> Exited

Job <Fepsintosoftmax_stateUncertainty0.25and0.25bigfish_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Dec  3 01:03:42 2020
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Dec  3 09:54:04 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Thu Dec  3 09:54:04 2020
Terminated at Thu Dec  3 09:54:17 2020
Results reported at Thu Dec  3 09:54:17 2020

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   5.52 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   14 sec.
    Turnaround time :                            31835 sec.

The output (if any) is above this job summary.

[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Fepsintosoftmax_stateUncertainty0.25and0.25bigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               1
    Reward normalization :      0
    Exploration :               epsintosoftmax
    Hidden size :               40
    Uncertainty weight :        0.25
    State difference :          1
    State difference weight :   0.25
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      10561140524 function calls (10335730678 primitive calls) in 82522.71 seconds

##    Ordered by: cumulative time
   List reduced from 1333 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 82522.714 82522.714 {built-in method builtins.exec}
                      1    0.043    0.043 82522.714 82522.714 <string>:1(<module>)
                      1  497.545  497.545 82522.670 82522.670 main.py:92(main)
                2232032  190.950    0.000 52139.203    0.023 agent.py:86(learn)
                2231532  813.558    0.000 51150.589    0.023 agent.py:96(TD_learn)
                2231532  143.268    0.000 23983.568    0.011 memory.py:35(sample_distribution)
                2231532  257.176    0.000 23301.088    0.010 helpers.py:15(stack)
        241024956/15621724 1056.604    0.000 15399.536    0.001 module.py:710(_call_impl)
                2232032  209.910    0.000 14400.657    0.006 agent.py:74(chooseMulti)
                6695096  216.431    0.000 14214.217    0.002 agent.py:212(forward)
               22317428 12289.622    0.001 12289.624    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               20085288 10654.380    0.001 10654.380    0.001 {built-in method cat}
               35707512  283.706    0.000 9898.487    0.000 container.py:115(forward)
              301295527 8498.912    0.000 8498.912    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6694596   38.536    0.000 8255.330    0.001 grad_mode.py:12(decorate_context)
                2232032   63.467    0.000 8186.078    0.004 environments.py:83(step)
                6694596 1953.196    0.000 8170.561    0.001 adam.py:51(step)
                2232032  140.497    0.000 8061.550    0.004 agent.py:84(<listcomp>)
               44640640 1314.927    0.000 7547.699    0.000 exploration.py:40(epsintosoftmax)
                2232032   93.861    0.000 7122.909    0.003 agent.py:62(rememberMulti)
                2232032  287.430    0.000 6672.147    0.003 agent.py:66(<listcomp>)
                6694596   29.801    0.000 6160.826    0.001 tensor.py:155(backward)
                6694596   35.734    0.000 6131.025    0.001 __init__.py:57(backward)
                6694596 5928.507    0.001 5928.507    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2232032   58.120    0.000 5245.223    0.002 environments.py:85(<listcomp>)
               45044208 1274.967    0.000 5241.683    0.000 helpers.py:8(clean)
               51738804 4403.652    0.000 4403.652    0.000 {built-in method as_tensor}
               40170576   69.733    0.000 3655.899    0.000 conv.py:418(forward)
               40170576   79.747    0.000 3552.204    0.000 conv.py:410(_conv_forward)
               40170576 3457.265    0.000 3457.265    0.000 {built-in method conv2d}
               53561768  113.516    0.000 3072.560    0.000 linear.py:90(forward)
               53561768  307.415    0.000 2903.048    0.000 functional.py:1655(linear)
                2232032   48.386    0.000 2636.685    0.001 environments.py:84(<listcomp>)
               44640640  173.158    0.000 2588.299    0.000 interop.py:274(step)
               44640640 1714.263    0.000 2549.427    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6695102  365.703    0.000 2304.523    0.000 rnn.py:109(flatten_parameters)
                6695096   80.848    0.000 1772.043    0.000 rnn.py:550(forward)
               46865672 1738.506    0.000 1738.506    0.000 {built-in method addmm}
              133891920 1631.757    0.000 1631.757    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               84805216   73.731    0.000 1628.351    0.000 activation.py:653(forward)
                6695096 1595.225    0.000 1595.225    0.000 {built-in method lstm}
               84805216  110.944    0.000 1554.621    0.000 functional.py:1277(leaky_relu)
                6695099 1493.147    0.000 1493.147    0.000 {built-in method _cudnn_rnn_flatten_weight}
               84805216 1432.995    0.000 1432.995    0.000 {built-in method torch._C._nn.leaky_relu}
              133891920 1422.193    0.000 1422.193    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               44640640   20.192    0.000 1148.114    0.000 wrapper.py:25(act)
               44640640   65.037    0.000 1127.922    0.000 env.py:197(act)
               44640640 1021.241    0.000 1025.236    0.000 libenv.py:352(act)
               66945960  903.647    0.000  903.647    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6694596  129.016    0.000  805.472    0.000 optimizer.py:166(zero_grad)
                   4464    1.573    0.000  797.664    0.179 agent.py:139(update_target_network)
               89684848   72.988    0.000  787.956    0.000 extract_dict_ob.py:9(observe)
               66945960  751.519    0.000  751.519    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89684848   38.351    0.000  714.968    0.000 wrapper.py:19(observe)
               33384724   62.750    0.000  709.582    0.000 functional.py:1465(softmax)
               89684848  173.262    0.000  676.616    0.000 libenv.py:344(observe)
               66945960  653.291    0.000  653.291    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               58128228   63.557    0.000  645.567    0.000 <__array_function__ internals>:2(prod)
               33384724  641.605    0.000  641.605    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               66945960  637.188    0.000  637.188    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2232032    6.337    0.000  588.669    0.000 agent.py:230(avoid_similar_state)
               58128268   45.674    0.000  570.778    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              333962912  558.807    0.000  558.807    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               58128228   73.556    0.000  525.103    0.000 fromnumeric.py:2881(prod)
               66945960  492.165    0.000  492.165    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              134325488  140.072    0.000  489.711    0.000 libenv.py:281(_maybe_copy_dict)
                   4464  141.871    0.032  483.464    0.108 memory.py:45(update_distribution)
               58128228  134.957    0.000  451.548    0.000 fromnumeric.py:70(_wrapreduction)
                6694596   15.680    0.000  449.120    0.000 loss.py:444(forward)
              402980928  439.482    0.000  439.482    0.000 {method 'copy' of 'numpy.ndarray' objects}
               53561768  435.851    0.000  435.851    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6694596   55.182    0.000  433.441    0.000 functional.py:2621(mse_loss)
               46881100  418.144    0.000  418.144    0.000 {built-in method numpy.array}
               44640640  373.354    0.000  373.354    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               31245283  339.884    0.000  370.678    0.000 module.py:774(__setattr__)
               44640640   39.997    0.000  349.024    0.000 wrapper.py:22(get_info)
               44640640  339.500    0.000  339.500    0.000 memory.py:17(inner)
               44640640  163.439    0.000  309.027    0.000 libenv.py:363(get_info)
                2232032  264.290    0.000  293.248    0.000 agent.py:131(convert_values)
                2231532  219.274    0.000  278.694    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               60364224  274.935    0.000  274.935    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                   8928  218.213    0.024  266.037    0.030 {built-in method _pickle.loads}
                6696096   12.259    0.000  264.313    0.000 functional.py:68(split)
              334729908  224.965    0.000  258.885    0.000 tensor.py:725(grad)
                6694596  256.421    0.000  256.421    0.000 {built-in method torch._C._nn.mse_loss}
               40169576  254.780    0.000  254.780    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                6696096   13.468    0.000  251.286    0.000 tensor.py:367(split)
                6695096   17.075    0.000  242.872    0.000 pooling.py:156(forward)
                8926128  242.619    0.000  242.619    0.000 {built-in method gather}
                2232032   25.264    0.000  240.703    0.000 environments.py:86(<listcomp>)
                6696096  236.382    0.000  236.382    0.000 {function Tensor.split at 0x7fde6b476940}
                6695096   11.771    0.000  225.797    0.000 _jit_internal.py:237(fn)
               44640660   31.489    0.000  215.452    0.000 environments.py:89(reset)
                6696096  213.185    0.000  213.185    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6695096   13.176    0.000  212.893    0.000 functional.py:564(_max_pool2d)
               26780396  183.975    0.000  204.808    0.000 __init__.py:66(is_acceptable)
                2571294  204.548    0.000  204.548    0.000 {built-in method tensor}
                6695096  198.964    0.000  198.964    0.000 {built-in method max_pool2d}
              241024956  176.187    0.000  176.187    0.000 {built-in method torch._C._get_tracing_state}
              236920140  172.497    0.000  172.688    0.000 module.py:758(__getattr__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8468490: <Fepsintosoftmax_stateUncertainty0.25and0.25bigfish_0> in cluster <dcc> Done

Job <Fepsintosoftmax_stateUncertainty0.25and0.25bigfish_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Thu Dec  3 15:58:38 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Dec  4 10:36:58 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Dec  4 10:36:58 2020
Terminated at Sat Dec  5 09:32:28 2020
Results reported at Sat Dec  5 09:32:28 2020

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

    CPU time :                                   84843.00 sec.
    Max Memory :                                 53863 MB
    Average Memory :                             53191.11 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               7577.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82531 sec.
    Turnaround time :                            149630 sec.

The output (if any) is above this job summary.

