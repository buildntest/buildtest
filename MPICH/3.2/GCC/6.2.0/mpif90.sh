#!/bin/sh

module purge
module load GCC/6.2.0
module=MPICH$1
version=3.2$2
module load $module/$version

if [ $? != 0 ]; then
	echo "unable to load module $module/$version"
	exit 1
fi

mpif90 -v
if [ $? != 0 ]; then
	echo "Unable to run mpif90 -v"
	exit 1
fi

