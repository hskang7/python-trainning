print('요일(월~일)을 입력하세요 : ')
dow = input()

if dow == '월' :
    print('Monday')
elif dow == '화' :
    print('Tuesday')
elif dow == '수' :
    print('Wednesday')
elif dow == '목' :
    print('Thursday')
elif dow == '금' :
    print('Friday')
elif dow == '토' :
    print('Saturday')
elif dow == '일' :
    print('Sunday')
else :
    print('잘못 입력된 요일입니다.')