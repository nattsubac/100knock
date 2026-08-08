# %%
from pathlib import Path
import re

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "materials/Pandas_100_knocks/input"
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def initialize1():
    return pd.read_csv(DATA_DIR / "titanic3.csv")


def initialize2():
    return pd.read_csv(DATA_DIR / "data1.csv")


df3 = pd.read_csv(DATA_DIR / "data1_2.csv")
df4 = pd.read_csv(DATA_DIR / "data1_3.csv")

# %%
# 1
df = initialize1()
df.head()

# %%
# 2
df = initialize1()
df.tail()

# %%
# 3
df = initialize1()
df.shape

# %%
# 4
df2 = initialize2()
df2.head()

# %%
# 5
df = initialize1()
df.sort_values('fare')

# %%
# 6
df = initialize1()
df_copy = df.copy()
df_copy.head()

# %%
# 7
df = initialize1()
print(df.dtypes)
print(df['cabin'].dtype)

# %%
# 8
df = initialize1()
print(df['pclass'].dtype)
df['pclass'] = df['pclass'].astype(str)
print(df['pclass'].dtype)

# %%
# 9
df = initialize1()
len(df)

# %%
# 10
df = initialize1()
df.info()

# %%
# 11
df = initialize1()
print(df['sex'].unique())
print(df['cabin'].unique())

# %%
# 12
df = initialize1()
df.columns.tolist()

# %%
# 13
df = initialize1()
df.index.values

# %%
# 14
df = initialize1()
df['name']

# %%
# 15
df = initialize1()
df[['name','sex']]

# %%
# 16
df = initialize1()
df[:4]

# %%
# 17
df = initialize1()
df[3:10]

# %%
# 18
df = initialize1()
df.loc[:,:]

# %%
# 19
df = initialize1()
df.loc[:,'fare']

# %%
# 20
df = initialize1()
df.loc[:10,'fare']

# %%
# 21
df = initialize1()
df.loc[:,['name','ticket']]

# %%
# 22
df = initialize1()
df.loc[:,'name':'cabin']

# %%
# 23
df = initialize1()
df.iloc[:5,4]

# %%
# 24
df = initialize1()
df_copy = df[["name", "age", "sex"]]
df_copy.to_csv(OUTPUT_DIR / "sample.csv", index=False)

# %%
# 25
df = initialize1()
df[df['age'] >= 30]

# %%
# 26
df = initialize1()
df[df['sex'] == 'female']

# %%
# 27
df = initialize1()
df[(df['sex'] == 'female' ) & (df['age'] >= 40)]

# %%
# 28
df = initialize1()
df.query('sex == "female" & age >= 40 ')

# %%
# 29
df = initialize1()
df[df["name"].str.contains("Mrs", na=False, regex=False)]

# %%
# 30
df = initialize1()
df.select_dtypes(include=["object", "string"])

# %%
# 31
df = initialize1()
df.nunique()

# %%
# 32
df = initialize1()
df['embarked'].value_counts()

# %%
# 33
df = initialize1()
df.loc[3,'age'] = 40
df.head()

# %%
# 34
df = initialize1()
df["sex"] = df["sex"].map({"male": 0, "female": 1})
df.head()

# %%
# 35
df = initialize1()
df['fare'] = df['fare'] + 100
df.head()

# %%
# 36
df = initialize1()
df['fare'] = df['fare'] * 2
df.head()

# %%
# 37
df = initialize1()
df['fare'] = df['fare'].round()
df.head()

# %%
# 38
df = initialize1()
df['test'] = 1
df.head()

# %%
# 39
df = initialize1()
df['test'] = df['cabin'].str.cat(df['embarked'],sep='_')
df.head()

# %%
# 40
df = initialize1()
df["test"] = df["age"].astype(str) + "_" + df["embarked"]
df.head()

# %%
# 41
df = initialize1()
df = df.drop('body',axis=1)
df.head()

# %%
# 42
df = initialize1()
df = df.drop(3,axis=0)
df.head()

# %%
# 43
df2 = initialize2()
df2.columns = ['name', 'class', 'Biology', 'Physics', 'Chemistry']
df2.head()

# %%
# 44
df2 = initialize2()
df2 = df2.rename(columns={'English' : 'Biology'})
df2.head()

# %%
# 45
df2 = initialize2()
df2 = df2.rename(index={1 : 10})
df2.head()

# %%
# 46
df = initialize1()
df.isna().sum()

# %%
# 47
df = initialize1()
df["age"] = df["age"].fillna(30)
df["age"].isna().sum()

# %%
# 48
df = initialize1()
df = df.dropna()
df.isna().sum()

# %%
# 49
df = initialize1()
df["survived"].to_numpy()

# %%
# 50
df = initialize1()
df.sample(frac=1)

# %%
# 51
df = initialize1()
df.sample(frac=1).reset_index(drop=True)

# %%
# 52
df2 = initialize2()
print(df2.duplicated().sum())
df2 = df2.drop_duplicates()
df2

# %%
# 53
df = initialize1()
df['name'].str.upper()

# %%
# 54
df = initialize1()
df['name'].str.lower()

# %%
# 55
df = initialize1()
df['sex'] = df['sex'].replace('female','Python')
df.head()

# %%
# 56
df = initialize1()
df.loc[0, "name"] = re.sub("Elisabeth", "", df.loc[0, "name"])
df.loc[0, "name"]

# %%
# 57
df5 = pd.read_csv(DATA_DIR / "data2.csv", encoding="cp932")
df5["test2"] = df5["都道府県"].str.strip() + "_" + df5["市区町村"].str.strip()
df5.head()

# %%
# 58
df2 = initialize2()
df2 = df2.transpose()
df2

# %%
# 59
df2 = initialize2()
df2 = pd.merge(df2,df3,on='name',how='left')
df2

# %%
# 60
df2 = initialize2()
df2 = pd.merge(df2,df3,on='name',how='right')
df2

# %%
# 61
df2 = initialize2()
df2 = pd.merge(df2,df3,on='name',how='inner')
df2

# %%
# 62
df2 = initialize2()
df2 = pd.merge(df2,df3,on='name',how='outer')
df2

# %%
# 63
df2 = initialize2()
df2 = pd.concat([df2,df4],axis=1)
df2

# %%
# 64
df2 = initialize2()
df2 = pd.concat([df2,df4],axis=1)
df2 = df2.loc[:,~df2.columns.duplicated()]
df2

# %%
# 65
df2 = initialize2()
df2 = pd.concat([df2,df4],axis=0)
df2

# %%
# 66
df = initialize1()
df['age'].mean()

# %%
# 67
df = initialize1()
df['age'].median()

# %%
# 68
df2 = initialize2()
subjects = ["English", "Mathematics", "History"]
print(df2[subjects].sum(axis=1))
print(df2[subjects].sum(axis=0))

# %%
# 69
df2 = initialize2()
df2['English'].max()

# %%
# 70
df2 = initialize2()
df2['English'].min()

# %%
# 71
df2 = initialize2()
scores = df2.drop(columns="name")
print(scores.groupby("class").max())
print(scores.groupby("class").min())
print(scores.groupby("class").mean())

# %%
# 72
df = initialize1()
df.describe()

# %%
# 73
df = initialize1()
df.corr(numeric_only=True)

# %%
# 74
df2 = initialize2()
from sklearn.preprocessing import StandardScaler

scores = df2[["English", "Mathematics", "History"]]
scaler = StandardScaler()
df2_std = pd.DataFrame(
    scaler.fit_transform(scores),
    columns=scores.columns,
    index=scores.index,
)
df2_std.describe()

# %%
# 75
df2 = initialize2()
from sklearn.preprocessing import StandardScaler

english = df2[["English"]]
scaler = StandardScaler()
df2_std = pd.DataFrame(
    scaler.fit_transform(english),
    columns=english.columns,
    index=english.index,
)
df2_std.describe()

# %%
# 76
df2 = initialize2()
from sklearn.preprocessing import MinMaxScaler

scores = df2[["English", "Mathematics", "History"]]
scaler = MinMaxScaler()
df2_minmax = pd.DataFrame(
    scaler.fit_transform(scores),
    columns=scores.columns,
    index=scores.index,
)
df2_minmax.describe()

# %%
# 77
df = initialize1()
print(df['fare'].idxmax())
print(df['fare'].idxmin())

# %%
# 78
df = initialize1()
print(df['fare'].quantile([0, 0.25, 0.5, 0.75, 1.0]))

# %%
# 79
df = initialize1()
print(df['age'].mode())
print(df['age'].value_counts())

# %%
# 80
df = initialize1()
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df["sex"] = encoder.fit_transform(df["sex"])
df.head()

# %%
# 81
df = initialize1()
df = pd.get_dummies(df, columns=["sex"], dtype=int)
df.head()

# %%
# 82
df = initialize1()
df.hist(figsize=(20, 20), color="b")

# %%
# 83
df = initialize1()
df['age'].plot(kind='hist')

# %%
# 84
df2 = initialize2()
df2['sum'] = df2.iloc[:,2:5].sum(axis=1)
df2[['name','sum']].plot(kind='bar',x=df2.columns[0])

# %%
# 85
df2 = initialize2()
df2[['name','English','Mathematics','History']].plot(kind='bar',figsize=(10,4),x=df2.columns[0])

# %%
# 86
df2 = initialize2()
df2[['name','English','Mathematics','History']].plot(kind='bar',figsize=(10,4),
                                                    x=df2.columns[0],stacked=True)

# %%
# 87
df = initialize1()
from pandas.plotting import scatter_matrix

scatter_matrix(df, figsize=(20, 20))

# %%
# 88
df = initialize1()
df.plot(kind='scatter',x='age',y='fare',figsize=(8,6))

# %%
# 89
df = initialize1()
df.plot(kind='scatter',x='age',y='fare',figsize=(8,6),title='age-fare scatter')

# %%
# 90
from sklearn.preprocessing import LabelEncoder

df = initialize1()
df_copy = df.copy()
encoder = LabelEncoder()
df_copy["sex"] = encoder.fit_transform(df_copy["sex"])
df_copy["embarked"] = encoder.fit_transform(df_copy["embarked"].astype(str))
df_copy.head()

# %%
# 91
df_copy.isna().sum()

# %%
# 92
df_copy["age"] = df_copy["age"].fillna(df_copy["age"].mean())
df_copy["fare"] = df_copy["fare"].fillna(df_copy["fare"].mean())
df_copy.isna().sum()

# %%
# 93
df_copy = df_copy.drop(
    columns=["name", "ticket", "cabin", "boat", "body", "home.dest"]
)
df_copy

# %%
# 94
feature_names = ["pclass", "age", "sex", "fare", "embarked"]
features = df_copy[feature_names].to_numpy()
target = df_copy["survived"].to_numpy()

# %%
# 95
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.3,
    random_state=0,
)

# %%
# 96
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# %%
# 97
pred = model.predict(X_test)
pred

# %%
# 98
from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

# %%
# 99
importance = pd.Series(
    model.feature_importances_,
    index=feature_names,
    name="importance",
)
importance.sort_values(ascending=False)

# %%
# 100
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
pd.DataFrame(pred).to_csv(
    OUTPUT_DIR / "submission.csv",
    header=False,
    index=False,
)
