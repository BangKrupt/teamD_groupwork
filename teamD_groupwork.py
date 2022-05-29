import random, pandas
from scipy.optimize import linear_sum_assignment

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

# Part 2-1(Optimal Solution) - Using scipy package
def Hungarian(array):
    row, col = linear_sum_assignment(array)
    minimized_cost = 0
    for m in range(0, n):
        minimized_cost += array[m][col[m]]
    print('\nOptimal solution is : Cost {}'.format(minimized_cost))

if __name__ == '__main__':
    CreateRandomData(n)
    find_smallest()
    Hungarian(array)