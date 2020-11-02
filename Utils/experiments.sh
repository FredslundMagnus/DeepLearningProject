#!/bin/sh
mkdir ../outputs/test_2/
mkdir ../outputs/test_2/Markdown
mkdir ../outputs/test_2/Agents
bsub -o "../outputs/test_2/Markdown/test_2_0.md" -J "test_2_0" -P "test_2-0 -lossf MME -discount 0.12 -lambd 0.3 -lr 0.0001 -dropout 0" < submit.sh
