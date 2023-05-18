# 入力した名前を表示するプログラム

# 入力した名前を受け取る
input_name = input("What's your name?")

# 指定された文字列「Hello (入力した名前) !」を変数display_nameに代入
display_name = "Hello " + input_name + " !"

print(display_name, end="")