
    Name :                      CHASER_U_S_0_0.001returnchaser-0
    Discount :                  0.995
    Environment :               chaser
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
    Uncertainty weight :        0
    State difference :          1
    State difference weight :   0.001
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12707133638 function calls (12497602837 primitive calls) in 82528.18 seconds

##    Ordered by: cumulative time
   List reduced from 1361 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82528.178 82528.178 {built-in method builtins.exec}
                      1    0.014    0.014 82528.178 82528.178 <string>:1(<module>)
                      1  479.430  479.430 82528.161 82528.161 main.py:92(main)
                2132488  234.128    0.000 55847.546    0.026 agent.py:84(learn)
                2047530  905.928    0.000 55082.251    0.027 agent.py:99(TD_learn)
                2047530  151.588    0.000 24556.601    0.012 memory.py:35(sample_distribution)
                2047530  304.163    0.000 23828.445    0.012 helpers.py:15(stack)
        223942848/14418667 1041.353    0.000 16261.305    0.001 module.py:715(_call_impl)
                6227548  212.522    0.000 15027.012    0.002 agent.py:231(forward)
               18682644 12235.851    0.001 12235.851    0.001 {built-in method cat}
               20731281 10974.046    0.001 10974.173    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               33186269  299.015    0.000 10635.287    0.000 container.py:115(forward)
                2132488   65.734    0.000 9679.180    0.005 environments.py:83(step)
                6142590   43.700    0.000 9651.964    0.002 grad_mode.py:23(decorate_context)
                6142590  276.892    0.000 9535.617    0.002 adam.py:55(step)
                2132488  211.383    0.000 8850.309    0.004 agent.py:70(chooseMulti)
                6142590 1785.959    0.000 8222.282    0.001 functional.py:53(adam)
                2048529  102.899    0.000 7464.503    0.004 agent.py:58(rememberMulti)
                2048529  313.700    0.000 6954.932    0.003 agent.py:62(<listcomp>)
              277459408 6651.628    0.000 6651.628    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                6142590   46.502    0.000 6337.553    0.001 tensor.py:181(backward)
                6142590   30.004    0.000 6291.051    0.001 __init__.py:68(backward)
                2132488   70.378    0.000 6167.736    0.003 environments.py:85(<listcomp>)
               42989314 1486.172    0.000 6153.090    0.000 helpers.py:8(clean)
                6142590 6085.092    0.001 6085.092    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               49131904 5211.898    0.000 5211.898    0.000 {built-in method as_tensor}
               37365288   72.977    0.000 3853.952    0.000 conv.py:422(forward)
               37365288   80.198    0.000 3748.207    0.000 conv.py:414(_conv_forward)
               37365288 3653.263    0.000 3653.263    0.000 {built-in method conv2d}
               49738423  116.323    0.000 3389.204    0.000 linear.py:92(forward)
               49738423  321.176    0.000 3211.558    0.000 functional.py:1669(linear)
                2132488   51.363    0.000 3172.701    0.001 environments.py:84(<listcomp>)
               42649760  189.562    0.000 3121.338    0.000 interop.py:274(step)
                6227554  402.701    0.000 2497.550    0.000 rnn.py:110(flatten_parameters)
              429981408 1194.162    0.000 1931.608    0.000 tensor.py:933(grad)
               43592836 1890.193    0.000 1890.193    0.000 {built-in method addmm}
                6142590  182.436    0.000 1886.389    0.000 optimizer.py:167(zero_grad)
                2048529  105.079    0.000 1814.857    0.001 agent.py:82(<listcomp>)
               78827634   91.800    0.000 1806.081    0.000 activation.py:713(forward)
              122851800 1743.560    0.000 1743.560    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6227548   72.027    0.000 1729.713    0.000 rnn.py:555(forward)
               78827634  114.224    0.000 1714.281    0.000 functional.py:1292(leaky_relu)
                6227551 1654.339    0.000 1654.339    0.000 {built-in method _cudnn_rnn_flatten_weight}
               78827634 1589.236    0.000 1589.236    0.000 {built-in method torch._C._nn.leaky_relu}
               42649760   22.990    0.000 1578.432    0.000 wrapper.py:25(act)
                6227548 1567.826    0.000 1567.826    0.000 {built-in method lstm}
               42649760   73.052    0.000 1555.442    0.000 env.py:197(act)
              122851800 1463.044    0.000 1463.044    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               42649760 1434.146    0.000 1438.557    0.000 libenv.py:352(act)
               40970580  156.930    0.000 1399.454    0.000 exploration.py:34(epsilonGreedy)
              541145977  341.406    0.000  943.282    0.000 overrides.py:1073(has_torch_function)
               61425900  911.007    0.000  911.007    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               85639074   76.585    0.000  828.640    0.000 extract_dict_ob.py:9(observe)
               61425900  828.079    0.000  828.079    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               61425900  772.684    0.000  772.684    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               85639074   41.241    0.000  752.055    0.000 wrapper.py:19(observe)
               85639074  182.343    0.000  710.814    0.000 libenv.py:344(observe)
               61425900  694.593    0.000  694.593    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2048529    6.064    0.000  653.614    0.000 agent.py:249(avoid_similar_state)
              603169604  240.776    0.000  578.778    0.000 {built-in method builtins.any}
              315201585  554.233    0.000  554.233    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               61425900  535.789    0.000  535.789    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   2132    0.932    0.000  531.168    0.249 agent.py:157(update_target_network)
               49738423  517.971    0.000  517.971    0.000 {method 't' of 'torch._C._TensorBase' objects}
              128288834  151.406    0.000  513.335    0.000 libenv.py:281(_maybe_copy_dict)
              384868634  454.563    0.000  454.563    0.000 {method 'copy' of 'numpy.ndarray' objects}
                6142590   13.349    0.000  443.036    0.000 loss.py:445(forward)
                6142590   44.485    0.000  429.687    0.000 functional.py:2637(mse_loss)
               11075410  157.277    0.000  399.895    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6397464   12.859    0.000  386.814    0.000 functional.py:74(split)
               42649760   42.798    0.000  378.651    0.000 wrapper.py:22(get_info)
                6397464   32.403    0.000  373.020    0.000 tensor.py:460(split)
               12285180  362.935    0.000  362.935    0.000 {built-in method gather}
               40970580  356.420    0.000  356.420    0.000 memory.py:17(inner)
                6397464  338.981    0.000  338.981    0.000 {function Tensor.split at 0x7fab12428d30}
               42649760  177.440    0.000  335.853    0.000 libenv.py:363(get_info)
               47433022  334.407    0.000  334.407    0.000 {method 'view' of 'torch._C._TensorBase' objects}
             1132030377  266.633    0.000  333.225    0.000 overrides.py:1086(<genexpr>)
               29007087  308.194    0.000  331.830    0.000 module.py:781(__setattr__)
               42649760  321.749    0.000  321.749    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                2047530  239.244    0.000  310.278    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               44701554  286.902    0.000  286.902    0.000 {built-in method numpy.array}
               24198490   23.789    0.000  281.317    0.000 <__array_function__ internals>:2(prod)
                2048529  277.835    0.000  281.222    0.000 agent.py:149(convert_values)
                   2132   77.608    0.036  278.413    0.131 memory.py:45(update_distribution)
                6142590  273.066    0.000  273.066    0.000 {built-in method torch._C._nn.mse_loss}
                2132488   28.472    0.000  273.008    0.000 environments.py:86(<listcomp>)
               24198530   18.425    0.000  253.027    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                6227548   16.196    0.000  251.283    0.000 pooling.py:152(forward)
               42649780   40.691    0.000  244.573    0.000 environments.py:89(reset)
                6145587  238.842    0.000  238.842    0.000 {method 'matmul' of 'torch._C._TensorBase' objects}
                6227548   11.315    0.000  235.087    0.000 _jit_internal.py:257(fn)
               24198490   30.995    0.000  234.602    0.000 fromnumeric.py:2881(prod)
                   4264  199.173    0.047  226.313    0.053 {built-in method _pickle.loads}
                6227548   12.301    0.000  222.563    0.000 functional.py:574(_max_pool2d)
               12286179  220.985    0.000  220.985    0.000 {method 'type' of 'torch._C._TensorBase' objects}
                2210559  213.481    0.000  213.481    0.000 {built-in method tensor}
                6227548  209.463    0.000  209.463    0.000 {built-in method max_pool2d}
               24198490   56.219    0.000  203.606    0.000 fromnumeric.py:70(_wrapreduction)
               61426146   83.117    0.000  189.049    0.000 tensor.py:596(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 8557123: <CHASER_U_S_0_0.001returnchaser_0> in cluster <dcc> Done

Job <CHASER_U_S_0_0.001returnchaser_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Dec 11 15:08:12 2020
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Dec 16 15:41:24 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Dec 16 15:41:24 2020
Terminated at Thu Dec 17 14:36:59 2020
Results reported at Thu Dec 17 14:36:59 2020

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

    CPU time :                                   85275.00 sec.
    Max Memory :                                 55027 MB
    Average Memory :                             54312.65 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               6413.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82535 sec.
    Turnaround time :                            516527 sec.

The output (if any) is above this job summary.

