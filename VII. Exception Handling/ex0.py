# p211
# print(10/0)     # infinity
# spam = 10
# print(4 + spam * 3)
# print('2' + 2)

# java
'''
try {
    exception 날법한 명령문
} catch (발생할 Exception e) {

} catch (Exception e) {

} finally {
    exception이 발생하든 안하든 무조건 실행할 명령문
}
'''

'''
python
try:
    명령문
except:
    예외 발생하면 처리하는 코드
else:
    예외 처리 되지 않으면 여기 실행
finally:
    무조건 실행하는 명령문
'''

list1 = [1, 2, 3]

# print(list1[2])
# print(list1[3])

try:
    print(list1[2])     # 정상실행
    print(list1[3])     # 예외발생
    print(list1[2])     # 실행안됨
except:
    print("리스트의 요소에 접근하지 못했습니다.")

print("-"*40)

f = open("file.txt", "w")

try:
    f.write("Hello World")      # 정상실행
    f.write(100)                # 예외발생
except:
    print("타입 예외 발생(100은 쓸 수 없습니다.)")
finally:
    print("예외 여부와 상관없이 무조건 실행합니다.")
    f.close()

print("-"*40)

# p217
list2 = [1, 2, 3]
try:
    print(list2[4])     # IndexError 발생
except IndexError as e:
    print(e)

list3 = [1, 2, 3]
try:
    print(list3[0])    # 1
    print(list3[1])    # 2
    print(list3[2])    # 3
    print(list3[3])    # IndexError
except :
    print("예외발생")
else :
    print("성공적으로 모든 코드를 실행되었습니다.")