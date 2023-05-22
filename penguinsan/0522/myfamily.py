# myfamily.py
from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, cat_name):
        super().__init__(name, age)
        self.cat_name = cat_name

    def cat_out(self):
        return f"飼い猫の名前は{self.cat_name}です"

    def my_intro(self):
        intro_text = super().my_intro()  # Introクラスのメソッドを呼び出す
        cat_text = self.cat_out()  # IntroFamクラスのメソッドを呼び出す
        return intro_text + "、" + cat_text

if __name__ == "__main__":
    import sys

    # コマンドライン引数から名前、年齢、飼い猫の名前を取得
    name = sys.argv[1]
    age = sys.argv[2]
    cat_name = sys.argv[3]

    # IntroFamクラスのインスタンスを作成
    intro_fam = IntroFam(name, age, cat_name)

    # my_introメソッドを呼び出して結果を表示
    result = intro_fam.my_intro()
    print(result)
