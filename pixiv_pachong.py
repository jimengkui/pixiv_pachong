# coding：utf-8
import requests
import json
import ssl
import os
import sys
import time
import re
import urllib
import threading

ssl._create_default_https_context = ssl._create_unverified_context
def html(url,headers):


    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = response.json()
    # print(html)
    return html

def dealhtml(html,headers,start,end):

    illusts_len = len(html['body'][0]['illusts'])
    # print(illusts_len)
    path = 'pixiv图片'+str(start)+'-'+str(end)
    if not os.path.isdir(path):
        print(1)
        os.makedirs(path)
    # print(illusts_len)
    for num in range(0,illusts_len):
        img_url_1200x1200 = html['body'][0]['illusts'][num]['url']['1200x1200']
        # img_url_768x1200 = html['body'][0]['illusts'][num]['url']['768x1200']
        user_name =  html['body'][0]['illusts'][num]['user_name']
        title = html['body'][0]['illusts'][num]['illust_title']
        upload_time = html['body'][0]['illusts'][num]['illust_upload_date']
        year = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[0])
        month = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[1])
        date = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[2])
        hour = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[3])
        minute = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[4])
        second = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[5])

        Upload_time = year + '年' + month + '月' + date + '日' + hour + "时" + minute + '分' + second + "秒"
        if title=="":
            title = "无"

        # print(img_url_1200x1200)
        # print(img_url_768x1200)
        # print( Upload_time)
        # print(user_name)
        # print(title)
        suffix_arr = ['jpg', 'png', 'gif', 'webp']
        # suffix = img_url_1200x1200.split(".")[-1]


        suffix = img_url_1200x1200.split(".")[-1]

        for suffix_i in suffix_arr:
            if suffix == suffix_i:
                image = requests.get(img_url_1200x1200,headers=headers).content
                # print(image)
                try:
                    with open(sys.path[
                                  0] + '/' + path + '/' + '上传者：' + user_name + '；图片标题：' + title + '；上传时间：' + Upload_time + '；_' + str(
                            num) + '.' + suffix_i, 'wb') as f:
                        f.write(image)
                    f.close()
                except:
                    print("有异常")
                    continue

            else:
                pass
def piviv_paichong(start,end):
    # print(start)
    for num in range(start,end):
        url = "https://www.pixiv.net/ajax/showcase/article?article_id="+str(num)
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "X-DevTools-Emulate-Network-Conditions-Client-Id": "6D4F19EDC6812154A505D844653464F0",
            'Referer': url,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8"}
        # print(url)
        try:
            url = url
            html1 = html(url,headers)
            dealhtml(html1,headers,start,end)
        except:
            print("%s有异常"%num)
            continue

# piviv_paichong(1,3)


def start(start,end,step):
    arr = []
    for i in range(start, end, step):
        arr.append(i)
    print(arr)
    paichong1 = threading.Thread(target=piviv_paichong,args=(arr[0],arr[1]) )
    paichong2 = threading.Thread(target=piviv_paichong,args=(arr[1],arr[2]) )
    paichong3 = threading.Thread(target=piviv_paichong, args=(arr[2], arr[3]))
    paichong4 = threading.Thread(target=piviv_paichong, args=(arr[3], arr[4]))
    paichong5 = threading.Thread(target=piviv_paichong, args=(arr[4], arr[5]))
    paichong6 = threading.Thread(target=piviv_paichong, args=(arr[5], arr[6]))
    paichong7 = threading.Thread(target=piviv_paichong, args=(arr[6], arr[7]))
    paichong8 = threading.Thread(target=piviv_paichong, args=(arr[7], arr[8]))
    paichong9 = threading.Thread(target=piviv_paichong, args=(arr[8], arr[9]))
    paichong10 = threading.Thread(target=piviv_paichong, args=(arr[9], end))



    paichong1.start()
    paichong2.start()
    paichong3.start()
    paichong4.start()
    paichong5.start()
    paichong6.start()
    paichong7.start()
    paichong8.start()
    paichong9.start()
    paichong10.start()
    # paichong1.join()
    # paichong2.join()
    # print ("退出主线程")
start(3000,4000,100)
#
# for num in range(1,2):
#     url = "https://www.pixiv.net/ajax/showcase/article?article_id="+str(num)
#     headers = {
#         "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
#         "X-DevTools-Emulate-Network-Conditions-Client-Id": "6D4F19EDC6812154A505D844653464F0",
#         'Referer': url,
#
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Language": "zh-CN,zh;q=0.8"}
#     try:
#         url = url
#         html = html(url,headers)
#         dealhtml(html,headers,1,3)
#     except:
#         print("%s有异常"%num)