#-------------------- start_time: 2026-08-1309:41:34.218 +09:00--------------------#
#conda環境を作成 name: rnaseq
#materials/environment.ymlにconda env export --no-builds > environment.ymlを作成するコードを記載
#ipykernelで登録したものをInteractive-1で表示するには、一度VScodeを再起動する必要がある
#8/13：RNA-seq癌種推定 
#最初はUCIの「Gene Expression Cancer
#RNA-Seq」が扱いやすい。801検体、20,531遺伝子、5癌種の多クラス分類データです。UCI公式データセット (https://archive.ics.uci.edu/dataset/401/gene%2Bexpression%2Bcancer%2Brna%2Bseqmicroarray-202)
#この日はモデル作成を急がず、次を理解します。

#1行が患者、1列が遺伝子発現量
# - 目的変数は5種類の癌種
# - サンプル数より特徴量数が圧倒的に多い
# - 癌種ごとの件数に偏りがあるか
# - PCAで癌種ごとの分離が見えるか
# 成果物は、例えば次の1ファイルです。

# rnaseq_cancer/
# └── 01_eda_and_split.py

# 完了条件は「X_train、X_test、y_train、y_testが作られ、各データの意味を説明できること」です。


#%%
import pandas as pd
import numpy as np

# %%
df_data = pd.read_csv("/Users/natsu/vscode/100knock/materials/TCGA-PANCAN-HiSeq-801x20531/data.csv", index_col=0)
df_data[df_data['gene_0'].isnull()]
#df_dataはgene_0で昇順ソートされているようにみられる。また、マイナスは存在しないか？
df_data.describe().loc['min'].min() #min行を表示したい
df_data.describe().loc['max'].max() #max行を表示したい
#結果は0.0であり、マイナスは存在しない。逆に最大値は約20.8であることから、0が最小値のカウントデータであることが掴める。
df_label = pd.read_csv("/Users/natsu/vscode/100knock/materials/TCGA-PANCAN-HiSeq-801x20531/labels.csv", index_col=0)
df_label.head()
df_data.isnull().describe().loc['unique'].min() # nullの検索、欠損なし。

# %%
# labelの分布を確認する
label_count = df_label.value_counts()
# BRCA:300, KIRC:146, LUAD:141, PRAD:136, COAD:78
# このデータは、癌種ごとの件数に偏りがあることがわかる。特にCOADが少ない。
print(label_count)
# %% PCAでかたよりを見てみる。
#目的：データ全体の構造を理解するための探索的解析(EDA: Exploratory data analysis)を行う。
#癌腫に対応した遺伝子発現パターンがありそうか、外れ値や他の検体から大きく離れた検体がないか。同じ癌腫の中に複数の集団がないか
#癌腫以外の要因がデータを支配していないか、PCAで時限削減しても癌腫の情報がのこりそうか。
df_result = pd.concat([df_label, df_data], axis=1) #表を結合
df_result.head()

# codexに教えてもらった
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

#説明変数：遺伝子発現量
X = df_data #癌腫ラベルをPCA入れないので、concatしたものは使わない
#目的変数：癌腫
y = df_label['Class']

#遺伝子ごとの標準化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled

# 20,531遺伝子を2つの主成分へ圧縮
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

#描画用DataFrame
df_pca = pd.DataFrame(X_pca, columns=['PC1','PC2'],index=X.index)
df_pca['Class'] = y # Class列を定義

# 各種成分が説明する分散の割合
print('PC1の寄与率:', pca.explained_variance_ratio_[0])
print('PC2の寄与率:', pca.explained_variance_ratio_[1])
print('累積寄与率:', pca.explained_variance_ratio_.sum())

#散布図
plt.figure(figsize=(9,7))
sns.scatterplot(
    data=df_pca,
    x='PC1',
    y='PC2',
    hue='Class', #指定した変数の値に応じて点の色を分ける引数
    palette='tab10', #使用する色のカラーパレットを指定
    alpha=0.8, #点の透明度
    s=60 #点の大きさ
)
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.1%})")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.1%})")
plt.title("PCA of RNA-seq gene expression")
plt.legend(title="Cancer type")
plt.tight_layout()
plt.show()

# %% 上の結果から、癌種ごとの分離は見えない。PCAの寄与率も低い。
# 20,531遺伝子を2つの主成分へ圧縮
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

#描画用DataFrame
df_pca = pd.DataFrame(X_pca, columns=['PC1','PC2','PC3'],index=X.index)
df_pca['Class'] = y # Class列を定義

# 各種成分が説明する分散の割合
print('PC1の寄与率:', pca.explained_variance_ratio_[0])
print('PC2の寄与率:', pca.explained_variance_ratio_[1])
print('PC3の寄与率:', pca.explained_variance_ratio_[2])
print('累積寄与率:', pca.explained_variance_ratio_.sum())

#散布図
fig, axes = plt.subplots(1,2, figsize=(14,6))
sns.scatterplot(
    data=df_pca,
    x='PC1',
    y='PC3',
    hue='Class', #指定した変数の値に応じて点の色を分ける引数
    palette='tab10', #使用する色のカラーパレットを指定
    alpha=0.7, #点の透明度
    s=50, #点の大きさ
    ax=axes[0]
)
sns.scatterplot(
    data=df_pca,
    x='PC2',
    y='PC3',
    hue='Class', #指定した変数の値に応じて点の色を分ける引数
    palette='tab10', #使用する色のカラーパレットを指定
    alpha=0.7, #点の透明度
    s=50, #点の大きさ
    ax=axes[1]
)
axes[0].set_title("PC1 vs PC3")
axes[1].set_title("PC2 vs PC3")
axes[0].set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.1%})")
axes[0].set_ylabel(f"PC3 ({pca.explained_variance_ratio_[2]:.1%})")
axes[1].set_xlabel(f"PC2 ({pca.explained_variance_ratio_[1]:.1%})")
axes[1].set_ylabel(f"PC3 ({pca.explained_variance_ratio_[2]:.1%})")
plt.tight_layout()
plt.show()
# %%
#  PC1–PC3平面では、LUADは広い範囲に分布し、他の癌種と重なっていた。一方、LUAD以外の癌種には一定の分離傾向が見られた。LUADは遺伝子発現パターンのばらつきが比較的大きい可能性がある。
# 最終目的は癌腫推定である。つまり今回の結果は、PCAによる教師なし学習で得られたグラフから癌腫の推定は難しいと判断される。
# 理由は、PC1/2/3の説明部分が少ない（20%くらい）点からデータ全体のばらつきを説明できていない点や、分布図に癌腫ごとに重なりがある点である。
# PC1-PC3では、LUADが広い範囲に分布し他癌腫に重なっていたことなどが結果の例である。
# ⇨実際に分類モデルを作成し、未知データに対する性能で判断する。

# まずは訓練・テストデータへの分割をする。
# EDAの情報としてまず
    # 1. CUDAのデータ数がすくない(# BRCA:300, KIRC:146, LUAD:141, PRAD:136, COAD:78)
        # -> trainとtestの分割を、同組成でおこなう。
    # 2. 遺伝子が正規分布上にのっていると仮定している場合、標準化した。結局分布を疑うことについては、結果を見ながらかんがえていくべきかな。

# %% 訓練・テストデータ分割
from sklearn.model_selection import train_test_split

X = df_data
y = df_label['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) #stratify=yで構成比を維持
print('X_train:', X_train.shape)
print('X_test:', X_test.shape)
print('y_train:', y_train.shape)
print('y_test:', y_test.shape)


# %%stratify=yが分かれているかチェック
print("全データ:", X.shape, y.shape)
print("訓練データ:", X_train.shape, y_train.shape)
print("テストデータ:", X_test.shape, y_test.shape)

print("\n全データの割合")
print(y.value_counts(normalize=True).sort_index())

print("\n訓練データの割合")
print(y_train.value_counts(normalize=True).sort_index())

print("\nテストデータの割合")
print(y_test.value_counts(normalize=True).sort_index())
# %%ベースライン分類モデルを作成する
# StandardScaler -> PCA -> logistic回帰 ->テストデータで評価

# StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
## 訓練データから平均・標準偏差を学習
X_train_scaled = scaler.fit_transform(X_train)
## 訓練データと同じ基準でテストデータも変換
X_test_scaled = scaler.transform(X_test) # fitをつけないことで、事前の学習した平均・標準偏差で行う。

print('X_train_scaled:', X_train_scaled.shape)
print('X_test_scaled:', X_test_scaled.shape)
# %% PCA サンプル数より特徴量数が遥かに多い高次元データでは過学習リスクがたかい。目安は
    #  - 特徴量数 << サンプル数：比較的扱いやすい
    #  - 特徴量数 ≈ サンプル数：過学習への注意が必要
    #  - 特徴量数 > サンプル数：過学習のリスクが高い
    #  - 特徴量数 >> サンプル数：強い正則化や次元削減が重要
#　しかし、特徴両数だけでは判断できない
    #  - モデルの複雑さ
    #  - 遺伝子間の相関
    #  - ノイズの量
    #  - 癌種間の違いの明瞭さ
    #  - 正則化の有無
    #  - 特徴量選択やPCAの有無
    #  - クラスごとのサンプル数

from sklearn.decomposition import PCA
pca = PCA(n_components=0.90)

# 訓練データで主成分を学習
X_train_pca = pca.fit_transform(X_train_scaled)
# 同じ主成分を使ってテストデータを変換
X_test_pca = pca.transform(X_test_scaled)

print("主成分数:", pca.n_components_)
print("累積寄与率:", pca.explained_variance_ratio_.sum())
print("X_train_pca:", X_train_pca.shape)
print("X_test_pca:", X_test_pca.shape)

# %%　ロジスティック回帰をしていく
# import
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

# pipeline構築
model = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(
        penalty='l2',
        C=1.0,
        max_iter=3000,
        random_state=42
    ))
])

# 訓練
model.fit(X_train, y_train)

#予測
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# 訓練データとテストデータの精度
print("訓練Accuracy:", accuracy_score(y_train, y_train_pred))
print("テストAccuracy:", accuracy_score(y_test, y_test_pred))
print(
    "テストBalanced Accuracy:",
    balanced_accuracy_score(y_test, y_test_pred)
)

# 癌種ごとの評価
print("\nClassification report")
print(classification_report(y_test, y_test_pred))
# %% 混同行列
labels = sorted(y.unique())
cm = confusion_matrix(
    y_test,
    y_test_pred,
    labels=labels
)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=labels
)

fig, ax = plt.subplots(figsize=(8, 7))
disp.plot(
    ax=ax,
    cmap="Blues",
    colorbar=False
)
ax.set_title("Logistic Regression: Confusion Matrix")
plt.tight_layout()
plt.show()
# %%
from sklearn.model_selection import StratifiedKFold, cross_validate

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_validate(
    model,
    X,
    y,
    cv=cv,
    scoring={
        "accuracy": "accuracy",
        "balanced_accuracy": "balanced_accuracy",
        "macro_f1": "f1_macro"
    },
    n_jobs=-1,
    return_train_score=True
)

print("訓練Accuracy:", scores["train_accuracy"])
print("検証Accuracy:", scores["test_accuracy"])
print("平均検証Accuracy:", scores["test_accuracy"].mean())
print("検証Accuracy標準偏差:", scores["test_accuracy"].std())

print("平均Balanced Accuracy:",
    scores["test_balanced_accuracy"].mean())

print("平均Macro F1:",
    scores["test_macro_f1"].mean())

#%%
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

y_cv_pred = cross_val_predict(
    model,
    X,
    y,
    cv=cv,
    n_jobs=-1
)

fig, ax = plt.subplots(figsize=(8,7))
ConfusionMatrixDisplay.from_predictions(
    y,
    y_cv_pred,
    labels=sorted(y.unique()),
    cmap='Blues',
    colorbar=False,
    ax=ax
)

ax.set_title('5-fold cross-validation confusion matrix')
plt.tight_layout()
plt.show()
# %%
misclassified = pd.DataFrame({
    "true": y,
    "predicted": y_cv_pred
})

misclassified = misclassified[
    misclassified["true"] != misclassified["predicted"]
]

print(misclassified)
