#!/bin/sh
mkdir ../outputs/CHASER_U_S_0_0chaser/
mkdir ../outputs/CHASER_U_S_0_0chaser/Markdown
mkdir ../outputs/CHASER_U_S_0_0chaser/Agents
mkdir ../outputs/CHASER_U_S_0_0chaser/Collectors
bsub -o "../outputs/CHASER_U_S_0_0chaser/Markdown/CHASER_U_S_0_0chaser_0.md" -J "CHASER_U_S_0_0chaser_0" -P "CHASER_U_S_0_0chaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/CHASER_U_S_0.1_0chaser/
mkdir ../outputs/CHASER_U_S_0.1_0chaser/Markdown
mkdir ../outputs/CHASER_U_S_0.1_0chaser/Agents
mkdir ../outputs/CHASER_U_S_0.1_0chaser/Collectors
bsub -o "../outputs/CHASER_U_S_0.1_0chaser/Markdown/CHASER_U_S_0.1_0chaser_0.md" -J "CHASER_U_S_0.1_0chaser_0" -P "CHASER_U_S_0.1_0chaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/CHASER_U_S_0_0.1chaser/
mkdir ../outputs/CHASER_U_S_0_0.1chaser/Markdown
mkdir ../outputs/CHASER_U_S_0_0.1chaser/Agents
mkdir ../outputs/CHASER_U_S_0_0.1chaser/Collectors
bsub -o "../outputs/CHASER_U_S_0_0.1chaser/Markdown/CHASER_U_S_0_0.1chaser_0.md" -J "CHASER_U_S_0_0.1chaser_0" -P "CHASER_U_S_0_0.1chaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1" < submit.sh
