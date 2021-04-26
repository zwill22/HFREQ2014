#!/bin/bash

for file in *.in; do

if [ ! -f ${file%.in}.out ]; then

dir=${PWD##*/}

cat > ${file%.in}.sub << EOF
#!/bin/bash -l
#PBS -N "${file%.in}"
#PBS -j oe
#PBS -l walltime=4:00:00
#PBS -l select=1:ncpus=24:mem=144gb
cd ${PWD}
source $HOME/.bashrc
#Setup scratch directory
tmp=\${TMPDIR}
export MKL_THREADING_LAYER=""
conda activate p4env
cp ${file} \${tmp}
cd \${tmp}
psi4 -n 24 -i "${file}" -o  "${file%.in}.out"
cp ${file%.in}.* ${PWD}
cd ${PWD}
EOF

echo ${file%.in}
qsub ${file%.in}.sub
fi
done
