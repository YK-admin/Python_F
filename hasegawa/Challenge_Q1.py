import sys
args = sys.argv

input_num = int(args[1])

factoring_list = []

for prime in range(2, input_num + 1):
    while input_num % prime == 0:
        factoring_list.append(prime)
        input_num = input_num // prime

    else:
        prime += 1

print(factoring_list, end="")
