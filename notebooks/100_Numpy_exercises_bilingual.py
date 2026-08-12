# %% [markdown]
# # NumPy 100本ノック（英語・日本語）
#
# `materials/numpy-100/100_Numpy_exercises.ipynb`を、VS CodeのPython Interactiveで実行できる`# %%`形式へ変換した演習ファイルです。
# 各問は原文（英語）と日本語訳を併記し、その直後に回答用の空コードセルを配置しています。
# `hint(問題番号)`でヒント、`answer(問題番号)`で解答例を表示できます。
#
# 出典: https://github.com/rougier/numpy-100

# %%
from pathlib import Path

import numpy as np


def _find_exercises_source():
    """実行場所にかかわらず、元教材の問題・ヒント・解答ファイルを探す。"""
    candidates = [
        Path.cwd() / "materials/numpy-100/source/exercises100.ktx",
        Path.cwd().parent / "materials/numpy-100/source/exercises100.ktx",
    ]

    if "__file__" in globals():
        candidates.insert(
            0,
            Path(__file__).resolve().parent.parent
            / "materials/numpy-100/source/exercises100.ktx",
        )

    for candidate in candidates:
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "materials/numpy-100/source/exercises100.ktx が見つかりません。"
        "100knockリポジトリ内で実行してください。"
    )


def _load_keyed_text(path):
    """`< q1`、`< h1`、`< a1`形式の元教材を辞書として読み込む。"""
    entries = {}
    key = None
    lines = []

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("<"):
            if key is not None:
                entries[key] = "\n".join(lines).strip()
            key = line.removeprefix("<").strip()
            lines = []
        elif key is not None:
            lines.append(line)

    if key is not None:
        entries[key] = "\n".join(lines).strip()

    return entries


def _validate_question_number(number):
    if not isinstance(number, int) or not 1 <= number <= 100:
        raise ValueError("問題番号は1から100までの整数で指定してください。")


_QHA = _load_keyed_text(_find_exercises_source())


def question(number):
    """英語の問題文を表示する。"""
    _validate_question_number(number)
    print(f"{number}. {_QHA[f'q{number}']}")


def hint(number):
    """指定した問題のヒントを表示する。"""
    _validate_question_number(number)
    print(_QHA[f"h{number}"])


def answer(number):
    """指定した問題の解答例を表示する。"""
    _validate_question_number(number)
    print(_QHA[f"a{number}"])


# 使用例（コメントを外して実行）
# hint(1)
# answer(1)

# %% [markdown]
# ## 1. Import the numpy package under the name `np` (★☆☆)
#
# **日本語:** NumPyパッケージを`np`という名前でインポートせよ。

# %%
import numpy as np
# %% [markdown]
# ## 2. Print the numpy version and the configuration (★☆☆)
#
# **日本語:** NumPyのバージョンと設定情報を表示せよ。

# %%
print(np.__version__)
np.show_config()
# %% [markdown]
# ## 3. Create a null vector of size 10 (★☆☆)
#
# **日本語:** 要素数10のゼロベクトルを作成せよ。

# %%
q3_vector = np.zeros(10)
print(q3_vector)

# %% [markdown]
# ## 4. How to find the memory size of any array (★☆☆)
#
# **日本語:** 任意の配列が使用するメモリサイズを求めるにはどうすればよいか。

# %%
Z = np.zeros((10, 10))
print('%d bytes' % (Z.size * Z.itemsize))

# %% [markdown]
# ## 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
#
# **日本語:** コマンドラインからNumPyの`add`関数のドキュメントを表示するにはどうすればよいか。

# %%
np.info(np.add)
# %% [markdown]
# ## 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
#
# **日本語:** 要素数10のゼロベクトルを作成し、5番目の値だけを1にせよ。

# %%
Z = np.zeros(10)
Z[4] = 1
print(Z)

# %% [markdown]
# ## 7. Create a vector with values ranging from 10 to 49 (★☆☆)
#
# **日本語:** 10から49までの値を持つベクトルを作成せよ。

# %%
q7_vector = np.array(range(10,50))
q7_vector

# %% [markdown]
# ## 8. Reverse a vector (first element becomes last) (★☆☆)
#
# **日本語:** ベクトルの要素順を反転せよ（先頭要素が末尾になる）。

# %%
q8_vector = q7_vector[::-1]
q8_vector

# %% [markdown]
# ## 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
#
# **日本語:** 0から8までの値を持つ3×3行列を作成せよ。

# %%
q9_matrix = np.array(range(9)).reshape(3,3)
q9_matrix

# %% [markdown]
# ## 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
#
# **日本語:** `[1, 2, 0, 0, 4, 0]`から非ゼロ要素のインデックスを求めよ。

# %%
q10_array = np.array([1,2,0,0,4,0])
print(np.nonzero(q10_array))

# %% [markdown]
# ## 11. Create a 3x3 identity matrix (★☆☆)
#
# **日本語:** 3×3の単位行列を作成せよ。

# %%
np.eye(3)
# %% [markdown]
# ## 12. Create a 3x3x3 array with random values (★☆☆)
#
# **日本語:** ランダムな値を持つ3×3×3配列を作成せよ。

# %%
np.random.random((3,3,3))
# %% [markdown]
# ## 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
#
# **日本語:** ランダムな値を持つ10×10配列を作成し、最小値と最大値を求めよ。

# %%
q13_matrix = np.random.random((10,10))
print(q13_matrix.min(), q13_matrix.max())
# %% [markdown]
# ## 14. Create a random vector of size 30 and find the mean value (★☆☆)
#
# **日本語:** 要素数30のランダムなベクトルを作成し、平均値を求めよ。

# %%
np.random.random(30).mean()

# %% [markdown]
# ## 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
#
# **日本語:** 外周が1、内部が0の2次元配列を作成せよ。

# %%
q15_array = np.ones((3,3))
q15_array[1:-1, 1:-1] = 0
q15_array

# %% [markdown]
# ## 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
#
# **日本語:** 既存の配列の周囲に、0で埋めた境界を追加するにはどうすればよいか。

# %%
q16_array = np.ones((3,3))
q16_array_with_border = np.pad(q16_array, pad_width=1, mode='constant', constant_values=0)
q16_array_with_border

# %% [markdown]
# ## 17. What is the result of the following expression? (★☆☆)
#
# **日本語:** 次の式の結果は何か。
#
# ```python
# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# np.nan in set([np.nan])
# 0.3 == 3 * 0.1
# ```

# %%
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1

# %% [markdown]
# ## 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
#
# **日本語:** 主対角線の1つ下に1、2、3、4を配置した5×5行列を作成せよ。

# %%
np.diag(1+np.arange(4),k=-1)

# %% [markdown]
# ## 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
#
# **日本語:** 8×8行列を作成し、市松模様で埋めよ。

# %%
x = np.zeros((8,8),dtype=int)
print(x)
x[1::2,::2] = 1
print(x)
x[::2,1::2] = 1
print(x)

# %% [markdown]
# ## 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
#
# **日本語:** 形状が`(6, 7, 8)`の配列について、100番目の要素のインデックス`(x, y, z)`を求めよ。

# %%
print(np.unravel_index(99,(6,7,8)))

# %% [markdown]
# ## 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
#
# **日本語:** `tile`関数を使って8×8の市松模様行列を作成せよ。

# %%
q21_matrix = np.tile(
    np.array([[0, 1], [1, 0]]),
    (4, 4),
)  # 第1引数は繰り返すパターン、第2引数は縦横の繰り返し回数
q21_matrix

# %% [markdown]
# ## 22. Normalize a 5x5 random matrix (★☆☆)
#
# **日本語:** ランダムな5×5行列を正規化せよ。

# %%
q22_matrix = np.random.random((5,5))
q22_std = (q22_matrix - q22_matrix.mean())/q22_matrix.std()
q22_std

# %% [markdown]
# ## 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
#
# **日本語:** 色を4つの符号なしバイト（RGBA）で表す独自の`dtype`を作成せよ。

# %%

# %% [markdown]
# ## 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
#
# **日本語:** 5×3行列と3×2行列の行列積を計算せよ。

# %%

# %% [markdown]
# ## 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
#
# **日本語:** 1次元配列について、3から8の間にあるすべての要素の符号をインプレースで反転せよ。

# %%

# %% [markdown]
# ## 26. What is the output of the following script? (★☆☆)
#
# **日本語:** 次のスクリプトの出力は何か。
#
# ```python
# # Author: Jake VanderPlas
#
# print(sum(range(5),-1))
# from numpy import *
# print(sum(range(5),-1))
# ```

# %%

# %% [markdown]
# ## 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
#
# **日本語:** 整数ベクトル`Z`について、次の式のうち有効なものはどれか。
#
# ```python
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z
# ```

# %%

# %% [markdown]
# ## 28. What are the result of the following expressions? (★☆☆)
#
# **日本語:** 次の式の結果は何か。
#
# ```python
# np.array(0) / np.array(0)
# np.array(0) // np.array(0)
# np.array([np.nan]).astype(int).astype(float)
# ```

# %%

# %% [markdown]
# ## 29. How to round away from zero a float array ? (★☆☆)
#
# **日本語:** 浮動小数点配列を、0から遠ざかる方向へ丸めるにはどうすればよいか。

# %%

# %% [markdown]
# ## 30. How to find common values between two arrays? (★☆☆)
#
# **日本語:** 2つの配列に共通する値を求めるにはどうすればよいか。

# %%

# %% [markdown]
# ## 31. How to ignore all numpy warnings (not recommended)? (★☆☆)
#
# **日本語:** NumPyのすべての警告を無視するにはどうすればよいか（非推奨）。

# %%

# %% [markdown]
# ## 32. Is the following expressions true? (★☆☆)
#
# **日本語:** 次の式は真か。
#
# ```python
# np.sqrt(-1) == np.emath.sqrt(-1)
# ```

# %%

# %% [markdown]
# ## 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
#
# **日本語:** 昨日、今日、明日の日付を取得するにはどうすればよいか。

# %%

# %% [markdown]
# ## 34. How to get all the dates corresponding to the month of July 2016? (★★☆)
#
# **日本語:** 2016年7月に該当するすべての日付を取得するにはどうすればよいか。

# %%

# %% [markdown]
# ## 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
#
# **日本語:** `((A+B)*(-A/2))`をコピーせずインプレースで計算するにはどうすればよいか。

# %%

# %% [markdown]
# ## 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)
#
# **日本語:** 正の乱数配列から整数部分を4通りの方法で取り出せ。

# %%

# %% [markdown]
# ## 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
#
# **日本語:** 各行が0から4までの値を持つ5×5行列を作成せよ。

# %%

# %% [markdown]
# ## 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
#
# **日本語:** 10個の整数を生成するジェネレータ関数を用意し、それを使って配列を作成せよ。

# %%

# %% [markdown]
# ## 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
#
# **日本語:** 0と1を除いた、その間の値を持つ要素数10のベクトルを作成せよ。

# %%

# %% [markdown]
# ## 40. Create a random vector of size 10 and sort it (★★☆)
#
# **日本語:** 要素数10のランダムなベクトルを作成し、並べ替えよ。

# %%

# %% [markdown]
# ## 41. How to sum a small array faster than np.sum? (★★☆)
#
# **日本語:** 小さな配列を`np.sum`より高速に合計するにはどうすればよいか。

# %%

# %% [markdown]
# ## 42. Consider two random arrays A and B, check if they are equal (★★☆)
#
# **日本語:** 2つのランダム配列`A`と`B`が等しいか確認せよ。

# %%

# %% [markdown]
# ## 43. Make an array immutable (read-only) (★★☆)
#
# **日本語:** 配列を変更不可（読み取り専用）にせよ。

# %%

# %% [markdown]
# ## 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
#
# **日本語:** 直交座標を表すランダムな10×2行列を極座標へ変換せよ。

# %%

# %% [markdown]
# ## 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
#
# **日本語:** 要素数10のランダムなベクトルを作成し、最大値を0に置き換えよ。

# %%

# %% [markdown]
# ## 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)
#
# **日本語:** `[0,1]×[0,1]`領域を覆う`x`座標と`y`座標を持つ構造化配列を作成せよ。

# %%

# %% [markdown]
# ## 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)
#
# **日本語:** 2つの配列`X`と`Y`から、コーシー行列`C`（`Cij = 1/(xi-yj)`）を作成せよ。

# %%

# %% [markdown]
# ## 48. Print the minimum and maximum representable values for each numpy scalar type (★★☆)
#
# **日本語:** NumPyの各スカラー型について、表現可能な最小値と最大値を表示せよ。

# %%

# %% [markdown]
# ## 49. How to print all the values of an array? (★★☆)
#
# **日本語:** 配列のすべての値を省略せず表示するにはどうすればよいか。

# %%

# %% [markdown]
# ## 50. How to find the closest value (to a given scalar) in a vector? (★★☆)
#
# **日本語:** ベクトル内で、指定したスカラー値に最も近い値を求めるにはどうすればよいか。

# %%

# %% [markdown]
# ## 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
#
# **日本語:** 位置`(x, y)`と色`(r, g, b)`を表す構造化配列を作成せよ。

# %%

# %% [markdown]
# ## 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
#
# **日本語:** 座標を表す形状`(100, 2)`のランダムな配列について、全点間の距離を求めよ。

# %%

# %% [markdown]
# ## 53. How to convert a float (32 bits) array into an integer (32 bits) array in place?
#
# **日本語:** 32ビット浮動小数点配列を32ビット整数配列へインプレースで変換するにはどうすればよいか。

# %%

# %% [markdown]
# ## 54. How to read the following file? (★★☆)
#
# **日本語:** 次の内容を持つファイルを読み込むにはどうすればよいか。
#
# ```
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11
# ```

# %%

# %% [markdown]
# ## 55. What is the equivalent of enumerate for numpy arrays? (★★☆)
#
# **日本語:** NumPy配列において、Pythonの`enumerate`に相当する処理は何か。

# %%

# %% [markdown]
# ## 56. Generate a generic 2D Gaussian-like array (★★☆)
#
# **日本語:** 汎用的な2次元ガウス分布状の配列を生成せよ。

# %%

# %% [markdown]
# ## 57. How to randomly place p elements in a 2D array? (★★☆)
#
# **日本語:** 2次元配列内へ`p`個の要素をランダムに配置するにはどうすればよいか。

# %%

# %% [markdown]
# ## 58. Subtract the mean of each row of a matrix (★★☆)
#
# **日本語:** 行列の各行から、その行の平均値を引け。

# %%

# %% [markdown]
# ## 59. How to sort an array by the nth column? (★★☆)
#
# **日本語:** 配列を第n列の値に基づいて並べ替えるにはどうすればよいか。

# %%

# %% [markdown]
# ## 60. How to tell if a given 2D array has null columns? (★★☆)
#
# **日本語:** 指定した2次元配列にゼロだけで構成された列があるか判定するにはどうすればよいか。

# %%

# %% [markdown]
# ## 61. Find the nearest value from a given value in an array (★★☆)
#
# **日本語:** 配列内から、指定した値に最も近い値を求めよ。

# %%

# %% [markdown]
# ## 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)
#
# **日本語:** 形状`(1, 3)`と`(3, 1)`の2配列について、イテレータを使って和を計算するにはどうすればよいか。

# %%

# %% [markdown]
# ## 63. Create an array class that has a name attribute (★★☆)
#
# **日本語:** `name`属性を持つ配列クラスを作成せよ。

# %%

# %% [markdown]
# ## 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)
#
# **日本語:** 指定したベクトルについて、別のインデックスベクトルが示す各要素に1を加えよ（インデックスの重複に注意すること）。

# %%

# %% [markdown]
# ## 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)
#
# **日本語:** インデックスリスト`I`に基づいて、ベクトル`X`の要素を配列`F`へ累積するにはどうすればよいか。

# %%

# %% [markdown]
# ## 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★☆)
#
# **日本語:** `dtype=ubyte`の形状`(w, h, 3)`の画像について、異なる色の数を求めよ。

# %%

# %% [markdown]
# ## 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)
#
# **日本語:** 4次元配列について、最後の2軸を一度に合計するにはどうすればよいか。

# %%

# %% [markdown]
# ## 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)
#
# **日本語:** 1次元ベクトル`D`と、各要素の所属グループを示す同サイズのベクトル`S`を使い、`D`の各部分集合の平均を求めよ。

# %%

# %% [markdown]
# ## 69. How to get the diagonal of a dot product? (★★★)
#
# **日本語:** 内積（行列積）の対角要素だけを求めるにはどうすればよいか。

# %%

# %% [markdown]
# ## 70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)
#
# **日本語:** ベクトル`[1, 2, 3, 4, 5]`について、各値の間に3個の連続した0を挟んだ新しいベクトルを作成せよ。

# %%

# %% [markdown]
# ## 71. Consider an array of dimension (5,5,3), how to multiply it by an array with dimensions (5,5)? (★★★)
#
# **日本語:** 形状`(5, 5, 3)`の配列に、形状`(5, 5)`の配列を掛けるにはどうすればよいか。

# %%

# %% [markdown]
# ## 72. How to swap two rows of an array? (★★★)
#
# **日本語:** 配列の2つの行を入れ替えるにはどうすればよいか。

# %%

# %% [markdown]
# ## 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★)
#
# **日本語:** 頂点を共有する10個の三角形を表す10組の三つ組について、全三角形を構成する一意な線分の集合を求めよ。

# %%

# %% [markdown]
# ## 74. Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)
#
# **日本語:** `bincount`の結果に対応するソート済み配列`C`から、`np.bincount(A) == C`となる配列`A`を作成せよ。

# %%

# %% [markdown]
# ## 75. How to compute averages using a sliding window over an array? (★★★)
#
# **日本語:** 配列上のスライディングウィンドウを使って移動平均を計算するにはどうすればよいか。

# %%

# %% [markdown]
# ## 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is  shifted by 1 (last row should be (Z[-3],Z[-2],Z[-1]) (★★★)
#
# **日本語:** 1次元配列`Z`から、先頭行が`(Z[0], Z[1], Z[2])`で、以降を1要素ずつずらし、最終行が`(Z[-3], Z[-2], Z[-1])`となる2次元配列を作成せよ。

# %%

# %% [markdown]
# ## 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)
#
# **日本語:** ブール値を反転、または浮動小数点数の符号をインプレースで反転するにはどうすればよいか。

# %%

# %% [markdown]
# ## 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i (P0[i],P1[i])? (★★★)
#
# **日本語:** 2次元の直線群を表す点集合`P0`、`P1`と点`p`について、`p`から各直線`(P0[i], P1[i])`までの距離を求めよ。

# %%

# %% [markdown]
# ## 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P[j]) to each line i (P0[i],P1[i])? (★★★)
#
# **日本語:** 2次元の直線群を表す点集合`P0`、`P1`と点集合`P`について、各点`P[j]`から各直線`(P0[i], P1[i])`までの距離を求めよ。

# %%

# %% [markdown]
# ## 80. Consider an arbitrary array, write a function that extracts a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★)
#
# **日本語:** 任意の配列について、指定要素を中心とする固定形状の部分配列を抽出する関数を作成せよ（必要な箇所は`fill`値で埋める）。

# %%

# %% [markdown]
# ## 81. Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to generate an array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]? (★★★)
#
# **日本語:** 配列`Z = [1,2,...,14]`から、`R = [[1,2,3,4], [2,3,4,5], ..., [11,12,13,14]]`を生成せよ。

# %%

# %% [markdown]
# ## 82. Compute a matrix rank (★★★)
#
# **日本語:** 行列のランクを計算せよ。

# %%

# %% [markdown]
# ## 83. How to find the most frequent value in an array?
#
# **日本語:** 配列内で最も頻繁に現れる値を求めるにはどうすればよいか。

# %%

# %% [markdown]
# ## 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)
#
# **日本語:** ランダムな10×10行列から、連続するすべての3×3ブロックを抽出せよ。

# %%

# %% [markdown]
# ## 85. Create a 2D array subclass such that Z[i,j] == Z[j,i] (★★★)
#
# **日本語:** `Z[i, j] == Z[j, i]`となる2次元配列のサブクラスを作成せよ。

# %%

# %% [markdown]
# ## 86. Consider a set of p matrices with shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★)
#
# **日本語:** 形状`(n, n)`の`p`個の行列と形状`(n, 1)`の`p`個のベクトルについて、`p`個の行列積の和を一度に計算せよ（結果の形状は`(n, 1)`）。

# %%

# %% [markdown]
# ## 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)
#
# **日本語:** 16×16配列について、ブロックサイズ4×4のブロック和を求めよ。

# %%

# %% [markdown]
# ## 88. How to implement the Game of Life using numpy arrays? (★★★)
#
# **日本語:** NumPy配列を使ってライフゲームを実装せよ。

# %%

# %% [markdown]
# ## 89. How to get the n largest values of an array (★★★)
#
# **日本語:** 配列から大きい方からn個の値を取得するにはどうすればよいか。

# %%

# %% [markdown]
# ## 90. Given an arbitrary number of vectors, build the cartesian product (every combination of every item) (★★★)
#
# **日本語:** 任意個数のベクトルから直積（各ベクトルの全要素の全組み合わせ）を作成せよ。

# %%

# %% [markdown]
# ## 91. How to create a record array from a regular array? (★★★)
#
# **日本語:** 通常の配列からレコード配列を作成するにはどうすればよいか。

# %%

# %% [markdown]
# ## 92. Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★)
#
# **日本語:** 大きなベクトル`Z`について、3通りの方法で`Z`の3乗を計算せよ。

# %%

# %% [markdown]
# ## 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★)
#
# **日本語:** 形状`(8, 3)`の配列`A`と形状`(2, 2)`の配列`B`について、`B`の各行の要素を順序に関係なく含む`A`の行を求めよ。

# %%

# %% [markdown]
# ## 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3]) (★★★)
#
# **日本語:** 10×3行列について、値がすべて同一ではない行（例：`[2, 2, 3]`）を抽出せよ。

# %%

# %% [markdown]
# ## 95. Convert a vector of ints into a matrix binary representation (★★★)
#
# **日本語:** 整数ベクトルを、各整数の二進表現を並べた行列へ変換せよ。

# %%

# %% [markdown]
# ## 96. Given a two dimensional array, how to extract unique rows? (★★★)
#
# **日本語:** 2次元配列から一意な行を抽出するにはどうすればよいか。

# %%

# %% [markdown]
# ## 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)
#
# **日本語:** 2つのベクトル`A`と`B`について、内積、外積、合計、要素積に相当する`einsum`式を書け。

# %%

# %% [markdown]
# ## 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)?
#
# **日本語:** 2つのベクトル`(X, Y)`で表される経路を、等間隔の点としてサンプリングするにはどうすればよいか。

# %%

# %% [markdown]
# ## 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★)
#
# **日本語:** 整数`n`と2次元配列`X`について、整数のみを含み、行の合計が`n`となる、多項分布の試行結果と解釈できる行を`X`から選択せよ。

# %%

# %% [markdown]
# ## 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★)
#
# **日本語:** 1次元配列`X`の平均について、ブートストラップ法による95%信頼区間を計算せよ（復元抽出をN回行い、各標本の平均を計算して、その平均群のパーセンタイルを求める）。

# %%
