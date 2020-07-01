# score_file = open("score.txt","w",encoding="utf8")
# print("수학 :0",file = score_file)
# print("영어 :50", file = score_file)
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end='')
# print(score_file.readline())

# import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름" : "우승일","나이":28 ,"취미":["운동","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file)
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

#import pickle
# with open('profile.pickle',"rb") as profile_file:
#     print(pickle.load(profile_file))


# with open('study.txt','w',encoding='utf8') as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있습니다.")
# with open('study.txt','r',encoding='utf8') as study_file:
#     print(study_file.read())

# import inspect
# import random
# print(inspect.getfile(random))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir(random))

# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제 에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리 표시

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# # print("오늘 날짜는 ",datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# print("오늘 날짜는", today)
# td = datetime.timedelta(days=100) 
# print("우리가 만난지 100일은 ", today + td)

# 모듈 사용 예제
import byme
byme.sign()