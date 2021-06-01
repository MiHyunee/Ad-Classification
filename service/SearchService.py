import ssl
import urllib
import json

#client_id = "client_id"
#client_secret = "client_secret"

client_id = "_SdymsLP_TCuIfpjPuz7"
client_secret = "mImtapr7Mh"

def searchBlog(search_word):
    display = "10"
    context = ssl._create_unverified_context()
    encText = urllib.parse.quote(search_word)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=" + display
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, context=context)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        json_data = json.loads(response_body.decode('utf-8'))

        # blog 라는 2차원 배열 초기화
        blog = []
        for i in range(int(display)):
            blog.append([0, 0])

        # blog는 title, link를 담는 이차원 배열
        k = 0
        for i in json_data['items']:
            blog[k][0] = i['title']
            blog[k][1] = i['link']
            k = k + 1

        print(blog)

    else:
        print("Error Code:" + rescode)

    return blog