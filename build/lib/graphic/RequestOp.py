import requests

# get模拟浏览器访问网页
resp = requests.get("https://www.baidu.com")
print(resp.text)
print(resp.status_code) #200代表返回成功



# request是python的第三方http网络请求库,外号http库。
# 作用:用代码模拟浏览器,去访问网页、调用接口,拿到服务器返回的数据
# 1. 爬取网页html、图片、接口数据
# 2.接口自动化测试：调用后端api
# 3.后端服务之间相互调用



