import sys
args = sys.argv

input_salary = int(args[1])

if int(input_salary) <= 1000000:
    tax_under_million = int(input_salary*0.1)
    payment = int(input_salary-tax_under_million)
    print("支給額:"+str(payment) + "、税額:" + str(tax_under_million), end="")
else:
    tax_over_million = int((input_salary-1000000)*0.2 + 100000)
    payment = int(input_salary-tax_over_million)
    print("支給額:"+str(payment) +"、税額:"+ str(tax_over_million), end="")