[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_ninja-0
    Discount :                  0.999
    Environment :               ninja
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


      10859022523 function calls (10636182303 primitive calls) in 86111.04 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86111.038 86111.038 {built-in method builtins.exec}
                      1    0.008    0.008 86111.037 86111.037 <string>:1(<module>)
                      1  545.316  545.316 86111.028 86111.028 main.py:11(main)
                3277047  113.694    0.000 59310.603    0.018 agent.py:46(learn)
                3276947  390.354    0.000 57446.866    0.018 agent.py:54(TD_learn)
                3276947  209.773    0.000 34552.036    0.011 memory.py:27(sample_distribution)
                3276947  323.406    0.000 33517.249    0.010 helpers.py:12(stack)
               29492871 17724.464    0.001 17724.492    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        239218931/16384835 1020.795    0.000 16134.067    0.001 module.py:710(_call_impl)
               13107888  261.139    0.000 15787.825    0.001 agent.py:117(forward)
               29492823 15069.167    0.001 15069.167    0.001 {built-in method cat}
                3277047   90.144    0.000 11052.244    0.003 environments.py:73(step)
               39323664  249.944    0.000 8635.123    0.000 container.py:115(forward)
              456286762 8355.646    0.000 8355.646    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3277047    9.502    0.000 8023.492    0.002 agent.py:32(rememberMulti)
                3277047  291.847    0.000 8013.989    0.002 agent.py:33(<listcomp>)
                3277047   48.355    0.000 6948.509    0.002 agent.py:41(chooseMulti)
                3277047   62.580    0.000 6690.107    0.002 environments.py:75(<listcomp>)
               65645883 1795.372    0.000 6639.471    0.000 helpers.py:8(clean)
               75476724 5595.758    0.000 5595.758    0.000 {built-in method as_tensor}
               65539440  108.458    0.000 5006.570    0.000 conv.py:418(forward)
               65539440  126.839    0.000 4850.721    0.000 conv.py:410(_conv_forward)
               65539440 4701.501    0.000 4701.501    0.000 {built-in method conv2d}
                3276947   22.005    0.000 4529.647    0.001 grad_mode.py:12(decorate_context)
                3276947 1146.427    0.000 4484.198    0.001 adam.py:51(step)
                3276947   18.060    0.000 4446.192    0.001 tensor.py:155(backward)
                3276947   22.277    0.000 4428.133    0.001 __init__.py:57(backward)
                3276947 4323.584    0.001 4323.584    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3277047   67.281    0.000 4063.093    0.001 environments.py:74(<listcomp>)
               65540940  243.906    0.000 3995.812    0.000 interop.py:274(step)
               13107894  586.794    0.000 3278.103    0.000 rnn.py:109(flatten_parameters)
               13107888  137.589    0.000 2968.697    0.000 rnn.py:550(forward)
               13107888 2662.924    0.000 2662.924    0.000 {built-in method lstm}
                3277047  115.589    0.000 2241.754    0.001 agent.py:44(<listcomp>)
               13107891 2024.457    0.000 2024.457    0.000 {built-in method _cudnn_rnn_flatten_weight}
               65540940   31.968    0.000 1992.105    0.000 wrapper.py:25(act)
               65540940   84.091    0.000 1960.137    0.000 env.py:197(act)
               65540940  182.785    0.000 1850.227    0.000 exploration.py:31(epsilonGreedy)
               65540940 1826.535    0.000 1832.842    0.000 libenv.py:352(act)
                  32770    6.258    0.000 1750.043    0.053 agent.py:81(update_target_network)
                  32770  446.962    0.014 1468.813    0.045 memory.py:37(update_distribution)
               78647328   85.388    0.000 1285.033    0.000 activation.py:653(forward)
               78647328  116.659    0.000 1199.645    0.000 functional.py:1277(leaky_relu)
               68883228 1124.017    0.000 1124.017    0.000 {built-in method numpy.array}
               78647328 1071.892    0.000 1071.892    0.000 {built-in method torch._C._nn.leaky_relu}
              131186823  100.891    0.000 1064.775    0.000 extract_dict_ob.py:9(observe)
              131186823   58.580    0.000  963.885    0.000 wrapper.py:19(observe)
              131186823  247.671    0.000  905.305    0.000 libenv.py:344(observe)
              104862304  819.562    0.000  819.562    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13107888   35.489    0.000  792.397    0.000 linear.py:90(forward)
               13107888   70.717    0.000  743.747    0.000 functional.py:1655(linear)
              104862304  731.475    0.000  731.475    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              196727763  203.779    0.000  655.350    0.000 libenv.py:281(_maybe_copy_dict)
               52432427  530.574    0.000  566.659    0.000 module.py:774(__setattr__)
              590216059  564.896    0.000  564.896    0.000 {method 'copy' of 'numpy.ndarray' objects}
               52431152  509.597    0.000  509.597    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               65540940   57.592    0.000  493.732    0.000 wrapper.py:22(get_info)
               13107888  492.674    0.000  492.674    0.000 {built-in method addmm}
              472461651  487.172    0.000  487.172    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                3276947  353.353    0.000  467.738    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               65540940  227.572    0.000  436.140    0.000 libenv.py:363(get_info)
               52431152  426.579    0.000  426.579    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               65540940  423.141    0.000  423.141    0.000 memory.py:15(inner)
                3276947   72.712    0.000  420.548    0.000 optimizer.py:166(zero_grad)
               13107888   29.514    0.000  381.662    0.000 pooling.py:156(forward)
               13107888   21.387    0.000  352.148    0.000 _jit_internal.py:237(fn)
               52431152  351.911    0.000  351.911    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               52431152  338.358    0.000  338.358    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13107888   23.534    0.000  328.590    0.000 functional.py:564(_max_pool2d)
               13107888  303.403    0.000  303.403    0.000 {built-in method max_pool2d}
                9831141   15.558    0.000  302.862    0.000 functional.py:68(split)
                9831141   16.073    0.000  286.054    0.000 tensor.py:367(split)
               65540940  275.938    0.000  275.938    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9831141  268.337    0.000  268.337    0.000 {function Tensor.split at 0x7f33962a9940}
               52431564  226.093    0.000  260.179    0.000 __init__.py:66(is_acceptable)
                3276748  242.490    0.000  242.490    0.000 memory.py:35(<listcomp>)
               52431152  238.178    0.000  238.178    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3277047   20.211    0.000  213.348    0.000 collector.py:7(collect)
                3276947    9.155    0.000  209.632    0.000 loss.py:444(forward)
                3277047   36.955    0.000  208.901    0.000 environments.py:76(<listcomp>)
                3276947   30.927    0.000  200.477    0.000 functional.py:2621(mse_loss)
              262373646   67.226    0.000  191.693    0.000 libenv.py:271(_maybe_copy_ndarray)
                6554095  191.587    0.000  191.587    0.000 {built-in method builtins.sum}
              262155808  156.020    0.000  182.113    0.000 tensor.py:725(grad)
               32769670  178.106    0.000  178.106    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               65540960   36.441    0.000  171.985    0.000 environments.py:79(reset)
              224014135  166.860    0.000  167.547    0.000 module.py:758(__getattr__)
                  65540   16.920    0.000  157.783    0.002 {built-in method _pickle.loads}
                6553894  153.922    0.000  153.922    0.000 {built-in method gather}
              239218931  144.386    0.000  144.386    0.000 {built-in method torch._C._get_tracing_state}
                  65540   28.926    0.000  117.188    0.002 {built-in method _pickle.dumps}
               13107888   36.284    0.000  112.362    0.000 rnn.py:524(check_forward_args)
                3276947  110.652    0.000  110.652    0.000 {built-in method torch._C._nn.mse_loss}
                8276723   11.523    0.000  110.279    0.000 <__array_function__ internals>:2(prod)
                1179718    1.333    0.000  108.634    0.000 storage.py:141(_load_from_bytes)
                1179718    5.714    0.000  107.301    0.000 serialization.py:486(load)
               13107888  104.528    0.000  104.528    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8276763    9.163    0.000   97.011    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               65645923   48.186    0.000   95.323    0.000 types.py:163(multimap)
                1179718    6.522    0.000   89.547    0.000 serialization.py:605(_legacy_load)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8371237: <Base_ninja_0> in cluster <dcc> Done

Job <Base_ninja_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:32 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Nov 20 05:58:11 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 20 05:58:11 2020
Terminated at Sat Nov 21 05:53:26 2020
Results reported at Sat Nov 21 05:53:26 2020

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

    CPU time :                                   88294.00 sec.
    Max Memory :                                 25252 MB
    Average Memory :                             24944.99 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5468.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86117 sec.
    Turnaround time :                            287814 sec.

The output (if any) is above this job summary.

