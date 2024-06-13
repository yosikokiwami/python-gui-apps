import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

"""
変数
    データを入れておく箱

データ型
    変数は決まったデータ型を持つ
    int: 数値型 ex) 1, 2, 3
    str: 文字列型 ex) "Hello", "World", "0", "123", ""

四則演算
    + - * /

関数
    処理をまとめたもの

フォーマット文字リテラル
    f"文字列 {変数名} 文字列"

"""


def add_button_action():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = int(entry1.get())  # 入力値を取得
    num2 = int(entry2.get())  # 入力値を取得
    label1.config(text=f"{num1} + {num2} = {num1 + num2}")  # 画面に出力


def sub_button_action():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    # TODO 1. 引き算の結果を表示してください
    num3 = num1 - num2
    label1.config(text=f"{num1}-{num2}={num3}")


def mul_button_action():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    num3 = num1 * num2
    label1.config(text=f"{num1}*{num2}={num3}")


def div_button_action():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    num3 = num1 / num2
    label1.config(text=f"{num1}/{num2}={num3}")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
entry2 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry2.pack(pady=10)

# ボタンの作成
# 足し算ボタン
button1 = tk.Button(window, text="+", command=add_button_action)  # 足し算ボタン
button1.pack(pady=10)

# 引き算ボタン
button2 = tk.Button(window, text="-", command=sub_button_action)  # 引き算ボタン
button2.pack(pady=10)

# TODO 2. 掛け算ボタン (button3) を作成してください
button3 = tk.Button(window, text="*", command=mul_button_action)  # 引き算ボタン
button3.pack(pady=10)

# TODO 3. 割り算ボタン (button4) を作成してください
button4 = tk.Button(window, text="*", command=div_button_action)  # 引き算ボタン
button4.pack(pady=10)
# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
