# input() >> 한 줄 입력받기
# input()의 결과는 문자열 '25' >> 25 정수로 바꿔줘야함
# 정수형 문자열을 정수로 바꾸는 함수 int('문자열')

N = int(input())

i=0
result=0

while i<N:
    i += 1
    result = result+i

print(result)