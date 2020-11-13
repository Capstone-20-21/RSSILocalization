import argparse
import os, sys
import subprocess
import pandas as pd
import Simulator

'''
Sample Usage:
-----------------------

python MultipleSource.py

Arguments:
--receiverPositions "..\ReceiverPositions\SampleReceiverPositions\ReceiverPositions__0_-1.5_2__50_1.5_2__101_7_1.dat"
--geometryFile "Simulator\Geometry.stl"
--outputFile "Outputs\ReceivedPowers__0_-1.5_2__50_1.5_2__101_7_1"
--sourceFile "Simulator\SourcePositions.txt"
--numReflectionMax 2
--numDiffractionMax 0
'''

def txt_file(string):
    # Check that string is .stl file
    root, ext = os.path.splitext(string)
    if not ext == ".txt":
        raise OSError(f"{string} is not a .txt file")

    # Check if file given does not exist
    if not os.path.isfile(os.path.realpath(string)):
        raise OSError(os.path.realpath(string) + " does not exist")

    return os.path.realpath(string)

def ParseArguments_MultiSource():
    """
    Parse the arguments needed for this function
    :return: (point1, point2, numPoints) - 3D vectors
    """
    parser = argparse.ArgumentParser(prog=sys.argv[0], description="Process script arguments")
    parser.add_argument('--receiverPositions', type=Simulator.dat_file, metavar="ReceiverPositions",
                        default="receiverPositions.dat",
                        help="Path to receiver positions .dat file")
    parser.add_argument('--outputFile', type=str, metavar="OutputFile", default="",
                        help="Path to output .csv file")
    parser.add_argument('--geometryFile', type=Simulator.stl_file, metavar="GeometryFile", default="Geometry.stl",
                        help="Path to geometry .stl file")
    parser.add_argument('--sourceFile', type=txt_file, metavar="SourceFile", help="Source Position (x,y,z) File",
                        default="Simulator\\SourcePositions.txt")
    parser.add_argument('--numReflectionMax', type=int, metavar="NumReflectionMax", help="Number Maximum of Reflections",
                        default=1)
    parser.add_argument('--numDiffractionMax', type=int, metavar="NumDiffractionMax",
                        help="Number Maximum of Diffractions",
                        default=0)


    arguments = parser.parse_args()

    receiverPositionsFile = arguments.receiverPositions
    outputFile = arguments.outputFile
    geometryFile = arguments.geometryFile
    sourceFile = arguments.sourceFile
    numReflectionMax = arguments.numReflectionMax
    numDiffractionMax = arguments.numDiffractionMax
    
    if outputFile=="":
        outputFile=f"Outputs\\r{numReflectionMax}_d{numDiffractionMax}_ReceivedPowers"

    return receiverPositionsFile, outputFile, geometryFile, sourceFile, numReflectionMax, numDiffractionMax

def main():

    print("MultipleSource.py:")
    print()

    receiverPositionsFile, outputFile, geometryFile, sourceFile, numReflectionMax, numDiffractionMax = ParseArguments_MultiSource()

    #parse source position file and call Simulator.py for each source positions
    source_position_df = pd.read_csv(sourceFile, header = None)

    for index, row in source_position_df.iterrows():
        sourcePosition = (row[0], row[1], row[2])

        desiredOutputFile = outputFile + '_s('+str(row[0])+','+str(row[1])+','+str(row[2])+').csv'

        sys.argv = ['Simulator.py','--receiverPositions', receiverPositionsFile, '--geometryFile', geometryFile,
        '--outputFile', desiredOutputFile, '--sourcePosition', str(sourcePosition), '--numReflectionMax', str(numReflectionMax),
        '--numDiffractionMax', str(numDiffractionMax)]

        Simulator.main()

        print("Finished running simulator")


if __name__ == '__main__':
    main()
