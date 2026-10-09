import numpy as np

c = 3e8 # m/s

class Filter:
    def __init__(self, waveLength: float, msrmnts: np.array, tag: str=""):
        self.waveLength = waveLength # nm
        self.msrmnts = msrmnts
        self.tag = tag

    @property
    def mean(self):
        return np.mean(self.msrmnts)
    
    @property
    def freq(self):
        return (c / (self.waveLength * 1e-9)) / 1e14 # for 10¹⁴ in table