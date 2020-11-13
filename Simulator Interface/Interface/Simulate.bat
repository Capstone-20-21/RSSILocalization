@echo off

echo Running Simulations:

REM Arguments
set RP=%1
echo   ReceiverPositions - %RP%

set GF=%2
echo   GeometryFile - %GF%

set SP=%3
echo   SourcePositions - %SP%

set NR=%4
echo   NumReflections - %NR%

set ND=%5
echo   NumDiffractions - %ND%

set OF=%6
echo   OutputFile - %OF%

if "%OF%"=="" (
  python MultipleSource.py --receiverPositions %RP% --geometryFile %GF% --sourceFile %SP% --numReflectionMax %NR% --numDiffractionMax %ND%
) else (
  python MultipleSource.py --receiverPositions %RP% --geometryFile %GF% --outputFile %OF% --sourceFile %SP% --numReflectionMax %NR% --numDiffractionMax %ND%
)