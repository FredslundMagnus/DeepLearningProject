#!/bin/sh
mkdir ../outputs/Final_stateUncertainty(0and0)bigfish/
mkdir ../outputs/Final_stateUncertainty(0and0)bigfish/Markdown
mkdir ../outputs/Final_stateUncertainty(0and0)bigfish/Agents
mkdir ../outputs/Final_stateUncertainty(0and0)bigfish/Collectors
bsub -o "../outputs/Final_stateUncertainty(0and0)bigfish/Markdown/Final_stateUncertainty(0and0)bigfish_0.md" -J "Final_stateUncertainty(0and0)bigfish_0" -P "Final_stateUncertainty(0and0)bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Final_stateUncertainty(0dot25and0)bigfish/
mkdir ../outputs/Final_stateUncertainty(0dot25and0)bigfish/Markdown
mkdir ../outputs/Final_stateUncertainty(0dot25and0)bigfish/Agents
mkdir ../outputs/Final_stateUncertainty(0dot25and0)bigfish/Collectors
bsub -o "../outputs/Final_stateUncertainty(0dot25and0)bigfish/Markdown/Final_stateUncertainty(0dot25and0)bigfish_0.md" -J "Final_stateUncertainty(0dot25and0)bigfish_0" -P "Final_stateUncertainty(0dot25and0)bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0.25 -state_difference_weight 0" < submit.sh
mkdir ../outputs/Final_stateUncertainty(0and0dot25)bigfish/
mkdir ../outputs/Final_stateUncertainty(0and0dot25)bigfish/Markdown
mkdir ../outputs/Final_stateUncertainty(0and0dot25)bigfish/Agents
mkdir ../outputs/Final_stateUncertainty(0and0dot25)bigfish/Collectors
bsub -o "../outputs/Final_stateUncertainty(0and0dot25)bigfish/Markdown/Final_stateUncertainty(0and0dot25)bigfish_0.md" -J "Final_stateUncertainty(0and0dot25)bigfish_0" -P "Final_stateUncertainty(0and0dot25)bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0 -state_difference_weight 0.25" < submit.sh
mkdir ../outputs/Final_stateUncertainty(0dot25and0dot25)bigfish/
mkdir ../outputs/Final_stateUncertainty(0dot25and0dot25)bigfish/Markdown
mkdir ../outputs/Final_stateUncertainty(0dot25and0dot25)bigfish/Agents
mkdir ../outputs/Final_stateUncertainty(0dot25and0dot25)bigfish/Collectors
bsub -o "../outputs/Final_stateUncertainty(0dot25and0dot25)bigfish/Markdown/Final_stateUncertainty(0dot25and0dot25)bigfish_0.md" -J "Final_stateUncertainty(0dot25and0dot25)bigfish_0" -P "Final_stateUncertainty(0dot25and0dot25)bigfish-0 -environment bigfish -uncertainty 1 -state_difference 1 -uncertainty_weight 0.25 -state_difference_weight 0.25" < submit.sh
