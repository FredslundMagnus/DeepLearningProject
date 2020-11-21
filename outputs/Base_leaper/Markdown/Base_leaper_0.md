[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_leaper-0
    Discount :                  0.999
    Environment :               leaper
    Hours :                     24
    Memory :                    200000
    Update every :              100
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      10030170927 function calls (9824452563 primitive calls) in 86125.16 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86125.161 86125.161 {built-in method builtins.exec}
                      1    0.011    0.011 86125.161 86125.161 <string>:1(<module>)
                      1  502.294  502.294 86125.149 86125.149 main.py:11(main)
                3025255  108.193    0.000 58682.532    0.019 agent.py:46(learn)
                3025155  441.099    0.000 57000.410    0.019 agent.py:54(TD_learn)
                3025155  192.723    0.000 31400.214    0.010 memory.py:27(sample_distribution)
                3025155  304.354    0.000 30414.036    0.010 helpers.py:12(stack)
        220838115/15125875  957.868    0.000 17045.270    0.001 module.py:710(_call_impl)
               12100720  251.814    0.000 16697.303    0.001 agent.py:117(forward)
               27226743 16280.517    0.001 16280.519    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               27226695 13468.895    0.000 13468.895    0.000 {built-in method cat}
                3025255   83.532    0.000 10862.964    0.004 environments.py:73(step)
               36302160  253.869    0.000 9189.057    0.000 container.py:115(forward)
                3025255    8.770    0.000 8767.186    0.003 agent.py:32(rememberMulti)
                3025255  366.453    0.000 8758.417    0.003 agent.py:33(<listcomp>)
              421037255 8615.535    0.000 8615.535    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3025255   48.708    0.000 7071.534    0.002 agent.py:41(chooseMulti)
                3025255   65.093    0.000 6724.822    0.002 environments.py:75(<listcomp>)
               60733969 1675.066    0.000 6687.664    0.000 helpers.py:8(clean)
                3025155   20.849    0.000 5809.307    0.002 grad_mode.py:12(decorate_context)
                3025155 1369.623    0.000 5766.528    0.002 adam.py:51(step)
               69809434 5738.683    0.000 5738.683    0.000 {built-in method as_tensor}
               60503600  100.044    0.000 5349.988    0.000 conv.py:418(forward)
               60503600  113.333    0.000 5206.235    0.000 conv.py:410(_conv_forward)
               60503600 5073.266    0.000 5073.266    0.000 {built-in method conv2d}
                3025155   17.965    0.000 4969.107    0.002 tensor.py:155(backward)
                3025155   19.780    0.000 4951.142    0.002 __init__.py:57(backward)
                3025155 4842.709    0.002 4842.709    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3025255   62.467    0.000 3806.895    0.001 environments.py:74(<listcomp>)
               60505100  234.644    0.000 3744.429    0.000 interop.py:274(step)
               12100726  565.037    0.000 3733.138    0.000 rnn.py:109(flatten_parameters)
               12100720  131.239    0.000 2890.613    0.000 rnn.py:550(forward)
               12100720 2601.578    0.000 2601.578    0.000 {built-in method lstm}
               12100723 2498.918    0.000 2498.918    0.000 {built-in method _cudnn_rnn_flatten_weight}
                3025255  130.600    0.000 2133.967    0.001 agent.py:44(<listcomp>)
               60505100   27.475    0.000 1791.736    0.000 wrapper.py:25(act)
               60505100   87.778    0.000 1764.260    0.000 env.py:197(act)
               60505100  208.948    0.000 1655.763    0.000 exploration.py:31(epsilonGreedy)
               60505100 1616.634    0.000 1622.323    0.000 libenv.py:352(act)
                  30252    5.669    0.000 1573.929    0.052 agent.py:81(update_target_network)
               72604320   65.851    0.000 1466.924    0.000 activation.py:653(forward)
               72604320  102.751    0.000 1401.073    0.000 functional.py:1277(leaky_relu)
                  30252  407.287    0.013 1307.572    0.043 memory.py:37(update_distribution)
               72604320 1288.554    0.000 1288.554    0.000 {built-in method torch._C._nn.leaky_relu}
               96804960 1143.127    0.000 1143.127    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              121239069   93.445    0.000 1042.711    0.000 extract_dict_ob.py:9(observe)
               96804960 1010.387    0.000 1010.387    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               63590560 1005.880    0.000 1005.880    0.000 {built-in method numpy.array}
              121239069   50.265    0.000  949.266    0.000 wrapper.py:19(observe)
              121239069  245.246    0.000  899.002    0.000 libenv.py:344(observe)
               12100720   32.286    0.000  836.211    0.000 linear.py:90(forward)
               12100720   64.746    0.000  791.985    0.000 functional.py:1655(linear)
              435705332  661.063    0.000  661.063    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              181744169  191.884    0.000  632.471    0.000 libenv.py:281(_maybe_copy_dict)
               48402480  625.716    0.000  625.716    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3025155   86.721    0.000  572.899    0.000 optimizer.py:166(zero_grad)
              545262759  567.372    0.000  567.372    0.000 {method 'copy' of 'numpy.ndarray' objects}
               12100720  539.396    0.000  539.396    0.000 {built-in method addmm}
               48402480  531.444    0.000  531.444    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               48403755  487.592    0.000  520.794    0.000 module.py:774(__setattr__)
               60505100   54.140    0.000  478.532    0.000 wrapper.py:22(get_info)
               48402480  470.440    0.000  470.440    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3025155  350.691    0.000  464.963    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               48402480  459.844    0.000  459.844    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               60505100  225.110    0.000  424.392    0.000 libenv.py:363(get_info)
               60505100  419.843    0.000  419.843    0.000 memory.py:15(inner)
               12100720   27.905    0.000  405.608    0.000 pooling.py:156(forward)
               12100720   19.199    0.000  377.703    0.000 _jit_internal.py:237(fn)
               12100720   21.218    0.000  356.491    0.000 functional.py:564(_max_pool2d)
               48402480  353.014    0.000  353.014    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               60505100  347.604    0.000  347.604    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               12100720  333.780    0.000  333.780    0.000 {built-in method max_pool2d}
                9075765   13.825    0.000  293.610    0.000 functional.py:68(split)
                9075765   16.330    0.000  278.676    0.000 tensor.py:367(split)
               48402892  239.738    0.000  273.607    0.000 __init__.py:66(is_acceptable)
                9075765  260.704    0.000  260.704    0.000 {function Tensor.split at 0x7f1352237940}
                3025255   35.320    0.000  247.714    0.000 environments.py:76(<listcomp>)
                3025155    7.907    0.000  218.664    0.000 loss.py:444(forward)
                3024956  218.290    0.000  218.290    0.000 memory.py:35(<listcomp>)
               60505120   38.596    0.000  212.418    0.000 environments.py:79(reset)
                3025155   28.886    0.000  210.758    0.000 functional.py:2621(mse_loss)
                3025255   21.445    0.000  207.212    0.000 collector.py:7(collect)
               30251750  201.326    0.000  201.326    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              242478138   62.979    0.000  200.547    0.000 libenv.py:271(_maybe_copy_ndarray)
              242012448  162.050    0.000  185.567    0.000 tensor.py:725(grad)
                6050511  184.397    0.000  184.397    0.000 {built-in method builtins.sum}
                6050310  170.268    0.000  170.268    0.000 {built-in method gather}
              220838115  168.824    0.000  168.824    0.000 {built-in method torch._C._get_tracing_state}
              206801631  154.848    0.000  155.431    0.000 module.py:758(__getattr__)
                  60504   15.808    0.000  150.568    0.002 {built-in method _pickle.loads}
                3025155  126.015    0.000  126.015    0.000 {built-in method torch._C._nn.mse_loss}
               12100720  116.943    0.000  116.943    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8022185   11.754    0.000  113.120    0.000 <__array_function__ internals>:2(prod)
                  60504   26.509    0.000  110.120    0.002 {built-in method _pickle.dumps}
               12100720   33.955    0.000  103.661    0.000 rnn.py:524(check_forward_args)
                1089070    1.216    0.000  101.209    0.000 storage.py:141(_load_from_bytes)
                1089070    5.206    0.000   99.993    0.000 serialization.py:486(load)
                8022225    8.576    0.000   99.694    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               11077393   92.989    0.000   92.989    0.000 {method 'reduce' of 'numpy.ufunc' objects}
               60734009   46.300    0.000   91.861    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8371234: <Base_leaper_0> in cluster <dcc> Done

Job <Base_leaper_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:31 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Nov 20 04:06:39 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 20 04:06:39 2020
Terminated at Sat Nov 21 04:02:15 2020
Results reported at Sat Nov 21 04:02:15 2020

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

    CPU time :                                   87699.00 sec.
    Max Memory :                                 25283 MB
    Average Memory :                             24967.21 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5437.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86137 sec.
    Turnaround time :                            281144 sec.

The output (if any) is above this job summary.

