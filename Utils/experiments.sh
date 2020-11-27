#!/bin/sh
mkdir ../outputs/epsgreedybigfish/
mkdir ../outputs/epsgreedybigfish/Markdown
mkdir ../outputs/epsgreedybigfish/Agents
mkdir ../outputs/epsgreedybigfish/Collectors
bsub -o "../outputs/epsgreedybigfish/Markdown/epsgreedybigfish_0.md" -J "epsgreedybigfish_0" -P "epsgreedybigfish-0 -environment bigfish -memory 500000 -exploration epsgreedy" < submit.sh
