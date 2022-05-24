n = input("2~6 사이 정수 입력: ")

array = [[1, 8, 7], [4, 3, 9], [5, 2, 6]]

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
