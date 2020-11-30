#!/bin/sh
mkdir ../outputs/Test_YES_parameters_NO_weightsfruitbot/
mkdir ../outputs/Test_YES_parameters_NO_weightsfruitbot/Markdown
mkdir ../outputs/Test_YES_parameters_NO_weightsfruitbot/Agents
mkdir ../outputs/Test_YES_parameters_NO_weightsfruitbot/Collectors
bsub -o "../outputs/Test_YES_parameters_NO_weightsfruitbot/Markdown/Test_YES_parameters_NO_weightsfruitbot_0.md" -J "Test_YES_parameters_NO_weightsfruitbot_0" -P "Test_YES_parameters_NO_weightsfruitbot-0 -environment fruitbot -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Test_NO_parameters_YES_weightsfruitbot/
mkdir ../outputs/Test_NO_parameters_YES_weightsfruitbot/Markdown
mkdir ../outputs/Test_NO_parameters_YES_weightsfruitbot/Agents
mkdir ../outputs/Test_NO_parameters_YES_weightsfruitbot/Collectors
bsub -o "../outputs/Test_NO_parameters_YES_weightsfruitbot/Markdown/Test_NO_parameters_YES_weightsfruitbot_0.md" -J "Test_NO_parameters_YES_weightsfruitbot_0" -P "Test_NO_parameters_YES_weightsfruitbot-0 -environment fruitbot -uncertainty 0 -state_difference 0 -uncertainty_weight 100 -state_difference_weight 100" < submit.sh
