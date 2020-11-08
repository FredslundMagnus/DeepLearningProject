[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
main.py:33: RuntimeWarning: divide by zero encountered in double_scalars
  all_return.append(total_rew / dones)
Discount_0.999_1-0 0.999 fruitbot 20.0 200000 100
    Play for :                  1 games.
    Minutes used :              1198 minutes.
    Hours used :                19 hours.

# Profiling


      2184827415 function calls (2127198601 primitive calls) in 71911.23 seconds

##    Ordered by: cumulative time
   List reduced from 1328 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 71911.230 71911.230 {built-in method builtins.exec}
                      1    0.015    0.015 71911.230 71911.230 <string>:1(<module>)
                      1  124.123  124.123 71911.214 71911.214 main.py:16(main)
                1016841  156.949    0.000 67734.150    0.067 agent.py:45(learn)
                1016841   85.829    0.000 21618.539    0.021 memory.py:27(sample_distribution)
                1016841  110.540    0.000 21145.327    0.021 helpers.py:12(stack)
        62029101/4406411  401.632    0.000 18019.658    0.004 module.py:710(_call_impl)
                3389570   93.158    0.000 17881.511    0.005 agent.py:94(forward)
                7118235 16002.884    0.002 16002.910    0.002 {method 'to' of 'torch._C._TensorBase' objects}
               10168710   98.843    0.000 15315.049    0.002 container.py:115(forward)
                1016841    8.292    0.000 13329.900    0.013 tensor.py:155(backward)
                1016841    8.927    0.000 13321.608    0.013 __init__.py:57(backward)
                1016841 13277.727    0.013 13277.727    0.013 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1016841    3.181    0.000 12314.844    0.012 memory.py:75(empty_cache)
                1016841 12310.276    0.012 12310.276    0.012 {built-in method torch._C._cuda_emptyCache}
               20337420   29.425    0.000 9011.447    0.000 activation.py:653(forward)
               20337420   45.775    0.000 8982.022    0.000 functional.py:1277(leaky_relu)
               20337420 8931.707    0.000 8931.707    0.000 {built-in method torch._C._nn.leaky_relu}
               16947850   48.194    0.000 5411.884    0.000 conv.py:418(forward)
               16947850   51.377    0.000 5343.919    0.000 conv.py:410(_conv_forward)
               16947850 5283.366    0.000 5283.366    0.000 {built-in method conv2d}
                7118187 4769.393    0.001 4769.393    0.001 {built-in method cat}
                1016841    9.195    0.000 2325.483    0.002 grad_mode.py:12(decorate_context)
                1016841  592.903    0.001 2304.881    0.002 adam.py:51(step)
                 339047    7.110    0.000 1631.326    0.005 agent.py:40(chooseMulti)
                 339047   10.615    0.000 1307.332    0.004 environments.py:73(step)
                3389576  212.364    0.000 1191.267    0.000 rnn.py:109(flatten_parameters)
                3389570   53.019    0.000 1035.720    0.000 rnn.py:550(forward)
               46902228  927.356    0.000  927.356    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                 339047   19.315    0.000  920.816    0.003 agent.py:43(<listcomp>)
                3389570  914.599    0.000  914.599    0.000 {built-in method lstm}
                 339047    1.056    0.000  895.048    0.003 agent.py:32(rememberMulti)
                 339047   31.646    0.000  893.992    0.003 agent.py:33(<listcomp>)
                6780940  325.918    0.000  852.426    0.000 exploration.py:28(epsilonGreedy)
                9861720  838.592    0.000  838.592    0.000 {built-in method as_tensor}
                3389573  739.100    0.000  739.100    0.000 {built-in method _cudnn_rnn_flatten_weight}
                 339047    7.071    0.000  736.699    0.002 environments.py:75(<listcomp>)
                6811197  206.124    0.000  733.212    0.000 helpers.py:8(clean)
                 339047    7.966    0.000  533.349    0.002 environments.py:74(<listcomp>)
                6780940   29.790    0.000  525.383    0.000 interop.py:274(step)
               32538912  420.598    0.000  420.598    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               32538912  378.937    0.000  378.937    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3389570   13.295    0.000  292.037    0.000 linear.py:90(forward)
                6780940    3.886    0.000  283.991    0.000 wrapper.py:25(act)
                6780940   10.541    0.000  280.106    0.000 env.py:197(act)
                3389570   27.483    0.000  273.232    0.000 functional.py:1655(linear)
                6780940  263.537    0.000  264.360    0.000 libenv.py:352(act)
               16269456  260.785    0.000  260.785    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               13559155  207.006    0.000  223.076    0.000 module.py:774(__setattr__)
               16269456  214.246    0.000  214.246    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1016841  156.721    0.000  207.593    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
                1016841   36.432    0.000  207.519    0.000 optimizer.py:166(zero_grad)
                   3390    0.806    0.000  185.810    0.055 agent.py:63(update_target_network)
               16269456  182.824    0.000  182.824    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3389570  180.126    0.000  180.126    0.000 {built-in method addmm}
               16269456  172.808    0.000  172.808    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   3390   43.056    0.013  149.572    0.044 memory.py:37(update_distribution)
                6780940  144.765    0.000  144.765    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                6780940  139.219    0.000  139.219    0.000 {method 'std' of 'torch._C._TensorBase' objects}
                3389570   10.114    0.000  134.767    0.000 pooling.py:156(forward)
               13592137   11.717    0.000  128.808    0.000 extract_dict_ob.py:9(observe)
                3389570    8.098    0.000  124.653    0.000 _jit_internal.py:237(fn)
                7803961  120.845    0.000  120.845    0.000 {built-in method numpy.array}
               13592137    6.918    0.000  117.092    0.000 wrapper.py:19(observe)
                3389570    7.715    0.000  115.813    0.000 functional.py:564(_max_pool2d)
               16269456  115.228    0.000  115.228    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               13592137   29.041    0.000  110.174    0.000 libenv.py:344(observe)
                3389570  107.492    0.000  107.492    0.000 {built-in method max_pool2d}
               13558292   82.914    0.000   96.047    0.000 __init__.py:66(is_acceptable)
               81347328   79.680    0.000   94.124    0.000 tensor.py:725(grad)
                1016841    3.037    0.000   88.957    0.000 loss.py:444(forward)
                1016841   12.509    0.000   85.920    0.000 functional.py:2621(mse_loss)
                1016241   83.290    0.000   83.290    0.000 memory.py:35(<listcomp>)
               20373077   24.681    0.000   80.176    0.000 libenv.py:281(_maybe_copy_dict)
                8812822   71.703    0.000   71.703    0.000 {method 'view' of 'torch._C._TensorBase' objects}
               51925959   70.465    0.000   70.465    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               61122621   68.760    0.000   68.760    0.000 {method 'copy' of 'numpy.ndarray' objects}
                2033682   68.500    0.000   68.500    0.000 {built-in method gather}
               57745049   66.699    0.000   66.789    0.000 module.py:758(__getattr__)
                6780940    6.404    0.000   58.191    0.000 wrapper.py:22(get_info)
               62029101   55.001    0.000   55.001    0.000 {built-in method torch._C._get_tracing_state}
                2145685    5.364    0.000   53.300    0.000 <__array_function__ internals>:2(prod)
                6780940   26.835    0.000   51.786    0.000 libenv.py:363(get_info)
                1016242   51.470    0.000   51.470    0.000 {built-in method numpy.arange}
                1017141    2.412    0.000   49.559    0.000 functional.py:68(split)
                6780940   49.075    0.000   49.075    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1016841   47.965    0.000   47.965    0.000 {built-in method torch._C._nn.mse_loss}
                3165316   47.787    0.000   47.787    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                2145725    3.935    0.000   47.195    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                1017141    2.449    0.000   46.958    0.000 tensor.py:367(split)
                1017141   44.259    0.000   44.259    0.000 {function Tensor.split at 0x7f9eb4d48790}
                2145685    6.846    0.000   43.260    0.000 fromnumeric.py:2881(prod)
                3389570   13.902    0.000   42.702    0.000 rnn.py:524(check_forward_args)
                6780940   40.515    0.000   40.515    0.000 memory.py:15(inner)
                 564352   15.670    0.000   38.707    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              258285114   37.909    0.000   37.909    0.000 {method 'values' of 'collections.OrderedDict' objects}
                3389570   37.223    0.000   37.223    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2145685   11.884    0.000   36.414    0.000 fromnumeric.py:70(_wrapreduction)
                1016841    8.390    0.000   34.457    0.000 __init__.py:25(_make_grads)
                1019631    2.861    0.000   32.842    0.000 {method 'sum' of 'numpy.ndarray' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 8273881: <Discount_0.999_1_0> in cluster <dcc> Done

Job <Discount_0.999_1_0> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Sat Nov  7 15:36:09 2020
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov  7 16:25:55 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov  7 16:25:55 2020
Terminated at Sun Nov  8 12:24:31 2020
Results reported at Sun Nov  8 12:24:31 2020

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

    CPU time :                                   31380.00 sec.
    Max Memory :                                 24822 MB
    Average Memory :                             24321.17 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5898.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   71916 sec.
    Turnaround time :                            74902 sec.

The output (if any) is above this job summary.

