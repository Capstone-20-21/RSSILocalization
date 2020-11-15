import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import math
import os

# Preparing/Reading output files
plottingFolder="Outputs/ToPlot/"
files = os.listdir(plottingFolder)

sources = []
configurations = []
for file in files:
    sourcePosition = file.split('(')[1].split(')')[0].split(',')
    sourcePosition = [float(i) for i in sourcePosition]
    sources.append(sourcePosition)
    config = file.split('_')
    configurations.append(f"{config[0]}_{config[1]}")

    
# XYZ Information
df = pd.read_csv(plottingFolder+files[0], sep=',', skipinitialspace=True)
x = np.array(df["X[m]"].tolist()).astype(float)
y = np.array(df["Y[m]"].tolist()).astype(float)
z = np.array(df["Z[m]"].tolist()).astype(float)


# Reading Powers
powers_per_source = []
for i, source in enumerate(sources):
    powers = []
    df = pd.read_csv(plottingFolder+files[i], sep=',', skipinitialspace=True)
    powers_raw = df["Power[dBm]"].tolist()
    for p in powers_raw:
        if isinstance(p, float):
            powers.append(p)
            continue
        if isinstance(p, int):
            powers.append(p)
            continue  
        if '-nan' in p:
            powers.append(-math.inf)
            continue
        if 'nan' in p:
            powers.append(math.inf)
            continue
        powers.append(float(p))
    
    powers = np.array(powers).astype(float)
    powers = np.nan_to_num(powers, posinf=0, neginf=np.nanmin(powers[powers != -np.inf]))
    
    powers_per_source.append(powers)
    

# Visualization
colors = ["navy", 'orangered']
colormap = matplotlib.colors.LinearSegmentedColormap.from_list('powers', colors) 
for i, source in enumerate(sources):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(x, y, z, c=powers_per_source[i], s=1, cmap=colormap, vmin=-100, vmax=0)
    ax.scatter3D(source[0],source[1],source[2], c='lime', s=20)
    ax.set_xlabel('X[m]')
    ax.set_ylabel('Y[m]')
    ax.set_zlabel('Z[m]')
    ax.set_title(f"Power Map - Source=({source[0]},{source[1]},{source[2]}) - Config={configurations[i]}")
    plt.tight_layout()
plt.show()


#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.scatter3D(x_positions, y_positions, z_positions, c=received_powers, s=1, cmap=plt.get_cmap('hot'))
#ax.scatter3D(source[0],source[1],source[2], c='b', s=20)
#ax.scatter3D(source2[0],source2[1],source2[2], c='b', s=20)
#ax.set_xlabel('X[m]')
#ax.set_ylabel('Y[m]')
#ax.set_zlabel('Z[m]')
#plt.tight_layout()
#plt.show()