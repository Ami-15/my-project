# 変数は、データ（数字や文字など）を入れておく「名前のついた箱」みたいなもの
# name という箱に "たろう" を入れてる.age という箱に 14 という数字を入れてる.
name = "たろう"  # " や ' で囲んだ部分は 文字（文字列）と呼ばれてる
age = 14

# 何かを画面に表示したいときは print() を使う
print("こんにちは！")
print(name)
print("年齢は", age, "歳です")

# f文字列 f"〜" の中に {変数} を書くと、その中身を文字にそのまま入れて表示できる
print(f"こんにちは、{name}さん！")
# f文字列がないとき
print("こんにちは、" + name + "さん！")

# if文（条件分岐）　: を忘れない。インデント（字下げ）はスペース4つ or タブ1つ（どっちかに統一）
age = 14
if age >= 13:
    print("中学生以上です")
else:
    print("小学生以下です")
# 比較演算子
#     == | 等しいか    | x == 10
#_    != | 等しくないか | x != 10
#      > | より大きいか | x > 5
#      < | より小さいか | x < 100
#     >= | 以上か      | x >= 18
#     <= | 以下か      | x <= 30
age = 15
if age >= 20:
    print("お酒が飲める年齢です。")
elif age >= 18:    #elif（それ以外の条件)  何回でも使える
    print("成人だけどお酒はまだだよ。")
else:    #else（それ以外全部）
    print("未成年です。")

# for文（くり返し） range(5) は「0から4まで」の5回くり返す
for i in range(5):
    print(i)

# 関数 何回も使う処理をひとまとめにしたもの。
def say_hello(name):     #def で関数をつくる say_hello が関数の名前
    print("こんにちは、" + name + "さん！")    # name は受け取るデータ（引数）
say_hello("たろう")
say_hello("はなこ")

# リスト（リスト＝箱の集まり） データをいくつもまとめて入れておける。
fruits = ["りんご", "バナナ", "みかん"]

for fruit in fruits:
    print(fruit)


# 文字列（str）
name = "太郎"
print(type(name))  # <class 'str'>

# 数値（int）
age = 25
print(type(age))   # <class 'int'>

# 浮動小数点（float）
height = 170.5
print(type(height))  # <class 'float'>


a = 10
b = 5
print(a + b)  # 足し算
print(a - b)  # 引き算

#文字列結合とf-stringの使い方
# 文字列の結合
first_name = "太郎"
last_name = "山田"
full_name = first_name + " " + last_name
print(full_name)  # 結果: 山田 太郎
# f-stringを使った文字列の結合
age = 25
print(f"{full_name}さんは{age}歳です")  # 結果: 山田 太郎さんは25歳です
