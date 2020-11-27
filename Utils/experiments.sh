#!/bin/sh
mkdir ../outputs/softmaxbigfish/
mkdir ../outputs/softmaxbigfish/Markdown
mkdir ../outputs/softmaxbigfish/Agents
mkdir ../outputs/softmaxbigfish/Collectors
bsub -o "../outputs/softmaxbigfish/Markdown/softmaxbigfish_0.md" -J "softmaxbigfish_0" -P "softmaxbigfish-0 -environment bigfish -memory 500000 -exploration softmax" < submit.sh
