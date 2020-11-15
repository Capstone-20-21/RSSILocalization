import subprocess
import os, sys
import argparse
from shutil import copyfile, move
from lxml import etree
from ast import literal_eval

'''
Sample Usage:
-----------------------

python Simulator.py

Arguments:
--receiverPositions "..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions__0_-1.5_2__50_1.5_2__101_7_1.dat"
--geometryFile "Simulator\Geometry.stl"
--outputFile "Outputs\ReceivedPowers__0_-1.5_2__50_1.5_2__101_7_1.csv"
--outputFolder "Outputs"
--sourcePosition (1,0,2)
--numReflectionMax 2
--numDiffractionMax 0

'''

class Vector3:
    def __init__(self, *args):
        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        else:
            tupleVector = literal_eval(args[0])
            self.x = tupleVector[0]
            self.y = tupleVector[1]
            self.z = tupleVector[2]

    def __str__(self):
        return f"({self.x} {self.y} {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def ConfigFormat(self):
        return f"<x>{self.x}</x> <y>{self.y}</y> <z>{self.z}</z>"

def csv_file(string):
    # Check that string is .csv file
    root, ext = os.path.splitext(string)
    if not ext == ".csv":
        raise OSError(f"{string} is not a .csv file")

    # Check if file given is in a directory that does not exist
    dir_name = os.path.realpath(os.path.dirname(string))
    if not os.path.isdir(dir_name):
        raise OSError(dir_name + " does not exist")

    return os.path.realpath(string)


def dat_file(string):
    # Check that string is .dat file
    root, ext = os.path.splitext(string)
    if not ext == ".dat":
        raise OSError(f"{string} is not a .dat file")

    # Check if file given does not exist
    if not os.path.isfile(os.path.realpath(string)):
        raise OSError(os.path.realpath(string) + " does not exist")

    return os.path.realpath(string)


def stl_file(string):
    # Check that string is .stl file
    root, ext = os.path.splitext(string)
    if not ext == ".stl":
        raise OSError(f"{string} is not a .stl file")

    # Check if file given does not exist
    if not os.path.isfile(os.path.realpath(string)):
        raise OSError(os.path.realpath(string) + " does not exist")

    return os.path.realpath(string)


def ParseArguments():
    """
    Parse the arguments needed for this function
    :return: (point1, point2, numPoints) - 3D vectors
    """
    
    parser = argparse.ArgumentParser(prog=sys.argv[0], description="Process script arguments")
    parser.add_argument('--receiverPositions', type=dat_file, metavar="ReceiverPositions",
                        default="..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions_environment_processed.dat",
                        help="Path to receiver positions .dat file")
    parser.add_argument('--outputFile', type=str, metavar="OutputFile", default="",
                        help="Path to output .csv file")
    parser.add_argument('--outputFolder', type=str, metavar="OutputFolder", default="Outputs",
                        help="Path to output folder")
    parser.add_argument('--geometryFile', type=stl_file, metavar="GeometryFile", default="..\..\..\BahenHallway.stl",
                        help="Path to geometry .stl file")
    parser.add_argument('--sourcePosition', type=Vector3, metavar="SourcePosition", help="Source Position (x,y,z)",
                        default=Vector3(0.01, 0.99, 1.5))
    parser.add_argument('--numReflectionMax', type=int, metavar="NumReflectionMax", help="Number Maximum of Reflections",
                        default=0)
    parser.add_argument('--numDiffractionMax', type=int, metavar="NumDiffractionMax",
                        help="Number Maximum of Diffractions",
                        default=0)


    arguments = parser.parse_args()

    receiverPositionsFile = arguments.receiverPositions
    outputFile = arguments.outputFile
    outputFolder = arguments.outputFolder
    geometryFile = arguments.geometryFile
    sourcePosition = arguments.sourcePosition
    numReflectionMax = arguments.numReflectionMax
    numDiffractionMax = arguments.numDiffractionMax
    
    if outputFile=="":
        receiverPositionsFileName= receiverPositionsFile.split('\\')[-1][:-4]
        outputFile=f"r{numReflectionMax}_d{numDiffractionMax}_{receiverPositionsFileName}_s({sourcePosition.x},{sourcePosition.y},{sourcePosition.z}).csv"
    else:
        csv_file(outputFile)

    return receiverPositionsFile, outputFile, outputFolder, geometryFile, sourcePosition, numReflectionMax, numDiffractionMax


def main():
    print("Simulator.py:")
    print()

    receiverPositionsFile, desiredOutputFile, outputFolder, geometryFile, sourcePosition, numReflectionMax, numDiffractionMax = ParseArguments()

    print(f"ReceiverPositions: {receiverPositionsFile}")
    print(f"Geometry: {geometryFile}")
    print(f"Output File: {desiredOutputFile}")
    print(f"Source Position: {str(sourcePosition)}")
    print()

    # Setup needed path variables
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    executablePath = scriptPath + "\\Simulator\\"
    executable = "RayTubeTracing.exe"

    # Rename config.xml to configBak.xml
    configFile = executablePath + "config.xml"
    backupConfigFile = executablePath + "configBak.xml"
    move(configFile, backupConfigFile)

    # Rename ReceivedPowers.csv to ReceivedPowersBakcsv
    outputFile = executablePath + "ReceivedPowers.csv"
    backupOutputFile = executablePath + "ReceivedPowersBak.csv"
    move(outputFile, backupOutputFile)

    # Generate new config.xml changes
    receiverPositionsReplacement = f"  <receiver_position_filename>{receiverPositionsFile}</receiver_position_filename>\n"
    geometryFileReplacement = f"  <geometry_filename>{geometryFile}</geometry_filename>\n"
    sourcePositionReplacement = f"  <source_position> {sourcePosition.ConfigFormat()} </source_position>\n"
    numReflectionMaxReplacement = f"  <num_reflection_max>{numReflectionMax}</num_reflection_max>\n"
    numDiffractionMaxReplacement = f"  <num_diffraction_max>{numDiffractionMax}</num_diffraction_max>\n"

    # Write new config.xml file
    with open(configFile, 'w') as newConfig, open(backupConfigFile, 'r') as oldConfig:
        for line in oldConfig:
            if "receiver_position_filename" in line:
                newConfig.write(receiverPositionsReplacement)
            elif "geometry_filename" in line:
                newConfig.write(geometryFileReplacement)
            elif "source_position" in line:
                newConfig.write(sourcePositionReplacement)
            elif "num_reflection_max" in line:
                newConfig.write(numReflectionMaxReplacement)
            elif "num_diffraction_max" in line:
                newConfig.write(numDiffractionMaxReplacement)
            else:
                newConfig.write(line)

    try:
        # Run ray tracer program
        subprocess.run([executablePath + executable], shell=True, cwd=executablePath)

        # Move output to desired location & revert backup
        desiredLocation = f"{outputFolder}\\{desiredOutputFile}"
        os.makedirs(os.path.dirname(desiredLocation), exist_ok=True)
        move(outputFile, desiredLocation)
    except Exception as e:
        print("ERROR RUNNING EXECUTABLE")
        print(e)
    finally:
        # Delete generated config.xml and revert backup
        os.remove(configFile)
        move(backupConfigFile, configFile)

        # revert backup ReceivedPowers.csv
        move(backupOutputFile, outputFile)

if __name__ == "__main__":
    main()
