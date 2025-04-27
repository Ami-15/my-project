# range() の基本ルール
# range(ストップ) 0からスタートして、ストップの手前まで
for i in range(5):
    print(i)
# 結果 0 1 2 3 4

# range(スタート, ストップ) タートからスタートする、ストップの手前まで
for i in range(2, 6):
    print(i)
# 結果 2 3 4 5
# Pythonの考え方「数えるとき、区切りがきれいになるように」リストの番号など、「何個分」って数える時に、すごく扱いやすいためわざと「終わりは含めない」ルールになっている

# range(スタート, ストップ, ステップ) スタートから、ステップずつ増やしながら、ストップの手前まで
for i in range(1, 10, 2):
    print(i)
# 結果 1 3 5 7 9

total = 0                  # 変数の初期化
for i in range(1, 11):     # range(1, 11) は、1から10までの数字を順番に作り出す
    total += i
print("1〜10の合計は:", total)

total = 0
for i in range(10, 0, -1):  # 逆向きにカウントダウン
    print(i)

for _ in range(5):          # 値を使わないなら、変数名を _としても良い
    print("Python最高！")
# 結果
# Python最高！
# Python最高！
# Python最高！
# Python最高！
# Python最高！

# 関数        | 何ができる？
# sum()       | 合計を出す
# list()      | リストにする
# min()       | 最小値を出す
# max()       | 最大値を出す
# reversed()  | 逆順にする
# enumerate() | 番号付きで取り出す


fruits = ["apple", "banana", "orange"]
for fruit in fruits: # fruitsリストの中から1個ずつ取り出して、fruitに入れる
    print(fruit)

for index, fruit in enumerate(fruits): # enumerate()を使うと、番号付きで取り出せる
    print(f"{index + 1}番目のフルーツは {fruit} です！")

for fruit in fruits:
    print(fruit.upper()) # .upper() は 文字を全部大文字にする関数



word = "hello"

for letter in word: # for ~ in ~: 1個ずつ順番に取り出してループできる(イテラブル（iterable）)
    print(letter)




# FizzBuzz問題
for i in range(1, 101):  # 1から100まで
    if i % 3 == 0 and i % 5 == 0:  # 3の倍数かつ5の倍数
        print("FizzBuzz")
    elif i % 3 == 0:  # 3の倍数だけ
        print("Fizz")
    elif i % 5 == 0:  # 5の倍数だけ
        print("Buzz")
    else:
        print(i)  # それ以外は数字をそのまま

# リストに結果をまとめてから表示
results = []  # 結果を保存するリスト

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        results.append("FizzBuzz")
    elif i % 3 == 0:
        results.append("Fizz")
    elif i % 5 == 0:
        results.append("Buzz")
    else:
        results.append(str(i))  # 数字も文字列に変換して追加

# 最後に結果を出力
print("\n".join(results))  #"\n".join(results) は、リストの中の文字列を改行で区切って1つにまとめる方法

# リスト内包表記 if-else を一行で書いて、リスト内包表記でまとめる
results = [
    "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
    "Fizz" if i % 3 == 0 else
    "Buzz" if i % 5 == 0 else
    str(i)
    for i in range(1, 101)
]

print("\n".join(results))

# 辞書を使って条件を簡潔にする
fizzbuzz_map = {3: "Fizz", 5: "Buzz"}

for i in range(1, 101):
    result = ""
    for key in fizzbuzz_map:
        if i % key == 0:
            result += fizzbuzz_map[key]  # FizzまたはBuzzを追加
    print(result or i)  # もしresultが空だったらi（数字）を表示

# 関数を使って分ける
def fizzbuzz(i):           # fizzbuzz(i)関数は、引数として与えられた数字 i に対して、Fizz, Buzz, FizzBuzz もしくはそのままの数字を返す。
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)

for i in range(1, 101):
    print(fizzbuzz(i))
