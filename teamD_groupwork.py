n = input("2~6 사이 정수 입력: ")

array = [[3, 8, 9], [4, 12, 7], [4, 8, 5]]

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

    sub_min_row(3)
    sub_min_col(3)
    print(array)
