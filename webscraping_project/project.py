import requests
import re
from bs4 import BeautifulSoup

def create_soup(url):
    res =requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    return soup

def scrape_weather():
    print('[오늘의 날씨]')
    url='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8'
    soup = create_soup(url)

    #날씨 정보 가져오기
    cast = soup.find('p',attrs={'class':'cast_txt'}).get_text()
    temp = soup.find('p',attrs={'class':'info_temperature'}).get_text().replace('도씨','')
    min_temp = soup.find('span',attrs={'class':'min'}).get_text()
    max_temp = soup.find('span',attrs={'class':'max'}).get_text()
    morning_rain_rate = soup.find('span',attrs={'class':'point_time morning'}).get_text().strip()
    afternoon_rain_rate = soup.find('span',attrs={'class':'point_time afternoon'}).get_text().strip()
    
    toxic_haze = soup.find('dl',attrs={'class':'indicator'})
    fine_dust = toxic_haze.find_all('dd')[0].get_text()
    ultrafine_dust =toxic_haze.find_all('dd')[1].get_text()

    print(cast)
    print('현재: {} (최저: {} / 최고: {})'.format(temp,min_temp,max_temp))
    print('오전: {} / 오후: {}'.format(morning_rain_rate,afternoon_rain_rate))
    print('미세먼지: {}'.format(fine_dust))
    print('초미세먼지: {}'.format(ultrafine_dust))
    print()

def scrape_headline_news():
    print('[헤드라인 뉴스]')
    url = 'https://news.naver.com/'
    soup = create_soup(url)
    
    news_list = soup.find('ul',attrs={'class':'hdline_article_list'}).find_all('li')
 
    for index,news in enumerate(news_list):
        title = news.div.a.get_text().strip()
        link = url + news.div.a['href']
        print('{}. {}'.format(index+1,title))
        print('링크: {}'.format(link+'\n'))
    print()

def scrape_it_news():
    print('[IT 뉴스]')
    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = create_soup(url)
    
    it_news_list = soup.find('ul',attrs={'class':'type06_headline'}).find_all('li',limit=5)
 
    for index,news in enumerate(it_news_list):
        a_idx = 0
        img = news.find('dt',attrs={'class':'photo'}).find('a')
        if img :
            a_idx = 1

        title = news.find_all('a')[a_idx].get_text().strip()
        link = news.find_all('a')[a_idx]['href']

        print('{},{}'.format(index+1,title))
        print('링크: {}'.format(link+'\n'))
    print()

def scrape_english():
    print('[오늘의 영어회화]')
    url ='https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;'
    soup = create_soup(url)

    senten = soup.find_all('div',attrs={'id':re.compile('^conv_kor_t')})
    print('(영어 지문)')
    for s in senten[len(senten)//2:]:
        print(s.get_text().strip())
    
    print()

    print('(한글 지문)')
    for s in senten[:len(senten)//2]:
        print(s.get_text().strip())



if __name__ == '__main__':
    scrape_weather()
    scrape_headline_news()
    scrape_it_news()
    scrape_english()