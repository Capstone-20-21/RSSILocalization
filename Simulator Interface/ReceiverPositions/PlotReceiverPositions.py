from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np



def PlotReceiverPositions(receiverPositions):
    x, y, z = [], [], []
    for position in receiverPositions:
        x.append(position.x)
        y.append(position.y)
        z.append(position.z)

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.scatter(x, y, z)
    plt.show()


