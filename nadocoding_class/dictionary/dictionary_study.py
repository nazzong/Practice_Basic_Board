cabinet = {3:"유재석", 100:"김태호"}
# dictionary = {key:value}
print(cabinet[3])
# print(cabinet[5])  값이없을때 오류로 출력안됨

print(cabinet.get(3))
print(cabinet.get(5)) # 값이 없어도 get을 사용하면 none으로 출력가능
print(cabinet.get(5, "사용가능")) # True일때 5에 해당하는 값을 출력하고, False일때 ,콤마 뒤 값을 출력한다. get(True, False)
print(cabinet.get(100, "사용가능")) #100이 True 이기 때문에 김태호가 출력된다.
print("출력")

# (key in dictionary) = True/False 를 출력한다.
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"} # key값은 문자열도 가능


# 새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간손님
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)




