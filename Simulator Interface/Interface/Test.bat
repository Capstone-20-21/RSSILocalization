@echo off

set RP="..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions_environment_processed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=0
set ND=0
Simulate.bat %RP% %GF% %SP% %NR% %ND%