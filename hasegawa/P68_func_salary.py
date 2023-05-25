# 関数を定義

def calc_salary(payment):
# 100万以下の税額と支給額を計算
    if int(payment) <= 1000000:
        tax_under_million = int(payment*0.1)
        pay_amount = int(payment - tax_under_million)
        print("給与:"+str(payment)+"、"+"支給額:"+str(pay_amount)+"、"+"税額:"+str(tax_under_million)+"、")
# 100万を超えるの税額と支給額を計算        
    else:
        tax_over_million = int((payment-1000000)*0.2 + 100000)
        pay_amount = int(payment-tax_over_million)
        print("給与:"+str(payment)+"、"+"支給額:"+str(pay_amount)+"、"+"税額:"+str(tax_over_million)+"、")