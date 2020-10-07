def  phonenumber_to_region(phone):
    phone_numbers = {"02": "서울", "051": "부산", "053": "대구", "032" : "인천",
                     "062": "광주", "042": "대전", "052": "울산", "044": "세종",
                     "031": "경기", "033": "강원", "043": "충북", "041": "충남",
                     "063": "전북", "061": "전남", "054": "경북", "055": "경남",
                     "064": "제주", "010":"휴대전화", "070":"인터넷전화"}

    phoneNum = "".join(phone.split("-"))
    phones=""

    for i in range(3):
        phones += phoneNum[i]

    for key, val in phone_numbers.items():
        if("02" in phones):
            return "서울"
        if(phones == key):
            return val


r1 = phonenumber_to_region("010-2357-9607")
r2 = phonenumber_to_region("062-872-4071")
r3 = phonenumber_to_region("031-872-4071")
print(r1)
print(r2)
print(r3)