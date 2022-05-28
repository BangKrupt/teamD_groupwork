import random, pandas

n = int(input("2~6사이 정수를 입력하세요:"))

# Part 1(데이터 생성): 사용자가 n의 값을 입력하면, n by n matrix 생성하고 1~100 사이 무작위 정수로 구성함.
def CreateRandomData(n):
    data = {}
    for i in range(1, n + 1):
        data["작업{}".format(i)] = [random.randrange(1, 101) for i in range(1, n + 1)]
    df = pandas.DataFrame(data)
    df.index = ['기계{}'.format(i) for i in range(1, n + 1)]
    print(df, '\n')
    global array
    array = [list(df.iloc[j]) for j in range(n)]

# Part 2(Simple Solution) : 기계 1부터 기계 n까지 순차적으로 최소비용의 작업 구하기
def find_smallest():
    print('Simple solution is :')
    indexlist = []
    for i in range(n):
        machine = '기계'+str(i + 1)
        while True:
            cost = min(array[i])
            costindex = array[i].index(cost)
            if costindex not in indexlist:
                work = '작업' + str(array[i].index(cost) + 1)
                indexlist.append(costindex)
                break
            else:
                array[i][costindex] = max(array[i]) + 1
        print('{} : {} (Cost:{})'.format(machine, work, cost))

# Part 2-1(Optimal Solution) - In progress
def sub_min_row(size):
    min_row = [min(row) for row in array]
    for i in range(size):
        for j in range(size):
            array[i][j] -= min_row[i]

def sub_min_col(size):
    min_col = [min(col) for col in zip(*array)]
    for i in range(size):
        for j in range(size):
            array[j][i] -= min_col[i]

if __name__ == '__main__':
    CreateRandomData(n)
    find_smallest()

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