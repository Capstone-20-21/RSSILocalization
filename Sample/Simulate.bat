
@echo off

set Program="..\Simulator\RayTubeTracing.exe"

echo;
echo '%0' started by %USERNAME% @ %COMPUTERNAME%: %DATE% %TIME%
echo current directory: '%CD%'
echo program file: '%Program%'

echo;

%Program%

echo;

echo '%0' finished: %DATE% %TIME%
echo;

