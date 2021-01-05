import torch

class RSSIMap:
    def __init__(self, source, RSSIValues, coordinates):
        self.source = source
        self.RSSIValues = RSSIValues
        self.coordinates = coordinates


def CSVToRSSIMap(pathToFile):
    """
    Create an RSSIMap object from simulator output CSV
    :param pathToFile: Path to the CSV output file
    :return: RSSI Map object
    """
    # TODO: Implement

def saveRSSIMap(map, path):
    """
    Save an RSSI Map
    :param map: The RSSI map to save
    :param path: path to save map in
    """
    # TODO: Implement

def saveRSSIMap(path):
    """
    Save an RSSI Map
    :param path: path to load the map from
    :return: RSSIMap object (loaded map)
    """
    # TODO: Implement

