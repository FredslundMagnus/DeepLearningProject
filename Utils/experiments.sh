#!/bin/sh
mkdir ../outputs/Discount_0.70/
mkdir ../outputs/Discount_0.70/Markdown
bsub -o "../outputs/Discount_0.70/Markdown/Discount_0.70_0.md" -J "Discount_0.70_0" -P "Discount_0.70-0 -lossf MME -discount 0.12 -lambd 0.3 -lr 0.0001 -dropout 0" < submit.sh
