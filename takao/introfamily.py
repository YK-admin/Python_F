import myself

class IntroFam(myself.Intro):
    def __init__(self, name, age, cat):
        super().__init__(name, age) # 継承
        self.cat = cat # 新しく定義

    def cat_out(self):
        cattxt = "飼い猫の名前は、" + self.cat + "です"
        return cattxt
    
    def print_all(self):
        print(self.name_out())
        print(self.age_out())
        print(self.cat_out())