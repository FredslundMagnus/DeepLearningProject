Traceback (most recent call last):
  File "main.py", line 26, in <module>
    serverRun()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/server.py", line 28, in serverRun
    showParams(params)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 101, in showParams
    timer = Timer()
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils/debug.py", line 68, in __init__
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
  File "main.py", line 19, in main
    act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 55, in chooseMulti
    return [self.explore(val.reshape(15)) for val in torch.split(vals, 1)], pixels, hn, cn, torch.split(self.network.hn, 1, dim=1), torch.split(self.network.cn, 1, dim=1)
  File "/zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/agent.py", line 55, in <listcomp>
    return [self.explore(val.reshape(15)) for val in torch.split(vals, 1)], pixels, hn, cn, torch.split(self.network.hn, 1, dim=1), torch.split(self.network.cn, 1, dim=1)
AttributeError: 'Agent' object has no attribute 'explore'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 8447011: <epsgreedybigfish_0> in cluster <dcc> Exited

Job <epsgreedybigfish_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 13:04:36 2020
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Nov 28 05:52:48 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Sat Nov 28 05:52:48 2020
Terminated at Sat Nov 28 05:53:32 2020
Results reported at Sat Nov 28 05:53:32 2020

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

    CPU time :                                   7.00 sec.
    Max Memory :                                 77 MB
    Average Memory :                             77.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               61363.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   44 sec.
    Turnaround time :                            60536 sec.

The output (if any) is above this job summary.


    Name :                      epsgreedybigfish-0
    Discount :                  0.995
    Environment :               bigfish
    Hours :                     23
    Memory :                    500000
    Update every :              500
    Use distribution :          1
    Double :                    1
    Total agents :              20
    Calculate every :           500
    Uncertainty :               0
    Reward normalization :      0
    Exploration :               greedy
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      12191068634 function calls (11948925299 primitive calls) in 82535.35 seconds

##    Ordered by: cumulative time
   List reduced from 1342 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                   80/1    0.000    0.000 82535.349 82535.349 {built-in method builtins.exec}
                      1    0.061    0.061 82535.349 82535.349 <string>:1(<module>)
                      1  434.128  434.128 82535.287 82535.287 main.py:11(main)
                2522636  107.011    0.000 52239.425    0.021 agent.py:57(learn)
                2522136  396.706    0.000 51361.924    0.020 agent.py:67(TD_learn)
                2522136  169.728    0.000 27880.047    0.011 memory.py:35(sample_distribution)
                2522136  292.530    0.000 27030.816    0.011 helpers.py:12(stack)
        254748236/12611180 1089.559    0.000 16340.684    0.001 module.py:715(_call_impl)
               10089044  273.759    0.000 16064.752    0.002 agent.py:147(forward)
              353169040 14053.432    0.000 14053.432    0.000 {method 'cpu' of 'torch._C._TensorBase' objects}
                2522636   40.395    0.000 13488.434    0.005 agent.py:51(chooseMulti)
               22700790 13405.759    0.001 13405.791    0.001 {method 'to' of 'torch._C._TensorBase' objects}
               22700724 12845.487    0.001 12845.487    0.001 {built-in method cat}
               40356176  285.850    0.000 9745.291    0.000 container.py:115(forward)
                2522636   72.496    0.000 9412.130    0.004 environments.py:73(step)
                2522636   90.081    0.000 8736.110    0.003 agent.py:55(<listcomp>)
               50452720  117.923    0.000 8413.070    0.000 exploration.py:27(greedy)
                2522636    7.681    0.000 6732.866    0.003 agent.py:42(rememberMulti)
                2522636  268.234    0.000 6725.185    0.003 agent.py:43(<listcomp>)
                2522636   59.133    0.000 6226.354    0.002 environments.py:75(<listcomp>)
               50487617 1633.390    0.000 6172.345    0.000 helpers.py:8(clean)
               58054025 5186.818    0.000 5186.818    0.000 {built-in method as_tensor}
                2522136   21.244    0.000 4925.980    0.002 grad_mode.py:23(decorate_context)
               60534264  110.460    0.000 4907.350    0.000 conv.py:422(forward)
                2522136  176.370    0.000 4874.529    0.002 adam.py:55(step)
               60534264  117.239    0.000 4751.865    0.000 conv.py:414(_conv_forward)
               60534264 4613.328    0.000 4613.328    0.000 {built-in method conv2d}
                2522136   22.807    0.000 4096.864    0.002 tensor.py:181(backward)
                2522136   15.021    0.000 4074.057    0.002 __init__.py:68(backward)
                2522136 3987.831    0.002 3987.831    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2522136  894.699    0.000 3964.325    0.002 functional.py:53(adam)
                2522636   55.483    0.000 2947.808    0.001 environments.py:74(<listcomp>)
               50452720  198.224    0.000 2892.324    0.000 interop.py:274(step)
               10089050  514.584    0.000 2816.180    0.000 rnn.py:110(flatten_parameters)
               10089044  106.785    0.000 2396.416    0.000 rnn.py:555(forward)
               10089044 2161.367    0.000 2161.367    0.000 {built-in method lstm}
               10089047 1719.550    0.000 1719.550    0.000 {built-in method _cudnn_rnn_flatten_weight}
               30267132   69.770    0.000 1630.930    0.000 linear.py:92(forward)
               90801396   88.459    0.000 1545.568    0.000 activation.py:713(forward)
               30267132  125.300    0.000 1530.235    0.000 functional.py:1669(linear)
               90801396  127.553    0.000 1457.109    0.000 functional.py:1292(leaky_relu)
               90801396 1315.693    0.000 1315.693    0.000 {built-in method torch._C._nn.leaky_relu}
              337966290  780.252    0.000 1313.705    0.000 tensor.py:933(grad)
               50452720   25.935    0.000 1278.557    0.000 wrapper.py:25(act)
               50452720   69.845    0.000 1252.623    0.000 env.py:197(act)
               50452720 1141.225    0.000 1146.201    0.000 libenv.py:352(act)
                2522136  103.129    0.000 1104.000    0.000 optimizer.py:167(zero_grad)
               30267132 1016.778    0.000 1016.778    0.000 {built-in method addmm}
              100940337   77.613    0.000  857.355    0.000 extract_dict_ob.py:9(observe)
               90796896  797.892    0.000  797.892    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              100940337   44.256    0.000  779.742    0.000 wrapper.py:19(observe)
                   5045    1.328    0.000  770.490    0.153 agent.py:101(update_target_network)
              100940337  200.316    0.000  735.486    0.000 libenv.py:344(observe)
                   5045  187.156    0.037  694.445    0.138 memory.py:45(update_distribution)
               90796896  677.915    0.000  677.915    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              413632044  225.330    0.000  659.575    0.000 overrides.py:1073(has_torch_function)
               52984946  591.960    0.000  591.960    0.000 {built-in method numpy.array}
              151393057  170.214    0.000  528.417    0.000 libenv.py:281(_maybe_copy_dict)
               40357345  433.905    0.000  462.091    0.000 module.py:781(__setattr__)
              454184216  451.415    0.000  451.415    0.000 {method 'copy' of 'numpy.ndarray' objects}
               45398448  435.748    0.000  435.748    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               45398448  415.265    0.000  415.265    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              448943472  163.587    0.000  412.791    0.000 {built-in method builtins.any}
               50452720   43.659    0.000  397.642    0.000 wrapper.py:22(get_info)
               45398448  385.401    0.000  385.401    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                7567908   12.614    0.000  384.976    0.000 functional.py:74(split)
              375799010  374.264    0.000  374.264    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7567908   32.275    0.000  371.258    0.000 tensor.py:460(split)
                2522136  281.879    0.000  370.279    0.000 {method 'choice' of 'numpy.random._generator.Generator' objects}
               50452720  182.791    0.000  353.983    0.000 libenv.py:363(get_info)
               50452720  349.367    0.000  349.367    0.000 memory.py:17(inner)
               45398448  340.398    0.000  340.398    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7567908  337.286    0.000  337.286    0.000 {function Tensor.split at 0x7fe19139aca0}
               10089044   24.493    0.000  322.058    0.000 pooling.py:152(forward)
               10089044   16.874    0.000  297.565    0.000 _jit_internal.py:257(fn)
               10089044   17.064    0.000  278.946    0.000 functional.py:574(_max_pool2d)
               10089044  260.340    0.000  260.340    0.000 {built-in method max_pool2d}
              857531220  195.554    0.000  246.786    0.000 overrides.py:1086(<genexpr>)
               45398448  241.952    0.000  241.952    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               30267132  237.857    0.000  237.857    0.000 {method 't' of 'torch._C._TensorBase' objects}
               50452720  232.959    0.000  232.959    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               10089044  227.628    0.000  227.628    0.000 {method 'clone' of 'torch._C._TensorBase' objects}
               40356188  193.003    0.000  218.114    0.000 __init__.py:67(is_acceptable)
                2522136  208.765    0.000  208.765    0.000 memory.py:43(<listcomp>)
                2522636   16.996    0.000  187.694    0.000 collector.py:7(collect)
              242389718  176.281    0.000  176.434    0.000 module.py:765(__getattr__)
                2522136    6.580    0.000  169.609    0.000 loss.py:445(forward)
                5045273  169.363    0.000  169.363    0.000 {built-in method builtins.sum}
                2522636   29.628    0.000  165.472    0.000 environments.py:76(<listcomp>)
                2522136   21.030    0.000  163.029    0.000 functional.py:2637(mse_loss)
               25222360  162.671    0.000  162.671    0.000 {method 'view' of 'torch._C._TensorBase' objects}
              201880674   56.014    0.000  160.967    0.000 libenv.py:271(_maybe_copy_ndarray)
              254748236  150.335    0.000  150.335    0.000 {built-in method torch._C._get_tracing_state}
               50452740   35.483    0.000  135.906    0.000 environments.py:79(reset)
               45398622   58.838    0.000  131.075    0.000 tensor.py:596(__hash__)
                5044272  127.137    0.000  127.137    0.000 {built-in method gather}
             1059349120  105.308    0.000  105.308    0.000 {method 'values' of 'collections.OrderedDict' objects}
                2522136   95.089    0.000   95.089    0.000 {built-in method torch._C._nn.mse_loss}
               10089047   29.923    0.000   84.510    0.000 __init__.py:246(__init__)
               10089044   26.795    0.000   84.478    0.000 rnn.py:529(check_forward_args)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 8447008: <epsgreedybigfish_0> in cluster <dcc> Done

Job <epsgreedybigfish_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Nov 27 12:58:30 2020
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Nov 27 14:32:49 2020
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/DeepAI/DeepLearningProject/Utils> was used as the working directory.
Started at Fri Nov 27 14:32:49 2020
Terminated at Sat Nov 28 13:28:40 2020
Results reported at Sat Nov 28 13:28:40 2020

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

    CPU time :                                   87359.00 sec.
    Max Memory :                                 56989 MB
    Average Memory :                             56233.36 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               4451.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                9
    Run time :                                   82550 sec.
    Turnaround time :                            88210 sec.

The output (if any) is above this job summary.

