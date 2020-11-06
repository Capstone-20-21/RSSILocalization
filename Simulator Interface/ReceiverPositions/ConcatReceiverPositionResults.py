import sys
import numpy as np
import argparse

def ParseArguments():
    """
    Parse the arguments needed for this function
    :return: outputFile_CC, outputFile_LC, outputFile_MC, outputFile_UC, outputFile_MR
    """
    parser = argparse.ArgumentParser(prog=sys.argv[0], description="Process script arguments")
    parser.add_argument('--filePath_connectingCorridor', metavar="FilePathCC", default="SampleReceiverPositions/ReceiverPositions_connectingCorridor.dat", help="Path to ReceiverPositions_connectingCorridor file")
    parser.add_argument('--filePath_lowerCorridor', metavar="FilePathLC", default="SampleReceiverPositions/ReceiverPositions_lowerCorridor.dat", help="Path to ReceiverPositions_lowerCorridor file")
    parser.add_argument('--filePath_mainCorridor', metavar="FilePathMC", default="SampleReceiverPositions/ReceiverPositions_mainCorridor.dat", help="Path to ReceiverPositions_mainCorridor file")
    parser.add_argument('--filePath_upperCorridor', metavar="FilePathUC", default="SampleReceiverPositions/ReceiverPositions_upperCorridor.dat", help="Path to ReceiverPositions_upperCorridor file")
    parser.add_argument('--filePath_mainRoom', metavar="FilePathMR", default="SampleReceiverPositions/ReceiverPositions_mainRoom.dat", help="Path to ReceiverPositions_mainRoom file")
    parser.add_argument('--filePath_output', metavar="FilePath", default="SampleReceiverPositions/ReceiverPositions_concat.dat", help="Path to output file")
    arguments = parser.parse_args()

    inputFile_CC = arguments.filePath_connectingCorridor
    inputFile_LC = arguments.filePath_lowerCorridor
    inputFile_MC = arguments.filePath_mainCorridor
    inputFile_UC = arguments.filePath_upperCorridor
    inputFile_MR = arguments.filePath_mainRoom
    inputFile_MR = arguments.filePath_mainRoom
    outputFile = arguments.filePath_output


    return inputFile_CC, inputFile_LC, inputFile_MC, inputFile_UC, inputFile_MR, outputFile

def main():
    print("Concatinating Receiver Position Files")
    print()

    receiverFile_CC, receiverFile_LC, receiverFile_MC, receiverFile_UC, receiverFile_MR, outputFile = ParseArguments()
    # read flash.dat to a list of lists
    CC_data = [i.strip().split() for i in open(receiverFile_CC).readlines()]
    LC_data = [i.strip().split() for i in open(receiverFile_LC).readlines()]
    MC_data = [i.strip().split() for i in open(receiverFile_MC).readlines()]
    UC_data = [i.strip().split() for i in open(receiverFile_UC).readlines()]
    MR_data = [i.strip().split() for i in open(receiverFile_MR).readlines()]

    num_of_pts = int(CC_data[1][0]) + int(LC_data[1][0]) + int(MC_data[1][0]) + int(UC_data[1][0]) + int(MR_data[1][0])

    lines = ["receiver positions", str(num_of_pts)]

    CC_data_new = CC_data[2:]
    LC_data_new = LC_data[2:]
    MC_data_new = MC_data[2:]
    UC_data_new = UC_data[2:]
    MR_data_new = MR_data[2:]

    files = [CC_data_new, LC_data_new, MC_data_new, UC_data_new, MR_data_new]

    for file in files:
        for position in file:
            xStr = position[0]
            yStr = position[1]
            zStr = position[2]
            lines.append(f" {xStr} {yStr} {zStr}")

    #print(lines)

    with open(outputFile, "w") as f:
        f.write("\n".join(lines)+"\n")



if __name__ == "__main__":
    main()
