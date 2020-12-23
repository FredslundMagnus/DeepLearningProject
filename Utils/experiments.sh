#!/bin/sh
mkdir ../outputs/NOPE_final_bigfish/
mkdir ../outputs/NOPE_final_bigfish/Markdown
mkdir ../outputs/NOPE_final_bigfish/Agents
mkdir ../outputs/NOPE_final_bigfish/Collectors
bsub -o "../outputs/NOPE_final_bigfish/Markdown/NOPE_final_bigfish_0.md" -J "NOPE_final_bigfish_0" -P "NOPE_final_bigfish-0 -environment bigfish -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_fruitbot/
mkdir ../outputs/NOPE_final_fruitbot/Markdown
mkdir ../outputs/NOPE_final_fruitbot/Agents
mkdir ../outputs/NOPE_final_fruitbot/Collectors
bsub -o "../outputs/NOPE_final_fruitbot/Markdown/NOPE_final_fruitbot_0.md" -J "NOPE_final_fruitbot_0" -P "NOPE_final_fruitbot-0 -environment fruitbot -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_chaser/
mkdir ../outputs/NOPE_final_chaser/Markdown
mkdir ../outputs/NOPE_final_chaser/Agents
mkdir ../outputs/NOPE_final_chaser/Collectors
bsub -o "../outputs/NOPE_final_chaser/Markdown/NOPE_final_chaser_0.md" -J "NOPE_final_chaser_0" -P "NOPE_final_chaser-0 -environment chaser -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
