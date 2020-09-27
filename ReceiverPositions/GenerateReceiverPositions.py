import sys
import numpy as np
from PlotReceiverPositions import PlotReceiverPositions

firstLine = "receiver positions"
scriptForm = "GenerateReceiverPositions.py x1, y1, z1, x2, y2, z2 (numXPoints) (numYPoints) (numZPoints)"
outputFile = "ReceiverPositions.dat"

minNumArguments = 6
maxNumArguments = 9

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z



def parseArguments(args):
    """
    Parse the arguments needed for this function
    :param args: arguments from sys.argv (includes file name)
    :return: (point1, point2, numPoints) - 3D vectors
    """
    numArguments = len(args)

    if numArguments == 1 or numArguments-1 < minNumArguments or numArguments-1 > maxNumArguments:
        print("ERROR - Too few arguments")
        print(f"Correct Form: {scriptForm}")
        sys.exit(-1)

    args = args[1:]
    numArguments = len(args)

    for i, argument in enumerate(args, 1):
        print(f"  Arg {i} - {argument}")
    print()

    point1 = Vector3(float(args[0]), float(args[1]), float(args[2]))
    point2 = Vector3(float(args[3]), float(args[4]), float(args[5]))
    if (point1 == point2):
        print("ERROR - Points are identical")
        sys.exit(-1)

    numPoints = Vector3(2, 2, 2)
    if numArguments > 6:
        numPoints.x = int(args[6])
    if numArguments > 7:
        numPoints.y = int(args[7])
    if numArguments > 8:
        numPoints.z = int(args[8])

    if numPoints.x < 2 or numPoints.y < 2 or numPoints.z < 2:
        print("ERROR - Too few points, minimum = 2")
        sys.exit(-1)

    return point1, point2, numPoints


def GenerateReceiverPositions(point1, point2, numPoints):
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

    receiverPositions = []
    for x in xPoints:
        for y in yPoints:
            for z in zPoints:
                receiverPositions.append(Vector3(x,y,z))

    return receiverPositions


def GenerateFile(receiverPositions):
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

    with open(outputFile, "w") as f:
        f.write("\n".join(lines)+"\n")

    return outputFile


if __name__=="__main__":
    arguments = sys.argv

    print("GenerateRecieverPositions.py:")
    print()

    point1, point2, numPoints = parseArguments(arguments)

    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Step: {numPoints}")
    print()

    receiverPositions = GenerateReceiverPositions(point1, point2, numPoints)
    fileName = GenerateFile(receiverPositions)

    print(f"File Generated - {fileName}")

    PlotReceiverPositions(receiverPositions)

    sys.exit(0)