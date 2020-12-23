#!/bin/sh
mkdir ../outputs/NOPEfruitbot/
mkdir ../outputs/NOPEfruitbot/Markdown
mkdir ../outputs/NOPEfruitbot/Agents
mkdir ../outputs/NOPEfruitbot/Collectors
bsub -o "../outputs/NOPEfruitbot/Markdown/NOPEfruitbot_0.md" -J "NOPEfruitbot_0" -P "NOPEfruitbot-0 -environment fruitbot -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/NOPEmaze/
mkdir ../outputs/NOPEmaze/Markdown
mkdir ../outputs/NOPEmaze/Agents
mkdir ../outputs/NOPEmaze/Collectors
bsub -o "../outputs/NOPEmaze/Markdown/NOPEmaze_0.md" -J "NOPEmaze_0" -P "NOPEmaze-0 -environment maze -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/NOPEchaser/
mkdir ../outputs/NOPEchaser/Markdown
mkdir ../outputs/NOPEchaser/Agents
mkdir ../outputs/NOPEchaser/Collectors
bsub -o "../outputs/NOPEchaser/Markdown/NOPEchaser_0.md" -J "NOPEchaser_0" -P "NOPEchaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
