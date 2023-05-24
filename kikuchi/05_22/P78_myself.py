from introduce import Intro
import sys
args = sys.argv

# 引数代入
name = args[1]
age = args[2]

me = Intro(name, age)

print(me.name_out())
print(me.age_out())