import pandas as pd
import numpy as np

# Creating data-frame
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]})
print(df)

# if-then on one column
df.loc[df.A > 5,'B'] = -1
print("\n",df)

# if-then with assignment to 2 columns
df.loc[df.A > 5, ['B','C']] = 500
print("\n",df)

# where() with mask
df_mask = pd.DataFrame({'A': [True]*4,
                        'B': [False]*4,
                        'C': [True, False]*2})
print(df.where(df_mask, -1000))

# if-then-else using where()
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]})
df['D'] = np.where(df['A'] > 5, 'high', 'low')
print("\n",df)

# Splitting
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]})
print("\n",df[df.A <= 5])
print("\n",df[df.A > 5])

# building criteria
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]})
# using and (without assignment)
print("\n",df.loc[(df['B'] < 25) & (df['C'] >= -40), 'A'])
# using or (without assignment)
print("\n",df.loc[(df['B'] > 25) & (df['C'] >= -40), 'A'])
# using or (with assignment)
df.loc[(df['B'] > 25) | (df['C'] >= 75), 'A'] = 0.1
print("\n",df)

# selecting the data closest to a given value
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]})
aValue = 43.0
print("\n",df.loc[(df.C - aValue).abs().argsort()])

# dynamically reducing a list of criteria using binary operator
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]})
Crit1 = df.A <= 5.5
Crit2 = df.B == 10.0
Crit3 = df.C > -40.0
AllCrit = Crit1 & Crit2 & Crit3
print("\n",df[AllCrit])

# selection using both row labels and value conditionals
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]})
print("\n",df[(df.A <= 6) & (df.index.isin([0, 2, 4]))])

# Slicing
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]},
                  index=['foo','bar','boo','kar'])
# Positional-oriented slicing
print("\n",df.loc['bar':'kar'])
print('\n',df.iloc[0:3])

# Inverse operator (~) to take complement of a mask
df = pd.DataFrame({'A': [4,5,6,7],
                   'B': [10,20,30,40],
                   'C': [100,50,-30,-50]})
print("\n",df[~((df.A <= 6) & (df.index.isin([0, 2, 4])))])

# Creating new columns using applymap
df = pd.DataFrame({'A': [1,2,1,3],
                   'B': [1,1,2,2],
                   'C': [2,1,3,1]})
source_cols = df.columns
new_cols = [str(x) + "_cat" for x in source_cols]
categories = {1: 'Alpha', 2: 'Beta', 3: 'Charlie'}
df[new_cols] = df[source_cols].applymap(categories.get)
print('\n',df)

# using min() with groupby
df = pd.DataFrame({'A': [1,1,1,2,2,2,3,3],
                   'B': [2,1,3,4,5,1,2,3]})
# idxmin() to get the index of the minimums
print('\n',df.loc[df.groupby("A")["B"].idxmin()])
# sort then take first of each
print('\n',df.sort_values(by="B").groupby("A", as_index=False).first())
