[W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())

    Name :                      Dist_eps-0
    Discount :                  0.999
    Environment :               fruitbot
    Hours :                     24
    Memory :                    200000
    Update every :              100
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           50
    Uncertainty :               0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      10030354010 function calls (9825827618 primitive calls) in 86117.24 seconds

##    Ordered by: cumulative time
   List reduced from 1321 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   79/1    0.000    0.000 86117.242 86117.242 {built-in method builtins.exec}
                      1    0.028    0.028 86117.242 86117.242 <string>:1(<module>)
                      1  500.555  500.555 86117.213 86117.213 main.py:11(main)
                3007726  107.789    0.000 58184.963    0.019 agent.py:46(learn)
                3007626  429.293    0.000 56490.729    0.019 agent.py:54(TD_learn)
                3007626  200.620    0.000 31189.725    0.010 memory.py:27(sample_distribution)
                3007626  307.435    0.000 30235.549    0.010 helpers.py:12(stack)
        219558498/15038230  968.060    0.000 16912.588    0.001 module.py:710(_call_impl)
               12030604  264.078    0.000 16568.895    0.001 agent.py:117(forward)
               27068982 16163.758    0.001 16163.822    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               27068934 13408.924    0.000 13408.924    0.000 {built-in method cat}
                3007726   82.846    0.000 11217.731    0.004 environments.py:73(step)
               36091812  259.288    0.000 9099.175    0.000 container.py:115(forward)
                3007726    9.161    0.000 8738.211    0.003 agent.py:32(rememberMulti)
                3007726  376.658    0.000 8729.050    0.003 agent.py:33(<listcomp>)
              414661089 8513.492    0.000 8513.492    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                3007726   49.517    0.000 7252.989    0.002 agent.py:41(chooseMulti)
                3007726   64.150    0.000 6649.670    0.002 environments.py:75(<listcomp>)
               60339359 1652.781    0.000 6608.138    0.000 helpers.py:8(clean)
                3007626   19.945    0.000 5746.137    0.002 grad_mode.py:12(decorate_context)
                3007626 1355.384    0.000 5703.474    0.002 adam.py:51(step)
               69362237 5681.345    0.000 5681.345    0.000 {built-in method as_tensor}
               60153020  102.814    0.000 5289.549    0.000 conv.py:418(forward)
               60153020  111.922    0.000 5144.483    0.000 conv.py:410(_conv_forward)
               60153020 5012.869    0.000 5012.869    0.000 {built-in method conv2d}
                3007626   18.007    0.000 4872.598    0.002 tensor.py:155(backward)
                3007626   21.493    0.000 4854.591    0.002 __init__.py:57(backward)
                3007626 4745.907    0.002 4745.907    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3007726   62.756    0.000 4255.378    0.001 environments.py:74(<listcomp>)
               60154520  239.453    0.000 4192.622    0.000 interop.py:274(step)
               12030610  565.905    0.000 3699.343    0.000 rnn.py:109(flatten_parameters)
               12030604  131.358    0.000 2859.646    0.000 rnn.py:550(forward)
               12030604 2564.504    0.000 2564.504    0.000 {built-in method lstm}
               12030607 2460.137    0.000 2460.137    0.000 {built-in method _cudnn_rnn_flatten_weight}
                3007726  133.997    0.000 2338.543    0.001 agent.py:44(<listcomp>)
               60154520   27.268    0.000 2246.180    0.000 wrapper.py:25(act)
               60154520   88.520    0.000 2218.912    0.000 env.py:197(act)
               60154520 2074.028    0.000 2079.592    0.000 libenv.py:352(act)
               60154520  212.758    0.000 1852.286    0.000 exploration.py:31(epsilonGreedy)
                  30077    5.665    0.000 1586.445    0.053 agent.py:81(update_target_network)
               72183624   68.680    0.000 1447.640    0.000 activation.py:653(forward)
               72183624  103.882    0.000 1378.960    0.000 functional.py:1277(leaky_relu)
                  30077  408.241    0.014 1320.548    0.044 memory.py:37(update_distribution)
               72183624 1265.485    0.000 1265.485    0.000 {built-in method torch._C._nn.leaky_relu}
               96244032 1131.967    0.000 1131.967    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              120493879   93.962    0.000 1034.455    0.000 extract_dict_ob.py:9(observe)
               63222101 1015.539    0.000 1015.539    0.000 {built-in method numpy.array}
               96244032 1004.296    0.000 1004.296    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              120493879   51.904    0.000  940.493    0.000 wrapper.py:19(observe)
              120493879  236.944    0.000  888.589    0.000 libenv.py:344(observe)
               12030604   31.441    0.000  819.207    0.000 linear.py:90(forward)
               12030604   64.513    0.000  776.148    0.000 functional.py:1655(linear)
              429329581  651.370    0.000  651.370    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              180648399  195.198    0.000  633.272    0.000 libenv.py:281(_maybe_copy_dict)
               48122016  620.603    0.000  620.603    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3007626   88.382    0.000  564.664    0.000 optimizer.py:166(zero_grad)
              541975274  558.480    0.000  558.480    0.000 {method 'copy' of 'numpy.ndarray' objects}
               48122016  528.291    0.000  528.291    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               12030604  525.042    0.000  525.042    0.000 {built-in method addmm}
               48123291  485.378    0.000  517.531    0.000 module.py:774(__setattr__)
               60154520   54.905    0.000  476.896    0.000 wrapper.py:22(get_info)
               48122016  459.922    0.000  459.922    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48122016  448.989    0.000  448.989    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3007626  331.385    0.000  432.637    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               60154520  221.038    0.000  421.992    0.000 libenv.py:363(get_info)
               60154520  416.954    0.000  416.954    0.000 memory.py:15(inner)
               12030604   28.310    0.000  406.426    0.000 pooling.py:156(forward)
               12030604   19.548    0.000  378.116    0.000 _jit_internal.py:237(fn)
               12030604   21.207    0.000  356.535    0.000 functional.py:564(_max_pool2d)
               60154520  352.261    0.000  352.261    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                6420551  150.198    0.000  347.183    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               48122016  345.812    0.000  345.812    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               12030604  333.925    0.000  333.925    0.000 {built-in method max_pool2d}
                9023178   14.758    0.000  307.716    0.000 functional.py:68(split)
                9023178   16.115    0.000  291.888    0.000 tensor.py:367(split)
                9023178  274.213    0.000  274.213    0.000 {function Tensor.split at 0x7fcbe4632940}
               48122428  239.143    0.000  272.729    0.000 __init__.py:66(is_acceptable)
               15848868   21.875    0.000  253.248    0.000 <__array_function__ internals>:2(prod)
                3007726   34.707    0.000  229.837    0.000 environments.py:76(<listcomp>)
               15848908   16.257    0.000  227.968    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                3007427  218.065    0.000  218.065    0.000 memory.py:35(<listcomp>)
                3007626    8.413    0.000  213.992    0.000 loss.py:444(forward)
               15848868   27.976    0.000  211.710    0.000 fromnumeric.py:2881(prod)
                3007626   28.526    0.000  205.578    0.000 functional.py:2621(mse_loss)
               30076460  203.019    0.000  203.019    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                3007726   19.219    0.000  198.947    0.000 collector.py:7(collect)
              240987758   67.033    0.000  198.610    0.000 libenv.py:271(_maybe_copy_ndarray)
               60154540   34.878    0.000  195.174    0.000 environments.py:79(reset)
              240610128  158.841    0.000  184.397    0.000 tensor.py:725(grad)
               15848868   50.839    0.000  183.735    0.000 fromnumeric.py:70(_wrapreduction)
                6015453  178.407    0.000  178.407    0.000 {built-in method builtins.sum}
              219558498  167.892    0.000  167.892    0.000 {built-in method torch._C._get_tracing_state}
                6015252  162.392    0.000  162.392    0.000 {built-in method gather}
               18886372  156.851    0.000  156.851    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                  60154   15.661    0.000  150.780    0.003 {built-in method _pickle.loads}
              205603359  150.155    0.000  150.718    0.000 module.py:758(__getattr__)
                3007626  122.690    0.000  122.690    0.000 {built-in method torch._C._nn.mse_loss}
               12030604  115.307    0.000  115.307    0.000 {method 't' of 'torch._C._TensorBase' objects}
                  60154   26.288    0.000  109.453    0.002 {built-in method _pickle.dumps}
               12030604   33.313    0.000  108.159    0.000 rnn.py:524(check_forward_args)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 8366146: <Dist_eps_0> in cluster <dcc> Done

Job <Dist_eps_0> was submitted from host <n-62-27-22> by user <s183905> in cluster <dcc> at Mon Nov 16 20:57:20 2020
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Nov 16 20:57:22 2020
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Mon Nov 16 20:57:22 2020
Terminated at Tue Nov 17 20:52:46 2020
Results reported at Tue Nov 17 20:52:46 2020

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

    CPU time :                                   87697.00 sec.
    Max Memory :                                 25316 MB
    Average Memory :                             25019.75 MB
    Total Requested Memory :                     30720.00 MB
    Delta Memory :                               5404.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   86177 sec.
    Turnaround time :                            86126 sec.

The output (if any) is above this job summary.

