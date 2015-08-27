import numpy
import urllib
import scipy
import random
import math
from sklearn.decomposition import PCA
from collections import defaultdict

def parseData(fname):
  for l in urllib.urlopen(fname):
    yield eval(l)

# print "Fetching dataset"
data = list(parseData("beer_50000.json"))
# data = list(parseData("non-alcoholic-beer.json"))
# print "Dataset ready", "\n"

R = [[r['review/overall'], r['review/taste'], r['review/aroma'], r['review/appearance'], r['review/palate']] for r in data] 

def mean5Dim(R):
    sums_5d = [0] * 5
    for r in R:
        for i, val in enumerate(r):
            sums_5d[i] += val
    return [x/len(R) for x in sums_5d]

mean_5d = mean5Dim(R)

print "Question 1"
print "----------\n"
print "5d mean:", mean_5d, "\n"

def reconErr(actuals, prediction):
    recon_err_list = [0] * 5
    
    for m in actuals:
        subtract = numpy.subtract(prediction, m)
        square = numpy.square(subtract)
        recon_err_list = numpy.add(square, recon_err_list)

    recon_err = 0
    for i in recon_err_list:
        recon_err += i

    return recon_err

recon_err = reconErr(R, mean_5d)

print "Question 2"
print "----------\n"
print "Reconstruction error:", recon_err, "\n"

def kMeans2Centroids(data, centroid_1, centroid_2):
    while True:
        cluster_1 = []
        cluster_2 = []

        for r in data:
            distance_1 = scipy.spatial.distance.euclidean(r, centroid_1)
            distance_2 = scipy.spatial.distance.euclidean(r, centroid_2)

            if distance_1 < distance_2:
                cluster_1.append(r)
            else:
                cluster_2.append(r)

        mean_1 = mean5Dim(cluster_1)
        mean_2 = mean5Dim(cluster_2)

        if numpy.array_equal(mean_1, centroid_1) and numpy.array_equal(mean_2, centroid_2):
            return centroid_1, centroid_2

        centroid_1 = mean_1
        centroid_2 = mean_2

centroids = kMeans2Centroids(R, [0,0,0,0,1], [0,0,0,1,0])

print "Question 3"
print "----------\n"
print "Centroid 1:", centroids[0]
print "Centroid 2:", centroids[1], "\n"

c1 = [4.17993, 4.23675, 4.14107, 4.08866, 4.12518]
c2 = [3.09862, 3.06899, 3.14020, 3.38222, 3.11332]

cluster_1 = []
cluster_2 = []

for r in R:
    distance_1 = scipy.spatial.distance.euclidean(r, c1)
    distance_2 = scipy.spatial.distance.euclidean(r, c2)

    if distance_1 < distance_2:
        cluster_1.append(r)
    else:
        cluster_2.append(r)

closer_to_c1 = len(cluster_1)
closer_to_c2 = len(cluster_2)

print "Question 5"
print "----------\n"
print "Around c1:", closer_to_c1
print "Around c2:", closer_to_c2, "\n"

recon_err_1 = reconErr(cluster_1, c1)
recon_err_2 = reconErr(cluster_2, c2)

print "Question 6"
print "----------\n"
print "Reconstruction error for c1:", recon_err_1
print "Reconstruction error for c2:", recon_err_2, "\n"
