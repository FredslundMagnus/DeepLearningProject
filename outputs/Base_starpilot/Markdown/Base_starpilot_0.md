[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_starpilot-0
    Discount :                  0.999
    Environment :               starpilot
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


      10610115033 function calls (10392460561 primitive calls) in 86146.84 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86146.844 86146.844 {built-in method builtins.exec}
                      1    0.018    0.018 86146.844 86146.844 <string>:1(<module>)
                      1  543.971  543.971 86146.825 86146.825 main.py:11(main)
                3200786  112.499    0.000 59743.673    0.019 agent.py:46(learn)
                3200686  382.458    0.000 57857.353    0.018 agent.py:54(TD_learn)
                3200686  202.725    0.000 35528.968    0.011 memory.py:27(sample_distribution)
                3200686  313.000    0.000 34518.271    0.011 helpers.py:12(stack)
               28806522 17922.877    0.001 17922.882    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               28806474 15879.307    0.001 15879.307    0.001 {built-in method cat}
        233651878/16003530 1011.001    0.000 15658.182    0.001 module.py:710(_call_impl)
               12802844  248.805    0.000 15326.271    0.001 agent.py:117(forward)
                3200786   85.898    0.000 10819.527    0.003 environments.py:73(step)
               38408532  245.029    0.000 8410.050    0.000 container.py:115(forward)
              445609569 8374.092    0.000 8374.092    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3200786    9.285    0.000 8219.384    0.003 agent.py:32(rememberMulti)
                3200786  257.774    0.000 8210.099    0.003 agent.py:33(<listcomp>)
                3200786   54.804    0.000 6637.500    0.002 environments.py:75(<listcomp>)
               64263900 1814.987    0.000 6610.920    0.000 helpers.py:8(clean)
                3200786   45.854    0.000 6556.281    0.002 agent.py:41(chooseMulti)
               73865958 5564.371    0.000 5564.371    0.000 {built-in method as_tensor}
               64014220  109.381    0.000 4862.308    0.000 conv.py:418(forward)
               64014220  121.123    0.000 4705.288    0.000 conv.py:410(_conv_forward)
               64014220 4561.677    0.000 4561.677    0.000 {built-in method conv2d}
                3200686   19.419    0.000 4445.124    0.001 grad_mode.py:12(decorate_context)
                3200686 1131.479    0.000 4404.888    0.001 adam.py:51(step)
                3200686   18.370    0.000 4349.702    0.001 tensor.py:155(backward)
                3200686   21.056    0.000 4331.332    0.001 __init__.py:57(backward)
                3200686 4231.038    0.001 4231.038    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3200786   67.377    0.000 3866.198    0.001 environments.py:74(<listcomp>)
               64015720  243.891    0.000 3798.821    0.000 interop.py:274(step)
               12802850  562.440    0.000 3168.479    0.000 rnn.py:109(flatten_parameters)
               12802844  131.924    0.000 2879.575    0.000 rnn.py:550(forward)
               12802844 2588.038    0.000 2588.038    0.000 {built-in method lstm}
                3200786  114.136    0.000 1986.590    0.001 agent.py:44(<listcomp>)
               12802847 1957.191    0.000 1957.191    0.000 {built-in method _cudnn_rnn_flatten_weight}
               64015720   31.406    0.000 1804.041    0.000 wrapper.py:25(act)
                  32007    6.266    0.000 1773.820    0.055 agent.py:81(update_target_network)
               64015720   80.927    0.000 1772.635    0.000 env.py:197(act)
               64015720 1640.917    0.000 1647.313    0.000 libenv.py:352(act)
               64015720  171.067    0.000 1601.511    0.000 exploration.py:31(epsilonGreedy)
                  32007  432.273    0.014 1499.284    0.047 memory.py:37(update_distribution)
               76817064   69.962    0.000 1255.413    0.000 activation.py:653(forward)
               76817064  107.510    0.000 1185.451    0.000 functional.py:1277(leaky_relu)
               67280221 1167.334    0.000 1167.334    0.000 {built-in method numpy.array}
              128279620   96.541    0.000 1070.475    0.000 extract_dict_ob.py:9(observe)
               76817064 1067.429    0.000 1067.429    0.000 {built-in method torch._C._nn.leaky_relu}
              128279620   55.376    0.000  973.934    0.000 wrapper.py:19(observe)
              128279620  238.538    0.000  918.558    0.000 libenv.py:344(observe)
              102421952  810.569    0.000  810.569    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12802844   34.440    0.000  764.598    0.000 linear.py:90(forward)
              102421952  717.765    0.000  717.765    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               12802844   65.998    0.000  717.065    0.000 functional.py:1655(linear)
              192295340  201.938    0.000  678.287    0.000 libenv.py:281(_maybe_copy_dict)
              576918027  586.046    0.000  586.046    0.000 {method 'copy' of 'numpy.ndarray' objects}
               51212251  520.063    0.000  554.941    0.000 module.py:774(__setattr__)
               51210976  494.067    0.000  494.067    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               64015720   53.630    0.000  486.560    0.000 wrapper.py:22(get_info)
               12802844  479.372    0.000  479.372    0.000 {built-in method addmm}
              461116679  464.345    0.000  464.345    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                3200686  346.991    0.000  457.144    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               64015720  226.154    0.000  432.930    0.000 libenv.py:363(get_info)
               64015720  420.839    0.000  420.839    0.000 memory.py:15(inner)
               51210976  415.507    0.000  415.507    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3200686   71.848    0.000  410.387    0.000 optimizer.py:166(zero_grad)
               12802844   28.983    0.000  372.411    0.000 pooling.py:156(forward)
               51210976  350.371    0.000  350.371    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12802844   20.614    0.000  343.428    0.000 _jit_internal.py:237(fn)
               51210976  333.438    0.000  333.438    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               12802844   22.534    0.000  320.838    0.000 functional.py:564(_max_pool2d)
                9602358   14.764    0.000  299.584    0.000 functional.py:68(split)
               12802844  296.634    0.000  296.634    0.000 {built-in method max_pool2d}
                9602358   17.053    0.000  283.555    0.000 tensor.py:367(split)
               64015720  270.943    0.000  270.943    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9602358  264.965    0.000  264.965    0.000 {function Tensor.split at 0x7f20b7096940}
               51211388  226.368    0.000  260.688    0.000 __init__.py:66(is_acceptable)
                3200487  238.121    0.000  238.121    0.000 memory.py:35(<listcomp>)
               51210976  232.847    0.000  232.847    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3200786   34.904    0.000  229.931    0.000 environments.py:76(<listcomp>)
                3200786   19.602    0.000  211.365    0.000 collector.py:7(collect)
                3200686    7.942    0.000  202.251    0.000 loss.py:444(forward)
               64015740   39.706    0.000  195.071    0.000 environments.py:79(reset)
                3200686   30.731    0.000  194.309    0.000 functional.py:2621(mse_loss)
                6401573  190.354    0.000  190.354    0.000 {built-in method builtins.sum}
              256559240   67.784    0.000  188.548    0.000 libenv.py:271(_maybe_copy_ndarray)
              256054928  149.016    0.000  174.869    0.000 tensor.py:725(grad)
               32007060  171.550    0.000  171.550    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              218800919  163.171    0.000  163.818    0.000 module.py:758(__getattr__)
                  64014   16.399    0.000  152.542    0.002 {built-in method _pickle.loads}
                6401372  148.795    0.000  148.795    0.000 {built-in method gather}
              233651878  138.397    0.000  138.397    0.000 {built-in method torch._C._get_tracing_state}
                  64014   28.369    0.000  115.729    0.002 {built-in method _pickle.dumps}
                8201768   11.482    0.000  108.985    0.000 <__array_function__ internals>:2(prod)
                3200686  108.619    0.000  108.619    0.000 {built-in method torch._C._nn.mse_loss}
               12802844   34.794    0.000  106.557    0.000 rnn.py:524(check_forward_args)
                1152250    1.265    0.000  105.535    0.000 storage.py:141(_load_from_bytes)
                1152250    5.568    0.000  104.270    0.000 serialization.py:486(load)
               12802844  100.427    0.000  100.427    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8201808    8.462    0.000   95.818    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              973016044   94.232    0.000   94.232    0.000 {method 'values' of 'collections.OrderedDict' objects}
               64263940   46.381    0.000   94.021    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 8371239: <Base_starpilot_0> in cluster <dcc> Done

Job <Base_starpilot_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Tue Nov 17 21:56:32 2020
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Nov 21 08:55:50 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 21 08:55:50 2020
Terminated at Sun Nov 22 08:52:01 2020
Results reported at Sun Nov 22 08:52:01 2020

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

    CPU time :                                   88258.00 sec.
    Max Memory :                                 25315 MB
    Average Memory :                             24993.54 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5405.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86170 sec.
    Turnaround time :                            384929 sec.

The output (if any) is above this job summary.

