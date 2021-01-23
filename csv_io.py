import io
from io import StringIO

import numpy as np
import pandas as pd

arr = np.array([1,2,3,4,5])
arr.reshape(1,-1).shape
buffer: StringIO = io.StringIO()

np.savetxt(buffer, arr, delimiter=',')
buffer.seek(0)
df = pd.read_csv(buffer, header=None)
print(df)
print(buffer.getvalue())


