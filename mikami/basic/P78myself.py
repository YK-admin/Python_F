import P78introduce
import sys
args = sys.argv

inputName = args[1]
inputAge = args[2]

sosukeIntoro = P78introduce.Intro(inputName, inputAge)
print(sosukeIntoro.name_out())
print(sosukeIntoro.age_out())