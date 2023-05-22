# introfamily.py
from introduce import Intro

class IntroFam(Intro):
    def cat_out(self, cat_name):
        return f"飼い猫の名前は{cat_name}です"

if __name__ == "__main__":
    import sys

    # コマンドライン引数から飼い猫の名前を取得
    cat_name = sys.argv[1]

    # IntroFamクラスのインスタンスを作成
    intro_fam = IntroFam()

    # cat_outメソッドを呼び出して結果を表示
    result = intro_fam.cat_out(cat_name)
    print(result)
