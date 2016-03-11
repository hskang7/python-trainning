print('수를 입력하세요 : ')
a = int(input())

if a > 10 :
    if a % 2 == 0 :
        print('10보다 큰 짝수')
    else :
        print('10보다 큰 홀수')        
else :
    if a % 2 == 0 :
        print('10이하의 짝수')
    else :
        print('10이하의 홀수')