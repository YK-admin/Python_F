from introduce import Intro
import sys
args = sys.argv

# 引数
name = sys.argv[1]
age = sys.argv[2]

selfintro = Intro(name, age)
print(selfintro.name_out())
print(selfintro.age_out())