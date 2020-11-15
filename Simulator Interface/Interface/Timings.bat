@echo off

set timingFile=diffractionTimings1.txt
set simulationOutputFile=diffractionSimulations1.txt

echo NewTest: >> %timingFile%

echo %TIME% >> %timingFile%
echo r1_d0 >> %timingFile%
set RP="..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions_environment_processed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=1
set ND=0
call Simulate.bat %RP% %GF% %SP% %NR% %ND% >> %simulationOutputFile%

echo %TIME% >> %timingFile%

echo r1_d1 >> %timingFile%
set RP="..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions_environment_processed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=1
set ND=1
call Simulate.bat %RP% %GF% %SP% %NR% %ND% >> %simulationOutputFile%

echo %TIME% >> %timingFile%

echo r1_d2 >> %timingFile%
set RP="..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions_environment_processed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=1
set ND=2
call Simulate.bat %RP% %GF% %SP% %NR% %ND% >> %simulationOutputFile%

echo %TIME% >> %timingFile%

echo r1_d3 >> %timingFile%
set RP="..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions_environment_processed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=1
set ND=3
call Simulate.bat %RP% %GF% %SP% %NR% %ND% >> %simulationOutputFile%

echo %TIME% >> %timingFile%

echo r1_d4 >> %timingFile%
set RP="..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions_environment_processed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=1
set ND=4
call Simulate.bat %RP% %GF% %SP% %NR% %ND% >> %simulationOutputFile%

echo %TIME% >> %timingFile%

echo r1_d5 >> %timingFile%
set RP="..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions_environment_processed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=1
set ND=5
call Simulate.bat %RP% %GF% %SP% %NR% %ND% >> %simulationOutputFile%

echo %TIME% >> %timingFile%
echo. >> %timingFile%