# 사칙연산 계산기 만들기

def main():
    #a와 b는 사칙연산에 사용되는 두 수
    a = 0
    b = 0




    while True:
<<<<<<< HEAD
        operation = input("연산 방법을 선택하세요(0: 덧셈, 1: 뺄셈, 2: 나눗셈, 3: 곱셈): ") #참고로 3 아니어도 곱셈임
=======
        a = int(input('계산할 두 번째 수를 입력하세요'))
        b = int(input('계산할 첫 번째 수를 입력하세요'))
>>>>>>> 193292039d5c9c232c548fe84ac6226b6f68ad2f


        if operation == '0':



        elif operation == '1':



        elif operation == '2':
            #나눗셈
            print(a/b)
            break
        
        else:
            #곱셈
            print(a*b)
            break
    



if __name__ == "__main__":
    main()