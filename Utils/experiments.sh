#!/bin/sh
mkdir ../outputs/Discount_0.70
mkdir ../outputs/Discount_0.70/csv
mkdir ../outputs/Discount_0.70/trained
mkdir ../outputs/Discount_0.70/TrainingCurve
mkdir ../outputs/Discount_0.70/Weights
mkdir ../outputs/Discount_0.70/Elo_Rating
mkdir ../outputs/Discount_0.70/Increase_in_Elo_over_time
mkdir ../outputs/Discount_0.70/data
bsub -o "../outputs/Discount_0.70/Discount_0.70_0.md" -J "Discount_0.70_0" -P "Discount_0.70-0 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_1.md" -J "Discount_0.70_1" -P "Discount_0.70-1 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_2.md" -J "Discount_0.70_2" -P "Discount_0.70-2 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_3.md" -J "Discount_0.70_3" -P "Discount_0.70-3 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_4.md" -J "Discount_0.70_4" -P "Discount_0.70-4 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_5.md" -J "Discount_0.70_5" -P "Discount_0.70-5 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_6.md" -J "Discount_0.70_6" -P "Discount_0.70-6 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_7.md" -J "Discount_0.70_7" -P "Discount_0.70-7 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_8.md" -J "Discount_0.70_8" -P "Discount_0.70-8 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount_0.70/Discount_0.70_9.md" -J "Discount_0.70_9" -P "Discount_0.70-9 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
