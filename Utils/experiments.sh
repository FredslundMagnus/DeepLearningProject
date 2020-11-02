#!/bin/sh
mkdir ../outputs/test_1/
mkdir ../outputs/test_1/Markdown
mkdir ../outputs/test_1/Agents
bsub -o "../outputs/test_1/Markdown/test_1_0.md" -J "test_1_0" -P "test_1-0 -lossf MME -discount 0.12 -lambd 0.3 -lr 0.0001 -dropout 0" < submit.sh
