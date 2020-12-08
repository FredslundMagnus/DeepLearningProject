#!/bin/sh
mkdir ../outputs/BIGFISH_U_S_0_0bigfish/
mkdir ../outputs/BIGFISH_U_S_0_0bigfish/Markdown
mkdir ../outputs/BIGFISH_U_S_0_0bigfish/Agents
mkdir ../outputs/BIGFISH_U_S_0_0bigfish/Collectors
bsub -o "../outputs/BIGFISH_U_S_0_0bigfish/Markdown/BIGFISH_U_S_0_0bigfish_0.md" -J "BIGFISH_U_S_0_0bigfish_0" -P "BIGFISH_U_S_0_0bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/BIGFISH_U_S_0.1_0bigfish/
mkdir ../outputs/BIGFISH_U_S_0.1_0bigfish/Markdown
mkdir ../outputs/BIGFISH_U_S_0.1_0bigfish/Agents
mkdir ../outputs/BIGFISH_U_S_0.1_0bigfish/Collectors
bsub -o "../outputs/BIGFISH_U_S_0.1_0bigfish/Markdown/BIGFISH_U_S_0.1_0bigfish_0.md" -J "BIGFISH_U_S_0.1_0bigfish_0" -P "BIGFISH_U_S_0.1_0bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/BIGFISH_U_S_0_0.1bigfish/
mkdir ../outputs/BIGFISH_U_S_0_0.1bigfish/Markdown
mkdir ../outputs/BIGFISH_U_S_0_0.1bigfish/Agents
mkdir ../outputs/BIGFISH_U_S_0_0.1bigfish/Collectors
bsub -o "../outputs/BIGFISH_U_S_0_0.1bigfish/Markdown/BIGFISH_U_S_0_0.1bigfish_0.md" -J "BIGFISH_U_S_0_0.1bigfish_0" -P "BIGFISH_U_S_0_0.1bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1" < submit.sh
