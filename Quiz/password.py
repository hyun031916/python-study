
# 집 비밀번호 설정 문제
#
# 집 비밀번호를 설정해야합니다
# 5~7자리의 숫자여야 하고 마지막엔 * 또는 #이 들어가야 합니다
# 동일한 숫자가 3개 이상일 수 없습니다
# *, #외의 특수문자는 들어갈 수 없습니다

def is_password(password):
	li = list()
	li = password; i=0
	if 6>len(li) or len(li)>8:
		return "False"
	if li[-1] in "*, #":
		for p in li[:-1]:
			if not p.isdigit():
				return "False"
			i = li.count(p)
			if(i >= 3):
				return "False"
		else:
			return "True"

print(is_password('1234*'))	#True
print(is_password('987654#'))	#True
print(is_password('25558#'))	#False
print(is_password('234878#'))	#True
print(is_password('23#878#'))	#False
print(is_password('#598'))	#False
print(is_password('99598'))	#False