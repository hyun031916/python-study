myList=[]

for i in range(0, 3):
    myList.append(0)
hap = 0

for i in range(0, 3):
    myList[i] = int(input("숫자 입력 : "))

for k in range(0, 3):
    hap = hap+myList[k]

print(hap)