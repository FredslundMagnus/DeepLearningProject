#!/bin/sh
mkdir ../outputs/greedyintosoftmaxbigfish/
mkdir ../outputs/greedyintosoftmaxbigfish/Markdown
mkdir ../outputs/greedyintosoftmaxbigfish/Agents
mkdir ../outputs/greedyintosoftmaxbigfish/Collectors
bsub -o "../outputs/greedyintosoftmaxbigfish/Markdown/greedyintosoftmaxbigfish_0.md" -J "greedyintosoftmaxbigfish_0" -P "greedyintosoftmaxbigfish-0 -environment bigfish -memory 500000 -exploration greedyintosoftmax" < submit.sh
