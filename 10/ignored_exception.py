my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요:")
    index = int(input())
    print(my_list[index]/0)
except Exception as err:    
    print("1) 예외가 발생했습니다. ({0})".format(err))
except ZeroDivisionError as err:
    print("2) 0으로 나눌 수 없습니다. ({0})".format(err))
except IndexError as err:
    print("3) 잘못된 첨자입니다. ({0})".format(err))