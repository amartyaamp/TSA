#!/bin/bash
echo $1
./ark-tweet-nlp-0.3.2/runTagger.sh --output-format conll $1 > POS_input.txt
python feature_extract.py
#python predict.py > $2

