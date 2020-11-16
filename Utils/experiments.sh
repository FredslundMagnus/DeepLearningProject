#!/bin/sh
mkdir ../outputs/Dist_eps/
mkdir ../outputs/Dist_eps/Markdown
mkdir ../outputs/Dist_eps/Agents
mkdir ../outputs/Dist_eps/Collectors
bsub -o "../outputs/Dist_eps/Markdown/Dist_eps_0.md" -J "Dist_eps_0" -P "Dist_eps-0 -environment fruitbot -use_distribution 1" < submit.sh
mkdir ../outputs/NoDist_eps/
mkdir ../outputs/NoDist_eps/Markdown
mkdir ../outputs/NoDist_eps/Agents
mkdir ../outputs/NoDist_eps/Collectors
bsub -o "../outputs/NoDist_eps/Markdown/NoDist_eps_0.md" -J "NoDist_eps_0" -P "NoDist_eps-0 -environment fruitbot -use_distribution 0" < submit.sh
mkdir ../outputs/Dist_LowMem_eps/
mkdir ../outputs/Dist_LowMem_eps/Markdown
mkdir ../outputs/Dist_LowMem_eps/Agents
mkdir ../outputs/Dist_LowMem_eps/Collectors
bsub -o "../outputs/Dist_LowMem_eps/Markdown/Dist_LowMem_eps_0.md" -J "Dist_LowMem_eps_0" -P "Dist_LowMem_eps-0 -environment fruitbot -use_distribution 1 -memory 50000" < submit.sh
mkdir ../outputs/NoDist_LowMem_eps/
mkdir ../outputs/NoDist_LowMem_eps/Markdown
mkdir ../outputs/NoDist_LowMem_eps/Agents
mkdir ../outputs/NoDist_LowMem_eps/Collectors
bsub -o "../outputs/NoDist_LowMem_eps/Markdown/NoDist_LowMem_eps_0.md" -J "NoDist_LowMem_eps_0" -P "NoDist_LowMem_eps-0 -environment fruitbot -use_distribution 0 -memory 50000" < submit.sh
