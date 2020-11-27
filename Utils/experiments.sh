#!/bin/sh
mkdir ../outputs/greedybigfish/
mkdir ../outputs/greedybigfish/Markdown
mkdir ../outputs/greedybigfish/Agents
mkdir ../outputs/greedybigfish/Collectors
bsub -o "../outputs/greedybigfish/Markdown/greedybigfish_0.md" -J "greedybigfish_0" -P "greedybigfish-0 -environment bigfish -memory 500000 -exploration greedy" < submit.sh
