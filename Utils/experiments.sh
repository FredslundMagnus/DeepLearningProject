#!/bin/sh
mkdir ../outputs/test_3/
mkdir ../outputs/test_3/Markdown
mkdir ../outputs/test_3/Agents
bsub -o "../outputs/test_2/Markdown/test_3_0.md" -J "test_3_0" -P "test_3-0 -lossf MME -discount 0.12 -lambd 0.3 -lr 0.0001 -dropout 0" < submit.sh
