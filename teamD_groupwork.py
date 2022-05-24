import random,pandas

def main():
    n=int(input("2~6사이 정수를 입력하세요:"))
    CreateRandomData(n)

# Part 1(데이터 생성): 사용자가 n의 값을 입력하면, n by n matrix 생성하고 1~100 사이 무작위 정수로 구성함.
def CreateRandomData(n):
    data={}
    for i in range(1,n+1):
        data["작업{}".format(i)]=[random.randrange(1,101) for i in range(1,n+1)]
    df = pandas.DataFrame(data)
    df.index=['기계{}'.format(i) for i in range(1,n+1)]
    print(df)


main()
