#Author: Ada D'arcy
#Date: 16th April 2021
#Comment: Python is so easy to use so please even if you dont have programming knowlege try to follow the instructions in the URLs below to get it running.

#First we import libraries that do all the heavy lifting. If you don't have them installed, follow instructions in links below:
import pandas as pd #install this https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
import matplotlib.pyplot as plt #install this https://matplotlib.org/stable/users/installing.html
from sklearn.cluster import KMeans #install this https://scikit-learn.org/stable/install.html
from sklearn.decomposition import PCA

#open file and select columns with JTBD questions for model features
training = pd.read_csv("jtbd_survey.csv")
jtbd_needs_only = training.iloc[:,49:96] #col 49->96 had our JTBD outcome statements.. others were profiling questions
print(jtbd_needs_only.head(5)); #Have a quick look to ensure we got the right columns to cluster
#understand how many clusters by trying 5 and seeing which has lowest sum of mean square error from k centroids
distortions = [] #A list to store the distortion from each cluster we try
K_to_try = range(1, 6) #A range of cluster sizes to try.. edit to try more

#loop K times and run KMeans for each K clusters
for i in K_to_try:
    model = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=1).fit(jtbd_needs_only)
    distortions.append(model.inertia_)
    
#Show a quick chart to demostrate the distortions found at each cluster. You only want a few clusters but you want to minimise noise so picking the 'elbow' in the line chart works pretty nicely
plt.plot(K_to_try, distortions, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Distortions')
plt.title('How many clusters should we use (elbow)?')
plt.show()

#Now run KMeans with the right cluster number of 3
result = KMeans(
    n_clusters=3,
    init='k-means++',
    random_state=1)
result.fit(jtbd_needs_only)
result=result.predict(jtbd_needs_only)

#Reduce to 2 dimensions so we can visuallise in 2D
pca = PCA(n_components = 2, random_state=1)
X_pca = pca.fit_transform(jtbd_needs_only)
print('Explained variance ratio : ' + str(pca.explained_variance_ratio_.cumsum()[1]))

#use the best K from elbow method (pick the number where the biggest angle/elbow in the line chart was)
model = KMeans(
    n_clusters=3,
    init='k-means++',
    random_state=1)
model.fit(X_pca)
y=model.predict(X_pca)

plt.scatter(X_pca[y == 0, 0], X_pca[y == 0, 1], s = 50, c = 'yellow', label = 'Cluster 1')
plt.scatter(X_pca[y == 1, 0], X_pca[y == 1, 1], s = 50, c = 'green', label = 'Cluster 2')
plt.scatter(X_pca[y == 2, 0], X_pca[y == 2, 1], s = 50, c = 'red', label = 'Cluster 3')
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s = 100, c = 'blue', label = 'Centroids')
plt.title('Clusters of Respondants by shared needs')
plt.xlabel('Pricnple Component 1')
plt.ylabel('Pricnple Component 2')
plt.legend()
plt.grid()
plt.show()

#make file to store clustering
result = pd.concat([training, pd.DataFrame(result, columns=['Cluster'])], axis=1) #concat this column to the matrix
result["Cluster"] = result["Cluster"] + 1
result.to_csv('clustered_survey.csv')
print("Clustering complete, check directory for new file 'clustered_survey.csv' which contains a new column called 'Cluster' at far right")
