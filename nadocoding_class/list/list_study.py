# list []

subway = [10, 20, 30]
print(subway)


subway = ["유재석", "조세호", "박명수"]
print(subway)


# 조세호가 어디 타고 있는가?
print(subway.index("조세호"))


# 하하 추가
subway.append("하하")
print(subway)

# 정형돈을 유재석과 조세호 사이에 넣기
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())

# 같은 이름의 사람이 몇명있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 뒤집기
num_list.reverse()
print(num_list)

# 모두지우기
# num_list.clear()
print(num_list)


# 리스트 확장
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)



