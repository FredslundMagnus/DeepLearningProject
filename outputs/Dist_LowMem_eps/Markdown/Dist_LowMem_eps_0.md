[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Dist_LowMem_eps-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    50000
    Update every :              100
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      11212071569 function calls (10983437477 primitive calls) in 86111.83 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.001    0.000 86111.831 86111.831 {built-in method builtins.exec}
                      1    0.020    0.020 86111.831 86111.831 <string>:1(<module>)
                      1  528.228  528.228 86111.810 86111.810 main.py:11(main)
                3362251  109.900    0.000 58246.740    0.017 agent.py:46(learn)
                3362151  396.894    0.000 57501.376    0.017 agent.py:54(TD_learn)
                3362151  217.211    0.000 34626.680    0.010 memory.py:27(sample_distribution)
                3362151  304.029    0.000 33617.001    0.010 helpers.py:12(stack)
               30259707 18225.858    0.001 18225.916    0.001 {method 'to' of 'torch._C._TensorBase' objects}
        245438823/16810855 1030.392    0.000 16204.423    0.001 module.py:710(_call_impl)
               13448704  268.958    0.000 15856.213    0.001 agent.py:117(forward)
               30259659 14733.387    0.000 14733.387    0.000 {built-in method cat}
                3362251   88.562    0.000 11427.867    0.003 environments.py:73(step)
              463584358 8791.867    0.000 8791.867    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               40346112  262.310    0.000 8722.924    0.000 container.py:115(forward)
                3362251    9.302    0.000 7901.479    0.002 agent.py:32(rememberMulti)
                3362251  282.288    0.000 7892.177    0.002 agent.py:33(<listcomp>)
                3362251   47.992    0.000 7778.239    0.002 agent.py:41(chooseMulti)
                3362251   65.198    0.000 6733.773    0.002 environments.py:75(<listcomp>)
               67451231 1802.364    0.000 6691.415    0.000 helpers.py:8(clean)
               77537684 5591.420    0.000 5591.420    0.000 {built-in method as_tensor}
               67243520  111.604    0.000 5019.326    0.000 conv.py:418(forward)
               67243520  130.143    0.000 4858.536    0.000 conv.py:410(_conv_forward)
               67243520 4706.239    0.000 4706.239    0.000 {built-in method conv2d}
                3362151   20.883    0.000 4498.371    0.001 grad_mode.py:12(decorate_context)
                3362151 1129.702    0.000 4453.408    0.001 adam.py:51(step)
                3362151   17.184    0.000 4419.107    0.001 tensor.py:155(backward)
                3362151   23.341    0.000 4401.923    0.001 __init__.py:57(backward)
                3362251   67.723    0.000 4381.877    0.001 environments.py:74(<listcomp>)
               67245020  244.208    0.000 4314.155    0.000 interop.py:274(step)
                3362151 4293.696    0.001 4293.696    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               13448710  583.898    0.000 3278.955    0.000 rnn.py:109(flatten_parameters)
                3362251  129.187    0.000 3060.382    0.001 agent.py:44(<listcomp>)
               13448704  144.110    0.000 2919.963    0.000 rnn.py:550(forward)
               67245020  179.486    0.000 2642.165    0.000 exploration.py:31(epsilonGreedy)
               13448704 2607.750    0.000 2607.750    0.000 {built-in method lstm}
               67245020   30.684    0.000 2325.485    0.000 wrapper.py:25(act)
               67245020   79.945    0.000 2294.802    0.000 env.py:197(act)
               67245020 2165.308    0.000 2171.764    0.000 libenv.py:352(act)
               13448707 2007.789    0.000 2007.789    0.000 {built-in method _cudnn_rnn_flatten_weight}
               80692224   89.356    0.000 1334.008    0.000 activation.py:653(forward)
               80692224  141.694    0.000 1244.652    0.000 functional.py:1277(leaky_relu)
               80692224 1092.126    0.000 1092.126    0.000 {built-in method torch._C._nn.leaky_relu}
              134696251   94.221    0.000 1052.816    0.000 extract_dict_ob.py:9(observe)
              134696251   58.361    0.000  958.595    0.000 wrapper.py:19(observe)
              134696251  251.171    0.000  900.234    0.000 libenv.py:344(observe)
              107588832  830.164    0.000  830.164    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13448704   35.660    0.000  805.359    0.000 linear.py:90(forward)
               13448704   71.853    0.000  756.524    0.000 functional.py:1655(linear)
              107588832  725.125    0.000  725.125    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              201941271  205.975    0.000  652.159    0.000 libenv.py:281(_maybe_copy_dict)
                  33622    5.885    0.000  635.464    0.019 agent.py:81(update_target_network)
               53795691  517.910    0.000  556.489    0.000 module.py:774(__setattr__)
              605857435  545.299    0.000  545.299    0.000 {method 'copy' of 'numpy.ndarray' objects}
               13448704  501.345    0.000  501.345    0.000 {built-in method addmm}
               53794416  499.240    0.000  499.240    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67245020   55.478    0.000  497.484    0.000 wrapper.py:22(get_info)
              479982731  472.362    0.000  472.362    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                3362151  342.187    0.000  446.105    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               67245020  232.976    0.000  442.006    0.000 libenv.py:363(get_info)
                3362151   72.682    0.000  419.116    0.000 optimizer.py:166(zero_grad)
               53794416  417.542    0.000  417.542    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               67245020  407.499    0.000  407.499    0.000 memory.py:15(inner)
               13448704   30.077    0.000  387.398    0.000 pooling.py:156(forward)
               70674216  368.619    0.000  368.619    0.000 {built-in method numpy.array}
               13448704   21.759    0.000  357.321    0.000 _jit_internal.py:237(fn)
                  33622   94.726    0.003  356.549    0.011 memory.py:37(update_distribution)
               53794416  355.284    0.000  355.284    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                7130782  144.764    0.000  350.797    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               53794416  341.602    0.000  341.602    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13448704   26.068    0.000  333.339    0.000 functional.py:564(_max_pool2d)
               10086753   17.106    0.000  307.465    0.000 functional.py:68(split)
               13448704  305.545    0.000  305.545    0.000 {built-in method max_pool2d}
               10086753   16.278    0.000  289.074    0.000 tensor.py:367(split)
               67245020  289.030    0.000  289.030    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               53794828  235.125    0.000  271.394    0.000 __init__.py:66(is_acceptable)
               10086753  271.079    0.000  271.079    0.000 {function Tensor.split at 0x7f717aefc940}
               17623855   23.194    0.000  263.618    0.000 <__array_function__ internals>:2(prod)
                3361952  241.349    0.000  241.349    0.000 memory.py:35(<listcomp>)
               53794416  237.069    0.000  237.069    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               17623895   17.744    0.000  237.032    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                3362251   35.535    0.000  223.655    0.000 environments.py:76(<listcomp>)
               17623855   30.846    0.000  219.288    0.000 fromnumeric.py:2881(prod)
                3362251   20.382    0.000  210.867    0.000 collector.py:7(collect)
                3362151    8.290    0.000  207.437    0.000 loss.py:444(forward)
                3362151   31.223    0.000  199.147    0.000 functional.py:2621(mse_loss)
                6724503  188.898    0.000  188.898    0.000 {built-in method builtins.sum}
               17623855   55.551    0.000  188.441    0.000 fromnumeric.py:70(_wrapreduction)
               67245040   39.039    0.000  188.126    0.000 environments.py:79(reset)
              269392502   68.905    0.000  185.336    0.000 libenv.py:271(_maybe_copy_ndarray)
               33621710  183.897    0.000  183.897    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              229838679  177.471    0.000  178.117    0.000 module.py:758(__getattr__)
              268972128  153.533    0.000  177.349    0.000 tensor.py:725(grad)
                  67244   16.728    0.000  156.779    0.002 {built-in method _pickle.loads}
               21019429  154.192    0.000  154.192    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                6724302  147.929    0.000  147.929    0.000 {built-in method gather}
              245438823  145.232    0.000  145.232    0.000 {built-in method torch._C._get_tracing_state}
                  67244   28.477    0.000  116.251    0.002 {built-in method _pickle.dumps}
               13448704   37.439    0.000  112.964    0.000 rnn.py:524(check_forward_args)
                3362151  110.365    0.000  110.365    0.000 {built-in method torch._C._nn.mse_loss}
                1210390    1.295    0.000  108.417    0.000 storage.py:141(_load_from_bytes)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8366148: <Dist_LowMem_eps_0> in cluster <dcc> Done

Job <Dist_LowMem_eps_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Mon Nov 16 20:57:20 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Nov 17 20:41:56 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Tue Nov 17 20:41:56 2020
Terminated at Wed Nov 18 20:37:15 2020
Results reported at Wed Nov 18 20:37:15 2020

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

    CPU time :                                   88440.00 sec.
    Max Memory :                                 8529 MB
    Average Memory :                             8255.55 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               22191.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86120 sec.
    Turnaround time :                            171595 sec.

The output (if any) is above this job summary.

