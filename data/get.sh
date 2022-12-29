#! /bin/bash
wget -nc https://www.csplib.org/Problems/prob001/data/ProblemDataSet200to400.zip
unzip -n ProblemDataSet200to400.zip
wget -nc https://www.csplib.org/Problems/prob001/data/CarSequencing-essence.zip
unzip -n CarSequencing-essence.zip -x __MACOSX/*
wget -nc https://www.csplib.org/Problems/prob001/data/data.txt
