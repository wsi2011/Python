# starbucks = ['아이언맨','토르','헐크']
# for customer in starbucks:
#     print("{0}, 커피가 준비 되었습니다" .format(customer))

#while
# customer = '토르'
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer,index))
#     index -= 1 
#     if index == 0:
#         print('커피는 폐기처분 되었습니다.')

#continue & break
# absent = [2,5] 
# no_book = [7]
# for student in range(1,11):
#     if student == absent :
#         continue
#     elif student in no_book:
#         print('오늘 수업 여기까지. {0}는 교무실로 따라와'.format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# from random import *
# cnt = 0 
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[o] {0}번째 손님 (소요시간:{1}분".format(i,time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간:{1}분)".format(i,time))

# print(cnt)

# def std_weight(height,gender):
#     if gender == '남자':
#         return height * height *22
#     else:
#         return height *height *21

# height = 175
# gender = '남자'
# weight = round(std_weight(height/100,gender),2)
# print("키 {0} cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))

