@echo off

set progressFile=SimulationProgress.log
set simulatorOutput=SimulatorOutput.log
echo. >> %progressFile%
echo. >> %progressFile%
echo New Simulation Run: >> %progressFile%
echo. >> %progressFile%

echo. > %simulatorOutput%
echo. >> %simulatorOutput%
echo New Simulation Run: >> %simulatorOutput%
echo. >> %simulatorOutput%


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=1
set ND=1
set OFLD="Outputs\Dataset"
echo r%NR%_d%ND% Starting: %TIME% >> %progressFile%
echo r%NR%_d%ND% >> %simulatorOutput%
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD% >> %simulatorOutput%
echo r%NR%_d%ND% Done: %TIME% >> %progressFile%
echo. >> %progressFile%
echo. >> %simulatorOutput%

set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=5
set ND=1
set OFLD="Outputs\Dataset"
echo r%NR%_d%ND% Starting: %TIME% >> %progressFile%
echo r%NR%_d%ND% >> %simulatorOutput%
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD% >> %simulatorOutput%
echo r%NR%_d%ND% Done: %TIME% >> %progressFile%
echo. >> %progressFile%
echo. >> %simulatorOutput%
