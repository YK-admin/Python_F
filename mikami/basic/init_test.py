class Intro:
    address = None
    
    def __init__(self):
        self.name = None
        self.age = None
    
sample = Intro()

print(sample.name)
print(sample.age)

sample.name = "太郎"
sample.age = 30

print(sample.name)
print(sample.age)

sample2 = Intro()

print(sample2.name)
print(sample2.age)