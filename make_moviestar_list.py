import os
import sys


path = "/none/sehwa/training-image-set/"
dirs = os.listdir(path)

f = open("movie_star_list.txt","w")
for d in dirs:
    nameList = d.split("_")
    movie_star_name = ""
    for n in nameList:
        movie_star_name += n + " "
    f.write(movie_star_name.rstrip()+"\n")
