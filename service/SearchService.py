import ssl
import urllib
import json
from model.BlogPage import BlogPage

def dataCrawling(postArray):
    k = 0
    blogPageArray = []
    for url in postArray:
        blogPageArray.append(BlogPage())
        split = url.split('/', 5)
        blogPageArray[k].setPageUrl("https://blog.naver.com/PostView.nhn?blogId=" + split[-2] + "&logNo=" + split[-1])
        k = k + 1

    return blogPageArray