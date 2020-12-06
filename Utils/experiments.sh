#!/bin/sh
mkdir ../outputs/Uncertainty0state_difference0.1softepsdodgeball/
mkdir ../outputs/Uncertainty0state_difference0.1softepsdodgeball/Markdown
mkdir ../outputs/Uncertainty0state_difference0.1softepsdodgeball/Agents
mkdir ../outputs/Uncertainty0state_difference0.1softepsdodgeball/Collectors
bsub -o "../outputs/Uncertainty0state_difference0.1softepsdodgeball/Markdown/Uncertainty0state_difference0.1softepsdodgeball_0.md" -J "Uncertainty0state_difference0.1softepsdodgeball_0" -P "Uncertainty0state_difference0.1softepsdodgeball-0 -environment dodgeball -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1 -exploration epsintosoftmax" < submit.sh
mkdir ../outputs/Uncertainty0state_difference0.1dodgeball/
mkdir ../outputs/Uncertainty0state_difference0.1dodgeball/Markdown
mkdir ../outputs/Uncertainty0state_difference0.1dodgeball/Agents
mkdir ../outputs/Uncertainty0state_difference0.1dodgeball/Collectors
bsub -o "../outputs/Uncertainty0state_difference0.1dodgeball/Markdown/Uncertainty0state_difference0.1dodgeball_0.md" -J "Uncertainty0state_difference0.1dodgeball_0" -P "Uncertainty0state_difference0.1dodgeball-0 -environment dodgeball -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/Uncertainty0.1state_difference0softepsdodgeball/
mkdir ../outputs/Uncertainty0.1state_difference0softepsdodgeball/Markdown
mkdir ../outputs/Uncertainty0.1state_difference0softepsdodgeball/Agents
mkdir ../outputs/Uncertainty0.1state_difference0softepsdodgeball/Collectors
bsub -o "../outputs/Uncertainty0.1state_difference0softepsdodgeball/Markdown/Uncertainty0.1state_difference0softepsdodgeball_0.md" -J "Uncertainty0.1state_difference0softepsdodgeball_0" -P "Uncertainty0.1state_difference0softepsdodgeball-0 -environment dodgeball -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0 -exploration epsintosoftmax" < submit.sh
mkdir ../outputs/Uncertainty0.1state_difference0dodgeball/
mkdir ../outputs/Uncertainty0.1state_difference0dodgeball/Markdown
mkdir ../outputs/Uncertainty0.1state_difference0dodgeball/Agents
mkdir ../outputs/Uncertainty0.1state_difference0dodgeball/Collectors
bsub -o "../outputs/Uncertainty0.1state_difference0dodgeball/Markdown/Uncertainty0.1state_difference0dodgeball_0.md" -J "Uncertainty0.1state_difference0dodgeball_0" -P "Uncertainty0.1state_difference0dodgeball-0 -environment dodgeball -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Uncertainty0state_difference0dodgeball/
mkdir ../outputs/Uncertainty0state_difference0dodgeball/Markdown
mkdir ../outputs/Uncertainty0state_difference0dodgeball/Agents
mkdir ../outputs/Uncertainty0state_difference0dodgeball/Collectors
bsub -o "../outputs/Uncertainty0state_difference0dodgeball/Markdown/Uncertainty0state_difference0dodgeball_0.md" -J "Uncertainty0state_difference0dodgeball_0" -P "Uncertainty0state_difference0dodgeball-0 -environment dodgeball -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Uncertainty0state_difference0softepsdodgeball/
mkdir ../outputs/Uncertainty0state_difference0softepsdodgeball/Markdown
mkdir ../outputs/Uncertainty0state_difference0softepsdodgeball/Agents
mkdir ../outputs/Uncertainty0state_difference0softepsdodgeball/Collectors
bsub -o "../outputs/Uncertainty0state_difference0softepsdodgeball/Markdown/Uncertainty0state_difference0softepsdodgeball_0.md" -J "Uncertainty0state_difference0softepsdodgeball_0" -P "Uncertainty0state_difference0softepsdodgeball-0 -environment dodgeball -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0 -exploration epsintosoftmax" < submit.sh
