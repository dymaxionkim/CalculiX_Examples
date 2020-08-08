#!/bin/sh

POSTURE=$1
J2_ANGLE=$2
J3_ANGLE=$3
J2X=$4
J2Z=$5
J3X=$6
J3Z=$7

rm -rf ./$POSTURE
mkdir ./$POSTURE
cp ./eigen.inp ./$POSTURE/eigen.inp
cp ./robot.py ./$POSTURE/robot.py
sed -i "s/J2_ANGLE/$J2_ANGLE/" ./$POSTURE/robot.py
sed -i "s/J3_ANGLE/$J3_ANGLE/" ./$POSTURE/robot.py
sed -i "s/J2X/$J2X/" ./$POSTURE/robot.py
sed -i "s/J2Z/$J2Z/" ./$POSTURE/robot.py
sed -i "s/J3X/$J3X/" ./$POSTURE/robot.py
sed -i "s/J3Z/$J3Z/" ./$POSTURE/robot.py

cd ./$POSTURE
salome -t ./robot.py > salome.log
# https://academic.bancey.com/successfully-clearing-ports-in-salome-code-aster/
python /home/osboxes/.Salome/BINARIES-UB18.04/KERNEL/bin/salome/killSalome.py
killall SALOME_Registry_Server
killall SALOME_ModuleCatalog_Server

unical robot.unv robot.inp
ccx eigen
#cgx eigen.frd
cd ..
