#!/bin/sh
mkdir ../outputs/NOPE_final_starpilot/
mkdir ../outputs/NOPE_final_starpilot/Markdown
mkdir ../outputs/NOPE_final_starpilot/Agents
mkdir ../outputs/NOPE_final_starpilot/Collectors
bsub -o "../outputs/NOPE_final_starpilot/Markdown/NOPE_final_starpilot_0.md" -J "NOPE_final_starpilot_0" -P "NOPE_final_starpilot-0 -environment starpilot -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_bossfight/
mkdir ../outputs/NOPE_final_bossfight/Markdown
mkdir ../outputs/NOPE_final_bossfight/Agents
mkdir ../outputs/NOPE_final_bossfight/Collectors
bsub -o "../outputs/NOPE_final_bossfight/Markdown/NOPE_final_bossfight_0.md" -J "NOPE_final_bossfight_0" -P "NOPE_final_bossfight-0 -environment bossfight -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_jumper/
mkdir ../outputs/NOPE_final_jumper/Markdown
mkdir ../outputs/NOPE_final_jumper/Agents
mkdir ../outputs/NOPE_final_jumper/Collectors
bsub -o "../outputs/NOPE_final_jumper/Markdown/NOPE_final_jumper_0.md" -J "NOPE_final_jumper_0" -P "NOPE_final_jumper-0 -environment jumper -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
