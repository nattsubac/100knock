# %% [markdown]
# # 初学者向けPandas100本ノックver1.0.7
# ##### Shift + Enter で各セルのコードが実行されます
# ・print(ans[ 問題番号 ]) で回答コード例を表示  
# ・Python3エンジニア認定データ分析試験にも沿った問題内容   
# ・Pandasの各メソッドの説明は以下のサイトが分かりやすいです  
#  　[note.nkmk.me](https://note.nkmk.me/pandas/)  
# ・"Data for Titanic passengers" from [VANDERBILT UNIVERSITY](https://biostat.app.vumc.org/wiki/Main/DataSets)  
#   
# **本コンテンツ作成時のpandasのバージョンは1.1.0**
#   
# 作成日:2020年9月24日  
# 最終更新日:2023年1月16日  
# 再配布・改編不可  
# 作成者：[kunishou](https://qiita.com/kunishou)

# %%
# Shift + Enterで題材データ、回答コードを読み込んで下さい

import pandas as pd
import glob

#題材データをdfに読み込み(タイタニック号の乗客データ、テストの点数データ 等)
def initialize1():
    df = pd.read_csv('../input/titanic3.csv')
    return df

def initialize2():
    df = pd.read_csv('../input/data1.csv')
    return df

df = initialize1()
df2 = initialize2()
df3 = pd.read_csv('../input/data1_2.csv')
df4 = pd.read_csv('../input/data1_3.csv')
df5 = pd.read_csv('../input/data2.csv',encoding='cp932')

#回答コードをansリストに格納
path = sorted(glob.glob('../input/a_' + '*.txt'))

ans = []

for _ in range(len(path)):
    with open(path[_], 'r',encoding='utf-8') as f:
        ans.append(f.read())
        
print(ans[0])

# %% [markdown]
# # Pandas基礎 (1 - 13)

# %%
# 【1】
# dfに読み込んだデータの最初の5行を表示
#print(ans[1]) #回答表示
df = initialize1() #初期化
df.head(5)
# %%
# 【2】
# dfに読み込んだデータの最後の5行を表示
#print(ans[2]) #回答表示
df = initialize1() #初期化
df.tail(5)
# %%
# 【3】
# dfのDataFrameサイズを確認
#print(ans[3]) #回答表示
df = initialize1() #初期化
df.shape
print(ans[3])
# %%
# 【4】
# inputフォルダ内のdata1.csvファイルを
# 読み込みdf2に格納して、最初の5行を表示
#print(ans[4]) #回答表示
df2 = pd.read_csv("../input/data1.csv")
df2.head(5)
print(ans[4])
# %%
# 【5】
# dfのfareの列で昇順に並び替えて表示
#print(ans[5]) #回答表示
df = initialize1() #初期化
df["fare"].sort_values()

print(ans[5])
# %%
# 【6】
# df_copyにdfをコピーして、最初の5行を表示
#print(ans[6]) #回答表示
df = initialize1() #初期化
df_copy = df.copy()
df_copy.head()
# %%
# 【7】
# ① dfの各列のデータ型を確認
# ② dfのcabinの列のデータ型を確認
#print(ans[7]) #回答表示
df = initialize1() #初期化
print(df.dtypes)
print(df["cabin"].dtype)

# %%
# 【8】
# ① dfのpclassの列のデータ型をdtypeで確認
# ② 数値型から文字型に変換し、データ型をdtypeで確認
#print(ans[8]) #回答表示
df = initialize1() #初期化
print(df["pclass"].dtype)
df["pclass"] = df["pclass"].to_string()
print(df["pclass"].dtype)

# to_string()がDataFrameやシリーズを文字列に変換するメソッド、astype()はデータ内部のデータ型を変換する。後者が安全
df = initialize1() #初期化
print(df["pclass"].dtype)
df["pclass"] = df["pclass"].astype(str)
print(df["pclass"].dtype)

# %%
# 【9】
# dfのレコード数(行数)を確認
#print(ans[9]) #回答表示
df = initialize1() #初期化
len(df)

# %%
# 【10】
# dfのレコード数(行数)、各列のデータ型、欠損値の有無を確認
#print(ans[10]) #回答表示
df = initialize1() #初期化
len(df)
print(df.dtypes)
df.isnull().sum

#全容確認
df.info()
# %%
# 【11】
# dfのsex,cabinの列の要素を確認
#print(ans[11]) #回答表示
df = initialize1() #初期化
df[["sex","cabin"]]

#要素（Feature）とは中に文字列の一覧であるかも
print(df["sex"].unique())
print(df["cabin"].unique())
# %%
# 【12】
# dfの列名一覧をlist形式で表示
#print(ans[12]) #回答表示
df = initialize1() #初期化
df.columns

#リスト化するためにはtolist()
df.columns.tolist()
# %%
# 【13】
# dfのインデックス一覧をndaaray形式で表示
#print(ans[13]) #回答表示
df = initialize1() #初期化#
arr = df.columns.to_numpy()
arr

#インデックスを一覧表示、valuesでndaaray形式に変換
print(df.index) # indexの始値start,終値stop,間隔step
print(df.index.values) # ndaarayに変換
print(df.columns) # 列名を表示、行名がindex
print(df.index.tolist()) #indexをリスト化

#列名はcolumns、行名はindexという命名なのかもね

# %% [markdown]
# # データ抽出 (14 - 32)

# %%
# 【14】
# dfのnameの列のみ表示
#print(ans[14]) #回答表示
df = initialize1() #初期化
df["name"]
# %%
# 【15】
# dfのnameとsexの列のみ表示
#print(ans[15]) #回答表示
df = initialize1() #初期化
df[["name", "sex"]]

# %%
# 【16】
# dfのindex(行)の4行目までを表示
#print(ans[16]) #回答表示
df = initialize1() #初期化
df[0:4]

#最初はしょうりゃくしてもOK 
df[:4]

# %%
# 【17】
# dfのindex(行)の4行目から10行目までを表示
#print(ans[17]) #回答表示
df = initialize1() #初期化
df[3:10]

#始値はindexと同じ値、終値は目的の行
# %%
# 【18】
# locを使ってdf全体を表示
#print(ans[18]) #回答表示
df = initialize1() #初期化
df.loc[:,:]

df
# %%
# 【19】
# locを使ってdfのfare列をすべて表示
#print(ans[19]) #回答表示
df = initialize1() #初期化
df["fare"].loc[:]

#こっちがきれい
df.loc[:,"fare"]

# %%
# 【20】
# locを使ってdfのfare列の10のラベルまで表示
#print(ans[20]) #回答表示
df = initialize1() #初期化
df.loc[:10,"fare"]

# %%
# 【21】
# locを使ってdfのnameとticketの列をすべて表示
#print(ans[21]) #回答表示
df = initialize1() #初期化
df.loc[:,["name","ticket"]]

#loc[行, 列]の法則。カンマ左に行の指定、すなわちインデックス番号を指定し、カンマ右に列の指定、つまり列名を入力する。

# %%
# 【22】
# locを使ってdfのnameからcabinまでの列をすべて表示
#print(ans[22]) #回答表示
df = initialize1() #初期化
df.loc[:,"name":"cabin"]

#スライスの情報は単一のワードとなる

# %%
# 【23】
# ilocを使ってdfのage列を5行目まで表示
#print(ans[23]) #回答表示
df = initialize1() #初期化

#locが行番号と列名でしていしてたのに対し、ilocは行番号と列番号で指定する。
age_index = df.columns.tolist().index("age")
df.iloc[:5, age_index]

# %%
# 【24】
# dfのname,age,sexの列のみ抽出しdf_copyに格納
# その後outputフォルダにcsvファイルで出力
# 出力ファイル名はsample.csv
#print(ans[24]) #回答表示
df = initialize1() #初期化
df_copy = df[["name","age","sex"]].copy()

#pd.read_csvに対するto_csv
df_copy.to_csv("../output/sample.csv")

#行番号、列名を削除したいときはindex=None, header=Noneをつける

# %%
# 【25】
# dfのage列の値が30以上のデータのみ抽出
#print(ans[25]) #回答表示
df = initialize1() #初期化
df.loc[df["age"] >= 30, "age"]

#列指定は省略しても良い
df[df["age"] >= 30]

#一列になるとSeries形式になる

# %%
# 【26】
# dfのsex列がfemaleのデータのみ抽出
#print(ans[26]) #回答表示
df = initialize1() #初期化
df[df["sex"] == "female"]
# %%
# 【27】
# dfのsex列がfemaleでかつageが40以上のデータのみ抽出
#print(ans[27]) #回答表示
df = initialize1() #初期化
df[df["sex"] == "female" & df["age"] >= 40]

#丸括弧を指定し、&より括弧の中身を先に計算させる、&をandに帰るとエラー、&は各行にそれぞれ使われるようになr
df[(df["sex"] == "female") & (df["age"] >= 40)]
# %%
# 【28】
# queryを用いてdfのsex列がfemaleでかつageが40以上のデータのみ抽出
#print(ans[28]) #回答表示
df = initialize1() #初期化

df.query('sex == "female" and age >= 40')

#queryを使うのは、可読性を高めるため。個人的な推測だが、変数を入れるのは苦手そう。f"
# %%
# 【29】
# dfのname列に文字列「Mrs」が含まれるデータを表示
#print(ans[29]) #回答表示
df = initialize1() #初期化
df.query('"Mrs" in name')

#完全一致判定になって意しまっている。in,queryなら以下の通り
df.query('name.str.contains("Mrs")', engine='python')

#query()つかわなくともいける
df[df["name"].str.contatins("Mrs", na=False, regex=False)]

# %%
# 【30】
# dfの中で文字列型の列のみを表示
#print(ans[30]) #回答表示
df = initialize1() #初期化
df["str" in df.dtypes]

#select_dtypesを使用して特定データ型の列を抽出
df.select_dtypes(include='str')

#逆に特定データ型を除外なら
df.select_dtypes(exclude='object')
# %%
# 【31】
# dfの各列の要素数の確認
#print(ans[31]) #回答表示
df = initialize1() #初期化
#考え: .indexだと、
df.count()

#こたえはnunique()は種類数を出す。本問題の要素数は種類の数を意味する。
df.nunique()
# %%
# 【32】
# dfのembarked列の要素と出現回数の確認
#print(ans[32]) #回答表示
df = initialize1() #初期化
df["embarked"].nunique()

#上だと種類の数を出す。
#方針: 要素をそれぞれリスト化　、リストを引数として出現回数を出す。
df["embarked"].value_counts()

# %% [markdown]
# # データ加工 (33 - 58)

# %%
# 【33】
# dfのindex名が「3」のage列を
# 30から40に変更し、先頭の5行を表示
#print(ans[33]) #回答表示
df = initialize1() #初期化
df.loc[3, "age"] = 40
df.loc[3, "age"]


# %%
# 【34】
# dfのsex列にてmale→0、femlae→1に
# 変更し、先頭の5行を表示
#print(ans[34]) #回答表示
df = initialize1() #初期化

#わからなかった。方針：エクセルのif関数のような処理ができたらいいのかな。
#リストで取り出し、forで回してlist作り、dfに戻す。置換方法がわからないのだが・・・
df["sex"].value_counts()
df_bool_sex = []
for sex in df["sex"].tolist():
    if sex == "male":
        df_bool_sex.append(0)
    elif sex == "female":
        df_bool_sex.append(1)
df_bool_sex
df["sex"] = df_bool_sex
df["sex"]
df["sex"].value_counts()

#回答
df = initialize1() #初期化
df['sex'][df['sex'] == 'male'] = 0
df['sex'][df['sex'] == 'female'] = 1
df.head()
#別解
df = initialize1() #初期化
df['sex'] = df['sex'].replace({'male' : 0, 'female' : 1})
df['sex'].value_counts()
# %%
# 【35】
# dfのfare列に100を足して、
# 先頭の5行を表示
#print(ans[35]) #回答表示
df = initialize1() #初期化
df.head()
df["fare"] += 100
df.head()
# %%
# 【36】
# dfのfare列に2を掛けて、
# 先頭の5行を表示
#print(ans[36]) #回答表示
df = initialize1() #初期化
df["fare"] = df["fare"] * 2
df.head()
# %%
# 【37】
# dfのfare列を小数点以下で丸めて、先頭の5行を表示
#print(ans[37]) #回答表示
df = initialize1() #初期化
df['fare'] = df['fare'].round()
df.head()

#.round(n)は、小数点n桁で丸める。丸めるとは、その桁まで表示すると言うこと。つまり、小数点n+1桁を四捨五入し、小数点n桁まで表示する。

# %%
# 【38】
# dfに列名「test」で値がすべて1の
# カラムを追加し、先頭の5行を表示
#print(ans[38]) #回答表示
df = initialize1() #初期化
df["test"] = 1
df.head()

# %%
# 【39】
# dfにcabinとembarkedの列を「_」で
# 結合した列を追加(列名は「test」)し、
# 先頭の5行を表示
#print(ans[39]) #回答表示
df = initialize1() #初期化
df["test"] = df["cabin"]+"_"+df["embarked"]
df.head()

#正解だった。別解は以下の通り。
df['test'] = df['cabin'].str.cat(df['embarked'], sep='_')
df.head()
# %%
# 【40】
# dfにageとembarkedの列を「_」で
# 結合した列を追加(列名は「test」)し、
# 先頭の5行を表示
#print(ans[40]) #回答表示
df = initialize1() #初期化

# %%
# 【41】
# dfからbodyの列を削除し、最初の5行を表示
#print(ans[41]) #回答表示
df = initialize1() #初期化
df = df.drop('body', axis=1)
df.head()

#df.drop()の状態では、df内にNaNの状態で格納される。NaNのSeriesは新たなdfに入れた時に、自然に削除されるみたいだ。

# %%
# 【42】
# dfからインデックス名「3」の行を削除し、最初の5行を表示
#print(ans[42]) #回答表示
df = initialize1() #初期化
df = df.drop(3, axis=0)
df.head()

# %%
# 【43】
# df2の列名を'name', 'class', 'Biology', 'Physics', 'Chemistry'に変更
# df2の最初の5行を表示
#print(ans[43]) #回答表示
df2 = initialize2() #初期化
df2 = df2.rename(columns={'English':'Biology', 'Mathematics':'Physics', 'History':'Chemistry'})
df2

#別解
df2 = initialize2() #初期化
df2.columns = ['name', 'class', 'Biology', 'Physics', 'Chemistry']
df2
# %%
# 【44】
# df2の列名を'English'をBiology'に変更
# df2の最初の5行を表示
#print(ans[44]) #回答表示
df2 = initialize2() #初期化
df2 = df2.rename(columns={'English':'Biology'})
df2
# %%
# 【45】
# df2のインデックス名「1」を「10」に変更
# df2の最初の5行を表示
#print(ans[45]) #回答表示
df2 = initialize2() #初期化
df2.rename(index={1:10})


# %%
# 【46】
# dfのすべての列の欠損値数を確認
#print(ans[46]) #回答表示
df = initialize1() #初期化
df.isna().sum()

#isnullでもisnaも同じらしい

# %%
# 【47】
# dfのage列の欠損値に30を代入
# その後、ageの欠損値数を確認
#print(ans[47]) #回答表示
df = initialize1() #初期化
df['age'].isna().sum()
df.loc[df["age"].isna(), "age"] = 30
df['age']

#欠損値の補完にはfillnaをしよう
df = initialize1()
df['age'] = df['age'].fillna(30)
df['age'].isnull().sum()

# %%
# 【48】
# dfでひとつでも欠損値がある行を削除
# その後、dfの欠損値数を確認
#print(ans[48]) #回答表示
df = initialize1() #初期化
#わからん、方針を考えようか
#indexごとにNaNのsumを出し、>=1であればdropする。みたいな感じ？
#df.drop(df.isna().sum(axis=1) >= 1,axis=0)
#df
#ヒントもらった
df = df.dropna()
df.isna().sum()
# %%
# 【49】
# dfのsurvivedの列をndarray形式(配列)で表示
#print(ans[49]) #回答表示
df = initialize1() #初期化
arr = df['survived'].to_numpy()
arr
#別解
df = initialize1()
df['survived'].values

#あそび
df = initialize1()
df.to_numpy()
# %%
# 【50】
# dfの行をシャッフルして表示
#print(ans[50]) #回答表示
df = initialize1() #初期化
df.sample(frac=1)
#標本を取り出す、と言う意味でサンプルらしい。
#毎回同じ順にしたければ、引数random=nとし、indexを振り直す場合もまた引数をいれるといい。

# %%
# 【51】
# dfの行をシャッフルし、インデックスを振り直して表示
#print(ans[51]) #回答表示
df = initialize1() #初期化
df.sample(frac=1).reset_index()
# %%
# 【52】
# ①df2の重複行数をカウント
# ②df2の重複行を削除し、df2を表示
#print(ans[52]) #回答表示
df2 = initialize2() #初期化
df2.drop_duplicates()
# %%
# 【53】
# dfのnameの列をすべて大文字に変換し表示
#print(ans[53]) #回答表示
df = initialize1() #初期化
df['name'].str.upper()
# %%
# 【54】
# dfのnameの列をすべて小文字に変換し表示
#print(ans[54]) #回答表示
df = initialize1() #初期化
df['name'].str.lower()
# %%
# 【55】
# dfのsex列に含まれる「female」という単語を
# 「Python」に置換。その後、1行目の
# 「female」が「Python」に置き換わったことを確認
#print(ans[55]) #回答表示
df = initialize1() #初期化
df['sex'] =df['sex'].replace('female','Python')
df.head(1)
# %%
# 【56】
# dfのname列1行目の「Allen, Miss. Elisabeth Walton」の
# 「Elisabeth」を消去(import reをインポート)
#print(ans[56]) #回答表示
df = initialize1() #初期化
import re #reは正規表現モジュール、なるほど理解
df.loc[0,'name'] = re.sub("Elisabeth", "", df.loc[0,"name"])
df

# dfの使い方、df[列名]でSeriesとなり、そこに[行番号]でセル指定できる。
# 別解
df['name'][0] = re.sub('Elisabeth', '', df['name'][0])
df['name'][0]
# %%
# 【57】
# df5の都道府県列と市区町村列を空白がないように
# 「_」で結合(新規列名は「test2」)し、先頭5行を表示
# ※df5の「test」列は通常通り結合した場合の結果
#print(ans[57]) #回答表示
df5 = pd.read_csv('../input/data2.csv',encoding='cp932')
df5
df5['test2'] = df5['都道府県'].str.strip()+"_"+df5['市区町村'].str.strip()
df5
# %%
# 【58】
# df2の行と列を入れ替えて表示
#print(ans[58]) #回答表示
df2 = initialize2() #初期化
df2.T
# %% [markdown]
# # マージと連結(59 - 65)

# %%
# 【59】
# df2にdf3を左結合（結合キーはname）し、df2に格納
#print(ans[59]) #回答表示
df2 = initialize2() #初期化
df2 = pd.merge(df2, df3, how='left', on='name')
df2

# %%
# 【60】
# df2にdf3を右結合（結合キーはname）し、df2に格納
#print(ans[60]) #回答表示
df2 = initialize2() #初期化
df2 = pd.merge(df2, df3, how='right', on='name')
df2
# %%
# 【61】
# df2にdf3を内部結合（結合キーはname）し、df2に格納
#print(ans[61]) #回答表示
df2 = initialize2() #初期化
df2.merge(df3, on="name")

# %%
# 【62】
# df2にdf3を外部結合し、df2に格納
#print(ans[62]) #回答表示
df2 = initialize2() #初期化
df2.merge(df3, how='outer', on="name")
# %%
# 【63】
# df2とdf4を列方向に連結し、df2に格納
#print(ans[63]) #回答表示
df2 = initialize2() #初期化
df2 = pd.concat([df2, df4], axis=1)
df2

# %%
# 【64】
# df2とdf4を列方向に連結後、重複している
# name列の片方を削除し、df2に格納
#print(ans[64]) #回答表示
df2 = initialize2() #初期化
df2 = pd.concat([df2, df4], axis=1)
df2 = df2.loc[:, ~df2.columns.duplicated()]
df2

#~はPandas中のnot演算である
# %%
# 【65】
# df2とdf4を行方向に連結し、df2に格納
#print(ans[65]) #回答表示
df2 = initialize2() #初期化
df2 = pd.concat([df2, df4], axis=0)
df2

# %% [markdown]
# # 統計 (66 - 79)

# %%
# 【66】
# dfのage列の平均値を確認
#print(ans[66]) #回答表示
df = initialize1() #初期化
df['age'].mean()

# %%
# 【67】
# dfのage列の中央値を確認
#print(ans[67]) #回答表示
df = initialize1() #初期化
df['age'].median()

# %%
# 【68】
# ①df2の生徒ごとの合計点（行方向の合計）
# ②df2の科目ごとの点数の総和（列方向の合計）
#print(ans[68]) #回答表示
df2 = initialize2() #初期化
#①
df2.sum(axis=0)

#②
kamoku = ['English', 'Mathematics', 'History']
df2[kamoku].sum(axis=1)

# %%
# 【69】
# df2のEnglishで得点の最大値
#print(ans[69]) #回答表示
df2 = initialize2() #初期化
df2['English'].max()
# %%
# 【70】
# df2のEnglishで得点の最小値
#print(ans[70]) #回答表示
df2 = initialize2() #初期化
df2['English'].min()
# %%
# 【71】
# df2においてclassでグルーピングし、クラスごとの科目の
# 最大値、最小値、平均値を求める(name列は削除しておく)
#print(ans[71]) #回答表示
df2 = initialize2() #初期化
df2 = df2.drop('name',axis=1)
df2_class_1 = df2[df2['class'] == 1][kamoku]
df2_class_2 = df2[df2['class'] == 2][kamoku]
def SampleStatics (df):
    arr = []
    for ID in kamoku:
        a = df[ID].max()
        b = df[ID].min()
        c = df[ID].mean()
        arr.append([a,b,c])
    return arr
arr_class_1 = pd.DataFrame(SampleStatics(df2_class_1), columns=['max','min','mean']).T
arr_class_2 = pd.DataFrame(SampleStatics(df2_class_2), columns=['max','min','mean']).T
arr_class_1.columns = kamoku
arr_class_2.columns = kamoku
print('class1', arr_class_1)
print('class2', arr_class_2)
#これだと、

#別解
df2 = initialize2() #初期化
df2 = df2.drop('name',axis=1)
print(df2.groupby('class').max())
print(df2.groupby('class').min())
print(df2.groupby('class').mean())

# %%
# 【72】
# dfの基本統計量を確認(describe)
#print(ans[72]) #回答表示
df = initialize1() #初期化
df.describe()
# %%
# 【73】
# dfの各列間の(Pearson)相関係数を確認
#print(ans[73]) #回答表示
df = initialize1() #初期化
df.corr(method="pearson", numeric_only=True)
#corr()
df = initialize1()
df.corr()
# %%
# 【74】
# scikit-learnを用いてdf2のEnglish、Mathematics、History列を標準化する
# (from sklearn.preprocessing import StandardScalerをインポート)
#print(ans[74]) #回答表示
df2 = initialize2() #初期化
df2 = df2.drop(['name','class'],axis=1) #不要列の削除

#標準化定義
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df2)

#変換とデータフレームへの置換
scaler.transform(df2)
df2_std = pd.DataFrame(scaler.transform(df2), columns=df2.columns)

df2_std.describe() # stdが等しくなっていることを確認

# %%
# 【75】
# scikit-learnを用いてdf2のEnglish列を標準化する
# (from sklearn.preprocessing import StandardScalerをインポート)
#print(ans[75]) #回答表示
df2 = initialize2() #初期化
df2[['English']] # DataFraeme
df2['English'] # Series

english = df2[['English']]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(english)
scaler.transform(english)
df2_std = pd.DataFrame(scaler.transform(english), columns=english.columns)

df2_std.describe()
# %%
# 【76】
# scikit-learnを用いてdf2のEnglish、Mathematics、History列を
# Min-Maxスケーリングする
# (from sklearn.preprocessing import MinMaxScalerをインポート)
#print(ans[76]) #回答表示
df2 = initialize2() #初期化
from sklearn.preprocessing import MinMaxScaler
df2 = df2.drop(['name','class'],axis=1) #不要列の削除
scaler = MinMaxScaler()
scaler.fit_transform(df2)
df2_minmax = pd.DataFrame(scaler.fit_transform(df2),columns=df2.columns)

df2_minmax.describe()
# %%
# 【77】
# dfのfare列の最大値、最小値の行名を取得
#print(ans[77]) #回答表示
df = initialize1() #初期化
df['fare'].idxmax()
df['fare'].idxmin()

# %%
# 【78】
# dfのfare列の0、25、50、75、100パーセンタイルを取得
#print(ans[78]) #回答表示
df = initialize1() #初期化
df['fare'].describe()

#指定するのであれば

print(df['fare'].quantile([0, 0.25, 0.5, 0.75, 1.0]))
# %%
# 【79】
# ①dfのage列の最頻値を取得
# ②value_counts()にてage列の要素数を
# 確認し、①の結果の妥当性を確認
#print(ans[79]) #回答表示
df = initialize1() #初期化
df['age'].mode()
df['age'].value_counts()

# %% [markdown]
# # ラベリング (80 - 81)

# %%
# 【80】
# dfのsex列をラベルエンコーディングし、
# dfの先頭5行を表示
# (from sklearn.preprocessing import LabelEncoderをインポート)
#print(ans[80]) #回答表示
df = initialize1() #初期化
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
print(df)
df['sex'] = encoder.fit_transform(df['sex'])
df.head()

# %%
# 【81】
# dfのsex列をOne-hotエンコーディングし、
# dfの先頭5行を表示
#print(ans[81]) #回答表示
df = initialize1() #初期化
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
encoded = ohe.fit_transform(df[['sex']])
encoded_df = pd.DataFrame(encoded, )

df.head()

df = initialize1()
df = pd.get_dummies(df,columns=['sex'])
df.head()
# %% [markdown]
# # Pandasプロット (82 - 89)
# Pandasプロットの機能については以下のサイトの説明が分かりやすいです  
# [自調自考の旅](https://own-search-and-study.xyz/2016/08/03/pandas%E3%81%AEplot%E3%81%AE%E5%85%A8%E5%BC%95%E6%95%B0%E3%82%92%E4%BD%BF%E3%81%84%E3%81%93%E3%81%AA%E3%81%99/)

# %%
# 【82】
# dfのすべての数値列のヒストグラムを表示
#print(ans[82]) #回答表示
df = initialize1() #初期化
df.plot(kind='hist')

#こういうのもある
df.hist(figsize=(20,20), color='b')
# %%
# 【83】
# dfのage列をヒストグラムで表示
#print(ans[83]) #回答表示
df = initialize1() #初期化
df['age'].hist(figsize=(5,5), color='b')
# %%
# 【84】
# df2のname列の要素ごとの3科目合計得点を棒グラフで表示
#print(ans[84]) #回答表示
df2 = initialize2() #初期化
df2.index = df2['name']
summary = df2.drop(['name','class'],axis=1).sum()
summary.plot(kind='bar')

df2 = initialize2() #初期化
df2['sum'] = df2.iloc[:,2:5].sum(axis=1) #3科目合計の列を作成
df2[['name','sum']].plot(kind='bar',x=df2.columns[0])
# %%
# 【85】
# df2のname列の要素ごとの3科目を棒グラフで
# 並べて表示
#print(ans[85]) #回答表示
df2 = initialize2() #初期化
df2[['name','English','Mathematics','History']].plot(kind='bar',figsize=(10,4),x=df2.columns[0])

# %%
# 【86】
# df2のname列の要素ごとの3科目を積み上げ棒グラフで表示
#print(ans[86]) #回答表示
df2 = initialize2() #初期化
df2[['name','English','Mathematics','History']].plot(kind='bar',figsize=(10,4),x=df2.columns[0], stacked=True)

# %%
# 【87】
# dfの各列間の散布図を表示
# (from pandas.plotting import scatter_matrixをインポート)
#print(ans[87]) #回答表示
df = initialize1() #初期化
from pandas.plotting import scatter_matrix
scatter_matrix(df,figsize=(10,10))

# %%
# 【88】
# dfのage列とfare列で散布図を作成
#print(ans[88]) #回答表示
df = initialize1() #初期化
from pandas.plotting import scatter_matrix
scatter_matrix(df[['age','fare']],figsize=(10,10))

df.plot(kind='scatter', x='age', y='fare', figsize=(8,6))
# %%
# 【89】
# 【88】で描画したグラフに「age-fare scatter」という
# グラフタイトルをつける
#print(ans[89]) #回答表示
df = initialize1() #初期化
df.plot(kind='scatter', x='age', y='fare', figsize=(8,6), title="age-fare scatter")
# %% [markdown]
# # タイタニック号の生存者予測 (90 - 100)  
# これまで触れてきたタイタニック号の乗客データを使用して、乗客の生存有無を  
# 予測してみます。  
#   
# ※90～100については順番通りにやらないと上手く動作しません

# %%
# 【90】ラベルエンコーディング
# df_copyのsexとembarked列をラベルエンコーディング
# (from sklearn.preprocessing import LabelEncoderをインポート)
# (df_copyはdfをコピーしたもの)
#print(ans[90]) #回答表示
df = initialize1()
from sklearn.preprocessing import LabelEncoder
df_copy =df.copy()
le = LabelEncoder()
df_copy['sex'] = le.fit_transform(df_copy['sex'])
df_copy['embarked'] = le.fit_transform(df_copy['embarked'])
df_copy.head()


# %%
# 【91】欠損値確認
# df_copyの欠損値を確認
#print(ans[91]) #回答表示
df_copy.isna().sum()
# %%
# 【92】欠損値補完
# df_copyのage、fare列の欠損値を各列の平均値で補完
#print(ans[92]) #回答表示
age_mean = df_copy['age'].mean()
fare_mean = df_copy['fare'].mean()
df_copy['age'] = df_copy['age'].fillna(age_mean)
df_copy['fare'] = df_copy['fare'].fillna(fare_mean)
df_copy.isna().sum()

# %%
# 【93】不要列の削除
# df_copyの中で機械学習で使用しない不要な行を削除
# (name, ticket, cabin, boat, body, home.destを削除)
#print(ans[93]) #回答表示
df_copy = df_copy.drop(['name', 'ticket', 'cabin', 'boat', 'body', 'home.dest'], axis=1)
df_copy
# %%
# 【94】ndarray形式への変換
# ①df_copyのpclass、age、sex、fare、embarkedの列を抽出し、ndarray形式に変換
# ②df_copyのsurvivedの列を抽出し、ndarray形式に変換
# (①をfeatures、②をtargetという変数にそれぞれ格納)
#print(ans[94]) #回答表示
features = df_copy[['pclass', 'age', 'sex', 'fare', 'embarked']].values
target = df_copy['survived'].values
# %%
# 【95】学習データとテストデータに分割
# 【94】で作成したfeatrues、targetを学習データとテストデータに分割
# (from sklearn.model_selection import  train_test_splitをインポート)
# ※分割時のパラメータは次を指定 test_size=0.3 random_state=0
#print(ans[95]) #回答表示
from sklearn.model_selection import train_test_split
features, features_test, target, target_test = train_test_split(features, target, test_size=0.3, random_state=0)

# %%
# 【96】学習の実行
# 学習データ(features、target)を用いランダムフォレストにて学習を実行
# (from sklearn.ensemble import RandomForestClassifierをインポート)
# ※パラメータは次を指定 n_estimators=100 random_state=0
#print(ans[96]) #回答表示
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=0) # ランダムフォレストインスタンス
model.fit(features, target)

# %%
# 【97】予測の実行
# test_Xデータの乗客の生存を予測
#print(ans[97]) #回答表示
pred = model.predict(features_test)
# %%
# 【98】予測精度の確認
# 予測結果がtest_y(生存有無の答え)とどれぐらい
# 整合していたかを確認(評価指標はaccuracy)
# (from sklearn.metrics import accuracy_scoreをインポート)
#print(ans[98]) #回答表示
from sklearn.metrics import accuracy_score
accuracy_score(pred, target_test)

# %%
# 【99】重要度の確認
# 学習における各列(特徴量)の
# 重要度を表示
#print(ans[99]) #回答表示
importance = model.feature_importances_ 
print('Feature Importances:')
for i, feat in enumerate(['pclass','age','sex','fare','embarked']):
    print('\t{0:20s} : {1:>.5f}'.format(feat, importance[i]))

# %%
# 【100】予測結果のcsv出力
# test_Xの予測結果をcsvでoutputフォルダに出力(ファイル名は「submission.csv」)
# (headerは不要)
#print(ans[100]) #回答表示
pred_df = pd.DataFrame(pred)
pred_df.to_csv('../output/submission.csv', header=False, index=False)

# %% [markdown]
# # ノックお疲れ様でした
# 各セルのoutput表示をすべてクリアにしたい場合は、ツールバーの  
# 「Kernel」→「Restart & Clear Output」を実行して下さい。
