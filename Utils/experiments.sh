#!/bin/sh
mkdir ../outputs/MAZE_U_S_0.1_0returnmaze/
mkdir ../outputs/MAZE_U_S_0.1_0returnmaze/Markdown
mkdir ../outputs/MAZE_U_S_0.1_0returnmaze/Agents
mkdir ../outputs/MAZE_U_S_0.1_0returnmaze/Collectors
bsub -o "../outputs/MAZE_U_S_0.1_0returnmaze/Markdown/MAZE_U_S_0.1_0returnmaze_0.md" -J "MAZE_U_S_0.1_0returnmaze_0" -P "MAZE_U_S_0.1_0returnmaze-0 -environment maze -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/MAZE_U_S_0_0.1returnmaze/
mkdir ../outputs/MAZE_U_S_0_0.1returnmaze/Markdown
mkdir ../outputs/MAZE_U_S_0_0.1returnmaze/Agents
mkdir ../outputs/MAZE_U_S_0_0.1returnmaze/Collectors
bsub -o "../outputs/MAZE_U_S_0_0.1returnmaze/Markdown/MAZE_U_S_0_0.1returnmaze_0.md" -J "MAZE_U_S_0_0.1returnmaze_0" -P "MAZE_U_S_0_0.1returnmaze-0 -environment maze -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/MAZE_U_S_0_0returnmaze/
mkdir ../outputs/MAZE_U_S_0_0returnmaze/Markdown
mkdir ../outputs/MAZE_U_S_0_0returnmaze/Agents
mkdir ../outputs/MAZE_U_S_0_0returnmaze/Collectors
bsub -o "../outputs/MAZE_U_S_0_0returnmaze/Markdown/MAZE_U_S_0_0returnmaze_0.md" -J "MAZE_U_S_0_0returnmaze_0" -P "MAZE_U_S_0_0returnmaze-0 -environment maze -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
