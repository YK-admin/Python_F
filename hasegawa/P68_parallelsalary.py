# func_salaryの関数をP68_func_salaryモジュールからインポート

from P68_func_salary import calc_salary

import sys
args = sys.argv

# argsをリストに代入
list_salary = args[1:]

# for文で一個ずつ関数に値を渡す
for input_salary in list_salary:

    input_salary = calc_salary(int(input_salary))