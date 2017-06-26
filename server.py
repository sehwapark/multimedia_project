import sys

sys.path.insert(0,'/home/sehwa/multimedia/openface/demos/')

import multimedia
import json


returnList = multimedia.getImages()

#for ret in returnList:
#    print ret
#    print returnList[ret].keys()
#    print returnList[ret]
print json.dumps(returnList)
