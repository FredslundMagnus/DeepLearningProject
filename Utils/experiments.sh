#!/bin/sh
mkdir ../outputs/NOPE_final_caveflyer/
mkdir ../outputs/NOPE_final_caveflyer/Markdown
mkdir ../outputs/NOPE_final_caveflyer/Agents
mkdir ../outputs/NOPE_final_caveflyer/Collectors
bsub -o "../outputs/NOPE_final_caveflyer/Markdown/NOPE_final_caveflyer_0.md" -J "NOPE_final_caveflyer_0" -P "NOPE_final_caveflyer-0 -environment caveflyer -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_climber/
mkdir ../outputs/NOPE_final_climber/Markdown
mkdir ../outputs/NOPE_final_climber/Agents
mkdir ../outputs/NOPE_final_climber/Collectors
bsub -o "../outputs/NOPE_final_climber/Markdown/NOPE_final_climber_0.md" -J "NOPE_final_climber_0" -P "NOPE_final_climber-0 -environment climber -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_coinrun/
mkdir ../outputs/NOPE_final_coinrun/Markdown
mkdir ../outputs/NOPE_final_coinrun/Agents
mkdir ../outputs/NOPE_final_coinrun/Collectors
bsub -o "../outputs/NOPE_final_coinrun/Markdown/NOPE_final_coinrun_0.md" -J "NOPE_final_coinrun_0" -P "NOPE_final_coinrun-0 -environment coinrun -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_dodgeball/
mkdir ../outputs/NOPE_final_dodgeball/Markdown
mkdir ../outputs/NOPE_final_dodgeball/Agents
mkdir ../outputs/NOPE_final_dodgeball/Collectors
bsub -o "../outputs/NOPE_final_dodgeball/Markdown/NOPE_final_dodgeball_0.md" -J "NOPE_final_dodgeball_0" -P "NOPE_final_dodgeball-0 -environment dodgeball -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
mkdir ../outputs/NOPE_final_heist/
mkdir ../outputs/NOPE_final_heist/Markdown
mkdir ../outputs/NOPE_final_heist/Agents
mkdir ../outputs/NOPE_final_heist/Collectors
bsub -o "../outputs/NOPE_final_heist/Markdown/NOPE_final_heist_0.md" -J "NOPE_final_heist_0" -P "NOPE_final_heist-0 -environment heist -uncertainty 1 -uncertainty_weight 0.1" < submit.sh
