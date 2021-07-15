import random

numbers = range(1, 46)
#range(a, b)    a는 범위에 포함되고 b는 포함되지 않는다
#1~45니까 b는 46
#random.sample(seq, k) : 시퀀스에서 중복되지 않는 랜덤한 길이 k의 리스트를 반환

print('로또번호는 : ', random.sample(numbers, 7)) #맨 마지막 수는 보너스
# 3개 맞으면 5등
# 4개 맞으면 4등
# 5개 맞으면 3등
# 5+1개 맞으면 2등
# 6개 맞으면 1등