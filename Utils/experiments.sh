#!/bin/sh
mkdir ../outputs/Uncertainty=0.5bigfish/
mkdir ../outputs/Uncertainty=0.5bigfish/Markdown
mkdir ../outputs/Uncertainty=0.5bigfish/Agents
mkdir ../outputs/Uncertainty=0.5bigfish/Collectors
bsub -o "../outputs/Uncertainty=0.5bigfish/Markdown/Uncertainty=0.5bigfish_0.md" -J "Uncertainty=0.5bigfish_0" -P "Uncertainty=0.5bigfish-0 -environment bigfish -uncertainty 1 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/NoUncertaintybigfish/
mkdir ../outputs/NoUncertaintybigfish/Markdown
mkdir ../outputs/NoUncertaintybigfish/Agents
mkdir ../outputs/NoUncertaintybigfish/Collectors
bsub -o "../outputs/NoUncertaintybigfish/Markdown/NoUncertaintybigfish_0.md" -J "NoUncertaintybigfish_0" -P "NoUncertaintybigfish-0 -environment bigfish -uncertainty 0 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/Uncertainty=0.5chaser/
mkdir ../outputs/Uncertainty=0.5chaser/Markdown
mkdir ../outputs/Uncertainty=0.5chaser/Agents
mkdir ../outputs/Uncertainty=0.5chaser/Collectors
bsub -o "../outputs/Uncertainty=0.5chaser/Markdown/Uncertainty=0.5chaser_0.md" -J "Uncertainty=0.5chaser_0" -P "Uncertainty=0.5chaser-0 -environment chaser -uncertainty 1 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/NoUncertaintychaser/
mkdir ../outputs/NoUncertaintychaser/Markdown
mkdir ../outputs/NoUncertaintychaser/Agents
mkdir ../outputs/NoUncertaintychaser/Collectors
bsub -o "../outputs/NoUncertaintychaser/Markdown/NoUncertaintychaser_0.md" -J "NoUncertaintychaser_0" -P "NoUncertaintychaser-0 -environment chaser -uncertainty 0 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/Uncertainty=0.5starpilot/
mkdir ../outputs/Uncertainty=0.5starpilot/Markdown
mkdir ../outputs/Uncertainty=0.5starpilot/Agents
mkdir ../outputs/Uncertainty=0.5starpilot/Collectors
bsub -o "../outputs/Uncertainty=0.5starpilot/Markdown/Uncertainty=0.5starpilot_0.md" -J "Uncertainty=0.5starpilot_0" -P "Uncertainty=0.5starpilot-0 -environment starpilot -uncertainty 1 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/NoUncertaintystarpilot/
mkdir ../outputs/NoUncertaintystarpilot/Markdown
mkdir ../outputs/NoUncertaintystarpilot/Agents
mkdir ../outputs/NoUncertaintystarpilot/Collectors
bsub -o "../outputs/NoUncertaintystarpilot/Markdown/NoUncertaintystarpilot_0.md" -J "NoUncertaintystarpilot_0" -P "NoUncertaintystarpilot-0 -environment starpilot -uncertainty 0 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/Uncertainty=0.5dodgeball/
mkdir ../outputs/Uncertainty=0.5dodgeball/Markdown
mkdir ../outputs/Uncertainty=0.5dodgeball/Agents
mkdir ../outputs/Uncertainty=0.5dodgeball/Collectors
bsub -o "../outputs/Uncertainty=0.5dodgeball/Markdown/Uncertainty=0.5dodgeball_0.md" -J "Uncertainty=0.5dodgeball_0" -P "Uncertainty=0.5dodgeball-0 -environment dodgeball -uncertainty 1 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/NoUncertaintydodgeball/
mkdir ../outputs/NoUncertaintydodgeball/Markdown
mkdir ../outputs/NoUncertaintydodgeball/Agents
mkdir ../outputs/NoUncertaintydodgeball/Collectors
bsub -o "../outputs/NoUncertaintydodgeball/Markdown/NoUncertaintydodgeball_0.md" -J "NoUncertaintydodgeball_0" -P "NoUncertaintydodgeball-0 -environment dodgeball -uncertainty 0 -reward_normalization 0 -memory 500000" < submit.sh
