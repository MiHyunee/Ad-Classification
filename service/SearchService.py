import ssl
import urllib
import json

client_id = "client_id"
client_secret = "client_secret"

def searchBlog(search_word):
    display = "100"
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
            #redirection 걸려있는 링크로 하면 body가 iframe으로 대체되서 내용 다 안나
            # iframe의 src 보니까 아래처럼 바꾸면 될것같음
            blogId = i['link'].replace("https://blog.naver.com/", '').replace('?', '').replace("Redirect=Log", '')
            blog[k][1] = "https://blog.naver.com/PostView.nhn?blogId=" + blogId
            k = k + 1

        print(blog)

    else:
        print("Error Code:" + rescode)

    return blog