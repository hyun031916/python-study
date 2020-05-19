# #for 연습
# #구구단 7단 출력하기
# for i in range(1, 9+1):
#     print("7 X", i, "=", (7*i));
# 
# #구구단 2-9단 출력하기
# #dan 2-9
# for dan in range(2,9+1):    #2-9
#     for i in range(1, 9+1): #1-9
#         print(dan ,"X", i, "=", (dan * i)); #i:1-9
#     print("----------")

#N자리수의 각 자리 숫자합 출력하기 (for문 이용) 331=>7
num = input("숫자를 입력하세요 : ")
sum = 0
for ch in num:
    sum += int(ch)
# for i in range(0, len(num)):
#     n = num[i]
#     #sum에 더하기
#     sum+= int(n)
#sum 출력
print(sum)
#369 게임 1 2 짝 4 5 짝 7 8 짝 10 11 12 짝
#전화번호부 만들고, 이름으로 검색하기
#주차요금 계산하기, 최초 30분 2000원, 10분당 1000원, 25000원 넣을 수 있음
#야구게임,
