# #for 연습
# #구구단 7단 출력하기
# for i in range(1, 9+1):
#     print("7 X", i, "=", (7*i));

#구구단 2-9단 출력하기
#dan 2-9
for dan in range(2,9+1):    #2-9
    for i in range(1, 9+1): #1-9
        print(dan ,"X", i, "=", (dan * i)); #i:1-9
    print("----------")