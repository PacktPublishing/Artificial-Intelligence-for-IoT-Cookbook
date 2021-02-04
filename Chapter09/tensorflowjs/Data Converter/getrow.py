import pickle
import pandas as pd
import numpy as np
import sys


np.set_printoptions(threshold=sys.maxsize)


seq_array = pickle.load( open( "save.p", "rb" ) )
print(len(seq_array))
one = seq_array[0].flatten()
print(len(one))

print(one)