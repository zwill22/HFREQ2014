#!/bin/bash

for folder in */; do
echo ${folder};
cd ${folder};

if [ ${folder} == *"-V"* ]; then
true
elif [ ${folder} == *"WM21"* ]; then
~/gmtkn30/scripts/run-dir.sh 24 1 . files
elif [ ${folder} == *"UW12"* ]; then
~/gmtkn30/scripts/run-dir.sh 24 1 . files
else
~/gmtkn30/scripts/run-dir.sh 24 4 . all
fi

cd ..;
done
