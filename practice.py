# print(abs(-5))
# print(pow(4,2))
# print(round(3.14))
# #=======================
# print("\n")
# from math import *
# print(floor(4.99)) # 내림
# print(ceil(3.14)) #올림
# print(sqrt(16)) #제곱근

# url = "http://naver.com"
# my_str = url.replace("http://","")
# #print(my_str)
# my_str = my_str.split(".")
# print(my_str[0])

cavinet = {3:"유재석", 100:"김태호"} # 자료형중 {}는 딕셔너리임.
# print(cavinet.get(5,"no value"))
# print('hi')
# print(3 in cavinet) # True
# print(5 in cavinet) # False


cavinet[5] = "조세호" # 딕셔너리에 추가
print(cavinet)

print(cavinet.items())

# 딕셔너리 전체 지우기
cavinet.clear()
print(cavinet)

