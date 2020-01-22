import pandas as pd
import numpy as np

df = np.random.random((100, 100))
df = pd.DataFrame(df)
df.to_csv('test.csv')