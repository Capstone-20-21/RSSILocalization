@echo off

set progressFile=SimulationProgress.log
echo. >> progressFile
echo. >> progressFile
echo New Simulation Run: >> progressFile
echo. >> progressFile


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=0
set ND=0
set OFLD="Outputs\Dataset\r%NR%_d%ND%"
echo r%NR%_d%ND% Starting: %TIME% >> progressFile
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD%
echo r%NR%_d%ND% Done: %TIME% >> progressFile
echo. >> progressFile


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=1
set ND=0
set OFLD="Outputs\Dataset\r%NR%_d%ND%"
echo r%NR%_d%ND% Starting: %TIME% >> progressFile
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD%
echo r%NR%_d%ND% Done: %TIME% >> progressFile
echo. >> progressFile


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=2
set ND=0
set OFLD="Outputs\Dataset\r%NR%_d%ND%"
echo r%NR%_d%ND% Starting: %TIME% >> progressFile
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD%
echo r%NR%_d%ND% Done: %TIME% >> progressFile
echo. >> progressFile


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=3
set ND=0
set OFLD="Outputs\Dataset\r%NR%_d%ND%"
echo r%NR%_d%ND% Starting: %TIME% >> progressFile
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD%
echo r%NR%_d%ND% Done: %TIME% >> progressFile
echo. >> progressFile


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=4
set ND=0
set OFLD="Outputs\Dataset\r%NR%_d%ND%"
echo r%NR%_d%ND% Starting: %TIME% >> progressFile
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD%
echo r%NR%_d%ND% Done: %TIME% >> progressFile
echo. >> progressFile


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=5
set ND=0
set OFLD="Outputs\Dataset\r%NR%_d%ND%"
echo r%NR%_d%ND% Starting: %TIME% >> progressFile
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD%
echo r%NR%_d%ND% Done: %TIME% >> progressFile
echo. >> progressFile


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=6
set ND=0
set OFLD="Outputs\Dataset\r%NR%_d%ND%"
echo r%NR%_d%ND% Starting: %TIME% >> progressFile
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD%
echo r%NR%_d%ND% Done: %TIME% >> progressFile
echo. >> progressFile


set RP="..\ReceiverPositions\SampleReceiverPositions\Bahen3DProcessed.dat"
set GF="..\..\..\BahenHallway.stl"
set SP="Simulator\sourcePositions_prevYear.txt"
set NR=7
set ND=0
set OFLD="Outputs\Dataset\r%NR%_d%ND%"
echo r%NR%_d%ND% Starting: %TIME% >> progressFile
call Simulate.bat %RP% %GF% %SP% %NR% %ND% %OFLD%
echo r%NR%_d%ND% Done: %TIME% >> progressFile
echo. >> progressFile