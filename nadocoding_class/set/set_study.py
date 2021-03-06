# set (집합)
# 중복안됨, 순서없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (둘다 모두 가능한 사람)
print(java & python)
print(java.intersection(python))

# 합집합 
print(java | python)
print(java.union(python))

# 차집합(자바는 할 수 있지만 파이썬은 못하는 개발자)
print(java - python)
print(java.difference(python))

# 파이썬을 할 수 있는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)





