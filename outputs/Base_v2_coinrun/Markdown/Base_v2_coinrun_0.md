[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Base_v2_coinrun-0
    Discount :                  0.995
    Environment :               coinrun
    Hours :                     24
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      9149363877 function calls (8949052019 primitive calls) in 86128.26 seconds

##    Ordered by: cumulative time
   List reduced from 1320 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86128.258 86128.258 {built-in method builtins.exec}
                      1    0.040    0.040 86128.258 86128.258 <string>:1(<module>)
                      1  468.875  468.875 86128.217 86128.217 main.py:12(main)
                2635976   97.546    0.000 53592.230    0.020 agent.py:46(learn)
                2635476  380.944    0.000 52755.913    0.020 agent.py:54(TD_learn)
                2635476  182.531    0.000 27724.428    0.011 memory.py:27(sample_distribution)
                2635476  280.458    0.000 26862.647    0.010 helpers.py:12(stack)
        213483556/13177880  923.329    0.000 16711.348    0.001 module.py:710(_call_impl)
               10542404  238.606    0.000 16406.779    0.002 agent.py:119(forward)
              357376483 14332.153    0.000 14332.153    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
               23720838 14284.780    0.001 14284.821    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                2635976   46.370    0.000 13694.287    0.005 agent.py:41(chooseMulti)
               23720784 11915.818    0.001 11915.818    0.001 {built-in method cat}
                2635976   70.533    0.000 10404.185    0.004 environments.py:73(step)
               31627212  258.754    0.000 9366.040    0.000 container.py:115(forward)
                2635976  125.255    0.000 8949.727    0.003 agent.py:44(<listcomp>)
               52719520  179.495    0.000 8500.791    0.000 exploration.py:33(epsilonGreedy)
                2635976    7.910    0.000 7758.003    0.003 agent.py:32(rememberMulti)
                2635976  321.465    0.000 7750.093    0.003 agent.py:33(<listcomp>)
                2635976   54.266    0.000 6064.898    0.002 environments.py:75(<listcomp>)
               52825848 1489.330    0.000 6025.130    0.000 helpers.py:8(clean)
                2635476   17.465    0.000 5707.166    0.002 grad_mode.py:12(decorate_context)
                2635476 1344.606    0.001 5669.989    0.002 adam.py:51(step)
               63254424  106.659    0.000 5611.047    0.000 conv.py:418(forward)
               63254424  116.292    0.000 5458.844    0.000 conv.py:410(_conv_forward)
               63254424 5322.226    0.000 5322.226    0.000 {built-in method conv2d}
               60732276 5234.900    0.000 5234.900    0.000 {built-in method as_tensor}
                2635476   15.461    0.000 4842.102    0.002 tensor.py:155(backward)
                2635476   18.883    0.000 4826.642    0.002 __init__.py:57(backward)
                2635476 4731.226    0.002 4731.226    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2635976   55.662    0.000 4064.139    0.002 environments.py:74(<listcomp>)
               52719520  214.346    0.000 4008.478    0.000 interop.py:274(step)
               10542410  528.607    0.000 3457.286    0.000 rnn.py:109(flatten_parameters)
               10542404  112.904    0.000 2749.597    0.000 rnn.py:550(forward)
               10542404 2493.749    0.000 2493.749    0.000 {built-in method lstm}
               10542407 2294.731    0.000 2294.731    0.000 {built-in method _cudnn_rnn_flatten_weight}
               52719520   27.088    0.000 2268.349    0.000 wrapper.py:25(act)
               52719520   79.281    0.000 2241.261    0.000 env.py:197(act)
               52719520 2110.191    0.000 2115.343    0.000 libenv.py:352(act)
               73796828   66.104    0.000 1499.599    0.000 activation.py:653(forward)
               73796828  102.162    0.000 1433.494    0.000 functional.py:1277(leaky_relu)
               73796828 1321.567    0.000 1321.567    0.000 {built-in method torch._C._nn.leaky_relu}
               94877136 1126.658    0.000 1126.658    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               94877136  996.445    0.000  996.445    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              105545368   82.361    0.000  926.017    0.000 extract_dict_ob.py:9(observe)
              105545368   49.497    0.000  843.656    0.000 wrapper.py:19(observe)
              105545368  212.774    0.000  794.159    0.000 libenv.py:344(observe)
               10542404   29.312    0.000  756.389    0.000 linear.py:90(forward)
                   5271    1.251    0.000  738.771    0.140 agent.py:81(update_target_network)
               10542404   59.640    0.000  716.165    0.000 functional.py:1655(linear)
                   5271  190.365    0.036  673.555    0.128 memory.py:37(update_distribution)
               47438568  615.791    0.000  615.791    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               55365538  579.107    0.000  579.107    0.000 {built-in method numpy.array}
              370341247  578.178    0.000  578.178    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                2635476   86.748    0.000  565.227    0.000 optimizer.py:166(zero_grad)
              158264888  169.770    0.000  560.436    0.000 libenv.py:281(_maybe_copy_dict)
               42170596  509.132    0.000  549.666    0.000 module.py:774(__setattr__)
               47438568  527.295    0.000  527.295    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              474799935  494.203    0.000  494.203    0.000 {method 'copy' of 'numpy.ndarray' objects}
               10542404  486.052    0.000  486.052    0.000 {built-in method addmm}
               47438568  459.604    0.000  459.604    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47438568  447.356    0.000  447.356    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               52719520   45.708    0.000  425.040    0.000 wrapper.py:22(get_info)
               11660157  167.322    0.000  415.508    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               52719520  388.114    0.000  388.114    0.000 memory.py:15(inner)
                2635476  294.197    0.000  382.453    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               52719520  203.368    0.000  379.332    0.000 libenv.py:363(get_info)
               10542404   23.413    0.000  366.740    0.000 pooling.py:156(forward)
               47438568  345.771    0.000  345.771    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10542404   17.487    0.000  343.327    0.000 _jit_internal.py:237(fn)
               10542404   19.120    0.000  324.021    0.000 functional.py:564(_max_pool2d)
               52719520  323.680    0.000  323.680    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               10542404  303.663    0.000  303.663    0.000 {built-in method max_pool2d}
               25955930   25.197    0.000  297.333    0.000 <__array_function__ internals>:2(prod)
               42169628  255.810    0.000  286.197    0.000 __init__.py:66(is_acceptable)
                7907928   13.951    0.000  269.542    0.000 functional.py:68(split)
               25955970   19.888    0.000  267.764    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                7907928   14.942    0.000  254.636    0.000 tensor.py:367(split)
               25955930   33.093    0.000  247.876    0.000 fromnumeric.py:2881(prod)
                7907928  238.270    0.000  238.270    0.000 {function Tensor.split at 0x7f14fd2d2940}
               25955930   59.238    0.000  214.783    0.000 fromnumeric.py:70(_wrapreduction)
                2635976   30.248    0.000  204.614    0.000 environments.py:76(<listcomp>)
               26355760  196.088    0.000  196.088    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                2635476  195.549    0.000  195.549    0.000 memory.py:35(<listcomp>)
                2635476    6.623    0.000  192.693    0.000 loss.py:444(forward)
              237192894  162.666    0.000  187.407    0.000 tensor.py:725(grad)
                2635476   24.729    0.000  186.070    0.000 functional.py:2621(mse_loss)
              211090736   63.356    0.000  178.461    0.000 libenv.py:271(_maybe_copy_ndarray)
                2635976   17.118    0.000  176.756    0.000 collector.py:7(collect)
               52719540   32.566    0.000  174.391    0.000 environments.py:79(reset)
               28596677  166.314    0.000  166.314    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                5271953  158.473    0.000  158.473    0.000 {built-in method builtins.sum}
              213483556  158.333    0.000  158.333    0.000 {built-in method torch._C._get_tracing_state}
                5270952  149.700    0.000  149.700    0.000 {built-in method gather}
              200516865  146.802    0.000  146.921    0.000 module.py:758(__getattr__)
                2635476  110.546    0.000  110.546    0.000 {built-in method torch._C._nn.mse_loss}
               10542404  107.698    0.000  107.698    0.000 {method 't' of 'torch._C._TensorBase' objects}
               10542404   30.539    0.000   92.163    0.000 rnn.py:524(check_forward_args)
              885561436   83.549    0.000   83.549    0.000 {method 'values' of 'collections.OrderedDict' objects}
               52825888   39.752    0.000   83.241    0.000 types.py:163(multimap)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8423561: <Base_v2_coinrun_0> in cluster <dcc> Done

Job <Base_v2_coinrun_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue Nov 24 19:48:56 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Nov 25 21:27:48 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Wed Nov 25 21:27:48 2020
Terminated at Thu Nov 26 21:23:30 2020
Results reported at Thu Nov 26 21:23:30 2020

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

    CPU time :                                   90422.00 sec.
    Max Memory :                                 56731 MB
    Average Memory :                             56007.55 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4709.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86143 sec.
    Turnaround time :                            178474 sec.

The output (if any) is above this job summary.

