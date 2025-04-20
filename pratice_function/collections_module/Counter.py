from collections import Counter

#해당 리스트 내 요소들이 몇 번 나오는지 딕셔너리 형태로 반환
counter = Counter(["hi", "hey", "hi", "hi", "hello", "hey"])

print(counter)
#주의 사항 그냥 counter 변수로 사용할 경우 Counter 객체 형태로 나오므로
#dict()로 변환한 뒤에 사용할 것
print(dict(counter))

print(counter['hi'])

#가장 많이 등장하는 녀석들로 내림차순하여 [튜플, 튜플, ...] 형식으로 리턴해줌.
print(counter.most_common())

#인자를 주어 k개의 데이터만 얻을 수도 있음.(내림 차순) 
print(Counter("hello world my name is junha!").most_common(1))

print(Counter("hello world my name is junha!").most_common(4))

#산술 연선자를 사용할 수 있음 
counter1 = Counter(["A", "A", "B"])
counter2 = Counter(["A", "B", "B"])

print(counter1 + counter2)
#단 뺄 경우 0 이하가 되는 경우 딕셔너리에서 제외됨. (삭제됨)
print(counter1 - counter2)