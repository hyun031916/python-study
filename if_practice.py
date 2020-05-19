#if 연습
#멤버수로 아이돌 찾기. 10:nct127, 9:EXO, 7:방탄소년단, 4:마마무, 13:슈퍼주니어, 그외 : 못찾았어요
member = int(input("아이돌을 찾아보자. 멤버수를 입력하라 : "))
if member == 10:
    print("nct127")
elif member==9:
    print("EXO")
elif member==7:
    print("방탄소년단")
elif member == 4:
    print("마마무")
elif member == 13:
    print("슈퍼주니어")
else:
    print("못 찾았어요.")