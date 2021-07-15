#조건에 따른 실행문장 선택하기 : 조건문
#미세먼지 농도(dust)의 값이 50초과이면 '50초과' 50이하이면 '50이하'를 출력
import random

dusts = [30, 45, 66, 72, 25, 13, 58, 44, 60, 75, 89, 80, 123, 138, 156, 149, 111, 182, 173, 164, 95, 103, 71, 69, 83, 136, 150]
randust = random.choice(dusts)

dust = 55

# if 조건문:        #조건문 안에는 참/거짓을 따질 수 있는 표현식(expression)이 들어가야한다
#     실행할 문장
# else:
#     실행할 문장

if dust >50:
    print('50 초과')
elif dust <= 50:
    print('50이하')

print(randust)
if randust >50:
    print('50 초과')
else:
    print('50 이하')

#0~30, 31~80, 81~150, 151~
#순차적으로 진행하면서 위의 조건이 만족시 아래 elif는 실행하지 않으므로 잘못된 코드(반대로 해야한다)
if randust <=30:
    print('좋음')
elif 80>= randust >30:
    print('보통')
elif 150>= randust >80:
    print('나쁨')
elif randust >150:
    print('매우나쁨')