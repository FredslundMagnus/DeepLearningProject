#!/bin/sh
mkdir ../outputs/Base_bigfish/
mkdir ../outputs/Base_bigfish/Markdown
mkdir ../outputs/Base_bigfish/Agents
mkdir ../outputs/Base_bigfish/Collectors
bsub -o "../outputs/Base_bigfish/Markdown/Base_bigfish_0.md" -J "Base_bigfish_0" -P "Base_bigfish-0 -environment bigfish" < submit.sh
mkdir ../outputs/Base_bossfight/
mkdir ../outputs/Base_bossfight/Markdown
mkdir ../outputs/Base_bossfight/Agents
mkdir ../outputs/Base_bossfight/Collectors
bsub -o "../outputs/Base_bossfight/Markdown/Base_bossfight_0.md" -J "Base_bossfight_0" -P "Base_bossfight-0 -environment bossfight" < submit.sh
mkdir ../outputs/Base_caveflyer/
mkdir ../outputs/Base_caveflyer/Markdown
mkdir ../outputs/Base_caveflyer/Agents
mkdir ../outputs/Base_caveflyer/Collectors
bsub -o "../outputs/Base_caveflyer/Markdown/Base_caveflyer_0.md" -J "Base_caveflyer_0" -P "Base_caveflyer-0 -environment caveflyer" < submit.sh
mkdir ../outputs/Base_chaser/
mkdir ../outputs/Base_chaser/Markdown
mkdir ../outputs/Base_chaser/Agents
mkdir ../outputs/Base_chaser/Collectors
bsub -o "../outputs/Base_chaser/Markdown/Base_chaser_0.md" -J "Base_chaser_0" -P "Base_chaser-0 -environment chaser" < submit.sh
mkdir ../outputs/Base_climber/
mkdir ../outputs/Base_climber/Markdown
mkdir ../outputs/Base_climber/Agents
mkdir ../outputs/Base_climber/Collectors
bsub -o "../outputs/Base_climber/Markdown/Base_climber_0.md" -J "Base_climber_0" -P "Base_climber-0 -environment climber" < submit.sh
mkdir ../outputs/Base_coinrun/
mkdir ../outputs/Base_coinrun/Markdown
mkdir ../outputs/Base_coinrun/Agents
mkdir ../outputs/Base_coinrun/Collectors
bsub -o "../outputs/Base_coinrun/Markdown/Base_coinrun_0.md" -J "Base_coinrun_0" -P "Base_coinrun-0 -environment coinrun" < submit.sh
mkdir ../outputs/Base_dodgeball/
mkdir ../outputs/Base_dodgeball/Markdown
mkdir ../outputs/Base_dodgeball/Agents
mkdir ../outputs/Base_dodgeball/Collectors
bsub -o "../outputs/Base_dodgeball/Markdown/Base_dodgeball_0.md" -J "Base_dodgeball_0" -P "Base_dodgeball-0 -environment dodgeball" < submit.sh
mkdir ../outputs/Base_fruitbot/
mkdir ../outputs/Base_fruitbot/Markdown
mkdir ../outputs/Base_fruitbot/Agents
mkdir ../outputs/Base_fruitbot/Collectors
bsub -o "../outputs/Base_fruitbot/Markdown/Base_fruitbot_0.md" -J "Base_fruitbot_0" -P "Base_fruitbot-0 -environment fruitbot" < submit.sh
mkdir ../outputs/Base_heist/
mkdir ../outputs/Base_heist/Markdown
mkdir ../outputs/Base_heist/Agents
mkdir ../outputs/Base_heist/Collectors
bsub -o "../outputs/Base_heist/Markdown/Base_heist_0.md" -J "Base_heist_0" -P "Base_heist-0 -environment heist" < submit.sh
mkdir ../outputs/Base_jumper/
mkdir ../outputs/Base_jumper/Markdown
mkdir ../outputs/Base_jumper/Agents
mkdir ../outputs/Base_jumper/Collectors
bsub -o "../outputs/Base_jumper/Markdown/Base_jumper_0.md" -J "Base_jumper_0" -P "Base_jumper-0 -environment jumper" < submit.sh
mkdir ../outputs/Base_leaper/
mkdir ../outputs/Base_leaper/Markdown
mkdir ../outputs/Base_leaper/Agents
mkdir ../outputs/Base_leaper/Collectors
bsub -o "../outputs/Base_leaper/Markdown/Base_leaper_0.md" -J "Base_leaper_0" -P "Base_leaper-0 -environment leaper" < submit.sh
mkdir ../outputs/Base_maze/
mkdir ../outputs/Base_maze/Markdown
mkdir ../outputs/Base_maze/Agents
mkdir ../outputs/Base_maze/Collectors
bsub -o "../outputs/Base_maze/Markdown/Base_maze_0.md" -J "Base_maze_0" -P "Base_maze-0 -environment maze" < submit.sh
mkdir ../outputs/Base_miner/
mkdir ../outputs/Base_miner/Markdown
mkdir ../outputs/Base_miner/Agents
mkdir ../outputs/Base_miner/Collectors
bsub -o "../outputs/Base_miner/Markdown/Base_miner_0.md" -J "Base_miner_0" -P "Base_miner-0 -environment miner" < submit.sh
mkdir ../outputs/Base_ninja/
mkdir ../outputs/Base_ninja/Markdown
mkdir ../outputs/Base_ninja/Agents
mkdir ../outputs/Base_ninja/Collectors
bsub -o "../outputs/Base_ninja/Markdown/Base_ninja_0.md" -J "Base_ninja_0" -P "Base_ninja-0 -environment ninja" < submit.sh
mkdir ../outputs/Base_plunder/
mkdir ../outputs/Base_plunder/Markdown
mkdir ../outputs/Base_plunder/Agents
mkdir ../outputs/Base_plunder/Collectors
bsub -o "../outputs/Base_plunder/Markdown/Base_plunder_0.md" -J "Base_plunder_0" -P "Base_plunder-0 -environment plunder" < submit.sh
mkdir ../outputs/Base_starpilot/
mkdir ../outputs/Base_starpilot/Markdown
mkdir ../outputs/Base_starpilot/Agents
mkdir ../outputs/Base_starpilot/Collectors
bsub -o "../outputs/Base_starpilot/Markdown/Base_starpilot_0.md" -J "Base_starpilot_0" -P "Base_starpilot-0 -environment starpilot" < submit.sh
