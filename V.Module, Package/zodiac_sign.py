# 문제 :
# 생일을 입력하면 태어난 연도의 띠를 리턴해주는 함수
#
# 힌트:
# 1980년도는 원숭이 띠입니다.
# 쥐 – 소 – 호랑이 – 토끼 – 용 – 뱀 – 말 – 양 – 원숭이 – 닭 – 개 – 돼지

def zodiac_sign(birth):
    animal = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양']
    arr = ""
    num = 0
    for i in birth:
        if i == "-":
            break
        arr += i
    num = int(arr)%12
    return arr+"년도는 "+animal[num]+"의 해입니다."



# 함수 호출 코드:
print(zodiac_sign("1990-10-21"))
print(zodiac_sign("1999-10-21"))
print(zodiac_sign("2003-10-21"))
# 실행결과:
# 1990년도는 말의 해 입니다.
# 1999년도는 토끼의 해 입니다.
# 2003년도는 양의 해 입니다.

