#!/bin/sh
mkdir ../outputs/Discount-0.70
bsub -o "../outputs/Discount-0.70/Discount-0.70-0.md" -J "Discount-0.70-0" -P "Discount-0.70-0 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-1.md" -J "Discount-0.70-1" -P "Discount-0.70-1 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-2.md" -J "Discount-0.70-2" -P "Discount-0.70-2 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-3.md" -J "Discount-0.70-3" -P "Discount-0.70-3 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-4.md" -J "Discount-0.70-4" -P "Discount-0.70-4 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-5.md" -J "Discount-0.70-5" -P "Discount-0.70-5 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-6.md" -J "Discount-0.70-6" -P "Discount-0.70-6 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-7.md" -J "Discount-0.70-7" -P "Discount-0.70-7 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-8.md" -J "Discount-0.70-8" -P "Discount-0.70-8 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
bsub -o "../outputs/Discount-0.70/Discount-0.70-9.md" -J "Discount-0.70-9" -P "Discount-0.70-9 -lossf MME -discount 0.7 -lambd 0.5 -lr 0.0001 -dropout 0" < submit.sh
