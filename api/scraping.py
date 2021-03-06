from bs4 import BeautifulSoup
import urllib.request
import time
import re
from api.models import animedb
from datetime import datetime
#start = time.time()

def scrapingreq(year,page,season):
  #try:
    animedb.objects.filter(year=str(year),season=str(season),page=str(page)).delete()

    anititle = []
    link =[]
    title_jp = []
    status = []
    #monthday = ["月","火","水","木","金","土","日"]


    ajaurl = []

    url = 'https://9anime.to/filter?language=subbed&release[]=' + str(year)+ '&season[]='+ str(season) + '&page=' + str(page)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")


    for tit in soup.find_all(class_="name"):
        anititle.append(tit.text)
        link.append(tit['href'])

    for aja in soup.find_all(class_="poster"):
        ajaurl.append('https://9anime.to/'+aja['data-tip'])


    for i in range(len(ajaurl)):
        url = ajaurl[i]
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        pre = []
        truetitle = ''

        for tit in soup.find_all("div",class_='meta'):
            for spa in tit.find_all("span"):
                pre.append(spa.text)

        pre2 = pre[4].replace("\n","")

        status.append(pre[1])

        title = re.sub('\s{2}',"",pre2).split("; ")
        if len(title)>=2:
            if int(len(title[len(title)-1]))>=50:
                for tit in soup.find_all(class_="title"):
                    tt = tit.text
                truetitle = re.sub('(\s2.+$)','',tt)
                title_jp.append(truetitle)
            else:
                title_jp.append(title[len(title)-1])

        else:
            if int(len(title[0]))>=50:
                for tit in soup.find_all(class_="title"):
                    tt = tit.text
                truetitle = re.sub('(\s2.+$)','',tt)
                title_jp.append(truetitle)
            else:
                title_jp.append(title[0])
        time.sleep(0.1)



    for i in range(len(anititle)):
        tit = anititle[i]
        lin = link[i]
        titj = title_jp[i]
        sta = status[i]
        sea = str(season)
        pg = str(page)
        yr = str(year)
        wd = '--'
        if len(tit)>500:
            continue

        db = animedb(title=tit,title_jp=titj,year=yr,season=sea,weekday=wd,status=sta,url=lin,page=pg)
        db.save()

    return 'done'

  #except:
   #   return 'error'