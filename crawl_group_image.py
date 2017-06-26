from icrawler.builtin import BingImageCrawler
from icrawler.builtin import GoogleImageCrawler
import os
import re


google_crawler = GoogleImageCrawler(parser_threads=10, downloader_threads=30,storage={'root_dir':'/none/sehwa/group-image-set/Angelina_Jolie'})
google_crawler.crawl(keyword="Angelina Jolie people",offset=0,max_num=1000,date_min =None,date_max=None, min_size=None, max_size=None)

'''
f = open("movie_star_list.txt", "r")

while True:
    line = f.readline()
    line = line.rstrip()
    if not line: break
    nameList = line.split(" ")

    dirName = ""
    if len(nameList) < 2:
        dirName = line
    else:
        dirName = ""
        for i in range(0,len(nameList)-1):
            dirName += nameList[i] + "_"
        dirName += nameList[len(nameList)-1]
    
    print dirName
    query = line+" people"
    google_crawler = GoogleImageCrawler(parser_threads=10, downloader_threads=30,storage={'root_dir':'/none/sehwa/group-image-set/'+dirName})
    google_crawler.crawl(keyword=query,offset=0,max_num=1000,date_min =None,date_max=None, min_size=None, max_size=None)

f.close()
'''
