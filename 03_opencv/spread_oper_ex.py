#가변 매개변수 사용 연습 !! ( * << 이거~)

# 함수를 정의할때 *를 사용하면 가변 변수
# 함수를 호출할때 *를 사용하면 펼침 연산자 / Spread Operator

def xtest(*argv):
    print(type(argv))
    print("len: ", len(argv))
    print("================")
    for i in argv:
        print(i)

# xtest(1, 2, 3, 4, 5)
# xtest(1, 2, 3)

# data = [1, 2, 3, 4, 5]
# xtest(data, 1, 2)
# xtest(*data, 3, 4) # 펼침(spread) 연산자 


# data2="1234"
# xtest(*data2) # 이러면 매개변수가 글자의 개수만큼 넘어감 즉, 4개가 넘어감

def xtest2(*argv, a=10, b=20):
    print(type(argv))
    print("len: ", len(argv))
    print("================")
    for i in argv:
        print(i)
    print(a, b)

xtest2(a=100, b=200)
t = {
    'a':300,
    'b':400
}

# xtest(a=300, b=400)의 의미
xtest2(**t) 
# 딕셔너리를 펼칠때는 *를 2개 써야함 !!!
