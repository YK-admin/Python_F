from introfamily import IntroFam
import sys
args = sys.argv

# 引数代入
name = args[1]
age = args[2]
cat_name = args[3]

me = IntroFam(name, age, cat_name)

print(me.name_out())
print(me.age_out())
print(me.cat_name_out())