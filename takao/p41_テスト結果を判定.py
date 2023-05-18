import sys
args = sys.argv

math = int(args[1])
jap = int(args[2])
eng = int(args[3])


if ((math>=70 and jap>=70 and eng>=70) or (math+jap+eng >= 270)):
    if (math>=50 and jap>=50 and eng>=50):
        print("合格",end="")
    else: print("不合格",end="")
else: print("不合格",end="")

# if (math+jap+eng >= 270) and (math>=50 and jap>=50 and eng>=50):
#     print("合格",end="")
# else: 
#     print("不合格",end="")


