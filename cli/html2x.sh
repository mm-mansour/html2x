#!/bin/sh
 if [ -z "$*" ];
 	then 
 		python engine.py -h
 		exit 0
 fi

python engine.py "$@"