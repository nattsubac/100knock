#-------------------- start_time: 2026-08-1411:09:13.844 +09:00--------------------#
#%% [markdown]
## 目的：
##### 1. RNA-seqのロジスティック回帰のPCAなしありでの比較。各種ベンチマークについて勉強してもいいかも
##### 2. 言語処理100本ノック
## やること：
##### 項目1について： 
##### - 昨日の再現
##### - ノートとしてまとめる
##### 項目2について:
##### - 環境構築
##### - 20ノック目標


# %% まずは昨日の復習から項目1
# import
from sklearn.pipeline import Pipeline #sklearnの処理をパイプライン化できる
from sklearn.preprocessing import StandardScaler #正規化
from sklearn.linear_model import LogisticRegression #ロジスティック回帰: 重みづけはどうやって設定されているんだろうな。
from sklearn.model_selection import train_test_split,cross_val_predict, StratifiedKFold, cross_validate #train_test_split:訓練データとテストデータに分ける、cross_val_predict:交差検証
from sklearn.decomposition import PCA #PCA
from sklearn.metrics import accuracy_score, balanced_accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay #モデル評価
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df_data = pd.read_csv("../materials/TCGA-PANCAN-HiSeq-801x20531/data.csv", index_col=0) #遺伝子発現Table
df_label = pd.read_csv("../materials/TCGA-PANCAN-HiSeq-801x20531/labels.csv", index_col=0) #サンプルの癌腫ラベル
# %% モデル開発
X = df_data
y = df_label['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y) #stratifyは必須
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

#標準化
scaler = StandardScaler()
X_train_scaler = scaler.fit_transform(X_train) #fitで、scaler内に各列の平均・標準偏差を格納、transformで実際に標準化のイメージ
X_test_scaler = scaler.transform(X_test) #訓練データの平均・標準偏差で実行。

#モデル作成
model = LogisticRegression(C=1.00, max_iter=3000, random_state=42) #もしl1を使うのであれば、本ver.では'l1_ratio'を設定。
#オプションを考える必要がある。
# penalty、L1正則化 (Lasso)とL2正則化(Ridge)、L1とL2の混合の3択。いずれもオーバーフィッティングにそな得るため。
    # 正則化（Regularization）は機械学習モデルが学習データに過剰に適合する過学習を抑える方法である。いずれも係数をいじる。
    # L1は係数をゼロにして特徴量を選択する。モデルがシンプルになって解釈がしやすい。スパース化（Sparsification）。
    # L2は係数全体を小さく均等に抑える。多重共線性（特徴量同士の強い相関）に強くなる。
    # elasticnetはL1とL2の組み合わせ
    # ->L2でいいかも。
# C: 正則化の強さの逆数
    # 小さいほど正則化が強く、過学習しにくい
    # 0.001-100程度を交差検証で探索可能
# max_iter: 収束するまでの最大反復数、最大降下法でもとめていくため、その繰り返しを設定。3000で収束警告が出なければ問題なし
# class_weight: class数が偏っている場合は'balanced'
# random_state: 乱数

model.fit(X_train_scaler, y_train) #標準化数値を入力
y_train_pred = model.predict(X_train_scaler)
y_test_pred = model.predict(X_test_scaler)
# %%
# モデルを評価する
# 訓練データとテストデータの精度
print("訓練Accuracy:", accuracy_score(y_train, y_train_pred))
print("テストAccuracy:", accuracy_score(y_test, y_test_pred))
print("テストBalanced Accuracy:",balanced_accuracy_score(y_test, y_test_pred))
# 癌種ごとの評価
print("\nClassification report")
print(classification_report(y_test, y_test_pred))

#混合行列の作成
labels = sorted(y.unique())
cm = confusion_matrix(y_test, y_test_pred, labels=labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
fig, ax = plt.subplots(figsize=(6,5))
disp.plot(ax=ax, cmap='Blues', colorbar=False)
ax.set_title('Prediction accuracy of Logistic Regression; Confusion matrix')
plt.tight_layout()
plt.show()
# %%　交差検証cross_validate
cv = StratifiedKFold(n_splits=5,shuffle=True,random_state=42)
scores = cross_validate(model, X, y, cv=cv, scoring={'accuracy':'accuracy', 'balanced_accuracy':'balanced_accuracy','macro_f1':'f1_macro'},n_jobs=-1, return_train_score=True)
print("訓練Accuracy:", scores["train_accuracy"])
print("検証Accuracy:", scores["test_accuracy"])
print("平均検証Accuracy:", scores["test_accuracy"].mean())
print("検証Accuracy標準偏差:", scores["test_accuracy"].std())
print("平均Balanced Accuracy:", scores["test_balanced_accuracy"].mean())
print("平均Macro F1:", scores["test_macro_f1"].mean())
# %%
y_cv_pred = cross_val_predict(model, X, y, cv=cv, n_jobs=-1)
fig, ax = plt.subplots(figsize=(8,7))
ConfusionMatrixDisplay.from_predictions(y, y_cv_pred, labels=sorted(y.unique()), cmap='Blues', colorbar=False, ax=ax)
ax.set_title('5-fold cross-validation confusion matrix')
plt.tight_layout()
plt.show()
# %% PCAでの実行
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

#標準化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) #fitで、scaler内に各列の平均・標準偏差を格納、transformで実際に標準化のイメージ
X_test_scaled = scaler.transform(X_test) #訓練データの平均・標準偏差で実行。

#X_trainだけPCAを学習
pca = PCA(n_components=0.90)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
#モデル作成
model = LogisticRegression(C=1.00, max_iter=3000, random_state=42) #もしl1を使うのであれば、本ver.では'l1_ratio'を設定。
model.fit(X_train_pca, y_train) #標準化数値を入力
y_train_pred = model.predict(X_train_pca)
y_test_pred = model.predict(X_test_pca)
# モデルを評価する
# 訓練データとテストデータの精度
print("訓練Accuracy:", accuracy_score(y_train, y_train_pred))
print("テストAccuracy:", accuracy_score(y_test, y_test_pred))
print("テストBalanced Accuracy:",balanced_accuracy_score(y_test, y_test_pred))
# 癌種ごとの評価
print("\nClassification report")
print(classification_report(y_test, y_test_pred))

#混合行列の作成
labels = sorted(y.unique())
cm = confusion_matrix(y_test, y_test_pred, labels=labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
fig, ax = plt.subplots(figsize=(6,5))
disp.plot(ax=ax, cmap='Blues', colorbar=False)
ax.set_title('Prediction accuracy of Logistic Regression; Confusion matrix')
plt.tight_layout()
plt.show()
#交差検証cross_validate
cv = StratifiedKFold(n_splits=5,shuffle=True,random_state=42)
scores = cross_validate(model, X, y, cv=cv, scoring={'accuracy':'accuracy', 'balanced_accuracy':'balanced_accuracy','macro_f1':'f1_macro'},n_jobs=-1, return_train_score=True)
print("訓練Accuracy:", scores["train_accuracy"])
print("検証Accuracy:", scores["test_accuracy"])
print("平均検証Accuracy:", scores["test_accuracy"].mean())
print("検証Accuracy標準偏差:", scores["test_accuracy"].std())
print("平均Balanced Accuracy:", scores["test_balanced_accuracy"].mean())
print("平均Macro F1:", scores["test_macro_f1"].mean())
# cross_val_predict
y_cv_pred = cross_val_predict(model, X, y, cv=cv, n_jobs=-1)
fig, ax = plt.subplots(figsize=(8,7))
ConfusionMatrixDisplay.from_predictions(y, y_cv_pred, labels=sorted(y.unique()), cmap='Blues', colorbar=False, ax=ax)
ax.set_title('5-fold cross-validation confusion matrix')
plt.tight_layout()
plt.show()
# %%
