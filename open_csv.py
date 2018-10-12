import sys
import pandas as pd
import numpy as np
import os 

readfile = sys.argv[1]

data = pd.read_csv(sys.argv[1])
print(data)
