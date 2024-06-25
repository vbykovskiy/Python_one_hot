import pandas as pd
import random

lst = (['robot'] * 10) + (['human'] * 10)
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data['i'] = 1
data = data.set_index([data.index, 'whoAmI'])
data = data.unstack(level=-1, fill_value=0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None

print(data.head(20))
