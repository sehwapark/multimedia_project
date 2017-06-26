from pymongo import MongoClient
from bson import ObjectId

conn = MongoClient('localhost')
db = conn['admin']
db.authenticate('admin','dbdb916')
db = conn['multimedia']
col = db['taggedImages_c20']
resultCol = db['relationship_c20']

starList = []
f = open("movie_star_list.txt", "r")
while True:
    line = f.readline()
    line = line.rstrip()
    if not line: break
    nameList = line.split(" ")

    name = ""
    if len(nameList) < 2:
        name = line
    else:
        for i in range(0,len(nameList)-1):
            name += nameList[i] + "_"
        name += nameList[len(nameList)-1]
    starList.append(name)

starDic = {}
starIdf = {}
imgDic = {}
for star in starList:
    relationship = {}
    imgList = []
    imgDic[star] = {}
    for star2 in starList:
        relationship[star2] = {}
        relationship[star2]['frequency'] = 0
        relationship[star2]['relationship'] = 0
        relationship[star2]['imgs'] = imgList
        imgDic[star][star2] = []

    starDic[star] = relationship
    starIdf[star] = 0


count = 0
docs = col.find()
for doc in docs:
    path = ""
    tags = []
    oid = ""
    for key in doc.keys():
        if key != "_id":
            path = key
            tags = doc[key]
        else:
            oid = doc[key]

    fileName = path + tags['ext']
    fileNameList = fileName.split("/")
    starName = fileNameList[len(fileNameList)-2]
    
    if len(tags) > 1:
        for tag in tags['tags']:
            if tag != starName:
                count += 1
                starDic[starName][tag]['frequency'] += 1
                starDic[tag][starName]['frequency'] += 1
                imgDic[starName][tag].append(fileName)
                imgDic[tag][starName].append(fileName)

                starIdf[tag] += 1
                starIdf[starName] += 1
'''
for star in starDic:
    i=0
    for key in starDic[star]:
        relationshipFileName = "./relationshipImgs_c20/"+star+"_"+str(i)+".txt"
        fw = open(relationshipFileName, "w")
        for img in imgDic[star][key]:
            fw.write(star+" "+key+" "+img+"\n")
        starDic[star][key]['imgs'] = relationshipFileName
        i += 1
'''

for star in starDic:
    i=0
    for key in starDic[star].keys():
        relationshipFileName = "/home/sehwa/multimedia/relationshipImgs_c20/"+star+"_"+str(i)+".txt"
        fw = open(relationshipFileName, "w")
        starDic[star][key]['relationship'] = float(starDic[star][key]['frequency'])/starIdf[key]
        for img in imgDic[star][key]:
#        for img in starDic[star][key]['imgs']:
            fw.write(img+"\n")
        fw.close()
        starDic[star][key]['imgs'] = relationshipFileName
        i += 1


for star in starDic:
    doc = {}
    doc['_id'] = ObjectId()
    doc['star'] = star
    doc['relationship'] = starDic[star]
    resultCol.insert(doc)

#print "Brad Pitt ", starDic["Brad_Pitt"].keys()

#starDic[]
