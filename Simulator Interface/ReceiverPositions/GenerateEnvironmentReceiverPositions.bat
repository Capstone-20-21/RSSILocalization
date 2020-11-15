
REM Lower Corridor
set bottomLeft=(-13,-28,1)
set topRight=(-8.5,-8,2.25)
set numX=10
set numY=41
set numZ=6
set outputFile="SampleReceiverPositions/ReceiverPositions_lowerCorridor.dat"
python GenerateReceiverPositions.py %bottomLeft% %topRight% --numX %numX% --numY %numY% --numZ %numZ% --filePath %outputFile%

REM Main Room
set bottomLeft=(-29.5,-7.5,1)
set topRight=(-8.5,10.5,2.25)
set numX=43
set numY=37
set numZ=6
set outputFile="SampleReceiverPositions/ReceiverPositions_mainRoom.dat"
python GenerateReceiverPositions.py %bottomLeft% %topRight% --numX %numX% --numY %numY% --numZ %numZ% --filePath %outputFile%

REM Connecting Corridor
set bottomLeft=(-12.5,11,1)
set topRight=(-8.5,13,2.25)
set numX=9
set numY=5
set numZ=6
set outputFile="SampleReceiverPositions/ReceiverPositions_connectingCorridor.dat"
python GenerateReceiverPositions.py %bottomLeft% %topRight% --numX %numX% --numY %numY% --numZ %numZ% --filePath %outputFile%

REM Main Corridor
set bottomLeft=(-43.5,13.5,1)
set topRight=(33,20.5,2.25)
set numX=154
set numY=15
set numZ=6
set outputFile="SampleReceiverPositions/ReceiverPositions_mainCorridor.dat"
python GenerateReceiverPositions.py %bottomLeft% %topRight% --numX %numX% --numY %numY% --numZ %numZ% --filePath %outputFile%

REM Upper Corridor
set bottomLeft=(21,21,1)
set topRight=(24,31.5,2.25)
set numX=7
set numY=22
set numZ=6
set outputFile="SampleReceiverPositions/ReceiverPositions_upperCorridor.dat"
python GenerateReceiverPositions.py %bottomLeft% %topRight% --numX %numX% --numY %numY% --numZ %numZ% --filePath %outputFile%