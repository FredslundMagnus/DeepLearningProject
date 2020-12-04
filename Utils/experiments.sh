#!/bin/sh
mkdir ../outputs/EpsSoftmax_state_transition0.1maze/
mkdir ../outputs/EpsSoftmax_state_transition0.1maze/Markdown
mkdir ../outputs/EpsSoftmax_state_transition0.1maze/Agents
mkdir ../outputs/EpsSoftmax_state_transition0.1maze/Collectors
bsub -o "../outputs/EpsSoftmax_state_transition0.1maze/Markdown/EpsSoftmax_state_transition0.1maze_0.md" -J "EpsSoftmax_state_transition0.1maze_0" -P "EpsSoftmax_state_transition0.1maze-0 -environment maze -uncertainty 0 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1 -exploration epsintosoftmax" < submit.sh
mkdir ../outputs/EpsSoftmax_state_transition0.25maze/
mkdir ../outputs/EpsSoftmax_state_transition0.25maze/Markdown
mkdir ../outputs/EpsSoftmax_state_transition0.25maze/Agents
mkdir ../outputs/EpsSoftmax_state_transition0.25maze/Collectors
bsub -o "../outputs/EpsSoftmax_state_transition0.25maze/Markdown/EpsSoftmax_state_transition0.25maze_0.md" -J "EpsSoftmax_state_transition0.25maze_0" -P "EpsSoftmax_state_transition0.25maze-0 -environment maze -uncertainty 0 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.25 -exploration epsintosoftmax" < submit.sh
mkdir ../outputs/Eps_state_transition0.1maze/
mkdir ../outputs/Eps_state_transition0.1maze/Markdown
mkdir ../outputs/Eps_state_transition0.1maze/Agents
mkdir ../outputs/Eps_state_transition0.1maze/Collectors
bsub -o "../outputs/Eps_state_transition0.1maze/Markdown/Eps_state_transition0.1maze_0.md" -J "Eps_state_transition0.1maze_0" -P "Eps_state_transition0.1maze-0 -environment maze -uncertainty 0 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/Eps_state_transition0.25maze/
mkdir ../outputs/Eps_state_transition0.25maze/Markdown
mkdir ../outputs/Eps_state_transition0.25maze/Agents
mkdir ../outputs/Eps_state_transition0.25maze/Collectors
bsub -o "../outputs/Eps_state_transition0.25maze/Markdown/Eps_state_transition0.25maze_0.md" -J "Eps_state_transition0.25maze_0" -P "Eps_state_transition0.25maze-0 -environment maze -uncertainty 0 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.25" < submit.sh
