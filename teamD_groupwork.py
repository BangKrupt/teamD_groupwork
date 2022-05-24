import os
import datetime

n = int(input("2~6 사이 정수 입력: "))
if n not in [2,3,4,5,6]:
    raise ValueError("2~6 사이 정수가 아닙니다.")


if not os.path.isdir("output"):
    os.mkdir("output")

if not os.path.exists("output/result.txt"):
    f = open("output/result.txt",'w',encoding="utf8")
    f.write("기록시작.\n")
    f.close()

with open("output/result.txt",'a',encoding="utf8") as f:
    stamp = str(datetime.datetime.now())
    log_line = stamp + "\t" + "데이터 생성됨.\n"
    f.write(log_line)