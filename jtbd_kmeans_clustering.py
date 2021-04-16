#Author: Ada D'arcy
#Date: 16th April 2021
#Comment: Python is so so easy to use so please even if you dont have programming knowlege try to follow the instructions in the URLs below to get it running.

#First we import libraries that do all the heavy lifting. If you don't have them installed, follow instructions in links below:
import pandas as pd #install this https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
import matplotlib.pyplot as plt #install this https://matplotlib.org/stable/users/installing.html
from sklearn.cluster import KMeans #install this https://scikit-learn.org/stable/install.html

#open file and select columns with JTBD questions for model features
training = pd.read_csv("jtbd_survey.csv")
jtbd_needs_only = training.iloc[:,49:96] #col 49->96 had our JTBD outcome statements.. others were profiling questions

#understand how many clusters by trying 5 and seeing which has lowest sum of mean square error from k centroids
distortions = [] #A list to store the distortion from each cluster we try
K_to_try = range(1, 6) #A range of cluster sizes to try.. edit to try more

#loop K times and run KMeans for each K clusters
for i in K_to_try:
    model = KMeans(
        n_clusters=i,
        init='k-means++',
        n_jobs=-1,
        random_state=1).fit(jtbd_needs_only)
    distortions.append(model.inertia_)
#Show a chart to demostrate the distortions found at each cluster. You only want a few clusters but you want to minimise noise so picking the 'elbow' in the line chart works pretty nicely
plt.plot(K_to_try, distortions, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Distortions')
plt.title('How many clusters should we use (elbow)?')
plt.show()

#Now run KMeans with the right cluster number of 3
result = KMeans(
    n_clusters=3,
    init='k-means++',
    n_jobs=-1,
    random_state=1)
result.fit(jtbd_needs_only).predict(jtbd_needs_only)

#make file to store clustering
result = pd.concat([training, pd.DataFrame(result, columns=['Cluster'])], axis=1) #concat this column to the matrix
result.to_csv('clustered_survey.csv')