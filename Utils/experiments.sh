#!/bin/sh
mkdir ../outputs/Base_v2_bigfish/
mkdir ../outputs/Base_v2_bigfish/Markdown
mkdir ../outputs/Base_v2_bigfish/Agents
mkdir ../outputs/Base_v2_bigfish/Collectors
bsub -o "../outputs/Base_v2_bigfish/Markdown/Base_v2_bigfish_0.md" -J "Base_v2_bigfish_0" -P "Base_v2_bigfish-0 -environment bigfish" < submit.sh
mkdir ../outputs/Base_v2_fruitbot/
mkdir ../outputs/Base_v2_fruitbot/Markdown
mkdir ../outputs/Base_v2_fruitbot/Agents
mkdir ../outputs/Base_v2_fruitbot/Collectors
bsub -o "../outputs/Base_v2_fruitbot/Markdown/Base_v2_fruitbot_0.md" -J "Base_v2_fruitbot_0" -P "Base_v2_fruitbot-0 -environment fruitbot" < submit.sh
mkdir ../outputs/Base_v2_jumper/
mkdir ../outputs/Base_v2_jumper/Markdown
mkdir ../outputs/Base_v2_jumper/Agents
mkdir ../outputs/Base_v2_jumper/Collectors
bsub -o "../outputs/Base_v2_jumper/Markdown/Base_v2_jumper_0.md" -J "Base_v2_jumper_0" -P "Base_v2_jumper-0 -environment jumper" < submit.sh
mkdir ../outputs/Base_v2_leaper/
mkdir ../outputs/Base_v2_leaper/Markdown
mkdir ../outputs/Base_v2_leaper/Agents
mkdir ../outputs/Base_v2_leaper/Collectors
bsub -o "../outputs/Base_v2_leaper/Markdown/Base_v2_leaper_0.md" -J "Base_v2_leaper_0" -P "Base_v2_leaper-0 -environment leaper" < submit.sh
