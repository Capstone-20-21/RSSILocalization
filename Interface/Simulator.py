import subprocess
import os, sys
import argparse
from shutil import copyfile, move
from lxml import etree

'''
Sample Usage:

python Simulator.py --receiverPositions "D:\Files\Local 
Storage\Development\School\Capstone\SimulatorInterface\ReceiverPositions\SampleReceiverPositions
\ReceiverPositions__0_-1.5_2__50_1.5_2__101_7_1.dat" --geometryFile "Simulator\Geometry.stl" --outputFile 
"Outputs\ReceivedPowers__0_-1.5_2__50_1.5_2__101_7_1.csv" 

'''


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
                        default="receiverPositions.dat",
                        help="Path to receiver positions .dat file")
    parser.add_argument('--outputFile', type=csv_file, metavar="OutputFile", default="Outputs\\ReceivedPowers.csv",
                        help="Path to output .csv file")
    parser.add_argument('--geometryFile', type=stl_file, metavar="GeometryFile", default="Geometry.stl",
                        help="Path to geometry .stl file")

    arguments = parser.parse_args()

    receiverPositionsFile = arguments.receiverPositions
    outputFile = arguments.outputFile
    geometryFile = arguments.geometryFile

    return receiverPositionsFile, outputFile, geometryFile


if __name__ == "__main__":
    print("Simulator.py:")
    print()

    receiverPositionsFile, desiredOutputFile, geometryFile = ParseArguments()

    print(f"ReceiverPositions: {receiverPositionsFile}")
    print(f"Geometry: {geometryFile}")
    print(f"Output File: {desiredOutputFile}")
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

    # Write new config.xml file
    with open(configFile, 'w') as newConfig, open(backupConfigFile, 'r') as oldConfig:
        for line in oldConfig:
            if "receiver_position_filename" in line:
                newConfig.write(receiverPositionsReplacement)
            elif "geometry_filename" in line:
                newConfig.write(geometryFileReplacement)
            else:
                newConfig.write(line)

    try:
        # Run ray tracer program
        subprocess.run([executablePath + executable], shell=True, cwd=executablePath)

        # Move output to desired location & revert backup
        move(outputFile, desiredOutputFile)
    except:
        print("ERROR RUNNING EXECUTABLE")
    finally:
        # Delete generated config.xml and revert backup
        os.remove(configFile)
        move(backupConfigFile, configFile)

        # revert backup ReceivedPowers.csv
        move(backupOutputFile, outputFile)


