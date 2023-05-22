import sys
args = sys.argv

food = args[1]

message = "I don't like {0}".format(food)

print(message, end="")