#!/bin/bash

basis=${1}

cd ${basis} || exit 1;
for functional in */; do
    cd ${functional} || exit 1
    i=0
    n=0
    for filename in *.in; do
      file=${filename%.in}
      n=$((n+1))
      if [ ! -f ${file}.out ]; then
        true
      elif `grep -q "End time" ${file}.out`; then
        i=$((i+1))
      elif `grep -q "Psi4 exiting successfully" ${file}.out`; then
        i=$((i+1))
      fi
    done
    if [[ ${i} != ${n} ]]; then
     echo "${functional}: $((n-i))/${n}"
    fi
    cd ..
done
cd ..
