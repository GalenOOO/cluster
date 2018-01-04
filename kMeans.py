import sys
reload(sys)
sys.setdefaultencoding('utf8')
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

def loadDataSet(filename):
	dataMat = []
	fr = open(filename)
	for line in fr.readlines():
		curLine = line.strip().split(' ')
		dataMat.append([int(curLine[0]),int(curLine[1])])
		# fltLine = map(float,curLine)
		# dataMat.append(fltLine)
	return dataMat

def distEclud(vecA,vecB):
	return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet, k):
	n = shape(dataSet)[1]
	centroids = mat(zeros((k,n)))
	for j in range(n):
		minJ = min(dataSet[:,j])
		rangeJ = float(max(dataSet[:,j]) - minJ)
		centroids[:,j] = minJ + rangeJ * random.rand(k,1)
	return centroids

def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
	m = shape(dataSet)[0]
	clusterAssment = mat(zeros((m,2)))
	centroids = createCent(dataSet,k)
	clusterChanged = True
	count = 0
	while clusterChanged and count < 10 :
		clusterChanged = False
		for i in range(m):
			minDist = inf; minIndex = -1
			for j in range(k):
				distJI = distMeas(centroids[j,:],dataSet[i,:])
				if distJI < minDist:
					minDist = distJI; minIndex = j 
			if clusterAssment[i,0] != minIndex: clusterChanged = True
			clusterAssment[i,:] = minIndex,minDist**2
		# print centroids
		for cent in range(k):
			ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
			centroids[cent,:] = mean(ptsInClust,axis = 0)
		count += 1
		print count
	return centroids,clusterAssment

def plotDot(dataSet,clusterAssment):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	xcord0 = []; ycord0 = []; xcord1 = []; ycord1 = []
	m = shape(dataSet)[0]
	for i in range(m):
		if clusterAssment[i][0] == 0 :
			xcord0.append(dataSet[i][0]); ycord0.append(dataSet[i][1])
		else:
			xcord1.append(dataSet[i][0]); ycord1.append(dataSet[i][1])
	ax.scatter(xcord0,ycord0, marker='o', c='g' )
	ax.scatter(xcord1,ycord1, marker='*', c='deeppink')
	ax.axis([-10,300,-10,600])
	plt.title('Cluster')
	plt.show()

def homework():
	dataArr = loadDataSet('julei1.txt')
	cen,clu = kMeans(mat(dataArr),2)
	plotDot(dataArr,array(clu))

# def homework2():
# 	dataArr = loadDataSet('julei2.txt')
# 	cen,clu = kMeans(mat(dataArr),7)
# 	plotDot(dataArr,array(clu))






