import random, pandas

n = int(input("2~6사이 정수를 입력하세요:"))

# Part 1(데이터 생성): 사용자가 n의 값을 입력하면, n by n matrix 생성하고 1~100 사이 무작위 정수로 구성함.
def CreateRandomData(n):
    data = {}
    for i in range(1, n + 1):
        data["작업{}".format(i)] = [random.randrange(1, 101) for i in range(1, n + 1)]
    df = pandas.DataFrame(data)
    df.index = ['기계{}'.format(i) for i in range(1, n + 1)]
    print(df)
    global array
    array = [list(df.iloc[j]) for j in range(n)]

# Part 2
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
    sub_min_row(n)
    sub_min_col(n)
    print(array)