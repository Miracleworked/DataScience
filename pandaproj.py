import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')

#Object creation
print("\n- - - Object creation - - -")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df2 = pd.DataFrame({'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'})

#Viewing data
print("\n- - - Viewing data - - -")
print(s.to_numpy())

#Selection
print("\n- - - Selection - - -")
print(df.loc[dates[0]])
print(df.iloc[5])

#Operations
print("\n- - - Operations - - -")
print(df.apply(np.cumsum))

#Merge
print("\n- - - Merge - - -")
print(df.append(s, ignore_index=True))

#Grouping
print("\n- - - Grouping - - -")
print(df.groupby('C').sum())

#Reshaping
print("\n- - - Reshaping - - -")
print(df2.stack())

#Time Series
print("\n- - - Time Series - - -")
rng = pd.date_range('1/1/2013 00:00', periods=6, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts.tz_localize('Australia/Sydney'))

#Plotting
print("\n- - - Plotting - - -")
cs = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#print(cs.plot())
cs.plot();
df.plot();

#Getting Data In Out (csv)
#print("\n- - - Getting Data In Out (csv) - - -")
