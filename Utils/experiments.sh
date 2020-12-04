#!/bin/sh
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0.25and0bigfish/
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0.25and0bigfish/Markdown
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0.25and0bigfish/Agents
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0.25and0bigfish/Collectors
bsub -o "../outputs/Fepsintosoftmax_stateUncertainty0.25and0bigfish/Markdown/Fepsintosoftmax_stateUncertainty0.25and0bigfish_0.md" -J "Fepsintosoftmax_stateUncertainty0.25and0bigfish_0" -P "Fepsintosoftmax_stateUncertainty0.25and0bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0.25 -state_difference_weight 0 -exploration epsintosoftmax" < submit.sh
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0and0.25bigfish/
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0and0.25bigfish/Markdown
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0and0.25bigfish/Agents
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0and0.25bigfish/Collectors
bsub -o "../outputs/Fepsintosoftmax_stateUncertainty0and0.25bigfish/Markdown/Fepsintosoftmax_stateUncertainty0and0.25bigfish_0.md" -J "Fepsintosoftmax_stateUncertainty0and0.25bigfish_0" -P "Fepsintosoftmax_stateUncertainty0and0.25bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.25 -exploration epsintosoftmax" < submit.sh
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0.25and0.25bigfish/
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0.25and0.25bigfish/Markdown
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0.25and0.25bigfish/Agents
mkdir ../outputs/Fepsintosoftmax_stateUncertainty0.25and0.25bigfish/Collectors
bsub -o "../outputs/Fepsintosoftmax_stateUncertainty0.25and0.25bigfish/Markdown/Fepsintosoftmax_stateUncertainty0.25and0.25bigfish_0.md" -J "Fepsintosoftmax_stateUncertainty0.25and0.25bigfish_0" -P "Fepsintosoftmax_stateUncertainty0.25and0.25bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0.25 -state_difference_weight 0.25 -exploration epsintosoftmax" < submit.sh
