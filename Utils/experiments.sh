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
mkdir ../outputs/U_S_0.1_0.1returnchaser/
mkdir ../outputs/U_S_0.1_0.1returnchaser/Markdown
mkdir ../outputs/U_S_0.1_0.1returnchaser/Agents
mkdir ../outputs/U_S_0.1_0.1returnchaser/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnchaser/Markdown/U_S_0.1_0.1returnchaser_0.md" -J "U_S_0.1_0.1returnchaser_0" -P "U_S_0.1_0.1returnchaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/U_S_0.1_0.1returndodgeball/
mkdir ../outputs/U_S_0.1_0.1returndodgeball/Markdown
mkdir ../outputs/U_S_0.1_0.1returndodgeball/Agents
mkdir ../outputs/U_S_0.1_0.1returndodgeball/Collectors
bsub -o "../outputs/U_S_0.1_0.1returndodgeball/Markdown/U_S_0.1_0.1returndodgeball_0.md" -J "U_S_0.1_0.1returndodgeball_0" -P "U_S_0.1_0.1returndodgeball-0 -environment dodgeball -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/U_S_0.1_0.1returnstarpilot/
mkdir ../outputs/U_S_0.1_0.1returnstarpilot/Markdown
mkdir ../outputs/U_S_0.1_0.1returnstarpilot/Agents
mkdir ../outputs/U_S_0.1_0.1returnstarpilot/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnstarpilot/Markdown/U_S_0.1_0.1returnstarpilot_0.md" -J "U_S_0.1_0.1returnstarpilot_0" -P "U_S_0.1_0.1returnstarpilot-0 -environment starpilot -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/U_S_0.1_0.1returnleaper/
mkdir ../outputs/U_S_0.1_0.1returnleaper/Markdown
mkdir ../outputs/U_S_0.1_0.1returnleaper/Agents
mkdir ../outputs/U_S_0.1_0.1returnleaper/Collectors
bsub -o "../outputs/U_S_0.1_0.1returnleaper/Markdown/U_S_0.1_0.1returnleaper_0.md" -J "U_S_0.1_0.1returnleaper_0" -P "U_S_0.1_0.1returnleaper-0 -environment leaper -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
