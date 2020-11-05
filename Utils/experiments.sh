#!/bin/sh
mkdir ../outputs/bigfish_normalised/
mkdir ../outputs/bigfish_normalised/Markdown
mkdir ../outputs/bigfish_normalised/Agents
mkdir ../outputs/bigfish_normalised/Means
bsub -o "../outputs/bigfish_normalised/Markdown/bigfish_normalised_0.md" -J "bigfish_normalised_0" -P "bigfish_normalised-0 -environment bigfish" < submit.sh
mkdir ../outputs/chaser_normalised/
mkdir ../outputs/chaser_normalised/Markdown
mkdir ../outputs/chaser_normalised/Agents
mkdir ../outputs/chaser_normalised/Means
bsub -o "../outputs/chaser_normalised/Markdown/chaser_normalised_0.md" -J "chaser_normalised_0" -P "chaser_normalised-0 -environment chaser" < submit.sh
mkdir ../outputs/fruitbot_normalised/
mkdir ../outputs/fruitbot_normalised/Markdown
mkdir ../outputs/fruitbot_normalised/Agents
mkdir ../outputs/fruitbot_normalised/Means
bsub -o "../outputs/fruitbot_normalised/Markdown/fruitbot_normalised_0.md" -J "fruitbot_normalised_0" -P "fruitbot_normalised-0 -environment fruitbot" < submit.sh
