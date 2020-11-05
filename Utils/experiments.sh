#!/bin/sh
mkdir ../outputs/bigfish_test/
mkdir ../outputs/bigfish_test/Markdown
mkdir ../outputs/bigfish_test/Agents
bsub -o "../outputs/bigfish_test/Markdown/bigfish_test_0.md" -J "bigfish_test_0" -P "bigfish_test-0 -environment bigfish" < submit.sh
mkdir ../outputs/chaser_test/
mkdir ../outputs/chaser_test/Markdown
mkdir ../outputs/chaser_test/Agents
bsub -o "../outputs/chaser_test/Markdown/chaser_test_0.md" -J "chaser_test_0" -P "chaser_test-0 -environment chaser" < submit.sh
mkdir ../outputs/fruitbot_test/
mkdir ../outputs/fruitbot_test/Markdown
mkdir ../outputs/fruitbot_test/Agents
bsub -o "../outputs/fruitbot_test/Markdown/fruitbot_test_0.md" -J "fruitbot_test_0" -P "fruitbot_test-0 -environment fruitbot" < submit.sh
