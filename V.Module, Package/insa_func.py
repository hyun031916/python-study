import hello_func
import greeting_func

def main():
    print('insa_func 모듈입니다.')
    print(f'__name__ : {__name__}') #_main__
    hello_func.hello()
    greeting_func.greeting()


main()