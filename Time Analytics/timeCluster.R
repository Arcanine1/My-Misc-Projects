#PURPOSE: Creates Clusters

pacman::p_load(dendextend)

#defines numbers of clusters
num <- 5

#gets data
source("importFUNCTION.R")
time<- importAndCleanData()

#Creates cluster
distance_time <- dist(time, method = "manhattan")
hclust_time <- hclust(distance_time)

#makes output look good
dendo <- as.dendrogram(hclust_time)
hang.dendrogram(dendo)
dendo <- color_branches(dendo, k=num)
dendo <- color_labels(dendo,k=num)

#graphs
plot(dendo)
rect.dendrogram(dendo,k=num)