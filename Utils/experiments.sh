#!/bin/sh
mkdir ../outputs/Base_v2_caveflyer/
mkdir ../outputs/Base_v2_caveflyer/Markdown
mkdir ../outputs/Base_v2_caveflyer/Agents
mkdir ../outputs/Base_v2_caveflyer/Collectors
bsub -o "../outputs/Base_v2_caveflyer/Markdown/Base_v2_caveflyer_0.md" -J "Base_v2_caveflyer_0" -P "Base_v2_caveflyer-0 -environment caveflyer" < submit.sh
mkdir ../outputs/Base_v2_coinrun/
mkdir ../outputs/Base_v2_coinrun/Markdown
mkdir ../outputs/Base_v2_coinrun/Agents
mkdir ../outputs/Base_v2_coinrun/Collectors
bsub -o "../outputs/Base_v2_coinrun/Markdown/Base_v2_coinrun_0.md" -J "Base_v2_coinrun_0" -P "Base_v2_coinrun-0 -environment coinrun" < submit.sh
mkdir ../outputs/Base_v2_dodgeball/
mkdir ../outputs/Base_v2_dodgeball/Markdown
mkdir ../outputs/Base_v2_dodgeball/Agents
mkdir ../outputs/Base_v2_dodgeball/Collectors
bsub -o "../outputs/Base_v2_dodgeball/Markdown/Base_v2_dodgeball_0.md" -J "Base_v2_dodgeball_0" -P "Base_v2_dodgeball-0 -environment dodgeball" < submit.sh
mkdir ../outputs/Base_v2_heist/
mkdir ../outputs/Base_v2_heist/Markdown
mkdir ../outputs/Base_v2_heist/Agents
mkdir ../outputs/Base_v2_heist/Collectors
bsub -o "../outputs/Base_v2_heist/Markdown/Base_v2_heist_0.md" -J "Base_v2_heist_0" -P "Base_v2_heist-0 -environment heist" < submit.sh
mkdir ../outputs/Base_v2_maze/
mkdir ../outputs/Base_v2_maze/Markdown
mkdir ../outputs/Base_v2_maze/Agents
mkdir ../outputs/Base_v2_maze/Collectors
bsub -o "../outputs/Base_v2_maze/Markdown/Base_v2_maze_0.md" -J "Base_v2_maze_0" -P "Base_v2_maze-0 -environment maze" < submit.sh
mkdir ../outputs/Base_v2_miner/
mkdir ../outputs/Base_v2_miner/Markdown
mkdir ../outputs/Base_v2_miner/Agents
mkdir ../outputs/Base_v2_miner/Collectors
bsub -o "../outputs/Base_v2_miner/Markdown/Base_v2_miner_0.md" -J "Base_v2_miner_0" -P "Base_v2_miner-0 -environment miner" < submit.sh
mkdir ../outputs/Base_v2_ninja/
mkdir ../outputs/Base_v2_ninja/Markdown
mkdir ../outputs/Base_v2_ninja/Agents
mkdir ../outputs/Base_v2_ninja/Collectors
bsub -o "../outputs/Base_v2_ninja/Markdown/Base_v2_ninja_0.md" -J "Base_v2_ninja_0" -P "Base_v2_ninja-0 -environment ninja" < submit.sh
mkdir ../outputs/Base_v2_plunder/
mkdir ../outputs/Base_v2_plunder/Markdown
mkdir ../outputs/Base_v2_plunder/Agents
mkdir ../outputs/Base_v2_plunder/Collectors
bsub -o "../outputs/Base_v2_plunder/Markdown/Base_v2_plunder_0.md" -J "Base_v2_plunder_0" -P "Base_v2_plunder-0 -environment plunder" < submit.sh
