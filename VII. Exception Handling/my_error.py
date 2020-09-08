# 219
class MyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class NotEvenNumberError(Exception):
    def __str__(self):
        return "아니 짝수만 더할 수 있다고; 류현서"

def even_number_add(a, b):
    if a % 2 != 0 or b % 2 != 0:
        raise NotEvenNumberError
    return a + b

try:
    a = even_number_add(2, 2)
    print(str(a))               # 4
    b = even_number_add(4, 2)
    print(str(b))               # 6
    c = even_number_add(2, 1)
    print(str(c))               # NotEvenNumberError
except NotEvenNumberError as e:
    print(e)
    print("짝수만 더할 수 있습니다.")