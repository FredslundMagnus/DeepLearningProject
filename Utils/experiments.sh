#!/bin/sh
mkdir ../outputs/Dist/
mkdir ../outputs/Dist/Markdown
mkdir ../outputs/Dist/Agents
mkdir ../outputs/Dist/Collectors
bsub -o "../outputs/Dist/Markdown/Dist_0.md" -J "Dist_0" -P "Dist-0 -environment fruitbot -use_distribution 1" < submit.sh
mkdir ../outputs/NoDist/
mkdir ../outputs/NoDist/Markdown
mkdir ../outputs/NoDist/Agents
mkdir ../outputs/NoDist/Collectors
bsub -o "../outputs/NoDist/Markdown/NoDist_0.md" -J "NoDist_0" -P "NoDist-0 -environment fruitbot -use_distribution 0" < submit.sh
mkdir ../outputs/Dist_LowMem/
mkdir ../outputs/Dist_LowMem/Markdown
mkdir ../outputs/Dist_LowMem/Agents
mkdir ../outputs/Dist_LowMem/Collectors
bsub -o "../outputs/Dist_LowMem/Markdown/Dist_LowMem_0.md" -J "Dist_LowMem_0" -P "Dist_LowMem-0 -environment fruitbot -use_distribution 1 -memory 50000" < submit.sh
mkdir ../outputs/NoDist_LowMem/
mkdir ../outputs/NoDist_LowMem/Markdown
mkdir ../outputs/NoDist_LowMem/Agents
mkdir ../outputs/NoDist_LowMem/Collectors
bsub -o "../outputs/NoDist_LowMem/Markdown/NoDist_LowMem_0.md" -J "NoDist_LowMem_0" -P "NoDist_LowMem-0 -environment fruitbot -use_distribution 0 -memory 50000" < submit.sh
