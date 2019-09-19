
# 과제1_2장
# 점프투 파이썬 2장의 내용을 과제로 냈습니다.
# 설치가 끝난 사람은 과제도 한번 풀어 보세요.
# 1. 변수 a,b에 각각 30 과 30.5를 할당하세요
# In [ ]:
a = 30
b = 30.5
# 2. 변수 a와 b의 자료형을 출력하세요
# type() 함수 : 변수의 자료형을 확인하는 함수
# In [ ]:
print(type(a))
print(type(b))
# 3. 변수 c 에 hello world을 문자열 자료형으로 값을 할당하고 이 문자열의 길이를 출력하세요
# len()함수 : 문자열의 길이를 확인하는 함수
# In [ ]:
c = 'hello world'
print(len(c))
# 4. 변수 c의 hello world에서 world만 출력하세요
# offset인덱스 사용. [숫자:숫자]
# In [ ]:
print(c[6:])
# 5. 변수 d를 역순으로 출력하세요.
# offset인덱스 사용[숫자:숫자:숫자] 역순이 되게 하는 stride 사용
# In [3]:
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = d[-1:-11:-1]
print(d)
# 6. join함수를 사용하여 리스트 안의 원소를 하나의 문자열로 합쳐 보세요
# In [5]:
# k = ['I', 'like', 'python', 'and', 'programing']
# In [6]:
# #이렇게 한문장으로 만드세요. "I like python and programing"
# In [ ]:
k = ['I', 'like', 'python', 'and', 'programing']
print(" ".join(k))
# 7. 국어 :80, 수학: 90, 영어: 100 점인 data가 있다 이 data를 dictionary type으로 하나의 변수에 할당하세요.
# In [ ]:
scores = {'국어':80, '수학':90, '영어':100}
print(scores)
# 8. 위에 할당한 dictionary에 과학 88점을 추가하세요.
# In [ ]:
scores['과학'] = 88
print(scores)
# 9. 변수 i를 split함수를 써서 list type 으로 변환하세요
# In [7]:
# i = ["I", "like", "a", "python"]
i = "I like a python"
i = i.split(" ")
print(i)

# 10. format을 이용하여 다음 값을 출력하세요
# "나는 사과를 a개 먹었습니다에서 a에 할당한 상수 값이 들어오게 하세요"
# In [10]:
from random import *
a = randint(1,100)
# In [11]:
print(f'나는 오늘 사과를 %d개 먹었습니다.' % a  )

