#!/bin/sh
mkdir ../outputs/NOPE_final_leaper/
mkdir ../outputs/NOPE_final_leaper/Markdown
mkdir ../outputs/NOPE_final_leaper/Agents
mkdir ../outputs/NOPE_final_leaper/Collectors
bsub -o "../outputs/NOPE_final_leaper/Markdown/NOPE_final_leaper_0.md" -J "NOPE_final_leaper_0" -P "NOPE_final_leaper-0 -environment leaper -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_maze/
mkdir ../outputs/NOPE_final_maze/Markdown
mkdir ../outputs/NOPE_final_maze/Agents
mkdir ../outputs/NOPE_final_maze/Collectors
bsub -o "../outputs/NOPE_final_maze/Markdown/NOPE_final_maze_0.md" -J "NOPE_final_maze_0" -P "NOPE_final_maze-0 -environment maze -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_miner/
mkdir ../outputs/NOPE_final_miner/Markdown
mkdir ../outputs/NOPE_final_miner/Agents
mkdir ../outputs/NOPE_final_miner/Collectors
bsub -o "../outputs/NOPE_final_miner/Markdown/NOPE_final_miner_0.md" -J "NOPE_final_miner_0" -P "NOPE_final_miner-0 -environment miner -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_ninja/
mkdir ../outputs/NOPE_final_ninja/Markdown
mkdir ../outputs/NOPE_final_ninja/Agents
mkdir ../outputs/NOPE_final_ninja/Collectors
bsub -o "../outputs/NOPE_final_ninja/Markdown/NOPE_final_ninja_0.md" -J "NOPE_final_ninja_0" -P "NOPE_final_ninja-0 -environment ninja -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_plunder/
mkdir ../outputs/NOPE_final_plunder/Markdown
mkdir ../outputs/NOPE_final_plunder/Agents
mkdir ../outputs/NOPE_final_plunder/Collectors
bsub -o "../outputs/NOPE_final_plunder/Markdown/NOPE_final_plunder_0.md" -J "NOPE_final_plunder_0" -P "NOPE_final_plunder-0 -environment plunder -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
