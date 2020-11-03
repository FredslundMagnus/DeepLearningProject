#!/bin/sh
mkdir ../outputs/test_4/
mkdir ../outputs/test_4/Markdown
mkdir ../outputs/test_4/Agents
bsub -o "../outputs/test_4/Markdown/test_4_0.md" -J "test_4_0" -P "test_4-0 -lossf MME -discount 0.12 -lambd 0.3 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/test_4/Markdown/test_4_1.md" -J "test_4_1" -P "test_4-1 -lossf MME -discount 0.12 -lambd 0.3 -lr 0.0001 -dropout 0" < submit.sh
