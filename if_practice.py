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
#
# #평점 매기기. 90 이상 : A, 80 이상 90 미만: B, 70점 이상 80미만 : C, 60점 이상 70미만: F
# score = int(input("당신의 점수는?"))
# if 90<=score:
#     print("A")
# elif 80<=score:  #java : 80<=score && score<90
#     print("B")
# elif 70<=score:
#     print("C")
# elif score<70:
#     print("F")

#학번 => 학년, 학과, 반, 번호 분석하기
student_number = input("당신의 학번은 : ")    #2310
grade = student_number[0];
classroom = student_number[1];
major = "null"; #1, 2: 뉴미디어소프트웨어, 3, 4: 뉴미디어웹솔루션, 5, 6: 뉴미디어디자인
if classroom == "1" or classroom == "2":
    major="뉴미디어소프트웨어"
elif classroom == "3" or classroom == "4":
    major="뉴미디어웹솔루션"
elif classroom == "5" or classroom == "6":
    major="뉴미디어디자인"
number = student_number[2:];
print(grade,"학년 ", major,"과 ", classroom,"반 ", number,"번입니다.")

