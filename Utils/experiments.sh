#!/bin/sh
mkdir ../outputs/UUncertainty+Avoid_State0and0fruitbot/
mkdir ../outputs/UUncertainty+Avoid_State0and0fruitbot/Markdown
mkdir ../outputs/UUncertainty+Avoid_State0and0fruitbot/Agents
mkdir ../outputs/UUncertainty+Avoid_State0and0fruitbot/Collectors
bsub -o "../outputs/UUncertainty+Avoid_State0and0fruitbot/Markdown/UUncertainty+Avoid_State0and0fruitbot_0.md" -J "UUncertainty+Avoid_State0and0fruitbot_0" -P "UUncertainty+Avoid_State0and0fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/UUncertainty+Avoid_State0and-1fruitbot/
mkdir ../outputs/UUncertainty+Avoid_State0and-1fruitbot/Markdown
mkdir ../outputs/UUncertainty+Avoid_State0and-1fruitbot/Agents
mkdir ../outputs/UUncertainty+Avoid_State0and-1fruitbot/Collectors
bsub -o "../outputs/UUncertainty+Avoid_State0and-1fruitbot/Markdown/UUncertainty+Avoid_State0and-1fruitbot_0.md" -J "UUncertainty+Avoid_State0and-1fruitbot_0" -P "UUncertainty+Avoid_State0and-1fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 0 -state_difference_weight -1" < submit.sh
mkdir ../outputs/UUncertainty+Avoid_State0and1fruitbot/
mkdir ../outputs/UUncertainty+Avoid_State0and1fruitbot/Markdown
mkdir ../outputs/UUncertainty+Avoid_State0and1fruitbot/Agents
mkdir ../outputs/UUncertainty+Avoid_State0and1fruitbot/Collectors
bsub -o "../outputs/UUncertainty+Avoid_State0and1fruitbot/Markdown/UUncertainty+Avoid_State0and1fruitbot_0.md" -J "UUncertainty+Avoid_State0and1fruitbot_0" -P "UUncertainty+Avoid_State0and1fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 0 -state_difference_weight 1" < submit.sh
mkdir ../outputs/UUncertainty+Avoid_State-1and0fruitbot/
mkdir ../outputs/UUncertainty+Avoid_State-1and0fruitbot/Markdown
mkdir ../outputs/UUncertainty+Avoid_State-1and0fruitbot/Agents
mkdir ../outputs/UUncertainty+Avoid_State-1and0fruitbot/Collectors
bsub -o "../outputs/UUncertainty+Avoid_State-1and0fruitbot/Markdown/UUncertainty+Avoid_State-1and0fruitbot_0.md" -J "UUncertainty+Avoid_State-1and0fruitbot_0" -P "UUncertainty+Avoid_State-1and0fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight -1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/UUncertainty+Avoid_State1and0fruitbot/
mkdir ../outputs/UUncertainty+Avoid_State1and0fruitbot/Markdown
mkdir ../outputs/UUncertainty+Avoid_State1and0fruitbot/Agents
mkdir ../outputs/UUncertainty+Avoid_State1and0fruitbot/Collectors
bsub -o "../outputs/UUncertainty+Avoid_State1and0fruitbot/Markdown/UUncertainty+Avoid_State1and0fruitbot_0.md" -J "UUncertainty+Avoid_State1and0fruitbot_0" -P "UUncertainty+Avoid_State1and0fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/UUncertainty+Avoid_State0and10fruitbot/
mkdir ../outputs/UUncertainty+Avoid_State0and10fruitbot/Markdown
mkdir ../outputs/UUncertainty+Avoid_State0and10fruitbot/Agents
mkdir ../outputs/UUncertainty+Avoid_State0and10fruitbot/Collectors
bsub -o "../outputs/UUncertainty+Avoid_State0and10fruitbot/Markdown/UUncertainty+Avoid_State0and10fruitbot_0.md" -J "UUncertainty+Avoid_State0and10fruitbot_0" -P "UUncertainty+Avoid_State0and10fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 0 -state_difference_weight 10" < submit.sh
