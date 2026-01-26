import pandas as pd
import numpy as np

ser = pd.Series()

print("Pandas series: ", ser)

data = np.array(['g', 'e', 'e', 'k', 's'])

ser = pd.Series(data)

print("Pandas series:\n", ser)