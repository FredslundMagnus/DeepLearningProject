#!/bin/sh
mkdir ../outputs/Discount_0.995_dist/
mkdir ../outputs/Discount_0.995_dist/Markdown
mkdir ../outputs/Discount_0.995_dist/Agents
mkdir ../outputs/Discount_0.995_dist/Means
bsub -o "../outputs/Discount_0.995_dist/Markdown/Discount_0.995_dist_0.md" -J "Discount_0.995_dist_0" -P "Discount_0.995_dist-0 -environment fruitbot -discount 0.995 -hours 15 -use_distribution 1" < submit.sh
mkdir ../outputs/Discount_0.995_samp/
mkdir ../outputs/Discount_0.995_samp/Markdown
mkdir ../outputs/Discount_0.995_samp/Agents
mkdir ../outputs/Discount_0.995_samp/Means
bsub -o "../outputs/Discount_0.995_samp/Markdown/Discount_0.995_samp_0.md" -J "Discount_0.995_samp_0" -P "Discount_0.995_samp-0 -environment fruitbot -discount 0.995 -hours 15 -use_distribution 0" < submit.sh
