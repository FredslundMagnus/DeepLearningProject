#!/bin/sh
mkdir ../outputs/Uncertainty0state_difference0.1softepschaser/
mkdir ../outputs/Uncertainty0state_difference0.1softepschaser/Markdown
mkdir ../outputs/Uncertainty0state_difference0.1softepschaser/Agents
mkdir ../outputs/Uncertainty0state_difference0.1softepschaser/Collectors
bsub -o "../outputs/Uncertainty0state_difference0.1softepschaser/Markdown/Uncertainty0state_difference0.1softepschaser_0.md" -J "Uncertainty0state_difference0.1softepschaser_0" -P "Uncertainty0state_difference0.1softepschaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1 -exploration epsintosoftmax" < submit.sh
mkdir ../outputs/Uncertainty0state_difference0.1chaser/
mkdir ../outputs/Uncertainty0state_difference0.1chaser/Markdown
mkdir ../outputs/Uncertainty0state_difference0.1chaser/Agents
mkdir ../outputs/Uncertainty0state_difference0.1chaser/Collectors
bsub -o "../outputs/Uncertainty0state_difference0.1chaser/Markdown/Uncertainty0state_difference0.1chaser_0.md" -J "Uncertainty0state_difference0.1chaser_0" -P "Uncertainty0state_difference0.1chaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/Uncertainty0.1state_difference0softepschaser/
mkdir ../outputs/Uncertainty0.1state_difference0softepschaser/Markdown
mkdir ../outputs/Uncertainty0.1state_difference0softepschaser/Agents
mkdir ../outputs/Uncertainty0.1state_difference0softepschaser/Collectors
bsub -o "../outputs/Uncertainty0.1state_difference0softepschaser/Markdown/Uncertainty0.1state_difference0softepschaser_0.md" -J "Uncertainty0.1state_difference0softepschaser_0" -P "Uncertainty0.1state_difference0softepschaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0 -exploration epsintosoftmax" < submit.sh
mkdir ../outputs/Uncertainty0.1state_difference0chaser/
mkdir ../outputs/Uncertainty0.1state_difference0chaser/Markdown
mkdir ../outputs/Uncertainty0.1state_difference0chaser/Agents
mkdir ../outputs/Uncertainty0.1state_difference0chaser/Collectors
bsub -o "../outputs/Uncertainty0.1state_difference0chaser/Markdown/Uncertainty0.1state_difference0chaser_0.md" -J "Uncertainty0.1state_difference0chaser_0" -P "Uncertainty0.1state_difference0chaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Uncertainty0state_difference0chaser/
mkdir ../outputs/Uncertainty0state_difference0chaser/Markdown
mkdir ../outputs/Uncertainty0state_difference0chaser/Agents
mkdir ../outputs/Uncertainty0state_difference0chaser/Collectors
bsub -o "../outputs/Uncertainty0state_difference0chaser/Markdown/Uncertainty0state_difference0chaser_0.md" -J "Uncertainty0state_difference0chaser_0" -P "Uncertainty0state_difference0chaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Uncertainty0state_difference0chaser/
mkdir ../outputs/Uncertainty0state_difference0chaser/Markdown
mkdir ../outputs/Uncertainty0state_difference0chaser/Agents
mkdir ../outputs/Uncertainty0state_difference0chaser/Collectors
bsub -o "../outputs/Uncertainty0state_difference0chaser/Markdown/Uncertainty0state_difference0chaser_0.md" -J "Uncertainty0state_difference0chaser_0" -P "Uncertainty0state_difference0chaser-0 -environment chaser -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0 -exploration epsintosoftmax" < submit.sh
