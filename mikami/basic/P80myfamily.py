import P80introfamily
import sys
args = sys.argv

inputName = args[1]
inputAge = args[2]
inputCat = args[3]

mikamiSubIntoro = P80introfamily.IntoroFam(inputName, inputAge, inputCat)
print(mikamiSubIntoro.name_out())
print(mikamiSubIntoro.age_out())
print(mikamiSubIntoro.cat_out())
