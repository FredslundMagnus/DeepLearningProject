#!/bin/sh
mkdir ../outputs/Final_stateUncertainty0and)bigfish/
mkdir ../outputs/Final_stateUncertainty0and)bigfish/Markdown
mkdir ../outputs/Final_stateUncertainty0and)bigfish/Agents
mkdir ../outputs/Final_stateUncertainty0and)bigfish/Collectors
bsub -o "../outputs/Final_stateUncertainty0and)bigfish/Markdown/Final_stateUncertainty0and)bigfish_0.md" -J "Final_stateUncertainty0and)bigfish_0" -P "Final_stateUncertainty0and)bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Final_stateUncertainty0.25and0bigfish/
mkdir ../outputs/Final_stateUncertainty0.25and0bigfish/Markdown
mkdir ../outputs/Final_stateUncertainty0.25and0bigfish/Agents
mkdir ../outputs/Final_stateUncertainty0.25and0bigfish/Collectors
bsub -o "../outputs/Final_stateUncertainty0.25and0bigfish/Markdown/Final_stateUncertainty0.25and0bigfish_0.md" -J "Final_stateUncertainty0.25and0bigfish_0" -P "Final_stateUncertainty0.25and0bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0.25 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Final_stateUncertainty0and0.25bigfish/
mkdir ../outputs/Final_stateUncertainty0and0.25bigfish/Markdown
mkdir ../outputs/Final_stateUncertainty0and0.25bigfish/Agents
mkdir ../outputs/Final_stateUncertainty0and0.25bigfish/Collectors
bsub -o "../outputs/Final_stateUncertainty0and0.25bigfish/Markdown/Final_stateUncertainty0and0.25bigfish_0.md" -J "Final_stateUncertainty0and0.25bigfish_0" -P "Final_stateUncertainty0and0.25bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.25" < submit.sh
mkdir ../outputs/Final_stateUncertainty0.25and0.25bigfish/
mkdir ../outputs/Final_stateUncertainty0.25and0.25bigfish/Markdown
mkdir ../outputs/Final_stateUncertainty0.25and0.25bigfish/Agents
mkdir ../outputs/Final_stateUncertainty0.25and0.25bigfish/Collectors
bsub -o "../outputs/Final_stateUncertainty0.25and0.25bigfish/Markdown/Final_stateUncertainty0.25and0.25bigfish_0.md" -J "Final_stateUncertainty0.25and0.25bigfish_0" -P "Final_stateUncertainty0.25and0.25bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0.25 -state_difference_weight 0.25" < submit.sh
