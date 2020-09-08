# #가변인자 : 변할 수 있는 인자의 개수
def max_min(*args):
    # max_v = args[0]
    # min_v = args[0]
    # for n in args:
    #     if(n > max_v):
    #         max_v=n
    #     elif(n < min_v):
    #         min_v = n
    # return max_v, min_v
    return max(args), min(args)
max_value , min_value = max_min(6, 2, 7, 8, 3, -7)
print(max_value, min_value)
max_value, min_value = max_min(1, 9, 10, 0, -16)
print(max_value, min_value)
# #키워드 인자 : 인자에 이름이 붙어있음
# #인자 기본값 :

def print_name_age(name, age = 18):
    #print(name,"님은", age,"살")
    print("{}님은 {}살".format(name, age))
print_name_age("권혜수")       #권혜수님은 18살
print_name_age("강종아", age=17)   #강종아님은 17살
print_name_age("김수연", age="뱃")   #강종아님은 17살
# #가변 키워드 인자 : 인자에 이름이 붙어있으면서 변할 수 있는수
def say_hi(*names, hi="안녕~"):
    for name in names:
        print("{}님 {}".format(name, hi))
        
say_hi("김정아")
say_hi("김정아", "김지영")                #김정아님 안녕~ \n 김지영님 안녕~
say_hi("김정아", "김지영", hi='니하오')     #김정아님 니하오\n 김지영님 니하오