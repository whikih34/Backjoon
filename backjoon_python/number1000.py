# input() -> 한 줄 문자열 그대로 가져오기
# split() -> 공백을 기준으로 잘라서 각각 리스트에 넣기
# map(int) -> input() 함수가 입력받은 값은 문자열이므로 map 함수가 int 함수를 적용시켜 정수형으로 바꾸기
# split()이 반환하는 자료형은 리스트이기 때문에 int() 함수를 씌울 수 없고 map() 함수를 써야 함
# 간단하게 말해면 정수를 입력받음
a, b = map(int, input().split())

answer = a + b
print(answer)

# map(function, iterable)
# 파이썬의 내장 함수로,
# 리스트 같은 반복 가능한 자료(iterable)의 각 원소에 특정 함수를 적용시켜서
# 새로운 반복자(iterator)를 만들어 주는 함수
