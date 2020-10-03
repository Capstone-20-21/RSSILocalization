import sys
import numpy as np
import argparse
from PlotReceiverPositions import PlotReceiverPositions
from ast import literal_eval

firstLine = "receiver positions"

'''
Sample Usage:

python GenerateReceiverPositions.py (0,-1.5,0) (50,1.5,4) --numX 101 --numY 7 --numZ 9 --filePath 
"SampleReceiverPositions/ReceiverPositions__0_-1.5_0__50_1.5_4__101_7_9.dat" 

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


def ParseArguments():
    """
    Parse the arguments needed for this function
    :return: (point1, point2, numPoints) - 3D vectors
    """
    parser = argparse.ArgumentParser(prog=sys.argv[0], description="Process script arguments")
    parser.add_argument('point1', type=Vector3, metavar="Point1", help="Bottom Left Point")
    parser.add_argument('point2', type=Vector3, metavar="Point2", help="Top Right Point")
    parser.add_argument('--numX', type=int, metavar="NumX", default=2, help="Number of x locations to split by")
    parser.add_argument('--numY', type=int, metavar="NumY", default=2, help="Number of y locations to split by")
    parser.add_argument('--numZ', type=int, metavar="NumZ", default=2, help="Number of z locations to split by")
    parser.add_argument('--plot', nargs="?", metavar="Plot", const=True, default=False, help="Should display plot of receiver positions")
    parser.add_argument('--print', nargs="?", metavar="Print", const=True, default=False, help="Should print receiver positions")
    parser.add_argument('--noSave', nargs="?", metavar="NoSave", const=True, default=False, help="Should write receiver positions in receiverPositions.dat")
    parser.add_argument('--filePath', metavar="FilePath", default="receiverPositions.dat", help="Path to file")
    arguments = parser.parse_args()

    point1 = arguments.point1
    point2 = arguments.point2

    numX = arguments.numX if arguments.numX is not None else 2
    numY = arguments.numY if arguments.numY is not None else 2
    numZ = arguments.numZ if arguments.numZ is not None else 2
    numPoints = Vector3(numX, numY, numZ)

    return point1, point2, numPoints, {"plot": arguments.plot, "print": arguments.print, "noSave": arguments.noSave, "file": arguments.filePath}


def GenerateReceiverPositions(point1, point2, numPoints, printPositions=False):
    """
    Generate the receiver positions in a rectangle
    :param point1: Bottom left corner
    :param point2: Top right corner
    :param numPoints: Number of points in each dimension
    :return: receiver positions - List of Vecotr3
    """

    xPoints = np.linspace(point1.x, point2.x, numPoints.x) if point1.x != point2.x else [point1.x]
    yPoints = np.linspace(point1.y, point2.y, numPoints.y) if point1.y != point2.y else [point1.y]
    zPoints = np.linspace(point1.z, point2.z, numPoints.z) if point1.z != point2.z else [point1.z]

    if printPositions:
        print("Receiver Positions (x y z):")
    receiverPositions = []
    for x in xPoints:
        for y in yPoints:
            for z in zPoints:
                receiverPositions.append(Vector3(x,y,z))
                if printPositions:
                    print(f"  {receiverPositions[-1]}")

    if printPositions:
        print()

    return receiverPositions


def GenerateFile(receiverPositions, fileName="ReceiverPositions.dat"):
    """
    Generate a file containing the receiver positions
    :param receiverPositions: List of receiver positions
    """
    lines = [firstLine, str(len(receiverPositions))]
    for position in receiverPositions:
        xStr = int(position.x) if position.x.is_integer() else "{:.6e}".format(position.x)
        yStr = int(position.y) if position.y.is_integer() else "{:.6e}".format(position.y)
        zStr = int(position.z) if position.z.is_integer() else "{:.6e}".format(position.z)
        lines.append(f" {xStr} {yStr} {zStr}")

    with open(fileName, "w") as f:
        f.write("\n".join(lines)+"\n")

    return fileName


if __name__ == "__main__":
    print("GenerateRecieverPositions.py:")
    print()

    point1, point2, numPoints, optionals = ParseArguments()

    print(f"Point 1 (x y z): {point1}")
    print(f"Point 2 (x y z): {point2}")
    print(f"Number of Points (x y z): {numPoints}")
    print()

    receiverPositions = GenerateReceiverPositions(point1, point2, numPoints, printPositions=optionals["print"])
    if not optionals["noSave"]:
        fileName = GenerateFile(receiverPositions, fileName=optionals["file"])
        print(f"File Generated - {fileName}")

    if optionals["plot"]:
        PlotReceiverPositions(receiverPositions)