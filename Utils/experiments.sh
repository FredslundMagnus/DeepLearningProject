#!/bin/sh
mkdir ../outputs/Test_1/
mkdir ../outputs/Test_1/Markdown
mkdir ../outputs/Test_1/Agents
mkdir ../outputs/Test_1/Collectors
bsub -o "../outputs/Test_1/Markdown/Test_1_0.md" -J "Test_1_0" -P "Test_1-0 -environment fruitbot -discount 0.995 -hours 1 -use_distribution 0" < submit.sh
