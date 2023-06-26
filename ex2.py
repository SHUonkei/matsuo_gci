# 以下のライブラリを使うので、あらかじめ読み込んでおいてください
import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame# 例
series = Series([1,1,2,3,5,8,13])
print(series)
# indexをアルファベットでつける
series_i = Series(
    [1,1,2,3,5,8,13],
    index=['a', 'b', 'c', 'd', 'e', 'f','g'])
print(series_i)

print('要素:', series_i.values)
print('インデックス:', series_i.index)




data = {'ID':['100','101','102','103','104'],
            'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
            'Birth_year':[1990,1989,1992,1997,1982],
            'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

df = DataFrame(data)

print(df)
print(df.head())

print(df.iloc[0:4, [0,2]])