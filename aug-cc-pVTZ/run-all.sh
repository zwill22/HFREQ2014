#!/bin/bash

for folder in */; do
echo ${folder};
cd ${folder};

if [ ${folder} == *"-V"* ]; then
true
else
~/gmtkn30/scripts/run-dir.sh 24 4 . all
fi

cd ..;
done
