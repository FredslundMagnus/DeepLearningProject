#!/bin/sh
mkdir ../outputs/U_S_0.1_0.1returnmaze/
mkdir ../outputs/U_S_0.1_0.1returnmaze/Markdown
mkdir ../outputs/U_S_0.1_0.1returnmaze/Agents
mkdir ../outputs/U_S_0.1_0.1returnmaze/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnmaze/Markdown/U_S_0.1_0.1returnmaze_0.md" -J "U_S_0.1_0.1returnmaze_0" -P "U_S_0.1_0.1returnmaze-0 -environment maze -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/U_S_0.1_0.1returnbigfish/
mkdir ../outputs/U_S_0.1_0.1returnbigfish/Markdown
mkdir ../outputs/U_S_0.1_0.1returnbigfish/Agents
mkdir ../outputs/U_S_0.1_0.1returnbigfish/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnbigfish/Markdown/U_S_0.1_0.1returnbigfish_0.md" -J "U_S_0.1_0.1returnbigfish_0" -P "U_S_0.1_0.1returnbigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/U_S_0.1_0.1returnfruitbot/
mkdir ../outputs/U_S_0.1_0.1returnfruitbot/Markdown
mkdir ../outputs/U_S_0.1_0.1returnfruitbot/Agents
mkdir ../outputs/U_S_0.1_0.1returnfruitbot/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnfruitbot/Markdown/U_S_0.1_0.1returnfruitbot_0.md" -J "U_S_0.1_0.1returnfruitbot_0" -P "U_S_0.1_0.1returnfruitbot-0 -environment fruitbot -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
