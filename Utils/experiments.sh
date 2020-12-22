#!/bin/sh
mkdir ../outputs/NOPEstarpilot/
mkdir ../outputs/NOPEstarpilot/Markdown
mkdir ../outputs/NOPEstarpilot/Agents
mkdir ../outputs/NOPEstarpilot/Collectors
bsub -o "../outputs/NOPEstarpilot/Markdown/NOPEstarpilot_0.md" -J "NOPEstarpilot_0" -P "NOPEstarpilot-0 -environment starpilot -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/NOPEbossfight/
mkdir ../outputs/NOPEbossfight/Markdown
mkdir ../outputs/NOPEbossfight/Agents
mkdir ../outputs/NOPEbossfight/Collectors
bsub -o "../outputs/NOPEbossfight/Markdown/NOPEbossfight_0.md" -J "NOPEbossfight_0" -P "NOPEbossfight-0 -environment bossfight -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
mkdir ../outputs/NOPEjumper/
mkdir ../outputs/NOPEjumper/Markdown
mkdir ../outputs/NOPEjumper/Agents
mkdir ../outputs/NOPEjumper/Collectors
bsub -o "../outputs/NOPEjumper/Markdown/NOPEjumper_0.md" -J "NOPEjumper_0" -P "NOPEjumper-0 -environment jumper -uncertainty 1 -state_difference 1 -uncertainty_weight 0.1 -state_difference_weight 0.1" < submit.sh
