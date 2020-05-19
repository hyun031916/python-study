# #if 연습
# #멤버수로 아이돌 찾기. 10:nct127, 9:EXO, 7:방탄소년단, 4:마마무, 13:슈퍼주니어, 그외 : 못찾았어요
# member = int(input("아이돌을 찾아보자. 멤버수를 입력하라 : "))
# if member == 10:
#     print("nct127")
# elif member==9:
#     print("EXO")
# elif member==7:
#     print("방탄소년단")
# elif member == 4:
#     print("마마무")
# elif member == 13:
#     print("슈퍼주니어")
# else:
#     print("못 찾았어요.")

#평점 매기기. 90 이상 : A, 80 이상 90 미만: B, 70점 이상 80미만 : C, 60점 이상 70미만: F
score = int(input("당신의 점수는?"))
if 90<=score:
    print("A")
elif 80<=score:  #java : 80<=score && score<90
    print("B")
elif 70<=score:
    print("C")
elif score<70:
    print("F")

