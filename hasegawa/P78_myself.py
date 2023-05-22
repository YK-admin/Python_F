import sys
args = sys.argv
from P78_introduce import Intro

My_name = args[1]
My_age = args[2]

My_intro = Intro(My_name, My_age)

print(My_intro.name_out())
print(My_intro.age_out())