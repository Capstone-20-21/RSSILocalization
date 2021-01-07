import torch
import numpy as np
import pandas as pd
from itertools import repeat

class RSSIMap:
    def __init__(self, source, RSSIValues):
      self.source = source
      self.RSSIValues = RSSIValues

    def add_noise(self, noise=1):
      if noise == 1:
        self.RSSIValues['Power[dBm]'] = self.RSSIValues['Power[dBm]'] + 1
      else:
        self.RSSIValues['Power[dBm]'] = self.RSSIValues['Power[dBm]'] - 1
        
    def zero_pad(self):
      x_pos = self.RSSIValues['X[m]'].to_list() # retrieve coordinates which have power values from map
      y_pos = self.RSSIValues['Y[m]'].to_list()

      coords = list(zip(x_pos, y_pos)) # all coordinates
      unique_coords = sorted(set(coords), key=coords.index) # unique coordinates
      missing_coords = []

      for i in np.arange(min(x_pos), max(x_pos)+0.5, 0.5): # all x positions existing in dataset
        for j in np.arange(min(y_pos), max(y_pos)+0.5, 0.5): # all y positions existing in dataset
          pair = (i, j)
          if pair not in unique_coords:
            missing_coords.append(pair)
      
      missing_x, missing_y = zip(*missing_coords)
      missing_entries = list(zip(missing_x, missing_y, ['z']*len(missing_coords), [0.0]*len(missing_coords)))
      missing_entries = [list(entry) for entry in missing_entries]

      # must duplicate each coordinate entry for every z value (there are 6)
      duplicated_entries = [x for item in missing_entries for x in repeat(item, 6)]
      z = [1.00, 1.25, 1.5, 1.75, 2.00, 2.25] * len(missing_entries)

      new_entries = []
      for i, entry in enumerate(duplicated_entries):
          cpy = entry.copy() # work around due to pointers created through repeat
          cpy[2] = z[i]
          new_entries.append(cpy)
          i+=1

      new_entries = pd.DataFrame(new_entries)
      new_entries.columns = ['X[m]', 'Y[m]', 'Z[m]', 'Power[dBm]']

      self.RSSIValues = self.RSSIValues.append(new_entries, ignore_index=True)

def CSVToRSSIMap(pathToFile):
    """
    Create an RSSIMap object from simulator output CSV
    :param pathToFile: Path to the CSV output file
    :return: RSSI Map object
    """
    df = pd.read_csv(pathToFile, sep=',', skipinitialspace=True) # read CSV file

    src_start_idx = pathToFile.index('(') # extract source positions from file name
    src_end_idx = pathToFile.index(')')
    source_positions = pathToFile[src_start_idx+1:src_end_idx]
    source_positions = source_positions.split(',') # transform source positions string into a list of floats
    source_positions = list(map(float, source_positions))

    RSSIValues = df[['X[m]', 'Y[m]', 'Z[m]', 'Power[dBm]']]
    RSSIValues = RSSIValues.apply(pd.to_numeric, errors='coerce') # convert data from string to float

    # RSSIValues = RSSIValues.fillna(0) # SIMPLE WAY (just zero it out)
    # better: interpolate nan values; method TBD!
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate
    RSSIValues = RSSIValues.interpolate(method='nearest')

    rssi_map = RSSIMap(source_positions, RSSIValues)

    return rssi_map

def saveRSSIMap(map, path):
    """
    Save an RSSI Map
    :param map: The RSSI map to save
    :param path: path to save map in
    """
    # TODO: Implement

def loadRSSIMap(path):
    """
    load an RSSI Map
    :param path: path to load the map from
    :return: RSSIMap object (loaded map)
    """
    # TODO: Implement
