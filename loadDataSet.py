def loadDataSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        dataMat.append([int(curLine[0]),int(curLine[1])])
        # fltLine = map(float,curLine)
        # dataMat.append(fltLine)
    return dataMat


def loadDataSet2(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        dataMat.append(int(curLine[0]))
        # fltLine = map(float,curLine)
        # dataMat.append(fltLine)
    return dataMat