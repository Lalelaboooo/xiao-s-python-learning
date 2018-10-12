import pandas as pd
import numpy as np
import sys
input_file = sys.argv[1]

data = pd.read_csv(input_file)
print(data)

data.to_pickle('student_pickle.pickle')
