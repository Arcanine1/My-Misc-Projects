pacman::p_load(dendextend)
source("CleanUpFUNCTION.R")

#defines numbers of clusters
num <- 5

#gets data
time <- read.csv("~/Desktop/Time.csv", row.names = 1)

#merges data
time <- CleanUp(time)

#converts to dist
distance_time <- dist(time, method = "manhattan")

#creates cluster
hclust_time <- hclust(distance_time)

#converts to dendogran
dendo <- as.dendrogram(hclust_time)

#makes look good
hang.dendrogram(dendo)
dendo <- color_branches(dendo, k=num)
dendo <- color_labels(dendo,k=num)

#graphs
plot(dendo)
rect.dendrogram(dendo,k=num)