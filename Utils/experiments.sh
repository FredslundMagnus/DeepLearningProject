#!/bin/sh
mkdir ../outputs/NoNormalizationNoUncertainty/
mkdir ../outputs/NoNormalizationNoUncertainty/Markdown
mkdir ../outputs/NoNormalizationNoUncertainty/Agents
mkdir ../outputs/NoNormalizationNoUncertainty/Collectors
bsub -o "../outputs/NoNormalizationNoUncertainty/Markdown/NoNormalizationNoUncertainty_0.md" -J "NoNormalizationNoUncertainty_0" -P "NoNormalizationNoUncertainty-0 -environment fruitbot -use_distribution 0 -uncertainty 0 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/YesNormalizationNoUncertainty/
mkdir ../outputs/YesNormalizationNoUncertainty/Markdown
mkdir ../outputs/YesNormalizationNoUncertainty/Agents
mkdir ../outputs/YesNormalizationNoUncertainty/Collectors
bsub -o "../outputs/YesNormalizationNoUncertainty/Markdown/YesNormalizationNoUncertainty_0.md" -J "YesNormalizationNoUncertainty_0" -P "YesNormalizationNoUncertainty-0 -environment fruitbot -use_distribution 0 -uncertainty 0 -reward_normalization 1 -memory 500000" < submit.sh
mkdir ../outputs/NoNormalizationYesUncertainty/
mkdir ../outputs/NoNormalizationYesUncertainty/Markdown
mkdir ../outputs/NoNormalizationYesUncertainty/Agents
mkdir ../outputs/NoNormalizationYesUncertainty/Collectors
bsub -o "../outputs/NoNormalizationYesUncertainty/Markdown/NoNormalizationYesUncertainty_0.md" -J "NoNormalizationYesUncertainty_0" -P "NoNormalizationYesUncertainty-0 -environment fruitbot -use_distribution 0 -uncertainty 1 -reward_normalization 0 -memory 500000" < submit.sh
mkdir ../outputs/YesNormalizationYesUncertainty/
mkdir ../outputs/YesNormalizationYesUncertainty/Markdown
mkdir ../outputs/YesNormalizationYesUncertainty/Agents
mkdir ../outputs/YesNormalizationYesUncertainty/Collectors
bsub -o "../outputs/YesNormalizationYesUncertainty/Markdown/YesNormalizationYesUncertainty_0.md" -J "YesNormalizationYesUncertainty_0" -P "YesNormalizationYesUncertainty-0 -environment fruitbot -use_distribution 0 -uncertainty 1 -reward_normalization 1 -memory 500000" < submit.sh
