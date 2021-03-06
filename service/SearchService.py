import ssl
import urllib
import json
from model.BlogPage import BlogPage

client_id = "client_id"
client_secret = "client_secret"


def searchBlog(search_word):
    display = "7"
    context = ssl._create_unverified_context()
    encText = urllib.parse.quote(search_word)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=" + display + "&start=" + "11"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, context=context)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        json_data = json.loads(response_body.decode('utf-8'))

        # blog는 title, link를 담는 이차원 배열
        blogPageArray = []
        k = 0
        for i in json_data['items']:
            #네이버 블로그만 필터
            if('naver' in i['link']):
                # blog 라는 2차원 배열 초기화
                blogPageArray.append(BlogPage())
                # link
                blogId = i['link'].replace("https://blog.naver.com/", '').replace('?', '').replace("Redirect=Log", '')
                blogPageArray[k].setPageUrl("https://blog.naver.com/PostView.nhn?blogId=" + blogId)
                # title
                blogPageArray[k].setTitle(i['title'])
                k = k + 1

    else:
        print("Error Code:" + rescode)

    return blogPageArray


def dataCrawling(postArray):
    k = 0
    blogPageArray = []
    for url in postArray:
        blogPageArray.append(BlogPage())
        split = url.split('/', 5)
        blogPageArray[k].setPageUrl("https://blog.naver.com/PostView.nhn?blogId=" + split[-2] + "&logNo=" + split[-1])
        k = k + 1

    return blogPageArray