#!/bin/sh
mkdir ../outputs/U_S_0.1_0.1returnstarpilot/
mkdir ../outputs/U_S_0.1_0.1returnstarpilot/Markdown
mkdir ../outputs/U_S_0.1_0.1returnstarpilot/Agents
mkdir ../outputs/U_S_0.1_0.1returnstarpilot/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnstarpilot/Markdown/U_S_0.1_0.1returnstarpilot_0.md" -J "U_S_0.1_0.1returnstarpilot_0" -P "U_S_0.1_0.1returnstarpilot-0 -environment starpilot -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/U_S_0.1_0.1returnbossfight/
mkdir ../outputs/U_S_0.1_0.1returnbossfight/Markdown
mkdir ../outputs/U_S_0.1_0.1returnbossfight/Agents
mkdir ../outputs/U_S_0.1_0.1returnbossfight/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnbossfight/Markdown/U_S_0.1_0.1returnbossfight_0.md" -J "U_S_0.1_0.1returnbossfight_0" -P "U_S_0.1_0.1returnbossfight-0 -environment bossfight -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/U_S_0.1_0.1returndodgeball/
mkdir ../outputs/U_S_0.1_0.1returndodgeball/Markdown
mkdir ../outputs/U_S_0.1_0.1returndodgeball/Agents
mkdir ../outputs/U_S_0.1_0.1returndodgeball/Collectors
bsub -o "../outputs/U_S_0.1_0.1returndodgeball/Markdown/U_S_0.1_0.1returndodgeball_0.md" -J "U_S_0.1_0.1returndodgeball_0" -P "U_S_0.1_0.1returndodgeball-0 -environment dodgeball -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/U_S_0.1_0.1returnchaser/
mkdir ../outputs/U_S_0.1_0.1returnchaser/Markdown
mkdir ../outputs/U_S_0.1_0.1returnchaser/Agents
mkdir ../outputs/U_S_0.1_0.1returnchaser/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnchaser/Markdown/U_S_0.1_0.1returnchaser_0.md" -J "U_S_0.1_0.1returnchaser_0" -P "U_S_0.1_0.1returnchaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
