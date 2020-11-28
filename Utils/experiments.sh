#!/bin/sh
mkdir ../outputs/Uncertainty+Avoid_State(0,0)fruitbot/
mkdir ../outputs/Uncertainty+Avoid_State(0,0)fruitbot/Markdown
mkdir ../outputs/Uncertainty+Avoid_State(0,0)fruitbot/Agents
mkdir ../outputs/Uncertainty+Avoid_State(0,0)fruitbot/Collectors
bsub -o "../outputs/Uncertainty+Avoid_State(0,0)fruitbot/Markdown/Uncertainty+Avoid_State(0,0)fruitbot_0.md" -J "Uncertainty+Avoid_State(0,0)fruitbot_0" -P "Uncertainty+Avoid_State(0,0)fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Uncertainty+Avoid_State(0,-1)fruitbot/
mkdir ../outputs/Uncertainty+Avoid_State(0,-1)fruitbot/Markdown
mkdir ../outputs/Uncertainty+Avoid_State(0,-1)fruitbot/Agents
mkdir ../outputs/Uncertainty+Avoid_State(0,-1)fruitbot/Collectors
bsub -o "../outputs/Uncertainty+Avoid_State(0,-1)fruitbot/Markdown/Uncertainty+Avoid_State(0,-1)fruitbot_0.md" -J "Uncertainty+Avoid_State(0,-1)fruitbot_0" -P "Uncertainty+Avoid_State(0,-1)fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 0 -state_difference_weight -1" < submit.sh
mkdir ../outputs/Uncertainty+Avoid_State(0,1)fruitbot/
mkdir ../outputs/Uncertainty+Avoid_State(0,1)fruitbot/Markdown
mkdir ../outputs/Uncertainty+Avoid_State(0,1)fruitbot/Agents
mkdir ../outputs/Uncertainty+Avoid_State(0,1)fruitbot/Collectors
bsub -o "../outputs/Uncertainty+Avoid_State(0,1)fruitbot/Markdown/Uncertainty+Avoid_State(0,1)fruitbot_0.md" -J "Uncertainty+Avoid_State(0,1)fruitbot_0" -P "Uncertainty+Avoid_State(0,1)fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 0 -state_difference_weight 1" < submit.sh
mkdir ../outputs/Uncertainty+Avoid_State(-1,0)fruitbot/
mkdir ../outputs/Uncertainty+Avoid_State(-1,0)fruitbot/Markdown
mkdir ../outputs/Uncertainty+Avoid_State(-1,0)fruitbot/Agents
mkdir ../outputs/Uncertainty+Avoid_State(-1,0)fruitbot/Collectors
bsub -o "../outputs/Uncertainty+Avoid_State(-1,0)fruitbot/Markdown/Uncertainty+Avoid_State(-1,0)fruitbot_0.md" -J "Uncertainty+Avoid_State(-1,0)fruitbot_0" -P "Uncertainty+Avoid_State(-1,0)fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight -1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Uncertainty+Avoid_State(1,0)fruitbot/
mkdir ../outputs/Uncertainty+Avoid_State(1,0)fruitbot/Markdown
mkdir ../outputs/Uncertainty+Avoid_State(1,0)fruitbot/Agents
mkdir ../outputs/Uncertainty+Avoid_State(1,0)fruitbot/Collectors
bsub -o "../outputs/Uncertainty+Avoid_State(1,0)fruitbot/Markdown/Uncertainty+Avoid_State(1,0)fruitbot_0.md" -J "Uncertainty+Avoid_State(1,0)fruitbot_0" -P "Uncertainty+Avoid_State(1,0)fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Uncertainty+Avoid_State(0,10)fruitbot/
mkdir ../outputs/Uncertainty+Avoid_State(0,10)fruitbot/Markdown
mkdir ../outputs/Uncertainty+Avoid_State(0,10)fruitbot/Agents
mkdir ../outputs/Uncertainty+Avoid_State(0,10)fruitbot/Collectors
bsub -o "../outputs/Uncertainty+Avoid_State(0,10)fruitbot/Markdown/Uncertainty+Avoid_State(0,10)fruitbot_0.md" -J "Uncertainty+Avoid_State(0,10)fruitbot_0" -P "Uncertainty+Avoid_State(0,10)fruitbot-0 -environment fruitbot -uncertainty True -state_difference True -uncertainty_weight 1 -state_difference_weight 10" < submit.sh
