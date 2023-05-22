import sys
args = sys.argv
import P80

My_name = args[1]
My_age = args[2]
My_cat = args[3]

My_fam_intro = P80.IntroFam(My_name, My_age, My_cat)

print(My_fam_intro.name_out())
print(My_fam_intro.age_out())
print(My_fam_intro.cat_out())