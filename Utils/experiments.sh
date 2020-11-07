#!/bin/sh
mkdir ../outputs/Discount_0.9_1/
mkdir ../outputs/Discount_0.9_1/Markdown
mkdir ../outputs/Discount_0.9_1/Agents
mkdir ../outputs/Discount_0.9_1/Means
bsub -o "../outputs/Discount_0.9_1/Markdown/Discount_0.9_1_0.md" -J "Discount_0.9_1_0" -P "Discount_0.9_1-0 -environment fruitbot -discount 0.9 -hours 20" < submit.sh
mkdir ../outputs/Discount_0.95_1/
mkdir ../outputs/Discount_0.95_1/Markdown
mkdir ../outputs/Discount_0.95_1/Agents
mkdir ../outputs/Discount_0.95_1/Means
bsub -o "../outputs/Discount_0.95_1/Markdown/Discount_0.95_1_0.md" -J "Discount_0.95_1_0" -P "Discount_0.95_1-0 -environment fruitbot -discount 0.95 -hours 20" < submit.sh
mkdir ../outputs/Discount_0.99_1/
mkdir ../outputs/Discount_0.99_1/Markdown
mkdir ../outputs/Discount_0.99_1/Agents
mkdir ../outputs/Discount_0.99_1/Means
bsub -o "../outputs/Discount_0.99_1/Markdown/Discount_0.99_1_0.md" -J "Discount_0.99_1_0" -P "Discount_0.99_1-0 -environment fruitbot -discount 0.99 -hours 20" < submit.sh
mkdir ../outputs/Discount_0.995_1/
mkdir ../outputs/Discount_0.995_1/Markdown
mkdir ../outputs/Discount_0.995_1/Agents
mkdir ../outputs/Discount_0.995_1/Means
bsub -o "../outputs/Discount_0.995_1/Markdown/Discount_0.995_1_0.md" -J "Discount_0.995_1_0" -P "Discount_0.995_1-0 -environment fruitbot -discount 0.995 -hours 20" < submit.sh
mkdir ../outputs/Discount_0.999_1/
mkdir ../outputs/Discount_0.999_1/Markdown
mkdir ../outputs/Discount_0.999_1/Agents
mkdir ../outputs/Discount_0.999_1/Means
bsub -o "../outputs/Discount_0.999_1/Markdown/Discount_0.999_1_0.md" -J "Discount_0.999_1_0" -P "Discount_0.999_1-0 -environment fruitbot -discount 0.999 -hours 20" < submit.sh
