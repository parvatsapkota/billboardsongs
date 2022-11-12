import urllib.request
import re
import webbrowser
import json
# import selenium.webdriver as webdriver
# from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests
import time


import smtplib

# Connect to Website and pull in data
# url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
#
# result = requests.get(url)
# # print(result.text)
#
# doc = BeautifulSoup(result.text, "html.parser")
#
#
# prices = doc.find_all(text="$")
# parent = prices[0].parent
# print(parent)
#
# strong = parent.find("strong")
# print(strong.string)


url = "https://www.billboard.com/charts/hot-100/"
result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, "html.parser")
# print(doc)


# tags = doc.find('<span class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"> Steve Lucy</span>')
# print(tags)


# tags = doc.find('h3',id = "title-of-a-story")
# creator= tags.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
# print(creator)

creator_list = []
tags = doc.find_all('h3',id = "title-of-a-story")
count = 0
for t in tags:
    dummy = t.next_sibling.next_sibling
    # print(dummy)
    # print(count)
    j = 0
    if count == 6 or (count-6) % 4 == 0:
        # print("dummy txt:",dummy.text)
        text = dummy.text
        text = text.replace("\t", "")
        text = text.replace("\n","")
        # print("text:",text)
        if count != 2:
            creator_list.append(text)
        j = 0
    j += 1
    count += 1
    if count == 406:
        break
print(creator_list)


song_list = []
num = 0
i = 0
for t in tags:

    a = t.text
    a = a.replace("\t","")
    a = a.replace("\n","")
    # print(a)
    if num > 5:
        if i == 0 or i == 4:
            song_list.append(a)
            i = 0
        i += 1
    num += 1
print(song_list)






# # print(trs) # It starts like this: ing-l-1@mobile-max"> <h3 class="c-title a-no-
# # print(trs[3]) # It starts like this: <div class="o-chart-results-list-row-container">
# # print(trs.children) # list obj has no attribute children
# bachha = list(trs[3].children) #It starts like this: ['\n', <ul class="o-chart-results-list-row. 1. Bad Habit
# print(bachha[1])


# bachha = list(trs[5].children) #It starts like this: ['\n', <ul class="o-chart-results-list-row. 2. UnHoly


# print(bachha2)
# print(bachha2[7])

# for tam in tags.find_all('ul'):
#     print(tam)






for i in range(len(song_list)):
    #Enter your keyword inside the double quotes here
    search_keyword= song_list[i]+"by"+creator_list[i]+"vevo"

    #This will replace space with + sign
    search_keyword = search_keyword.replace(" ", "+")
    print("search_keyword",search_keyword)


    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    a_website = "https://www.youtube.com/watch?v=" + video_ids[0]


    api_key="AIzaSyD6wuUNRKm2oc7hrneM5acNUvsPdpT_2l0"
    searchUrl="https://www.googleapis.com/youtube/v3/videos?id="+video_ids[0]+"&key="+api_key+"&part=contentDetails"

    with urllib.request.urlopen(searchUrl) as url:
        response = url.read()
        print(response)
    data = json.loads(response)
    all_data=data['items']
    contentDetails=all_data[0]['contentDetails']
    duration=contentDetails['duration']
    print(duration)

    #This will change the hr format to seconds format
    #PT1H56M2S
    #PT5M
    #PT1H16S
    #PT8S
    for i in range(len(duration)):
        # if duration[i] == 'H':
        #     hour = duration[i-1]
        #     minute = duration[i+1] + duration[i+2]
        #     second = duration[i+4]
        if duration[i] == 'M':
            if i == 4:
                print(4)
                total_sec = (duration[i-2]*10 + duration[i-1])* 60
                if len(duration) > 5:
                    if duration[i+2] == 'S':
                        total_sec += duration[i+1]
                    elif duration[i+3] == 'S':
                        total_sec += duration[i + 1]*10 + duration[i+2]
            if i == 3:
                print(3)
                total_sec = int((duration[i-1]))* 60
                if len(duration) > 4:
                    if duration[i+2] == 'S':
                        total_sec += int(duration[i+1])
                    elif duration[i+3] == 'S':
                        total_sec += int(duration[i + 1])*10 + int(duration[i+2])
    pausing_time = total_sec + 5

    # One option to open a browser: Improve on this so that the tab closes automatically later on
    # browser = webdriver.Chrome('C:/Drivers/chromedriver.exe')
    # browser.get(a_website)
    # browser.execute_script('document.getElementsByTagName("video_ids[0]")[0].play()')

    #Another option to open a broswer
    # webbrowser = 'windows-default'
    webbrowser.open_new(a_website)
    time.sleep(pausing_time)
