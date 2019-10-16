import numpy


def readtrackfile(filename):
    dataDir = './627projectfile/'
    file_track = dataDir + filename
    ftrackItem = open(file_track, 'r')

    dictrack = {}

    for line in ftrackItem:
        arr_track = line.strip().split('|')
        userID = arr_track[0]
        otherID=arr_track[1:]
        key, value=userID,otherID
        dictrack[key]=value
    return dictrack





    ftrackItem.close()
track = readtrackfile('trackData2.txt')
print (track.get("270572"))