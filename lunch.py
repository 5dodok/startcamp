import random
# 주석

menu = ['한식', '일식', '중식', '양식']
lunch = random.choice(menu)
print(menu[1])
print(lunch)

number = {'한식':'123-456', '일식':'123-456', '중식':'123-456', '양식':'123-456'}

print(number[lunch])

#오늘의 점심은 xxx입니다. 전화번호는 xxx-xxx입니다.
print('오늘의 점심은',lunch,'입니다. 전화번호는',number[lunch],'입니다')
#더 깔끔하고 쉽게 표현할 때 f : format 사용
print(f'오늘의 점심은 {lunch}입니다. 전화번호는 {number[lunch]}입니다.')