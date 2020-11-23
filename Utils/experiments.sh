#!/bin/sh
mkdir ../outputs/Base_v2_bossfight/
mkdir ../outputs/Base_v2_bossfight/Markdown
mkdir ../outputs/Base_v2_bossfight/Agents
mkdir ../outputs/Base_v2_bossfight/Collectors
bsub -o "../outputs/Base_v2_bossfight/Markdown/Base_v2_bossfight_0.md" -J "Base_v2_bossfight_0" -P "Base_v2_bossfight-0 -environment bossfight" < submit.sh
mkdir ../outputs/Base_v2_chaser/
mkdir ../outputs/Base_v2_chaser/Markdown
mkdir ../outputs/Base_v2_chaser/Agents
mkdir ../outputs/Base_v2_chaser/Collectors
bsub -o "../outputs/Base_v2_chaser/Markdown/Base_v2_chaser_0.md" -J "Base_v2_chaser_0" -P "Base_v2_chaser-0 -environment chaser" < submit.sh
mkdir ../outputs/Base_v2_starpilot/
mkdir ../outputs/Base_v2_starpilot/Markdown
mkdir ../outputs/Base_v2_starpilot/Agents
mkdir ../outputs/Base_v2_starpilot/Collectors
bsub -o "../outputs/Base_v2_starpilot/Markdown/Base_v2_starpilot_0.md" -J "Base_v2_starpilot_0" -P "Base_v2_starpilot-0 -environment starpilot" < submit.sh
mkdir ../outputs/Base_v2_climber/
mkdir ../outputs/Base_v2_climber/Markdown
mkdir ../outputs/Base_v2_climber/Agents
mkdir ../outputs/Base_v2_climber/Collectors
bsub -o "../outputs/Base_v2_climber/Markdown/Base_v2_climber_0.md" -J "Base_v2_climber_0" -P "Base_v2_climber-0 -environment climber" < submit.sh
