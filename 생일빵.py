'''
문제
cho함수: 나이를 인자값으로 넣으면 긴초, 짧은초 개수와 그림을 출력한다.

punch 함수: 나이를 인자값으로 넣으면 퍽을 나이만큼 출력한다. 단 한줄에 10개씩


함수 호출 코드
cho(24)
punch(24)


실행결과
생일초 긴초: 2개, 짧은초: 4개입니다.
   **
   ||****
   ||||||
------------
|          |
|          |
|          |
------------

퍽 퍽 퍽 퍽 퍽 퍽 퍽 퍽 퍽 퍽
퍽 퍽 퍽 퍽 퍽 퍽 퍽 퍽 퍽 퍽
퍽 퍽 퍽 퍽

'''

def cho(age):
    long_candle = age//10
    short_candle = age%10
    print("생일초 긴 초",long_candle,"개, 짧은 초", short_candle, "개 준비해드리겠습니다.")
    hap = long_candle+short_candle
    print("   "+("* ")*(age//10))
    print("   "+("| ")*(age//10)+("* ")*(age%10))
    print("   "+("| ")*(age//10+age%10))
    print("--------------------------------------------")
    print("|                                          |\n"*4)
    print("--------------------------------------------")


def punch(age):
    for i in range(age//10):
        print("퍽"*10)
    print("퍽"*(age%10))

name = input("이름을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))
print(name+"님 생일 축하드려요~**")
cho(age)
punch(age)




















