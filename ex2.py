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



print("next section -------------")
data = {
        'ID':['100','101','102','103','104'],
        'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
        'Birth_year':[1990,1989,1992,1997,1982],
        'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']
        }
#data は　dict


df = DataFrame(data)

print(df)

print("section")
print(df.head())
print("section")
print(df.iloc[0:4, [0,2]])

print(df.iloc[0:4,[0,1]])
print(DataFrame({10:[2],20:[3],30:[5]}))
#{key:velue(= list)}
#っだったらddataframeに入るのか



# webからデータを取得したり、zipファイルを扱うためのライブラリ
import requests, zipfile
from io import StringIO
import io

# データがあるurlの指定
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'

# # データをurlから取得する
# r = requests.get(url, stream=True)

# # zipfileを読み込み展開する
# z = zipfile.ZipFile(io.BytesIO(r.content))
# z.extractall()

student_data_math = pd.read_csv('student-mat.csv')
print(student_data_math.head())

# データの読み込み
# 区切りに";"がついているので注意
student_data_math = pd.read_csv('student-mat.csv', sep=';')
student_data_math.head()
print(student_data_math)

#print(?pd.read_csv)

# すべてのカラムの情報等チェック
print(student_data_math.info())

# 基本統計量をチェック
print(student_data_math.describe())

# 転置
df.T
print(df)
print(df.T)

# 列名の指定（1つの場合）
print(df['Birth_year'])
print(df.Birth_year)
#jsみたいだな
print(df.iloc[1])
# 列名の指定(複数の場合)
print(df[['ID', 'Birth_year']])

#numpyのndarrayっぽい


# 新しい列の作成
df['Score'] = np.arange(5)*10
print(df)


# 行名の指定
print(df[0:3])