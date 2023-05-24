import sys

def prime_f_list(num): #prime_f_list という名前の関数を定義.この関数は引数 num を受け取ります.num は素因数分解を行いたい整数.
    divisors = [] #空のリスト divisors を作成.このリストは素因数を格納するために使用される.
    for prime in range(2, num+1): # prime という変数を使って、2 から num までの範囲を反復します.これにより、素数を見つけるためのループが設定されます.
        while (num % prime) == 0: # num を prime で割った余りが 0 である間、以下の処理を繰り返します.
            divisors.append(prime) 
            num //= prime
    return divisors # ループが終了した後、divisors リストを返します.

number= int(sys.argv[1]) # コマンドライン引数から数値を取得

result = prime_f_list(number) # 素因数分解の結果を取得

print(f"{result}",end="") # 結果を出力